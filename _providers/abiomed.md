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
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abiomed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.heartrecovery.com/en-us
- group: operate
  title: ''
  type: Support
  url: https://www.heartrecovery.com/en-us/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.heartrecovery.com/en-us/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.heartrecovery.com/en-us/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.impellaconnect.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/abiomed_stock/
coverage:
  checked: '2026-09-06'
  detail: 'Abiomed sells regulated cardiac hardware — the Impella heart-pump family and its Automated Impella Controller console — and its only software is two end-user products with no developer surface: the customer-only Impella Connect clinician portal, whose Angular SPA catch-all answers HTTP 200 with the same HTML shell for /openapi.json, /swagger.json, /llms.txt and every /.well-known/* path, and the Impella App; abiomed.com 301s to www.heartrecovery.com, whose 375-URL sitemap contains no developer, API or integration page at all, api.impellaconnect.com is a private portal backend that answers every path with an nginx 502, and there is no SDK on npm or PyPI and no Abiomed-named GitHub organisation with a single public first-party repo.'
  evidence:
  - status: 200
    url: https://www.heartrecovery.com/en-us
  - status: 200
    url: https://www.heartrecovery.com/en-us/sitemap.xml
  - status: 404
    url: https://www.heartrecovery.com/openapi.json
  - status: 404
    url: https://www.heartrecovery.com/.well-known/api-catalog
  - status: 200
    url: https://www.impellaconnect.com/openapi.json
  - status: 502
    url: https://api.impellaconnect.com/openapi.json
  - status: 404
    url: https://api.impellaconnect.com/api-docs
  - status: 200
    url: https://api.github.com/orgs/Abiomed/repos
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: 'Abiomed is a Danvers, Massachusetts medical device manufacturer and, since December 22 2022, a standalone business inside Johnson & Johnson MedTech, which acquired it for approximately $16.6 billion. The company designs, manufactures and supports the Impella family of percutaneous micro-axial heart pumps — Impella CP, 5.5, RP Flex and the SmartAssist sensor line — used for temporary mechanical circulatory support during high-risk percutaneous coronary intervention and in cardiogenic shock, alongside the Automated Impella Controller console, the Breethe OXY-1 ECMO system and the Impella Connect remote case-review service. Its product is regulated hardware sold to hospitals and cath labs, supported by a 24/7 clinical support centre, not software sold to developers. Abiomed''s digital surface is limited to two end-user products: Impella Connect, a customer-only clinician portal that receives one-way RTMPS video of the console screen over port 443, and the Impella App for clinical
  reference. Abiomed publishes no developer portal, no API reference, no OpenAPI or other machine-readable specification, no SDK on npm, PyPI or any other registry, and maintains no public source-code organisation; the corporate site abiomed.com now redirects to the brand site at heartrecovery.com.'
image: https://www.heartrecovery.com/themes/heartrecovery_theme/heartrecovery/logo-jjmt-main.svg
layout: provider
modified: '2026-09-06'
name: Abiomed
nav: Providers
network: true
overview: 'Abiomed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Health Care, Cardiology, and Mechanical Circulatory Support.


  Abiomed''s developer surface includes support and 6 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Abiomed Domain Security
  slug: abiomed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: abiomed
tags:
- Company
- Medical Devices
- Health Care
- Cardiology
- Mechanical Circulatory Support
- Heart Pumps
- Medical Technology
- Hospitals
- Clinical Support
- Life Sciences
website: https://www.heartrecovery.com/en-us
---
