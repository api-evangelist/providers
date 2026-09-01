---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/fullcast/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atrium-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/atrium-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/atrium-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.atriumhq.com
- group: start
  title: ''
  type: Login
  url: https://app.atriumhq.com/auth/login
coverage:
  checked: '2026-08-13'
  detail: Atrium was acquired by Fullcast and now ships as Fullcast Performance — every path on atriumhq.com, including /.well-known/*, answers a blanket HTTP 301 to https://www.fullcast.com/product/fullcast-performance/, and the only Atrium host still resolving is the customer application login at app.atriumhq.com.
  evidence:
  - status: 301
    url: https://www.atriumhq.com/
  - status: 404
    url: https://app.atriumhq.com/.well-known/agent-card.json
  - status: 0
    url: https://docs.atriumhq.com/
  reason: defunct
  state: none
created: '2026-07-17'
description: Atrium is a sales-effectiveness and sales-performance business intelligence platform for revenue teams. It continuously monitors sales KPIs to surface anomalies in rep and team performance, detects which behaviors and activities are driving (or dragging) output, and delivers AI-powered coaching recommendations to managers and reps. The product connects directly to Salesforce, HubSpot, data warehouses, and communication tools rather than exposing a public developer API. Founded in San Francisco by Jason Heidema (CEO) and Peter Kazanjy and backed by Andreessen Horowitz (a16z), Bullpen Capital, and Electric Capital, Atrium was acquired by Fullcast in 2025 and is now offered as Fullcast Performance; atriumhq.com redirects to fullcast.com and only the customer application login at app.atriumhq.com remains on the Atrium domain.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/atrium.png
layout: provider
modified: '2026-08-13'
name: Atrium
nav: Providers
network: true
overview: Atrium is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Analytics, Business Intelligence, and Sales Performance.
plans:
- name: Atrium Plans Pricing
  plan_count: 0
  slug: atrium-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Atrium Rate Limits
  slug: atrium-rate-limits
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atrium/refs/heads/main/screenshots/atrium-2026-07-25T201627.png
security:
- kind: domain-security
  name: Atrium Domain Security
  slug: atrium-domain-security
  summary_line: TLSv1.3 · DMARC
slug: atrium
tags:
- Company
- Sales
- Analytics
- Business Intelligence
- Sales Performance
- Revenue Operations
- CRM
website: https://www.atriumhq.com
---
