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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: Global View APIs for alerts, external alert ingestion, and on-prem storage dashboards. Function-based JSON POST bodies over a Solr-style query engine, served from the Virtana cloud platform.
  name: Virtana Global View API
  slug: virtana-global-view-api
- description: Versioned REST API (/api/sdk/p/2/...) with ~11 top-level endpoints (inventory, schema, and more). OpenAPI/Swagger is downloadable from the IO appliance (releases 7.1.0+). Per-endpoint rate limiting ap
  name: Virtana Infrastructure Observability Public API
  slug: virtana-infrastructure-observability-public-api
- description: Cloud Cost Management (CCM) APIs exposing the cost/usage slicing available in the Virtana Platform UI for integration into user dashboards, including filter-by options on API calls to retrieve alert a
  name: Virtana Cloud Cost Management API
  slug: virtana-cloud-cost-management-api
artifact_total: 8
asyncapis:
- description: ''
  name: Virtual Instruments Webhooks
  slug: virtual-instruments-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virtual-instruments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.virtana.com/
- group: start
  title: ''
  type: Portal
  url: https://docs.virtana.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.virtana.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.virtana.com/en/global-view/using-global-view-apis.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.virtana.com/en/infrastructure-observability/io-user-guide/public-api/getting-started-with-the-public-api.html
- group: operate
  title: ''
  type: Support
  url: https://www.virtana.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.virtana.com/blog/
- group: start
  title: ''
  type: Login
  url: https://app.cloud.virtana.com/ui/new-signin
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.virtana.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.virtana.com/legal-notices/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.virtana.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.virtana.com/en/what-s-new-in-virtana-.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/virtual-instruments-changelog.yml
- group: learn
  title: ''
  type: Training
  url: https://training.virtana.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/virtual-instruments-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/virtual-instruments-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/virtual-instruments-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/virtual-instruments-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/virtual-instruments-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/virtual-instruments-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/virtual-instruments-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/virtual-instruments-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/virtual-instruments-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.virtana.com/trust/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/virtual-instruments-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/virtual-instruments-sandbox.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/virtual-instruments
created: '2026-07-17'
description: Virtana (formerly Virtual Instruments) is an AI-powered hybrid infrastructure observability company whose platform monitors and optimizes performance, cost, and risk across on-premises, colocation, and cloud environments. The platform spans Infrastructure Observability, Container Observability, Application and Service Observability, AI Factory (GPU/AI workload) Observability, Storage Load Testing, and Cloud Cost Management. Virtana exposes public developer surfaces — the Global View APIs (alerts, external alert ingestion, on-prem storage dashboards), the Infrastructure Observability Public REST API (/api/sdk/p/2), and a Cloud Cost Management API — all secured with OAuth2 client-credentials bearer tokens, plus an official Model Context Protocol (MCP) server that gives AI agents live access to metric, alert, inventory, relationship, and schema data over streaming HTTP.
image: https://www.virtana.com/wp-content/uploads/2023/09/virtana-logo.svg
layout: provider
mcp_servers:
- description: Virtana publishes an official Model Context Protocol (MCP) server surface for its observability platform. Two product endpoints are offered — Global View (GV) and Infrastructure Observability (IO) — e
  name: Virtana (Virtual Instruments) MCP Server
  slug: virtana-virtual-instruments-mcp-server
modified: '2026-07-21'
name: Virtana (Virtual Instruments)
nav: Providers
network: true
overview: 'Virtana (Virtual Instruments) publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Observability, Monitoring, and Storage.


  The Virtana (Virtual Instruments) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Virtana (Virtual Instruments)''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, changelog, and 21 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 64.3
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 47.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/virtual-instruments/refs/heads/main/screenshots/virtual-instruments-2026-08-17T082756.png
security:
- kind: authentication
  name: Virtual Instruments Authentication
  slug: virtual-instruments-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Virtual Instruments Domain Security
  slug: virtual-instruments-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Virtual Instruments Trust Center
  slug: virtual-instruments-trust-center
  summary_line: SOC 2 Type II, TX-RAMP Level 2, CSA STAR Registry
slug: virtual-instruments
tags:
- Company
- Infrastructure
- Observability
- Monitoring
- Storage
- Cloud Cost Management
- AIOps
- Performance
- Alerts
- MCP
website: https://www.virtana.com/
---
