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
- description: The Josys API provides programmatic access to the Josys SaaS and IT asset management platform, including endpoints for users, applications, devices, licenses, and provisioning workflows.
  name: Josys API
  slug: josys-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/josys-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JoSys
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/josys-inc
- group: company
  title: ''
  type: Website
  url: https://www.josys.com
- group: other
  title: ''
  type: Developer
  url: https://developer.josys.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.josys.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://josys.com/llms.txt
created: '2026-03-27'
description: Josys is a SaaS and IT asset management platform providing automated provisioning, license optimization, and device management. Josys publishes a developer API for programmatic access to the platform.
finops:
- name: Josys Finops
  service_category: API
  slug: josys-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/josys.png
layout: provider
modified: '2026-04-28'
name: Josys
nav: Providers
network: true
overview: Josys publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include IT Asset Management, SaaS Management, Identity, and Device Management.
plans:
- name: Josys Plans Pricing
  plan_count: 3
  slug: josys-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Josys Rate Limits
  slug: josys-rate-limits
score:
  band: emerging
  composite: 21.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 21.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/josys/refs/heads/main/screenshots/josys-2026-06-20T183803.png
security:
- kind: domain-security
  name: Josys Domain Security
  slug: josys-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: josys
tags:
- IT Asset Management
- SaaS Management
- Identity
- Device Management
website: https://www.josys.com
---
