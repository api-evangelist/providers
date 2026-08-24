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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ifttt Agentic Access
  operation_count: 3
  slug: ifttt-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 2
apis:
- description: Public HTTP API for triggering IFTTT Applets from any device or service by sending GET or POST requests to a per-user trigger URL. Supports up to three positional values per call or arbitrary JSON pay
  name: IFTTT Maker Webhooks API
  slug: webhooks-api
- description: The Trigger API from IFTTT — 2 operation(s) for trigger.
  name: IFTTT Trigger API
  slug: ifttt-trigger-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: IFTTT Webhooks (Maker) Trigger API
  slug: open-ifttt-trigger-api
- collection_type: open
  name: IFTTT Webhooks (Maker) API
  slug: open-ifttt
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ifttt-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ifttt-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ifttt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ifttt
- group: company
  title: ''
  type: Website
  url: https://ifttt.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.ifttt.com/hc/en-us/articles/115010230347-Webhooks-service-FAQ
- group: commercial
  title: ''
  type: Pricing
  url: https://ifttt.com/plans
- group: start
  title: ''
  type: Signup
  url: https://ifttt.com/join
- group: other
  title: ''
  type: Developer Platform
  url: https://platform.ifttt.com
created: '2026-05-11'
description: IFTTT (If This Then That) is a consumer and prosumer automation platform that connects more than 750 apps, devices, and services through conditional Applets that chain triggers to actions. The IFTTT Maker Webhooks service exposes a public HTTP API that lets developers fire triggers and execute Applets from any internet-connected device using a personal Webhooks key for authentication, with both form-encoded and JSON payload variants supported.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ifttt.png
layout: provider
modified: '2026-05-11'
name: IFTTT
nav: Providers
network: true
overview: 'IFTTT publishes 1 API on the [APIs.io](https://apis.io/) network: Trigger API. Tagged areas include Automation, Webhook, iPaaS, No-Code, and Smart Home.


  IFTTT''s developer surface includes documentation, pricing, signup flow, and 6 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 25.6
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 46.9
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 25.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ifttt/refs/heads/main/screenshots/ifttt-2026-06-20T183215.png
security:
- kind: domain-security
  name: Ifttt Domain Security
  slug: ifttt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ifttt
tags:
- Automation
- Webhook
- iPaaS
- No-Code
- Smart Home
- IoT
website: https://ifttt.com
---
