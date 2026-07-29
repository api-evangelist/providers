---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Steel Dev Agentic Access
  operation_count: 17
  slug: steel-dev-agentic-access
  summary_line: 17 operations · 12 acting
api_count: 4
apis:
- description: Manage files inside a session's browser context.
  name: Steel Files API
  slug: steel-dev-files-api
- description: Stateless one-off scrape, screenshot, PDF, and search.
  name: Steel Quick Actions API
  slug: steel-dev-quick-actions-api
- description: Scrape, screenshot, and PDF the page in a running session.
  name: Steel Session Actions API
  slug: steel-dev-session-actions-api
- description: Launch, inspect, and release cloud browser sessions.
  name: Steel Sessions API
  slug: steel-dev-sessions-api
artifact_total: 11
collections:
- collection_type: open
  name: Steel API
  slug: open-steel-dev
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/steel-dev-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/steel-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/steel-dev-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/steel-dev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/steel-dev
- group: company
  title: ''
  type: Website
  url: https://steel.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.steel.dev
- group: commercial
  title: ''
  type: Plans
  url: plans/steel-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/steel-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/steel-dev-finops.yml
created: '2026-06-20'
description: Steel is the open-source browser API for AI agents and apps. The Steel Cloud REST API (https://api.steel.dev/v1) launches and manages cloud browser sessions, runs stateless quick actions (scrape, screenshot, pdf, search), and exposes a live session viewer, while long-running automation connects to a per-session Chrome DevTools Protocol (CDP) WebSocket driven with Playwright, Puppeteer, or Selenium. The same surface ships self-hosted under Apache-2.0 as steel-browser.
finops:
- name: Steel Dev Finops
  service_category: Web Automation and Browser Infrastructure
  slug: steel-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/steel-dev.png
layout: provider
modified: '2026-06-20'
name: Steel
nav: Providers
network: true
overview: 'Steel publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Files API, Quick Actions API, Session Actions API, and 1 more. Tagged areas include Browser, Web Automation, Scraping, AI Agents, and Open Source.


  Steel''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Steel Dev Plans Pricing
  plan_count: 6
  slug: steel-dev-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Steel Dev Rate Limits
  slug: steel-dev-rate-limits
score:
  band: thin
  composite: 36.6
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Steel Dev Authentication
  slug: steel-dev-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Steel Dev Domain Security
  slug: steel-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: steel-dev
tags:
- Browser
- Web Automation
- Scraping
- AI Agents
- Open Source
website: https://steel.dev
---
