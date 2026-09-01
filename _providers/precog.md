---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 35
  human_in_the_loop: 4
  name: Precog Agentic Access
  operation_count: 62
  slug: precog-agentic-access
  summary_line: 62 operations · 35 acting · 4 human-in-the-loop
api_count: 3
apis:
- description: The Admin API from Precog — 4 operation(s) for admin.
  name: Precog Admin API
  slug: precog-admin-api
- description: The Data Model API from Precog — 1 operation(s) for data model.
  name: Precog Data Model API
  slug: precog-data-model-api
- description: The Datasets API from Precog — 1 operation(s) for datasets.
  name: Precog Datasets API
  slug: precog-datasets-api
- description: The Destinations API from Precog — 2 operation(s) for destinations.
  name: Precog Destinations API
  slug: precog-destinations-api
- description: The Issues API from Precog — 4 operation(s) for issues.
  name: Precog Issues API
  slug: precog-issues-api
- description: The Kinds API from Precog — 3 operation(s) for kinds.
  name: Precog Kinds API
  slug: precog-kinds-api
- description: The Loads API from Precog — 1 operation(s) for loads.
  name: Precog Loads API
  slug: precog-loads-api
- description: The Log API from Precog — 1 operation(s) for log.
  name: Precog Log API
  slug: precog-log-api
- description: The Pipelines API from Precog — 18 operation(s) for pipelines.
  name: Precog Pipelines API
  slug: precog-pipelines-api
- description: The Semantic Model API from Precog — 3 operation(s) for semantic model.
  name: Precog Semantic Model API
  slug: precog-semantic-model-api
- description: The Sources API from Precog — 6 operation(s) for sources.
  name: Precog Sources API
  slug: precog-sources-api
- description: The Stripe API from Precog — 2 operation(s) for stripe.
  name: Precog Stripe API
  slug: precog-stripe-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: http-api Admin API
  slug: open-precog-admin-api
- collection_type: open
  name: http-api Admin Data Model API
  slug: open-precog-data-model-api
- collection_type: open
  name: http-api Admin Datasets API
  slug: open-precog-datasets-api
- collection_type: open
  name: http-api Admin Destinations API
  slug: open-precog-destinations-api
- collection_type: open
  name: http-api Admin Issues API
  slug: open-precog-issues-api
- collection_type: open
  name: http-api Admin Kinds API
  slug: open-precog-kinds-api
- collection_type: open
  name: http-api Admin Loads API
  slug: open-precog-loads-api
- collection_type: open
  name: http-api Admin Log API
  slug: open-precog-log-api
- collection_type: open
  name: http-api Admin Pipelines API
  slug: open-precog-pipelines-api
- collection_type: open
  name: http-api Admin Semantic Model API
  slug: open-precog-semantic-model-api
- collection_type: open
  name: http-api Admin Sources API
  slug: open-precog-sources-api
- collection_type: open
  name: http-api Admin Stripe API
  slug: open-precog-stripe-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/precog-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/precog-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/precog-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://precog.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://studio.precog.cloud/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://studio.precog.cloud/docs/
- group: start
  title: ''
  type: SignUp
  url: https://studio.precog.cloud/login
- group: commercial
  title: ''
  type: Pricing
  url: https://precog.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://precog.com/blog
- group: operate
  title: ''
  type: Support
  url: https://precog.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://precog.com/end-user-license-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://precog.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/precog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/precog-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/precog-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/precog-security.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/precog-scopes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/precog-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://api.precog.cloud/.well-known/security.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/precog-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://precog.com/express-security
- group: design
  title: ''
  type: Conformance
  url: conformance/precog-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/precog-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/precog-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/precog-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/precog-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/precog-public-http-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/precog-admin-http-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/precog-metadata-http-api-overlay.yaml
created: '2026-07-17'
description: Precog is an enterprise AI platform that acts as a "context engine" — turning fragmented, context-stripped data from SaaS applications and databases into live semantic layers that business users can query in natural language through AI assistants like Claude and ChatGPT. Its Intelligent Ingest builds no-code ETL pipelines from any business application into a data warehouse, detecting data relationships automatically and injecting business logic, definitions and relationships during ingestion, while its AI Assistants layer adds source tracing and SQL visibility for trustworthy answers. Precog exposes a public HTTP REST API (sources, destinations, pipelines, datasets, semantic-model generation) and an OAuth-secured Model Context Protocol (MCP) server, and was surfaced through the Techstars portfolio into the API Evangelist network.
image: https://studio.precog.cloud/precog-logo-full.svg
json_schemas:
- name: Foundation Semantic Model
  property_count: 3
  slug: precog-foundation-semantic-model.schema
layout: provider
mcp_servers:
- description: Precog operates a hosted, OAuth 2.0-secured Model Context Protocol (MCP) server that exposes the Precog "context engine" (semantic layers over ingested business data) to AI assistants such as Claude a
  name: Precog MCP Server
  slug: precog-mcp-server
modified: '2026-07-20'
name: Precog
nav: Providers
network: true
overview: 'Precog publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Data Model API, Datasets API, and 9 more. Tagged areas include Company, Data Integration, ETL, Artificial Intelligence, and Semantic Layer.


  Precog''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, support, and 24 more developer resources.'
random_paper: 10
scopes:
- name: Precog Scopes
  scope_count: 3
  slug: precog-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 18
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 56.4
    developer_ergonomics: 39.9
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/precog/refs/heads/main/screenshots/precog-2026-08-17T081331.png
security:
- kind: authentication
  name: Precog Authentication
  slug: precog-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Precog Domain Security
  slug: precog-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Precog Vulnerability Disclosure
  slug: precog-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Precog Trust Center
  slug: precog-trust-center
  summary_line: SOC 2 Type II
slug: precog
tags:
- Company
- Data Integration
- ETL
- Artificial Intelligence
- Semantic Layer
- MCP
- Data Pipeline
- Analytics
- Enterprise
website: https://precog.com/
---
