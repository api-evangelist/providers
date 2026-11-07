---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Gonitro Agentic Access
  operation_count: 45
  slug: gonitro-agentic-access
  summary_line: 45 operations · 28 acting
api_count: 3
apis:
- baseURL: https://api.gonitro.dev
  baseurl_source: declared
  description: The Authentication API from GoNitro — 1 operation(s) for authentication.
  name: GoNitro Authentication API
  slug: gonitro-authentication-api
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
  description: The Webhooks API from GoNitro — 4 operation(s) for webhooks.
  name: GoNitro Webhooks API
  slug: gonitro-webhooks-api
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
  href: https://artifacts.apis.io/gonitro/capabilities/gonitro-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gonitro-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/gonitro/plans/gonitro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gonitro-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/gonitro/overlays/gonitro-pdf-services-overlay.yaml
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
  href: https://artifacts.apis.io/gonitro/changelog/gonitro-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gonitro-changelog.yml
- group: operate
  href: https://artifacts.apis.io/gonitro/lifecycle/gonitro-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/gonitro-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gonitro/lifecycle/gonitro-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gonitro-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gonitro/asyncapi/gonitro-sign-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/gonitro-sign-asyncapi.yml
- group: docs
  href: https://artifacts.apis.io/gonitro/asyncapi/gonitro-sign-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/gonitro-sign-asyncapi.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.gonitro.com/trust-center/compliance
- group: auth
  href: https://artifacts.apis.io/gonitro/security/gonitro-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gonitro-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/gonitro/security/gonitro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gonitro-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gonitro/authentication/gonitro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gonitro-authentication.yml
- group: design
  href: https://artifacts.apis.io/gonitro/conventions/gonitro-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gonitro-conventions.yml
- group: design
  href: https://artifacts.apis.io/gonitro/errors/gonitro-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gonitro-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gonitro/errors/gonitro-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/gonitro-error-codes.yml
- group: design
  href: https://artifacts.apis.io/gonitro/conformance/gonitro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gonitro-conformance.yml
- group: design
  href: https://artifacts.apis.io/gonitro/data-model/gonitro-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gonitro-data-model.yml
- group: agent
  href: https://artifacts.apis.io/gonitro/mcp/gonitro-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gonitro-mcp.yml
- group: agent
  href: https://artifacts.apis.io/gonitro/llms/gonitro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gonitro-llms.txt
- group: agent
  href: https://artifacts.apis.io/gonitro/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/gonitro/agentic-access/gonitro-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gonitro-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/gonitro/packages/gonitro-packages.yml
  title: ''
  type: Packages
  url: packages/gonitro-packages.yml
- group: agent
  href: https://artifacts.apis.io/gonitro/well-known/gonitro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gonitro-well-known.yml
- group: design
  href: https://artifacts.apis.io/gonitro/arazzo/gonitro-create-and-send-envelope.yml
  title: ''
  type: Arazzo
  url: arazzo/gonitro-create-and-send-envelope.yml
created: '2026-07-17'
description: 'Nitro Software (GoNitro) is a document productivity company providing PDF editing, electronic signatures, redaction, and intelligent document automation for enterprises, small businesses, and professionals. Nitro exposes two public REST APIs on api.gonitro.dev: the Nitro PDF Services API (convert, transform, extract, and generate PDFs — conversions, compression, merge/split, OCR, redaction, PII detection, table and form extraction, and archival PDF/A) and the Nitro Sign API (enterprise eSignature envelope, document, participant, and field workflows with sealed documents and audit trails). Both use machine-to-machine OAuth 2.0 client-credentials, short-lived JWT bearer tokens, RFC 9457 problem+json errors, and asynchronous job processing. Nitro is ISO 27001, SOC 2, and HIPAA compliant and an accredited eIDAS Qualified Trust Service Provider.'
finops:
- has_sources: true
  method: derived
  name: Gonitro Finops
  primary_unit: ''
  service_category: ''
  slug: gonitro-finops
  template: true
image: https://www.gonitro.com/hubfs/EN%20-%20Featured%20Images%20-%20Priority%20Pages%20-%20Home%20-%201200x628.png
layout: provider
mcp_servers:
- description: Local (stdio) MCP server; 6 tools listed.
  name: Nitro PDF Services MCP
  slug: nitro-pdf-services-mcp
modified: '2026-07-19'
name: GoNitro
nav: Providers
network: true
overview: 'GoNitro publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Platform API, Sign API, and 1 more. Tagged areas include Company, Documents, PDF, E-Signature, and Document Automation.


  The GoNitro catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  GoNitro''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Gonitro Plans Pricing
  plan_count: 6
  slug: gonitro-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: GoNitro API Rules
  rule_count: 51
  severity_counts:
    error: 35
    hint: 0
    info: 4
    warn: 12
  slug: gonitro-rules
score:
  band: strong
  composite: 65.5
  coverage:
    artifact_dirs: 31
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 58.8
    developer_ergonomics: 63.7
    discoverability: 78.6
    operational_transparency: 50.0
  previous_composite: 65.5
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
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: eidas
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gonitro/gonitro-2026-07-25T220034.png
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
skill_count: 2
skills:
- name: Create and send a Nitro Sign envelope
  slug: gonitro-create-and-send-envelope
- name: Optimize or transform a PDF with Nitro PDF Services
  slug: gonitro-optimize-pdf
slug: gonitro
tags:
- Company
- Documents
- PDF
- E-Signature
- Document Automation
- Document Conversion
- Data Extraction
- Redaction
- OCR
- Productivity
- Compliance
website: https://www.gonitro.com
---
