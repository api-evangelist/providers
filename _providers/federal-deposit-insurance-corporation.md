---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Federal Deposit Insurance Corporation Agentic Access
  operation_count: 7
  slug: federal-deposit-insurance-corporation-agentic-access
  summary_line: 7 operations
api_count: 7
apis:
- description: Demographic statistics
  name: Federal Deposit Insurance Corporation Demographics API
  slug: federal-deposit-insurance-corporation-demographics-api
- description: Summary of deposits
  name: Federal Deposit Insurance Corporation Deposits API
  slug: federal-deposit-insurance-corporation-deposits-api
- description: Failed bank information
  name: Federal Deposit Insurance Corporation Failures API
  slug: federal-deposit-insurance-corporation-failures-api
- description: Financial reports and metrics
  name: Federal Deposit Insurance Corporation Financials API
  slug: federal-deposit-insurance-corporation-financials-api
- description: Institution historical events
  name: Federal Deposit Insurance Corporation History API
  slug: federal-deposit-insurance-corporation-history-api
- description: FDIC-insured institution data
  name: Federal Deposit Insurance Corporation Institutions API
  slug: federal-deposit-insurance-corporation-institutions-api
- description: Branch and office locations
  name: Federal Deposit Insurance Corporation Locations API
  slug: federal-deposit-insurance-corporation-locations-api
artifact_total: 15
collections:
- collection_type: open
  name: FDIC BankFind Suite API
  slug: open-bankfind
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/federal-deposit-insurance-corporation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-deposit-insurance-corporation-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fdic
- group: company
  title: ''
  type: Website
  url: https://www.fdic.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://banks.data.fdic.gov/docs/
created: '2024-12-25'
description: The Federal Deposit Insurance Corporation (FDIC) is an independent agency of the United States government that provides deposit insurance to depositors in US commercial banks and savings institutions. The FDIC also supervises and examines banks for safety and soundness, promotes consumer protection, and publishes the BankFind Suite API for accessing data on FDIC-insured institutions.
examples:
- key_count: 2
  name: Institution
  slug: institution
finops:
- name: Federal Deposit Insurance Corporation Finops
  service_category: API
  slug: federal-deposit-insurance-corporation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-deposit-insurance-corporation.png
layout: provider
modified: '2026-05-19'
name: Federal Deposit Insurance Corporation
nav: Providers
network: true
overview: 'Federal Deposit Insurance Corporation publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Demographics API, Deposits API, Failures API, and 4 more. Tagged areas include Banking, Federal Government, Financial Data, and Insurance.


  The Federal Deposit Insurance Corporation catalog on APIs.io includes 1 Spectral governance ruleset.


  Federal Deposit Insurance Corporation''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Federal Deposit Insurance Corporation Plans Pricing
  plan_count: 3
  slug: federal-deposit-insurance-corporation-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Federal Deposit Insurance Corporation Rate Limits
  slug: federal-deposit-insurance-corporation-rate-limits
rules:
- name: Federal Deposit Insurance Corporation API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: bankfind-rules
score:
  band: thin
  composite: 30.4
  delta: -2.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.8
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 10.4
    operational_transparency: 31.6
  previous_composite: 32.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-deposit-insurance-corporation/refs/heads/main/screenshots/federal-deposit-insurance-corporation-2026-06-20T181118.png
security:
- kind: domain-security
  name: Federal Deposit Insurance Corporation Domain Security
  slug: federal-deposit-insurance-corporation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: federal-deposit-insurance-corporation
tags:
- Banking
- Federal Government
- Financial Data
- Insurance
website: https://www.fdic.gov/
---
