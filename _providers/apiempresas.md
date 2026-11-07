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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/apiempresas/hosts/apiempresas-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apiempresas-hosts.yml
- group: other
  href: https://artifacts.apis.io/apiempresas/vendors/apiempresas-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apiempresas-vendors.yml
- group: build
  href: https://artifacts.apis.io/apiempresas/packages/apiempresas-packages.yml
  title: ''
  type: SDKs
  url: packages/apiempresas-packages.yml
- group: build
  href: https://artifacts.apis.io/apiempresas/packages/apiempresas-packages.yml
  title: ''
  type: Packages
  url: packages/apiempresas-packages.yml
- group: auth
  href: https://artifacts.apis.io/apiempresas/security/apiempresas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apiempresas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apiempresas.es/
created: '2026-10-30'
description: APIEmpresas provides APIs that give access to Spanish company data, including registration details, tax identifiers, risk profiles, and related business information. The service offers endpoints for searching companies by CIF/NIF, retrieving activity status, accessing a comprehensive database of enterprises, and obtaining risk assessments. Documentation indicates support for integration via WordPress plugins and other tools, and the platform appears to expose OpenAPI specifications and llms.txt for developers. The site is protected by Cloudflare, and robots.txt lists allowed API paths such as /buscar-empresa-por-cif, /como-saber-si-una-empresa-esta-activa, /perfil-de-riesgo, and /fuentes-de-datos, reflecting a focus on business intelligence and compliance data.
layout: provider
modified: '2026-10-30'
name: APIEmpresas
nav: Providers
network: true
overview: APIEmpresas is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Company Data, Risk Assessment, and Spanish.
random_paper: 2
score:
  band: minimal
  composite: 3.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 35.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 4.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apiempresas Domain Security
  slug: apiempresas-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apiempresas
tags:
- Company
- Company Data
- Risk Assessment
- Spanish
website: https://apiempresas.es/
---
