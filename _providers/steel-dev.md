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
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Steel Dev Agentic Access
  operation_count: 17
  slug: steel-dev-agentic-access
  summary_line: 17 operations · 12 acting
api_count: 1
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
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Steel Files API
  slug: open-steel-dev-files-api
- collection_type: open
  name: Steel Files Quick Actions API
  slug: open-steel-dev-quick-actions-api
- collection_type: open
  name: Steel Files Session Actions API
  slug: open-steel-dev-session-actions-api
- collection_type: open
  name: Steel Files Sessions API
  slug: open-steel-dev-sessions-api
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
overview: 'Steel publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Files API, Quick Actions API, Session Actions API, and 1 more. Tagged areas include Browser, Web Automation, Scraping, AI Agents, and Open-Source.


  Steel''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Steel Dev Plans Pricing
  plan_count: 6
  slug: steel-dev-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Steel Dev Rate Limits
  slug: steel-dev-rate-limits
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 49.5
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- Open-Source
website: https://steel.dev
---
