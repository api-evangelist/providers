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
  href: https://raw.githubusercontent.com/api-evangelist/clariter/refs/heads/main/hosts/clariter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clariter-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clariter/refs/heads/main/vendors/clariter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clariter-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clariter.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clariter.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://clariter.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clariter/refs/heads/main/security/clariter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clariter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clariter.com
coverage:
  checked: '2026-10-08'
  detail: No public developer program or API documentation is available on clariter.com.
  evidence:
  - status: 200
    url: https://clariter.com
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Clariter is a global cleantech company producing sustainable petrochemicals upcycled from plastic waste. It offers high‑quality alternatives to fossil‑based products for thousands of industrial and consumer applications, helping create circularity and reduce carbon waste. The company’s proprietary technology turns plastic waste into profitable, sustainable solutions, addressing the global plastic waste epidemic.
image: https://clariter.com/wp-content/themes/clariter/assets/img/fb.jpg
layout: provider
modified: '2026-10-08'
name: Clariter
nav: Providers
network: true
overview: Clariter is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cleantech, Sustainability, Petrochemicals, Circular Economy, and Plastic Waste.
random_paper: 18
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clariter Domain Security
  slug: clariter-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clariter
tags:
- Cleantech
- Sustainability
- Petrochemicals
- Circular Economy
- Plastic Waste
website: https://clariter.com
---
