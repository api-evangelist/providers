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
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: A live GraphQL endpoint at api.dayforward.com/graphql that backs the Dayforward consumer application. Observed responding to GraphQL over HTTP POST (an empty operation returns a GRAPHQL_VALIDATION_FAI
  name: Dayforward GraphQL API
  slug: graphql
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://dayforward.io/
- group: company
  title: ''
  type: ConsumerWebsite
  url: https://www.dayforward.com/
- group: company
  title: ''
  type: About
  url: https://dayforward.io/about
- group: start
  title: ''
  type: SignUp
  url: https://www.dayforward.com/signin
- group: operate
  title: ''
  type: Support
  url: https://www.dayforward.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.dayforward.com/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dayforward.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dayforward.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/noho-digital
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dayfwrd/
- group: company
  title: ''
  type: Careers
  url: https://www.dayforward.com/careers
- group: design
  title: ''
  type: Conformance
  url: conformance/dayforward-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dayforward-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dayforward-domain-security.yml
created: '2026-08-04'
description: Dayforward is a New York-based life insurance technology and services group founded in 2019 by Aaron Shapiro. It owns Commercial Travelers Life Insurance Company (NY-domiciled carrier) and Dayforward Insurance Agency LLC (licensed in all 50 states), and sells income-replacement term life insurance direct to consumers at dayforward.com. Since pivoting to B2B at dayforward.io it licenses Workbench — a SaaS platform covering the full life insurance lifecycle from agent selling and automated underwriting through policy administration and service — plus managed distribution, underwriting and administration services to other carriers and distributors. Workbench is marketed as including "APIs, plug-and-play widgets, single sign-on support, and robust administration tools", but Dayforward publishes no public developer portal, API documentation, OpenAPI definition or SDKs.
image: https://storage.googleapis.com/df-prod-cdn/img/unfurl.jpg
layout: provider
modified: '2026-08-04'
name: Dayforward
nav: Providers
network: true
overview: 'Dayforward publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Life Insurance, Insurtech, and Financial Services.


  Dayforward''s developer surface includes signup flow, support, FAQ, and 11 more developer resources.'
random_paper: 31
score:
  band: emerging
  composite: 19.2
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 19.2
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 28.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dayforward/refs/heads/main/screenshots/dayforward-2026-08-07T164205.png
security:
- kind: domain-security
  name: Dayforward Domain Security
  slug: dayforward-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dayforward
tags:
- Company
- Insurance
- Life Insurance
- Insurtech
- Financial Services
- Underwriting
- Policy Administration
- SaaS
- GraphQL
website: https://dayforward.io/
---
