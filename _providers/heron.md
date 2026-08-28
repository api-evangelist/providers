---
access_model:
  confidence: high
  label: Book a demo; credentials issued by Heron
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans/heron-plans-pricing.yml
  - authentication/heron-authentication.yml
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Heron's REST API for document intake, parsing, enrichment, cashflow underwriting, webhooks, and broker/funder submission flows.
  name: Heron API
  slug: heron-api
artifact_total: 9
asyncapis:
- description: 'Heron sends webhook notifications about the progress of asynchronous processes (end-user processing/review and PDF document parsing) to a URL you configure in the Heron dashboard (Settings tab). Each '
  name: Heron Webhooks
  slug: heron-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.herondata.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.herondata.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.herondata.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.herondata.io/api-reference/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.herondata.io/
- group: start
  title: ''
  type: Login
  url: https://dashboard.herondata.io/auth/signin
- group: company
  title: ''
  type: Blog
  url: https://www.herondata.io/blog
- group: operate
  title: ''
  type: Support
  url: mailto:hello@herondata.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.herondata.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.herondata.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.herondata.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/heron-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.herondata.io/security
- group: auth
  title: ''
  type: Security
  url: https://www.herondata.io/disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/heron-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heron-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/heron-data
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/heron-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/heron-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/heron-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/heron-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/heron-error-codes.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/heron-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/heron-rate-limits.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/heron-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/heron-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/heron-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/heron-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/heron-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/heron-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.herondata.io/miscellaneous/release-notes
- group: agent
  title: ''
  type: MCPServer
  url: mcp/heron-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/heron-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/heron-a2a.yml
- group: build
  title: ''
  type: Packages
  url: packages/heron-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/heron-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/heron-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/heron-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/heron-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/heron-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/heron-herondata-skill.md
created: '2026-07-17'
description: Heron (Heron Data) is a financial-services document-automation and cashflow-underwriting platform. Its API and AI platform handle document intake, classification, parsing and validation, enrichment, policy/rule evaluation, and CRM sync across 50+ document types (bank statements, tax returns, financial statements, ACORD forms). Lenders, MCA funders, brokers, and insurers upload documents for an "end user" (company), then read back parsed transactions, a Heron Score, scorecards, cashflow P&L, anomaly/fraud checks, and decline analytics. Heron publishes an OpenAPI 3.0 contract at app.herondata.io/swagger covering 226 paths and 272 operations, a conformant A2A agent card and a published Agent Skill on its documentation host, and a live unauthenticated MCP endpoint for documentation retrieval. The REST API authenticates with an x-api-key header, signals rate limits via x-ratelimit-* headers, and pushes async progress through webhooks. Backed by Insight Partners.
image: https://cdn.prod.website-files.com/675862616b5e61c9450cfef0/677e4fc1e48ddcd5917c71ca_home-og-img.jpg
layout: provider
mcp_servers:
- description: Heron ships a hosted, remote MCP server for its DOCUMENTATION, not for its REST API. The three published tools search, read and give feedback on docs.herondata.io — they do not create end users, uploa
  name: Heron MCP Server
  slug: heron-mcp-server
modified: '2026-08-14'
name: Heron
nav: Providers
network: true
overview: 'Heron publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Document Automation, Underwriting, and Lending.


  The Heron catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Heron''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 35 more developer resources.'
plans:
- name: Heron Plans Pricing
  plan_count: 0
  slug: heron-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Heron Rate Limits
  slug: heron-rate-limits
score:
  band: strong
  composite: 61.0
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 30.3
    contract_quality: 46.6
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 73.7
  previous_composite: 61.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heron/refs/heads/main/screenshots/heron-2026-07-25T221032.png
security:
- kind: authentication
  name: Heron Authentication
  slug: heron-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Heron Domain Security
  slug: heron-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Heron Vulnerability Disclosure
  slug: heron-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Heron Trust Center
  slug: heron-trust-center
  summary_line: SOC 2
slug: heron
tags:
- Company
- Financial-Services
- Document Automation
- Underwriting
- Lending
- Cash Flow Analytics
- Fintech
- Data Enrichment
- Bank Statements
- Transaction Enrichment
- Agent Ready
website: https://www.herondata.io/
---
