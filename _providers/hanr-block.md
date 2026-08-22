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
api_count: 1
apis:
- description: The H&R Block API provides access to platform services and data for enterprise integration and automation.
  name: H&R Block API
  slug: hanr-block-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hanr-block-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hrblock-dsa
- group: company
  title: ''
  type: Website
  url: https://www.hrblock.com
created: '2026-04-19'
description: H&R Block is a major US corporation and Fortune 1000 company. The H&R Block API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Hanr Block Finops
  service_category: Tax Preparation / Financial Services Partner API
  slug: hanr-block-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hanr-block.png
layout: provider
modified: '2026-04-19'
name: H&R Block
nav: Providers
network: true
overview: H&R Block publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Tax Preparation, Financial Services, and Fortune 1000.
plans:
- name: Hanr Block Plans Pricing
  plan_count: 1
  slug: hanr-block-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Hanr Block Rate Limits
  slug: hanr-block-rate-limits
score:
  band: minimal
  composite: 8.7
  delta: -0.3
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 9.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hanr-block/refs/heads/main/screenshots/hanr-block-2026-06-20T182508.png
security:
- kind: domain-security
  name: Hanr Block Domain Security
  slug: hanr-block-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hanr-block
tags:
- Tax Preparation
- Financial Services
- Fortune 1000
website: https://www.hrblock.com
---
