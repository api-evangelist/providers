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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 75.0
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Gonitro Agentic Access
  operation_count: 45
  slug: gonitro-agentic-access
  summary_line: 45 operations · 28 acting
api_count: 8
apis:
- description: The Authentication API from GoNitro — 1 operation(s) for authentication.
  name: GoNitro Authentication API
  slug: gonitro-authentication-api
- description: The Conversions API from GoNitro — 1 operation(s) for conversions.
  name: GoNitro Conversions API
  slug: gonitro-conversions-api
- description: The Extractions API from GoNitro — 1 operation(s) for extractions.
  name: GoNitro Extractions API
  slug: gonitro-extractions-api
- description: The Generations API from GoNitro — 1 operation(s) for generations.
  name: GoNitro Generations API
  slug: gonitro-generations-api
- description: The Jobs API from GoNitro — 2 operation(s) for jobs.
  name: GoNitro Jobs API
  slug: gonitro-jobs-api
- description: The Platform API from GoNitro — 6 operation(s) for platform.
  name: GoNitro Platform API
  slug: gonitro-platform-api
- description: The Sign API from GoNitro — 22 operation(s) for sign.
  name: GoNitro Sign API
  slug: gonitro-sign-api
- description: The Transformations API from GoNitro — 1 operation(s) for transformations.
  name: GoNitro Transformations API
  slug: gonitro-transformations-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Authenticate, create an envelope, add a document, participant, and signature field, then send it for signing.
  name: Create and send a Nitro Sign envelope
  slug: gonitro-create-and-send-envelope
artifact_total: 16
asyncapis:
- description: Event surface for Nitro. Sign delivers envelope lifecycle webhooks (HTTP POST) signed with RFC 9421 HTTP Message Signatures (HMAC-SHA256; headers Content-Digest, Signature-Input, Signature). One webho
  name: Nitro Sign & PDF Services Webhooks
  slug: gonitro-sign-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.gonitro.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.gonitro.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gonitro.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.gonitro.com/docs/api-reference/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.gonitro.com/docs/getting-started/basic-setup
- group: operate
  title: ''
  type: Support
  url: https://www.gonitro.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.gonitro.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nitro
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gonitro.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://developers.gonitro.com/docs/authentication/credentials
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gonitro.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gonitro.com/legal/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://raw.githubusercontent.com/Nitro/nitro-platform-sample-code/main/postman/Nitro%20Automation%20Platform%20APIs.postman_collection.json
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gonitro.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gonitro-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/gonitro-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gonitro-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gonitro-sign-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/gonitro-sign-asyncapi.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.gonitro.com/trust-center/compliance
- group: auth
  title: ''
  type: TrustCenter
  url: security/gonitro-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gonitro-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gonitro-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gonitro-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gonitro-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/gonitro-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gonitro-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gonitro-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gonitro-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gonitro-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gonitro-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/gonitro-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gonitro-well-known.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gonitro-create-and-send-envelope.yml
created: '2026-07-17'
description: 'Nitro Software (GoNitro) is a document productivity company providing PDF editing, electronic signatures, redaction, and intelligent document automation for enterprises, small businesses, and professionals. Nitro exposes two public REST APIs on api.gonitro.dev: the Nitro PDF Services API (convert, transform, extract, and generate PDFs — conversions, compression, merge/split, OCR, redaction, PII detection, table and form extraction, and archival PDF/A) and the Nitro Sign API (enterprise eSignature envelope, document, participant, and field workflows with sealed documents and audit trails). Both use machine-to-machine OAuth 2.0 client-credentials, short-lived JWT bearer tokens, RFC 9457 problem+json errors, and asynchronous job processing. Nitro is ISO 27001, SOC 2, and HIPAA compliant and an accredited eIDAS Qualified Trust Service Provider.'
image: https://www.gonitro.com/hubfs/EN%20-%20Featured%20Images%20-%20Priority%20Pages%20-%20Home%20-%201200x628.png
layout: provider
mcp_servers:
- description: ''
  name: gonitro-mcp.yml
  slug: gonitro-mcpyml
modified: '2026-07-19'
name: GoNitro
nav: Providers
network: true
overview: 'GoNitro publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Conversions API, Extractions API, and 5 more. Tagged areas include Company, Documents, PDF, eSignature, and Electronic Signatures.


  The GoNitro catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GoNitro''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
random_paper: 5
score:
  band: strong
  composite: 60.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 66.8
    developer_ergonomics: 71.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 60.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Gonitro Authentication
  slug: gonitro-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Gonitro Domain Security
  slug: gonitro-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Gonitro Trust Center
  slug: gonitro-trust-center
  summary_line: ISO 27001, SOC 2, HIPAA, QTSP (Qualified Trust Service Provider, accredited by LSTI under eIDAS), EU-U.S. Data Privacy Framework (with UK and Swiss extensions)
slug: gonitro
tags:
- Company
- Documents
- PDF
- eSignature
- Electronic Signatures
- Document Automation
- Document Conversion
- Data Extraction
- Redaction
- OCR
- Productivity
- Compliance
website: https://www.gonitro.com
---
