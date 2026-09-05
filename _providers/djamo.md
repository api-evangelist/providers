---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://api-civ.djamo.com
  baseurl_source: declared
  description: REST API for businesses to collect payments, send single and mass transfers, check balance, manage sub-companies, and receive HMAC-signed webhooks.
  name: Djamo Business API
  slug: djamo-business-api
artifact_total: 4
asyncapis:
- description: Server-to-server webhook events emitted by the Djamo Business API for transaction lifecycle and charge status changes. Each delivery is signed with an HMAC-SHA256 signature (base64) in the `x-djamo-hm
  name: Djamo Business API Webhooks
  slug: djamo-webhooks-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/djamo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.djamo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.djamo.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.djamo.com/fr-ci/tarifs-business
- group: start
  title: ''
  type: SignUp
  url: https://go.djamo.com/app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.djamo.com/fr-ci/conditions-generales-et-tarifaires
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.djamo.com/fr-ci/politique-de-confidentialite
- group: company
  title: ''
  type: Blog
  url: https://www.djamo.com/fr-ci/apprendre
- group: operate
  title: ''
  type: Support
  url: https://docs.djamo.com/contact.html
created: '2026-07-17'
description: Djamo is a mobile-first fintech serving Côte d'Ivoire and Sénégal, giving 1.5M+ users current and savings accounts with an IBAN, virtual and physical Visa cards, money transfers to Mobile Money and bank accounts, bill payments, short-term credit, and BRVM investment products. For businesses, Djamo exposes a REST Business API that lets companies collect payments ("Pay with Djamo"), send single and mass transfers to recipients by phone number, check their real-time balance, and manage marketplace sub-companies, secured with bearer tokens and HMAC-signed webhooks. Djamo is a Y Combinator alumnus backed by investors including Partech.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/djamo.png
layout: provider
modified: '2026-07-18'
name: Djamo
nav: Providers
network: true
overview: 'Djamo publishes 1 API on the [APIs.io](https://apis.io/) network: Business API. Tagged areas include Company, Financial-Services, Fintech, Payments, and Banking.


  The Djamo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Djamo''s developer surface includes pricing, signup flow, engineering blog, support, and 5 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 44.8
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 42.6
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/djamo/refs/heads/main/screenshots/djamo-2026-07-25T212138.png
security:
- kind: authentication
  name: Djamo Authentication
  slug: djamo-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Djamo Domain Security
  slug: djamo-domain-security
  summary_line: TLSv1.3
slug: djamo
tags:
- Company
- Financial-Services
- Fintech
- Payments
- Banking
- Money Transfer
- Africa
- Côte d'Ivoire
- Sénégal
website: https://www.djamo.com/
---
