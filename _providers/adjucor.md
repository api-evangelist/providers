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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adjucor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adjucor.com/
- group: company
  title: ''
  type: About
  url: https://adjucor.com/technology/
- group: company
  title: ''
  type: Blog
  url: https://adjucor.com/news/
- group: operate
  title: ''
  type: Support
  url: https://adjucor.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adjucor.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adjucor
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/adjucor
coverage:
  checked: '2026-09-07'
  detail: 'AdjuCor GmbH builds an implantable cardiac support device (reBEAT) in Munich and sells hardware to heart teams, not software to developers: its entire public surface is a seven-page WordPress marketing site (home, technology, team, news, contact, privacy policy) with no developer, docs, portal, API or integration link anywhere in the nav, footer or page source, and that WordPress router answers every non-page path — including a random control path — with the same 2,679-byte "WordPress > Error" page under HTTP 500, so /openapi.json, /swagger.json, /api-docs, /llms.txt, /wp-json/, /?rest_route=/ and every /.well-known/ path are all hard misses; api., docs., developer., developers., portal., app., data. and connect..adjucor.com do not resolve in DNS at all, there is no adjucor GitHub organization (404) and no package named adjucor on npm or PyPI. The one subdomain that does resolve, cloud.adjucor.com, is a login-walled self-hosted Nextcloud 25.0.3 appliance — third-party software
    AdjuCor runs internally, not an API it publishes — whose only served /.well-known/ document is Nextcloud''s own vendor-default security.txt pointing at hackerone.com/nextcloud and expired 2023-04-30, so it is recorded as a miss rather than credited to AdjuCor.'
  evidence:
  - status: 200
    url: https://adjucor.com/
  - status: 500
    url: https://adjucor.com/openapi.json
  - status: 500
    url: https://adjucor.com/swagger.json
  - status: 500
    url: https://adjucor.com/api-docs
  - status: 500
    url: https://adjucor.com/llms.txt
  - status: 500
    url: https://adjucor.com/wp-json/
  - status: 500
    url: https://adjucor.com/?rest_route=/
  - status: 500
    url: https://adjucor.com/developers
  - status: 500
    url: https://adjucor.com/.well-known/agent-card.json
  - status: 500
    url: https://adjucor.com/.well-known/agent.json
  - status: 500
    url: https://adjucor.com/.well-known/api-catalog
  - status: 500
    url: https://adjucor.com/.well-known/security.txt
  - status: 500
    url: https://adjucor.com/zz-api-evangelist-control-9f3a
  - status: 404
    url: https://cloud.adjucor.com/.well-known/agent-card.json
  - status: 200
    url: https://cloud.adjucor.com/.well-known/security.txt
  - status: 404
    url: https://api.github.com/orgs/adjucor
  reason: not-a-software-company
  state: none
created: '2026-09-07'
description: AdjuCor GmbH is a Munich, Germany medical device company, founded in 2012, that develops reBEAT — an implantable, patient-specific cardiac support system for advanced heart failure. reBEAT is an epicardial device that conforms to the outside of the heart and delivers uni- or biventricular mechanical circulatory support without ever contacting blood, which is intended to avoid the thrombosis, stroke and haemolysis risks that constrain conventional blood-pumping ventricular assist devices. It is implanted on the beating heart in a minimally invasive, suture-free procedure by a heart team. The company reported first-in-human implantations in 2023 and runs an EIC co-funded EU project toward market entry; the device remains investigational. AdjuCor is a hardware manufacturer rather than a software business, and publishes no developer program, public API, SDK, or machine-readable API contract on any host it operates.
image: https://adjucor.com/wp-content/uploads/2024/03/AdjuCor_Logo.png
layout: provider
modified: '2026-09-07'
name: AdjuCor GmbH
nav: Providers
network: true
overview: 'AdjuCor GmbH is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Cardiology, and Heart Failure.


  AdjuCor GmbH''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adjucor Domain Security
  slug: adjucor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adjucor
tags:
- Company
- Medical Devices
- Healthcare
- Cardiology
- Heart Failure
- Implantable Devices
- Mechanical Circulatory Support
- Medtech
- Germany
website: https://adjucor.com/
---
