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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The LendingClub API provides access to platform services and data for enterprise integration and automation.
  name: LendingClub API
  slug: lendingclub-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lendingclub-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LendingClub
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lending-club
- group: company
  title: ''
  type: Website
  url: https://www.lendingclub.com
created: '2026-04-19'
description: LendingClub is a major US corporation and Fortune 1000 company. The LendingClub API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Lendingclub Finops
  service_category: Financial Services / API
  slug: lendingclub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lendingclub.png
layout: provider
modified: '2026-04-19'
name: LendingClub
nav: Providers
network: true
overview: LendingClub publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Personal Loans, and Banking.
plans:
- name: Lendingclub Plans Pricing
  plan_count: 1
  slug: lendingclub-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Lendingclub Rate Limits
  slug: lendingclub-rate-limits
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 8.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lendingclub/refs/heads/main/screenshots/lendingclub-2026-06-20T184419.png
security:
- kind: domain-security
  name: Lendingclub Domain Security
  slug: lendingclub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lendingclub
tags:
- Fintech
- Personal Loans
- Banking
website: https://www.lendingclub.com
---
