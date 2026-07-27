---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 27.9
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: Read-only REST API over the Financial Services Register, the FCA's public record of authorised firms, individuals, funds and appointed representatives. Resources are addressed by Firm Reference Number
  name: FCA Financial Services Register API
  slug: fca-financial-services-register-api
- description: Anonymous machine-to-machine query interface over the file artefacts the FCA publishes through data.fca.org.uk, documented in the FCA's own FIRDS and FITRS technical specifications. It is an OpenSearc
  name: FCA Data Publication API (FIRDS / FITRS)
  slug: fca-data-publication-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fca-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fca.org.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fca.org.uk/firms/financial-services-register
- group: other
  title: ''
  type: Handbook
  url: https://handbook.fca.org.uk/
- group: other
  title: ''
  type: Data
  url: https://www.fca.org.uk/data
- group: start
  title: ''
  type: Registers
  url: https://data.fca.org.uk/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/financial-conduct-authority
- group: company
  title: ''
  type: Blog
  url: https://www.fca.org.uk/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://register.fca.org.uk/Developer/s/
- group: docs
  title: ''
  type: APIReference
  url: https://register.fca.org.uk/Developer/s/
- group: start
  title: ''
  type: SignUp
  url: https://register.fca.org.uk/Developer/ShAPI_LoginPage?ec=302&startURL=%2FDeveloper%2Fs%2F
- group: operate
  title: ''
  type: Support
  url: https://www.fca.org.uk/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fca.org.uk/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fca.org.uk/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fca.org.uk/firms/financial-services-register/data-extract
- group: auth
  title: ''
  type: Authentication
  url: authentication/fca-uk-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fca-uk-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fca-uk-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fca-uk-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fca-uk-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fca-uk-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fca-uk-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/fca-uk-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fca-uk-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fca-uk-llms.txt
created: '2026-07-25'
description: 'The Financial Conduct Authority (FCA) is the United Kingdom''s conduct regulator for around 42,000 financial services firms and the prudential regulator for most non-bank firms, operating alongside the Prudential Regulation Authority under the dual-regulation model. In insurance the FCA owns conduct regulation of general insurance and protection markets through ICOBS and the Consumer Duty, authorises and supervises insurers, Lloyd''s managing agents, MGAs, brokers and appointed representatives, and publishes market-wide insurance data such as the annual General Insurance Value Measures. Its API posture is that of a regulator, not a carrier: there is no open-insurance obligation in the UK and the FCA publishes no insurance product API of its own. It does operate two genuine public APIs. The Financial Services Register API at register.fca.org.uk/services/V0.1 exposes firm, individual and fund authorisation records including insurance permissions and appointed-representative relationships;
  access is free and self-serve but the developer portal and its reference documentation sit behind a Salesforce registration login, and authentication is by X-Auth-Email and X-Auth-Key headers. The data publication API at api.data.fca.org.uk is an anonymous OpenSearch-style query interface over FIRDS and FITRS file artefacts, documented in the FCA''s own published technical specifications — markets reference data, not insurance data. Neither API has an OpenAPI definition. Everything else the FCA publishes for the insurance market is documents and spreadsheets: the Handbook, market bulletins, consultation papers, and XLSX data releases. The FCA''s Open Finance roadmap of 14 April 2026 names insurance as an in-scope sector but remains a vision document, with a formal discussion paper on the first scheme not due until Q4 2026, so no insurance data-sharing API mandate exists. No ACORD reference appears anywhere on fca.org.uk.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Financial Conduct Authority
nav: Providers
network: true
overview: 'Financial Conduct Authority publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Regulator, Market Infrastructure, and Financial Services.


  Financial Conduct Authority''s developer surface includes documentation, engineering blog, API reference, signup flow, support, pricing, authentication, and 18 more developer resources.'
random_paper: 23
rate_limits:
- limit_count: 0
  name: Fca Uk Rate Limits
  slug: fca-uk-rate-limits
score:
  band: thin
  composite: 30.6
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 30.6
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fca-uk/refs/heads/main/screenshots/fca-uk-2026-07-25T214305.png
security:
- kind: authentication
  name: Fca Uk Authentication
  slug: fca-uk-authentication
  summary_line: apiKey/none · 2 schemes
- kind: domain-security
  name: Fca Uk Domain Security
  slug: fca-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fca-uk
tags:
- Insurance
- United Kingdom
- Regulator
- Market Infrastructure
- Financial Services
- Public Register
- Conduct Regulation
- Open Finance
- Insurance Intermediaries
- Risk Data
- Market Data
- Reference Data
- MiFID II
website: https://www.fca.org.uk/
---
