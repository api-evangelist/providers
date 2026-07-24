---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 23.1
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: USAA exposes member-permissioned financial data — account metadata, current and available balances, and transaction history for checking, savings, credit, and investment accounts — through consumer-pe
  name: USAA Open Banking via Aggregators
  slug: open-banking-aggregation
- description: USAA maintains a small set of public open-source projects on GitHub focused on internal developer tooling and cybersecurity rather than published product APIs. Notable repositories include sonar-quali
  name: USAA Open Source GitHub Projects
  slug: github-open-source
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.usaa.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usaa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usaa
- group: docs
  title: ''
  type: Documentation
  url: https://www.financialdataexchange.org/FDX/FDX/News/Spotlights/Member%20Spotlight%20USAA.aspx
- group: commercial
  title: ''
  type: Plans
  url: plans/usaa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/usaa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/usaa-finops.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/usaa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.usaa.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usaa-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/usaa-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/usaa-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/usaa-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/usaa-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/usaa-llms.txt
created: '2024-12-03'
description: USAA (United Services Automobile Association) is a Fortune 100 financial services group offering banking, investing, and insurance products exclusively to people and families who serve, or have served, in the United States military. USAA does not publish a first-party public developer portal or downloadable API specifications. Third-party access to member financial data is delivered through consumer-permissioned open-banking aggregators — Plaid, Mastercard Open Banking (formerly Flinks), and BankSync — using OAuth 2.0 tokenized authorization rather than shared credentials. USAA is an active member and board participant of the Financial Data Exchange (FDX) and helps shape the FDX API standard for secure open finance data sharing in the US.
finops:
- name: Usaa Finops
  service_category: Financial Services
  slug: usaa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usaa.png
json_schemas:
- name: USAA Bank Account
  property_count: 9
  slug: usaa-bank-account
- name: USAA Transaction
  property_count: 11
  slug: usaa-transaction
json_structures:
- name: Usaa Bank Account Structure
  property_count: 0
  slug: usaa-bank-account-structure
jsonld:
- class_count: 2
  name: Us Usaa Context
  property_count: 12
  slug: us-usaa-context
layout: provider
modified: '2026-07-23'
name: USAA
nav: Providers
network: true
overview: 'USAA publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Insurance, Military Finance, and Open Banking.


  The USAA catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  USAA''s developer surface includes documentation, authentication, and 13 more developer resources.'
plans:
- name: Usaa Plans Pricing
  plan_count: 1
  slug: usaa-plans-pricing
press:
- date: '2026-05-25'
  title: USAA selects Quavo's AI to strengthen compliance
  url: https://fintech.global/2025/09/04/usaa-selects-quavos-ai-to-strengthen-compliance/
- date: '2026-05-25'
  title: USAA revamps mobile app
  url: https://www.bankingdive.com/news/usaa-revamps-mobile-app/622303/
- date: '2026-05-25'
  title: USAA to use AI and gen AI across operations
  url: https://www.linkedin.com/posts/autofinancenews_usaa-aims-to-unplug-the-keyboard-with-gen-activity-7319068655399407616-yGkE
- date: '2026-05-25'
  title: 'USAA CIO on Generative AI: ''Relentless Learners Will Create ...'
  url: https://deloitte.wsj.com/sustainable-business/usaa-cio-on-generative-ai-relentless-learners-will-create-the-future-3ad0c760
- date: '2026-05-25'
  title: Responsible Use of Artificial Intelligence
  url: https://www.usaa.com/about/artificial-intelligence/
random_paper: 18
rate_limits:
- limit_count: 1
  name: Usaa Rate Limits
  slug: usaa-rate-limits
rules:
- name: USAA API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: usaa-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.3
  delta: 8.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 19.6
    discoverability: 80.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 29.1
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 50.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/usaa/refs/heads/main/screenshots/usaa-2026-06-20T200644.png
security:
- kind: authentication
  name: Usaa Authentication
  slug: usaa-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Usaa Domain Security
  slug: usaa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Usaa Vulnerability Disclosure
  slug: usaa-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: usaa
tags:
- Financial Services
- Banking
- Insurance
- Military Finance
- Open Banking
- Open Finance
- Financial Data Exchange
- United States
- Fortune 100
website: https://www.usaa.com
---
