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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 18
  human_in_the_loop: 2
  name: Notte Agentic Access
  operation_count: 33
  slug: notte-agentic-access
  summary_line: 33 operations · 18 acting · 2 human-in-the-loop
api_count: 7
apis:
- description: Run autonomous web agents from natural-language tasks.
  name: Notte Agents API
  slug: notte-agents-api
- description: Service health check.
  name: Notte Health API
  slug: notte-health-api
- description: Perception layer - observe, step (execute), and scrape a live session page.
  name: Notte Page API
  slug: notte-page-api
- description: Disposable digital identities with email, phone, and 2FA.
  name: Notte Personas API
  slug: notte-personas-api
- description: One-shot scraping of a URL or raw HTML, plus AI web search.
  name: Notte Scraping API
  slug: notte-scraping-api
- description: Create and manage remote cloud browser sessions.
  name: Notte Sessions API
  slug: notte-sessions-api
- description: Secure credential and credit-card storage injected into runs.
  name: Notte Vaults API
  slug: notte-vaults-api
artifact_total: 14
collections:
- collection_type: open
  name: Notte API
  slug: open-notte
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/notte-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/notte-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/notte-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nottelabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nottelabs
- group: company
  title: ''
  type: Website
  url: https://notte.cc
- group: docs
  title: ''
  type: Documentation
  url: https://docs.notte.cc
- group: commercial
  title: ''
  type: Plans
  url: plans/notte-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/notte-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/notte-finops.yml
created: '2026-06-20'
description: Notte is web browser and agent infrastructure for AI. The REST API at api.notte.cc provisions cloud browser sessions, runs autonomous web agents from natural-language tasks, observes and acts on pages, scrapes structured data, and manages personas, vaults, profiles, and serverless functions. The core framework is open source (SSPL-1.0) on GitHub under nottelabs.
finops:
- name: Notte Finops
  service_category: AI and Machine Learning
  slug: notte-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/notte.png
layout: provider
modified: '2026-06-20'
name: Notte
nav: Providers
network: true
overview: 'Notte publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Health API, Page API, and 4 more. Tagged areas include AI, Web Agents, Browser Automation, Sessions, and Scraping.


  Notte''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Notte Plans Pricing
  plan_count: 5
  slug: notte-plans-pricing
random_paper: 90
rate_limits:
- limit_count: 6
  name: Notte Rate Limits
  slug: notte-rate-limits
score:
  band: thin
  composite: 39.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/notte/refs/heads/main/screenshots/notte-2026-06-20T190427.png
security:
- kind: authentication
  name: Notte Authentication
  slug: notte-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Notte Domain Security
  slug: notte-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: notte
tags:
- AI
- Web Agents
- Browser Automation
- Sessions
- Scraping
website: https://notte.cc
---
