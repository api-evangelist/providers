---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.8
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: 'Real-time Nasdaq market data delivered over Apache Kafka (TLS) with SASL/OAUTHBEARER authentication against a Keycloak pro-realm token endpoint. Topics documented in the NCDS Java and Python SDKs: GID'
  name: Nasdaq Cloud Data Service (NCDS) — Kafka Streams
  slug: nasdaq-cloud-data-service-ncds-kafka-streams
- description: 'REST access to Nasdaq Data Link tabular datasets: GET /api/v3/datatables/{datatable_code}.{format} with row and column filters (qopts.columns), cursor pagination (qopts.cursor_id), metadata, and bulk '
  name: Nasdaq Data Link Tables API
  slug: nasdaq-data-link-tables-api
- description: 'Asynchronous bulk download of Nasdaq Data Link tables: GET /api/v1/bulkdownloads/{datatable_code} with row filters returns a job (PENDING, RUNNING, SUCCEEDED...) and file URLs fetched with the X-Api-T'
  name: Nasdaq Data Link Bulk Download API
  slug: nasdaq-data-link-bulk-download-api
- baseURL: https://{base_url}/v1
  baseurl_source: declared
  description: Request-based REST API for real-time and delayed Nasdaq, BX, PSX and CQT equities (last sale, last trade, last quote, snapshot, trends, bars), indexes, ETPs and options chains/prices, plus reference d
  name: Nasdaq Cloud Data Service (NCDS) REST API
  slug: nasdaq-cloud-data-service-ncds-rest-api
artifact_total: 10
asyncapis:
- description: AsyncAPI 2.6 description of the Nasdaq Cloud Data Service (NCDS) public delivery surface. NCDS delivers real-time exchange data over Apache Kafka (TLS) using SASL/OAUTHBEARER against a Keycloak `pro-r
  name: Nasdaq Cloud Data Service (NCDS) — Kafka Streams
  slug: nasdaq-asyncapi
common:
- group: operate
  href: https://artifacts.apis.io/nasdaq/rate-limits/nasdaq-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nasdaq-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/nasdaq/rules/nasdaq-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/nasdaq-asyncapi-spectral-rules.yml
- group: docs
  href: https://artifacts.apis.io/nasdaq/asyncapi/nasdaq-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/nasdaq-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/nasdaq/conventions/nasdaq-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nasdaq-conventions.yml
- group: auth
  href: https://artifacts.apis.io/nasdaq/authentication/nasdaq-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nasdaq-authentication.yml
- group: design
  href: https://artifacts.apis.io/nasdaq/lifecycle/nasdaq-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nasdaq-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/nasdaq/errors/nasdaq-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/nasdaq-error-codes.yml
- group: auth
  href: https://artifacts.apis.io/nasdaq/well-known/nasdaq-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nasdaq-status-security.txt
- group: agent
  href: https://artifacts.apis.io/nasdaq/well-known/nasdaq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nasdaq-well-known.yml
- group: other
  href: https://artifacts.apis.io/nasdaq/hosts/nasdaq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nasdaq-hosts.yml
- group: build
  href: https://artifacts.apis.io/nasdaq/integrations/nasdaq-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/nasdaq-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/nasdaq/vendors/nasdaq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nasdaq-vendors.yml
- group: build
  href: https://artifacts.apis.io/nasdaq/packages/nasdaq-packages.yml
  title: ''
  type: Packages
  url: packages/nasdaq-packages.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaq.com/
- group: auth
  href: https://artifacts.apis.io/nasdaq/security/nasdaq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nasdaq-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nasdaq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nasdaq
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.nasdaq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.nasdaq.com/products/data/data-link/api
- group: operate
  title: ''
  type: StatusPage
  url: https://status.data.nasdaq.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nasdaq.com/privacy-statement
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/nasdaq
- group: docs
  title: ''
  type: Documentation
  url: https://docs.data.nasdaq.com/
created: '2026-05-05'
description: 'Nasdaq, Inc. operates the Nasdaq stock exchanges and sells market data, index, and financial technology products. Its developer surface is Nasdaq Data Link (data.nasdaq.com): a Tables API (REST, api_key, JSON/XML/CSV, 10,000-row pages with cursor and bulk export), a Bulk Download API, a request-based REST API for real-time and delayed equities, indexes, ETPs and options (Nasdaq Cloud Data Service, OAuth client-credentials, customer-specific base URL), and a Kafka-based Streaming API delivered through first-party Java and Python SDKs.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nasdaq.png
layout: provider
modified: '2026-10-19'
name: Nasdaq
nav: Providers
network: true
overview: 'Nasdaq is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Cloud Data Service (NCDS) — Kafka Streams, Cloud Data Service (NCDS) REST API, and 2 more. Tagged areas include Data Marketplace, Financial Data, Fortune 1000, Kafka, and Market Data.


  The Nasdaq catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Nasdaq''s developer surface includes authentication, documentation, and 21 more developer resources.'
plans:
- name: Nasdaq Plans Pricing
  plan_count: 0
  slug: nasdaq-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 12
  name: Nasdaq Rate Limits
  slug: nasdaq-rate-limits
rules:
- authorship: generated
  effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Nasdaq — asyncapi rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: nasdaq-asyncapi-spectral-rules
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 46.9
    developer_ergonomics: 45.2
    discoverability: 66.1
    operational_transparency: 60.5
  previous_composite: 40.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 18.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nasdaq/nasdaq-2026-06-20T190000.png
security:
- kind: authentication
  name: Nasdaq Authentication
  slug: nasdaq-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Nasdaq Domain Security
  slug: nasdaq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nasdaq
tags:
- Data Marketplace
- Financial Data
- Fortune 1000
- Kafka
- Market Data
- Stock Exchange
- Streaming
- Financial Services
- Capital Markets
- Economics
website: https://www.nasdaq.com/
---
