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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API documentation is not publicly machine‑readable; the website returns a JavaScript shell with no accessible OpenAPI or other contract.
  name: BrainsGate API
  slug: brainsgate-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brainsgate/refs/heads/main/hosts/brainsgate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainsgate-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brainsgate/refs/heads/main/security/brainsgate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainsgate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.brainsgate.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.brainsgate.com
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: BrainsGate is a medical device company focused on developing innovative therapies for central nervous system (CNS) diseases. Their platform technology uses electrical stimulation of the Spheno‑Palatine Ganglion (SPG) to increase cerebral blood flow, targeting applications such as acute ischemic stroke and chronic vascular dementia. The company is based in Israel and aims to bring novel neuro‑stimulation treatments to patients worldwide.
layout: provider
modified: '2026-10-03'
name: BrainsGate
nav: Providers
network: true
overview: BrainsGate is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Devices, Neurotechnology, CNS Therapy, Israel, and Innovation.
random_paper: 0
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - israel
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 4.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brainsgate Domain Security
  slug: brainsgate-domain-security
  summary_line: no transport/DNS hardening detected
slug: brainsgate
tags:
- Medical Devices
- Neurotechnology
- CNS Therapy
- Israel
- Innovation
website: http://www.brainsgate.com
---
