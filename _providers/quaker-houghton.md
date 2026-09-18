---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.3
  scored_at: '2026-09-17'
api_count: 2
apis:
- baseURL: https://home.quakerhoughton.com/wp-json/tribe/events/v1
  baseurl_source: declared
  description: The stable Events Calendar v1 REST API on home.quakerhoughton.com, the corporate site, serving its event calendar as JSON — events with dates, venue, organizer, categories and tags. Read access is ano
  name: Quaker Houghton Events API
  slug: quaker-houghton-events-api
- baseURL: https://home.quakerhoughton.com/wp-json/tec/v1
  baseurl_source: declared
  description: 'The newer, experimental Events Calendar `tec/v1` REST namespace on home.quakerhoughton.com: 16 operations across events, venues and organizers, with an OpenAPI 3.0.4 document served live at /wp-json/t'
  name: Quaker Houghton TEC v1 Events API
  slug: quaker-houghton-tec-v1-events-api
- description: A remote Model Context Protocol server served from home.quakerhoughton.com by the WordPress MCP Adapter plugin, discovered through the RFC 8414 and RFC 9728 documents the host publishes under /.well-k
  name: Quaker Houghton MCP Server
  slug: quaker-houghton-mcp-server
artifact_total: 10
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quaker-houghton/refs/heads/main/security/quaker-houghton-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/quaker-houghton/refs/heads/main/well-known/quaker-houghton-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/quaker-houghton-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quaker-houghton/refs/heads/main/mcp/quaker-houghton-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/quaker-houghton-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/quaker-houghton/refs/heads/main/mcp/quaker-houghton-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/quaker-houghton-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quaker-houghton/refs/heads/main/scopes/quaker-houghton-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/quaker-houghton-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quaker-houghton/refs/heads/main/authentication/quaker-houghton-authentication.yml
  title: ''
  type: Authentication
  url: authentication/quaker-houghton-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quaker-houghton/refs/heads/main/conformance/quaker-houghton-conformance.yml
  title: ''
  type: Conformance
  url: conformance/quaker-houghton-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quaker-houghton/refs/heads/main/errors/quaker-houghton-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/quaker-houghton-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quaker-houghton/refs/heads/main/lifecycle/quaker-houghton-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/quaker-houghton-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quaker-houghton/refs/heads/main/conventions/quaker-houghton-conventions.yml
  title: ''
  type: Conventions
  url: conventions/quaker-houghton-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quaker-houghton/refs/heads/main/data-model/quaker-houghton-data-model.yml
  title: ''
  type: DataModel
  url: data-model/quaker-houghton-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quaker-houghton/refs/heads/main/llms/quaker-houghton-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/quaker-houghton-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quaker-houghton/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/quaker-houghton/refs/heads/main/packages/quaker-houghton-packages.yml
  title: ''
  type: Packages
  url: packages/quaker-houghton-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/quaker-houghton/refs/heads/main/plans/quaker-houghton-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/quaker-houghton-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/quaker-houghton/refs/heads/main/rate-limits/quaker-houghton-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/quaker-houghton-rate-limits.yml
created: '2026-04-19'
description: 'Quaker Houghton (NYSE: KWR) is a global industrial process fluids company headquartered in Conshohocken, Pennsylvania, formed by the 2019 combination of Quaker Chemical and Houghton International. It makes metalworking, metal rolling, casting, forging and hydraulic fluids for the steel, aluminum, automotive, aerospace and machinery industries, and sells fluid management services under the QH Fluid Intelligence brand. It publishes no public API, developer portal or machine-readable contract.'
finops:
- name: Quaker Houghton Finops
  service_category: Industrial Fluids
  slug: quaker-houghton-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quaker-houghton.png
layout: provider
mcp_servers:
- description: 'Quaker Houghton serves a remote Model Context Protocol server on its corporate WordPress host. It is not announced anywhere — no MCP registry entry, no documentation page, no llms.txt — and was found '
  name: Quaker Houghton MCP Server
  slug: quaker-houghton-mcp-server
modified: '2026-09-17'
name: Quaker Houghton
nav: Providers
network: true
overview: 'Quaker Houghton publishes 2 APIs on the [APIs.io](https://apis.io/) network: Events API and TEC v1 Events API. Tagged areas include Industrial Fluids, Chemicals, Manufacturing, Metalworking, and Lubricants.


  Quaker Houghton''s developer surface includes support, authentication, and 18 more developer resources.'
plans:
- name: Quaker Houghton Plans Pricing
  plan_count: 1
  slug: quaker-houghton-plans-pricing
random_paper: 8
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
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 15.2
  facets:
    access_clarity: 39.5
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 25.6
    discoverability: 68.5
    operational_transparency: 0.0
  previous_composite: 11.2
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/quaker-houghton/refs/heads/main/screenshots/quaker-houghton-2026-06-20T192359.png
security:
- kind: authentication
  name: Quaker Houghton Authentication
  slug: quaker-houghton-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Quaker Houghton Domain Security
  slug: quaker-houghton-domain-security
  summary_line: TLSv1.3 · DMARC
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
