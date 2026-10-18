---
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/correos/refs/heads/main/well-known/correos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/correos-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/correos/refs/heads/main/hosts/correos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/correos-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/correos/refs/heads/main/vendors/correos-vendors.yml
  title: ''
  type: Vendors
  url: vendors/correos-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/correos/refs/heads/main/security/correos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/correos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.correos.es
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.correos.es/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.correos.es/s/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.correos.es/s/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.correos.es/s/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.correos.es/s/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developers.correos.es/s/privacidad-web
coverage:
  checked: '2026-10-13'
  detail: Developer portal pages are rendered via JavaScript and provide no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://developers.correos.es/s/?language=es
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Correos is the national postal service of Spain, offering a wide range of mailing, parcel, and logistics solutions. Its digital platform provides APIs for tracking shipments, locating offices, managing Citypaq lockers, and accessing e‑commerce services. The company also runs a developer portal with documentation, sandbox environments, and support resources for integrating its services into applications.
image: https://www.correos.es/content/dam/correos/imagenes/iconos/CORREOS-1000x1000.png
layout: provider
modified: '2026-10-13'
name: Correos
nav: Providers
network: true
overview: 'Correos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Postal, Logistics, and Spain.


  Correos'' developer surface includes documentation, API reference, getting-started guide, and 8 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Correos Domain Security
  slug: correos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: correos
tags:
- Company
- Postal
- Logistics
- Spain
website: https://www.correos.es
---
