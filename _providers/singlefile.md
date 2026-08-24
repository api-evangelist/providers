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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Singlefile Agentic Access
  operation_count: 50
  slug: singlefile-agentic-access
  summary_line: 50 operations · 25 acting
api_count: 7
apis:
- description: Formation and compliance documents
  name: SingleFile documents API
  slug: singlefile-documents-api
- description: Business entities — create, list, read, update, and their contacts, documents, jurisdictions, orders and tasks
  name: SingleFile entities API
  slug: singlefile-entities-api
- description: Entity jurisdictions and DBAs across US states
  name: SingleFile jurisdictions API
  slug: singlefile-jurisdictions-api
- description: Filing orders — create, place, update, and document-request driven order creation
  name: SingleFile orders API
  slug: singlefile-orders-api
- description: Organizations that own entities — CRUD plus contacts, documents, entities, orders and tasks
  name: SingleFile organizations API
  slug: singlefile-organizations-api
- description: JSON schemas for order payloads by entity_type, filing_type and jurisdiction
  name: SingleFile schemas API
  slug: singlefile-schemas-api
- description: Compliance tasks and deadlines
  name: SingleFile tasks API
  slug: singlefile-tasks-api
artifact_total: 23
asyncapis:
- description: Webhook event surface for SingleFile. Endpoints are configured in Profile Settings > Webhook Settings; deliveries are HTTPS-only and retried with exponential backoff on 5xx.
  name: SingleFile Webhooks
  slug: singlefile-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SingleFile External API Documentation documents API
  slug: open-singlefile-documents-api
- collection_type: open
  name: SingleFile External API Documentation documents entities API
  slug: open-singlefile-entities-api
- collection_type: open
  name: SingleFile External API Documentation documents jurisdictions API
  slug: open-singlefile-jurisdictions-api
- collection_type: open
  name: SingleFile External API Documentation documents orders API
  slug: open-singlefile-orders-api
- collection_type: open
  name: SingleFile External API Documentation documents organizations API
  slug: open-singlefile-organizations-api
- collection_type: open
  name: SingleFile External API Documentation documents schemas API
  slug: open-singlefile-schemas-api
- collection_type: open
  name: SingleFile External API Documentation documents tasks API
  slug: open-singlefile-tasks-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/singlefile-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/singlefile-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/singlefile-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/singlefile-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/singlefile-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.singlefile.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.singlefile.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.singlefile.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.singlefile.ai/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.singlefile.ai/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.singlefile.ai/blog/
- group: start
  title: ''
  type: SignUp
  url: https://www.singlefile.ai/get-started/
- group: start
  title: ''
  type: Login
  url: https://app.singlefile.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.singlefile.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.singlefile.ai/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.singlefile.ai/faqs/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/singlefile-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/singlefile-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/singlefile-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/singlefile-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.singlefile.ai/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/singlefile-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/singlefile-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/singlefile-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/singlefile-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/singlefile-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/singlefile-rate-limits.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/singlefile-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/singlefile-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: SingleFile is an AI-powered entity management and corporate compliance platform for corporations, law firms, and investment organizations. It automates business entity formation, EIN filing, annual report filing, registered agent services, UCC filings, and Corporate Transparency Act (BOI/FinCEN) reporting across all 52 US jurisdictions. The SingleFile External API (v1) exposes organizations, entities, contacts, jurisdictions, documents, orders, tasks, and filing schemas over a REST/JSON interface secured with OAuth 2.0 client credentials, with webhooks for real-time order, document, entity, jurisdiction, and task events. SingleFile is SOC 2 Type II certified.
image: https://www.singlefile.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: SingleFile MCP Server
  slug: singlefile-mcp-server
modified: '2026-07-21'
name: SingleFile
nav: Providers
network: true
overview: 'SingleFile publishes 7 APIs on the [APIs.io](https://apis.io/) network, including documents API, entities API, jurisdictions API, and 4 more. Tagged areas include Company, Compliance, Legal, Entity Management, and Corporate Compliance.


  The SingleFile catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SingleFile''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, support, and 23 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 3
  name: Singlefile Rate Limits
  slug: singlefile-rate-limits
scopes:
- name: Singlefile Scopes
  scope_count: 2
  slug: singlefile-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 49.5
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 30.3
    contract_quality: 52.9
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 39.5
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/singlefile/refs/heads/main/screenshots/singlefile-2026-08-17T081903.png
security:
- kind: authentication
  name: Singlefile Authentication
  slug: singlefile-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Singlefile Domain Security
  slug: singlefile-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Singlefile Trust Center
  slug: singlefile-trust-center
  summary_line: SOC 2 Type II
slug: singlefile
tags:
- Company
- Compliance
- Legal
- Entity Management
- Corporate Compliance
- Registered Agent
- Business Filings
- Regulatory
- Webhook
- Authentication
website: https://www.singlefile.ai
---
