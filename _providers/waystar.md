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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
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
artifact_total: 12
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/waystar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/waystar-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/waystar
- group: company
  title: ''
  type: Website
  url: https://www.waystar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.waystar.com/
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
- group: company
  title: ''
  type: Blog
  url: https://www.waystar.com/feed/
created: '2026-07-04'
description: Waystar is a healthcare payments and revenue cycle management (RCM) software company that operates a national clearinghouse connecting providers to payers. Its cloud platform spans financial clearance (eligibility, prior authorization, patient estimation), claim management, payment and remittance management, and denial prevention and recovery. Waystar exposes integration through REST APIs, web services, HL7, sFTP/batch, RPA, and X12 EDI transactions (270/271 eligibility, 276/277 claim status, 837 claims, 835 remittance/ERA, 278 authorization). API access is delivered through a partner/developer program at developer.waystar.com; detailed endpoint specifications, sandbox credentials, and authentication (HMAC-SHA256 / OAuth 2.0) are gated behind registration and a signed partnership, so the API surface below is modeled from Waystar's public product and developer-portal descriptions and the underlying X12 standards rather than from a published OpenAPI definition.
finops:
- name: Waystar Finops
  service_category: Healthcare Revenue Cycle Management
  slug: waystar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/waystar.png
layout: provider
modified: '2026-07-04'
name: Waystar
nav: Providers
network: true
overview: 'Waystar publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Revenue Cycle Management, RCM, Clearinghouse, and Healthcare Payments.


  Waystar''s developer surface includes documentation, signup flow, engineering blog, and 8 more developer resources.'
plans:
- name: Waystar Plans Pricing
  plan_count: 2
  slug: waystar-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 4
  name: Waystar Rate Limits
  slug: waystar-rate-limits
score:
  band: emerging
  composite: 20.7
  delta: -3.2
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 23.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Waystar Domain Security
  slug: waystar-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Waystar Vulnerability Disclosure
  slug: waystar-vulnerability-disclosure
  summary_line: disclosure policy published
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
