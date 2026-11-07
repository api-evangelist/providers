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
  href: https://artifacts.apis.io/wearecurie-ai/hosts/wearecurie-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wearecurie-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/wearecurie-ai/vendors/wearecurie-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wearecurie-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/wearecurie-ai/security/wearecurie-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wearecurie-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wearecurie.ai/
coverage:
  checked: '2026-10-29'
  detail: The provider's website requires login, returning a private site page (401) and no public documentation or API specifications are accessible.
  evidence:
  - status: 401
    url: https://www.wearecurie.ai/
  reason: customer-only-docs
  state: gated
created: '2026-10-28'
description: 'Curie is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by sequoia-capital) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-28'
name: Curie
nav: Providers
network: true
overview: Curie is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 19
score:
  band: minimal
  composite: 1.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 26.8
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 1.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Wearecurie Ai Domain Security
  slug: wearecurie-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wearecurie-ai
tags:
- Company
website: https://www.wearecurie.ai/
---
