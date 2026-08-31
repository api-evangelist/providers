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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unest.co
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unest-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unest-llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://unest.co/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unest.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unest.co/privacy
- group: company
  title: ''
  type: Blog
  url: https://unest.co/insights
- group: operate
  title: ''
  type: Support
  url: https://unest.co/faq
- group: start
  title: ''
  type: SignUp
  url: https://web.unest.co
created: '2026-07-17'
description: UNest is a Los Angeles-based fintech app that helps parents and families save and invest for their children's futures through UTMA/UGMA custodial investment accounts, with brand rewards contributions, gifting, financial literacy content, and term life insurance offered through Ladder. UNest Advisers, LLC is an SEC-registered investment adviser, with brokerage through UNest Securities, LLC (FINRA/SIPC) and clearing through Apex Clearing. The company is a consumer mobile-app business and publishes no public developer API, though its site ships a real llms.txt. Surfaced as a 500 Global portfolio company in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unest.png
layout: provider
modified: '2026-07-21'
name: UNest
nav: Providers
network: true
overview: 'UNest is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Investing, Custodial Accounts, and Savings.


  UNest''s developer surface includes pricing, engineering blog, support, signup flow, and 6 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Unest Domain Security
  slug: unest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unest
tags:
- Company
- Fintech
- Investing
- Custodial Accounts
- Savings
- Insurance
- Family Finance
website: https://unest.co
---
