---
aid: elsevier
name: Elsevier
description: Elsevier is a Dutch academic publishing company specializing in scientific, technical, and medical content. Its products include journals such as The Lancet and Cell, the ScienceDirect collection of electronic journals, the online citation database Scopus, the SciVal research performance platform, and the ClinicalKey search engine for clinicians.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Content
  - Journals
  - Medical
  - Research
  - Scientific
  - Technical
created: '2023-11-22'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: elsevier:elsevier-scopus-apis
    name: Elsevier Scopus APIs
    description: Scopus delivers a comprehensive view of the world of research, allowing tracking, analysis, and visualization of research data across publishers, journals, books, conference proceedings, and trade publications.
    humanURL: https://dev.elsevier.com/sc_apis.html
    tags:
      - Citations
      - Research
      - Scientific
    properties:
      - type: Documentation
        url: https://dev.elsevier.com/scopus.html
      - type: Specification
        url: https://dev.elsevier.com/api_docs.html
  - aid: elsevier:elsevier-sciencedirect-apis
    name: Elsevier ScienceDirect APIs
    description: ScienceDirect APIs expose peer-reviewed full-text scientific, technical and medical content from all scholarly publications indexed by ScienceDirect, Elsevier's premier scientific platform.
    humanURL: https://dev.elsevier.com/sd_apis.html
    tags:
      - Full Text
      - Journals
      - Scientific
    properties:
      - type: Documentation
        url: https://dev.elsevier.com/sciencedirect.html
      - type: Specification
        url: https://dev.elsevier.com/api_docs.html
  - aid: elsevier:elsevier-scival-api
    name: Elsevier SciVal API
    description: The SciVal API gives access to a comprehensive set of metrics for researchers (Scopus Author profiles) and 8,500+ institutions available in SciVal, Elsevier's platform for research performance benchmarking.
    humanURL: https://dev.elsevier.com/scival_apis.html
    tags:
      - Benchmarking
      - Metrics
      - Research
    properties:
      - type: Documentation
        url: https://dev.elsevier.com/scival.html
      - type: Specification
        url: https://dev.elsevier.com/api_docs.html
  - aid: elsevier:elsevier-engineering-village-api
    name: Elsevier Engineering Village API
    description: Engineering Village APIs provide programmatic access to engineering research literature, indexed publications, and engineering-focused content across multiple databases.
    humanURL: https://dev.elsevier.com/ev.html
    tags:
      - Engineering
      - Research
    properties:
      - type: Documentation
        url: https://dev.elsevier.com/ev.html
  - aid: elsevier:elsevier-embase-api
    name: Elsevier Embase API
    description: Embase APIs provide access to biomedical and pharmacological abstracts and indexing for life sciences research, drug development, and evidence-based medicine.
    humanURL: https://dev.elsevier.com/embase.html
    tags:
      - Biomedical
      - Medical
      - Pharmacology
    properties:
      - type: Documentation
        url: https://dev.elsevier.com/embase.html
common:
  - type: Portal
    url: https://dev.elsevier.com/
  - type: GettingStarted
    url: https://dev.elsevier.com/getting_started.html
  - type: Documentation
    url: https://dev.elsevier.com/api_docs.html
  - type: UseCases
    url: https://dev.elsevier.com/use_cases.html
  - type: TermsOfService
    url: https://dev.elsevier.com/api_service_agreement.html
  - type: PrivacyPolicy
    url: http://www.elsevier.com/locate/privacypolicy
  - type: Examples
    url: https://dev.elsevier.com/examples.html
  - type: Guides
    url: https://dev.elsevier.com/technical_documentation.html
  - type: SDK
    url: https://github.com/ElsevierDev/elsapy
  - type: Support
    url: https://dev.elsevier.com/support.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
