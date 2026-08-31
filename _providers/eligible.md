---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://eligible.com/pricing
  - https://eligible.com/signup
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-08-30'
api_count: 5
apis:
- description: The Coverage API performs real-time insurance eligibility and benefits verification for a patient against a payer. Clients submit provider NPI, payer ID, and member identity information and receive st
  name: Eligible Coverage API
  slug: coverage
- description: The Claims API supports submission, tracking, and status checking of professional and institutional healthcare claims to payers across the Eligible network. The API also provides claim acknowledgement
  name: Eligible Claims API
  slug: claims
- description: The Payment Estimation API calculates expected patient out-of-pocket amounts for a service before it is rendered, combining benefit details from a coverage check with provider contracted rates and acc
  name: Eligible Payment Estimation API
  slug: payment-estimation
- description: 'The Enrollment API manages the trading partner enrollment workflow that providers must complete with payers in order to exchange eligibility, claims, and remittance transactions through Eligible. The '
  name: Eligible Enrollment API
  slug: enrollment
- description: The Payers API exposes the directory of insurance payers supported by Eligible, including payer identifiers, names, supported transaction types, enrollment requirements, and webhook capabilities. Clie
  name: Eligible Payers API
  slug: payers
artifact_total: 12
asyncapis:
- description: ''
  name: Eligible Webhooks
  slug: eligible-webhooks
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eligible-api
- group: company
  title: ''
  type: Website
  url: https://eligible.com/
- group: docs
  title: ''
  type: Documentation
  url: https://eligible.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://eligible.com/reference
- group: company
  title: ''
  type: Blog
  url: https://eligible.com/blog/feed/
- group: operate
  title: ''
  type: Support
  url: https://eligible.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eligible
- group: commercial
  title: ''
  type: Pricing
  url: https://eligible.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://eligible.com/signup
- group: start
  title: ''
  type: Login
  url: https://eligible.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eligible.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eligible.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.eligible.com
- group: auth
  title: ''
  type: Compliance
  url: https://eligible.com/compliance
- group: auth
  title: ''
  type: TrustCenter
  url: security/eligible-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eligible-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eligible-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eligible-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eligible-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eligible-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eligible-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/eligible-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/eligible-packages.yml
- group: design
  title: ''
  type: Components
  url: components/eligible-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eligible-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/eligible-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/eligible-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/eligible-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eligible-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/eligible-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eligible-llms.txt
created: '2024-07-02'
description: Eligible provides insurance billing APIs for healthcare businesses, enabling the integration of insurance billing experiences into healthcare applications. The platform supports eligibility verification, coverage discovery, claims submission and tracking, payment estimation, enrollment, and remittance processing across a large network of US payers.
finops:
- name: Eligible Finops
  service_category: API
  slug: eligible-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eligible.png
layout: provider
modified: '2026-08-15'
name: Eligible
nav: Providers
network: true
overview: 'Eligible publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Billing, Eligibility, Healthcare, Insurance, and Claims.


  The Eligible catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Eligible''s developer surface includes documentation, API reference, engineering blog, support, pricing, signup flow, authentication, and 24 more developer resources.'
plans:
- name: Eligible Plans Pricing
  plan_count: 2
  slug: eligible-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Eligible Rate Limits
  slug: eligible-rate-limits
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 54.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eligible/refs/heads/main/screenshots/eligible-2026-08-17T123412.png
security:
- kind: authentication
  name: Eligible Authentication
  slug: eligible-authentication
  summary_line: apiKey · 5 schemes
- kind: domain-security
  name: Eligible Domain Security
  slug: eligible-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Eligible Trust Center
  slug: eligible-trust-center
  summary_line: HITRUST r2, HITRUST CSF, NIST Cybersecurity Framework v1.1, SOC 2, CAQH CORE Phase I, CAQH CORE Phase II, CAQH CORE Phase III, CAQH CORE Phase IV, EHNAC HNAP, EHNAC CEAP, HIPAA
slug: eligible
tags:
- Billing
- Eligibility
- Healthcare
- Insurance
- Claims
website: https://eligible.com/
---
