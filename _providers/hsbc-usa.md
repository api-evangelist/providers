---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: HSBC group corporate transaction-banking API for initiating outbound payments programmatically, documented on HSBC's Developer Portal and available to wholesale clients including HSBC USA corporate re
  name: Treasury - Payment Initiation
  slug: treasury-payment-initiation
- description: HSBC group corporate collections API consolidating multiple collection and receivables channels behind a single interface, documented on HSBC's Developer Portal for wholesale clients. API reference an
  name: Omni Collect - Single API
  slug: omni-collect
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.us.hsbc.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hsbc.com
- group: docs
  title: ''
  type: Documentation
  url: https://develop.hsbc.com/apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hsbc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hsbc
- group: company
  title: ''
  type: About
  url: https://www.about.us.hsbc.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.us.hsbc.com/privacy-notice/
- group: operate
  title: ''
  type: Support
  url: https://www.us.hsbc.com/customer-service/
- group: operate
  title: ''
  type: Contact
  url: https://develop.hsbc.com/contact-us
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hsbc-usa-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hsbc-usa-security.txt
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/engagements/hsbc-vdp-pro
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hsbc-usa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hsbc-usa-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hsbc-usa-llms.txt
created: '2026-07-23'
description: HSBC USA is the United States arm of HSBC Holdings plc, operating principally through HSBC Bank USA, N.A., a nationally chartered bank supervised by the Office of the Comptroller of the Currency (OCC). After exiting mass-market domestic retail banking in 2022 — selling its East Coast branches and national online deposit business to Citizens and its West Coast branches to Cathay Bank — HSBC refocused its US operations on global wholesale, commercial and corporate banking, global banking and markets, and wealth management for internationally connected clients. On the open-finance front, HSBC USA does not publish a US-specific first-party developer program; public API access is provided through HSBC's group-wide corporate and institutional Developer Portal (developer.hsbc.com), whose transaction-banking API products serve US wholesale clients but require registration and login to reach the actual API reference and specifications. There is no publicly downloadable OpenAPI, and consumer-permissioned
  data access for remaining US accounts is mediated through third-party aggregators rather than a documented first-party consumer data-sharing API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: HSBC USA
nav: Providers
network: true
overview: 'HSBC USA publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, United States, Corporate Banking, and Transaction Banking.


  HSBC USA''s developer surface includes documentation, support, and 13 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 16.9
  delta: -2.3
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 77.8
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 19.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 20.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hsbc-usa/refs/heads/main/screenshots/hsbc-usa-2026-07-25T221547.png
security:
- kind: domain-security
  name: Hsbc Usa Domain Security
  slug: hsbc-usa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hsbc Usa Vulnerability Disclosure
  slug: hsbc-usa-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: hsbc-usa
tags:
- Financial Services
- Banking
- United States
- Corporate Banking
- Transaction Banking
- Wealth Management
- Open Finance
- Payments
website: https://www.us.hsbc.com/
---
