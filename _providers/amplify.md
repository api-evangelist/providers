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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 5.4
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Private partner-facing API behind api.getamplifylife.com, used for Amplify's embedded distribution motion ("Embed your products inside trusted partner ecosystems via API", per the Carrier Solutions pa
  name: Amplify Distribution API
  slug: distribution
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://getamplifylife.com
- group: company
  title: ''
  type: Blog
  url: https://getamplifylife.com/learn/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://getamplifylife.com/learn/faq
- group: start
  title: ''
  type: Login
  url: https://portal.getamplifylife.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://quotes.getamplifylife.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getamplifylife.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getamplifylife.com/privacy-policy
- group: design
  title: ''
  type: Components
  url: components/amplify-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amplify-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amplify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amplify-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amplify-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amplify-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amplify-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amplify-llms.txt
created: '2026-07-17'
description: 'Amplify (Amplify Life Insurance) is an insurtech founded in 2019 and launched in 2020, building what it calls the modern infrastructure for life insurance. It sells term, permanent, indexed universal life (IUL), annuity, final expense whole life and accidental death benefit products, with an emphasis on cash-value policies customers can borrow against while alive. Amplify distributes through four motions on one platform: a direct-to-consumer digital experience, an advisor and referral network, embedded distribution inside partner products, and white-label carrier partnerships with carriers and reinsurers including FGL, EMC and Munich Re. Its public developer surface is minimal: there is no developer portal, no published OpenAPI and no public SDKs. The company does operate a production API host (api.getamplifylife.com) fronted by AWS API Gateway that rejects unauthenticated calls, and it publishes embeddable IUL/VUL calculator widgets under /embed/ used for partner and advisor
  placements.'
image: https://getamplifylife.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: Amplify
nav: Providers
network: true
overview: 'Amplify publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Life Insurance, and Financial-Services.


  Amplify''s developer surface includes engineering blog, pricing, authentication, and 12 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 22.1
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 22.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amplify/refs/heads/main/screenshots/amplify-2026-07-25T200128.png
security:
- kind: authentication
  name: Amplify Authentication
  slug: amplify-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Amplify Domain Security
  slug: amplify-domain-security
  summary_line: TLSv1.2 · DMARC
slug: amplify
tags:
- Company
- Insurance
- Insurtech
- Life Insurance
- Financial-Services
- Fintech
- Embedded Finance
- Annuities
website: https://getamplifylife.com
---
