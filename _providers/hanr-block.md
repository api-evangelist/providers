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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
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
random_paper: 24
rate_limits:
- limit_count: 1
  name: Hanr Block Rate Limits
  slug: hanr-block-rate-limits
score:
  band: emerging
  composite: 15.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 15.9
  schema_version: 0.5
  scored_at: '2026-07-23'
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
