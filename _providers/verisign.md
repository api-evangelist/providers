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
- description: The VeriSign API provides access to platform services and data for enterprise integration and automation.
  name: VeriSign API
  slug: verisign-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verisign-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/verisign
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/verisign
- group: company
  title: ''
  type: Website
  url: https://www.verisign.com
created: '2026-04-19'
description: VeriSign is a major US corporation and Fortune 1000 company. The VeriSign API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Verisign Finops
  service_category: Internet Infrastructure
  slug: verisign-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/verisign.png
layout: provider
modified: '2026-04-19'
name: VeriSign
nav: Providers
network: true
overview: VeriSign publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include DNS, Internet Infrastructure, and Security.
plans:
- name: Verisign Plans Pricing
  plan_count: 1
  slug: verisign-plans-pricing
random_paper: 126
rate_limits:
- limit_count: 1
  name: Verisign Rate Limits
  slug: verisign-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/verisign/refs/heads/main/screenshots/verisign-2026-06-20T200928.png
security:
- kind: domain-security
  name: Verisign Domain Security
  slug: verisign-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: verisign
tags:
- DNS
- Internet Infrastructure
- Security
website: https://www.verisign.com
---
