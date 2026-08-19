---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Clari Agentic Access
  operation_count: 15
  slug: clari-agentic-access
  summary_line: 15 operations · 7 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: The Clari Copilot API provides access to conversation intelligence features including call recordings, transcripts, AI-generated summaries and action items, coaching scorecards, competitor sentiment s
  name: Clari Copilot API
  slug: clari-copilot-api
- description: 'Clari''s first-party remote Model Context Protocol server. It exposes live Clari + Salesloft revenue context — accounts, deals, people, calls and conversation intelligence, cadences and activity, team '
  name: Clari MCP Server
  slug: clari-mcp-server
- description: The Activity API API from Clari — 1 operation(s) for activity api.
  name: Clari Activity API API
  slug: clari-activity-api-api
- description: The Administrative API API from Clari — 1 operation(s) for administrative api.
  name: Clari Administrative API API
  slug: clari-administrative-api-api
- description: The Audit API API from Clari — 2 operation(s) for audit api.
  name: Clari Audit API API
  slug: clari-audit-api-api
- description: The Bulk Export Framework API from Clari — 3 operation(s) for bulk export framework.
  name: Clari Bulk Export Framework API
  slug: clari-bulk-export-framework-api
- description: The Bulk Ingest Job Status API API from Clari — 1 operation(s) for bulk ingest job status api.
  name: Clari Bulk Ingest Job Status API API
  slug: clari-bulk-ingest-job-status-api-api
- description: The Export API from Clari — 1 operation(s) for export.
  name: Clari Export API
  slug: clari-export-api
- description: The Forecast API API from Clari — 1 operation(s) for forecast api.
  name: Clari Forecast API API
  slug: clari-forecast-api-api
- description: The Ingestion API API from Clari — 3 operation(s) for ingestion api.
  name: Clari Ingestion API API
  slug: clari-ingestion-api-api
- description: The Opportunity API API from Clari — 1 operation(s) for opportunity api.
  name: Clari Opportunity API API
  slug: clari-opportunity-api-api
artifact_total: 41
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Clari API Reference Activity API API
  slug: open-clari-activity-api-api
- collection_type: open
  name: Clari API Reference Activity API Administrative API API
  slug: open-clari-administrative-api-api
- collection_type: open
  name: Clari API Reference Activity API Audit API API
  slug: open-clari-audit-api-api
- collection_type: open
  name: Clari API Reference Activity API Bulk Export Framework API
  slug: open-clari-bulk-export-framework-api
- collection_type: open
  name: Clari API Reference Activity API Bulk Ingest Job Status API API
  slug: open-clari-bulk-ingest-job-status-api-api
- collection_type: open
  name: rest-api
  slug: open-clari-copilot-api
- collection_type: open
  name: Clari API Reference Activity API Export API
  slug: open-clari-export-api
- collection_type: open
  name: Clari API Reference Activity API Forecast API API
  slug: open-clari-forecast-api-api
- collection_type: open
  name: Clari API Reference Activity API Ingestion API API
  slug: open-clari-ingestion-api-api
- collection_type: open
  name: Clari API Reference Activity API Opportunity API API
  slug: open-clari-opportunity-api-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clari-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/clari-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clari-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clari-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.clari.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.clari.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/clari
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clari
- group: company
  title: ''
  type: Blog
  url: https://www.clari.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clari.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://clari.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://x.com/clarihq
- group: commercial
  title: ''
  type: Plans
  url: plans/clari-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clari-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/clari-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/clari-vocabulary.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clari-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/clari-tool-crosswalk.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/clari-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clari-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clari-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clari-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clari-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/clari-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clari-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/clari-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clari-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/clari-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clari-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.clari.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.clari.com/documentation/external_spec
- group: start
  title: ''
  type: GettingStarted
  url: https://community.clari.com/product-q-a-6/how-to-use-copilot-apis-2258
- group: operate
  title: ''
  type: Support
  url: https://clari.my.site.com/customer/s/get-support
- group: operate
  title: ''
  type: Community
  url: https://community.clari.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clari.com/privacy/
- group: auth
  title: ''
  type: Security
  url: security/clari-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clari-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://www.clari.com/security/
- group: auth
  title: ''
  type: SecurityAddendum
  url: https://www.clari.com/security-addendum/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@clarihq
- group: company
  title: ''
  type: Careers
  url: https://www.clari.com/careers/
- group: company
  title: ''
  type: Press
  url: https://www.clari.com/press/
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/clari-context.jsonld
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
created: '2026-06-13'
description: Clari is an enterprise revenue orchestration platform that publishes three machine surfaces. The Clari Revenue API v5 (api.clari.com/v4) is an asynchronous, job-based export and ingest surface — queue a forecast, activity or audit export, poll until the job reads DONE, then download the results — plus a partner Ingestion API for pushing third-party data into Clari accounts and opportunities. The Clari Copilot REST API (rest-api.copilot.clari.com) is a synchronous conversation-intelligence and CRM surface covering calls, transcripts, AI summaries, action items, competitor sentiment, coaching scorecards, and CRUD over accounts, contacts and deals keyed on the customer's own CRM id. Clari also runs a first-party remote MCP server at mcp.clari.com/mcp, OAuth protected via Okta and listed natively in the Claude connector directory, which exposes live Clari + Salesloft revenue context to AI agents. Both HTTP APIs authenticate with header API keys, support no idempotency keys, and
  return no rate-limit headers.
examples:
- key_count: 3
  name: Clari Activity Export Example
  slug: clari-activity-export-example
- key_count: 3
  name: Clari Forecast Export Example
  slug: clari-forecast-export-example
- key_count: 3
  name: Clari Job Status Example
  slug: clari-job-status-example
finops:
- name: Clari Finops
  service_category: ''
  slug: clari-finops
graphqls:
- description: '> **NOT PUBLISHED BY CLARI — DO NOT WIRE THIS AS AN API.**'
  name: Clari GraphQL Schema
  slug: clari-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clari.png
json_schemas:
- name: ClariExportJob
  property_count: 7
  slug: clari-export-job
- name: ClariForecastExportRequest
  property_count: 6
  slug: clari-forecast-export-request
- name: ClariIngestionRequest
  property_count: 1
  slug: clari-ingestion-request
jsonld:
- class_count: 28
  name: Clari Context
  property_count: 6
  slug: clari-context
layout: provider
mcp_servers:
- description: ''
  name: clari-mcp.yml
  slug: clari-mcpyml
modified: '2026-08-13'
name: Clari
nav: Providers
network: true
overview: 'Clari publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Copilot API, Activity API API, Administrative API API, and 7 more. Tagged areas include Revenue Operations, Forecasting, Pipeline Management, Sales Intelligence, and Activity Intelligence.


  The Clari catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clari''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, API reference, getting-started guide, and 38 more developer resources.'
plans:
- name: Clari Plans Pricing
  plan_count: 0
  slug: clari-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 5
  name: Clari Rate Limits
  slug: clari-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Clari API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: clari-jsonschema-spectral-rules
scopes:
- name: Clari Scopes
  scope_count: 0
  slug: clari-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.1
  delta: -8.9
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 41.7
    contract_quality: 73.6
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 41.7
    operational_transparency: 78.9
  previous_composite: 71.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/clari/refs/heads/main/screenshots/clari-2026-06-20T174439.png
security:
- kind: authentication
  name: Clari Authentication
  slug: clari-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Clari Domain Security
  slug: clari-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Clari Vulnerability Disclosure
  slug: clari-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Clari Trust Center
  slug: clari-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27701, SOC 2 Type II, CSA, ADA, GDPR
slug: clari
tags:
- Revenue Operations
- Forecasting
- Pipeline Management
- Sales Intelligence
- Activity Intelligence
- Deal Insights
- CRM
- Conversation Intelligence
- B2B
- Enterprise
- MCP
- Agents
- Sales Engagement
- Bulk Export
- Data Ingestion
website: https://www.clari.com/
---
