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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/lexyom-com/hosts/lexyom-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lexyom-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/lexyom-com/vendors/lexyom-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lexyom-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.lexyom.com/login
- group: auth
  href: https://artifacts.apis.io/lexyom-com/security/lexyom-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lexyom-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lexyom.com
coverage:
  checked: '2026-10-25'
  detail: Lexyom provides legal services and does not expose a software API.
  evidence:
  - status: 200
    url: https://lexyom.com
  reason: not-a-software-company
  state: none
created: '2026-10-25'
description: Lexyom LLP is an international law firm with offices in New York and Dubai that provides legal services to financial institutions, proprietary trading firms, and brokerage companies. It offers financial institution setup, company registration, trademark registration, broker licensing, contract drafting and review, and retainer representation.
image: https://storage.googleapis.com/gpt-engineer-file-uploads/attachments/og-images/f5eca051-462d-42ea-b07e-85d707be710d?Expires=1772400715&GoogleAccessId=go-api-on-aws%40gpt-engineer-390607.iam.gserviceaccount.com&Signature=PcKnGMSpkDCvoKeMfuG93bfMUZ2AuvTwardV3rNSEo0UnY7jO%2Fg0neVN9PBreBt9BL7P27WGX7%2By4g2YUOU1ogrBkareVJf5xlAB2WtqyCuVRMfpGpQly9PzOzT58bicDSp3pP0TQ5APDL1PW5RKF5JKzRAjyobNVw2lf2UMOmaGI082RFCZyCCeadPyx5N9aoqaQPtQOYx%2FBMfDHaayKRjInu80AOlUJi7%2BAmuUzudXY1oiOU38zKhGCXqINu74u9YE58VSfTaf5o5wvajXpT5Cb1QM9R5gB3mZIHoWwyPelZ4kCVAr4Ix6fjYFhuNq%2Ffd0KrRvrISdGnWqZKU6tg%3D%3D
layout: provider
modified: '2026-10-25'
name: Lexyom
nav: Providers
network: true
overview: Lexyom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Legal Services, Financial Institution Setup, Broker Licensing, Company Registration, and Trademark Registration.
random_paper: 2
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lexyom Com Domain Security
  slug: lexyom-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lexyom-com
tags:
- Legal Services
- Financial Institution Setup
- Broker Licensing
- Company Registration
- Trademark Registration
- Contract Drafting
website: https://lexyom.com
---
