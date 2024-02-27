import __main__
import requests, json

class downloadData:
    def get(source, minAbuseScore = 2500):
        body = """
        {
            instances: fedinodes(where: {abuse_score: {_gte: """ + str(minAbuseScore) + """}}, order_by: {domain: asc}) {
                domain
                service_domain
                abuse_score
            }
        }
        """

        response = requests.post(url=source, json={"query": body})
        if response.status_code == 200:
            return response.content.decode()