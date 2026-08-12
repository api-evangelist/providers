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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
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
random_paper: 7
rate_limits:
- limit_count: 1
  name: Schlumberger Rate Limits
  slug: schlumberger-rate-limits
score:
  band: minimal
  composite: 10.9
  delta: -4.4
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 15.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
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
