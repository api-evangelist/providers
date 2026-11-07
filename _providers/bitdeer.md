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
- group: auth
  href: https://artifacts.apis.io/bitdeer/well-known/bitdeer-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bitdeer-status-security.txt
- group: agent
  href: https://artifacts.apis.io/bitdeer/well-known/bitdeer-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bitdeer-well-known.yml
- group: other
  href: https://artifacts.apis.io/bitdeer/hosts/bitdeer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitdeer-hosts.yml
- group: other
  href: https://artifacts.apis.io/bitdeer/vendors/bitdeer-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitdeer-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bitdeer.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.bitdeer.com/news
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.zendesk.com/documentation/developer-tools/getting-started/getting-a-trial-or-sponsored-account-for-development/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zendesk.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bitdeer.ai
- group: auth
  href: https://artifacts.apis.io/bitdeer/security/bitdeer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitdeer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bitdeer.com/
- group: operate
  title: ''
  type: Support
  url: https://bitdeersupport.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.bitdeer.ai/en/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://www.bitdeer.com/sealminer/roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bitdeer.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bitdeer.com/privacy-policy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://api.zendesk.com/mcp
  - status: 200
    url: https://www.bitdeer.com/
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: 'BitDeer (NASDAQ: BTDR) is a world-leading technology company providing enterprise high-performance computing (HPC), AI cloud infrastructure, SEALMINER equipment, and sustainable Bitcoin mining solutions.'
image: https://oss.bitdeer.tech/202603/a6fc3edfefe382db90bda1ffe51b0696.png
layout: provider
modified: '2026-10-25'
name: BitDeer
nav: Providers
network: true
overview: 'BitDeer is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, HPC, Bitcoin, and Mining.


  BitDeer''s developer surface includes getting-started guide, documentation, support, engineering blog, and 12 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 49.1
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bitdeer/bitdeer-2026-11-03T121757.png
security:
- kind: domain-security
  name: Bitdeer Domain Security
  slug: bitdeer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bitdeer
tags:
- Company
- Cloud
- HPC
- Bitcoin
- Mining
website: https://www.bitdeer.com/
---
