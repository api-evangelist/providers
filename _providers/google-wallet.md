---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Wallet Agentic Access
  operation_count: 10
  slug: google-wallet-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
apis:
- baseURL: https://walletobjects.googleapis.com/walletobjects/v1
  baseurl_source: declared
  description: Manage event ticket classes and objects
  name: Google Wallet Event Tickets API
  slug: google-wallet-event-tickets-api
- baseURL: https://walletobjects.googleapis.com/walletobjects/v1
  baseurl_source: declared
  description: Manage generic pass classes and objects
  name: Google Wallet Generic Passes API
  slug: google-wallet-generic-passes-api
- baseURL: https://walletobjects.googleapis.com/walletobjects/v1
  baseurl_source: declared
  description: Manage wallet issuers
  name: Google Wallet Issuers API
  slug: google-wallet-issuers-api
- baseURL: https://walletobjects.googleapis.com/walletobjects/v1
  baseurl_source: declared
  description: Create save-to-wallet JWTs
  name: Google Wallet JWT API
  slug: google-wallet-jwt-api
- baseURL: https://walletobjects.googleapis.com/walletobjects/v1
  baseurl_source: declared
  description: Manage loyalty card classes and objects
  name: Google Wallet Loyalty Cards API
  slug: google-wallet-loyalty-cards-api
artifact_total: 26
collections:
- collection_type: postman
  name: Google Wallet Event Tickets API
  slug: postman-google-wallet-event-tickets-api
- collection_type: postman
  name: Google Wallet Event Tickets Generic Passes API
  slug: postman-google-wallet-generic-passes-api
- collection_type: postman
  name: Google Wallet Event Tickets Issuers API
  slug: postman-google-wallet-issuers-api
- collection_type: postman
  name: Google Wallet Event Tickets JWT API
  slug: postman-google-wallet-jwt-api
- collection_type: postman
  name: Google Wallet Event Tickets Loyalty Cards API
  slug: postman-google-wallet-loyalty-cards-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Wallet Event Tickets API
  slug: open-google-wallet-event-tickets-api
- collection_type: open
  name: Google Wallet Event Tickets Generic Passes API
  slug: open-google-wallet-generic-passes-api
- collection_type: open
  name: Google Wallet Event Tickets Issuers API
  slug: open-google-wallet-issuers-api
- collection_type: open
  name: Google Wallet Event Tickets JWT API
  slug: open-google-wallet-jwt-api
- collection_type: open
  name: Google Wallet Event Tickets Loyalty Cards API
  slug: open-google-wallet-loyalty-cards-api
- collection_type: open
  name: Google Wallet API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-wallet/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-wallet-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-wallet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-wallet-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google-wallet
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/wallet
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/wallet/generic/getting-started/onboarding-guide
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/wallet
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/wallet/generic/getting-started/onboarding-guide
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/wallet/support
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/google-wallet/refs/heads/main/json-ld/google-wallet.jsonld
created: '2026-03-13'
description: The Google Wallet API enables developers to create and manage digital passes including event tickets, boarding passes, loyalty cards, gift cards, offers, transit passes, and generic passes. It provides REST endpoints for creating pass classes (templates) and pass objects (instances), managing issuers, handling media uploads, and generating JWT tokens for save-to-wallet functionality on Android devices and the web.
finops:
- name: Google Wallet Finops
  service_category: API
  slug: google-wallet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-wallet.png
json_schemas:
- name: Google Wallet API Schema
  property_count: 0
  slug: google-wallet
jsonld:
- class_count: 0
  name: Google Wallet Context
  property_count: 11
  slug: google-wallet
layout: provider
modified: '2026-05-19'
name: Google Wallet
nav: Providers
network: true
overview: 'Google Wallet publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Event Tickets API, Generic Passes API, Issuers API, and 2 more. Tagged areas include Digital Wallet, Google Wallet, Loyalty Cards, Mobile Payments, and Passes.


  The Google Wallet catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Wallet''s developer surface includes developer portal, getting-started guide, documentation, authentication, support, and 9 more developer resources.'
plans:
- name: Google Wallet Plans Pricing
  plan_count: 3
  slug: google-wallet-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Google Wallet Rate Limits
  slug: google-wallet-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Wallet API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-wallet-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 63.3
    catalog_earned_first_party: 0.0
    catalog_gap: 51.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 59.2
    developer_ergonomics: 44.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-wallet/refs/heads/main/screenshots/google-wallet-2026-06-20T182248.png
security:
- kind: domain-security
  name: Google Wallet Domain Security
  slug: google-wallet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Wallet Vulnerability Disclosure
  slug: google-wallet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-wallet
tags:
- Digital Wallet
- Google Wallet
- Loyalty Cards
- Mobile Payments
- Passes
- Tickets
website: https://developers.google.com/wallet
---
