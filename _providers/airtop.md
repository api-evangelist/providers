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
- acting_count: 14
  human_in_the_loop: 1
  name: Airtop Agentic Access
  operation_count: 20
  slug: airtop-agentic-access
  summary_line: 20 operations · 14 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: Query, extract, and scrape page content with AI.
  name: Airtop AI Query API
  slug: airtop-ai-query-api
- description: Drive a page with natural-language click, type, hover, and scroll.
  name: Airtop Page Interaction API
  slug: airtop-page-interaction-api
- description: Persist and delete browser profiles.
  name: Airtop Profiles API
  slug: airtop-profiles-api
- description: Capture window screenshots.
  name: Airtop Screenshots API
  slug: airtop-screenshots-api
- description: Create and manage cloud browser sessions.
  name: Airtop Sessions API
  slug: airtop-sessions-api
- description: Create, navigate, and close browser windows inside a session.
  name: Airtop Windows API
  slug: airtop-windows-api
artifact_total: 13
collections:
- collection_type: open
  name: Airtop API
  slug: open-airtop
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airtop-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airtop-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airtop-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.airtop.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/airtop-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airtop-ai
- group: company
  title: ''
  type: Website
  url: https://www.airtop.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.airtop.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/airtop-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/airtop-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/airtop-finops.yml
created: '2026-06-20'
description: Airtop is a cloud-browser API for AI agents. It runs remote Chromium sessions in the cloud and exposes them through a REST API so agents can open windows, navigate pages, and interact with sites using natural-language instructions - clicking, typing, scraping, and querying pages with AI - without brittle selectors or self-hosted browser infrastructure.
finops:
- name: Airtop Finops
  service_category: Web and Application Services
  slug: airtop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airtop.png
layout: provider
modified: '2026-06-20'
name: Airtop
nav: Providers
network: true
overview: 'Airtop publishes 6 APIs on the [APIs.io](https://apis.io/) network, including AI Query API, Page Interaction API, Profiles API, and 3 more. Tagged areas include Browser Automation, AI Agents, Cloud Browser, Web Scraping, and Headless Chrome.


  Airtop''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Airtop Plans Pricing
  plan_count: 5
  slug: airtop-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Airtop Rate Limits
  slug: airtop-rate-limits
score:
  band: thin
  composite: 38.6
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airtop/refs/heads/main/screenshots/airtop-2026-06-20T171435.png
security:
- kind: authentication
  name: Airtop Authentication
  slug: airtop-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Airtop Domain Security
  slug: airtop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: airtop
tags:
- Browser Automation
- AI Agents
- Cloud Browser
- Web Scraping
- Headless Chrome
website: https://www.airtop.ai
---
