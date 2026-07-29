---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ebix-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ebix-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ebix-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.ebix.com/
- group: company
  title: ''
  type: About
  url: https://www.ebix.com/who-we-are
- group: docs
  title: ''
  type: Documentation
  url: https://www.ebix.com/solutions/property-and-casualty-insurance
- group: docs
  title: ''
  type: Documentation
  url: https://www.ebix.com/solutions/property-and-casualty-insurance/translation-services
- group: docs
  title: ''
  type: Documentation
  url: https://www.ebix.com/solutions/property-and-casualty-insurance/team-up
- group: docs
  title: ''
  type: Documentation
  url: https://www.ebix.com/solutions/property-and-casualty-insurance/ebixevolution
- group: docs
  title: ''
  type: Documentation
  url: https://www.ebix.com/solutions/life-insurance
- group: docs
  title: ''
  type: Documentation
  url: https://www.ebix.com/solutions/health-insurance-and-employee-benefits
- group: docs
  title: ''
  type: Documentation
  url: https://www.ebix.com/solutions/health-content-and-wellness
- group: docs
  title: ''
  type: Documentation
  url: https://www.ebix.com/solutions/risk-compliance-and-management/risk-envision
- group: docs
  title: ''
  type: Documentation
  url: https://www.ebix.com/solutions/ebixone
- group: docs
  title: ''
  type: Documentation
  url: https://www.ebix.com/solutions/lending-asset-and-wealth-management
- group: docs
  title: ''
  type: Documentation
  url: https://www.ebix.com/solutions/travel-and-mobility
- group: docs
  title: ''
  type: Documentation
  url: https://www.ebix.com/services/payments
- group: docs
  title: ''
  type: Documentation
  url: https://www.ebix.com/services/travels
- group: docs
  title: ''
  type: Documentation
  url: https://www.ebix.com/services/ed-tech-and-insurance
- group: docs
  title: ''
  type: Documentation
  url: https://www.ebixasp.com/
- group: operate
  title: ''
  type: ProductHelp
  url: https://www.ebixasp.com/ebixasphelp/maintenance/Real_Time_Interface/Install_Download_Real-Time_Interface.htm
- group: operate
  title: ''
  type: Support
  url: https://www.ebixasp.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.ebix.com/news-and-media
- group: operate
  title: ''
  type: PressRelease
  url: https://www.prnewswire.com/news-releases/ebix-launches-plug-and-play-connector-platform-for-insurtech-and-fintech-extending-its-integration-capabilities-directly-into-client-environments-302576698.html
- group: operate
  title: ''
  type: Contact
  url: https://www.ebix.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ebix.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ebix.com/terms-of-use
- group: company
  title: ''
  type: Investors
  url: https://www.ebix.com/investors
- group: other
  title: ''
  type: AnnualReport
  url: https://www.ebix.com/pdf/Annual-Report-2024-25.pdf
- group: other
  title: ''
  type: Brand
  url: https://www.ebix.com/download-brand-toolkit
- group: other
  title: ''
  type: Sitemap
  url: https://www.ebix.com/sitemap.xml
- group: other
  title: ''
  type: Robots
  url: https://www.ebix.com/robots.txt
created: '2026-07-25'
description: 'Ebix is a United States insurance software and exchange company headquartered in Johns Creek, Georgia, operating as market infrastructure between carriers, MGAs, brokers and agencies rather than as a carrier itself. Its portfolio spans property and casualty agency management (EbixASP), P&C policy administration and broker systems (EbixEvolution, PlacingHub, Sunrise Exchange, iClose), life insurance and annuity distribution connectivity (EbixExchange), health insurance and employee benefits administration, health content, risk and compliance (RiskEnvision, WCExchange), and — through the EbixCash arm — travel, payments and forex services. Its core P&C plumbing is ACORD-native rather than API-native: TEAM-UP moves policy, claims and direct-bill commission download to agency management systems as ACORD-standard AL3 files, its Translation Services practice converts carrier-proprietary formats into ACORD AL3 and ACORD XML using Java/XML/XSLT, EbixASP maintains a continuously updated
  ACORD forms library with bi-directional exchange against ACORD applications, and the EbixASP Real-Time Interface synchronizes carrier credentials and service transactions with IVANS. Ebix markets API-driven quote-to-bind workflows and, since October 2025, a plug-and-play connector platform built with 1SilverBullet that exposes quoting, eApp, enrollment, underwriting checks, payments and policy servicing as modular APIs with "a standardized connector fabric with pre-built mappings and a developer portal" — but no public self-serve developer portal, API reference or machine-readable specification could be confirmed as of 2026-07-25. Every probed developer path on ebix.com (/developers, /api, /developer, /partners, /integrations) returns the site''s single-page-app homepage shell rather than a developer surface; developer.ebix.com and docs.ebix.com do not resolve; api.ebix.com answers with a JSON 404 and no documented routes; and the live EbixCash API Hub at api.ebixcash.com serves an OpenAPI
  document that returns HTTP 401 "Missing Authorization header". The one agent-facing discovery document Ebix does publish is a real llms.txt at www.ebix.com/llms.txt, which indexes the solution, service and corporate pages but names no API, portal or specification; every /.well-known/ probe across www.ebix.com, api.ebix.com, api.ebixcash.com and ebixasp.com missed, no first-party SDK exists in any public package registry, and no trust center, security.txt or vulnerability-disclosure program was found. Ebix''s integration surface is therefore customer- and partner-gated, sold and documented under contract, which is the norm for United States insurance infrastructure where no federal regulator and no open-insurance mandate exists. Ebix filed Chapter 11 in December 2023, sold its North American life and annuity assets to Zinnia, and exited bankruptcy on 30 August 2024 consolidated with Eraaya Lifespaces.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Ebix
nav: Providers
network: true
overview: 'Ebix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United States, Property and Casualty, Life Insurance, and Health Insurance.


  Ebix''s developer surface includes documentation, support, engineering blog, and 29 more developer resources.'
random_paper: 29
score:
  band: emerging
  composite: 17.6
  delta: -0.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 18.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 28.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ebix/refs/heads/main/screenshots/ebix-2026-07-25T212726.png
security:
- kind: authentication
  name: Ebix Authentication
  slug: ebix-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ebix Domain Security
  slug: ebix-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: ebix
tags:
- Insurance
- United States
- Property and Casualty
- Life Insurance
- Health Insurance
- Employee Benefits
- Agency Management
- Policy Administration
- Claims
- ACORD
- Insurtech
- Market Infrastructure
website: https://www.ebix.com/
---
