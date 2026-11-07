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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/osmo-ai/hosts/osmo-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/osmo-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/osmo-ai/vendors/osmo-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/osmo-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.osmo.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.osmo.ai/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.osmo.ai/blog
- group: auth
  href: https://artifacts.apis.io/osmo-ai/security/osmo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/osmo-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://osmo.ai/
coverage:
  checked: '2026-10-22'
  detail: Home page loads via Cloudflare and serves HTML with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.osmo.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Osmo provides an AI‑driven platform that lets brands create custom fine‑fragrance formulas from text, images or concepts. The service includes formulation, sampling, iteration with fragrance advisors, and end‑to‑end production and packaging for perfumes and eau de parfums, targeting brand builders from indie labels to global CPG firms.
layout: provider
modified: '2026-10-22'
name: Osmo
nav: Providers
network: true
overview: 'Osmo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fragrance, Artificial Intelligence, Product Development, Manufacturing, and Packaging.


  Osmo''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/osmo-ai/osmo-ai-2026-11-03T140748.png
security:
- kind: domain-security
  name: Osmo Ai Domain Security
  slug: osmo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: osmo-ai
tags:
- Fragrance
- Artificial Intelligence
- Product Development
- Manufacturing
- Packaging
website: https://osmo.ai/
---
