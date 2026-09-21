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
  href: https://raw.githubusercontent.com/api-evangelist/airislabsb51a/refs/heads/main/security/airislabsb51a-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airislabsb51a-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.airis-labs.com/
- group: company
  title: ''
  type: About
  url: https://www.airis-labs.com/about
- group: other
  title: ''
  type: Leadership
  url: https://www.airis-labs.com/about
- group: operate
  title: ''
  type: ContactSales
  url: https://www.airis-labs.com/get-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airis-labs.com/information/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airis-labs.com/information/privacy-notice
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airislabs
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/airis-labs
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/airislabsb51a/refs/heads/main/regulatory/airislabsb51a-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/airislabsb51a-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/airislabsb51a/refs/heads/main/regulatory/airislabsb51a-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/airislabsb51a-regulatory-posture.yml
coverage:
  checked: '2026-09-19'
  detail: Airis Labs is a demo-led defense-AI vendor whose entire public surface is a five-page Webflow marketing site (sitemap.xml lists home, about, get-a-demo, privacy notice, terms of use); no docs, api, developer, app, status or mcp subdomain resolves (all NXDOMAIN) and /docs, /api, /developers, /openapi.json and every /.well-known/* path return 404.
  evidence:
  - status: 200
    url: https://www.airis-labs.com/sitemap.xml
  - status: 404
    url: https://www.airis-labs.com/docs
  - status: 404
    url: https://www.airis-labs.com/openapi.json
  - status: 404
    url: https://www.airis-labs.com/.well-known/agent-card.json
  - status: 403
    url: https://equityzen.com/company/airislabsb51a
  reason: no-developer-program
  state: none
created: '2026-09-19'
description: Airis Labs (AI RIS Labs Ltd.) is a defense and public-safety AI company, founded in 2023 and based in Washington, D.C. and Tel Aviv, whose User-Generated Field Intelligence (UGFI) platform turns unstructured user-generated video and other visual sources - smartphones, social media, digital forensics, CCTV, body cams, drones and FMV - into structured, searchable intelligence for government, homeland security, law enforcement and military analysts, with agentic analyst workflows and self-hosted or sovereign-cloud deployment. The company markets a demo-led, customer-controlled product and publishes no public API, SDK, developer portal or machine-readable contract.
image: https://cdn.prod.website-files.com/68241742ad17ac94212468d8/682418aa4db6ec8782b4aee8_webclip.png
layout: provider
modified: '2026-09-19'
name: Airis Labs
nav: Providers
network: true
overview: Airis Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defense, Homeland Security, Public Safety, and Video Intelligence.
random_paper: 19
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 9.2
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Airislabsb51A Domain Security
  slug: airislabsb51a-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: airislabsb51a
tags:
- Company
- Defense
- Homeland Security
- Public Safety
- Video Intelligence
- Computer-Vision
- Artificial Intelligence
- Intelligence Analysis
- Agentic AI
website: https://www.airis-labs.com/
---
