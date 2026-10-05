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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API documentation not publicly available; no machine-readable contract discovered.
  name: BlueWillow Biologics API
  slug: bluewillow-biologics-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bluewillow-biologics/refs/heads/main/hosts/bluewillow-biologics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluewillow-biologics-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bluewillow-biologics/refs/heads/main/security/bluewillow-biologics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluewillow-biologics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluewillow.com/
- group: company
  title: ''
  type: About
  url: https://bluewillow.com/about-nanobio/
- group: company
  title: ''
  type: News
  url: https://bluewillow.com/news/
- group: operate
  title: ''
  type: Contact
  url: https://bluewillow.com/contact/
coverage:
  checked: '2026-09-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found on discovered hosts.
  evidence:
  - status: 0
    url: https://api.bluewillow.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: BlueWillow Biologics is a clinical‑stage biotechnology company pioneering intranasal vaccine technology. Their NanoVax® platform delivers antigens via an oil‑in‑water emulsion, aiming to transform prevention and treatment of infectious diseases, pandemic preparedness, and food allergies. The company originated from University of Michigan research and now advances human clinical trials of its adjuvant and delivery system.
image: https://bluewillow.com/wp-content/uploads/2020/03/BlueWillow-Logo.jpg
layout: provider
modified: '2026-09-29'
name: BlueWillow Biologics
nav: Providers
network: true
overview: 'BlueWillow Biologics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Intranasal Vaccines, Clinical Stage, Nanotechnology, and Health.


  BlueWillow Biologics'' developer surface includes product news and 5 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bluewillow Biologics Domain Security
  slug: bluewillow-biologics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bluewillow-biologics
tags:
- Biotechnology
- Intranasal Vaccines
- Clinical Stage
- Nanotechnology
- Health
- Company
website: https://bluewillow.com/
---
