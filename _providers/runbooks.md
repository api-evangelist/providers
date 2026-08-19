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
- description: The Runbooks platform provides an integrated IT operations suite covering ITSM (service desk, incident management, knowledge base, change management, CSAT tracking, SLA management), ITAM (hardware and
  name: Runbooks IT Operations Platform
  slug: runbooks
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runbooks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://runbooks.com
- group: commercial
  title: ''
  type: Pricing
  url: https://runbooks.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.runbooks.com
- group: auth
  title: ''
  type: Security
  url: https://runbooks.com/security
created: '2025-01-01'
description: Runbooks is an all-in-one IT operations platform purpose-built for IT teams and managed service providers (MSPs). It consolidates ITSM (service desk, ticketing, incident management, knowledge base, SLA management), ITAM (hardware and software asset tracking, lifecycle management, warranty tracking, QR code asset labels), BizOps (CRM, client management, quarterly business reviews, budget forecasting, vendor management), SecOps (audit logs, MFA, password management), and Insights (automated reports, satisfaction tracking, quality assurance, KPI analytics) into a single integrated system. The platform targets IT departments and MSPs managing 50-5,000 users at a flat $25 per tech per month pricing model with no tiers or hidden fees. Runbooks is SOC 2 compliant with 99.9% uptime.
finops:
- name: Runbooks Finops
  service_category: API
  slug: runbooks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/runbooks.png
layout: provider
modified: '2026-05-02'
name: Runbooks
nav: Providers
network: true
overview: 'Runbooks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include ITSM, ITAM, IT Operations, Managed Service Provider, and Help Desk.


  Runbooks'' developer surface includes pricing and 4 more developer resources.'
plans:
- name: Runbooks Plans Pricing
  plan_count: 3
  slug: runbooks-plans-pricing
random_paper: 138
rate_limits:
- limit_count: 5
  name: Runbooks Rate Limits
  slug: runbooks-rate-limits
score:
  band: emerging
  composite: 12.4
  delta: -4.7
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 17.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/runbooks/refs/heads/main/screenshots/runbooks-2026-06-20T193248.png
security:
- kind: domain-security
  name: Runbooks Domain Security
  slug: runbooks-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: runbooks
tags:
- ITSM
- ITAM
- IT Operations
- Managed Service Provider
- Help Desk
- Asset Management
- Incident Management
- Security Operations
- CRM
- IT Service Management
website: https://runbooks.com
---
