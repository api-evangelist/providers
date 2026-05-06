---
aid: datafiniti
name: Datafiniti
description: Datafiniti is a Data as a Service (DaaS) provider that collects, organizes, and standardizes large-scale data from the public web, delivering ready-to-use datasets for property, people, business, and product data through their API, web portal, and bulk downloads.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Business Data
  - Data Aggregation
  - Data as a Service
  - People Data
  - Product Data
  - Property Data
url: https://raw.githubusercontent.com/api-evangelist/datafiniti/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: company
position: Consumer
access: 3rd-Party
apis:
  - aid: datafiniti:datafiniti-api
    name: Datafiniti API
    description: Unified Datafiniti REST API exposing search and download endpoints for businesses, products, properties, and people datasets, plus the bearer token authentication endpoint.
    humanURL: https://docs.datafiniti.co/docs/api-introduction
    baseURL: https://api.datafiniti.co/v4
    tags:
      - Authentication
      - Bulk Downloads
      - Search
    properties:
      - type: Documentation
        url: https://docs.datafiniti.co/docs/api-introduction
      - type: OpenAPI
        url: openapi/datafiniti-api.yml
      - type: JSONSchema
        url: json-schema/search-request.json
  - aid: datafiniti:business-data-api
    name: Datafiniti Business Data API
    description: Access a large catalog of business listings aggregated from hundreds of online directories and review websites, integrated with firmographics and reviews. Over 131 million business records available.
    humanURL: https://www.datafiniti.co/data/business-data
    tags:
      - Business Data
      - Business Listings
      - Firmographics
    properties:
      - type: Documentation
        url: https://developer.datafiniti.co
  - aid: datafiniti:product-data-api
    name: Datafiniti Product Data API
    description: Access millions of product records spanning major retailers, brands, and categories including detailed product information, pricing data, and reviews. Over 506 million product records available.
    humanURL: https://www.datafiniti.co/data/product-data
    tags:
      - E-Commerce
      - Pricing Data
      - Product Data
    properties:
      - type: Documentation
        url: https://developer.datafiniti.co/docs/getting-started-with-product-data
  - aid: datafiniti:property-data-api
    name: Datafiniti Property Data API
    description: Access a large catalog of real estate listings from dozens of websites, integrated with pricing data, amenities, and reviews. Over 205 million property records available.
    humanURL: https://www.datafiniti.co/data/property-data
    tags:
      - Listings
      - Property Data
      - Real Estate
    properties:
      - type: Documentation
        url: https://docs.datafiniti.co/docs/constructing-property-queries
  - aid: datafiniti:people-data-api
    name: Datafiniti People Data API
    description: Access people data records aggregated from public web sources. Over 4 million people records available.
    humanURL: https://www.datafiniti.co/data/people-data
    tags:
      - Contact Data
      - People Data
    properties:
      - type: Documentation
        url: https://developer.datafiniti.co
common:
  - type: Website
    url: https://www.datafiniti.co
  - type: Documentation
    url: https://docs.datafiniti.co/docs/api-introduction
  - type: Developer Portal
    url: https://developer.datafiniti.co
  - type: Sign Up
    url: https://portal.datafiniti.co/sign-up
  - type: Login
    url: https://portal.datafiniti.co
  - type: Blog
    url: https://blog.datafiniti.co
  - type: JSON-LD
    url: json-ld/datafiniti-context.jsonld
  - type: Vocabulary
    url: vocabulary/datafiniti-vocabulary.yml
  - type: Capabilities
    url: capabilities/datafiniti-capabilities.yml
  - type: Rules
    url: rules/datafiniti-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
