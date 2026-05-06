---
aid: diamond-search
url: https://raw.githubusercontent.com/api-evangelist/diamond-search/refs/heads/main/apis.yml
name: Diamond Search
description: IDEX Online is the leading polished diamonds trading platform for professionals, providing unbiased, market-driven diamond pricing tools, news and research. The IDEX Onsite and Data Report APIs deliver natural diamond, lab grown diamond, and market data feeds to subscribers of the IDEX trading platform.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Contract
position: Consuming
access: 3rd-Party
tags:
  - Diamonds
  - Lab Grown
  - Pricing
  - Trading
created: '2024-11-13'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: diamond-search:idex-onsite-full-feed-api
    name: IDEX Onsite Full Feed API
    humanURL: https://api.idexonline.com/Onsite/FullFeed
    baseURL: https://api.idexonline.com/onsite/api
    tags:
      - Diamonds
      - Feed
    properties:
      - type: Documentation
        url: https://api.idexonline.com/Onsite/FullFeed
      - type: OpenAPI
        url: openapi/idex-onsite-full-feed-api-openapi.yml
    description: In this natural diamond feed API you will send an HTTP request with the requested identifiers in JSON, and you will get the full details of matching pre-filtered diamonds back in the requested format. This service is available as an add-on to all subscribers of the IDEX trading platform, however, results may vary based on your subscription type and permissions. Filters and markups can be set on IDEX.
    contact:
      - FN: IDEX Online Support
        email: support@idexonline.com
  - aid: diamond-search:idex-lab-grown-file-api
    name: IDEX Lab Grown File API
    humanURL: https://api.idexonline.com/Onsite/LabGrownFullFile
    baseURL: https://api.idexonline.com/Onsite
    tags:
      - Diamonds
      - Lab Grown
    properties:
      - type: Documentation
        url: https://api.idexonline.com/Onsite/LabGrownFullFile
      - type: OpenAPI
        url: openapi/idex-lab-grown-file-api-openapi.yml
    description: In this lab grown diamond feed API you will send an HTTP request with the requested identifiers in JSON, and you will get the full details of all filtered available diamonds back in a zipped CSV file. This service is available as an add-on to all subscribers of the IDEX trading platform, however, results may vary based on your subscription type and permissions. This feed will return all lab grown diamond listings available for onsite feeds from IDEX.
    contact:
      - FN: IDEX Online Support
        email: support@idexonline.com
  - aid: diamond-search:idex-data-report-api
    name: IDEX Data Report API
    humanURL: https://api.idexonline.com/IdexDataApi/Report3
    baseURL: https://api.idexonline.com/IdexDataApi
    tags:
      - Diamonds
      - Reports
    properties:
      - type: Documentation
        url: https://api.idexonline.com/IdexDataApi/Report3
      - type: OpenAPI
        url: openapi/idex-data-report-api-openapi.yml
    description: In this API you will send an HTTP request with a date for which you want the report. You will get back a zipped CSV file. The file creation process may take a few minutes.
    contact:
      - FN: IDEX Online Support
        email: support@idexonline.com
common:
  - type: Newsroom
    name: IDEX Online RSS Feeds
    url: http://www.idexonline.com/rssfeeds
    description: Really Simple Syndication (RSS) is a format for content distribution. IDEX Online offers a number of RSS feeds. Using an RSS reader, online service, or your browser, you can subscribe for free to any of IDEX Online's channels or track a specific subject.
  - type: Login
    name: IDEX Online Login
    url: https://www.idexonline.com/ns24/auth/login.aspx
  - type: Sign-Up
    name: IDEX Online Sign-Up
    url: https://www.idexonline.com/register.aspx
  - type: PrivacyPolicy
    name: IDEX Online Privacy Guarantees
    url: http://www.idexonline.com/Privacy
  - type: TermsOfService
    name: IDEX Online Terms and Conditions
    url: http://www.idexonline.com/Conditions
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
