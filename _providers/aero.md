---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aero.com/
- group: operate
  title: ''
  type: Support
  url: https://aero.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aero.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aero.com/privacy-policy
coverage:
  checked: '2026-08-06'
  detail: Aero is a consumer semi-private airline whose only machine-readable distribution channel is Sabre GDS under airline designator 5E / plating carrier 307 — a third-party channel, not an API it publishes; aero.com is a Next.js SPA that answers 200 with the homepage for every unknown path (including /openapi.json and every /.well-known/* probe), robots.txt disallows its internal /api/* routes, and api./developer./docs.aero.com are wildcard DNS with no valid certificate.
  evidence:
  - status: 200
    url: https://aero.com/openapi.json
  - status: 200
    url: https://aero.com/thisdoesnotexist-control-12345
  - status: 200
    url: https://aero.com/.well-known/agent-card.json
  - status: 200
    url: https://aero.com/robots.txt
  - status: 200
    url: https://aero.com/gds-ticketing-guide
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: 'Aero Technologies, Inc. is a Van Nuys, California semi-private airline founded in 2019 by Uber co-founder Garrett Camp, selling individual seats on scheduled flights and on-demand charters operated exclusively from private terminals. Its fleet comprises Embraer ERJ135 and Legacy 600 jets plus Gulfstream IV-SP aircraft, flying Los Angeles to New York City, Aspen, Sun Valley, Napa Valley, Los Cabos, Las Vegas, Maui, Miami, Heber and Greater Palm Springs. Aero distributes through aero.com, its mobile app, a travel-advisor channel, and Sabre GDS under airline designator 5E with plating carrier 307. It is a consumer travel brand: no public developer API, developer portal, SDK, webhook surface or machine-readable specification is published.'
image: https://aero.com/_next/static/images/social-e232bb93c09bb5dc467b8481214a3c30.jpg
layout: provider
modified: '2026-08-06'
name: Aero
nav: Providers
network: true
overview: 'Aero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Air Travel, Airlines, and Private Aviation.


  Aero''s developer surface includes support and 4 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aero/refs/heads/main/screenshots/aero-2026-08-07T161005.png
security:
- kind: domain-security
  name: Aero Domain Security
  slug: aero-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aero
tags:
- Company
- Travel
- Air Travel
- Airlines
- Private Aviation
- Transportation
- Booking
- Consumer
website: https://aero.com/
---
