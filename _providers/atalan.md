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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atalan/refs/heads/main/hosts/atalan-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atalan-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atalan/refs/heads/main/vendors/atalan-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atalan-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atalan/refs/heads/main/security/atalan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atalan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atalan.com
- group: docs
  title: ''
  type: Documentation
  url: https://atalan.com/access-hub/
- group: docs
  title: ''
  type: APIReference
  url: https://atalan.com/access-outreach/
- group: start
  title: ''
  type: GettingStarted
  url: https://atalan.com/about/
- group: company
  title: ''
  type: Blog
  url: https://atalan.com/newsroom/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atalan.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atalan.com/privacy-policy/
created: '2026-09-26'
description: Atalan provides a technology-enabled clinical partnership that gives doctors, medical centers, and hospitals unprecedented access to a network of leading clinical laboratories. By offering a comprehensive platform with tools, dashboards, and outreach services, Atalan streamlines lab testing, results delivery, and partnership management, improving diagnostic decision-making and patient outcomes across the United States.
image: https://atalan.com/wp-content/uploads/2023/09/atalan-newsroom-featured.jpg
layout: provider
modified: '2026-09-26'
name: Atalan
nav: Providers
network: true
overview: 'Atalan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Laboratory, Diagnostics, Platform, and Access.


  Atalan''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 6 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 15.0
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
    developer_ergonomics: 31.0
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atalan Domain Security
  slug: atalan-domain-security
  summary_line: TLSv1.3
slug: atalan
tags:
- Healthcare
- Laboratory
- Diagnostics
- Platform
- Access
website: https://www.atalan.com
---
