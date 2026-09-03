---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Prodigi Agentic Access
  operation_count: 10
  slug: prodigi-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.prodigi.com/v4.0
  baseurl_source: declared
  description: Create, retrieve, list, and act on print orders.
  name: Prodigi Orders API
  slug: prodigi-orders-api
- baseURL: https://api.prodigi.com/v4.0
  baseurl_source: declared
  description: Query the product catalogue by SKU.
  name: Prodigi Products API
  slug: prodigi-products-api
- baseURL: https://api.prodigi.com/v4.0
  baseurl_source: declared
  description: Request pricing and shipping breakdowns before ordering.
  name: Prodigi Quotes API
  slug: prodigi-quotes-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Prodigi Print Orders API
  slug: open-prodigi-orders-api
- collection_type: open
  name: Prodigi Print Orders Products API
  slug: open-prodigi-products-api
- collection_type: open
  name: Prodigi Print Orders Quotes API
  slug: open-prodigi-quotes-api
- collection_type: open
  name: Prodigi Print API
  slug: open-prodigi
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/prodigi-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prodigi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prodigi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prodigi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Prodigi-Group
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prodigi
- group: company
  title: ''
  type: Website
  url: https://www.prodigi.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.prodigi.com/print-api/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/prodigi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prodigi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/prodigi-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.prodigi.com/blog/
created: '2026-06-25'
description: Prodigi is a global print-on-demand and dropshipping platform that connects merchants to a worldwide network of print labs. The Prodigi Print API (v4.0) lets developers create and manage print orders, fetch real-time quotes, and query the product catalogue, with print and shipping fulfilled at wholesale prices direct from the manufacturer.
finops:
- name: Prodigi Finops
  service_category: Print and Fulfillment
  slug: prodigi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prodigi.png
layout: provider
modified: '2026-06-25'
name: Prodigi
nav: Providers
network: true
overview: 'Prodigi publishes 3 APIs on the [APIs.io](https://apis.io/) network: Orders API, Products API, and Quotes API. Tagged areas include Print on Demand, Printing, Dropshipping, Fulfillment, and E-Commerce.


  Prodigi''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Prodigi Plans Pricing
  plan_count: 2
  slug: prodigi-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Prodigi Rate Limits
  slug: prodigi-rate-limits
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 54.9
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prodigi/refs/heads/main/screenshots/prodigi-2026-09-02T152115.png
security:
- kind: authentication
  name: Prodigi Authentication
  slug: prodigi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Prodigi Domain Security
  slug: prodigi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: prodigi
tags:
- Print on Demand
- Printing
- Dropshipping
- Fulfillment
- E-Commerce
website: https://www.prodigi.com
---
