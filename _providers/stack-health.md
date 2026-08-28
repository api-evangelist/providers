---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://stackhealthcare.com
- group: start
  title: ''
  type: SignUp
  url: https://app.stackhealthcare.com/quote
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stackhealthcare.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stackhealthcare.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.stackhealthcare.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.stackhealthcare.com/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/stack-health-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stack-health-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stack-health-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stack-health-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://app.stackhealthcare.com/.well-known/security.txt
created: '2026-07-17'
description: Stack Healthcare (stackhealthcare.com) is a health-insurance fintech offering affordable, flexible coverage for small businesses and their teams. Operating as a technology company rather than a bank, Stack acts as a HIPAA Business Associate to employer-sponsored health plans, processing Protected Health Information for enrollment and benefits administration, and partners with Stripe for payments and Celtic Bank for issuing commercial cards. The company was surfaced as a portfolio company of 8vc and added to the API Evangelist network. As of this enrichment pass Stack publishes no public API, developer portal, SDK, or documentation surface — the product is a waitlist-gated web application — so this profile captures the identity, security, and compliance posture that is publicly verifiable.
image: https://stackhealthcare.com/favicon.ico
layout: provider
modified: '2026-07-21'
name: Stack Health
nav: Providers
network: true
overview: 'Stack Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Insurance, Healthcare, Fintech, and Insurance.


  Stack Health''s developer surface includes signup flow and 10 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 18.4
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 18.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Stack Health Domain Security
  slug: stack-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stack Health Vulnerability Disclosure
  slug: stack-health-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Stack Health Trust Center
  slug: stack-health-trust-center
  summary_line: HIPAA
slug: stack-health
tags:
- Company
- Health Insurance
- Healthcare
- Fintech
- Insurance
- Employee Benefits
- Small Business
- HIPAA
website: https://stackhealthcare.com
---
