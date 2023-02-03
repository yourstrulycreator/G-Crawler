from googleapiclient.discovery import build
import json
import pandas as pd

gsearch = []

search_term = input("Enter your keyword: ")

page = input("What page do you want crawl? Hint: first, second, tenth: ")

if page == "first":
    i = 0
elif page == "second":
    i = 1
elif page == "third":
    i = 2
elif page == "fourth":
    i = 3
elif page == "fifth":
    i = 4
elif page == "sixth":
    i = 5
elif page == "seventh":
    i = 6
elif page == "eigth":
    i = 7
elif page == "ninth":
    i = 8
elif page == "tenth":
    i = 9
else:
    i = 0


def google_search(search_term: str, api_key: str, cse_id: str, **kwargs) -> json:
    """Perform a Google search using Custom Search API"""
    # Build request
    service = build("customsearch", "v1", developerKey=api_key)
    # Execute request
    # i = 1
    query_result = (
        service.cse()
        .list(q=search_term, cx=cse_id, start=str(i) + "1", **kwargs)
        .execute()
    )
    return query_result


# Initialize search parameters
my_api_key = ""
my_cse_id = ""
num_search_results = 10

# Execute search
query_result = google_search(search_term, my_api_key, my_cse_id, num=num_search_results)

# Print result
print(query_result)

# Store result 1
# with open('output_data.txt', 'w') as output_file:
#    json.dump(query_result, output_file)


# Store result 2
for item in query_result["items"]:

    title = item["title"]

    link = item["link"]

    description = item["snippet"]

    element_info = {"title": title, "link": link, "description": description}

    gsearch.append(element_info)

# print(len(cbdsearch))

df = pd.DataFrame(gsearch)

# print(df)

fn = "crawl_data_set_{0}.csv".format(str(i))
df.to_csv("gcrawl_data_set_{0}.csv".format(str(i)))
