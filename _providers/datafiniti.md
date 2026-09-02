---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Datafiniti Agentic Access
  operation_count: 5
  slug: datafiniti-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 1
apis:
- description: Access a large catalog of business listings aggregated from hundreds of online directories and review websites, integrated with firmographics and reviews. Over 131 million business records available.
  name: Datafiniti Business Data API
  slug: business-data-api
- description: Access millions of product records spanning major retailers, brands, and categories including detailed product information, pricing data, and reviews. Over 506 million product records available.
  name: Datafiniti Product Data API
  slug: product-data-api
- description: Access a large catalog of real estate listings from dozens of websites, integrated with pricing data, amenities, and reviews. Over 205 million property records available.
  name: Datafiniti Property Data API
  slug: property-data-api
- description: Access people data records aggregated from public web sources. Over 4 million people records available.
  name: Datafiniti People Data API
  slug: people-data-api
- description: The Authentication API from Datafiniti — 1 operation(s) for authentication.
  name: Datafiniti Authentication API
  slug: datafiniti-authentication-api
- description: The Businesses API from Datafiniti — 1 operation(s) for businesses.
  name: Datafiniti Businesses API
  slug: datafiniti-businesses-api
- description: The People API from Datafiniti — 1 operation(s) for people.
  name: Datafiniti People API
  slug: datafiniti-people-api
- description: The Products API from Datafiniti — 1 operation(s) for products.
  name: Datafiniti Products API
  slug: datafiniti-products-api
- description: The Properties API from Datafiniti — 1 operation(s) for properties.
  name: Datafiniti Properties API
  slug: datafiniti-properties-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Datafiniti API
  slug: open-datafiniti-api
- collection_type: open
  name: Datafiniti Authentication API
  slug: open-datafiniti-authentication-api
- collection_type: open
  name: Datafiniti Authentication Businesses API
  slug: open-datafiniti-businesses-api
- collection_type: open
  name: Datafiniti Authentication People API
  slug: open-datafiniti-people-api
- collection_type: open
  name: Datafiniti Authentication Products API
  slug: open-datafiniti-products-api
- collection_type: open
  name: Datafiniti Authentication Properties API
  slug: open-datafiniti-properties-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/datafiniti-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datafiniti-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/datafiniti-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datafiniti
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/datafiniti
- group: company
  title: ''
  type: Website
  url: https://www.datafiniti.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datafiniti.co/docs/api-introduction
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.datafiniti.co
- group: start
  title: ''
  type: Signup
  url: https://portal.datafiniti.co/sign-up
- group: start
  title: ''
  type: Login
  url: https://portal.datafiniti.co
- group: company
  title: ''
  type: Blog
  url: https://blog.datafiniti.co
- group: design
  title: ''
  type: JSONLD
  url: json-ld/datafiniti-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/datafiniti-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/datafiniti-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.datafiniti.co/llms.txt
created: '2026-03-26'
description: Datafiniti is a Data as a Service (DaaS) provider that collects, organizes, and standardizes large-scale data from the public web, delivering ready-to-use datasets for property, people, business, and product data through their API, web portal, and bulk downloads.
finops:
- name: Datafiniti Finops
  service_category: Data as a Service
  slug: datafiniti-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datafiniti.png
json_schemas:
- name: AuthRequest
  property_count: 2
  slug: datafiniti-authrequest
- name: AuthResponse
  property_count: 1
  slug: datafiniti-authresponse
- name: SearchRequest
  property_count: 5
  slug: datafiniti-searchrequest
- name: SearchResponse
  property_count: 5
  slug: datafiniti-searchresponse
- name: Datafiniti Search Request
  property_count: 5
  slug: search-request
json_structures:
- name: Datafiniti Structure
  property_count: 0
  slug: datafiniti-structure
jsonld:
- class_count: 0
  name: Datafiniti Context
  property_count: 5
  slug: datafiniti-context
layout: provider
modified: '2026-05-19'
name: Datafiniti
nav: Providers
network: true
overview: 'Datafiniti publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Businesses API, People API, and 2 more. Tagged areas include Business Data, Data Aggregation, Data as a Service, People Data, and Product Data.


  The Datafiniti catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Datafiniti''s developer surface includes authentication, documentation, signup flow, engineering blog, and 11 more developer resources.'
plans:
- name: Datafiniti Plans Pricing
  plan_count: 3
  slug: datafiniti-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Datafiniti Rate Limits
  slug: datafiniti-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Datafiniti API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: datafiniti-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Datafiniti API Rules
  rule_count: 5
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 1
  slug: datafiniti-rules
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 54.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 28.8
    contract_quality: 59.5
    developer_ergonomics: 27.4
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datafiniti/refs/heads/main/screenshots/datafiniti-2026-06-20T175637.png
security:
- kind: authentication
  name: Datafiniti Authentication
  slug: datafiniti-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Datafiniti Domain Security
  slug: datafiniti-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datafiniti
tags:
- Business Data
- Data Aggregation
- Data as a Service
- People Data
- Product Data
- Property Data
website: https://www.datafiniti.co
---
