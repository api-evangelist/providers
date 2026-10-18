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
- description: API information not publicly documented.
  name: If Insurance API
  slug: if-insurance-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/if-se/refs/heads/main/hosts/if-se-hosts.yml
  title: ''
  type: Hosts
  url: hosts/if-se-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/if-se/refs/heads/main/security/if-se-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/if-se-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://if.se/
coverage:
  checked: '2026-10-15'
  detail: OpenAPI spec endpoints return redirects or HTML, no machine‑readable contract discovered.
  evidence:
  - status: 0
    url: https://api.if.se/openapi.json
  - status: 301
    url: https://if.se/openapi.json
  - status: 302
    url: https://minasidor.if.se/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: If Insurance is a leading insurance provider in the Nordics, offering a wide range of personal and corporate insurance products including home, vehicle, health, and travel coverage. The company focuses on digital customer experiences, providing online policy management, claims handling, and personalized advice through its web portal and mobile apps. With a strong market presence and commitment to innovation, If Insurance serves millions of customers across several European countries.
image: https://v.imgi.no/55jb4pnnr7-MOODBOARD/2042
layout: provider
modified: '2026-10-15'
name: If Insurance
nav: Providers
network: true
overview: If Insurance is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Nordic, Digital, and Finance.
random_paper: 6
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 4
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
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 5.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: If Se Domain Security
  slug: if-se-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: if-se
tags:
- Company
- Insurance
- Nordic
- Digital
- Finance
website: https://if.se/
---
