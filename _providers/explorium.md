---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 113
  human_in_the_loop: 0
  name: Explorium Agentic Access
  operation_count: 127
  slug: explorium-agentic-access
  summary_line: 127 operations · 113 acting
api_count: 1
apis:
- description: 'Native remote Model Context Protocol server exposing the AgentSource data as 11 agent tools - match-business, fetch-businesses, fetch-businesses- statistics, fetch-businesses-events, enrich-business, '
  name: Explorium AgentSource MCP Server
  slug: explorium-agentsource-mcp-server
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Match, fetch, stat, autocomplete, and event/enrollment operations over the Explorium business dataset (v1).
  name: Explorium Businesses API
  slug: explorium-businesses-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Inspect the shared credit pool that meters all Explorium API usage, including the credit menu and consumption aggregation (v1).
  name: Explorium Credits API
  slug: explorium-credits-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Match, fetch, stat, autocomplete, and event/enrollment operations over the Explorium prospect dataset (v1).
  name: Explorium Prospects API
  slug: explorium-prospects-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Register, retrieve, delete, and connectivity-test the webhook endpoints that receive Explorium business and prospect event notifications (v1).
  name: Explorium Webhooks API
  slug: explorium-webhooks-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Submit any v2 company or people enrichment — plus AI research — as an asynchronous job over an uploaded entity-ID dataset.
  name: Explorium Async Enrichment Jobs API
  slug: explorium-asyncenrichmentjobs-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: List, poll, and cancel the asynchronous enrichment jobs that back batch runs of up to 10,000 records (v2).
  name: Explorium Async Jobs API
  slug: explorium-asyncjobs-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Bulk (multi-record) versions of every v1 company enrichment, processing up to 50 business IDs per request.
  name: Explorium Bulk Business Enrichments API
  slug: explorium-bulkbusinessenrichments-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: 'Single-record company enrichments (v1): firmographics, technographics, webstack, website traffic and changes, financial indicators, funding and acquisition, workforce trends, company hierarchies, rati'
  name: Explorium Business Enrichments API
  slug: explorium-businessenrichments-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Run a customer-specific custom enrichment, single-record or in bulk, by custom enrichment ID.
  name: Explorium Custom Enrichments API
  slug: explorium-customenrichments-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Upload an entity-ID dataset that asynchronous v2 enrichment jobs run against.
  name: Explorium Entity ID Datasets API
  slug: explorium-entityiddatasets-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Liveness and payload-size health probes for the Explorium AgentSource service.
  name: Explorium Healthcheck API
  slug: explorium-healthcheck-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Bulk (multi-record) versions of the v1 people enrichments, processing up to 50 prospect IDs per request.
  name: Explorium Prospects Bulk Enrichments API
  slug: explorium-prospectsbulkenrichments-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: 'Single-record people enrichments (v1): contact information, professional profiles, and LinkedIn posts for a matched prospect.'
  name: Explorium Prospects Enrichments API
  slug: explorium-prospectsenrichments-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Resolve free-text input to the standardized filter values the v2 search API accepts.
  name: Explorium V2 Autocomplete API
  slug: explorium-v2autocomplete-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Synchronous v2 company enrichments — the same seventeen attribute families as v1, on the unified v2 request shape.
  name: Explorium V2 Business Enrichments API
  slug: explorium-v2businessenrichments-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Match, fetch, and stat over the company dataset on the v2 (beta) surface, where bulk and single input share one endpoint.
  name: Explorium V2 Businesses API
  slug: explorium-v2businesses-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Credit balance and consumption aggregation on the v2 (beta) surface.
  name: Explorium V2 Credits API
  slug: explorium-v2credits-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: 'Synchronous v2 people enrichments: contact information, professional profiles, and LinkedIn posts.'
  name: Explorium V2 Prospect Enrichments API
  slug: explorium-v2prospectenrichments-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Match, fetch, and stat over the people dataset on the v2 (beta) surface.
  name: Explorium V2 Prospects API
  slug: explorium-v2prospects-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Run a custom, AI-powered research task over a list of businesses or prospects using a natural-language query or prompt template, grounded in real-time web data (beta).
  name: Explorium V2 Research API
  slug: explorium-v2research-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Report the deployed version of the Explorium AgentSource service.
  name: Explorium Version API
  slug: explorium-version-api
artifact_total: 42
asyncapis:
- description: ''
  name: Explorium Webhooks
  slug: explorium-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Explorium AgentSource Business Enrichments API
  slug: open-explorium-business-enrichments-api
- collection_type: open
  name: Explorium AgentSource Business Enrichments Businesses API
  slug: open-explorium-businesses-api
- collection_type: open
  name: Explorium AgentSource Business Enrichments Credits API
  slug: open-explorium-credits-api
- collection_type: open
  name: Explorium AgentSource Business Enrichments Events API
  slug: open-explorium-events-api
- collection_type: open
  name: Explorium AgentSource Business Enrichments Prospect Enrichments API
  slug: open-explorium-prospect-enrichments-api
- collection_type: open
  name: Explorium AgentSource Business Enrichments Prospects API
  slug: open-explorium-prospects-api
- collection_type: open
  name: Explorium AgentSource Business Enrichments Webhooks API
  slug: open-explorium-webhooks-api
- collection_type: open
  name: Explorium AgentSource API
  slug: open-explorium
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/explorium-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/explorium-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/explorium-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/explorium-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/explorium-ai
- group: company
  title: ''
  type: Website
  url: https://www.explorium.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developers.explorium.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developers.explorium.ai/mcp-docs/agentsource-mcp
- group: commercial
  title: ''
  type: Plans
  url: plans/explorium-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/explorium-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/explorium-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.explorium.ai/blog/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/explorium-agentsource-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/explorium-agentsource-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/explorium-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/explorium-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/explorium-api-catalog.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/explorium-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/explorium-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/explorium-a2a.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/explorium-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/explorium-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.explorium.ai/data-security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/explorium-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/explorium-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/explorium-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/explorium-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/explorium-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/explorium-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/explorium-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/explorium-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/explorium-agentsource.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.explorium.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.explorium.ai/reference/quick-starts/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.explorium.ai/reference/quick-starts/quick-starts
- group: auth
  title: ''
  type: Authentication
  url: https://www.explorium.ai/auth.md
- group: operate
  title: ''
  type: Support
  url: https://developers.explorium.ai/reference/support-help-center
- group: commercial
  title: ''
  type: Pricing
  url: https://www.explorium.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.explorium.ai/sign-up/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.explorium.ai/explorium-website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.explorium.ai/privacy-policy/
- group: start
  title: ''
  type: Console
  url: https://www.explorium.ai/mcp-playground/
created: '2026-07-11'
description: Explorium is the B2B data layer for AI agents and go-to-market systems. Its AgentSource platform is one external-data and enrichment API plus a hosted MCP server, resolving, fetching, enriching and monitoring a company dataset and a people dataset aggregated from 100+ external sources. The REST API at https://api.explorium.ai publishes an anonymous OpenAPI 3.1 description covering 127 operations across two parallel surfaces - v1 (stable) and v2 (beta) - spanning entity matching, filtered fetch with cursor pagination, market-sizing statistics, autocomplete, seventeen company enrichment families and three people enrichment families (single, bulk to 50, and asynchronous to 10,000), AI-powered research, eighteen business and prospect event types delivered over HMAC-signed webhooks, and a shared prepaid credit pool that meters every call. Authentication is an api_key header on REST and OAuth 2.0 on MCP. Explorium is unusually agent-forward at the discovery layer, serving an RFC 9727
  api-catalog, a conformant A2A agent card, an MCP server card, an ARD capability catalog, an agent-skills index and llms.txt from its own domain.
finops:
- name: Explorium Finops
  service_category: Data and Analytics
  slug: explorium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/explorium.png
layout: provider
mcp_servers:
- description: ''
  name: Explorium MCP Server
  slug: explorium-mcp-server
- description: ''
  name: Explorium MCP Server
  slug: explorium-mcp-server-2
modified: '2026-08-14'
name: Explorium
nav: Providers
network: true
overview: 'Explorium publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Businesses API, Credits API, Prospects API, and 18 more. Tagged areas include Data Enrichment, B2B Data, Company Data, Prospect Enrichment, and Firmographics.


  The Explorium catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Explorium''s developer surface includes authentication, documentation, engineering blog, changelog, sandbox, API reference, getting-started guide, and 36 more developer resources.'
plans:
- name: Explorium Plans Pricing
  plan_count: 5
  slug: explorium-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 6
  name: Explorium Rate Limits
  slug: explorium-rate-limits
score:
  band: exemplar
  composite: 66.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 59.9
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 66.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/explorium/refs/heads/main/screenshots/explorium-2026-07-25T213931.png
security:
- kind: authentication
  name: Explorium Authentication
  slug: explorium-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Explorium Domain Security
  slug: explorium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Explorium Vulnerability Disclosure
  slug: explorium-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Explorium Trust Center
  slug: explorium-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CCPA
slug: explorium
tags:
- Data Enrichment
- B2B Data
- Company Data
- Prospect Enrichment
- Firmographics
- Technographics
- Web Intelligence
- Reference Data
- AI Agents
- MCP
- Agent Readiness
- Sales Intelligence
- Business Events
- Webhook
- Market Intelligence
website: https://www.explorium.ai
---
