---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.6
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: The Glia platform REST API. Serves operators, sites, engagements, queues and reporting resources over api.glia.com (US) and api.glia.eu (EU). Authentication is a bearer token minted from an API key id
  name: Glia REST API
  slug: glia-rest-api
- description: Glia Functions is a serverless JavaScript runtime (workerd) inside the Glia platform, with REST endpoints for functions, versions, deployments, logs, applets, a KV store and cron-style scheduled trigg
  name: Glia Functions API
  slug: glia-functions-api
- description: The public browser SDK for embedding Glia engagements into a web property - queueing for engagement, chat, media upgrades, screen sharing, CoBrowsing, visitor authentication, surveys and message cente
  name: Glia Visitor JS SDK
  slug: glia-visitor-js-sdk
artifact_total: 8
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/salemove/glia-functions-tools/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/salemove/glia-functions-tools/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.glia.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.glia.com/glia-dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.glia.com/
- group: docs
  title: ''
  type: APIReference
  url: https://sdk-docs.glia.com/visitor-js-api/current/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/salemove
- group: company
  title: ''
  type: Blog
  url: https://www.glia.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.glia.com/services-support
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.glia.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.glia.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.glia.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.glia.com/security-compliance/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.glia.com/security-compliance/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.glia.com
- group: auth
  title: ''
  type: Security
  url: https://www.glia.com/security-bounty
- group: auth
  title: ''
  type: Compliance
  url: https://www.glia.com/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/glia-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/glia-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/glia-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/glia-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/glia-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/glia-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/glia-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/glia-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/glia-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/glia-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/glia-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/glia-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/glia-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glia-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/glia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/glia-trust-center.yml
- group: design
  title: ''
  type: Components
  url: components/glia-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/glia-data-model.yml
created: '2026-08-04'
description: Glia (formerly SaleMove) is a digital customer service and applied-AI platform built for banks, credit unions and insurers, unifying chat, voice, video, messaging and CoBrowsing under what the company calls ChannelLess architecture. Its AI layer is packaged as Glia Banker (customer-facing AI agent), Glia CoPilot (real-time agent assist) and Glia Analyst (manager/QA AI), alongside Glia Voice. The developer surface is a REST API at api.glia.com with regional US/EU hosts, a public Visitor JS SDK for embedding engagements in web properties, native iOS/Android/Ionic widget SDKs published to CocoaPods and Maven Central, and Glia Functions - a workerd-based serverless JavaScript runtime with a first-party CLI and MCP server. Developer documentation is served from a Fern-hosted portal that requires a Glia account login, so no public OpenAPI is published.
image: https://cdn.prod.website-files.com/680f1550811d9719bdbcf21b/680f7b6051475b02b05d75c6_logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Glia MCP Server
  slug: glia-mcp-server
modified: '2026-08-04'
name: Glia
nav: Providers
network: true
overview: 'Glia publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Service, Contact Center, Banking, and Credit Unions.


  Glia''s developer surface includes documentation, API reference, engineering blog, support, pricing, CLI, authentication, and 28 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 41.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 45.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/glia/refs/heads/main/screenshots/glia-2026-08-07T165740.png
security:
- kind: authentication
  name: Glia Authentication
  slug: glia-authentication
  summary_line: http/apiKey · 4 schemes
- kind: domain-security
  name: Glia Domain Security
  slug: glia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Glia Vulnerability Disclosure
  slug: glia-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Glia Trust Center
  slug: glia-trust-center
  summary_line: SOC 2 Type 2, PCI DSS, HIPAA/HITECH Type 1, CCPA
slug: glia
tags:
- Company
- Customer Service
- Contact Center
- Banking
- Credit Unions
- Financial-Services
- Conversational AI
- Voice
- Co-Browsing
- Serverless
website: https://www.glia.com
---
