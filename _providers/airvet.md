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
  scored_at: '2026-09-20'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airvet/refs/heads/main/security/airvet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airvet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.airvet.com/
- group: company
  title: ''
  type: Blog
  url: https://www.airvet.com/blog
- group: operate
  title: ''
  type: Support
  url: https://airvet.zendesk.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/airvet
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airvet.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airvet.com/pet-parents-terms-of-service
- group: start
  title: ''
  type: Login
  url: https://web.airvet.com/
- group: company
  title: ''
  type: Partners
  url: https://www.airvet.com/partners
- group: other
  title: ''
  type: AppStore
  url: https://apps.apple.com/us/app/airvet-for-pet-parents/id1448478595
- group: other
  title: ''
  type: GooglePlay
  url: https://play.google.com/store/apps/details?id=com.myairvet.android.parent
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/airvet/refs/heads/main/regulatory/airvet-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/airvet-regulatory-posture.yml
coverage:
  checked: '2026-09-19'
  detail: 'Airvet is a consumer/employer-benefit pet telehealth app with no developer program: no developer, docs or api subdomain resolves in DNS, the airvet GitHub organization has zero public repositories, the Zendesk help center has no article matching "api", "developer" or "integration", and airvet.com itself sits behind a Vercel Security Checkpoint that answers every path (including /developers, /docs, /api, /openapi.json and every /.well-known/ path) with HTTP 429, so the only surfaces readable were the HubSpot marketing host, the Next.js parent portal and the help-center API - none of which publish a contract.'
  evidence:
  - status: 429
    url: https://www.airvet.com/developers
  - status: 429
    url: https://airvet.com/openapi.json
  - status: 200
    url: https://api.github.com/users/airvet
  - status: 200
    url: https://airvet.zendesk.com/api/v2/help_center/articles/search.json?query=developer
  - status: 503
    url: https://api.myairvet.com/
  - status: 404
    url: https://web.airvet.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-09-19'
description: Airvet is a Los Angeles-based pet telehealth company, founded in 2018, that connects pet parents with licensed veterinarians 24/7 by video and chat through its Airvet for Pet Parents app (iOS/Android) and a companion Airvet Doctor app for its nationwide network of vets. It sells the service two ways - as "Vetcare as a Benefit", an employer-sponsored benefit adopted by companies such as Adobe, Activision, Synchrony and PepsiCo that covers every pet in an employee's household, and as a direct annual consumer membership - and layers on partner offers such as Pumpkin wellness plans and Healthy Paws insurance. Airvet is a consumer/B2B2C telehealth product, not an API platform - as of this profile it publishes no developer portal, API documentation, SDKs, webhooks or machine-readable API contract, and its GitHub organization has no public repositories.
image: https://avatars.githubusercontent.com/u/48732512
layout: provider
modified: '2026-09-19'
name: Airvet
nav: Providers
network: true
overview: 'Airvet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pet Care, Veterinary, Telehealth, Employee Benefits, and Health.


  Airvet''s developer surface includes engineering blog, support, and 10 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 50.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Airvet Domain Security
  slug: airvet-domain-security
  summary_line: TLSv1.3 · DMARC
slug: airvet
tags:
- Pet Care
- Veterinary
- Telehealth
- Employee Benefits
- Health
- Mobile App
- Pets
- Company
website: https://www.airvet.com/
---
