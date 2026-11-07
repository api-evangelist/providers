---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
    agent_skills: derived
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
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://curatorsearch.com
  baseurl_source: spec
  description: The Data API from CuratorSearch — 1 operation(s) for data.
  name: CuratorSearch Data API
  slug: curatorsearch-data-api
- baseURL: https://curatorsearch.com
  baseurl_source: spec
  description: The Jobs API from CuratorSearch — 2 operation(s) for jobs.
  name: CuratorSearch Jobs API
  slug: curatorsearch-jobs-api
artifact_total: 10
common:
- group: other
  href: https://artifacts.apis.io/curatorsearch/capabilities/curatorsearch-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/curatorsearch-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/curatorsearch/mcp/curatorsearch-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/curatorsearch-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://curatorsearch.com/mcp
- group: company
  title: ''
  type: Website
  url: https://curatorsearch.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://curatorsearch.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://curatorsearch.com/developers
- group: operate
  title: ''
  type: Support
  url: https://curatorsearch.com/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://curatorsearch.com/developers#attribution
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://curatorsearch.com/privacy
- group: agent
  href: https://artifacts.apis.io/curatorsearch/well-known/curatorsearch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/curatorsearch-well-known.yml
- group: auth
  href: https://artifacts.apis.io/curatorsearch/authentication/curatorsearch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/curatorsearch-authentication.yml
- group: design
  href: https://artifacts.apis.io/curatorsearch/conventions/curatorsearch-conventions.yml
  title: ''
  type: Conventions
  url: conventions/curatorsearch-conventions.yml
- group: design
  href: https://artifacts.apis.io/curatorsearch/lifecycle/curatorsearch-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/curatorsearch-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/curatorsearch/conformance/curatorsearch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/curatorsearch-conformance.yml
- group: design
  href: https://artifacts.apis.io/curatorsearch/errors/curatorsearch-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/curatorsearch-problem-types.yml
- group: design
  href: https://artifacts.apis.io/curatorsearch/data-model/curatorsearch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/curatorsearch-data-model.yml
- group: agent
  href: https://artifacts.apis.io/curatorsearch/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/curatorsearch/overlays/curatorsearch-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/curatorsearch-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/curatorsearch/components/curatorsearch-components.yml
  title: ''
  type: Components
  url: components/curatorsearch-components.yml
- group: commercial
  href: https://artifacts.apis.io/curatorsearch/plans/curatorsearch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/curatorsearch-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/curatorsearch/rate-limits/curatorsearch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/curatorsearch-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/curatorsearch/security/curatorsearch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curatorsearch-domain-security.yml
- group: build
  href: https://artifacts.apis.io/curatorsearch/mcp/curatorsearch-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/curatorsearch-tool-crosswalk.yml
- group: other
  title: ''
  type: RSS
  url: https://curatorsearch.com/feed.xml
created: '2026-09-19'
description: An independent, daily-refreshed record of museum/gallery/curatorial vacancies and advertised salaries, aggregated from 400+ institutions' careers pages. Exposes a keyless REST/JSON API, an OpenAPI 3.1 contract, a hosted MCP server, llms.txt, open datasets (CC BY 4.0, with DOI), and RSS.
image: https://curatorsearch.com/icon.png
layout: provider
mcp_servers:
- description: Official hosted MCP server for CuratorSearch. Stateless Streamable HTTP (POST) endpoint on the provider's primary domain, no key required. Live tools/list retrieved anonymously and saved verbatim to m
  name: CuratorSearch MCP Server
  slug: curatorsearch
modified: '2026-09-20'
name: CuratorSearch
nav: Providers
network: true
overview: 'CuratorSearch publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Data API and Jobs API. Tagged areas include Agent-Native, MCP, OpenAPI, Llms.txt, and Open Data.


  The CuratorSearch catalog on APIs.io includes 1 Spectral governance ruleset.


  CuratorSearch''s developer surface includes documentation, support, authentication, and 21 more developer resources.'
plans:
- name: Curatorsearch Plans Pricing
  plan_count: 0
  slug: curatorsearch-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Curatorsearch Rate Limits
  slug: curatorsearch-rate-limits
rules:
- authorship: generated
  effective_rule_count: 73
  extends:
  - spectral:oas
  name: CuratorSearch API Rules
  rule_count: 32
  severity_counts:
    error: 30
    hint: 0
    info: 1
    warn: 1
  slug: curatorsearch-rules
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 10.5
    contract_governance: 31.8
    contract_quality: 44.2
    developer_ergonomics: 25.6
    discoverability: 66.7
    operational_transparency: 0.0
  previous_composite: 33.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/curatorsearch/curatorsearch-2026-10-11T103432.png
security:
- kind: authentication
  name: Curatorsearch Authentication
  slug: curatorsearch-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Curatorsearch Domain Security
  slug: curatorsearch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: check-pay-transparency
  slug: curatorsearch-check-pay-transparency
- name: find-museum-jobs
  slug: curatorsearch-find-museum-jobs
slug: curatorsearch
tags:
- Agent-Native
- MCP
- OpenAPI
- Llms.txt
- Open Data
- Job
- Cultural Heritage
- Museums
- curatorial
- salary-transparency
- glam
- museum jobs
- Job Board
- Salaries
- Pay Transparency
- Datasets
- RSS
website: https://curatorsearch.com
---
