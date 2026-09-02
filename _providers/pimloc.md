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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Pimloc Agentic Access
  operation_count: 22
  slug: pimloc-agentic-access
  summary_line: 22 operations · 11 acting
api_count: 1
apis:
- description: Account information
  name: Pimloc Account API
  slug: pimloc-account-api
- description: Token exchange and user session
  name: Pimloc Authentication API
  slug: pimloc-authentication-api
- description: Upload, redact, download and manage media
  name: Pimloc Media API
  slug: pimloc-media-api
- description: Enterprise project and user management
  name: Pimloc Projects API
  slug: pimloc-projects-api
- description: The Secure Redact API API from Pimloc — 0 operation(s) for secure redact api.
  name: Pimloc Secure Redact API
  slug: pimloc-secure-redact-api-api
artifact_total: 15
asyncapis:
- description: Secure Redact processes media asynchronously. When a state_callback and/or export_callback URL is supplied on upload, the platform POSTs event payloads to those URLs as media moves through the redacti
  name: Secure Redact Media Callbacks
  slug: pimloc-secureredact-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Secure Redact Account API
  slug: open-pimloc-account-api
- collection_type: open
  name: Secure Redact Account Authentication API
  slug: open-pimloc-authentication-api
- collection_type: open
  name: Secure Redact Account Media API
  slug: open-pimloc-media-api
- collection_type: open
  name: Secure Redact Account Projects API
  slug: open-pimloc-projects-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pimloc-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pimloc-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.secureredact.co.uk
- group: docs
  title: ''
  type: Documentation
  url: https://www.secureredact.ai/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://docs.secureredact.co.uk
- group: start
  title: ''
  type: GettingStarted
  url: https://www.secureredact.ai/apis
- group: company
  title: ''
  type: Website
  url: https://www.secureredact.ai
- group: operate
  title: ''
  type: Support
  url: https://www.secureredact.ai/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.secureredact.ai/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://www.secureredact.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.secureredact.co.uk/signup
- group: start
  title: ''
  type: Login
  url: https://app.secureredact.co.uk/app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.secureredact.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.secureredact.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pimloc
- group: auth
  title: ''
  type: Authentication
  url: authentication/pimloc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pimloc-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pimloc-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pimloc-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pimloc-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.secureredact.ai/
- group: build
  title: ''
  type: Packages
  url: packages/pimloc-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pimloc-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pimloc-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pimloc-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/pimloc-secureredact-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/pimloc-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pimloc-sandbox.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/pimloc-secureredact-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/pimloc-secureredact-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Pimloc is a UK-based AI company whose Secure Redact platform automates the redaction and anonymization of personally identifiable information (PII) in video, audio, images and documents — blurring faces, license plates, screens, on-screen text and full bodies with high accuracy. Used across law enforcement, local government, transport, insurance, healthcare, education and retail to meet GDPR, CCPA, HIPAA, FOIA and DSAR obligations, Secure Redact offers a browser SaaS and a v3 REST API. The API supports a fully automated Standard Flow (upload by URL, process, download) and an Enterprise Flow (review and edit in the UI, with projects, users and audit/chain-of-custody trails), plus audio transcription, video search and webhook callbacks. Pimloc is backed by Speedinvest.
image: https://www.secureredact.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Pimloc MCP Server
  slug: pimloc-mcp-server
modified: '2026-07-20'
name: Pimloc
nav: Providers
network: true
overview: 'Pimloc publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Authentication API, Media API, and 2 more. Tagged areas include Company, Privacy, Video Redaction, Anonymization, and PII.


  The Pimloc catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pimloc''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 49.6
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.1
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 58.3
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pimloc/refs/heads/main/screenshots/pimloc-2026-08-17T081234.png
security:
- kind: authentication
  name: Pimloc Authentication
  slug: pimloc-authentication
  summary_line: http-basic/http-bearer · 2 schemes
- kind: domain-security
  name: Pimloc Domain Security
  slug: pimloc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pimloc
tags:
- Company
- Privacy
- Video Redaction
- Anonymization
- PII
- Data Protection
- Artificial Intelligence
- Compliance
- Video Analytics
website: https://www.secureredact.ai
---
