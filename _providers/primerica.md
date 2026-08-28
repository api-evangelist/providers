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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Primerica API provides access to platform services and data for enterprise integration and automation.
  name: Primerica API
  slug: primerica-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/primerica-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Primerica
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/primerica
- group: company
  title: ''
  type: Website
  url: https://www.primerica.com
created: '2026-04-19'
description: Primerica is a major US corporation and Fortune 1000 company. The Primerica API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Primerica Finops
  service_category: Financial Services
  slug: primerica-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/primerica.png
layout: provider
modified: '2026-04-19'
name: Primerica
nav: Providers
network: true
overview: Primerica publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Financial-Services, and Life Insurance.
plans:
- name: Primerica Plans Pricing
  plan_count: 1
  slug: primerica-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Primerica Rate Limits
  slug: primerica-rate-limits
score:
  band: minimal
  composite: 7.9
  delta: 1.9
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 6.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/primerica/refs/heads/main/screenshots/primerica-2026-06-20T192103.png
security:
- kind: domain-security
  name: Primerica Domain Security
  slug: primerica-domain-security
  summary_line: TLSv1.2 · DMARC
slug: primerica
tags:
- Insurance
- Financial-Services
- Life Insurance
website: https://www.primerica.com
---
