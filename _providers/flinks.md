---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Flinks Agentic Access
  operation_count: 12
  slug: flinks-agentic-access
  summary_line: 12 operations · 11 acting
api_count: 6
apis:
- description: The Authorize API from Flinks — 1 operation(s) for authorize.
  name: Flinks Authorize API
  slug: flinks-authorize-api
- description: The Connect API from Flinks — 5 operation(s) for connect.
  name: Flinks Connect API
  slug: flinks-connect-api
- description: The Enrich API from Flinks — 1 operation(s) for enrich.
  name: Flinks Enrich API
  slug: flinks-enrich-api
- description: The Fraud API from Flinks — 2 operation(s) for fraud.
  name: Flinks Fraud API
  slug: flinks-fraud-api
- description: The Identity API from Flinks — 1 operation(s) for identity.
  name: Flinks Identity API
  slug: flinks-identity-api
- description: The Score API from Flinks — 2 operation(s) for score.
  name: Flinks Score API
  slug: flinks-score-api
artifact_total: 15
collections:
- collection_type: open
  name: Flinks API
  slug: open-flinks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flinks-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/flinks-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/flinks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flinks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flinks-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flinks
- group: company
  title: ''
  type: Website
  url: https://flinks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flinks.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/flinks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flinks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/flinks-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://flinks.com/blog/
created: '2026-07-01'
description: Flinks is a Canadian financial data platform (owned by National Bank of Canada) that lets businesses connect to consumer and business bank accounts to aggregate account, transaction, and statement data, verify identity, and derive income, credit-risk, and fraud analytics. Access begins with a Flinks Connect authentication session and a multi-step /Authorize (MFA) call, after which banking, enrichment, and analytics endpoints are invoked with the returned RequestId.
finops:
- name: Flinks Finops
  service_category: Financial Data and Analytics
  slug: flinks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flinks.png
layout: provider
modified: '2026-07-01'
name: Flinks
nav: Providers
network: true
overview: 'Flinks publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authorize API, Connect API, Enrich API, and 3 more. Tagged areas include Financial Data, Open Banking, Bank Aggregation, Fintech, and Canada.


  Flinks'' developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Flinks Plans Pricing
  plan_count: 2
  slug: flinks-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 4
  name: Flinks Rate Limits
  slug: flinks-rate-limits
score:
  band: thin
  composite: 38.1
  delta: 2.1
  facets:
    commercial_clarity: 36.8
    contract_quality: 53.7
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.0
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 50.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Flinks Authentication
  slug: flinks-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Flinks Domain Security
  slug: flinks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flinks Vulnerability Disclosure
  slug: flinks-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Flinks Trust Center
  slug: flinks-trust-center
  summary_line: SOC 2, PCI DSS
slug: flinks
tags:
- Financial Data
- Open Banking
- Bank Aggregation
- Fintech
- Canada
website: https://flinks.com/
---
