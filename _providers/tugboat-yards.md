---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Publisher-scoped REST API for the Tugboat audience-funding platform, covering API-key verification, pages, offers and offer issues, subscribers, orders, the deprecated WePay checkouts interface, per-k
  name: Tugboat Yards API (defunct)
  slug: tugboat-yards-api-defunct
artifact_total: 4
asyncapis:
- description: ''
  name: Tugboat Yards Webhooks
  slug: tugboat-yards-webhooks
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tugboat-yards-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/tugboat-yards-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tugboat-yards-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tugboat-yards-domain-security.yml
created: '2026-07-17'
description: Tugboat Yards Inc. was a San Francisco startup (product name "Tugboat") that built tools for independent publishers and media creators to raise direct financial support from their audiences, and was backed by a16z. The company is defunct - the product was live circa 2012-2014, the tugboatyards.com domain was reduced to a registrar parking page by 2016, and as of July 2026 the domain publishes no A/AAAA records. It did operate a real, documented publisher API at api.tugboatyards.com (key-check, pages, offers, subscribers, orders, checkout configuration, placements, and Instant Payment Notification webhooks) with a first-party Python client, pytugboat. That surface is offline; the artifacts in this repository are a historical record recovered from the provider's own 2015 documentation via the Wayback Machine and from the still-live pytugboat docs on Read the Docs. This profile is preserved as part of the a16z venture-portfolio graph in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tugboat-yards.png
layout: provider
modified: '2026-07-21'
name: Tugboat Yards
nav: Providers
network: true
overview: 'Tugboat Yards publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Publishing, Crowdfunding, and Audience Funding.


  The Tugboat Yards catalog on APIs.io includes 1 event-driven AsyncAPI specification.'
random_paper: 6
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 21.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: authentication
  name: Tugboat Yards Authentication
  slug: tugboat-yards-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tugboat Yards Domain Security
  slug: tugboat-yards-domain-security
  summary_line: no transport/DNS hardening detected
slug: tugboat-yards
tags:
- Company
- Media
- Publishing
- Crowdfunding
- Audience Funding
- Payments
- Defunct
---
