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
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.1
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 11
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
modified: '2026-07-25'
name: USAA
nav: Providers
network: true
overview: 'USAA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Insurance, Military Finance, and Open Banking.


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
random_paper: 6
rate_limits:
- limit_count: 1
  name: Usaa Rate Limits
  slug: usaa-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: USAA API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: usaa-jsonschema-spectral-rules
score:
  band: emerging
  composite: 20.1
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.0
    contract_quality: 11.3
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 28.0
    operational_transparency: 18.4
  previous_composite: 20.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 29.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
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
- Financial-Services
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
