---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.xdi.systems/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/xdi/refs/heads/main/hosts/xdi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xdi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/xdi/refs/heads/main/vendors/xdi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/xdi-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://xdi.systems/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xdi/refs/heads/main/security/xdi-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/xdi-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xdi/refs/heads/main/security/xdi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xdi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://xdi.systems
- group: docs
  title: ''
  type: Documentation
  url: https://xdi.systems/solutions/apis
- group: docs
  title: ''
  type: APIReference
  url: https://xdi.systems/solutions/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://xdi.systems/how-to-get-started
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xdi.systems/privacy-policy
coverage:
  checked: '2026-10-14'
  detail: The provider's website returns HTML but no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://xdi.systems
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: XDI (Cross Dependency Initiative) provides physical climate risk expertise, offering solutions such as asset risk screening, deep‑dive analyses, reporting, stress‑testing, and resilience planning. Their platform delivers data and insights to help financial, corporate, government, and civil‑society clients understand, report, and mitigate climate‑related risks across portfolios.
layout: provider
modified: '2026-10-14'
name: XDI
nav: Providers
network: true
overview: 'XDI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Climate, Risk Management, Data, Analytics, and Solutions.


  XDI''s developer surface includes documentation, API reference, getting-started guide, and 8 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Xdi Domain Security
  slug: xdi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Xdi Trust Center
  slug: xdi-trust-center
  summary_line: ISO 27001
slug: xdi
tags:
- Climate
- Risk Management
- Data
- Analytics
- Solutions
website: https://xdi.systems
---
