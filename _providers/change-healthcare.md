---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: The Change Healthcare API provides access to platform services and data for enterprise integration and automation.
  name: Change Healthcare API
  slug: change-healthcare-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/change-healthcare-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/changehealthcare
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/change-healthcare
- group: company
  title: ''
  type: Website
  url: https://www.changehealthcare.com
created: '2026-04-19'
description: Change Healthcare is a major US corporation and Fortune 1000 company. The Change Healthcare API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Change Healthcare Finops
  service_category: Healthcare / Data Exchange
  slug: change-healthcare-finops
graphqls:
- description: This conceptual GraphQL schema represents the Change Healthcare (now part of Optum/UnitedHealth Group) healthcare transaction and data platform. Change Healthcare operates as one of the largest health
  name: Change Healthcare GraphQL Schema
  slug: change-healthcare-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/change-healthcare.png
layout: provider
modified: '2026-04-19'
name: Change Healthcare
nav: Providers
network: true
overview: Change Healthcare publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Technology, and Analytics.
plans:
- name: Change Healthcare Plans Pricing
  plan_count: 2
  slug: change-healthcare-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Change Healthcare Rate Limits
  slug: change-healthcare-rate-limits
score:
  band: emerging
  composite: 18.7
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 43.2
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 18.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/change-healthcare/refs/heads/main/screenshots/change-healthcare-2026-06-20T174215.png
security:
- kind: domain-security
  name: Change Healthcare Domain Security
  slug: change-healthcare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: change-healthcare
tags:
- Healthcare
- Technology
- Analytics
website: https://www.changehealthcare.com
---
