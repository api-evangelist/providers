---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API providing trust scoring and MCP endpoint monitoring.
  name: Dominion Observatory API
  slug: dominion-observatory-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/dominionobservatory-com/plans/dominionobservatory-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dominionobservatory-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/dominionobservatory-com/authentication/dominionobservatory-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dominionobservatory-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dominionobservatory-com/conformance/dominionobservatory-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dominionobservatory-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dominionobservatory-com/llms/dominionobservatory-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dominionobservatory-com-llms.txt
- group: other
  href: https://artifacts.apis.io/dominionobservatory-com/a2a/dominionobservatory-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dominionobservatory-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/dominionobservatory-com/well-known/dominionobservatory-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dominionobservatory-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dominionobservatory-com/hosts/dominionobservatory-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dominionobservatory-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dominionobservatory-com/vendors/dominionobservatory-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dominionobservatory-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/dominionobservatory-com/packages/dominionobservatory-com-packages.yml
  title: ''
  type: Packages
  url: packages/dominionobservatory-com-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://dominionobservatory.com/baselines/security
- group: build
  title: ''
  type: SDKs
  url: https://dominionobservatory.com/sdk
- group: commercial
  title: ''
  type: Pricing
  url: https://dominionobservatory.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://dominionobservatory.com/baselines/media
- group: start
  title: ''
  type: GettingStarted
  url: https://dominionobservatory.com/get-started
- group: company
  title: ''
  type: Blog
  url: https://dominionobservatory.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://dominionobservatory.com/docs
- group: auth
  href: https://artifacts.apis.io/dominionobservatory-com/security/dominionobservatory-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dominionobservatory-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dominionobservatory.com/
created: '2026-11-05'
description: Dominion Observatory provides a neutral, third‑party layer that measures MCP server behavior at runtime – uptime, success rate, latency from real agent traffic – and displays “unrated” when no data exists. It offers free look‑ups of any server without requiring an API key, delivering trust scores and signed diligence receipts for the Agent Economy.
image: https://dominionobservatory.com/og-image.png
layout: provider
modified: '2026-11-05'
name: Dominion Observatory
nav: Providers
network: true
overview: 'Dominion Observatory is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include MCP, Trust, Monitoring, Compliance, and Gateways.


  Dominion Observatory''s developer surface includes authentication, pricing, getting-started guide, engineering blog, API reference, and 13 more developer resources.'
plans:
- name: Dominionobservatory Com Plans Pricing
  plan_count: 5
  slug: dominionobservatory-com-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 67.9
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dominionobservatory Com Authentication
  slug: dominionobservatory-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dominionobservatory Com Domain Security
  slug: dominionobservatory-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dominionobservatory-com
tags:
- MCP
- Trust
- Monitoring
- Compliance
- Gateways
website: https://dominionobservatory.com/
---
