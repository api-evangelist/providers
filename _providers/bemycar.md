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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bemycar/refs/heads/main/hosts/bemycar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bemycar-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bemycar/refs/heads/main/vendors/bemycar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bemycar-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bemycar/refs/heads/main/security/bemycar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bemycar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bemycar.pro
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bemycar.pro/privacidad/
- group: commercial
  title: ''
  type: LegalNotice
  url: https://bemycar.pro/aviso-legal/
coverage:
  checked: '2026-09-27'
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine-readable contract was found at the API host.
  evidence:
  - status: error
    url: https://api.bemycar.pro/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Bemycar develops and commercializes generative artificial intelligence technology to maximize efficiency and increase sales for companies in the automotive and mobility sectors. Their solutions include AI-driven lead management, enriched lead capture, automated record reactivation, and automated NPS surveys, all delivered via a cloud platform tailored for the automotive industry.
image: https://bemycar.pro/wp-content/uploads/2024/05/Iogo_verde-nuevo_fono-blanco-morado.png
layout: provider
modified: '2026-09-27'
name: Bemycar
nav: Providers
network: true
overview: Bemycar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Artificial Intelligence, Lead Management, and Mobility.
random_paper: 13
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bemycar Domain Security
  slug: bemycar-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bemycar
tags:
- Company
- Automotive
- Artificial Intelligence
- Lead Management
- Mobility
website: https://bemycar.pro
---
