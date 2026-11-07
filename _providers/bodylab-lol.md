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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/bodylab-lol/well-known/bodylab-lol-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bodylab-lol-well-known.yml
- group: other
  href: https://artifacts.apis.io/bodylab-lol/hosts/bodylab-lol-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bodylab-lol-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bodylab.lol/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bodylab.lol/privacy
- group: start
  title: ''
  type: Login
  url: https://bodylab.lol/login
- group: auth
  href: https://artifacts.apis.io/bodylab-lol/security/bodylab-lol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bodylab-lol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bodylab.lol/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were discoverable at the API host.
  evidence:
  - status: 0
    url: https://api.bodylab.lol/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Body Lab provides a web‑based platform that reads your training load and morning recovery to prescribe one daily workout. It balances strength and endurance for long‑term performance, offering free access with metric‑backed recommendations. The service targets cyclists, runners, hikers and lifters, emphasizing data‑driven training and transparent performance metrics.
image: https://bodylab.lol/opengraph-image?34d8015f90ca75d2
layout: provider
modified: '2026-11-02'
name: Body Lab
nav: Providers
network: true
overview: Body Lab is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fitness, Health, Training, Free, and Company.
random_paper: 1
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bodylab Lol Domain Security
  slug: bodylab-lol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bodylab-lol
tags:
- Fitness
- Health
- Training
- Free
- Company
website: https://bodylab.lol/
---
