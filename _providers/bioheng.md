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
- description: Imviva provides an API platform but no machine‑readable contract was discovered. The website lists product information but no developer documentation or OpenAPI spec is publicly available.
  name: Bioheng API
  slug: bioheng-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bioheng/refs/heads/main/hosts/bioheng-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bioheng-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bioheng/refs/heads/main/security/bioheng-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bioheng-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.imvivabio.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/bioheng
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: Bioheng, operating under the brand Imviva, is a clinical-stage biotechnology company focused on developing allogeneic CAR‑T cell therapies for oncology and autoimmune diseases. The company aims to create scalable, off‑the‑shelf cell therapies to broaden patient access and advance regenerative medicine.
layout: provider
modified: '2026-09-28'
name: Bioheng
nav: Providers
network: true
overview: Bioheng publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Cell Therapy, Oncology, Autoimmune Disease, and Clinical Stage.
random_paper: 6
score:
  band: minimal
  composite: 4.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Bioheng Domain Security
  slug: bioheng-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bioheng
tags:
- Biotechnology
- Cell Therapy
- Oncology
- Autoimmune Disease
- Clinical Stage
website: https://www.imvivabio.com
---
