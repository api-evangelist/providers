---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Heartland Financial USA API provides access to platform services and data for enterprise integration and automation.
  name: Heartland Financial USA API
  slug: heartland-financial-usa-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heartland-financial-usa-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/htlfusa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/poweredbyhtlf
- group: company
  title: ''
  type: Website
  url: https://www.htlf.com
created: '2026-04-19'
description: Heartland Financial USA is a major US corporation and Fortune 1000 company. The Heartland Financial USA API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Heartland Financial Usa Finops
  service_category: Banking / Financial Services
  slug: heartland-financial-usa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/heartland-financial-usa.png
layout: provider
modified: '2026-04-19'
name: Heartland Financial USA
nav: Providers
network: true
overview: Heartland Financial USA publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Banking and Financial Services.
plans:
- name: Heartland Financial Usa Plans Pricing
  plan_count: 1
  slug: heartland-financial-usa-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Heartland Financial Usa Rate Limits
  slug: heartland-financial-usa-rate-limits
score:
  band: emerging
  composite: 14.0
  delta: -2.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 16.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Heartland Financial Usa Domain Security
  slug: heartland-financial-usa-domain-security
  summary_line: DMARC
slug: heartland-financial-usa
tags:
- Banking
- Financial Services
website: https://www.htlf.com
---
