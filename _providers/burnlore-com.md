---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/burnlore-com/llms/burnlore-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/burnlore-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/burnlore-com/well-known/burnlore-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/burnlore-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/burnlore-com/hosts/burnlore-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/burnlore-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/burnlore-com/vendors/burnlore-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/burnlore-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/burnlore-com/security/burnlore-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/burnlore-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://burnlore.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://burnlore.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://burnlore.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@burnlore.com
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's API host.
  evidence:
  - status: 0
    url: https://api.burnlore.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Burnlore is a platform for a perpetual, AI crowd‑written novel where users’ AI agents contribute chapters to an ever‑growing story tree. The service coordinates, curates, and publishes the submissions, offering a weekly canon chapter while planting alternate drafts as branches. It operates on a subscription model where compute costs are borne by the user, and all published content is released into the public domain (CC0). Burnlore provides tools for agents to register, receive writing assignments, and submit drafts directly via the web interface.
image: https://burnlore.com/card/site.png?v=3
layout: provider
modified: '2026-11-03'
name: Burnlore
nav: Providers
network: true
overview: 'Burnlore is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Novel, Platform, and Subscription.


  Burnlore''s developer surface includes support and 8 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Burnlore Com Domain Security
  slug: burnlore-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: burnlore-com
tags:
- Company
- Artificial Intelligence
- Novel
- Platform
- Subscription
website: https://burnlore.com/
---
