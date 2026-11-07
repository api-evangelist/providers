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
- group: agent
  href: https://artifacts.apis.io/nines-com/llms/nines-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nines-com-llms.txt
- group: other
  href: https://artifacts.apis.io/nines-com/hosts/nines-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nines-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/nines-com/vendors/nines-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nines-com-vendors.yml
- group: build
  title: ''
  type: SDKs
  url: https://sironamedical.com/platform/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sironamedical.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://sironamedical.com/company/press
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sironamedical.com/solutions/developers
- group: company
  title: ''
  type: Blog
  url: https://sironamedical.com/resources/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://sironamedical.com/platform/training
- group: auth
  href: https://artifacts.apis.io/nines-com/security/nines-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nines-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.nines.com
coverage:
  checked: '2026-10-21'
  detail: The provider's website redirects to sironamedical.com which serves only HTML with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://sironamedical.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: 'Nines is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by accel) and added to the network as a stub for full-pipeline profiling.'
image: https://sironamedical.com/share/home.jpg
layout: provider
modified: '2026-10-21'
name: Nines
nav: Providers
network: true
overview: 'Nines is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Nines'' developer surface includes engineering blog, getting-started guide, and 9 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 38.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.4
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nines-com/nines-com-2026-11-03T140221.png
security:
- kind: domain-security
  name: Nines Com Domain Security
  slug: nines-com-domain-security
  summary_line: DMARC
slug: nines-com
tags:
- Company
website: http://www.nines.com
---
