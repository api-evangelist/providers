---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.8
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: A remote Model Context Protocol endpoint served by the Flume Console at /api/v1/context/mcp. It is protected by OAuth 2.0 and advertises RFC 9728 protected-resource metadata, returning a 401 with a WW
  name: Flume Context MCP Server
  slug: flume-context-mcp-server
- description: The Account Contracts API from Flume Health — 2 operation(s) for account contracts.
  name: Flume Health Account Contracts API
  slug: flume-health-account-contracts-api
- description: The Accounts API from Flume Health — 4 operation(s) for accounts.
  name: Flume Health Accounts API
  slug: flume-health-accounts-api
- description: The AutomapJobs API from Flume Health — 3 operation(s) for automapjobs.
  name: Flume Health Automap Jobs API
  slug: flume-health-automapjobs-api
- description: The Connections API from Flume Health — 2 operation(s) for connections.
  name: Flume Health Connections API
  slug: flume-health-connections-api
- description: The Context Discovery API from Flume Health — 17 operation(s) for context discovery.
  name: Flume Health Context Discovery API
  slug: flume-health-context-discovery-api
- description: The Context Graph API from Flume Health — 3 operation(s) for context graph.
  name: Flume Health Context Graph API
  slug: flume-health-context-graph-api
- description: The Context Knowledge API from Flume Health — 25 operation(s) for context knowledge.
  name: Flume Health Context Knowledge API
  slug: flume-health-context-knowledge-api
- description: The Endpoint Maps API from Flume Health — 2 operation(s) for endpoint maps.
  name: Flume Health Endpoint Maps API
  slug: flume-health-endpoint-maps-api
- description: The Endpoints API from Flume Health — 23 operation(s) for endpoints.
  name: Flume Health Endpoints API
  slug: flume-health-endpoints-api
- description: The Flags API from Flume Health — 2 operation(s) for flags.
  name: Flume Health Flags API
  slug: flume-health-flags-api
- description: The Jobs v2 API from Flume Health — 3 operation(s) for jobs v2.
  name: Flume Health Jobs v2 API
  slug: flume-health-jobs-v2-api
- description: The Objects API from Flume Health — 5 operation(s) for objects.
  name: Flume Health Objects API
  slug: flume-health-objects-api
- description: The Reports API from Flume Health — 1 operation(s) for reports.
  name: Flume Health Reports API
  slug: flume-health-reports-api
- description: The Shards API from Flume Health — 2 operation(s) for shards.
  name: Flume Health Shards API
  slug: flume-health-shards-api
- description: The SourceFile API from Flume Health — 4 operation(s) for sourcefile.
  name: Flume Health Source File API
  slug: flume-health-sourcefile-api
- description: The Telemetry API from Flume Health — 1 operation(s) for telemetry.
  name: Flume Health Telemetry API
  slug: flume-health-telemetry-api
- description: The Transactions API from Flume Health — 2 operation(s) for transactions.
  name: Flume Health Transactions API
  slug: flume-health-transactions-api
- description: The Users API from Flume Health — 5 operation(s) for users.
  name: Flume Health Users API
  slug: flume-health-users-api
- description: The WorkerSizes API from Flume Health — 2 operation(s) for workersizes.
  name: Flume Health Worker Sizes API
  slug: flume-health-workersizes-api
artifact_total: 28
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/flume-health-capability-edges.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/flume-health-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.flumehealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.flumehealth.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flumehealth.com/
- group: docs
  title: ''
  type: APIReference
  url: https://console.flumehealth.com/api/docs
- group: operate
  title: ''
  type: Support
  url: https://support.flumehealth.com/portal/en/home
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flumehealth.com/
- group: start
  title: ''
  type: Login
  url: https://console.flumehealth.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flumehealth.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flumehealth.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flumehealth
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/flume-health-console-api-openapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flume-health-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/flume-health-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flume-health-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flume-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/flume-health-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flume-health-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flume-health-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flume-health-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flume-health-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flume-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/flume-health-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flume-health-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/flume-health-console-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flume-health-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/flume-health-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/flume-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flume-health-rate-limits.yml
created: '2026-08-16'
description: Flume Health is a New York based healthcare data platform for the payer ecosystem. Its Relay product is an integration platform (iPaaS) that maps eligibility, claims, and other health plan data between source and destination Endpoints — SFTP, cloud storage, databases, Snowflake, and APIs — through a canonical Flume Data Model, with Connections, Shards, Transactions, and mapping jobs managed from the Flume Console. A newer Context layer adds a knowledge graph over a customer's data estate, natural-language query, and domain agents for actuarial, claims, coding, and compliance work, exposed to AI clients through an OAuth-protected Model Context Protocol endpoint. The public Flume Console API is a 153-operation Swagger 2.0 contract served from console.flumehealth.com, authenticated with OpenID Connect / OAuth 2.0 at auth.flumehealth.com. Flume sold its third-party administrator operations to Vitori Health in 2023 to focus on the software platform.
image: https://flumehealth.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Flume Context MCP Server
  slug: flume-context-mcp-server
- description: ''
  name: Flume Health MCP Server
  slug: flume-health-mcp-server
modified: '2026-08-16'
name: Flume Health
nav: Providers
network: true
overview: 'Flume Health publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Account Contracts API, Accounts API, Automap Jobs API, and 16 more. Tagged areas include Healthcare, Health Plans, Payers, Healthcare Data, and Data Integration.


  Flume Health''s developer surface includes documentation, API reference, support, authentication, and 27 more developer resources.'
plans:
- name: Flume Health Plans Pricing
  plan_count: 0
  slug: flume-health-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Flume Health Rate Limits
  slug: flume-health-rate-limits
scopes:
- name: Flume Health Scopes
  scope_count: 14
  slug: flume-health-scopes
  summary_line: 14 scopes · implicit
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 52.0
    developer_ergonomics: 44.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 49.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 65.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flume-health/refs/heads/main/screenshots/flume-health-2026-08-17T080932.png
security:
- kind: authentication
  name: Flume Health Authentication
  slug: flume-health-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Flume Health Domain Security
  slug: flume-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Flume Health Trust Center
  slug: flume-health-trust-center
  summary_line: SOC 2 Type II, HITRUST CSF, HIPAA
slug: flume-health
tags:
- Healthcare
- Health Plans
- Payers
- Healthcare Data
- Data Integration
- iPaaS
- Eligibility
- Claims
- Knowledge Graph
- MCP
- agent-native
- Authentication
- Data Engineering
- Interoperability
website: https://www.flumehealth.com/
---
