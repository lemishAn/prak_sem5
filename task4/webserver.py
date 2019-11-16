from http.server import HTTPServer, BaseHTTPRequestHandler
from collections import Counter
import pickle
from pycorenlp import StanfordCoreNLP
import threading

def tmp(line):
    if line[8] == '':
        return 0
    else:
        return int(line[8])    

def retweet_top10(lst): # most common tweet
    return (reversed(sorted(lst,key = tmp)))

def tmp2(line):
    if not line[14].isdigit():
        return 0
    else:
        return int(line[14])    


def author_top10 (lst):
    followers = list(reversed(sorted(lst, key=tmp2)))[:10]
    follower = []
    j = 0
    for i in followers:
        follower.append([])
        follower[j].append(i[4])
        follower[j].append(i[14])
        j += 1
    return follower


def tweet_top10 (lst): # 10 most common words
    tweet = list()
    for i in lst:
        tweet.extend(i[6].split())
    tweet_top = Counter(tweet)
    tmp = tweet_top.most_common(10)
    tmp2 = []
    for i in range(len(tmp)):
        tmp2.append([])
        tmp2[i].append(tmp[i][0])
        tmp2[i].append(tmp[i][1])
    return tmp2

def country(lst):
    country_tweet = set()
    country_retweet = set()
    for i in lst:
        if i[11] != '':
            if i[6][:2] == "RT":
                country_retweet.add(i[11])
            else:
                country_tweet.add(i[11])
    return list(country_tweet), list(country_retweet)

def stat(data):
    if len(data) < 10:
        error = 'Not enough data'
        print(error)
    else:
        tweet_top = tweet_top10(data)
        retweet_top = (list(retweet_top10(data)))[:10]
        retweet_top10_necessary = []
        for i in range(len(retweet_top)):
            retweet_top10_necessary.append([])
            retweet_top10_necessary[i].append(retweet_top[i][6])
            retweet_top10_necessary[i].append(retweet_top[i][3])
            retweet_top10_necessary[i].append(retweet_top[i][8])
        author_top = author_top10(data)
        country_tweet, country_retweet = country(data)
        # print(tweet_top)
        # print(retweet_top10_necessary)
        # print(author_top)
        data_for_client = [['Popular words', 'Number of words']]
        data_for_client.extend(tweet_top)
        data_for_client.extend([])
        data_for_client.extend([['Tweet content', 'author', 'RT']])
        data_for_client.extend(retweet_top10_necessary)
        data_for_client.extend([['author', 'followers']])
        data_for_client.extend(author_top)
        data_for_client.extend([['country_tweet'], country_tweet])
        data_for_client.extend([['country_retweet'], country_retweet])
        message = pickle.dumps(data_for_client)
        return message

def process_stat(post_data):
    data = pickle.loads(post_data)
    res = stat(data)
    return res

def process_enti(post_data):
    data = pickle.loads(post_data)
    nlp = StanfordCoreNLP('http://localhost:9000')
    pos = []
    for i in data:
        text = i[6].replace('\n',' ')
        # print(i[6])
        result = nlp.annotate( text, properties = {'annotators': 'ner', 'outputFormat': 'json', 'timeout': 100000, })
        # print(result["sentences"][0])
        for word in result["sentences"][0]["tokens"]:
            pos.append('{} ({})'.format(word["word"], word["ner"]))
            # print(pos)
            # print('')
            # print(text)
    string = " ".join(pos)
    # print(pos)
    message = pickle.dumps(string)
    return message

class RequestHeandler1(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "multipart/form-data")
        self.end_headers()

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._html("hi!"))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        res = process_stat(post_data)
        self._set_headers()
        self.wfile.write(res)
        

class RequestHeandler2(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "multipart/form-data")
        self.end_headers()

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._html("hi!"))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        res = process_enti(post_data)
        self._set_headers()
        self.wfile.write(res)

        

def run1(server_class=HTTPServer, handler_class=RequestHeandler1, addr="127.11.0.1", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()

def run2(server_class=HTTPServer, handler_class=RequestHeandler2, addr="127.11.0.1", port=8001):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()

th1 = threading.Thread(target=run1)
th2 = threading.Thread(target=run2)
th1.start()
th2.start()


