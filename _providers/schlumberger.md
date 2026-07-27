---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
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
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: The SLB (Schlumberger) API provides access to platform services and data for enterprise integration and automation.
  name: SLB (Schlumberger) API
  slug: schlumberger-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/schlumberger-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/schlumberger-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Schlumberger
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/slbglobal
- group: company
  title: ''
  type: Website
  url: https://www.slb.com
created: '2026-04-19'
description: SLB (Schlumberger) is a major US corporation and Fortune 1000 company. The SLB (Schlumberger) API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Schlumberger Finops
  service_category: Energy Services
  slug: schlumberger-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/schlumberger.png
layout: provider
modified: '2026-04-19'
name: SLB (Schlumberger)
nav: Providers
network: true
overview: SLB (Schlumberger) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy and Oilfield Services.
plans:
- name: Schlumberger Plans Pricing
  plan_count: 1
  slug: schlumberger-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 1
  name: Schlumberger Rate Limits
  slug: schlumberger-rate-limits
score:
  band: emerging
  composite: 17.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 17.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/schlumberger/refs/heads/main/screenshots/schlumberger-2026-06-20T193540.png
security:
- kind: domain-security
  name: Schlumberger Domain Security
  slug: schlumberger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Schlumberger Vulnerability Disclosure
  slug: schlumberger-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: schlumberger
tags:
- Energy
- Oilfield Services
website: https://www.slb.com
---
