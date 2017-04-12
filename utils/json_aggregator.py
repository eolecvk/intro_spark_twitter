


def jsonfiles_to_json(indir_path, outfile_path):
    """
    Group a collection of json objects in individividual files into a single json file,
    one line per json object
    cf https://docs.databricks.com/spark/latest/data-sources/read-json.html
    """
    import os
    import simplejson as json

    # Generate list of tweet file full paths
    fpaths = [os.path.join(indir_path, fname) for fname in os.listdir(indir_path)]

    # Define list of tweets to write in output file
    result = []

    # Open each tweet file and get relevant fields
    for fpath in fpaths:

        try:
            with open(fpath, 'r') as fp:
                tweet = json.load(fp)

            tweet_id = tweet['id']
            user_id = tweet['user']['id']
            text = (tweet['text']
                .replace('\n',' ')
                .replace('\t',' ')
                .replace('\r',' ')
                .replace('"',' '))

            new_record = {
                "tweet_id" : tweet_id,
                "user_id" : user_id,
                "text" : text
                }

            new_record_str = json.dumps(new_record, separators=(',', ':'))

            result.append(new_record_str)

        except Exception as e:
            print(e)
            continue

    # Write list of json objects to file (one obj per line)
    with open(outfile_path, 'w') as fp:
        for line in result:
            fp.write(line + '\n')






def jsonfiles_to_csv(dirpath, tsvpath):
    """
    inputs:
        + dirpath : full path of dir that contains the tweets .json file
        + csvpath : full path of output tsv file
    Compiles a collection of tweets as a tsv file.
    The tweet fields that are kept include: `user_id`, `tweet_id`, and `tweet_text`
    """
    import os
    import csv

    # Generate list of tweet file full paths
    fpaths = [os.path.join(dirpath, fname) for fname in os.listdir(dirpath)]

    # Define result list (to be written to output file)
    result = []

    # Open each tweet file and get relevant fields
    for fpath in fpaths:

        try:
            with open(fpath, 'r') as fp:
                tweet = json.load(fp)

            tweet_id = tweet['id']
            user_id = tweet['user']['id']
            text = (tweet['text']
                .replace('\n',' ')
                .replace('\t',' ')
                .replace('\r',' ')
                .replace('"',' '))

            new_record = (tweet_id, user_id, text)
            result.append(new_record)

        except Exception as e:
            print(e)
            print("Issue with file: [{}]".format(fpath))

    # Save output to .tsv file
    with open(tsvpath, 'w') as fp:
        wr = csv.writer(fp, delimiter='\t')
        wr.writerows(result)

# -----------------------------------------------------------------------


if __name__ == "__main__":

    dirpath = "FULL/PATH/TO/INPUT/TWEET/DIR"
    outpath = "FULL/PATH/TO/OUTPUT/JSON/FILE"

    jsonfiles_to_json(dirpath, outpath)