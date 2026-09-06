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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/4c-medical-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.4cmed.com/
- group: company
  title: ''
  type: Blog
  url: https://www.4cmed.com/news
coverage:
  checked: '2026-09-05'
  detail: 4C Medical Technologies is a clinical-stage cardiac device manufacturer whose product is a physical implant (the AltaValve TMVR system); its entire web presence is an 11-page Squarespace marketing site with no developer, docs, or API section, and api/developer/dev/ docs/portal.4cmed.com do not resolve in DNS.
  evidence:
  - status: 200
    url: https://www.4cmed.com/sitemap.xml
  - status: 404
    url: https://www.4cmed.com/.well-known/security.txt
  - status: 404
    url: https://www.4cmed.com/openapi.json
  - status: 404
    url: https://www.4cmed.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/4cmedical
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: 4C Medical Technologies, Inc. is a privately held, clinical-stage medical device company headquartered at 6655 Wedgwood Road North, Suite 160, Maple Grove, Minnesota, developing minimally invasive therapies for structural heart disease. Its lead product is the AltaValve System, a supra-annular transcatheter mitral valve replacement (TMVR) device delivered by transseptal or transapical catheter and designed to expand the treatable severe mitral regurgitation patient population, streamline the procedure and preserve the native mitral valve; the device is fully recapturable until released from the delivery catheter. AltaValve holds FDA Breakthrough Device designation and is enrolling the ATLAS global pivotal trial (NCT06465745) in the United States and Europe. The company closed a $175M Series D financing led by Boston Scientific in March 2025. It is a physical medical device manufacturer and publishes no developer program, public API, SDK or machine-readable API contract of any
  kind.
image: https://static1.squarespace.com/static/5d44355a750fb500017eb6d6/t/5d4469ce32542a0001da654f/1663268739947/4C%2Blogo%2Bwhite.jpg?format=1500w
layout: provider
modified: '2026-09-05'
name: 4C Medical Technologies
nav: Providers
network: true
overview: '4C Medical Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Health, Cardiology, and Structural Heart.


  4C Medical Technologies'' developer surface includes engineering blog and 2 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 4C Medical Technologies Domain Security
  slug: 4c-medical-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: 4c-medical-technologies
tags:
- Company
- Medical Devices
- Health
- Cardiology
- Structural Heart
- Medical Technology
- Clinical Trials
website: https://www.4cmed.com/
---
