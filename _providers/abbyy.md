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
- description: ABBYY provides intelligent document processing and process intelligence solutions powered by AI.
  name: ABBYY
  slug: abbyy
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/abbyy-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abbyy-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/abbyy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abbyy
- group: company
  title: ''
  type: Website
  url: https://www.abbyy.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.abbyy.com/developers/
created: '2026-03-27'
description: ABBYY provides intelligent document processing and process intelligence solutions powered by AI.
finops:
- name: Abbyy Finops
  service_category: API
  slug: abbyy-finops
image: /assets/icons/abbyy.png
layout: provider
modified: '2026-03-27'
name: ABBYY
nav: Providers
network: true
overview: 'ABBYY publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Automation and Document Processing.


  ABBYY''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Abbyy Plans Pricing
  plan_count: 3
  slug: abbyy-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Abbyy Rate Limits
  slug: abbyy-rate-limits
score:
  band: minimal
  composite: 10.2
  delta: -2.1
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abbyy/refs/heads/main/screenshots/abbyy-2026-07-25T181335.png
security:
- kind: domain-security
  name: Abbyy Domain Security
  slug: abbyy-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Abbyy Trust Center
  slug: abbyy-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: abbyy
tags:
- AI Automation
- Document Processing
website: https://www.abbyy.com
---
