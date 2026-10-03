---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 26
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-03-26'
description: An index and topic collection covering API aggregation, marketplaces, directories, unified APIs, and catalog platforms. API aggregation brings together multiple APIs under a single interface, simplifying integration, reducing maintenance overhead, and enabling consistent authentication and data normalization across disparate services. This collection includes API marketplaces like RapidAPI, unified API platforms like Merge and Apideck, API directories like APIs.guru and APIs.io, web scraping aggregators, and open-source catalog tools like Backstage.
examples:
- key_count: 10
  name: Aggregation Api Catalog Entry Example
  slug: aggregation-api-catalog-entry-example
- key_count: 7
  name: Aggregation Unified Api Example
  slug: aggregation-unified-api-example
features:
- description: API aggregation platforms expose multiple underlying APIs through a single, standardized interface, reducing the integration burden for developers.
  name: Unified API Interface
- description: API directories and marketplaces like RapidAPI, APIs.guru, and APIs.io help developers discover, evaluate, and subscribe to APIs from multiple providers.
  name: API Marketplaces and Discovery
- description: Unified API platforms like Merge and Apideck normalize data schemas across disparate HR, CRM, and accounting systems into a consistent model.
  name: Data Normalization
- description: Aggregation layers handle OAuth, API keys, and other authentication flows across multiple providers, presenting a single auth interface to the consumer.
  name: Authentication Abstraction
- description: Internal API catalog tools like Backstage and Stoplight enable organizations to document, discover, and govern APIs across the enterprise.
  name: API Catalogs and Internal Discovery
- description: Platforms like Bright Data, Apify, and ScrapingBee aggregate web data and expose it through structured APIs, removing the need for custom scraper maintenance.
  name: Web Scraping as API
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: The largest API marketplace with 40,000+ APIs available to developers through a unified subscription and API key model.
  name: RapidAPI
- description: Unified API for HR, payroll, accounting, CRM, and ATS integrations across 100+ providers.
  name: Merge
- description: Unified API platform for CRM, file storage, accounting, and e-commerce integrations.
  name: Apideck
- description: API aggregation platform enabling AI agents to use 100+ apps as structured tools.
  name: Composio
- description: Open-source developer portal and API catalog platform from Spotify for internal service discovery.
  name: Backstage
- description: Open-source directory of machine-readable API specifications (OpenAPI) maintained by the community.
  name: APIs.guru
- description: Financial data aggregation platform connecting apps to bank accounts and financial institutions.
  name: Plaid
- description: Open-source unified API for OAuth integrations across 200+ apps.
  name: Nango
json_schemas:
- name: APICatalogEntry
  property_count: 10
  slug: aggregation-api-catalog-entry
- name: UnifiedAPI
  property_count: 7
  slug: aggregation-unified-api
json_structures:
- name: Aggregation Api Catalog Entry Structure
  property_count: 10
  slug: aggregation-api-catalog-entry-structure
- name: Aggregation Unified Api Structure
  property_count: 7
  slug: aggregation-unified-api-structure
jsonld:
- class_count: 5
  name: Aggregation Context
  property_count: 12
  slug: aggregation-context
layout: provider
modified: '2026-04-19'
name: Aggregation
nav: Providers
network: true
overview: 'Aggregation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include API Aggregation, API Directory, and API Marketplace.


  The Aggregation catalog on APIs.io includes 1 JSON-LD context.


  Aggregation''s developer surface includes developer portal and 1 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 39.3
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: aggregation
tags:
- API Aggregation
- API Directory
- API Marketplace
use_cases:
- description: Unified API platforms like Merge and Apideck enable applications to sync with dozens of HR systems (BambooHR, Workday, ADP) through a single normalized API.
  name: Unified HR and CRM Integration
- description: API providers publish their APIs to marketplaces like RapidAPI to reach new developer audiences and monetize access through tiered subscription plans.
  name: API Marketplace Distribution
- description: Organizations use API catalogs like Backstage or Stoplight to document, version, and govern internal APIs across product teams.
  name: Internal API Governance
- description: Platforms like Plaid and Codat aggregate financial account data from banks and accounting systems into normalized APIs for fintech applications.
  name: Financial Data Aggregation
- description: Aggregation platforms like Composio expose hundreds of third-party APIs as unified tool sets that AI agents can discover and invoke.
  name: AI Agent Tool Federation
website: https://apievangelist.com
---
