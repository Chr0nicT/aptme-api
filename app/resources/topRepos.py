from flask_restful import Resource
import json

class TopRepos(Resource):
    def get(self):
        top = {}
        with open('app/db/link_count.json', 'r+') as json_file:
            data = json.load(json_file)
            sortdict = [(k, data[k]) for k in sorted(data, key=data.get, reverse=True)]
            for k, v in sortdict:
                if len(k) >= 12:
                    if "hackyouriphone" not in k:
                        if "kiiimo" not in k:
                            if "xarold" not in k:
                                if "pulandres" not in k:
                                    if "https://cool" != k:
                                        top.update({k,v})
        return top