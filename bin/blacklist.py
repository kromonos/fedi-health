import __main__
import json, csv

class blacklist:
    def create(jsonData, tier = 0):
        header = ['domain', 'severity', 'reject_media', 'reject_reports', 'public_comment', 'obfuscate']
        data = json.loads(jsonData);

        with open('../_unified_tier' + str(tier) + '_blocklist.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(header)

            for domain in data['data']['instances']:
                data = [
                    domain['domain'],
                    'suspend',
                    'False',
                    'False',
                    '',
                    'False'
                ]
                writer.writerow(data)