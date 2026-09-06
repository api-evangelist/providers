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
  band: agent-aware
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 14.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
asyncapis:
- description: ''
  name: Paynearme Callbacks Webhooks
  slug: paynearme-callbacks-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://home.paynearme.com/
- group: docs
  title: ''
  type: Documentation
  url: https://paynearme.zendesk.com/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://paynearme.zendesk.com/
- group: company
  title: ''
  type: Blog
  url: https://home.paynearme.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paynearme
- group: start
  title: ''
  type: Login
  url: https://paynearme.com/single_sign_on
- group: start
  title: ''
  type: SignUp
  url: https://home.paynearme.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paynearme.com/doc/bn_user/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paynearme.com/doc/bn_user/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://home.paynearme.com/data-security/
- group: design
  title: ''
  type: Conformance
  url: conformance/paynearme-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/paynearme-callbacks-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paynearme-domain-security.yml
created: '2026-07-17'
description: PayNearMe is a modern payments platform that helps businesses accept, disburse, and manage payments across cash, card, ACH, digital wallets and pay-by-bank while lowering the total cost of acceptance by increasing acceptance rates, driving self-service, and simplifying payment exceptions. It is best known for its cash-at-retail network of 62,000+ locations (7-Eleven, CVS, Walmart, Walgreens, Kroger, Casey's, Family Dollar, Dollar General and more) alongside a full electronic billing and payments stack. PayNearMe serves auto and consumer lending, credit unions, iGaming and sports betting, buy-here-pay-here dealers, tolling, mortgage servicing, and law firms, and integrates with merchant loan-management and dealer platforms through server-to-server callbacks (webhooks) and a partner API. This profile was added to the API Evangelist network from a VC portfolio lead and enriched from PayNearMe's public developer, security, and integration surface.
image: https://s31799.pcdn.co/wp-content/themes/paynearme-sage-theme-07.08.26/public/images/global/logo.46cdfe.svg
layout: provider
modified: '2026-07-20'
name: PayNearMe
nav: Providers
network: true
overview: 'PayNearMe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Billing, and ACH.


  The PayNearMe catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PayNearMe''s developer surface includes documentation, support, engineering blog, signup flow, and 9 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 33.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paynearme/refs/heads/main/screenshots/paynearme-2026-08-07T191652.png
security:
- kind: domain-security
  name: Paynearme Domain Security
  slug: paynearme-domain-security
  summary_line: TLSv1.3 · DMARC
slug: paynearme
tags:
- Company
- Fintech
- Payments
- Billing
- ACH
- Cash Payments
- Digital Wallet
- Lending
- iGaming
- Webhook
website: https://home.paynearme.com/
---
