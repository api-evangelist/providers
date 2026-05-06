---
aid: cancer-gov
name: Cancer.gov
url: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
tags:
  - Cancer
  - Federal Government
  - Healthcare
  - Research
  - Clinical Trials
  - Genomics
  - Surveillance
  - Open Data
access: Open
created: '2024-07-02'
modified: '2026-04-23'
position: Provider
specificationVersion: '0.19'
description: Cancer.gov is the web presence of the National Cancer Institute (NCI), the U.S. federal government's principal agency for cancer research and training. NCI and its partner programs expose a rich set of open APIs covering cancer clinical trials, genomic data, cancer-incidence surveillance, research data and models, terminology and vocabularies, and PDQ content — giving researchers, advocacy groups, clinicians, and application developers programmatic access to authoritative cancer data and content.
apis:
  - aid: cancer-gov:clinical-trials-api
    name: NCI Clinical Trials Search API
    description: RESTful API that lets developers build applications, search tools, and digital platforms over NCI-supported cancer clinical trials data sourced from NCI's Clinical Trials Reporting Program (CTRP). The same API powers NCI's public Clinical Trials Search. Developers register for a free API key through the CTS Developer Accounts portal.
    humanURL: https://clinicaltrialsapi.cancer.gov/
    baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
    tags:
      - Clinical Trials
      - CTRP
      - Research
    properties:
      - type: Documentation
        url: https://clinicaltrialsapi.cancer.gov/
      - type: SignUp
        url: https://clinicaltrialsapi.cancer.gov/
      - type: ParentPage
        url: https://www.cancer.gov/syndication/api
  - aid: cancer-gov:gdc-api
    name: NCI Genomic Data Commons (GDC) API
    description: The external-facing REST interface for the NCI Genomic Data Commons. Drives the GDC Data Portal and GDC Submission Portal and is open for programmatic access. Provides query, download, and submission endpoints for cancer genomics datasets including TCGA, TARGET, CPTAC, and other NCI-funded genomic programs.
    humanURL: https://gdc.cancer.gov/developers/gdc-application-programming-interface-api
    baseURL: https://api.gdc.cancer.gov
    tags:
      - Genomics
      - TCGA
      - Research Data
    properties:
      - type: Documentation
        url: https://docs.gdc.cancer.gov/API/Users_Guide/Getting_Started/
      - type: Reference
        url: https://docs.gdc.cancer.gov/Encyclopedia/pages/REST_API/
      - type: Portal
        url: https://portal.gdc.cancer.gov/
  - aid: cancer-gov:seer-api
    name: NCI SEER API
    description: RESTful API for the Surveillance, Epidemiology, and End Results (SEER) Program. Supports SEER datasets plus staging APIs for cancer staging (TNM and Collaborative Stage algorithms), enabling developers to embed authoritative incidence, survival, and staging logic into their own systems.
    humanURL: https://api.seer.cancer.gov/
    baseURL: https://api.seer.cancer.gov
    tags:
      - Surveillance
      - Epidemiology
      - Staging
      - SEER
    properties:
      - type: Documentation
        url: https://api.seer.cancer.gov/docs
      - type: Portal
        url: https://api.seer.cancer.gov/
  - aid: cancer-gov:modac-api
    name: NCI MoDaC API
    description: The NCI Model and Data Clearinghouse (MoDaC) API provides programmatic access to cancer research data, computational models, and associated tools hosted in MoDaC. Developers can search, retrieve metadata, and download model/data artifacts produced by NCI-funded research programs.
    humanURL: https://modac.cancer.gov/
    tags:
      - Research Data
      - Models
      - Clearinghouse
    properties:
      - type: Documentation
        url: https://modac.cancer.gov/swagger-ui/4.14.0/index.html
      - type: Portal
        url: https://modac.cancer.gov/
  - aid: cancer-gov:evs-api
    name: NCI EVS Terminology API
    description: Enterprise Vocabulary Services (EVS) exposes NCI Thesaurus and NCI Metathesaurus content — over 192,000 concepts, 154,000 textual definitions, 623,000 synonyms and 630,000 inter-concept relationships — through a search and browse API used to code, analyze, and share cancer and biomedical research information.
    humanURL: https://evs.nci.nih.gov/
    tags:
      - Terminology
      - Vocabulary
      - NCI Thesaurus
    properties:
      - type: Documentation
        url: https://evs.nci.nih.gov/
      - type: Explorer
        url: https://evsexplore.semantics.cancer.gov/
      - type: WhitePaper
        url: https://evs.nci.nih.gov/ftp1/NCI_Metathesaurus/EVS%20Metathesaurus%20White%20Paper.pdf
  - aid: cancer-gov:syndication-services
    name: NCI Content Syndication Services
    description: A suite of syndicated content channels — RSS feeds, the NCI Dictionary Widget, and syndicated publication content — that partner sites and health platforms can embed to deliver authoritative cancer content sourced from cancer.gov.
    humanURL: https://www.cancer.gov/syndication
    tags:
      - Syndication
      - Content
      - Widgets
      - RSS
    properties:
      - type: Documentation
        url: https://www.cancer.gov/syndication
common:
  - type: Website
    url: https://www.cancer.gov/
  - type: Portal
    url: https://api.cancer.gov/
  - type: SyndicationServices
    url: https://www.cancer.gov/syndication
  - type: DataScience
    url: https://datascience.cancer.gov/
  - type: OpenDataPolicy
    url: https://www.cancer.gov/research/resources/open-science
  - type: PrivacyPolicy
    url: https://www.cancer.gov/policies/privacy-security
  - type: LicensingAndReuse
    url: https://www.cancer.gov/policies/copyright-reuse
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
