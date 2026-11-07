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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/purespectrum/well-known/purespectrum-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/purespectrum-status-security.txt
- group: auth
  title: ''
  type: Compliance
  url: https://trust.purespectrum.com/
- group: agent
  href: https://artifacts.apis.io/purespectrum/llms/purespectrum-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/purespectrum-llms.txt
- group: agent
  href: https://artifacts.apis.io/purespectrum/well-known/purespectrum-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/purespectrum-well-known.yml
- group: other
  href: https://artifacts.apis.io/purespectrum/hosts/purespectrum-hosts.yml
  title: ''
  type: Hosts
  url: hosts/purespectrum-hosts.yml
- group: other
  href: https://artifacts.apis.io/purespectrum/vendors/purespectrum-vendors.yml
  title: ''
  type: Vendors
  url: vendors/purespectrum-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.purespectrum.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.purespectrum.com/newsroom/
- group: auth
  href: https://artifacts.apis.io/purespectrum/security/purespectrum-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/purespectrum-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/purespectrum/security/purespectrum-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/purespectrum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://purespectrum.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.purespectrum.com/api-integration/
- group: operate
  title: ''
  type: Support
  url: https://purespectrum.helpjuice.com/en_US
- group: company
  title: ''
  type: Blog
  url: https://www.purespectrum.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.purespectrum.com/general-supplier-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.purespectrum.com/privacy-policy/
coverage:
  checked: '2026-10-21'
  detail: API documentation page renders HTML without a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.purespectrum.com/api-integration/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: PureSpectrum provides a self‑service research platform delivering high‑quality survey respondents across 125+ countries. Their AI‑driven PureScore™ system ensures data quality, while offering API automation and managed services for market research agencies, corporate insights teams, consulting firms, and enterprises.
image: https://www.purespectrum.com/wp-content/uploads/2026/02/Untitled-design.jpg
layout: provider
modified: '2026-10-21'
name: PureSpectrum
nav: Providers
network: true
overview: 'PureSpectrum is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Research, Data, and Market Research.


  PureSpectrum''s developer surface includes documentation, support, engineering blog, and 13 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 47.3
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/purespectrum/purespectrum-2026-11-03T141720.png
security:
- kind: domain-security
  name: Purespectrum Domain Security
  slug: purespectrum-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Purespectrum Trust Center
  slug: purespectrum-trust-center
  summary_line: SOC 2
slug: purespectrum
tags:
- Company
- Research
- Data
- Market Research
website: https://purespectrum.com
---
