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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Developer portal for Odynn providing API documentation (no machine-readable spec found).
  name: Odynn API
  slug: odynn-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/odynn/hosts/odynn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/odynn-hosts.yml
- group: other
  href: https://artifacts.apis.io/odynn/vendors/odynn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/odynn-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.odynn.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.odynn.com/legal/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.odynn.com/press/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.odynn.com/
- group: auth
  href: https://artifacts.apis.io/odynn/security/odynn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/odynn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://odynn.com
coverage:
  checked: '2026-10-25'
  detail: Developer portal provides HTML docs but no OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract.
  evidence:
  - status: 200
    url: https://developer.odynn.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Odynn offers an AI‑native, white‑label platform that enables neobanks, card issuers, fintechs and other financial institutions to embed travel booking, rewards and loyalty services directly into their products. The solution includes modular APIs, an agentic SDK and white‑label travel search, allowing partners to launch travel portals and loyalty programs in weeks rather than months.
image: https://www.odynn.com/opengraph-image.png?opengraph-image.19x-b_mx0w3t_.png
layout: provider
modified: '2026-10-25'
name: Odynn
nav: Providers
network: true
overview: 'Odynn is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Loyalty, Fintech, White‑label, and API.


  Odynn''s developer surface includes documentation and 7 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Odynn Domain Security
  slug: odynn-domain-security
  summary_line: TLSv1.3 · DMARC
slug: odynn
tags:
- Travel
- Loyalty
- Fintech
- White‑label
- API
- SDK
website: https://odynn.com
---
