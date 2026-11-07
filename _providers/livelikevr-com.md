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
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://90phutzal.tv/security-policy
- group: auth
  href: https://artifacts.apis.io/livelikevr-com/well-known/livelikevr-com-90phutzal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/livelikevr-com-90phutzal-security.txt
- group: agent
  href: https://artifacts.apis.io/livelikevr-com/well-known/livelikevr-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/livelikevr-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/livelikevr-com/hosts/livelikevr-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/livelikevr-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/livelikevr-com/vendors/livelikevr-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/livelikevr-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/livelikevr-com/security/livelikevr-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/livelikevr-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/livelikevr-com/security/livelikevr-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/livelikevr-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://livelikevr.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://livelikevr.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: 'LiveLike is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by techstars) and added to the network as a stub for full-pipeline profiling.'
image: https://cdn.90phutzal.tv/2022/10/logo-90phut-tv-truc-tiep-bong-da.jpg
layout: provider
modified: '2026-10-24'
name: LiveLike
nav: Providers
network: true
overview: LiveLike is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 9
score:
  band: minimal
  composite: 3.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 30.4
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 3.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/livelikevr-com/livelikevr-com-2026-11-03T135008.png
security:
- kind: domain-security
  name: Livelikevr Com Domain Security
  slug: livelikevr-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Livelikevr Com Vulnerability Disclosure
  slug: livelikevr-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: livelikevr-com
tags:
- Company
website: https://livelikevr.com/
---
