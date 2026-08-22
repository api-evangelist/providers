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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Wallet Agentic Access
  operation_count: 10
  slug: google-wallet-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 5
apis:
- description: Manage event ticket classes and objects
  name: Google Wallet Event Tickets API
  slug: google-wallet-event-tickets-api
- description: Manage generic pass classes and objects
  name: Google Wallet Generic Passes API
  slug: google-wallet-generic-passes-api
- description: Manage wallet issuers
  name: Google Wallet Issuers API
  slug: google-wallet-issuers-api
- description: Create save-to-wallet JWTs
  name: Google Wallet JWT API
  slug: google-wallet-jwt-api
- description: Manage loyalty card classes and objects
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
  composite: 46.5
  delta: -4.4
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 60.8
    developer_ergonomics: 47.6
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 50.9
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
