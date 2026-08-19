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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Wintrust's commercial "API banking" for treasury clients. Rather than a documented REST API, Wintrust connects business customers directly to its secure file transfer protocol (SFTP) for account balan
  name: Wintrust Treasury Management API Banking (SFTP)
  slug: wintrust-treasury-api-banking
- description: Wintrust does not expose a direct consumer open-banking API. Third-party applications reach Wintrust / iBusinessBanking account balances, transaction history and account-holder data through open-banki
  name: Wintrust Open Banking Data Access (Plaid, aggregator-mediated)
  slug: wintrust-open-banking-aggregator-access
artifact_total: 6
common:
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wintrust.com/privacy-information.html
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wintrust-financial-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wintrust-financial-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wintrust-financial-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.wintrust.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.wintrust.com/business-solutions/mid-market/banking/treasury-management.html
- group: company
  title: ''
  type: Blog
  url: https://www.wintrust.com/financial-education.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wintrust-financial-corporation
created: '2026-04-19'
description: Wintrust Financial Corporation is a Rosemont, Illinois-based financial holding company operating a network of chartered community banks (Wintrust Bank, N.A. and its affiliates) primarily across Illinois, Wisconsin, Indiana and Florida, plus specialty lending, wealth management and mortgage businesses. Wintrust does not publish a first-party public developer portal or downloadable API specifications; its programmatic surface is delivered through commercial treasury management. Wintrust describes "API banking" that connects businesses directly to its secure file transfer protocol (SFTP) for account balance and activity reporting, payment files (Positive Pay, ACH, wires, EDI, lockbox) and data-format translation (NACHA, EDI 820, BAI2). Consumer and small-business account data is reachable to third parties through open-banking aggregators — Plaid is the confirmed aggregator supporting Wintrust / iBusinessBanking access.
finops:
- name: Wintrust Financial Finops
  service_category: Banking
  slug: wintrust-financial-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wintrust-financial.png
layout: provider
modified: '2026-07-25'
name: Wintrust Financial
nav: Providers
network: true
overview: 'Wintrust Financial publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Financial Services, Treasury Management, Commercial Banking, and Open Banking.


  Wintrust Financial''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Wintrust Financial Plans Pricing
  plan_count: 1
  slug: wintrust-financial-plans-pricing
random_paper: 102
rate_limits:
- limit_count: 1
  name: Wintrust Financial Rate Limits
  slug: wintrust-financial-rate-limits
score:
  band: emerging
  composite: 11.5
  delta: -3.8
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 5.3
  previous_composite: 15.3
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 16.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wintrust-financial/refs/heads/main/screenshots/wintrust-financial-2026-06-20T201518.png
security:
- kind: domain-security
  name: Wintrust Financial Domain Security
  slug: wintrust-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wintrust-financial
tags:
- Banking
- Financial Services
- Treasury Management
- Commercial Banking
- Open Banking
- United States
website: https://www.wintrust.com
---
