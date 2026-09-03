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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Onomondo Agentic Access
  operation_count: 28
  slug: onomondo-agentic-access
  summary_line: 28 operations · 14 acting
api_count: 1
apis:
- baseURL: https://api.onomondo.com
  baseurl_source: declared
  description: Manage cloud connectors that forward device traffic.
  name: Onomondo Connectors API
  slug: onomondo-connectors-api
- baseURL: https://api.onomondo.com
  baseurl_source: declared
  description: Manage network allow-lists (whitelists) of MCC/MNC entries.
  name: Onomondo Network Lists API
  slug: onomondo-network-lists-api
- baseURL: https://api.onomondo.com
  baseurl_source: declared
  description: Manage and inspect SIMs in your fleet.
  name: Onomondo SIMs API
  slug: onomondo-sims-api
- baseURL: https://api.onomondo.com
  baseurl_source: declared
  description: Send SMS to devices and retrieve SMS usage.
  name: Onomondo SMS API
  slug: onomondo-sms-api
- baseURL: https://api.onomondo.com
  baseurl_source: declared
  description: Search organization tags used to group SIMs.
  name: Onomondo Tags API
  slug: onomondo-tags-api
- baseURL: https://api.onomondo.com
  baseurl_source: declared
  description: Retrieve data usage for SIMs and tags.
  name: Onomondo Usage API
  slug: onomondo-usage-api
- baseURL: https://api.onomondo.com
  baseurl_source: declared
  description: Subscribe to SIM events delivered as HTTP POST callbacks.
  name: Onomondo Webhooks API
  slug: onomondo-webhooks-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Onomondo Connectors API
  slug: open-onomondo-connectors-api
- collection_type: open
  name: Onomondo Connectors Network Lists API
  slug: open-onomondo-network-lists-api
- collection_type: open
  name: Onomondo Connectors SIMs API
  slug: open-onomondo-sims-api
- collection_type: open
  name: Onomondo Connectors SMS API
  slug: open-onomondo-sms-api
- collection_type: open
  name: Onomondo Connectors Tags API
  slug: open-onomondo-tags-api
- collection_type: open
  name: Onomondo Connectors Usage API
  slug: open-onomondo-usage-api
- collection_type: open
  name: Onomondo Connectors Webhooks API
  slug: open-onomondo-webhooks-api
- collection_type: open
  name: Onomondo API
  slug: open-onomondo
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/onomondo-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/onomondo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onomondo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/onomondo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onomondo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onomondo
- group: company
  title: ''
  type: Website
  url: https://onomondo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.onomondo.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/onomondo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/onomondo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/onomondo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://onomondo.com/blog/feed/
created: '2026-06-21'
description: Onomondo is a global IoT cellular-connectivity platform that connects devices to 680+ networks across 180+ countries using a single core network. The Onomondo API (https://api.onomondo.com) provides programmatic management of SIMs, data usage, network lists, SMS, webhooks, connectors, and tags with Bearer API-key authentication.
finops:
- name: Onomondo Finops
  service_category: IoT and Connectivity
  slug: onomondo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onomondo.png
layout: provider
modified: '2026-06-21'
name: Onomondo
nav: Providers
network: true
overview: 'Onomondo publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Connectors API, Network Lists API, SIMs API, and 4 more. Tagged areas include IoT, Connectivity, Cellular, SIM, and Telecom.


  Onomondo''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Onomondo Plans Pricing
  plan_count: 5
  slug: onomondo-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Onomondo Rate Limits
  slug: onomondo-rate-limits
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.0
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onomondo/refs/heads/main/screenshots/onomondo-2026-08-07T190606.png
security:
- kind: authentication
  name: Onomondo Authentication
  slug: onomondo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Onomondo Domain Security
  slug: onomondo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: onomondo
tags:
- IoT
- Connectivity
- Cellular
- SIM
- Telecom
website: https://onomondo.com/
---
