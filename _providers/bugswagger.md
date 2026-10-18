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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bugswagger/refs/heads/main/hosts/bugswagger-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bugswagger-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bugswagger/refs/heads/main/vendors/bugswagger-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bugswagger-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bugswagger.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bugswagger.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://bugswagger.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bugswagger
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bugswagger/refs/heads/main/security/bugswagger-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bugswagger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bugswagger.com
coverage:
  checked: '2026-10-06'
  detail: Home page returns a JavaScript shell with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://bugswagger.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: BugSwagger provides senior security engineers who hand‑test web, API, mobile, cloud, and red‑team assessments. Their services include thorough penetration testing with real findings, detailed reports, and retesting. The team emphasizes manual testing over automated scanners, offering expert insight without junior outsourcing.
image: https://bugswagger.com/logo.png
layout: provider
modified: '2026-10-06'
name: Bugswagger
nav: Providers
network: true
overview: 'Bugswagger is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Bugswagger''s developer surface includes pricing, engineering blog, and 6 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 39.3
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bugswagger Domain Security
  slug: bugswagger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bugswagger
tags:
- Company
website: https://bugswagger.com
---
