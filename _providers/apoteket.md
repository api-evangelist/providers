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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apoteket/refs/heads/main/hosts/apoteket-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apoteket-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://www.apoteket.se/tidsperiod/support/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apoteket/refs/heads/main/security/apoteket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apoteket-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.apoteket.se/
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at the API host https://api.apoteket.se/.
  evidence:
  - status: 200
    url: https://api.apoteket.se/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Apoteket is Sweden’s leading pharmacy retailer, operating a nationwide chain of pharmacies and an extensive online store. Founded in 1971, it is a state‑owned enterprise that provides prescription medicines, over‑the‑counter products, health advice, and digital services such as e‑prescriptions and home delivery. The company reinvests profits into public health, education, and social care, reflecting its public‑service mission. Apoteket’s digital platforms offer APIs for product catalogs, order management, and customer accounts, supporting integration with healthcare providers and third‑party services.
layout: provider
modified: '2026-10-12'
name: Apoteket
nav: Providers
network: true
overview: 'Apoteket is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmacy, Healthcare, Sweden, and E-Commerce.


  Apoteket''s developer surface includes support and 3 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apoteket Domain Security
  slug: apoteket-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: apoteket
tags:
- Company
- Pharmacy
- Healthcare
- Sweden
- E-Commerce
website: https://www.apoteket.se/
---
