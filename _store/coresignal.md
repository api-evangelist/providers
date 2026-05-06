---
aid: coresignal
name: Coresignal
x-type: company
description: Coresignal is a data-as-a-service company providing access to public web data on companies, employees, and jobs through a suite of REST APIs. The platform aggregates and refines more than 4.5 billion data records covering 75M+ companies (with 500+ data fields), 865M+ employee profiles (300+ fields), and 461M+ job postings (85+ fields). Coresignal offers Multi-source, Clean, and Base data tiers across Company, Employee, and Jobs APIs, plus specialized real-time, employee posts, agentic search, and company enrichment endpoints. Authentication uses a single apikey HTTP header.
url: https://raw.githubusercontent.com/api-evangelist/coresignal/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: 3rd-Party
position: Consumer
tags:
  - Agentic Search
  - B2B Data
  - Companies
  - Company Data
  - Data as a Service
  - Elasticsearch
  - Employee Data
  - Employees
  - Enrichment
  - Firmographics
  - Job Postings
  - Jobs
  - Lead Generation
  - People Data
  - Sales Intelligence
  - Talent Intelligence
  - Web Data
created: '2025-02-12'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: coresignal:multi-source-company-api
    name: Coresignal Multi-source Company API
    description: The Multi-source Company API returns enriched company records combining data from multiple public web sources, deduplicated and standardized with 500+ data fields covering firmographics, technographics, headcount, revenue, and locations. Search uses Elasticsearch DSL. Results are paginated and credits-priced per response.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.coresignal.com/multi-source-company-api/
    baseURL: https://api.coresignal.com/cdapi/v2/multi_source_company
    tags:
      - Companies
      - Firmographics
      - Multi-source
    properties:
      - type: Documentation
        url: https://docs.coresignal.com/multi-source-company-api/
      - type: DataDictionary
        url: https://docs.coresignal.com/multi-source-company-api/data-dictionary
      - type: Sample
        url: https://docs.coresignal.com/multi-source-company-api/sample
      - type: SearchFilters
        url: https://docs.coresignal.com/multi-source-company-api/search-filters
      - type: ElasticsearchDSL
        url: https://docs.coresignal.com/multi-source-company-api/search-with-es-dsl
      - type: Collect
        url: https://docs.coresignal.com/multi-source-company-api/collect
      - type: BulkCollect
        url: https://docs.coresignal.com/multi-source-company-api/bulk-collect
      - type: Webhooks
        url: https://docs.coresignal.com/multi-source-company-api/subscriptions
      - type: OpenAPI
        url: openapi/coresignal-multi-source-company-api-openapi.yml
      - type: Rules
        url: rules/coresignal-multi-source-company-api-rules.yml
      - type: Capabilities
        url: capabilities/coresignal-company-data-collection-capabilities.yml
  - aid: coresignal:multi-source-employee-api
    name: Coresignal Multi-source Employee API
    description: The Multi-source Employee API returns enriched employee profiles aggregated from multiple public sources with 300+ data fields covering experience, education, skills, certifications, and connections. Search uses Elasticsearch DSL with rich filter support, pagination, and collect/bulk_collect endpoints for retrieving full records by ID.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.coresignal.com/multi-source-employee-api/
    baseURL: https://api.coresignal.com/cdapi/v2/multi_source_employee
    tags:
      - Employees
      - Multi-source
      - People Data
    properties:
      - type: Documentation
        url: https://docs.coresignal.com/multi-source-employee-api/
      - type: DataDictionary
        url: https://docs.coresignal.com/multi-source-employee-api/data-dictionary
      - type: Sample
        url: https://docs.coresignal.com/multi-source-employee-api/sample
      - type: SearchFilters
        url: https://docs.coresignal.com/multi-source-employee-api/search-filters
      - type: ElasticsearchDSL
        url: https://docs.coresignal.com/multi-source-employee-api/search-with-es-dsl
      - type: Collect
        url: https://docs.coresignal.com/multi-source-employee-api/collect
      - type: BulkCollect
        url: https://docs.coresignal.com/multi-source-employee-api/bulk-collect
      - type: Webhooks
        url: https://docs.coresignal.com/multi-source-employee-api/subscriptions
      - type: OpenAPI
        url: openapi/coresignal-multi-source-employee-api-openapi.yml
      - type: Rules
        url: rules/coresignal-multi-source-employee-api-rules.yml
      - type: Capabilities
        url: capabilities/coresignal-employee-data-collection-capabilities.yml
  - aid: coresignal:multi-source-jobs-api
    name: Coresignal Multi-source Jobs API
    description: The Multi-source Jobs API returns enriched job posting records aggregated from multiple public sources with 85+ data fields covering title, location, company, salary, posted date, source URLs, and full job descriptions. Search uses Elasticsearch DSL with collect endpoints for retrieving full records by ID.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.coresignal.com/multi-source-jobs-api/
    baseURL: https://api.coresignal.com/cdapi/v2/multi_source_jobs
    tags:
      - Jobs
      - Multi-source
      - Recruiting
    properties:
      - type: Documentation
        url: https://docs.coresignal.com/multi-source-jobs-api/
      - type: DataDictionary
        url: https://docs.coresignal.com/multi-source-jobs-api/data-dictionary
      - type: Sample
        url: https://docs.coresignal.com/multi-source-jobs-api/sample
      - type: SearchFilters
        url: https://docs.coresignal.com/multi-source-jobs-api/search-filters
      - type: ElasticsearchDSL
        url: https://docs.coresignal.com/multi-source-jobs-api/search-with-es-dsl
      - type: Collect
        url: https://docs.coresignal.com/multi-source-jobs-api/collect
      - type: OpenAPI
        url: openapi/coresignal-multi-source-jobs-api-openapi.yml
      - type: Rules
        url: rules/coresignal-multi-source-jobs-api-rules.yml
      - type: Capabilities
        url: capabilities/coresignal-jobs-data-collection-capabilities.yml
  - aid: coresignal:agentic-search-api
    name: Coresignal Agentic Search API
    description: The Agentic Search API enables natural language search across Coresignal's company, employee, and jobs datasets, returning relevant records based on conversational queries. Designed for AI agents and automated workflows that need quick B2B data lookups without crafting Elasticsearch queries.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.coresignal.com/agentic-search-api/
    baseURL: https://api.coresignal.com/cdapi/v2/agentic_search
    tags:
      - Agentic Search
      - AI Agents
      - Natural Language
    properties:
      - type: Documentation
        url: https://docs.coresignal.com/agentic-search-api/
  - aid: coresignal:company-enrichment-api
    name: Coresignal Company Enrichment API
    description: The Company Enrichment API takes a company domain or name and returns a fully-enriched company record. Designed for sales and marketing systems that need to enrich CRM records or web form submissions in real time.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.coresignal.com/company-enrichment-api/
    baseURL: https://api.coresignal.com/cdapi/v2/company_enrichment
    tags:
      - Companies
      - Enrichment
      - CRM
    properties:
      - type: Documentation
        url: https://docs.coresignal.com/company-enrichment-api/
common:
  - type: Website
    url: https://coresignal.com
  - type: DeveloperPortal
    url: https://docs.coresignal.com/
  - type: Documentation
    url: https://docs.coresignal.com/
  - type: APIsOverview
    url: https://docs.coresignal.com/api-introduction/apis-overview
  - type: Authorization
    url: https://docs.coresignal.com/api-introduction/authorization
  - type: GettingStarted
    url: https://docs.coresignal.com/api-introduction/getting-started
  - type: RateLimits
    url: https://docs.coresignal.com/api-introduction/rate-limits
  - type: ResponseCodes
    url: https://docs.coresignal.com/api-introduction/response-codes
  - type: Credits
    url: https://docs.coresignal.com/api-introduction/credits
  - type: Webhooks
    url: https://docs.coresignal.com/api-introduction/webhooks
  - type: Dashboard
    url: https://dashboard.coresignal.com/sign-in
  - type: SignUp
    url: https://dashboard.coresignal.com/sign-up
  - type: Pricing
    url: https://coresignal.com/pricing/
  - type: Solutions
    url: https://coresignal.com/solutions/
  - type: UseCases
    url: https://coresignal.com/use-cases/
  - type: Blog
    url: https://coresignal.com/blog/
  - type: Vocabulary
    url: vocabulary/coresignal-vocabulary.yml
  - type: JSONLD
    url: json-ld/coresignal-context.jsonld
  - type: PrivacyPolicy
    url: https://coresignal.com/privacy-policy/
  - type: TermsOfService
    url: https://coresignal.com/terms-and-conditions/
  - type: Status
    url: https://status.coresignal.com/
  - type: LinkedIn
    url: https://www.linkedin.com/company/coresignal
  - type: Twitter
    url: https://twitter.com/coresignal
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
