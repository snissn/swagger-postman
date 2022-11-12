import json
import os
from pprint import pprint
import sys
import testdata

from torch import prepare_multiprocessing_environment
data = json.load(open("posty.json"))
swagger_data = json.load(open("swagger.json"))

def iterate_rules(rules):
    if type(rules) == type([]):
        for rule in rules:
            iterate_rules(rule)
    if type(rules) == type({}):
        if rules.get("item"):
            iterate_rules(rules["item"])
        else:
            process_rule(rules)


def read_swagger(rule):
    #pprint(rule)
    paths = []
    for item in rule['request']['url']['path']:
        if item.startswith(":"):
            paths.append("{" + item[1:] + "}")
        else:
            paths.append(item)

    path = "/" + "/".join(paths)
    method = rule["request"].get("method").lower()
    return swagger_data['paths'][path][method]

def handle_query(query, swagger):
    key = query['key']
    if key == "body":
        print(swagger)
        assert 0 == 1
    else:
        query['value'] = testdata.data[key]
    #print(query)
    #assert 0 == 1
def handle_variable(query):
    query['value'] = testdata.data[query['key']]
    #print(variable)
    #assert 0 == 1
def handle_form(post_body, swagger):
    for item in post_body:
        handle_query(item, swagger)
    #print("handle_form",post_body) 
    #assert 0 == 1
def handle_json(rule):
    post_body =rule.get('request')
    swagger = read_swagger(rule)
    for parameter in swagger['parameters']:
        if parameter.get("in") == "body":
            if parameter.get("name") == "body":
                key = parameter['schema'].get('$ref', 'body')
                post_body['body']['raw'] = json.dumps(testdata.data[key])
            else:
                post_body['body']['raw'] = json.dumps(testdata.data[ parameter.get("name")])


def process_rule(rule):


#    swagger = read_swagger(rule)
    rule['event'] = [
                {
                    "listen": "test",
                    "script": {
                        "type": "text/javascript",
                        "exec": [
                            "tests[\"Status code is 200\"] = (responseCode.code >= 200 && responseCode.code < 300);"
                        ]
                    }
                }
            ]
    #pprint.pprint(rule)
    swagger = read_swagger(rule)
    queries = rule.get("request").get("url",{}).get("query",[])
    for query in queries:
        handle_query(query, swagger)
        #print(1,query["key"])
        pass

    variables = rule.get("request").get("url",{}).get("variable",[])
    for variable in variables:
        handle_variable(variable)
        pass
        #print(3,variable["key"])

    post_body = rule.get('request').get("body",{}).get("urlencoded")
    if post_body:
        handle_form(post_body, swagger)
        pass
        #print(2,post_body)

    post_body = rule.get('request').get("body",{}).get("raw")
    if post_body:
        #pprint(rule)
        handle_json(rule)
        pass
        #print(2,post_body)


    for index, urlpart in enumerate(rule['request']['url']['path']):
        if urlpart.startswith(":"):
            rule['request']['url']['path'][index] = testdata.data[urlpart[1:]]



def main():
    BASEURL = "http://localhost:3004"
    APIKEY =  os.environ['APIKEY']
    variables = data['variable']
    for variable in variables:
        if variable.get("key") == "baseUrl":
            variable["value"] = BASEURL
    apikey = data['auth']['apikey']
    for item in apikey:
        if item['key'] == "value":
            item['value'] = "Bearer " + APIKEY


    rules = data['item']
    iterate_rules(rules)
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
