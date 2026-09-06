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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Airtop Agentic Access
  operation_count: 20
  slug: airtop-agentic-access
  summary_line: 20 operations · 14 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: Query, extract, and scrape page content with AI.
  name: Airtop AI Query API
  slug: airtop-ai-query-api
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: Drive a page with natural-language click, type, hover, and scroll.
  name: Airtop Page Interaction API
  slug: airtop-page-interaction-api
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: Persist and delete browser profiles.
  name: Airtop Profiles API
  slug: airtop-profiles-api
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: Capture window screenshots.
  name: Airtop Screenshots API
  slug: airtop-screenshots-api
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: Create and manage cloud browser sessions.
  name: Airtop Sessions API
  slug: airtop-sessions-api
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: Create, navigate, and close browser windows inside a session.
  name: Airtop Windows API
  slug: airtop-windows-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Airtop AI Query API
  slug: open-airtop-ai-query-api
- collection_type: open
  name: Airtop AI Query Page Interaction API
  slug: open-airtop-page-interaction-api
- collection_type: open
  name: Airtop AI Query Profiles API
  slug: open-airtop-profiles-api
- collection_type: open
  name: Airtop AI Query Screenshots API
  slug: open-airtop-screenshots-api
- collection_type: open
  name: Airtop AI Query Sessions API
  slug: open-airtop-sessions-api
- collection_type: open
  name: Airtop AI Query Windows API
  slug: open-airtop-windows-api
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
random_paper: 4
rate_limits:
- limit_count: 4
  name: Airtop Rate Limits
  slug: airtop-rate-limits
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.4
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
