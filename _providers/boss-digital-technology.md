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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Developer portal providing information about digital transformation services.
  name: Boss Digital Technology API
  slug: boss-digital-technology-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boss-digital-technology/refs/heads/main/hosts/boss-digital-technology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boss-digital-technology-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boss-digital-technology/refs/heads/main/vendors/boss-digital-technology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boss-digital-technology-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bossdigital.tech/privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.bossdigital.tech/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boss-digital-technology/refs/heads/main/security/boss-digital-technology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boss-digital-technology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bossdigital.tech/
coverage:
  detail: No OpenAPI or other machine-readable contract found on API hosts.
  evidence:
  - status: 404
    url: https://api.bossdigital.tech/openapi.json
  - status: 404
    url: https://api.bossdigital.tech/openapi.yaml
  - status: 404
    url: https://api.bossdigital.tech/v1/openapi.json
  - status: 404
    url: https://api.bossdigital.tech/api-docs
  - status: 404
    url: https://api.bossdigital.tech/docs
  - status: 404
    url: https://api.bossdigital.tech/redoc
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Boss Digital Technology is a digital transformation agency offering web design, mobile app development, performance marketing, and strategic consulting services. It helps brands scale through comprehensive digital solutions, emphasizing user experience, technology integration, and growth-focused strategies.
image: https://www.bossdigital.tech/wp-content/uploads/2021/08/plain_blue.png
layout: provider
modified: '2026-10-03'
name: Boss Digital Technology
nav: Providers
network: true
overview: 'Boss Digital Technology publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Transformation, Web Design, Mobile App, Marketing, and Agency.


  Boss Digital Technology''s developer surface includes documentation and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boss Digital Technology Domain Security
  slug: boss-digital-technology-domain-security
  summary_line: TLSv1.3 · DMARC
slug: boss-digital-technology
tags:
- Digital Transformation
- Web Design
- Mobile App
- Marketing
- Agency
website: https://www.bossdigital.tech/
---
