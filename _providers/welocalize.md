---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.7
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.welocalize.com/
- group: auth
  href: https://artifacts.apis.io/welocalize/well-known/welocalize-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/welocalize-status-security.txt
- group: agent
  href: https://artifacts.apis.io/welocalize/well-known/welocalize-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/welocalize-well-known.yml
- group: other
  href: https://artifacts.apis.io/welocalize/hosts/welocalize-hosts.yml
  title: ''
  type: Hosts
  url: hosts/welocalize-hosts.yml
- group: other
  href: https://artifacts.apis.io/welocalize/vendors/welocalize-vendors.yml
  title: ''
  type: Vendors
  url: vendors/welocalize-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.welocalize.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.welocalize.com/newsroom/
- group: auth
  href: https://artifacts.apis.io/welocalize/security/welocalize-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/welocalize-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/welocalize/security/welocalize-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/welocalize-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://welocalize.com/
coverage:
  checked: '2026-10-27'
  detail: No public developer documentation or API reference pages were found for Opal by Welocalize.
  evidence:
  - status: 200
    url: https://www.welocalize.com/wp-signup.php?new=welocalize.com
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: Opal by Welocalize provides AI‑enhanced language services and the Opal platform, a cloud‑based solution for translation, localization, and content adaptation. The company leverages machine learning to accelerate multilingual content delivery for enterprises, offering APIs for translation, terminology management, and workflow automation. Welocalize serves global brands across technology, finance, and life‑sciences sectors, emphasizing data security and compliance.
image: https://www.welocalize.com/wp-content/uploads/2026/04/Welocalize-WeloGlobalPrimary-Full-Color-Dark.png
layout: provider
modified: '2026-10-27'
name: Opal by Welocalize
nav: Providers
network: true
overview: Opal by Welocalize is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Localization, AI, Translation, and Enterprise.
random_paper: 15
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Welocalize Domain Security
  slug: welocalize-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Welocalize Trust Center
  slug: welocalize-trust-center
  summary_line: ISO 27001, GDPR
slug: welocalize
tags:
- Company
- Localization
- AI
- Translation
- Enterprise
website: https://welocalize.com/
---
