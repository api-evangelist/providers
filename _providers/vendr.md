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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Vendr Agentic Access
  operation_count: 6
  slug: vendr-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- description: The Vendr Model Context Protocol (MCP) server exposes Vendr pricing intelligence to AI agents via the MCP standard. It provides tools for searching the product catalog, retrieving custom price estimat
  name: Vendr MCP Server
  slug: vendr-mcp
- description: Search and retrieve software product catalog data
  name: Vendr Catalog API
  slug: vendr-catalog-api
- description: Fair price estimates and negotiation insights
  name: Vendr Pricing API
  slug: vendr-pricing-api
- description: Define and submit purchase scope requirements
  name: Vendr Scope API
  slug: vendr-scope-api
- description: Subscribe to and manage event notifications
  name: Vendr Webhooks API
  slug: vendr-webhooks-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vendr OpenPrice Catalog API
  slug: open-vendr-catalog-api
- collection_type: open
  name: Vendr OpenPrice Catalog Pricing API
  slug: open-vendr-pricing-api
- collection_type: open
  name: Vendr OpenPrice Catalog Scope API
  slug: open-vendr-scope-api
- collection_type: open
  name: Vendr OpenPrice Catalog Webhooks API
  slug: open-vendr-webhooks-api
- collection_type: open
  name: Vendr OpenPrice API
  slug: open-vendr
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/vendrinc/vendr-mcp/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/vendrinc/vendr-mcp/releases
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vendr-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vendr-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vendr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vendr-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vendr-co
- group: company
  title: ''
  type: Website
  url: https://www.vendr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.vendr.com/docs/introduction
- group: commercial
  title: ''
  type: PricingPage
  url: https://www.vendr.com/pricing-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vendrinc
- group: operate
  title: ''
  type: Support
  url: mailto:developers@vendr.com
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.vendr.com/docs/introduction
- group: auth
  title: ''
  type: Authentication
  url: https://developers.vendr.com/docs/introduction
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/vendrinc/vendr-mcp
- group: company
  title: ''
  type: Blog
  url: https://vendr.com/blog
created: '2026-03-16'
description: Vendr is a SaaS procurement intelligence platform that helps businesses manage software spending through data-driven pricing insights and negotiation guidance. The Vendr API (OpenPrice API) provides access to real contract pricing data from 200,000+ verified software agreements across 20,000+ products, enabling developers to embed fair pricing estimates, negotiation insights, product catalog data, and purchase scope management into their applications.
examples:
- key_count: 2
  name: Vendr Create Webhook Example
  slug: vendr-create-webhook-example
- key_count: 2
  name: Vendr Get Pricing Estimate Example
  slug: vendr-get-pricing-estimate-example
- key_count: 2
  name: Vendr Search Catalog Example
  slug: vendr-search-catalog-example
- key_count: 2
  name: Vendr Submit Scope Example
  slug: vendr-submit-scope-example
finops:
- name: Vendr Finops
  service_category: API
  slug: vendr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vendr.png
json_schemas:
- name: Vendr Catalog Product
  property_count: 7
  slug: vendr-catalog-product
- name: Vendr Pricing Response
  property_count: 7
  slug: vendr-pricing-response
json_structures:
- name: Vendr Pricing Response Structure
  property_count: 0
  slug: vendr-pricing-response-structure
jsonld:
- class_count: 32
  name: Vendr Context
  property_count: 1
  slug: vendr-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Vendr
nav: Providers
network: true
overview: 'Vendr publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Pricing API, Scope API, and 1 more. Tagged areas include Pricing, Procurement, Software-as-a-Service, Software Spend Management, and Negotiation.


  The Vendr catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vendr''s developer surface includes authentication, documentation, support, engineering blog, and 12 more developer resources.'
plans:
- name: Vendr Plans Pricing
  plan_count: 3
  slug: vendr-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Vendr Rate Limits
  slug: vendr-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Vendr API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vendr-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Vendr API Rules
  rule_count: 11
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 7
  slug: vendr-rules
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 16
    catalog_gap: 41.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 28.8
    contract_quality: 70.4
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 25.0
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vendr/refs/heads/main/screenshots/vendr-2026-06-20T200912.png
security:
- kind: authentication
  name: Vendr Authentication
  slug: vendr-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Vendr Domain Security
  slug: vendr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Vendr Trust Center
  slug: vendr-trust-center
  summary_line: SOC 2, GDPR
slug: vendr
tags:
- Pricing
- Procurement
- Software-as-a-Service
- Software Spend Management
- Negotiation
website: https://www.vendr.com/
---
