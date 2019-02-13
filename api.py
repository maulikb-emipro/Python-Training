from woocommerce import API

wcapi = API(
    url="http://localhost",
    consumer_key="ck_04ab269a4018329da12eb99054ffa32531d45bbf",
    consumer_secret="cs_dcee6139173e130d44f5b5c3443755f626624040",
    wp_api=True,
    version="wc/v3"
    )

print(wcapi.get("products/13").json())
