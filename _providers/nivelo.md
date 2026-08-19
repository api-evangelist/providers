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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Nivelo's real-time ACH return-risk scoring API. A RESTful endpoint that accepts ACH transaction data as JSON and returns a risk score and a prediction of the likelihood of an ACH return, so originator
  name: Nivelo Scorer API
  slug: nivelo-scorer-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://nivelo.io/
- group: company
  title: ''
  type: About
  url: https://nivelo.io/about
- group: start
  title: ''
  type: SignUp
  url: https://nivelo.io/employer/sign-up-nivelo
- group: start
  title: ''
  type: Login
  url: https://nivelo.io/auth/sign-in
- group: operate
  title: ''
  type: Support
  url: https://nivelo.io/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nivelo.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nivelo.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nivelo.io/privacy
- group: company
  title: ''
  type: Careers
  url: https://nivelo.io/careers
- group: auth
  title: ''
  type: Authentication
  url: authentication/nivelo-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nivelo-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nivelo-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://nivelo.io/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nivelo-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nivelo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://nivelo.io/security
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nivelofi
- group: other
  title: ''
  type: X
  url: https://twitter.com/nivelo_payments
created: '2026-07-17'
description: Nivelo is a New York City fintech that operates a payments risk and money-movement platform for the payroll industry, serving payment service providers (PSPs) and professional employer organizations (PEOs). Nivelo provides real-time payment risk intelligence and automated money movement across ACH, Wires, RTP, and FedNow rails, with capabilities including NSF (non-sufficient funds) prevention, ACH returns management, KYB and fraud monitoring, and treasury management. Its products include Exposure Scan (payment-risk identification), the Scorer Engine (a real-time ACH return-risk scoring API that predicts the likelihood of an ACH transaction failing before origination), and Instant Payroll (instant debits with auto-routing across payment rails to reduce failed payroll disbursements). Nivelo was founded in 2020 by Eli Polanco and Philippe Legault and raised a $2.5M seed round led by FirstMark, Barclays, and Anthemis.
image: https://nivelo.io/
layout: provider
modified: '2026-07-20'
name: Nivelo
nav: Providers
network: true
overview: 'Nivelo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, ACH, Fintech, and Payroll.


  Nivelo''s developer surface includes signup flow, support, authentication, and 15 more developer resources.'
random_paper: 57
score:
  band: emerging
  composite: 26.0
  delta: -1.1
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 27.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nivelo/refs/heads/main/screenshots/nivelo-2026-08-07T185344.png
security:
- kind: authentication
  name: Nivelo Authentication
  slug: nivelo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nivelo Domain Security
  slug: nivelo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nivelo Vulnerability Disclosure
  slug: nivelo-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Nivelo Trust Center
  slug: nivelo-trust-center
  summary_line: SOC 2 Type 2, FCRA, CCPA, GDPR
slug: nivelo
tags:
- Company
- Payments
- ACH
- Fintech
- Payroll
- Risk
- Fraud Detection
- Money Movement
- Real-Time Payments
- Treasury
- FedNow
- RTP
website: https://nivelo.io/
---
