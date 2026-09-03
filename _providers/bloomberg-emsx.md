---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
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
    error_semantics: verified
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
  score: 25.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Bloomberg Emsx Agentic Access
  operation_count: 19
  slug: bloomberg-emsx-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 1
apis:
- description: API for order creation, routing, management and execution monitoring through Bloomberg EMSX platform. Supports order lifecycle management, broker selection, route management, fill tracking, and real-t
  name: Bloomberg EMSX Trading API
  slug: bloomberg-emsx-trading-api
- baseURL: https://api.bloomberg.com/emsxapi/v1
  baseurl_source: spec
  description: Query available brokers and broker strategies
  name: Bloomberg EMSX Brokers API
  slug: bloomberg-emsx-brokers-api
- baseURL: https://api.bloomberg.com/emsxapi/v1
  baseurl_source: spec
  description: Retrieve available order and route fields
  name: Bloomberg EMSX Field Lists API
  slug: bloomberg-emsx-field-lists-api
- baseURL: https://api.bloomberg.com/emsxapi/v1
  baseurl_source: spec
  description: Query and monitor trade executions and fills
  name: Bloomberg EMSX Fills API
  slug: bloomberg-emsx-fills-api
- baseURL: https://api.bloomberg.com/emsxapi/v1
  baseurl_source: spec
  description: Create, modify, delete, and query trading orders
  name: Bloomberg EMSX Orders API
  slug: bloomberg-emsx-orders-api
- baseURL: https://api.bloomberg.com/emsxapi/v1
  baseurl_source: spec
  description: Create, modify, delete, and manage order routes to brokers
  name: Bloomberg EMSX Routes API
  slug: bloomberg-emsx-routes-api
- baseURL: https://api.bloomberg.com/emsxapi/v1
  baseurl_source: spec
  description: Manage EMSX trading teams
  name: Bloomberg EMSX Teams API
  slug: bloomberg-emsx-teams-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bloomberg EMSX Trading Brokers API
  slug: open-bloomberg-emsx-brokers-api
- collection_type: open
  name: Bloomberg EMSX Trading Brokers Field Lists API
  slug: open-bloomberg-emsx-field-lists-api
- collection_type: open
  name: Bloomberg EMSX Trading Brokers Fills API
  slug: open-bloomberg-emsx-fills-api
- collection_type: open
  name: Bloomberg EMSX Trading Brokers Orders API
  slug: open-bloomberg-emsx-orders-api
- collection_type: open
  name: Bloomberg EMSX Trading Brokers Routes API
  slug: open-bloomberg-emsx-routes-api
- collection_type: open
  name: Bloomberg EMSX Trading Brokers Teams API
  slug: open-bloomberg-emsx-teams-api
- collection_type: open
  name: Bloomberg EMSX Trading API
  slug: open-bloomberg-emsx-trading
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bloomberg-emsx-capability-edges.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/bloomberg/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bloomberg-emsx-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bloomberg-emsx-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-emsx-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bloomberg-emsx-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bloomberg.com/professional/support/api-library/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
created: '2024-01-01'
description: Bloomberg Execution Management System (EMSX) API provides programmatic access to Bloomberg's order and execution management platform for trading operations.
finops:
- name: Bloomberg Emsx Finops
  service_category: API
  slug: bloomberg-emsx-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-emsx.png
json_schemas:
- name: Bloomberg EMSX Fill
  property_count: 17
  slug: bloomberg-emsx-fill
- name: Bloomberg EMSX Order
  property_count: 23
  slug: bloomberg-emsx-order
- name: Bloomberg EMSX Route
  property_count: 24
  slug: bloomberg-emsx-route
jsonld:
- class_count: 0
  name: Bloomberg Emsx Context
  property_count: 6
  slug: bloomberg-emsx-context
layout: provider
modified: '2026-08-27'
name: Bloomberg EMSX
nav: Providers
network: true
overview: 'Bloomberg EMSX publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Brokers API, Field Lists API, Fills API, and 3 more. Tagged areas include Bloomberg, Execution Management, Financial-Services, Order Management, and Trading.


  The Bloomberg EMSX catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bloomberg EMSX''s developer surface includes authentication, developer portal, documentation, support, and 7 more developer resources.'
plans:
- name: Bloomberg Emsx Plans Pricing
  plan_count: 3
  slug: bloomberg-emsx-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Bloomberg Emsx Rate Limits
  slug: bloomberg-emsx-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Bloomberg EMSX API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bloomberg-emsx-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 13
    catalog_gap: 70.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 63.8
    developer_ergonomics: 42.9
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 61.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-emsx/refs/heads/main/screenshots/bloomberg-emsx-2026-07-25T203400.png
security:
- kind: authentication
  name: Bloomberg Emsx Authentication
  slug: bloomberg-emsx-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bloomberg Emsx Domain Security
  slug: bloomberg-emsx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bloomberg Emsx Vulnerability Disclosure
  slug: bloomberg-emsx-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bloomberg-emsx
tags:
- Bloomberg
- Execution Management
- Financial-Services
- Order Management
- Trading
website: https://www.bloomberg.com/professional/
---
