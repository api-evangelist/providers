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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Scanner Agentic Access
  operation_count: 25
  slug: scanner-agentic-access
  summary_line: 25 operations · 13 acting
api_count: 6
apis:
- description: Run asynchronous or blocking full-text queries over indexed logs.
  name: Scanner Ad Hoc Queries API
  slug: scanner-ad-hoc-queries-api
- description: Create, list, update, and delete streaming detection rules.
  name: Scanner Detection Rules API
  slug: scanner-detection-rules-api
- description: Manage alert destinations (Slack, Webhook, PagerDuty).
  name: Scanner Event Sinks API
  slug: scanner-event-sinks-api
- description: List and retrieve searchable indexes for a tenant.
  name: Scanner Indexes API
  slug: scanner-indexes-api
- description: Account and query-capacity metrics.
  name: Scanner Info API
  slug: scanner-info-api
- description: Upload, manage, and download lookup table files for enrichment.
  name: Scanner Lookup Tables API
  slug: scanner-lookup-tables-api
artifact_total: 12
asyncapis:
- description: ''
  name: Scanner Webhooks
  slug: scanner-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.scanner.dev/scanner/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scanner.dev/scanner/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.scanner.dev/scanner/using-scanner-complete-feature-reference/developer-tools/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.scanner.dev/scanner/getting-started/quick-setup-overview
- group: company
  title: ''
  type: Blog
  url: https://scanner.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://scanner.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.scanner.dev/
- group: start
  title: ''
  type: Login
  url: https://app.scanner.dev/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scanner.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scanner.dev/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://scanner.dev/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/scanner-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scanner-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/scanner-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: CLI
  url: cli/scanner-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/scanner-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/scanner-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/scanner-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/scanner-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/scanner-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/scanner-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://scanner.dev/trust
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/scanner-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/scanner-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scanner-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scanner-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/scanner-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scanner-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scanner.dev/
created: '2026-07-17'
description: Scanner is a cloud-native security data platform that indexes security logs directly in Amazon S3 to deliver full-text search across petabytes, continuous streaming threat detection, and programmatic and agent-native access to security data — an alternative to traditional SIEMs and data lakes. Its REST API (v1) covers searchable indexes, detection rules, event sinks, lookup tables, ad hoc queries, and query-capacity info, and it ships a hosted Model Context Protocol (MCP) server plus a detection-rules-as-code CLI (scanner-cli). Authentication is a Scanner API key presented as an HTTP Bearer token; console SSO is brokered by Stytch (Okta, Google Workspace, Microsoft Entra, SCIM). SOC 2 Type II certified and GDPR compliant. Backed by CRV.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scanner.png
layout: provider
mcp_servers:
- description: ''
  name: scanner-mcp.yml
  slug: scanner-mcpyml
modified: '2026-07-21'
name: Scanner
nav: Providers
network: true
overview: 'Scanner publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Ad Hoc Queries API, Detection Rules API, Event Sinks API, and 3 more. Tagged areas include Company, Security, SIEM, Log Analytics, and Threat Detection.


  The Scanner catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Scanner''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 23 more developer resources.'
random_paper: 26
score:
  band: developing
  composite: 54.8
  delta: -2.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 59.5
    developer_ergonomics: 64.7
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 23.7
  previous_composite: 57.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Scanner Authentication
  slug: scanner-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Scanner Domain Security
  slug: scanner-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Scanner Trust Center
  slug: scanner-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: scanner
tags:
- Company
- Security
- SIEM
- Log Analytics
- Threat Detection
- Security Operations
- Observability
- MCP
website: https://scanner.dev/
---
