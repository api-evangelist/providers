---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the Quaker Houghton website at home.quakerhoughton.com: the route index of the site''s content management system, catalogued as one site surface rather than a'
  name: Quaker Houghton Website (WordPress REST)
  slug: home-quakerhoughton-com-website-wordpress-rest
- description: A remote Model Context Protocol server served from home.quakerhoughton.com by the WordPress MCP Adapter plugin, discovered through the RFC 8414 and RFC 9728 documents the host publishes under /.well-k
  name: Quaker Houghton MCP Server
  slug: quaker-houghton-mcp-server
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/quaker-houghton/finops/quaker-houghton-finops.yml
  title: ''
  type: FinOps
  url: finops/quaker-houghton-finops.yml
- group: auth
  href: https://artifacts.apis.io/quaker-houghton/security/quaker-houghton-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quaker-houghton-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quakerhoughton
- group: company
  title: ''
  type: Website
  url: https://home.quakerhoughton.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://home.quakerhoughton.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://home.quakerhoughton.com/contact/
- group: agent
  href: https://artifacts.apis.io/quaker-houghton/well-known/quaker-houghton-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/quaker-houghton-well-known.yml
- group: agent
  href: https://artifacts.apis.io/quaker-houghton/mcp/quaker-houghton-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/quaker-houghton-mcp.yml
- group: build
  href: https://artifacts.apis.io/quaker-houghton/mcp/quaker-houghton-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/quaker-houghton-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/quaker-houghton/scopes/quaker-houghton-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/quaker-houghton-scopes.yml
- group: auth
  href: https://artifacts.apis.io/quaker-houghton/authentication/quaker-houghton-authentication.yml
  title: ''
  type: Authentication
  url: authentication/quaker-houghton-authentication.yml
- group: design
  href: https://artifacts.apis.io/quaker-houghton/conformance/quaker-houghton-conformance.yml
  title: ''
  type: Conformance
  url: conformance/quaker-houghton-conformance.yml
- group: design
  href: https://artifacts.apis.io/quaker-houghton/errors/quaker-houghton-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/quaker-houghton-problem-types.yml
- group: design
  href: https://artifacts.apis.io/quaker-houghton/lifecycle/quaker-houghton-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/quaker-houghton-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/quaker-houghton/conventions/quaker-houghton-conventions.yml
  title: ''
  type: Conventions
  url: conventions/quaker-houghton-conventions.yml
- group: design
  href: https://artifacts.apis.io/quaker-houghton/data-model/quaker-houghton-data-model.yml
  title: ''
  type: DataModel
  url: data-model/quaker-houghton-data-model.yml
- group: agent
  href: https://artifacts.apis.io/quaker-houghton/llms/quaker-houghton-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/quaker-houghton-llms.txt
- group: agent
  href: https://artifacts.apis.io/quaker-houghton/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/quaker-houghton/packages/quaker-houghton-packages.yml
  title: ''
  type: Packages
  url: packages/quaker-houghton-packages.yml
- group: commercial
  href: https://artifacts.apis.io/quaker-houghton/plans/quaker-houghton-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/quaker-houghton-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/quaker-houghton/rate-limits/quaker-houghton-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/quaker-houghton-rate-limits.yml
created: '2026-04-19'
description: 'Quaker Houghton (NYSE: KWR) is a global industrial process fluids company headquartered in Conshohocken, Pennsylvania, formed by the 2019 combination of Quaker Chemical and Houghton International. It makes metalworking, metal rolling, casting, forging and hydraulic fluids for the steel, aluminum, automotive, aerospace and machinery industries, and sells fluid management services under the QH Fluid Intelligence brand. It publishes no public API, developer portal or machine-readable contract.'
finops:
- has_sources: true
  method: generated
  name: Quaker Houghton Finops
  primary_unit: ''
  service_category: Industrial Fluids
  slug: quaker-houghton-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quaker-houghton.png
layout: provider
mcp_servers:
- description: 'Quaker Houghton serves a remote Model Context Protocol server on its corporate WordPress host. It is not announced anywhere — no MCP registry entry, no documentation page, no llms.txt — and was found '
  name: Quaker Houghton MCP Server
  slug: quaker-houghton
modified: '2026-09-17'
name: Quaker Houghton
nav: Providers
network: true
overview: 'Quaker Houghton publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Industrial Fluids, Chemicals, Manufacturing, Metalworking, and Lubricants.


  Quaker Houghton''s developer surface includes support, authentication, and 19 more developer resources.'
plans:
- name: Quaker Houghton Plans Pricing
  plan_count: 1
  slug: quaker-houghton-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Quaker Houghton Rate Limits
  slug: quaker-houghton-rate-limits
scopes:
- name: Quaker Houghton Scopes
  scope_count: 1
  slug: quaker-houghton-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 23.2
    discoverability: 60.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 20.0
  provenance:
    conformance: derived
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/quaker-houghton/quaker-houghton-2026-06-20T192359.png
security:
- kind: authentication
  name: Quaker Houghton Authentication
  slug: quaker-houghton-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Quaker Houghton Domain Security
  slug: quaker-houghton-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: List Quaker Houghton upcoming events
  slug: quaker-houghton-list-upcoming-events
slug: quaker-houghton
tags:
- Industrial Fluids
- Chemicals
- Manufacturing
- Metalworking
- Lubricants
- Event
- MCP
website: https://home.quakerhoughton.com/
---
