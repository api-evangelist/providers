---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: half
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Movehome Org Agentic Access
  operation_count: 13
  slug: movehome-org-agentic-access
  summary_line: 13 operations · 4 acting
api_count: 1
apis:
- description: 'Agent2Agent (A2A 0.3.0) surface: an agent card served from https://movehome.org/.well-known/agent-card.json (and the legacy /.well-known/agent.json, byte-identical) declaring three skills — search_pro'
  name: MoveHome.org A2A Property Agent
  slug: movehome-a2a-property-agent
- description: 'Remote Model Context Protocol server at https://movehome.org/mcp (alias /api/mcp): stateless Streamable HTTP, protocol version 2025-06-18, serverInfo movehome-property 1.0.0, anonymous. tools/list ans'
  name: MoveHome.org Property MCP Server
  slug: movehome-property-mcp-server
- description: Public registry of real-estate A2A agents operated by MoveHome, exposed two ways. REST under https://movehome.org/api/registry/v1 (no OpenAPI published; anonymous; JSON with RFC 9457 problem details o
  name: MoveHome.org A2A Agent Registry API
  slug: movehome-a2a-registry-api
- baseURL: https://movehome.org/api/raia/portal/v1
  baseurl_source: declared
  description: Per-branch reconciliation, performance reporting and enquiry retrieval.
  name: Move Home Organisation CIC Branches API
  slug: movehome-org-branches-api
- baseURL: https://movehome.org/api/raia/portal/v1
  baseurl_source: declared
  description: Upload, update, retrieve and remove residential or commercial listings.
  name: Move Home Organisation CIC Listings API
  slug: movehome-org-listings-api
- baseURL: https://movehome.org/api/raia/portal/v1
  baseurl_source: declared
  description: Health and metadata.
  name: Move Home Organisation CIC Operational API
  slug: movehome-org-operational-api
- baseURL: https://movehome.org/api/raia/portal/v1
  baseurl_source: declared
  description: Portal product activations such as Premium Listings and Featured Properties.
  name: Move Home Organisation CIC Products API
  slug: movehome-org-products-api
artifact_total: 24
asyncapis:
- description: ''
  name: Movehome Org Webhooks
  slug: movehome-org-webhooks
common:
- group: design
  href: https://artifacts.apis.io/movehome-org/rules/movehome-org-rules.yml
  title: ''
  type: Spectral
  url: rules/movehome-org-rules.yml
- group: design
  href: https://artifacts.apis.io/movehome-org/json-ld/movehome-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/movehome-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/movehome-org/vocabulary/movehome-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/movehome-org-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/movehome-org/hosts/movehome-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/movehome-org-hosts.yml
- group: build
  href: https://artifacts.apis.io/movehome-org/integrations/movehome-org-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/movehome-org-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/movehome-org/vendors/movehome-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/movehome-org-vendors.yml
- group: other
  href: https://artifacts.apis.io/movehome-org/overlays/movehome-org-raia-portal-feed-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/movehome-org-raia-portal-feed-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/movehome-org/skills/movehome-org-syndicate-listings.md
  title: ''
  type: AgentSkill
  url: skills/movehome-org-syndicate-listings.md
- group: company
  title: ''
  type: Website
  url: https://movehome.org/
- group: docs
  title: ''
  type: Documentation
  url: https://movehome.org/skills.md
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/MoveHome/MoveHome.Org/tree/main/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://movehome.org/skills.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MoveHome
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/MoveHome/MoveHome.Org
- group: operate
  title: ''
  type: Support
  url: https://github.com/MoveHome/MoveHome.Org/issues
- group: company
  title: ''
  type: About
  url: https://movehome.org/about
- group: commercial
  title: ''
  type: License
  url: https://github.com/MoveHome/MoveHome.Org/blob/main/LICENSE
- group: other
  href: https://artifacts.apis.io/movehome-org/a2a/movehome-org-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/movehome-org-a2a.yml
- group: agent
  href: https://artifacts.apis.io/movehome-org/mcp/movehome-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/movehome-org-mcp.yml
- group: build
  href: https://artifacts.apis.io/movehome-org/mcp/movehome-org-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/movehome-org-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/movehome-org/well-known/movehome-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/movehome-org-well-known.yml
- group: agent
  href: https://artifacts.apis.io/movehome-org/llms/movehome-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/movehome-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/movehome-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/movehome-org/agentic-access/movehome-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/movehome-org-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/movehome-org/authentication/movehome-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/movehome-org-authentication.yml
- group: auth
  href: https://artifacts.apis.io/movehome-org/scopes/movehome-org-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/movehome-org-scopes.yml
- group: design
  href: https://artifacts.apis.io/movehome-org/conventions/movehome-org-conventions.yml
  title: ''
  type: Conventions
  url: conventions/movehome-org-conventions.yml
- group: design
  href: https://artifacts.apis.io/movehome-org/conventions/movehome-org-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/movehome-org-conventions.yml
- group: design
  href: https://artifacts.apis.io/movehome-org/errors/movehome-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/movehome-org-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/movehome-org/rate-limits/movehome-org-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/movehome-org-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/movehome-org/plans/movehome-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/movehome-org-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/movehome-org/lifecycle/movehome-org-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/movehome-org-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/movehome-org/conformance/movehome-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/movehome-org-conformance.yml
- group: design
  href: https://artifacts.apis.io/movehome-org/data-model/movehome-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/movehome-org-data-model.yml
- group: design
  href: https://artifacts.apis.io/movehome-org/asyncapi/movehome-org-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/movehome-org-webhooks.yml
- group: other
  href: https://artifacts.apis.io/movehome-org/regulatory/movehome-org-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/movehome-org-regulatory-posture.yml
- group: auth
  href: https://artifacts.apis.io/movehome-org/security/movehome-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/movehome-org-domain-security.yml
created: '2026-09-19'
description: 'Move Home Organisation CIC (Companies House 17202438, incorporated 6 May 2026, Poole, England) is an asset-locked UK Community Interest Company that runs MoveHome.org, a free, not-for-profit property listing aggregator built as the open-source reference consumer of the RAIA Protocol — the Real Estate AI Agent standard whose charter names the same CIC as its governing body — with listings federated from estate agencies and the transaction side handled by the separate commercial company EstateAigents.com Ltd. Its machine surface is agent-native and anonymous: an A2A 0.3.0 agent card at /.well-known/agent-card.json (graded conformant) with search_properties, get_property and create_enquiry skills over JSON-RPC at https://movehome.org/api/a2a; a read-only MCP server at https://movehome.org/mcp and a second MCP server over its public registry of real-estate A2A agents; an unauthenticated registry REST API under /api/registry/v1; and, for CRMs pushing listings in, an OAuth2 client-credentials
  implementation of the RAIA Portal Feed API (OpenAPI 3.1.0, 13 operations, RFC 9457 problem details) at https://movehome.org/api/raia/portal/v1. The site publishes an llms.txt/skills.md for agents but no privacy policy, terms, status page, changelog, SDK or pricing page.'
finops:
- has_sources: true
  method: derived
  name: Movehome Org Finops
  primary_unit: ''
  service_category: ''
  slug: movehome-org-finops
  template: true
image: https://movehome.org/branding/icon.png
json_schemas:
- name: RAIA Agent Card
  property_count: 13
  slug: movehome-org-raia-agent-card
- name: RAIA Enquiry
  property_count: 7
  slug: movehome-org-raia-enquiry
- name: RAIA Property Listing
  property_count: 39
  slug: movehome-org-raia-listing
jsonld:
- class_count: 42
  name: Movehome Org Context
  property_count: 136
  slug: movehome-org-context
layout: provider
mcp_servers:
- description: MoveHome operates TWO remote MCP servers on its apex host, both stateless Streamable HTTP, both anonymous, both speaking MCP protocol version 2025-06-18 and both answering initialize and tools/list wi
  name: Move Home Organisation CIC MCP Server
  slug: movehome-org-mcp-yml
- description: ''
  name: MoveHome A2A Registry MCP endpoint (Streamable HTTP)
  slug: movehome-a2a-registry-mcp-endpoint-streamable-http
modified: '2026-10-20'
name: Move Home Organisation CIC
nav: Providers
network: true
overview: 'Move Home Organisation CIC publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Branches API, Listings API, Operational API, and 4 more. Tagged areas include Real Estate, Property, Lettings, Property Sales, and Agents.


  The Move Home Organisation CIC catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Move Home Organisation CIC''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 32 more developer resources.'
plans:
- name: Movehome Org Plans Pricing
  plan_count: 1
  slug: movehome-org-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 9
  name: Movehome Org Rate Limits
  slug: movehome-org-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Move Home Organisation CIC API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: movehome-org-rules
scopes:
- name: Movehome Org Scopes
  scope_count: 3
  slug: movehome-org-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 33
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 21.1
    contract_governance: 35.6
    contract_quality: 66.6
    developer_ergonomics: 45.2
    discoverability: 75.0
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 54.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/movehome-org/movehome-org-2026-10-11T111312.png
security:
- kind: authentication
  name: Movehome Org Authentication
  slug: movehome-org-authentication
  summary_line: none/oauth2 · 2 schemes
- kind: domain-security
  name: Movehome Org Domain Security
  slug: movehome-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: movehome-org-search-and-enquire
  slug: movehome-org-search-and-enquire
- name: movehome-org-syndicate-listings
  slug: movehome-org-syndicate-listings
slug: movehome-org
tags:
- Real Estate
- Property
- Lettings
- Property Sales
- Agents
- A2A
- MCP
- Agent-Native
- Agent Registry
- Non-Profit
- Open Source
- RAIA Protocol
- United Kingdom
website: https://movehome.org/
---
