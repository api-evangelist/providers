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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 404
  human_in_the_loop: 8
  name: Alphaus Agentic Access
  operation_count: 586
  slug: alphaus-agentic-access
  summary_line: 586 operations · 404 acting · 8 human-in-the-loop
api_count: 15
apis:
- description: 'Admin API. Base URL: https://api.alphaus.cloud/m/blue'
  name: Alphaus Admin API
  slug: alphaus-admin-api
- description: '(BETA) Billing API. Base URL: https://api.alphaus.cloud/m/blue/billing'
  name: Alphaus Billing API
  slug: alphaus-billing-api
- description: 'Cost API. Base URL: https://api.alphaus.cloud/m/blue/cost'
  name: Alphaus Cost API
  slug: alphaus-cost-api
- description: '(BETA) Cover API. Base URL: https://api.alphaus.cloud/m/blue/cover'
  name: Alphaus Cover API
  slug: alphaus-cover-api
- description: '(ALPHA) Flag API. Base URL: https://api.alphaus.cloud/m/blue'
  name: Alphaus Flags API
  slug: alphaus-flags-api
- description: '(ALPHA) Flow API. Base URL: https://api.alphaus.cloud/m/blue/flow'
  name: Alphaus Flow API
  slug: alphaus-flow-api
- description: '(Alpha) GuaranteedCommitments API. Base URL: https://api.alphaus.cloud/m/blue/gc'
  name: Alphaus GuaranteedCommitments API
  slug: alphaus-guaranteedcommitments-api
- description: '(BETA) IAM API. Base URL: https://api.alphaus.cloud/m/blue'
  name: Alphaus Iam API
  slug: alphaus-iam-api
- description: '(ALPHA) Luster API. Base URL: https://api.alphaus.cloud/m/blue/luster'
  name: Alphaus Luster API
  slug: alphaus-luster-api
- description: '(BETA) Long operations API. Base URL: https://api.alphaus.cloud/m/blue'
  name: Alphaus Operations API
  slug: alphaus-operations-api
- description: '(BETA) Organization API. Base URL: https://api.alphaus.cloud/m/blue'
  name: Alphaus Organization API
  slug: alphaus-organization-api
- description: '(BETA) Preferences API. Base URL: https://api.alphaus.cloud/m/blue'
  name: Alphaus Preferences API
  slug: alphaus-preferences-api
- description: '(BETA) Pricing API. Base URL: https://api.alphaus.cloud/m/blue/pricing'
  name: Alphaus Pricing API
  slug: alphaus-pricing-api
- description: '(Alpha) Prism API. Base URL: https://api.alphaus.cloud/m/blue/prism'
  name: Alphaus Prism API
  slug: alphaus-prism-api
- description: '(Alpha) Vortex API. Base URL: https://api.alphaus.cloud/m/blue/vortex'
  name: Alphaus Vortex API
  slug: alphaus-vortex-api
artifact_total: 20
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/alphaus-blueapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alphaus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alphaus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alphaus.cloud
- group: start
  title: ''
  type: DeveloperPortal
  url: https://labs.alphaus.cloud/docs/blueapi/overview/
- group: docs
  title: ''
  type: Documentation
  url: https://labs.alphaus.cloud/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://labs.alphaus.cloud/blueapidocs/
- group: start
  title: ''
  type: GettingStarted
  url: https://labs.alphaus.cloud/docs/blueapi/overview/
- group: auth
  title: ''
  type: Authentication
  url: authentication/alphaus-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/alphaus-scopes.yml
- group: operate
  title: ''
  type: Support
  url: https://help.alphaus.cloud/en/
- group: company
  title: ''
  type: Blog
  url: https://labs.alphaus.cloud/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alphauslabs
- group: start
  title: ''
  type: Login
  url: https://login.alphaus.cloud/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alphaus.cloud/en/ripple-wave-terms-of-services
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alphaus.cloud/en/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.alphaus.cloud/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alphaus-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/alphaus-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/alphaus-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/alphaus-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alphaus-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alphaus-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alphaus-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/alphaus-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alphaus-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alphaus-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Alphaus is a Tokyo-based cloud FinOps company (No. 1 in Japan) whose platform helps enterprises, managed service providers, and cloud resellers manage and optimize multi-cloud spend across AWS, Azure, and GCP. Its products include Octo (cost visibility and optimization), Ripple and WavePro (reseller billing automation and invoicing), and Cover (cost anomaly detection and recommendation intelligence). Developers integrate through the Blue API — a unified protobuf/gRPC surface with a grpc-gateway JSON/REST proxy and generated OpenAPI — spanning 15 services and nearly 600 operations, complemented by the bluectl CLI and Go, Python, and TypeScript SDKs.
image: https://cdn.prod.website-files.com/657180a2db5e5db9774cd4a3/65ba1d60bf395fcd9cbb3bdb_home.png
layout: provider
mcp_servers:
- description: ''
  name: alphaus-mcp.yml
  slug: alphaus-mcpyml
modified: '2026-07-17'
name: Alphaus
nav: Providers
network: true
overview: 'Alphaus publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Billing API, Cost API, and 12 more. Tagged areas include Company, FinOps, Cloud Cost Management, Cloud, and Billing.


  Alphaus'' developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, CLI, and 21 more developer resources.'
random_paper: 30
scopes:
- name: Alphaus Scopes
  scope_count: 1
  slug: alphaus-scopes
  summary_line: 1 scope
score:
  band: developing
  composite: 43.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 42.7
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alphaus/refs/heads/main/screenshots/alphaus-2026-07-25T195758.png
security:
- kind: authentication
  name: Alphaus Authentication
  slug: alphaus-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Alphaus Domain Security
  slug: alphaus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alphaus
tags:
- Company
- FinOps
- Cloud Cost Management
- Cloud
- Billing
- Multi-Cloud
- Azure
- GCP
- gRPC
- Cost Optimization
- Reseller Billing
- API
website: https://alphaus.cloud
---
