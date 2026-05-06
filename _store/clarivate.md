---
aid: clarivate
name: Clarivate
url: https://raw.githubusercontent.com/api-evangelist/clarivate/refs/heads/main/apis.yml
created: '2024-12-16'
modified: '2026-04-23'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Citations
  - Data
  - Drug Pipeline
  - Insights
  - Intellectual Property
  - Life Sciences
  - Patents
  - Publications
  - Research
description: 'Clarivate is a global information services company providing data, insights, and analytics across academia, government, life sciences, healthcare, and intellectual property. Clarivate exposes a unified developer portal at developer.clarivate.com that catalogs APIs across its product families: Web of Science for publication and citation data, Derwent for patent data, Cortellis for life sciences and drug pipeline intelligence, and supporting tools such as InCites and ScholarOne. APIs are subscription-based and authenticated with per-API keys issued through the developer portal after subscription approval.'
apis:
  - aid: clarivate:web-of-science-api
    name: Web of Science APIs
    tags:
      - Bibliometrics
      - Citations
      - Publications
      - Research Analytics
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.clarivate.com/apis/wos
    properties:
      - url: https://developer.clarivate.com/apis/wos
        type: Documentation
    description: Web of Science APIs deliver publication and citation data drawn from the curated Web of Science Core Collection, supporting bibliometric analysis, research evaluation, and institutional assessment workflows.
  - aid: clarivate:derwent-innovation-api
    name: Derwent Innovation API
    tags:
      - Derwent
      - Intellectual Property
      - Patents
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.clarivate.com/apis/derwent
    properties:
      - url: https://developer.clarivate.com/apis/derwent
        type: Documentation
    description: The Derwent Innovation API provides programmatic access to Derwent World Patents Index data, including normalized patent records, families, and citations used for IP intelligence and competitive analysis.
  - aid: clarivate:cortellis-api
    name: Cortellis APIs
    tags:
      - Clinical Trials
      - Cortellis
      - Drug Pipeline
      - Life Sciences
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cortellis.com/
    properties:
      - url: https://developer.clarivate.com/apis/cortellis
        type: Documentation
      - url: https://www.cortellis.com/
        type: Portal
    description: Cortellis APIs expose the Clarivate life sciences intelligence platform, covering drug pipelines, clinical trials, regulatory intelligence, deals, and competitive intelligence for biopharma and medical-device companies.
  - aid: clarivate:incites-api
    name: InCites Benchmarking and Analytics API
    tags:
      - Benchmarking
      - InCites
      - Research Analytics
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.clarivate.com/apis/incites
    properties:
      - url: https://developer.clarivate.com/apis/incites
        type: Documentation
    description: The InCites API provides programmatic access to the Clarivate research benchmarking platform, enabling institutional research performance analytics built on Web of Science data.
common:
  - type: Website
    url: https://clarivate.com/
  - type: Portal
    url: https://developer.clarivate.com/
  - type: API Catalog
    url: https://developer.clarivate.com/apis
  - type: Support
    url: https://support.clarivate.com/
  - type: Privacy Policy
    url: https://clarivate.com/privacy-center/
  - type: Terms of Service
    url: https://clarivate.com/legal-center/
  - type: JSON-LD
    url: json-ld/clarivate-context.jsonld
  - type: Spectral
    url: rules/clarivate-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/clarivate-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
