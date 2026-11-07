---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Drconsulta2 Agentic Access
  operation_count: 3
  slug: drconsulta2-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- baseURL: https://integracaoprodutosapi.drconsulta.com
  baseurl_source: declared
  description: The Autenticação API from Drconsulta2 — 1 operation(s) for autenticação.
  name: Drconsulta2 Autenticação API
  slug: drconsulta2-autentica-o-api
- baseURL: https://integracaoprodutosapi.drconsulta.com
  baseurl_source: declared
  description: Gets data from Oracle
  name: Drconsulta2 Oracle API
  slug: drconsulta2-oracle-api
- baseURL: https://integracaoprodutosapi.drconsulta.com
  baseurl_source: declared
  description: Gets data from S2
  name: Drconsulta2 S2 API
  slug: drconsulta2-s2-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/drconsulta2/agentic-access/drconsulta2-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/drconsulta2-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/drconsulta2/rules/drconsulta2-rules.yml
  title: ''
  type: Spectral
  url: rules/drconsulta2-rules.yml
- group: design
  href: https://artifacts.apis.io/drconsulta2/vocabulary/drconsulta2-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/drconsulta2-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/drconsulta2/errors/drconsulta2-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/drconsulta2-problem-types.yml
- group: design
  href: https://artifacts.apis.io/drconsulta2/conformance/drconsulta2-conformance.yml
  title: ''
  type: Conformance
  url: conformance/drconsulta2-conformance.yml
- group: other
  href: https://artifacts.apis.io/drconsulta2/hosts/drconsulta2-hosts.yml
  title: ''
  type: Hosts
  url: hosts/drconsulta2-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DrConsulta
- group: auth
  href: https://artifacts.apis.io/drconsulta2/authentication/drconsulta2-authentication.yml
  title: ''
  type: Authentication
  url: authentication/drconsulta2-authentication.yml
- group: auth
  href: https://artifacts.apis.io/drconsulta2/security/drconsulta2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drconsulta2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drconsulta.com
created: '2026-10-24'
description: Drconsulta2 is a Brazilian telemedicine platform that connects patients with doctors for online consultations, examinations, and health monitoring. It offers a network of medical professionals, a scheduling system, and digital health records, aiming to provide accessible and affordable healthcare services across Brazil.
layout: provider
modified: '2026-10-24'
name: Drconsulta2
nav: Providers
network: true
overview: 'Drconsulta2 publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Autenticação API, Oracle API, and S2 API. Tagged areas include Company.


  The Drconsulta2 catalog on APIs.io includes 1 Spectral governance ruleset.


  Drconsulta2''s developer surface includes authentication and 9 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Drconsulta2 API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: drconsulta2-rules
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 40.6
    developer_ergonomics: 11.9
    discoverability: 53.6
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 20.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/drconsulta2/drconsulta2-2026-11-03T131027.png
security:
- kind: authentication
  name: Drconsulta2 Authentication
  slug: drconsulta2-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Drconsulta2 Domain Security
  slug: drconsulta2-domain-security
  summary_line: TLSv1.3 · DMARC
slug: drconsulta2
tags:
- Company
website: https://drconsulta.com
---
