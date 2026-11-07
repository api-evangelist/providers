---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 28
  human_in_the_loop: 4
  name: Dpf It Com Agentic Access
  operation_count: 36
  slug: dpf-it-com-agentic-access
  summary_line: 36 operations · 28 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.dpf-it.com
  baseurl_source: declared
  description: Account management endpoints (password reset, etc.)
  name: DPF Account API
  slug: dpf-it-com-account-api
- baseURL: https://api.dpf-it.com
  baseurl_source: declared
  description: User authentication and registration endpoints
  name: DPF Authentication API
  slug: dpf-it-com-authentication-api
- baseURL: https://api.dpf-it.com
  baseurl_source: declared
  description: Workspace external connections (e.g. SFTP) with managed keypairs
  name: DPF Connections API
  slug: dpf-it-com-connections-api
- baseURL: https://api.dpf-it.com
  baseurl_source: declared
  description: 'Contact form endpoint with two modes: authenticated (user info auto-populated from account) and unauthenticated (email required in request body). No authentication required to submit.'
  name: DPF Contact API
  slug: dpf-it-com-contact-api
- baseURL: https://api.dpf-it.com
  baseurl_source: declared
  description: Data transformation pipeline management and orchestration
  name: DPF Data Specs API
  slug: dpf-it-com-data-specs-api
- baseURL: https://api.dpf-it.com
  baseurl_source: declared
  description: Apache Iceberg REST Catalog proxy with JWT authentication and workspace-scoped namespace access control. Provides standard Iceberg REST Catalog API access to your Iceberg tables.
  name: DPF Iceberg REST Catalog API
  slug: dpf-it-com-iceberg-rest-catalog-api
- baseURL: https://api.dpf-it.com
  baseurl_source: declared
  description: Scheduled ingestion triggers (e.g. SFTP polling) with AI-generated pre/post-processing code
  name: DPF Job Triggers API
  slug: dpf-it-com-job-triggers-api
- baseURL: https://api.dpf-it.com
  baseurl_source: declared
  description: Remote Streamable HTTP MCP (Model Context Protocol) server. A single JSON-RPC endpoint, authenticated with a Bearer token from either the OAuth 2.1 Authorization Server (recommended) or a plain `/auth
  name: DPF MCP API
  slug: dpf-it-com-mcp-api
- baseURL: https://api.dpf-it.com
  baseurl_source: declared
  description: PKCE-only OAuth 2.1 authorization server with Dynamic Client Registration (DCR) and refresh token rotation. Used by remote MCP clients (VS Code, Cursor, Claude, ChatGPT) to obtain a DPF access token v
  name: DPF OAuth 2.1 Authorization Server API
  slug: dpf-it-com-oauth-2-1-authorization-server-api
- baseURL: https://api.dpf-it.com
  baseurl_source: declared
  description: DuckDB-powered SQL query interface for executing analytical queries against Iceberg tables. Queries are scoped to a single authorized namespace per request.
  name: DPF Query API
  slug: dpf-it-com-query-api
- baseURL: https://api.dpf-it.com
  baseurl_source: declared
  description: Workspace management and collaboration endpoints
  name: DPF Workspaces API
  slug: dpf-it-com-workspaces-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/dpf-it-com/agentic-access/dpf-it-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dpf-it-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/dpf-it-com/plans/dpf-it-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dpf-it-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dpf-it-com/rules/dpf-it-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dpf-it-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dpf-it-com/json-ld/dpf-it-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dpf-it-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dpf-it-com/vocabulary/dpf-it-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dpf-it-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dpf-it-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dpf-it-com/data-model/dpf-it-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dpf-it-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/dpf-it-com/errors/dpf-it-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dpf-it-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dpf-it-com/conformance/dpf-it-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dpf-it-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dpf-it-com/llms/dpf-it-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dpf-it-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dpf-it-com/mcp/dpf-it-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dpf-it-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dpf-it-com/well-known/dpf-it-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dpf-it-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dpf-it-com/hosts/dpf-it-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dpf-it-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dpf-it-com/vendors/dpf-it-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dpf-it-com-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://dpf-it.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/dpf-it-com/authentication/dpf-it-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dpf-it-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dpf-it-com/security/dpf-it-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dpf-it-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dpf-it.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dpf-it.com/integration-guide.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dpf-it.com/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dpf-it.com/terms-of-service.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dpf-it.com/privacy-policy.html
created: '2026-11-05'
description: DPF is an AI‑powered data processing platform offering zero‑ETL transformation to Apache Iceberg. It enables users to ingest, transform, and load data in open formats via natural‑language prompts, provides a built‑in query engine, and supports bring‑your‑own‑compute integrations for collaborative data workflows.
image: https://www.dpf-it.com/logo.jpg
json_schemas:
- name: Check Spec Files Response
  property_count: 2
  slug: dpf-it-com-check-spec-files-response
- name: Create Spec
  property_count: 15
  slug: dpf-it-com-create-spec-request
- name: Get Status Response (queried by jobId)
  property_count: 2
  slug: dpf-it-com-get-status-by-job-id-response
- name: Get Status Response (queried by specId)
  property_count: 2
  slug: dpf-it-com-get-status-by-spec-id-response
- name: QueryResponse
  property_count: 2
  slug: dpf-it-com-query-response
- name: Update Spec
  property_count: 16
  slug: dpf-it-com-update-spec-request
jsonld:
- class_count: 100
  name: Dpf It Com Context
  property_count: 111
  slug: dpf-it-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.dpf-it.com.
  name: DPF MCP Server
  slug: dpf-it-com-mcp-yml
modified: '2026-11-05'
name: DPF
nav: Providers
network: true
overview: 'DPF publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Authentication API, Connections API, and 8 more. Tagged areas include Data, Artificial Intelligence, ETL, Apache Iceberg, and Platform.


  The DPF catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DPF''s developer surface includes API reference, authentication, documentation, pricing, and 18 more developer resources.'
plans:
- name: Dpf It Com Plans Pricing
  plan_count: 4
  slug: dpf-it-com-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: DPF API Rules
  rule_count: 64
  severity_counts:
    error: 54
    hint: 0
    info: 2
    warn: 8
  slug: dpf-it-com-rules
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 65.3
    developer_ergonomics: 30.4
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dpf It Com Authentication
  slug: dpf-it-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dpf It Com Domain Security
  slug: dpf-it-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: dpf-it-com-create-and-load-iceberg-table
  slug: dpf-it-com-create-and-load-iceberg-table
- name: dpf-it-com-execute-query
  slug: dpf-it-com-execute-query
- name: dpf-it-com-obtain-access-token
  slug: dpf-it-com-obtain-access-token
slug: dpf-it-com
tags:
- Data
- Artificial Intelligence
- ETL
- Apache Iceberg
- Platform
- Company
website: https://www.dpf-it.com/
---
