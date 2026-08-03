---
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
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: 'Real-time fraud and risk detection API surface. Customers stream user events and transactions to a DataVisor integration endpoint and receive detection results, risk scores and reason codes back. The '
  name: DataVisor Fraud and Risk Platform API
  slug: fraud-and-risk-platform
- description: Device intelligence surface. The dEdge SDK is embedded in an iOS app, Android app or HTML5 web page, sends encrypted device data to the dEdge server, and receives a device token. That token is then us
  name: DataVisor dEdge Device Intelligence WebAPI
  slug: dedge-device-intelligence
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.datavisor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.datavisor.com/integrations/datavisor-integration-guide-for-comprehensive-fraud-solution
- group: docs
  title: ''
  type: APIReference
  url: https://www.datavisor.com/datavisor-api-guide
- group: operate
  title: ''
  type: Support
  url: https://datavisor.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.datavisor.com/blog
- group: company
  title: ''
  type: About
  url: https://www.datavisor.com/about
- group: company
  title: ''
  type: Careers
  url: https://apply.workable.com/datavisor-jobs/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/datavisor/
- group: company
  title: ''
  type: Partners
  url: https://www.datavisor.com/partners
- group: other
  title: ''
  type: Marketplace
  url: https://azuremarketplace.microsoft.com/en/marketplace/apps/datavisor.datavisor_dcube
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.datavisor.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datavisor.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: conformance/datavisor-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/datavisor-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/datavisor-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/datavisor-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datavisor-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/datavisor-llms.txt
created: '2026-08-01'
description: 'DataVisor is a Mountain View, California fraud and risk platform company founded in 2013 that applies unsupervised machine learning, rules, device intelligence and link analysis to detect fraud and financial crime in real time for banks, credit unions, fintechs, digital payments, life insurance and digital enterprises. The platform covers ACH and wire fraud, account onboarding, application fraud, account takeover, card fraud, check fraud, FinCrime/AML and promotion abuse, and is delivered as an API-integrated detection engine: customers stream events to a DataVisor integration endpoint over real-time synchronous HTTPS REST (TLS 1.2) or batch/cloud-bucket pipes, and consume detection results, scores and reason codes back through APIs or bucket push. Named product modules include the Fraud and Risk Platform, the dEdge device intelligence SDK and WebAPI, dOps fraud and risk operations, dVecto managed ML detection, the UML Modeling Studio and the Vera conversational AI agent. API
  references and the integration guide are published publicly, but the API guide itself, the detailed endpoint documentation and the admin console are gated behind customer accounts and technical account managers.'
image: https://cdn.prod.website-files.com/6761698ddf0927f45e0c6407/69a89878e0d86861b9163582_DataVisor-OG.png
layout: provider
modified: '2026-08-01'
name: DataVisor
nav: Providers
network: true
overview: 'DataVisor publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fraud Detection, Fraud Prevention, Anti-Money Laundering, and Financial Crime.


  DataVisor''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 13 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 24.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 77.8
    governance: 12.5
    operational_transparency: 0.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 38.0
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Datavisor Authentication
  slug: datavisor-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Datavisor Domain Security
  slug: datavisor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datavisor
tags:
- Company
- Fraud Detection
- Fraud Prevention
- Anti-Money Laundering
- Financial Crime
- Risk Management
- Machine Learning
- Artificial Intelligence
- Device Intelligence
- Banking
- Payments
- Compliance
website: https://www.datavisor.com/
---
