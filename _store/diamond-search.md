---
aid: diamond-search
url: >-
  https://raw.githubusercontent.com/api-search/diamond-search/refs/heads/main/apis.yml
apis:
  - aid: diamond-search:idex-onsite-full-feed-api
    name: IDEX Onsite Full Feed API
    tags:
      - Diamonds
    humanURL: https://api.idexonline.com/Onsite/FullFeed
    properties:
      - url: https://api.idexonline.com/Onsite/FullFeed
        type: Documentation
      - url: properties/idex-onsite-full-feed-api-openapi.yml
        type: OpenAPI
    description: >-
      In this natural diamond feed API you will send an HTTP request with the
      requested identifiers in JSON, and you will get the full details of
      matching pre-filtered diamonds back in the requested format. This service
      is available as an add-on to all subscribers of the IDEX trading platform,
      however, results may vary based on your subscription type and permissions.
      Filters and markups can be set on IDEX.
  - aid: diamond-search:idex-lab-grown-file-api
    name: IDEX Lab Grown File API
    tags:
      - Diamonds
      - Lab Grown
    humanURL: https://api.idexonline.com/Onsite/LabGrownFullFile
    properties:
      - url: https://api.idexonline.com/Onsite/LabGrownFullFile
        type: Documentation
      - url: properties/idex-lab-grown-file-api-openapi.yml
        type: OpenAPI
    description: >-
      In this lab grown diamond feed API you will send an HTTP request with the
      requested identifiers in JSON, and you will get the full details of all
      filtered available diamonds back in a zipped CSV file. This service is
      available as an add-on to all subscribers of the IDEX trading platform,
      however, results may vary based on your subscription type and permissions.
      This feed will return all lab grown diamond listings available for onsite
      feeds from IDEX.
  - aid: diamond-search:idex-data-report-api
    name: IDEX Data Report API
    tags:
      - Diamonds
      - Lab Grown
    humanURL: https://api.idexonline.com/IdexDataApi/Report3
    properties:
      - url: https://api.idexonline.com/IdexDataApi/Report3
        type: Documentation
      - url: properties/idex-data-report-api-openapi.yml
        type: OpenAPI
    description: >-
      In this API you will send an HTTP request with a date for which you want
      the report. You will get back a zipped CSV file. The file creation process
      may take a few minutes.
name: Diamond Search
tags:
  - Diamonds
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: http://www.idexonline.com/rssfeeds
    name: IDEX online
    type: Newsroom
    description: >-
      Really Simple Syndication (RSS) is a format for content distribution. IDEX
      Online offers a number of RSS feeds. Using an RSS reader, online service,
      or your browser, you can subscribe for free to any of IDEX Onlines
      channels or track a specific subject.
  - url: https://www.idexonline.com/ns24/auth/login.aspx
    name: >-
      IDEX Online - Diamond Exchange, Diamond Prices, News, Research and
      Analysis
    type: Login
    description: 'null'
  - url: https://www.idexonline.com/register.aspx
    name: none
    type: Sign-Up
    description: 'null'
  - url: http://www.idexonline.com/Privacy
    name: IDEX online - Guarantees
    type: PrivacyPolicy
    description: 'null'
  - url: http://www.idexonline.com/Conditions
    name: IDEX online - Terms and Conditions
    type: TermsOfService
    description: 'null'
created: '2024-11-13'
modified: '2024-12-30'
position: Consuming
description: >-
  IDEX Online is the leading polished diamonds trading platform for
  professionals, providing unbiased, market-driven diamond pricing tools, news
  and research.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---