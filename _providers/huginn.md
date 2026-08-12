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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: The Huginn platform is a self-hosted Ruby on Rails application that orchestrates agents, scenarios, and events. Operators install and run their own instance and configure agents to consume and produce
  name: Huginn Platform
  slug: huginn-platform
- description: Each Huginn instance exposes a Web Requests endpoint that lets external systems POST or GET events into a configured Webhook Agent. The endpoint lives at /users/{user_id}/web_requests/{agent_id}/{secr
  name: Huginn Web Requests API
  slug: huginn-web-requests-api
artifact_total: 5
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/huginn/huginn/releases
- group: company
  title: ''
  type: Website
  url: https://github.com/huginn/huginn
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/huginn/huginn/wiki
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/huginn/huginn
- group: commercial
  title: ''
  type: License
  url: https://github.com/huginn/huginn/blob/master/LICENSE
- group: operate
  title: ''
  type: Issues
  url: https://github.com/huginn/huginn/issues
- group: design
  title: ''
  type: Rules
  url: https://raw.githubusercontent.com/api-evangelist/huginn/refs/heads/main/huginn-rules.yml
created: '2026-03-27'
description: Huginn is an open-source system for building agents that perform automated tasks online. Self-hosted agents can monitor the web, send and receive events, and trigger workflows. Each Huginn instance exposes a JSON-based HTTP interface (the Web Requests API) that lets external systems trigger scenarios and post events into the platform.
finops:
- name: Huginn Finops
  service_category: API
  slug: huginn-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/huginn.png
layout: provider
modified: '2026-04-28'
name: Huginn
nav: Providers
network: true
overview: 'Huginn publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, Automation, Open Source, Self-Hosted, and Workflow Automation.


  Huginn''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Huginn Plans Pricing
  plan_count: 3
  slug: huginn-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 5
  name: Huginn Rate Limits
  slug: huginn-rate-limits
score:
  band: emerging
  composite: 13.9
  delta: -5.8
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 19.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/huginn/refs/heads/main/screenshots/huginn-2026-06-20T182927.png
slug: huginn
tags:
- Agents
- Automation
- Open Source
- Self-Hosted
- Workflow Automation
---
