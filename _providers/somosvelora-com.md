---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: near-conformant
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Model Context Protocol (MCP) server exposing ARCA invoicing, MercadoPago payments, and logistics via a single endpoint.
  name: Velora MCP
  slug: velora-mcp
- baseURL: https://tools.somosvelora.com
  baseurl_source: declared
  description: 'somosvelora-com API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: somosvelora-com API
  slug: somosvelora-com-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/somosvelora-com/rules/somosvelora-com-rules.yml
  title: ''
  type: Spectral
  url: rules/somosvelora-com-rules.yml
- group: design
  href: https://artifacts.apis.io/somosvelora-com/json-ld/somosvelora-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/somosvelora-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/somosvelora-com/vocabulary/somosvelora-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/somosvelora-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/somosvelora-com/data-model/somosvelora-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/somosvelora-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/somosvelora-com/conformance/somosvelora-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/somosvelora-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/somosvelora-com/llms/somosvelora-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/somosvelora-com-llms.txt
- group: other
  href: https://artifacts.apis.io/somosvelora-com/a2a/somosvelora-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/somosvelora-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/somosvelora-com/mcp/somosvelora-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/somosvelora-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/somosvelora-com/well-known/somosvelora-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/somosvelora-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/somosvelora-com/hosts/somosvelora-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/somosvelora-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/somosvelora-com/vendors/somosvelora-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/somosvelora-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://somosvelora.com/security
- group: auth
  href: https://artifacts.apis.io/somosvelora-com/security/somosvelora-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/somosvelora-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://somosvelora.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://somosvelora.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://somosvelora.com/developers
- group: company
  title: ''
  type: Blog
  url: https://somosvelora.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crossi-dev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://somosvelora.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://somosvelora.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://tools.somosvelora.com/api/mcp
  - status: 401
    url: https://somosvelora.com/mcp
  - status: 200
    url: https://somosvelora.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Velora is an agentic commerce platform that enables businesses to sell, charge, invoice and ship end‑to‑end using AI agents. It operates via the Model Context Protocol (MCP) and integrates with WhatsApp, MercadoPago, ARCA and other services. Users can interact through the Velora app, ChatGPT, Claude or Gemini. The platform provides public MCP tools, a sandbox, and a developer portal with documentation and an open‑source GitHub repository. Built on Google Cloud, it offers cryptographic identity, auditability, and compliance with Argentine fiscal regulations.
image: https://somosvelora.com/opengraph-image?6f6fcc4766c7fbdc
json_schemas:
- name: PostApiMcpPublicRequest
  property_count: 4
  slug: somosvelora-com-post-api-mcp-public-request
- name: Velora Mcp Tools
  property_count: 0
  slug: velora-mcp-tools
jsonld:
- class_count: 1
  name: Somosvelora Com Context
  property_count: 4
  slug: somosvelora-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at tools.somosvelora.com.
  name: somosvelora-com MCP Server
  slug: somosvelora-com-mcp-yml
modified: '2026-10-30'
name: somosvelora-com
nav: Providers
network: true
overview: 'somosvelora-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Commerce, AI Agents, Argentina, and MCP.


  The somosvelora-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  somosvelora-com''s developer surface includes documentation, engineering blog, and 18 more developer resources.'
plans:
- name: Somosvelora Com Plans Pricing
  plan_count: 0
  slug: somosvelora-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Somosvelora Com Rate Limits
  slug: somosvelora-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: somosvelora-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: somosvelora-com-rules
scopes:
- name: Somosvelora Com Scopes
  scope_count: 0
  slug: somosvelora-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 31
    catalog_earned: 53.2
    catalog_earned_first_party: 0.0
    catalog_gap: 61.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 17.8
    developer_ergonomics: 10.7
    discoverability: 75.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - argentina
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/somosvelora-com/somosvelora-com-2026-11-03T143517.png
security:
- kind: authentication
  name: Somosvelora Com Authentication
  slug: somosvelora-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Somosvelora Com Domain Security
  slug: somosvelora-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: somosvelora-com
tags:
- Artificial Intelligence
- Commerce
- AI Agents
- Argentina
- MCP
- Company
website: https://somosvelora.com/
---
