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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Mobile marketing API platform providing endpoints for advertisers and publishers.
  name: Mintegral API
  slug: mintegral-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.mintegral.com/en/security
- group: other
  href: https://artifacts.apis.io/mintegral/hosts/mintegral-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mintegral-hosts.yml
- group: other
  href: https://artifacts.apis.io/mintegral/vendors/mintegral-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mintegral-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.mintegral.com/en/help-center
- group: auth
  title: ''
  type: Security
  url: https://www.mintegral.com/en/security
- group: auth
  href: https://artifacts.apis.io/mintegral/security/mintegral-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mintegral-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/mintegral/security/mintegral-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mintegral-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mintegral.com/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.mintegral.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.mintegral.com/en
- group: company
  title: ''
  type: Blog
  url: https://www.mintegral.com/en/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mintegral.com/en/privacy
coverage:
  checked: '2026-10-28'
  detail: The developer documentation is served as JavaScript‑rendered pages, preventing machine‑readable discovery.
  evidence:
  - status: 200
    url: https://www.mintegral.com/en
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Mintegral provides AI‑powered mobile marketing solutions that help advertisers acquire, retain, and monetize users across gaming, subscription, and e‑commerce apps. Their platform offers app growth, retargeting, monetization, and creative studio tools, leveraging advanced AI to optimize ad spend and drive engagement. Mintegral serves global advertisers and publishers, emphasizing data‑driven growth and comprehensive campaign management.
image: https://assets-official.mobvista.com/uploads/2024/05/13/MTG%20web%20%E7%BC%A9%E7%95%A5%E5%9B%BE%202024.04.08_%E9%A6%96%E9%A1%B5%20EN.jpg
layout: provider
modified: '2026-10-28'
name: Mintegral
nav: Providers
network: true
overview: 'Mintegral is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MobileMarketing, AI, Advertising, and AppGrowth.


  Mintegral''s developer surface includes support, documentation, engineering blog, and 9 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mintegral Domain Security
  slug: mintegral-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mintegral Trust Center
  slug: mintegral-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: mintegral
tags:
- Company
- MobileMarketing
- AI
- Advertising
- AppGrowth
website: https://www.mintegral.com/en
---
