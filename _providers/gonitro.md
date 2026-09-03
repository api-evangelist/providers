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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.2
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Gonitro Agentic Access
  operation_count: 45
  slug: gonitro-agentic-access
  summary_line: 45 operations · 28 acting
api_count: 2
apis:
- baseURL: https://api.gonitro.dev
  baseurl_source: declared
  description: The Authentication API from GoNitro — 1 operation(s) for authentication.
  name: GoNitro Authentication API
  slug: gonitro-authentication-api
- baseURL: https://api.gonitro.dev
  baseurl_source: declared
  description: The Conversions API from GoNitro — 1 operation(s) for conversions.
  name: GoNitro Conversions API
  slug: gonitro-conversions-api
- baseURL: https://api.gonitro.dev
  baseurl_source: declared
  description: The Extractions API from GoNitro — 1 operation(s) for extractions.
  name: GoNitro Extractions API
  slug: gonitro-extractions-api
- baseURL: https://api.gonitro.dev
  baseurl_source: declared
  description: The Generations API from GoNitro — 1 operation(s) for generations.
  name: GoNitro Generations API
  slug: gonitro-generations-api
- baseURL: https://api.gonitro.dev
  baseurl_source: declared
  description: The Jobs API from GoNitro — 2 operation(s) for jobs.
  name: GoNitro Jobs API
  slug: gonitro-jobs-api
- baseURL: https://api.gonitro.dev
  baseurl_source: declared
  description: The Platform API from GoNitro — 6 operation(s) for platform.
  name: GoNitro Platform API
  slug: gonitro-platform-api
- baseURL: https://api.gonitro.dev
  baseurl_source: declared
  description: The Sign API from GoNitro — 22 operation(s) for sign.
  name: GoNitro Sign API
  slug: gonitro-sign-api
- baseURL: https://api.gonitro.dev
  baseurl_source: declared
  description: The Transformations API from GoNitro — 1 operation(s) for transformations.
  name: GoNitro Transformations API
  slug: gonitro-transformations-api
arazzos:
- description: Authenticate, create an envelope, add a document, participant, and signature field, then send it for signing.
  name: Create and send a Nitro Sign envelope
  slug: gonitro-create-and-send-envelope
artifact_total: 32
asyncapis:
- description: Event surface for Nitro. Sign delivers envelope lifecycle webhooks (HTTP POST) signed with RFC 9421 HTTP Message Signatures (HMAC-SHA256; headers Content-Digest, Signature-Input, Signature). One webho
  name: Nitro Sign & PDF Services Webhooks
  slug: gonitro-sign-asyncapi
collections:
- collection_type: postman
  name: Nitro PDF Services Public Authentication API
  slug: postman-gonitro-authentication-api
- collection_type: postman
  name: Nitro PDF Services Public Authentication Conversions API
  slug: postman-gonitro-conversions-api
- collection_type: postman
  name: Nitro PDF Services Public Authentication Extractions API
  slug: postman-gonitro-extractions-api
- collection_type: postman
  name: Nitro PDF Services Public Authentication Generations API
  slug: postman-gonitro-generations-api
- collection_type: postman
  name: Nitro PDF Services Public Authentication Jobs API
  slug: postman-gonitro-jobs-api
- collection_type: postman
  name: Nitro PDF Services Public Authentication Platform API
  slug: postman-gonitro-platform-api
- collection_type: postman
  name: Nitro PDF Services Public Authentication Sign API
  slug: postman-gonitro-sign-api
- collection_type: postman
  name: Nitro PDF Services Public Authentication Transformations API
  slug: postman-gonitro-transformations-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nitro PDF Services Public Authentication API
  slug: open-gonitro-authentication-api
- collection_type: open
  name: Nitro PDF Services Public Authentication Conversions API
  slug: open-gonitro-conversions-api
- collection_type: open
  name: Nitro PDF Services Public Authentication Extractions API
  slug: open-gonitro-extractions-api
- collection_type: open
  name: Nitro PDF Services Public Authentication Generations API
  slug: open-gonitro-generations-api
- collection_type: open
  name: Nitro PDF Services Public Authentication Jobs API
  slug: open-gonitro-jobs-api
- collection_type: open
  name: Nitro PDF Services Public Authentication Platform API
  slug: open-gonitro-platform-api
- collection_type: open
  name: Nitro PDF Services Public Authentication Sign API
  slug: open-gonitro-sign-api
- collection_type: open
  name: Nitro PDF Services Public Authentication Transformations API
  slug: open-gonitro-transformations-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/gonitro-pdf-services-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/gonitro/overview
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
  name: Nitro PDF Services MCP
  slug: nitro-pdf-services-mcp
modified: '2026-07-19'
name: GoNitro
nav: Providers
network: true
overview: 'GoNitro publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Conversions API, Extractions API, and 5 more. Tagged areas include Company, Documents, PDF, E-Signature, and Electronic Signatures.


  The GoNitro catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GoNitro''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
random_paper: 14
score:
  band: strong
  composite: 57.6
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 65.9
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 57.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gonitro/refs/heads/main/screenshots/gonitro-2026-07-25T220034.png
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
- E-Signature
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
