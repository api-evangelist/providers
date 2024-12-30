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
    description: >-
      In this lab grown diamond feed API you will send an HTTP request with the
      requested identifiers in JSON, and you will get the full details of all
      filtered available diamonds back in a zipped CSV file. This service is
      available as an add-on to all subscribers of the IDEX trading platform,
      however, results may vary based on your subscription type and permissions.
      This feed will return all lab grown diamond listings available for onsite
      feeds from IDEX.
  - aid: diamond-search:idex-data-report-api
    name: IDEX Date Report API
    tags:
      - Diamonds
      - Lab Grown
    humanURL: https://api.idexonline.com/IdexDataApi/Report3
    properties:
      - url: https://api.idexonline.com/IdexDataApi/Report3
        type: Documentation
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