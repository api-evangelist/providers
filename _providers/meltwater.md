---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Meltwater Agentic Access
  operation_count: 80
  slug: meltwater-agentic-access
  summary_line: 80 operations · 32 acting
api_count: 3
apis:
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Account Management API and Usage APIs
  name: Meltwater Account Management API
  slug: meltwater-account-management-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Upload your own content into the Meltwater Platform.
  name: Meltwater Bring Your Own Content (BYOC) API
  slug: meltwater-bring-your-own-content-byoc-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Fetch analytics on data within your private index.
  name: Meltwater Explore+ Analytics API
  slug: meltwater-explore-analytics-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Manage your Explore+ assets including searches and custom fields.
  name: Meltwater Explore+ Assets API
  slug: meltwater-explore-assets-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Export earned documents from your private index.
  name: Meltwater Explore+ Search API
  slug: meltwater-explore-search-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Analyse multiple types of Meltwater data, run volume time series, top tags and sentiment counts.
  name: Meltwater Listening Analytics API
  slug: meltwater-listening-analytics-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Data exports for onetime and recurring jobs.
  name: Meltwater Listening Exports API
  slug: meltwater-listening-exports-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Search Meltwater data using saved searches to integrate with your own API connectors and internal systems.
  name: Meltwater Listening Search API
  slug: meltwater-listening-search-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Manage Saved Searches
  name: Meltwater Listening Search Management API
  slug: meltwater-listening-search-management-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Streaming of Meltwater data to integrate with your internal systems and workflows.
  name: Meltwater Listening Streaming API
  slug: meltwater-listening-streaming-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: AI-powered chat completion and project listing features.
  name: Meltwater Mira API API
  slug: meltwater-mira-api-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Retrieve owned social metrics and analytics.
  name: Meltwater Owned Analytics API
  slug: meltwater-owned-analytics-api
- description: Meltwater MCP is a single remote Model Context Protocol server that exposes a customer's Meltwater assets (saved searches, tags and other configured objects) and Meltwater data (news and social mentio
  name: Meltwater MCP
  slug: meltwater-mcp
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Analyze data with metrics and KPIs for LLM prompts
  name: Meltwater Analyze API
  slug: meltwater-analyze-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Export content and manage export jobs
  name: Meltwater Export API
  slug: meltwater-export-api
- baseURL: https://api.meltwater.com
  baseurl_source: declared
  description: Endpoints to list LLM prompts and folders available for analytics
  name: Meltwater LLM API
  slug: meltwater-llm-api
artifact_total: 44
asyncapis:
- description: ''
  name: Meltwater Webhooks
  slug: meltwater-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Meltwater Account Management API
  slug: open-meltwater-account-management-api
- collection_type: open
  name: Meltwater Account Management Bring Your Own Content (BYOC) API
  slug: open-meltwater-bring-your-own-content-byoc-api
- collection_type: open
  name: Meltwater Account Management Explore+ Analytics API
  slug: open-meltwater-explore-analytics-api
- collection_type: open
  name: Meltwater Account Management Explore+ Assets API
  slug: open-meltwater-explore-assets-api
- collection_type: open
  name: Meltwater Account Management Explore+ Search API
  slug: open-meltwater-explore-search-api
- collection_type: open
  name: Meltwater Account Management Listening Analytics API
  slug: open-meltwater-listening-analytics-api
- collection_type: open
  name: Meltwater Account Management Listening Exports API
  slug: open-meltwater-listening-exports-api
- collection_type: open
  name: Meltwater Account Management Listening Search API
  slug: open-meltwater-listening-search-api
- collection_type: open
  name: Meltwater Account Management Listening Search Management API
  slug: open-meltwater-listening-search-management-api
- collection_type: open
  name: Meltwater Account Management Listening Streaming API
  slug: open-meltwater-listening-streaming-api
- collection_type: open
  name: Meltwater Account Management Mira API API
  slug: open-meltwater-mira-api-api
- collection_type: open
  name: Meltwater Account Management Owned Analytics API
  slug: open-meltwater-owned-analytics-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/meltwater-api-v4-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/meltwater-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/meltwater-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meltwater-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/meltwater-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.meltwater.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.meltwater.com/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/meltwater
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meltwater
- group: company
  title: ''
  type: Blog
  url: https://www.meltwater.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.meltwater.com/en/suite/data-api-integration
- group: operate
  title: ''
  type: StatusPage
  url: https://status.api.meltwater.com
- group: other
  title: ''
  type: X
  url: https://x.com/Meltwater
- group: commercial
  title: ''
  type: Plans
  url: plans/meltwater-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/meltwater-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/meltwater-finops.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/meltwater-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/meltwater-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.meltwater.com/.well-known/security.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/meltwater-trust-center.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/meltwater-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/meltwater-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meltwater-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/meltwater-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/meltwater-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/meltwater-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/meltwater-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/meltwater-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/meltwater-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/meltwater-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/meltwater-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/meltwater-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/meltwater-packages.yml
- group: build
  title: ''
  type: Examples
  url: examples/meltwater-api-examples.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/meltwater-vocabulary.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/meltwater-schemas.json
- group: design
  title: ''
  type: Rules
  url: rules/meltwater-jsonschema-spectral-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/meltwater-api.jsonld
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.meltwater.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.meltwater.com/api-reference/api-reference-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.meltwater.com/guides/getting-started/overview
- group: operate
  title: ''
  type: Support
  url: https://developer.meltwater.com/help/support
- group: operate
  title: ''
  type: FAQ
  url: https://developer.meltwater.com/help/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.meltwater.com/en/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.meltwater.com/en/privacy
- group: start
  title: ''
  type: Login
  url: https://app.meltwater.com/
- group: start
  title: ''
  type: Console
  url: https://developer.meltwater.com/tools/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meltwater
created: '2026-06-13'
description: Meltwater is a media intelligence platform providing REST APIs for media monitoring, social listening, journalist outreach, PR analytics, and brand reputation management. The API enables programmatic access to billions of editorial, blog, and social media conversations across news sources and social networks, with capabilities for searching, exporting, streaming, and analyzing mentions, as well as fetching owned social account analytics.
examples:
- key_count: 80
  name: Meltwater Api Examples
  slug: meltwater-api-examples
finops:
- name: Meltwater Finops
  service_category: ''
  slug: meltwater-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meltwater.png
json_schemas:
- name: Meltwater API Schemas
  property_count: 0
  slug: meltwater-schemas
jsonld:
- class_count: 52
  name: Meltwater Api Context
  property_count: 1
  slug: meltwater-api
layout: provider
mcp_servers:
- description: ''
  name: Meltwater MCP Server
  slug: meltwater-mcp-server
modified: '2026-08-13'
name: Meltwater
nav: Providers
network: true
overview: 'Meltwater publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Account Management API, Bring Your Own Content (BYOC) API, Explore+ Analytics API, and 12 more. Tagged areas include Media Monitoring, Social Listening, PR Analytics, Brand Intelligence, and News API.


  The Meltwater catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Meltwater''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, sandbox, code examples, and 42 more developer resources.'
plans:
- name: Meltwater Plans Pricing
  plan_count: 3
  slug: meltwater-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 7
  name: Meltwater Rate Limits
  slug: meltwater-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Meltwater API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: meltwater-jsonschema-spectral-rules
scopes:
- name: Meltwater Scopes
  scope_count: 5
  slug: meltwater-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: exemplar
  composite: 70.9
  coverage:
    artifact_dirs: 30
    catalog_gap: 31.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 29.5
    contract_quality: 71.8
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 29.5
    operational_transparency: 84.2
  previous_composite: 70.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/screenshots/meltwater-2026-06-20T185137.png
security:
- kind: authentication
  name: Meltwater Authentication
  slug: meltwater-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Meltwater Domain Security
  slug: meltwater-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Meltwater Vulnerability Disclosure
  slug: meltwater-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Meltwater Trust Center
  slug: meltwater-trust-center
  summary_line: trust center published
slug: meltwater
tags:
- Media Monitoring
- Social Listening
- PR Analytics
- Brand Intelligence
- News API
- Social Analytics
- Media Intelligence
website: https://www.meltwater.com
---
