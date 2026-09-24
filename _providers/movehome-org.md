---
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.9
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Movehome Org Agentic Access
  operation_count: 13
  slug: movehome-org-agentic-access
  summary_line: 13 operations · 4 acting
api_count: 4
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
  description: MoveHome's inbound syndication API for CRMs, agencies and partners pushing listings in, at https://movehome.org/api/raia/portal/v1 — an implementation of the RAIA Protocol Working Group's vendor-neutr
  name: RAIA Portal Feed API (MoveHome.org implementation)
  slug: raia-portal-feed-api
artifact_total: 17
asyncapis:
- description: ''
  name: Movehome Org Webhooks
  slug: movehome-org-webhooks
common:
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
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/a2a/movehome-org-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/movehome-org-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/mcp/movehome-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/movehome-org-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/mcp/movehome-org-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/movehome-org-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/well-known/movehome-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/movehome-org-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/llms/movehome-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/movehome-org-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/agentic-access/movehome-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/movehome-org-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/authentication/movehome-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/movehome-org-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/scopes/movehome-org-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/movehome-org-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/conventions/movehome-org-conventions.yml
  title: ''
  type: Conventions
  url: conventions/movehome-org-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/conventions/movehome-org-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/movehome-org-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/errors/movehome-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/movehome-org-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/rate-limits/movehome-org-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/movehome-org-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/plans/movehome-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/movehome-org-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/lifecycle/movehome-org-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/movehome-org-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/conformance/movehome-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/movehome-org-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/data-model/movehome-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/movehome-org-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/asyncapi/movehome-org-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/movehome-org-webhooks.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/packages/movehome-org-packages.yml
  title: ''
  type: Packages
  url: packages/movehome-org-packages.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/regulatory/movehome-org-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/movehome-org-regulatory-posture.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/movehome-org/refs/heads/main/security/movehome-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/movehome-org-domain-security.yml
created: '2026-09-19'
description: 'Move Home Organisation CIC (Companies House 17202438, incorporated 6 May 2026, Poole, England) is an asset-locked UK Community Interest Company that runs MoveHome.org, a free, not-for-profit property listing aggregator built as the open-source reference consumer of the RAIA Protocol — the Real Estate AI Agent standard whose charter names the same CIC as its governing body — with listings federated from estate agencies and the transaction side handled by the separate commercial company EstateAigents.com Ltd. Its machine surface is agent-native and anonymous: an A2A 0.3.0 agent card at /.well-known/agent-card.json (graded conformant) with search_properties, get_property and create_enquiry skills over JSON-RPC at https://movehome.org/api/a2a; a read-only MCP server at https://movehome.org/mcp and a second MCP server over its public registry of real-estate A2A agents; an unauthenticated registry REST API under /api/registry/v1; and, for CRMs pushing listings in, an OAuth2 client-credentials
  implementation of the RAIA Portal Feed API (OpenAPI 3.1.0, 13 operations, RFC 9457 problem details) at https://movehome.org/api/raia/portal/v1. The site publishes an llms.txt/skills.md for agents but no privacy policy, terms, status page, changelog, SDK or pricing page.'
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
layout: provider
mcp_servers:
- description: ''
  name: Move Home Organisation CIC MCP Server
  slug: move-home-organisation-cic-mcp-server
- description: ''
  name: MoveHome Property MCP endpoint (Streamable HTTP)
  slug: movehome-property-mcp-endpoint-streamable-http
- description: ''
  name: MoveHome A2A Registry MCP endpoint (Streamable HTTP)
  slug: movehome-a2a-registry-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: Move Home Organisation CIC
nav: Providers
network: true
overview: 'Move Home Organisation CIC publishes 1 API on the [APIs.io](https://apis.io/) network: RAIA Portal Feed API (MoveHome.org implementation). Tagged areas include Real Estate, Property, Lettings, Property Sales, and Agents.


  The Move Home Organisation CIC catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Move Home Organisation CIC''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 25 more developer resources.'
plans:
- name: Movehome Org Plans Pricing
  plan_count: 1
  slug: movehome-org-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 9
  name: Movehome Org Rate Limits
  slug: movehome-org-rate-limits
scopes:
- name: Movehome Org Scopes
  scope_count: 3
  slug: movehome-org-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 70.0
    catalog_earned_first_party: 20.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 64.8
    developer_ergonomics: 61.9
    discoverability: 81.5
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Movehome Org Authentication
  slug: movehome-org-authentication
  summary_line: none/oauth2 · 2 schemes
- kind: domain-security
  name: Movehome Org Domain Security
  slug: movehome-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
