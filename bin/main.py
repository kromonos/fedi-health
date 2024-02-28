import sys
from fetch import downloadData
from blacklist import blacklist

def main():
    baseUrl = 'https://gql.api.bka.li/api/rest/fediabuse/'

    try:
        tier0 = downloadData.get(baseUrl + '2000')
        blacklist.create(tier0)

        tier1 = downloadData.get(baseUrl + '1500')
        blacklist.create(tier1, 1)

        tier2 = downloadData.get(baseUrl + '1000')
        blacklist.create(tier2, 2)

        tier3 = downloadData.get(baseUrl + '750')
        blacklist.create(tier3, 3)

    except ValueError as ve:
        return str(ve)

if __name__ == "__main__":
    sys.exit(main())