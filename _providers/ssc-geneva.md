---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Ssc Geneva Agentic Access
  operation_count: 7
  slug: ssc-geneva-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.ssctech.example.com/geneva/v1
  baseurl_source: declared
  description: Investor accounts and capital activity
  name: SS&C Geneva Investors API
  slug: ssc-geneva-investors-api
- baseURL: https://api.ssctech.example.com/geneva/v1
  baseurl_source: declared
  description: Net Asset Value calculation and reporting
  name: SS&C Geneva NAV API
  slug: ssc-geneva-nav-api
- baseURL: https://api.ssctech.example.com/geneva/v1
  baseurl_source: declared
  description: Portfolio and fund management
  name: SS&C Geneva Portfolios API
  slug: ssc-geneva-portfolios-api
- baseURL: https://api.ssctech.example.com/geneva/v1
  baseurl_source: declared
  description: Portfolio positions and holdings
  name: SS&C Geneva Positions API
  slug: ssc-geneva-positions-api
- baseURL: https://api.ssctech.example.com/geneva/v1
  baseurl_source: declared
  description: Trade capture and processing
  name: SS&C Geneva Trades API
  slug: ssc-geneva-trades-api
artifact_total: 30
collections:
- collection_type: postman
  name: SS&C Geneva Fund Accounting Investors API
  slug: postman-ssc-geneva-investors-api
- collection_type: postman
  name: SS&C Geneva Fund Accounting Investors NAV API
  slug: postman-ssc-geneva-nav-api
- collection_type: postman
  name: SS&C Geneva Fund Accounting Investors Portfolios API
  slug: postman-ssc-geneva-portfolios-api
- collection_type: postman
  name: SS&C Geneva Fund Accounting Investors Positions API
  slug: postman-ssc-geneva-positions-api
- collection_type: postman
  name: SS&C Geneva Fund Accounting Investors Trades API
  slug: postman-ssc-geneva-trades-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SS&C Geneva Fund Accounting API
  slug: open-ssc-geneva-fund-accounting
- collection_type: open
  name: SS&C Geneva Fund Accounting Investors API
  slug: open-ssc-geneva-investors-api
- collection_type: open
  name: SS&C Geneva Fund Accounting Investors NAV API
  slug: open-ssc-geneva-nav-api
- collection_type: open
  name: SS&C Geneva Fund Accounting Investors Portfolios API
  slug: open-ssc-geneva-portfolios-api
- collection_type: open
  name: SS&C Geneva Fund Accounting Investors Positions API
  slug: open-ssc-geneva-positions-api
- collection_type: open
  name: SS&C Geneva Fund Accounting Investors Trades API
  slug: open-ssc-geneva-trades-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ssc-geneva/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ssc-geneva-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ssc-geneva-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ssc-geneva-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ssc-advent
- group: company
  title: ''
  type: Website
  url: https://www.ssctech.com/
- group: start
  title: ''
  type: Portal
  url: https://www.ssctech.com/products
- group: company
  title: ''
  type: Blog
  url: https://www.ssctech.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.ssctech.com/about/support-client-portals
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ssctech.com/about/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://www.ssctech.com/resources
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/openapi/ssc-geneva-fund-accounting-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/json-schema/ssc-geneva-portfolio-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/json-structure/ssc-geneva-fund-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/json-ld/ssc-geneva-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/rules/ssc-geneva-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/vocabulary/ssc-geneva-vocabulary.yml
created: '2026-03-18'
description: SS&C Geneva is an enterprise-grade fund accounting and portfolio management platform for asset managers, hedge funds, and fund administrators. Geneva provides APIs for NAV calculation, trade processing, investor accounting, position management, and regulatory reporting across multi-asset portfolios including equities, fixed income, derivatives, and alternative investments.
examples:
- key_count: 4
  name: Ssc Geneva Get Nav Example
  slug: ssc-geneva-get-nav-example
- key_count: 4
  name: Ssc Geneva List Portfolios Example
  slug: ssc-geneva-list-portfolios-example
finops:
- name: Ssc Geneva Finops
  service_category: API
  slug: ssc-geneva-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ssc-geneva.png
json_schemas:
- name: SS&C Geneva Portfolio
  property_count: 16
  slug: ssc-geneva-portfolio
json_structures:
- name: Ssc Geneva Fund Structure
  property_count: 0
  slug: ssc-geneva-fund-structure
jsonld:
- class_count: 23
  name: Ssc Geneva Context
  property_count: 12
  slug: ssc-geneva-context
layout: provider
modified: '2026-05-19'
name: SS&C Geneva
nav: Providers
network: true
overview: 'SS&C Geneva publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Investors API, NAV API, Portfolios API, and 2 more. Tagged areas include Fund Accounting, Asset Management, Portfolio-Management, Financial-Services, and Hedge Funds.


  The SS&C Geneva catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SS&C Geneva''s developer surface includes authentication, developer portal, engineering blog, support, documentation, and 12 more developer resources.'
plans:
- name: Ssc Geneva Plans Pricing
  plan_count: 3
  slug: ssc-geneva-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Ssc Geneva Rate Limits
  slug: ssc-geneva-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SS&C Geneva API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ssc-geneva-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: SS&C Geneva API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 1
    info: 0
    warn: 5
  slug: ssc-geneva-rules
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 42.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 65.6
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/screenshots/ssc-geneva-2026-06-20T194436.png
security:
- kind: authentication
  name: Ssc Geneva Authentication
  slug: ssc-geneva-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Ssc Geneva Domain Security
  slug: ssc-geneva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ssc-geneva
tags:
- Fund Accounting
- Asset Management
- Portfolio-Management
- Financial-Services
- Hedge Funds
- NAV Calculation
website: https://www.ssctech.com/
---
