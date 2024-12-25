---
aid: elsevier
url: https://raw.githubusercontent.com/apis-json/artisanal/main/apis/elsevier.yml
apis:
  - aid: elsevier:elsevier-scopus-apis
    name: Elsevier Scopus APIs
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://dev.elsevier.com/sc_apis.html
    overlays:
      - url: overlays/https://dev.elsevier.com/elsdoc/scopus-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://dev.elsevier.com/scopus.html
        type: Documentation
      - url: https://dev.elsevier.com/elsdoc/scopus
        type: OpenAPI
    description: >-
      Scopus delivers a comprehensive view of the world of research. Scopus.com
      allows you to track analyze and visualize research data from 5000
      different publishers. It covers 78 million items including records from
      journals, books and book series, conference proceedings and trade
      publications across 16 million Author Profiles and 70,000 Institutional
      Profiles All of this comes together to power your research and help you to
      stay abreast with current publications, find co-authors, analyze journals
      to publish in and track and monitor global trends
  - aid: elsevier:elsevier-sciencedirect-apis
    name: Elsevier ScienceDirect APIs
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://dev.elsevier.com/sd_apis.html
    overlays:
      - url: >-
          overlays/https://dev.elsevier.com/elsdoc/sciencedirect-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://dev.elsevier.com/sciencedirect.html
        type: Documentation
      - url: https://dev.elsevier.com/elsdoc/sciencedirect
        type: OpenAPI
    description: >+
      ScienceDirect APIs expose peer-reviewed full-text scientific, technical
      and medical content from all scholarly publications indexed by
      ScienceDirect, Elsevier's premier scientific platform.

  - aid: elsevier:elsevier-scival-api
    name: Elsevier SciVal API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://dev.elsevier.com/scival_apis.html
    overlays:
      - url: overlays/https://dev.elsevier.com/elsdoc/scival-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://dev.elsevier.com/scival.html
        type: Documentation
      - url: https://dev.elsevier.com/elsdoc/scival
        type: OpenAPI
    description: >+
      The SciVal API gives access to a comprehensive basket of metrics for
      researchers (Scopus Author profiles) and all 8,500+ institutions available
      in SciVal, Elsevier's platform for research performance benchmarking. It
      returns metrics from SciVal for a given a Scopus Author or Institution
      identifier (or multiples of each).

name: Elsevier
tags:
  - Scientific
  - Technical
  - Medical
  - Content
  - Journals
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
common:
  - url: https://dev.elsevier.com/
    type: Portal
  - url: https://dev.elsevier.com/use_cases.html
    type: Use Cases
  - url: https://dev.elsevier.com/api_service_agreement.html
    type: Terms of Service
  - url: https://dev.elsevier.com/examples.html
    type: Examples
  - url: https://dev.elsevier.com/technical_documentation.html
    type: Guides
  - url: https://github.com/ElsevierDev/elsapy
    type: SDK
  - url: https://dev.elsevier.com/support.html
    type: Support
  - url: http://www.elsevier.com/locate/privacypolicy
    type: Privacy Policy
created: 2023/11/22
modified: '2024-11-14'
overlays:
  - url: overlays/apis-io-search.yml
    type: APIs.io Search
  - url: overlays/apis-io-search.yml
    type: API Evangelist Ratings
description: >-
  Elsevier is a Dutch academic publishing company specializing in scientific,
  technical, and medical content. Its products include journals such as The
  Lancet, Cell, the ScienceDirect collection of electronic journals, Trends, the
  Current Opinion series, the online citation database Scopus, the SciVal tool
  for measuring research performance, the ClinicalKey search engine for
  clinicians, and the ClinicalPath evidence-based cancer care service. 
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.16'
---