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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/webbeds/refs/heads/main/hosts/webbeds-hosts.yml
  title: ''
  type: Hosts
  url: hosts/webbeds-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/webbeds/refs/heads/main/vendors/webbeds-vendors.yml
  title: ''
  type: Vendors
  url: vendors/webbeds-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.webbeds.com/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: https://www.webbeds.com/buyers/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.webbeds.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.webbeds.com/news/
- group: start
  title: ''
  type: Login
  url: https://www.webbeds.com/login/
- group: other
  title: ''
  type: Leadership
  url: https://www.webbeds.com/about/leadership/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WebBeds
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/webbeds/refs/heads/main/security/webbeds-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/webbeds-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://webbeds.com/
coverage:
  checked: 2026-09-23
  detail: No OpenAPI or other machine-readable contract found at standard endpoints.
  evidence:
  - status: timeout
    url: https://api.webbeds.com/openapi.json
  - status: 404
    url: https://webbeds.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-23'
description: WebBeds marketplace unites global supply with global demand, connecting hotels with travel buyers worldwide, making distribution simpler, smarter and more flexible. It operates a global B2B travel marketplace, offering hotels, resorts, and other accommodations to travel agencies and online travel agents through its API platform.
image: https://webbeds.sfo2.cdn.digitaloceanspaces.com/public/Uploads/Brand_Icons_Red_WB_200px200ppi__FocusFillWzEyMDAsNjMwLCJ5IiwyODVd.png
layout: provider
modified: '2026-09-23'
name: WebBeds
nav: Providers
network: true
overview: 'WebBeds is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Marketplace, B2B, and Hospitality.


  WebBeds'' developer surface includes support and 10 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 42.9
    operational_transparency: 5.3
  previous_composite: 12.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Webbeds Domain Security
  slug: webbeds-domain-security
  summary_line: TLSv1.3 · DMARC
slug: webbeds
tags:
- Travel
- Marketplace
- B2B
- Hospitality
website: https://webbeds.com/
---
