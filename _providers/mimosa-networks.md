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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 18.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/mimosa-networks/llms/mimosa-networks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mimosa-networks-llms.txt
- group: agent
  href: https://artifacts.apis.io/mimosa-networks/well-known/mimosa-networks-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mimosa-networks-well-known.yml
- group: other
  href: https://artifacts.apis.io/mimosa-networks/hosts/mimosa-networks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mimosa-networks-hosts.yml
- group: other
  href: https://artifacts.apis.io/mimosa-networks/vendors/mimosa-networks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mimosa-networks-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mimosa.co/legal/terms-use
- group: auth
  title: ''
  type: Security
  url: https://mimosa.co/legal/security
- group: company
  title: ''
  type: Newsroom
  url: https://mimosa.co/news/awb
- group: auth
  href: https://artifacts.apis.io/mimosa-networks/security/mimosa-networks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mimosa-networks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mimosa.co/
- group: docs
  title: ''
  type: Documentation
  url: https://mimosa.co/support
- group: company
  title: ''
  type: Blog
  url: https://mimosa.co/blog
- group: operate
  title: ''
  type: Support
  url: https://mimosa.co/support
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mimosa.my.site.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mimosa.co/legal
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 401
    url: https://mimosa.my.site.com/mcp/v1
  - status: 200
    url: https://mimosa.co/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Mimosa Networks provides fixed wireless access solutions, delivering ultra‑reliable, high‑speed connectivity up to 3 Gbps for point‑to‑point and point‑to‑multipoint networks. Their product portfolio includes the 6 Series PTP and PTMP radios, antennas, accessories, and cloud‑based management, serving cable operators, multi‑family, public safety, and other sectors.
layout: provider
modified: '2026-10-26'
name: Mimosa Networks
nav: Providers
network: true
overview: 'Mimosa Networks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fixed Wireless, Connectivity, Networking, and Infrastructure.


  Mimosa Networks'' developer surface includes documentation, engineering blog, support, and 11 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 52.7
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mimosa-networks/mimosa-networks-2026-11-03T135620.png
security:
- kind: domain-security
  name: Mimosa Networks Domain Security
  slug: mimosa-networks-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: mimosa-networks
tags:
- Company
- Fixed Wireless
- Connectivity
- Networking
- Infrastructure
website: https://mimosa.co/
---
