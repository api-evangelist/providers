---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/higlobe-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/higlobe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/higlobe-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/higlobe-llms.txt
- group: company
  title: ''
  type: Website
  url: https://higlobe.com
- group: commercial
  title: ''
  type: Pricing
  url: https://higlobe.com/pricing
- group: auth
  title: ''
  type: Security
  url: https://higlobe.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://higlobe.com/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://higlobe.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://higlobe.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://higlobe.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.higlobe.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://higlobe.com/webapp/en/sign-up
- group: start
  title: ''
  type: Login
  url: https://higlobe.com/webapp/en/login
created: '2026-07-17'
description: Higlobe is a regulated cross-border money transfer service that lets freelancers, independent contractors, and businesses receive international payments from clients in the United States and the European Union. Members open a USD or EUR receiving account, share a payment request or account details with their payer, and withdraw funds to a local bank account with near-instant, 24/7 settlement at a flat, low cost. The platform also offers a Visa Signature card, a yield on account balances, and payer-facing payment requests. Higlobe is registered as a Money Service Business (MSB) with FinCEN under the U.S. Department of the Treasury and publishes a SOC 2 Type 2 / SOC 3 security posture. Higlobe is a consumer/business fintech product and does not currently publish a public developer API, OpenAPI, SDK, or developer portal; this profile captures its public identity, security, and commercial surface. Backed by Battery Ventures; added to the API Evangelist network for enrichment.
image: https://cdn.prod.website-files.com/63e626d88ff2d64582912f42/6477b61f90cb9f9fa91d9586_higlobe-global-transfers-share-image.png
layout: provider
modified: '2026-07-19'
name: Higlobe
nav: Providers
network: true
overview: 'Higlobe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Cross-Border Payments, Money Transfer, and Remittance.


  Higlobe''s developer surface includes pricing, engineering blog, support, signup flow, and 10 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 21.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/higlobe/refs/heads/main/screenshots/higlobe-2026-08-07T181807.png
security:
- kind: domain-security
  name: Higlobe Domain Security
  slug: higlobe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Higlobe Vulnerability Disclosure
  slug: higlobe-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Higlobe Trust Center
  slug: higlobe-trust-center
  summary_line: SOC 2, GDPR
slug: higlobe
tags:
- Company
- Payments
- Cross-Border Payments
- Money Transfer
- Remittance
- Fintech
- Financial-Services
- Freelancers
- Receiving Accounts
website: https://higlobe.com
---
