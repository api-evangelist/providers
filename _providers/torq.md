---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Torq REST API allows programmatic management of workspace resources including workflows, users, secrets, triggers, and webhooks. API keys are workspace-scoped and support both US and EU regional e
  name: Torq REST API
  slug: torq-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/torq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://torq.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.torq.io/docs/what-is-torq
- group: docs
  title: ''
  type: APIReference
  url: https://developers.torq.io/apidocs/overview
- group: other
  title: ''
  type: KnowledgeBase
  url: https://kb.torq.io/en/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/torqio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/torqio/
- group: other
  title: ''
  type: X
  url: https://x.com/torq_io
- group: company
  title: ''
  type: Blog
  url: https://torq.io/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.torq.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/torq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/torq-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/torq-finops.yml
created: 2026-06-13
description: Torq is an enterprise-grade AI-driven hyper-automation security platform that enables security operations teams to triage, investigate, and respond to threats at machine speed. The REST API provides programmatic management of workspace resources including workflows, users, secrets, triggers, webhooks, and automated incident response playbooks. Torq supports no-code, low-code, and full-code security automation with 300+ integrations and regional endpoints in the US and EU.
finops:
- name: Torq Finops
  service_category: ''
  slug: torq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/torq.png
jsonld:
- class_count: 36
  name: Torq Context
  property_count: 0
  slug: torq-context
layout: provider
modified: 2026-06-13
name: Torq
nav: Providers
network: true
overview: 'Torq publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Security Automation, SOAR, Hyper-Automation, Security Orchestration, and Incident Response.


  The Torq catalog on APIs.io includes 1 JSON-LD context.


  Torq''s developer surface includes documentation, API reference, engineering blog, and 10 more developer resources.'
plans:
- name: Torq Plans Pricing
  plan_count: 3
  slug: torq-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Torq Rate Limits
  slug: torq-rate-limits
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 47.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 37.3
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 33.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/torq/refs/heads/main/screenshots/torq-2026-06-20T195501.png
security:
- kind: domain-security
  name: Torq Domain Security
  slug: torq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: torq
tags:
- Security Automation
- SOAR
- Hyper-Automation
- Security Orchestration
- Incident Response
- No-Code
- AI SOC
- Workflows
- Playbooks
- Security Operations
website: https://torq.io/
---
