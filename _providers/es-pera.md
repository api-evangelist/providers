---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://es-pera.org/api/v1
  baseurl_source: declared
  description: Salud y releases fijadas por el despliegue.
  name: ES·pera API Estado API
  slug: es-pera-estado-api
- baseURL: https://es-pera.org/api/v1
  baseurl_source: declared
  description: Métricas, directorio y detalle hospitalario nacional.
  name: ES·pera API Hospitales API
  slug: es-pera-hospitales-api
- baseURL: https://es-pera.org/api/v1
  baseurl_source: declared
  description: Catálogo acotado de listas de espera publicadas por las comunidades autónomas.
  name: ES·pera API Listas autonómicas API
  slug: es-pera-listas-auton-micas-api
artifact_total: 9
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://es-pera.org/actualizaciones/feed.atom
- group: other
  href: https://artifacts.apis.io/es-pera/overlays/es-pera-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/es-pera-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/es-pera/security/es-pera-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/es-pera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://es-pera.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://es-pera.org/metodologia/
- group: docs
  title: ''
  type: Documentation
  url: https://es-pera.org/metodologia/
- group: agent
  href: https://artifacts.apis.io/es-pera/llms/es-pera-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/es-pera-llms.txt
- group: agent
  href: https://artifacts.apis.io/es-pera/well-known/es-pera-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/es-pera-well-known.yml
- group: agent
  href: https://artifacts.apis.io/es-pera/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/es-pera/authentication/es-pera-authentication.yml
  title: ''
  type: Authentication
  url: authentication/es-pera-authentication.yml
- group: design
  href: https://artifacts.apis.io/es-pera/conventions/es-pera-conventions.yml
  title: ''
  type: Conventions
  url: conventions/es-pera-conventions.yml
- group: operate
  href: https://artifacts.apis.io/es-pera/rate-limits/es-pera-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/es-pera-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/es-pera/conformance/es-pera-conformance.yml
  title: ''
  type: Conformance
  url: conformance/es-pera-conformance.yml
- group: design
  href: https://artifacts.apis.io/es-pera/errors/es-pera-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/es-pera-problem-types.yml
- group: design
  href: https://artifacts.apis.io/es-pera/lifecycle/es-pera-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/es-pera-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/es-pera/data-model/es-pera-data-model.yml
  title: ''
  type: DataModel
  url: data-model/es-pera-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/es-pera/plans/es-pera-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/es-pera-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/es-pera/changelog/es-pera-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/es-pera-changelog.yml
- group: agent
  href: https://artifacts.apis.io/es-pera/mcp/es-pera-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/es-pera-mcp.yml
created: '2026-09-13'
description: ES·pera is an independent Spanish-language observatory that gathers scattered official Spanish National Health System (SNS) and autonomous-community publications on healthcare waiting lists and hospital activity, and republishes them as comparable, provenance-preserving open data. It exposes a free, open, unauthenticated read-only REST API (OpenAPI 3.1 at /api/v1) covering hospital entities, national activity metrics and autonomous waiting-list observations, served from immutable content-addressed data releases. Discovery is via an RFC 9727 API catalog, an llms.txt, and a provider-published Agent Skill; there is no MCP server, no A2A agent card, and no client SDK.
image: https://es-pera.org/favicon-espera.svg
layout: provider
modified: '2026-10-06'
name: ES·pera API
nav: Providers
network: true
overview: 'ES·pera API publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Estado API, Hospitales API, and Listas autonómicas API. Tagged areas include Healthcare, Open Data, Waiting Lists, hospital activity, and Spain.


  The ES·pera API catalog on APIs.io includes 1 Spectral governance ruleset.


  ES·pera API''s developer surface includes documentation, authentication, changelog, and 16 more developer resources.'
plans:
- name: Es Pera Plans Pricing
  plan_count: 0
  slug: es-pera-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Es Pera Rate Limits
  slug: es-pera-rate-limits
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: ES·pera API API Rules
  rule_count: 41
  severity_counts:
    error: 38
    hint: 0
    info: 2
    warn: 1
  slug: es-pera-rules
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 46.5
    catalog_earned_first_party: 8.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 0.0
    contract_governance: 13.6
    contract_quality: 46.9
    developer_ergonomics: 45.2
    discoverability: 67.9
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 33.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/es-pera/es-pera-2026-10-11T104252.png
security:
- kind: authentication
  name: Es Pera Authentication
  slug: es-pera-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Es Pera Domain Security
  slug: es-pera-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: es-pera-public-data
  slug: es-pera-public-data
slug: es-pera
tags:
- Healthcare
- Open Data
- Waiting Lists
- hospital activity
- Spain
- Public Sector
- Government Data
- SNS
website: https://es-pera.org/
---
