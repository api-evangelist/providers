---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 17
  human_in_the_loop: 2
  name: Notte Agentic Access
  operation_count: 33
  slug: notte-agentic-access
  summary_line: 33 operations · 17 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.notte.cc
  baseurl_source: declared
  description: Run autonomous web agents from natural-language tasks.
  name: Notte Agents API
  slug: notte-agents-api
- baseURL: https://api.notte.cc
  baseurl_source: declared
  description: Service health check.
  name: Notte Health API
  slug: notte-health-api
- baseURL: https://api.notte.cc
  baseurl_source: declared
  description: Perception layer - observe, step (execute), and scrape a live session page.
  name: Notte Page API
  slug: notte-page-api
- baseURL: https://api.notte.cc
  baseurl_source: declared
  description: Disposable digital identities with email, phone, and 2FA.
  name: Notte Personas API
  slug: notte-personas-api
- baseURL: https://api.notte.cc
  baseurl_source: declared
  description: One-shot scraping of a URL or raw HTML, plus AI web search.
  name: Notte Scraping API
  slug: notte-scraping-api
- baseURL: https://api.notte.cc
  baseurl_source: declared
  description: Create and manage remote cloud browser sessions.
  name: Notte Sessions API
  slug: notte-sessions-api
- baseURL: https://api.notte.cc
  baseurl_source: declared
  description: Secure credential and credit-card storage injected into runs.
  name: Notte Vaults API
  slug: notte-vaults-api
artifact_total: 22
collections:
- collection_type: open
  name: Notte Agents API
  slug: open-notte-agents-api
- collection_type: open
  name: Notte Agents Health API
  slug: open-notte-health-api
- collection_type: open
  name: Notte Agents Page API
  slug: open-notte-page-api
- collection_type: open
  name: Notte Agents Personas API
  slug: open-notte-personas-api
- collection_type: open
  name: Notte Agents Scraping API
  slug: open-notte-scraping-api
- collection_type: open
  name: Notte Agents Sessions API
  slug: open-notte-sessions-api
- collection_type: open
  name: Notte Agents Vaults API
  slug: open-notte-vaults-api
- collection_type: open
  name: Notte API
  slug: open-notte
common:
- group: other
  href: https://artifacts.apis.io/notte/capabilities/notte-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/notte-capability-edges.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.notte.cc/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.notte.cc/blog
- group: agent
  href: https://artifacts.apis.io/notte/agentic-access/notte-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/notte-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/notte/security/notte-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/notte-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/notte/authentication/notte-authentication.yml
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
  href: https://artifacts.apis.io/notte/plans/notte-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/notte-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/notte/rate-limits/notte-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/notte-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/notte/finops/notte-finops.yml
  title: ''
  type: FinOps
  url: finops/notte-finops.yml
created: '2026-06-20'
description: Notte is web browser and agent infrastructure for AI. The REST API at api.notte.cc provisions cloud browser sessions, runs autonomous web agents from natural-language tasks, observes and acts on pages, scrapes structured data, and manages personas, vaults, profiles, and serverless functions. The core framework is open source (SSPL-1.0) on GitHub under nottelabs.
finops:
- has_sources: true
  method: generated
  name: Notte Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: notte-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/notte.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.notte.cc over HTTP.
  name: Notte MCP Server
  slug: notte
modified: '2026-10-06'
name: Notte
nav: Providers
network: true
overview: 'Notte publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Health API, Page API, and 4 more. Tagged areas include Artificial Intelligence, Web Agents, Browser Automation, Sessions, and Web Scraping.


  Notte''s developer surface includes pricing, engineering blog, authentication, documentation, and 9 more developer resources.'
plans:
- name: Notte Plans Pricing
  plan_count: 8
  slug: notte-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Notte Rate Limits
  slug: notte-rate-limits
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 48.9
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/notte/notte-2026-06-20T190427.png
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
- Artificial Intelligence
- Web Agents
- Browser Automation
- Sessions
- Web Scraping
website: https://notte.cc
---
