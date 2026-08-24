---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 4
  name: Digio Agentic Access
  operation_count: 10
  slug: digio-agentic-access
  summary_line: 10 operations · 6 acting · 4 human-in-the-loop
api_count: 6
apis:
- description: Fetch government-issued documents (Aadhaar, PAN, driving licence and others) directly from India's DigiLocker with citizen consent for KYC.
  name: Digio DigiLocker API
  slug: digio-digilocker-api
- description: DigiShield - Anti-Money-Laundering and Counter-Financing-of-Terrorism screening and ongoing monitoring against sanctions and watchlists.
  name: Digio AML/CFT API
  slug: digio-aml-cft-api
- description: DigiDocs - template-based document and agreement creation with eStamp.
  name: Digio Documents API
  slug: digio-documents-api
- description: DigiCollect - eNACH / NACH electronic mandates for recurring debit.
  name: Digio eMandate API
  slug: digio-emandate-api
- description: DigiSign - Aadhaar and OTP based legally-valid electronic signatures.
  name: Digio eSign API
  slug: digio-esign-api
- description: DigiKYC - identity verification via CKYC, KRA, DigiLocker, and offline Aadhaar.
  name: Digio KYC API
  slug: digio-kyc-api
artifact_total: 25
asyncapis:
- description: ''
  name: Digio Webhooks
  slug: digio-webhooks
collections:
- collection_type: postman
  name: Digio Documents API
  slug: postman-digio-documents-api
- collection_type: postman
  name: Digio Documents eMandate API
  slug: postman-digio-emandate-api
- collection_type: postman
  name: Digio Documents eSign API
  slug: postman-digio-esign-api
- collection_type: postman
  name: Digio Documents KYC API
  slug: postman-digio-kyc-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Digio Documents API
  slug: open-digio-documents-api
- collection_type: open
  name: Digio Documents eMandate API
  slug: open-digio-emandate-api
- collection_type: open
  name: Digio Documents eSign API
  slug: open-digio-esign-api
- collection_type: open
  name: Digio Documents KYC API
  slug: open-digio-kyc-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/digio/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/digio-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/digio-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/digio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/digio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/digio-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/digio-tech
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/company/digio.in
- group: company
  title: ''
  type: Website
  url: https://www.digio.in/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.digio.in/
- group: commercial
  title: ''
  type: Plans
  url: plans/digio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/digio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/digio-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.digio.in/blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.digio.in/
- group: operate
  title: ''
  type: Support
  url: https://www.digio.in/contact-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.digio.in/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.digio.in/get-started/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.digio.in/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digio.in/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: collections/digio.postman_collection.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/digio-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/digio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/digio-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/digio-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/digio-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/digio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/digio-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/digio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/digio-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/digio-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/digio-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/digio-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/digio-sandbox.yml
created: '2026-07-17'
description: Digio is an India-based digital trust and paperwork automation platform. Its REST APIs deliver legally-valid Aadhaar and OTP eSign, eStamping, KYC (CKYC, KRA, DigiLocker, offline Aadhaar, and Video KYC), eNACH/NACH eMandates and UPI Autopay recurring payments, AML/CFT screening, and template-based document and agreement management. All endpoints use HTTPS with HTTP Basic authentication.
finops:
- name: Digio Finops
  service_category: Identity and Digital Trust
  slug: digio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/digio.png
layout: provider
mcp_servers:
- description: ''
  name: Digio MCP Server
  slug: digio-mcp-server
modified: '2026-06-20'
name: Digio
nav: Providers
network: true
overview: 'Digio publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Documents API, eMandate API, eSign API, and 1 more. Tagged areas include eSign, KYC, eNACH, eMandate, and Digital Signature.


  The Digio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Digio''s developer surface includes authentication, documentation, engineering blog, support, pricing, signup flow, sandbox, and 28 more developer resources.'
plans:
- name: Digio Plans Pricing
  plan_count: 1
  slug: digio-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Digio Rate Limits
  slug: digio-rate-limits
score:
  band: strong
  composite: 54.3
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 16.7
    contract_quality: 66.3
    developer_ergonomics: 44.6
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 42.1
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/digio/refs/heads/main/screenshots/digio-2026-07-25T212007.png
security:
- kind: authentication
  name: Digio Authentication
  slug: digio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Digio Domain Security
  slug: digio-domain-security
  summary_line: no transport/DNS hardening detected
- kind: vulnerability-disclosure
  name: Digio Vulnerability Disclosure
  slug: digio-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Digio Trust Center
  slug: digio-trust-center
  summary_line: ISO 27001, SOC 2
slug: digio
tags:
- eSign
- KYC
- eNACH
- eMandate
- Digital Signature
- India
- Fintech
- Identity Verification
website: https://www.digio.in/
---
