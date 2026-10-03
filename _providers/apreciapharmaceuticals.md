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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apreciapharmaceuticals/refs/heads/main/hosts/apreciapharmaceuticals-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apreciapharmaceuticals-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aprecia.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aprecia.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://aprecia.com/resources/news/tradeshow-flyer/
- group: other
  title: ''
  type: Leadership
  url: https://aprecia.com/team/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apreciapharmaceuticals/refs/heads/main/security/apreciapharmaceuticals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apreciapharmaceuticals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aprecia.com
coverage:
  checked: 2026-09-25
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.aprecia.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Apreciapharmaceuticals, operating as Aprecia Pharmaceuticals, is a pioneering specialty CDMO focused on 3D‑printed drug manufacturing. Founded in 2003 and based in Langhorne, PA, the company offers end‑to‑end development, clinical‑trial supply, and commercial‑scale production using FDA‑registered cGMP facilities. It is the world’s first to secure regulatory approval for a 3D‑printed medication (SPRITAM®) and continues to innovate in precision formulation, rapid prototyping, and flexible manufacturing to accelerate patient‑centered drug development.
image: https://aprecia.com/wp-content/uploads/2025/02/Aprecia-Logo-RGB_Horizontal-Full_Color.png
layout: provider
modified: '2026-09-25'
name: Apreciapharmaceuticals
nav: Providers
network: true
overview: Apreciapharmaceuticals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, 3D Printing, CDMO, and FDA.
random_paper: 5
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apreciapharmaceuticals Domain Security
  slug: apreciapharmaceuticals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apreciapharmaceuticals
tags:
- Company
- Pharmaceuticals
- 3D Printing
- CDMO
- FDA
website: https://aprecia.com
---
