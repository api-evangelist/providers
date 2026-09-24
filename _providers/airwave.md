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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airwave/refs/heads/main/security/airwave-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airwave-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.airwave.us/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.airwave.us/pricing.html
- group: operate
  title: ''
  type: Support
  url: https://www.airwave.us/contact.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airwave.us/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airwave.us/terms.html
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/company/airwave/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/airwave/refs/heads/main/plans/airwave-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/airwave-plans-pricing.yml
- group: operate
  title: ''
  type: IncidentNotification
  url: https://www.airwave.us/terms.html
coverage:
  checked: '2026-09-19'
  detail: The pricing page lists "API integrations — ERP, CRM, CMMS" and "Access to Airwave Glasses SDK" only inside the custom-priced Video Intelligence tier behind a "Talk to us" demo form; the site has no developer, docs or API page (each 302s to /404.html), and the Wavelength backend hosts the public app bundle names (coreapi.wvlnth.net) serve no OpenAPI, docs or discovery document.
  evidence:
  - status: 200
    url: https://www.airwave.us/pricing.html
  - status: 302
    url: https://www.airwave.us/developers
  - status: 302
    url: https://www.airwave.us/docs
  - status: 404
    url: https://coreapi.wvlnth.net/openapi.json
  - status: 404
    url: https://coreapi.wvlnth.net/docs
  reason: sales-gate
  state: gated
created: '2026-09-19'
description: 'Airwave (Indianapolis, founded 2022) is a field intelligence platform for industrial and field-service technicians: ANSI Z87+ smart safety glasses with a built-in camera, microphone and speakers record the job, and the Airwave software turns the footage into inspection reports, job hazard analyses, customer summaries and searchable job notes, with an AI assistant ("Blue") answering questions from uploaded manuals, parts lists and team knowledge. The pricing page lists API integrations (ERP, CRM, CMMS) and an Airwave Glasses SDK only in the custom-priced Video Intelligence tier behind a sales conversation; no public developer documentation, API reference or machine-readable contract is published.'
image: https://www.airwave.us/images/favicon.png
layout: provider
modified: '2026-09-19'
name: Airwave
nav: Providers
network: true
overview: 'Airwave is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Field Service, Smart Glasses, Wearables, and Computer Vision.


  Airwave''s developer surface includes pricing, support, and 7 more developer resources.'
plans:
- name: Airwave Plans Pricing
  plan_count: 3
  slug: airwave-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 18.6
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Airwave Domain Security
  slug: airwave-domain-security
  summary_line: TLSv1.3 · DMARC
slug: airwave
tags:
- Company
- Field Service
- Smart Glasses
- Wearables
- Computer Vision
- Industrial
- AI Assistant
- Inspection Reports
- Safety
website: https://www.airwave.us/
---
