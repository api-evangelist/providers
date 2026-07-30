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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Inbound HTTP API endpoints and per-table webhook sources that let external systems push JSON records into Clay tables to trigger enrichment, AI research, and downstream workflows, and pull or POST enr
  name: Clay HTTP API
  slug: http-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clay-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/grow-with-clay
- group: company
  title: ''
  type: Website
  url: https://www.clay.com
- group: docs
  title: ''
  type: Documentation
  url: https://university.clay.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clay.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.clay.com/signup
- group: operate
  title: ''
  type: Community
  url: https://community.clay.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://app.clay.com/llms.txt
created: '2026-05-11'
description: Clay is a go-to-market platform that combines people and company data enrichment from 150+ premium providers, AI research agents (Claygents), intent signals, and workflow automation for sales, marketing, and revenue operations teams. Clay exposes inbound HTTP API endpoints and webhooks so external systems can push records into Clay tables, trigger enrichments, and receive enriched data for CRM sync, lead scoring, and outbound workflows.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clay.png
layout: provider
modified: '2026-05-11'
name: Clay
nav: Providers
network: true
overview: 'Clay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Intelligence, Data Enrichment, GTM, Lead Generation, and Workflow Automation.


  Clay''s developer surface includes documentation, pricing, signup flow, and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 11.6
  delta: -2.4
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clay/refs/heads/main/screenshots/clay-2026-06-20T174449.png
security:
- kind: domain-security
  name: Clay Domain Security
  slug: clay-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clay
tags:
- Sales Intelligence
- Data Enrichment
- GTM
- Lead Generation
- Workflow Automation
- AI Agents
- Webhooks
website: https://www.clay.com
---
