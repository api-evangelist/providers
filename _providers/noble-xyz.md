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
- group: other
  href: https://artifacts.apis.io/noble-xyz/vendors/noble-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/noble-xyz-vendors.yml
- group: agent
  href: https://artifacts.apis.io/noble-xyz/llms/noble-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/noble-xyz-llms.txt
- group: other
  href: https://artifacts.apis.io/noble-xyz/hosts/noble-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/noble-xyz-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://noble.xyz/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://noble.xyz/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://noble.xyz/blog/orbiter
- group: docs
  title: ''
  type: Documentation
  url: https://docs.noble.xyz/
- group: auth
  href: https://artifacts.apis.io/noble-xyz/security/noble-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/noble-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.noble.xyz
coverage:
  checked: '2026-10-24'
  detail: The documentation site is a JavaScript‑rendered Framer site with no machine‑readable spec discovered.
  evidence:
  - status: 200
    url: https://noble.xyz/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: 'Noble is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by paradigm, polychain) and added to the network as a stub for full-pipeline profiling.'
image: https://framerusercontent.com/images/3pMcA54QM84UXNz7rhqC4IPZ0.jpg
layout: provider
modified: '2026-10-23'
name: Noble
nav: Providers
network: true
overview: 'Noble is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Stablecoins, Infrastructure, and Payments.


  Noble''s developer surface includes engineering blog, documentation, and 7 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 37.5
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 8.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/noble-xyz/noble-xyz-2026-11-03T140235.png
security:
- kind: domain-security
  name: Noble Xyz Domain Security
  slug: noble-xyz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: noble-xyz
tags:
- Stablecoins
- Infrastructure
- Payments
website: https://www.noble.xyz
---
