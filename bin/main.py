import sys
from fetch import downloadData
from blacklist import blacklist

def main():
    try:
        tier0 = downloadData.get('https://gql.api.bka.li/v1/graphql', 2000)
        blacklist.create(tier0)

        tier1 = downloadData.get('https://gql.api.bka.li/v1/graphql', 1500)
        blacklist.create(tier1, 1)

        tier2 = downloadData.get('https://gql.api.bka.li/v1/graphql', 1000)
        blacklist.create(tier2, 2)

    except ValueError as ve:
        return str(ve)

if __name__ == "__main__":
    sys.exit(main())