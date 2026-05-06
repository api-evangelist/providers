---
aid: campbell-soup
name: Campbell Soup
url: https://raw.githubusercontent.com/api-evangelist/campbell-soup/refs/heads/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
tags:
  - Food
  - Consumer Packaged Goods
  - Recipes
  - Brands
access: 3rd-Party
created: '2026-03-23'
modified: '2026-04-23'
position: Provider
specificationVersion: '0.19'
description: Campbell Soup Company (now rebranded as The Campbell's Company) is a manufacturer and marketer of high-quality branded convenience food products, including soups, simple meals, beverages, snacks, and packaged fresh foods under brands such as Campbell's, Swanson, Pace, Prego, V8, Pepperidge Farm, Goldfish, and Snyder's of Hanover. Historically Campbell's ran a public Campbell's Kitchen Developer API exposing recipes, products, UPC lookup, and nutrition data for web and mobile integrations, though current availability of the public developer portal varies and typically requires partner access.
apis:
  - aid: campbell-soup:campbells-kitchen-api
    name: Campbell's Kitchen API
    description: The Campbell's Kitchen API exposes the Campbell's Kitchen recipe and product catalog — including thousands of recipes across Campbell's, Swanson, Pace, Prego, and Pepperidge Farm brands — to developers building search-based recipe and product applications. The API supports search by key ingredients, product UPC, and keywords, and returns recipe details, photos, ratings, and updated Nutrition Facts panel data.
    humanURL: https://developer.campbellskitchen.com/
    tags:
      - Recipes
      - Nutrition
      - Products
      - UPC
    properties:
      - type: Documentation
        url: https://developer.campbellskitchen.com/documentation/api-overview
      - type: DeveloperPortal
        url: https://developer.campbellskitchen.com/
common:
  - type: Website
    url: https://www.thecampbellscompany.com/
  - type: ConsumerSite
    url: https://www.campbells.com/
  - type: Recipes
    url: https://www.campbells.com/recipes/
  - type: Products
    url: https://www.campbells.com/products/
  - type: DeveloperPortal
    url: https://developer.campbellskitchen.com/
  - type: PressRoom
    url: https://www.thecampbellscompany.com/newsroom/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
