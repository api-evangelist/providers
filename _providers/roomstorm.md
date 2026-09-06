---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Roomstorm's B2B hotel-room marketplace REST API (Django REST framework backend). Documented in API Blueprint, it covers a bootstrap discovery endpoint, JWT username/password authentication, hotel sear
  name: Roomstorm API
  slug: roomstorm-api
artifact_total: 3
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/walksource/roomstorm-api/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/walksource/roomstorm-api/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/roomstorm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.roomstorm.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/walksource
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/walksource/roomstorm-api
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/roomstorm-llms.txt
created: '2026-07-17'
description: Roomstorm is a real-time B2B hotel room marketplace, best known for building the airline industry's first fully automated platform for providing hotel accommodations to distressed passengers during flight disruptions. Founded by Maksim Izmaylov and backed by Y Combinator (Summer 2014), the San Francisco company connects airlines, hotels, and travelers so that irregular-operations (IROPS) rebooking, room sourcing, invoicing, and voucher issuance happen programmatically instead of through manual phone calls. Its backend exposes a JSON REST API (documented in API Blueprint) covering authentication, bookings, hotels, rooms, vacancies, organizations, vouchers, and airport search.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/roomstorm.png
layout: provider
modified: '2026-07-21'
name: Roomstorm
nav: Providers
network: true
overview: Roomstorm publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Hospitality, Hotels, and Airlines.
random_paper: 2
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  open_source:
    applies: true
    score: 0.0
  previous_composite: 10.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/roomstorm/refs/heads/main/screenshots/roomstorm-2026-09-02T154131.png
security:
- kind: authentication
  name: Roomstorm Authentication
  slug: roomstorm-authentication
  summary_line: http/cookie · 2 schemes
- kind: domain-security
  name: Roomstorm Domain Security
  slug: roomstorm-domain-security
  summary_line: TLSv1.3 · HSTS
slug: roomstorm
tags:
- Company
- Travel
- Hospitality
- Hotels
- Airlines
- Marketplace
- Bookings
- Y Combinator
website: https://www.roomstorm.com/
---
