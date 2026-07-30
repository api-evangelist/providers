---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Part of Cuscal's CMS REST API family for card issuers. Enables instant digital card issuance and provisioning of cards into mobile and digital wallets (the 'Pays') for online and in-store transactions
  name: Cuscal Digital Card Issuance API
  slug: cuscal-digital-card-issuance-api
- description: CMS REST API letting cardholders and back-office staff control and restrict card usage - locking and unlocking cards and blocking certain transaction types to reduce fraud. Documented on the Cuscal De
  name: Cuscal Card Controls API
  slug: cuscal-card-controls-api
- description: CMS REST API providing self-service PIN set and change functionality that issuers can embed in mobile payment apps, removing reliance on PIN mailers. Documented on the Cuscal Developer Hub; full refer
  name: Cuscal PIN Services API
  slug: cuscal-pin-services-api
artifact_total: 5
asyncapis:
- description: ''
  name: Cuscal Webhooks
  slug: cuscal-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cuscal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cuscal.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.developerhub.cuscal.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cuscal.com/payments/
- group: start
  title: ''
  type: Portal
  url: https://www.cuscalpaymentshub.com.au/
- group: company
  title: ''
  type: Blog
  url: https://www.cuscal.com/newsroom/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cuscal.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cuscal.com.au/cuscal-developer-hub-terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.cuscal.com/payments/enablement-support/enablement-support-services/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cuscal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cuscal
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cuscal-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cuscal-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/cuscal-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cuscal-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cuscal-llms.txt
created: '2026-07-24'
description: 'Cuscal Limited is Australia''s largest independent provider of payments and regulated data services outside the Big Four banks, founded in 1966 and listed on the ASX (ticker CCL). An Authorised Deposit-taking Institution regulated by APRA and ASIC, Cuscal supplies the connectivity and processing layer beneath hundreds of banks, mutuals, credit unions, fintechs, non-bank lenders and corporates - carrying scheme card issuing and acquiring, the New Payments Platform (NPP) with PayID and PayTo, Direct Entry, BPAY, RTGS, ATM services, AI-driven fraud monitoring, and Consumer Data Right (open banking) data-holder and accredited-data-recipient services. Its acquisitions of Indue and the Paymark/Strategic Payments Services businesses broadened its issuer-processor and acquiring reach. Cuscal''s API posture is B2B and relationship-gated: it runs a public-facing Developer Hub (ReadMe-hosted) documenting CMS REST APIs for card issuing, card controls and PIN services with webhook notifications,
  but the full reference and any machine-readable OpenAPI definitions sit behind client onboarding rather than open self-serve signup.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Cuscal
nav: Providers
network: true
overview: 'Cuscal publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Australia, Card Issuing, Issuer Processor, and Real-Time Payments.


  The Cuscal catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cuscal''s developer surface includes documentation, developer portal, engineering blog, support, and 12 more developer resources.'
random_paper: 61
score:
  band: thin
  composite: 32.0
  delta: 4.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.6
    developer_ergonomics: 23.9
    discoverability: 83.3
    governance: 12.5
    operational_transparency: 13.2
  previous_composite: 27.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 24.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cuscal/refs/heads/main/screenshots/cuscal-2026-07-25T211000.png
security:
- kind: domain-security
  name: Cuscal Domain Security
  slug: cuscal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cuscal
tags:
- Payments
- Australia
- Card Issuing
- Issuer Processor
- Real-Time Payments
- Acquiring
- Open Banking
- Consumer Data Right
- Account-to-Account
- Fraud
- Banking-as-a-Service
website: https://www.cuscal.com/
---
