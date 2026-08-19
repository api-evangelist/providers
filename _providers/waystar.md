---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.8
  scored_at: '2026-08-19'
api_count: 7
apis:
- description: Real-time and batch insurance eligibility and benefits verification, exchanging X12 270 inquiries and 271 responses to confirm coverage, plan details, copays, deductibles, and service-type benefits be
  name: Waystar Eligibility Verification API
  slug: waystar-eligibility-verification-api
- description: Automates prior authorization and referral determination and status, modeled on the X12 278 health care services review request/response. Covers submitting authorization requests, checking auth/referr
  name: Waystar Authorization & Referral API
  slug: waystar-prior-authorization-api
- description: Produces pre-service, good-faith patient cost estimates by combining eligibility/benefit data, contracted rates, and procedure codes to support price transparency and up-front patient collections. Mod
  name: Waystar Patient Estimation API
  slug: waystar-patient-estimation-api
- description: Submits, scrubs, edits, tracks, and manages professional, institutional, and dental claims through Waystar's clearinghouse, modeled on the X12 837P/837I/837D claim transaction set. Includes claim crea
  name: Waystar Claim Management API
  slug: waystar-claim-management-api
- description: Queries and monitors claim status across payers, modeled on the X12 276 status inquiry and 277 status response - returning received, accepted, pending, denied, and paid states. Supports both real-time
  name: Waystar Claim Status API
  slug: waystar-claim-status-api
- description: Retrieves electronic remittance advice (835/ERA), payments, and adjustments for automated payment posting and reconciliation, with raw X12 835 artifacts and parsed JSON. Modeled on the X12 835 transac
  name: Waystar Remittance & ERA API
  slug: waystar-remittance-era-api
- description: Identifies denied claims, exposes denial and remark codes and explanation-of-benefits detail, and supports appeal creation, packaging, and resubmission workflows. Modeled from Waystar's denial prevent
  name: Waystar Denial & Appeal Management API
  slug: waystar-denial-management-api
artifact_total: 13
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/waystar
- group: company
  title: ''
  type: Website
  url: https://www.waystar.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.waystar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.waystar.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.waystar.com/documents/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.waystar.com/documents/integration-basics/
- group: operate
  title: ''
  type: Support
  url: https://www.waystar.com/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WaystarInc
- group: start
  title: ''
  type: SignUp
  url: https://www.waystar.com/clients-partners/
- group: start
  title: ''
  type: Login
  url: https://www.waystar.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.waystar.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.waystar.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.waystar.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.waystar.com/feed/
- group: operate
  title: ''
  type: StatusPage
  url: http://status.esolutionsinc.com/
- group: auth
  title: ''
  type: Security
  url: https://www.waystar.com/responsible-disclosure/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/waystar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/waystar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/waystar-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/waystar-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/waystar-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/waystar-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/waystar-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/waystar-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/waystar-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/waystar-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/waystar-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/waystar-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/waystar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/waystar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/waystar-finops.yml
created: '2026-07-04'
description: Waystar is a healthcare payments and revenue cycle management (RCM) software company that operates a national clearinghouse connecting providers to payers. Its cloud platform spans financial clearance (eligibility, prior authorization, patient estimation), claim management, payment and remittance management, and denial prevention and recovery. Waystar exposes integration through REST APIs, web services, HL7, sFTP/batch, RPA, and X12 EDI transactions (270/271 eligibility, 276/277 claim status, 837 claims, 835 remittance/ERA, 278 authorization). API access is delivered through a partner/developer program at developer.waystar.com; the portal renders its full documentation navigation to anyone but serves a login form in place of every document body, and sandbox accounts are provisioned by email rather than self-service. Waystar publishes no OpenAPI, no llms.txt, no MCP server, no agent card and no client SDK in any package registry. Authentication is six hand-rolled schemes rather
  than one - HMAC-SHA1 body signatures on the classic Developer Suite, HMAC-SHA256 Authorization headers on Patient Estimation, credentials in the POST body on the eligibility gateway, HTTP Basic, WS-Security UsernameToken inside CAQH CORE SOAP envelopes, and X.509 client certificates - with no OAuth 2.0 and no OpenID Connect anywhere. The API surface below is documented from Waystar's public product pages, its developer-portal structure and the underlying X12 standards rather than from a published machine-readable definition.
finops:
- name: Waystar Finops
  service_category: Healthcare Revenue Cycle Management
  slug: waystar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/waystar.png
layout: provider
modified: '2026-08-15'
name: Waystar
nav: Providers
network: true
overview: 'Waystar publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Revenue Cycle Management, RCM, Clearinghouse, and Healthcare Payments.


  Waystar''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, engineering blog, authentication, and 24 more developer resources.'
plans:
- name: Waystar Plans Pricing
  plan_count: 2
  slug: waystar-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 7
  name: Waystar Rate Limits
  slug: waystar-rate-limits
score:
  band: developing
  composite: 46.9
  delta: 6.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 40.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 46.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
security:
- kind: authentication
  name: Waystar Authentication
  slug: waystar-authentication
  summary_line: hmac-signature/http-basic/credentials-in-payload/ws-security-usernametoken/mutualTLS/saml2-sso · 9 schemes
- kind: domain-security
  name: Waystar Domain Security
  slug: waystar-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Waystar Vulnerability Disclosure
  slug: waystar-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: waystar
tags:
- Healthcare
- Revenue Cycle Management
- RCM
- Clearinghouse
- Healthcare Payments
- Medical Billing
- X12 EDI
- Eligibility
- Claims
- Remittance
website: https://www.waystar.com/
---
