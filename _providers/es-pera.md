---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.6
  scored_at: '2026-09-14'
api_count: 1
apis:
- baseURL: https://es-pera.org/api/v1
  baseurl_source: declared
  description: 'Open, unauthenticated read-only REST API (GET/HEAD, JSON) over SNS hospital and autonomous-community waiting-list open data. Nine operations across health/releases, hospital entities and metrics, and '
  name: ES·pera Public Data API
  slug: espera-public-data-api
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/es-pera/refs/heads/main/security/es-pera-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/es-pera/refs/heads/main/llms/es-pera-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/es-pera-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/es-pera/refs/heads/main/well-known/es-pera-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/es-pera-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/es-pera/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/es-pera/refs/heads/main/authentication/es-pera-authentication.yml
  title: ''
  type: Authentication
  url: authentication/es-pera-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/es-pera/refs/heads/main/conventions/es-pera-conventions.yml
  title: ''
  type: Conventions
  url: conventions/es-pera-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/es-pera/refs/heads/main/rate-limits/es-pera-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/es-pera-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/es-pera/refs/heads/main/conformance/es-pera-conformance.yml
  title: ''
  type: Conformance
  url: conformance/es-pera-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/es-pera/refs/heads/main/errors/es-pera-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/es-pera-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/es-pera/refs/heads/main/lifecycle/es-pera-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/es-pera-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/es-pera/refs/heads/main/data-model/es-pera-data-model.yml
  title: ''
  type: DataModel
  url: data-model/es-pera-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/es-pera/refs/heads/main/plans/es-pera-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/es-pera-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/es-pera/refs/heads/main/changelog/es-pera-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/es-pera-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/es-pera/refs/heads/main/mcp/es-pera-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/es-pera-mcp.yml
created: '2026-09-13'
description: ES·pera is an independent Spanish-language observatory that gathers scattered official Spanish National Health System (SNS) and autonomous-community publications on healthcare waiting lists and hospital activity, and republishes them as comparable, provenance-preserving open data. It exposes a free, open, unauthenticated read-only REST API (OpenAPI 3.1 at /api/v1) covering hospital entities, national activity metrics and autonomous waiting-list observations, served from immutable content-addressed data releases. Discovery is via an RFC 9727 API catalog, an llms.txt, and a provider-published Agent Skill; there is no MCP server, no A2A agent card, and no client SDK.
image: https://es-pera.org/favicon-espera.svg
layout: provider
modified: '2026-09-13'
name: ES·pera API
nav: Providers
network: true
overview: 'ES·pera API publishes 1 API on the [APIs.io](https://apis.io/) network: ES·pera Public Data API. Tagged areas include Healthcare, Open Data, Waiting Lists, hospital activity, and Spain.


  ES·pera API''s developer surface includes documentation, authentication, changelog, and 14 more developer resources.'
plans:
- name: Es Pera Plans Pricing
  plan_count: 0
  slug: es-pera-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Es Pera Rate Limits
  slug: es-pera-rate-limits
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.0
    catalog_earned_first_party: 8.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 45.2
    discoverability: 70.4
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 34.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Es Pera Authentication
  slug: es-pera-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Es Pera Domain Security
  slug: es-pera-domain-security
  summary_line: TLSv1.3
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
