---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Echo Global Agentic Access
  operation_count: 14
  slug: echo-global-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 3
apis:
- description: GET and POST to shipment documents endpoints.
  name: Echo Global Logistics documents API
  slug: echo-global-documents-api
- description: The health API from Echo Global Logistics — 1 operation(s) for health.
  name: Echo Global Logistics health API
  slug: echo-global-health-api
- description: GET to ping endpoints.
  name: Echo Global Logistics ping API
  slug: echo-global-ping-api
- description: GET and POST to query shipment details endpoints.
  name: Echo Global Logistics query API
  slug: echo-global-query-api
- description: Used for creating and retrieving quotes.
  name: Echo Global Logistics quotes API
  slug: echo-global-quotes-api
- description: GET and POST to shipment rates endpoints.
  name: Echo Global Logistics rates API
  slug: echo-global-rates-api
- description: GET and POST to shipment endpoints.
  name: Echo Global Logistics shipments API
  slug: echo-global-shipments-api
- description: Obtaining and using tokens
  name: Echo Global Logistics token API
  slug: echo-global-token-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Echo Authorizer documents API
  slug: open-echo-global-documents-api
- collection_type: open
  name: Echo Authorizer documents health API
  slug: open-echo-global-health-api
- collection_type: open
  name: Echo Authorizer documents ping API
  slug: open-echo-global-ping-api
- collection_type: open
  name: Echo Authorizer documents query API
  slug: open-echo-global-query-api
- collection_type: open
  name: Echo Authorizer documents quotes API
  slug: open-echo-global-quotes-api
- collection_type: open
  name: Echo Authorizer documents rates API
  slug: open-echo-global-rates-api
- collection_type: open
  name: Echo Authorizer documents shipments API
  slug: open-echo-global-shipments-api
- collection_type: open
  name: Echo Authorizer documents token API
  slug: open-echo-global-token-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/echo-global-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/echo-global-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/echo-global-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/echo-global-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/echo-global-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.echo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.echo.com/technology/integrations/echosync/documentation/
- group: company
  title: ''
  type: Blog
  url: https://www.echo.com/resources/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/echo-global-logistics
- group: other
  title: ''
  type: X
  url: https://x.com/echologistics
- group: commercial
  title: ''
  type: Pricing
  url: https://www.echo.com/shippers/get-a-quote/
- group: commercial
  title: ''
  type: Plans
  url: plans/echo-global-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/echo-global-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/echo-global-finops.yml
created: '2026-06-13'
description: Tech-enabled freight brokerage with REST APIs for shipping quotes, booking LTL and FTL shipments, tracking deliveries, and managing carrier relationships. The EchoSync API suite includes the Partner-Connect API for load creation and LTL rating, the Customer API for truckload quoting, the Carrier API for digital freight marketplace access, and an Authorizer API for OAuth 2.0 token management.
examples:
- key_count: 4
  name: Create Ltl Shipment
  slug: create-ltl-shipment
- key_count: 4
  name: Create Truckload Quote
  slug: create-truckload-quote
- key_count: 5
  name: Get Oauth Token
  slug: get-oauth-token
- key_count: 4
  name: Search Available Loads
  slug: search-available-loads
finops:
- name: Echo Global Finops
  service_category: ''
  slug: echo-global-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/echo-global.png
json_schemas:
- name: Load
  property_count: 9
  slug: load
- name: Quote
  property_count: 11
  slug: quote
- name: Shipment
  property_count: 10
  slug: shipment
jsonld:
- class_count: 16
  name: Echo Global Context
  property_count: 0
  slug: echo-global
layout: provider
modified: '2026-06-13'
name: Echo Global Logistics
nav: Providers
network: true
overview: 'Echo Global Logistics publishes 8 APIs on the [APIs.io](https://apis.io/) network, including documents API, health API, ping API, and 5 more. Tagged areas include Freight, Logistics, Shipping, LTL, and Truckload.


  The Echo Global Logistics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Echo Global Logistics'' developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Echo Global Plans Pricing
  plan_count: 3
  slug: echo-global-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Echo Global Rate Limits
  slug: echo-global-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Echo Global Logistics API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: echo-global-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 36.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 61.5
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 31.6
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/echo-global/refs/heads/main/screenshots/echo-global-2026-06-20T180419.png
security:
- kind: authentication
  name: Echo Global Authentication
  slug: echo-global-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Echo Global Domain Security
  slug: echo-global-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Echo Global Vulnerability Disclosure
  slug: echo-global-vulnerability-disclosure
  summary_line: disclosure policy published
slug: echo-global
tags:
- Freight
- Logistics
- Shipping
- LTL
- Truckload
- Freight Brokerage
- Transportation
- Supply Chain
website: https://www.echo.com/
---
