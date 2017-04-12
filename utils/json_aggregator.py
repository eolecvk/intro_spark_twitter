
import csv


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






def json_to_csv(dirpath, tsvpath):
    """
    inputs:
        + dirpath : full path of dir that contains the tweets .json file
        + csvpath : full path of output tsv file
    Compiles a collection of tweets as a tsv file.
    The tweet fields that are kept include: `user_id`, `tweet_id`, and `tweet_text`
    """

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
            text = tweet['text'].replace('\n',' ').replace('\t',' ')

            new_record = (tweet_id, user_id, text)
            result.append(new_record)

        except Exception as e:
            print(e)
            print("Issue with file: [{}]".format(fpath))

    # Save output to .tsv file
    with open(tsvpath, 'w') as fp:
        wr = csv.writer(fp, delimiter='\t')
        wr.writerows(result)

    # Print log
    records_tsv = []
    tweet_ids_tsv = []
    user_ids_tsv = []

    with open(tsvpath, 'r') as fp:
        rd = csv.reader(fp, delimiter='\t')

        for record in rd:
            records_tsv.append(record)
            tweet_ids_tsv.append(record[0])
            user_ids_tsv.append(record[1])

    count_records_tsv = len(records_tsv)
    count_distinct_tweet_ids_tsv = len(set(tweet_ids_tsv))
    count_distinct_user_ids_tsv = len(set(user_ids_tsv))

    print("IN TSV:")
    print(count_records_tsv, count_distinct_tweet_ids_tsv, count_distinct_user_ids_tsv)

    count_records_actual = len(result)
    count_distinct_tweet_ids_actual = len(set([record[0] for record in result]))
    count_distinct_user_ids_actual = len(set([record[1] for record in result]))

    print("ACTUAL:")
    print(count_records_actual, count_distinct_tweet_ids_actual, count_distinct_user_ids_actual)


if __name__ == "__main__":

    dirpath = "/home/eolus/Documents/poc_data/tweets"
    tsvpath = "/home/eolus/Desktop/tweets.tsv"

    #json_to_csv(dirpath, tsvpath)

    jsonfiles_to_json(dirpath, "/home/eolus/Desktop/tweets.json")