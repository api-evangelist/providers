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
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.1
  scored_at: '2026-08-11'
api_count: 7
apis:
- description: The Great Britain market Account Information Service (AIS) API - retrieve account details, balances, and transactions for consenting Handelsbanken UK customers. Published to the Berlin Group NextGenPS
  name: Handelsbanken UK PSD2 Account Information API
  slug: handelsbanken-uk-account-information-api
- description: The Great Britain market Card Account Information (AIS) API - retrieve card account details, balances, and card transactions for consenting customers, to the Berlin Group NextGenPSD2 standard; consume
  name: Handelsbanken UK PSD2 Card Account Information API
  slug: handelsbanken-uk-card-account-information-api
- description: The Great Britain market Payment Initiation Service (PIS) API - initiate and manage payments from consenting Handelsbanken UK customer accounts, to the Berlin Group NextGenPSD2 standard; consumed unde
  name: Handelsbanken UK PSD2 Payment Initiation API
  slug: handelsbanken-uk-payment-initiation-api
- description: 'The Great Britain market Confirmation of Funds (CBPII / PIISP) API - check whether a specified amount is available on a consenting customer account, to the Berlin Group NextGenPSD2 standard; consumed '
  name: Handelsbanken UK PSD2 Confirmation of Funds API
  slug: handelsbanken-uk-confirmation-of-funds-api
- description: TPP enrolment API - register as a third-party provider and attach a PSD2 eIDAS (QWAC) or UK Open Banking (OBWAC) certificate to access live data on the production gateway. POST/PUT to /openbanking/psd
  name: Handelsbanken UK PSD2 Third-Parties API
  slug: handelsbanken-uk-third-parties-api
- description: First-party premium (beyond-PSD2) Accounts API documented on the Handelsbanken developer portal for commercial account data access outside the regulated Open Banking mandate.
  name: Handelsbanken UK Premium Accounts API
  slug: handelsbanken-uk-premium-accounts-api
- description: First-party premium (beyond-PSD2) Foreign Exchange API documented on the Handelsbanken developer portal for commercial FX rate and transaction services outside the regulated Open Banking mandate.
  name: Handelsbanken UK Premium FX API
  slug: handelsbanken-uk-premium-fx-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/handelsbanken-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.handelsbanken.co.uk/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.handelsbanken.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.handelsbanken.com/api/psd2
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.handelsbanken.com/api/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://developer.handelsbanken.com/api/user/register
- group: operate
  title: ''
  type: Support
  url: https://developer.handelsbanken.com/api/support
- group: other
  title: ''
  type: OpenBanking
  url: https://www.handelsbanken.com/en/open-banking
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/handelsbanken
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.handelsbanken.co.uk/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.handelsbanken.co.uk/en/privacy-notice
- group: company
  title: ''
  type: About
  url: https://www.handelsbanken.co.uk/en/about-us
- group: auth
  title: ''
  type: Compliance
  url: https://register.fca.org.uk/s/firm?id=0010X000049MNcuQAG
- group: auth
  title: ''
  type: Authentication
  url: authentication/handelsbanken-uk-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/handelsbanken-uk-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/handelsbanken-uk-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/handelsbanken-uk-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/handelsbanken-uk-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.handelsbanken.com/api/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/handelsbanken-uk-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/handelsbanken-uk-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/handelsbanken-uk-llms.txt
created: '2026-07-23'
description: Handelsbanken UK (Handelsbanken plc) is the UK relationship bank of Svenska Handelsbanken AB (publ), the Swedish banking group, and operates a decentralised network of over 200 local branches serving personal and business customers across Britain. Incorporated as a wholly-owned UK subsidiary and authorised by the Prudential Regulation Authority and regulated by the FCA and PRA (Financial Services Register number 806852, authorised since 2018), it is a full-service home-market bank rather than one of the CMA9-mandated institutions. Handelsbanken meets its UK Open Banking / PSD2 obligations through the group developer portal at developer.handelsbanken.com, where its Great Britain market APIs - Account Information (AIS), Card Account Information, Payment Initiation (PIS), and Confirmation of Funds - are published to the Berlin Group NextGenPSD2 standard rather than the OBIE Read/Write standard used by the CMA9. Third-party providers enrol against the production gateway at api.handelsbanken.com
  using a PSD2 eIDAS (QWAC/QSEALC) or UK Open Banking (OBWAC) certificate, with OAuth2 client authentication, mutual-TLS, and PSD2 strong customer authentication, and can test against a sandbox before going live.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Handelsbanken UK
nav: Providers
network: true
overview: 'Handelsbanken UK publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Open Banking, Financial Services, PSD2, and Berlin Group.


  Handelsbanken UK''s developer surface includes documentation, getting-started guide, signup flow, support, authentication, changelog, sandbox, and 15 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 32.2
  delta: -3.6
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 81.5
    governance: 12.5
    operational_transparency: 23.7
  previous_composite: 35.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 38.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/handelsbanken-uk/refs/heads/main/screenshots/handelsbanken-uk-2026-07-25T220612.png
security:
- kind: authentication
  name: Handelsbanken Uk Authentication
  slug: handelsbanken-uk-authentication
  summary_line: oauth2/mutualTLS · 4 schemes
- kind: domain-security
  name: Handelsbanken Uk Domain Security
  slug: handelsbanken-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: handelsbanken-uk
tags:
- Banking
- Open Banking
- Financial Services
- PSD2
- Berlin Group
- NextGenPSD2
- Payments
- Account Information
- United Kingdom
- Fintech
website: https://www.handelsbanken.co.uk/en/
---
