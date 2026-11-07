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
  href: https://artifacts.apis.io/adguard/well-known/adguard-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adguard-status-security.txt
- group: agent
  href: https://artifacts.apis.io/adguard/well-known/adguard-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adguard-well-known.yml
- group: other
  href: https://artifacts.apis.io/adguard/hosts/adguard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adguard-hosts.yml
- group: other
  href: https://artifacts.apis.io/adguard/vendors/adguard-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adguard-vendors.yml
- group: build
  href: https://artifacts.apis.io/adguard/packages/adguard-packages.yml
  title: ''
  type: SDKs
  url: packages/adguard-packages.yml
- group: build
  href: https://artifacts.apis.io/adguard/packages/adguard-packages.yml
  title: ''
  type: Packages
  url: packages/adguard-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adguard.com/terms-and-conditions.html?_plc=en
- group: operate
  title: ''
  type: Support
  url: https://adguard.com/en/support/faq.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adguard.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adguard.com/privacy.html
- group: company
  title: ''
  type: Blog
  url: https://adguard.com/en/blog/index.html
- group: auth
  href: https://artifacts.apis.io/adguard/security/adguard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adguard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adguard.com/
- group: docs
  title: ''
  type: Documentation
  url: https://adguard.com/en/adguard-home/overview.html
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on any discovered host.
  evidence:
  - status: 404
    url: https://api.adguard.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: AdGuard Home provides network-wide ad blocking and privacy protection software for routers, servers, and all devices on a local network. It blocks ads, trackers, and malware at the DNS level, offering customizable filtering, parental controls, and optional integration with AdGuard DNS and VPN services.
image: https://cdn.adguardcdn.com/website/adguard.com/video/meta/agnar_en.png
layout: provider
modified: '2026-10-28'
name: AdGuard Home
nav: Providers
network: true
overview: 'AdGuard Home is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Ad Blocking, Privacy, DNS Filtering, Network Security, and Open Source.


  AdGuard Home''s developer surface includes support, engineering blog, documentation, and 11 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 48.2
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.0
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/adguard/adguard-2026-11-03T120254.png
security:
- kind: domain-security
  name: Adguard Domain Security
  slug: adguard-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adguard
tags:
- Ad Blocking
- Privacy
- DNS Filtering
- Network Security
- Open Source
website: https://adguard.com/
---
