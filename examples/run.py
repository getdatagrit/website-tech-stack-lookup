# pip install apify-client
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagrit/website-tech-stack-lookup").call(run_input={
    "domains": [
        "shopify.com",
        "wordpress.org",
        "hubspot.com",
        "stripe.com",
        "vercel.com",
        "bbc.co.uk",
        "allbirds.com",
        "techcrunch.com",
        "webflow.com",
        "joomla.org",
        "github.com",
        "apify.com"
    ]
})
items = client.dataset(run["defaultDatasetId"]).list_items().items
print(len(items), "records")
print(items[0] if items else None)
