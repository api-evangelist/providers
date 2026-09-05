---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pay-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wearepay.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.wearepay.uk/what-we-do/
- group: other
  title: ''
  type: Standards
  url: https://www.wearepay.uk/what-we-do/standards-authority/
- group: build
  title: ''
  type: StandardsLibrary
  url: https://www.standardssource.com/fps
- group: other
  title: ''
  type: StandardsSource
  url: https://www.standardssource.com/stn
- group: start
  title: ''
  type: GettingStarted
  url: https://www.wearepay.uk/what-we-do/payment-systems/access-to-payment-systems/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://newseventsinsights.wearepay.uk/
- group: operate
  title: ''
  type: Support
  url: https://www.wearepay.uk/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wearepay.uk/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wearepay.uk/privacy/
- group: design
  title: ''
  type: Conformance
  url: conformance/pay-uk-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pay-uk-llms.txt
- group: operate
  title: ''
  type: Contact
  url: https://www.wearepay.uk/what-we-do/overlay-services/confirmation-of-payee/
created: '2026-07-24'
description: 'Pay.UK Limited is the recognised operator and standards body for the United Kingdom''s interbank retail payment systems. It runs the domestic rails that move most of the money in the UK economy: Bacs (batch Direct Debit and Direct Credit), the Faster Payment System (24/7 real-time account-to-account payments), and the Image Clearing System for cheques, alongside the Current Account Switch Service. On top of the rails it owns industry overlay services including Confirmation of Payee (the API-based account name-checking service that fights Authorised Push Payment fraud) and Request to Pay, and through its Standards Authority it defines UK payments standards and the ISO 20022 migration underpinning the New Payments Architecture. Pay.UK is a scheme and standards operator, not a self-serve API platform: it publishes rulebooks, participation requirements, and ISO 20022 message specifications rather than an open public API, and its technical standards are distributed through the gated
  Standards Source and Faster Payment System Standards Library portals (single-login, registration required). Confirmation of Payee is a documented, API-based peer-to-peer scheme that participants and approved vendors implement against Pay.UK''s technical standards. Home market is the United Kingdom.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Pay.UK
nav: Providers
network: true
overview: 'Pay.UK is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, United Kingdom, Real-Time Payments, ISO 20022, and Account-to-Account.


  Pay.UK''s developer surface includes documentation, getting-started guide, engineering blog, support, and 10 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 19.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pay-uk/refs/heads/main/screenshots/pay-uk-2026-08-07T191623.png
security:
- kind: domain-security
  name: Pay Uk Domain Security
  slug: pay-uk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pay-uk
tags:
- Payments
- United Kingdom
- Real-Time Payments
- ISO 20022
- Account-to-Account
- Faster Payments
- Direct Debit
- Payment Scheme
- Standards Body
- Confirmation of Payee
website: https://www.wearepay.uk/
---
