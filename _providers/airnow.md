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
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airnow/refs/heads/main/security/airnow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airnow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airnow.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/airnow/
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/airnowdata
coverage:
  checked: '2026-09-19'
  detail: airnow.com is a single-page Azure Static Web App brochure for the Airnow group (Lab Cave, AppMonsta, Mobstr, Vambrace) that answers every path, including /developers, /api, /openapi.json and every /.well-known/* document, with the same 63,778-byte HTML shell; the group's only API surface belongs to its subsidiary AppMonsta (api.appmonsta.com), and the former product domain airnowdata.com now 301s to an unrelated gambling site.
  evidence:
  - status: 200
    url: https://airnow.com/developers
  - status: 200
    url: https://airnow.com/openapi.json
  - status: 200
    url: https://airnow.com/.well-known/agent-card.json
  - status: 301
    url: https://airnowdata.com/
  - status: 0
    url: https://api.airnow.com/
  reason: no-developer-program
  state: none
created: '2026-09-19'
description: 'Airnow is a London-headquartered group of specialist mobile-app technology companies operating as one engine for app-first businesses: Lab Cave (Madrid, mobile game publishing and growth), AppMonsta (UK, programmatic ad-tech and an app-store intelligence dataset), Mobstr (UK, AI-driven mobile-app security scanning and GRC ratings) and Vambrace (UK, managed SOC and vCISO services). The group is fusing these into Project Chimera, a unified SaaS platform announced for 2026 that layers AI analytics, media buying and monetisation on a 24-million-app data lake. Airnow itself publishes no developer program, API reference or machine-readable contract; the API surface in the group sits with its subsidiary AppMonsta. Pre-IPO shares trade on EquityZen.'
layout: provider
modified: '2026-09-19'
name: Airnow
nav: Providers
network: true
overview: Airnow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobile App, App Intelligence, AdTech, and Mobile Security.
random_paper: 18
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 4.6
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Airnow Domain Security
  slug: airnow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: airnow
tags:
- Company
- Mobile App
- App Intelligence
- AdTech
- Mobile Security
- Holding Company
- United Kingdom
website: https://airnow.com/
---
