---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Associated Bank surfaces core-banking integration through its core provider, Jack Henry, via the jXchange SOAP API platform. Documented services for this institution include Account History Search, Ac
  name: Associated Bank jXchange (Jack Henry) Integration
  slug: associated-bank-jxchange
artifact_total: 2
common:
- group: operate
  title: ''
  type: ChangeLog
  url: https://newsroom.associatedbank.com/releases
- group: auth
  title: ''
  type: DomainSecurity
  url: security/associated-banc-corp-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/associated-banc-corp-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.associatedbank.com/
- group: company
  title: ''
  type: Blog
  url: https://newsroom.associatedbank.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/associated-bank
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.associatedbank.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.associatedbank.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.associatedbank.com/contact
created: '2026-07-23'
description: Associated Bank, N.A. is the primary banking subsidiary of Associated Banc-Corp (NYSE ASB), a nationally chartered commercial bank and the largest bank holding company headquartered in Wisconsin, based in Green Bay. With roughly $50 billion in total assets following the April 2026 acquisition of American National Corporation, Associated operates a full-service Midwest banking franchise of more than 200 locations across Wisconsin, Illinois, Iowa, Minnesota, Missouri and Nebraska, offering consumer, business, commercial and wealth-management services. Associated does not publish a first-party public developer portal or downloadable OpenAPI/Swagger specifications. Its digital banking runs on a core-provider stack (Jack Henry), and consumer-permissioned data access is delivered through third-party aggregators (Plaid, Tink/TrueLayer) rather than a direct first-party API. Its commercial treasury customers use the login-gated Associated Connect platform. No FDX participation or CFPB
  Section 1033 data-access posture is publicly documented as of this review.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Associated Bank
nav: Providers
network: true
overview: 'Associated Bank publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, United States, Regional Bank, and Commercial Banking.


  Associated Bank''s developer surface includes changelog, engineering blog, support, and 6 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 14.8
  delta: 1.8
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 13.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/associated-banc-corp/refs/heads/main/screenshots/associated-banc-corp-2026-07-25T201444.png
security:
- kind: domain-security
  name: Associated Banc Corp Domain Security
  slug: associated-banc-corp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: associated-banc-corp
tags:
- Financial Services
- Banking
- United States
- Regional Bank
- Commercial Banking
- Data Aggregation
- Open Finance
website: https://www.associatedbank.com/
---
