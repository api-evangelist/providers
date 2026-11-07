---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Airtop Agentic Access
  operation_count: 20
  slug: airtop-agentic-access
  summary_line: 20 operations · 12 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: Persist and delete browser profiles.
  name: Airtop Profiles API
  slug: airtop-profiles-api
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
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: The Agent Director API from Airtop — 1 operation(s) for agent director.
  name: Airtop Agent Director API
  slug: airtop-agent-director-api
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: The Agent Folders API from Airtop — 3 operation(s) for agent folders.
  name: Airtop Agent Folders API
  slug: airtop-agent-folders-api
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: The Agents API from Airtop — 61 operation(s) for agents.
  name: Airtop Agents API
  slug: airtop-agents-api
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: The Automations API from Airtop — 3 operation(s) for automations.
  name: Airtop Automations API
  slug: airtop-automations-api
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: The beta API from Airtop — 2 operation(s) for beta.
  name: Airtop Beta API
  slug: airtop-beta-api
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: The files API from Airtop — 3 operation(s) for files.
  name: Airtop Files API
  slug: airtop-files-api
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: The GTM Engineer API from Airtop — 21 operation(s) for gtm engineer.
  name: Airtop GTM Engineer API
  slug: airtop-gtm-engineer-api
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: The Knowledge Base API from Airtop — 9 operation(s) for knowledge base.
  name: Airtop Knowledge Base API
  slug: airtop-knowledge-base-api
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: The Requests API from Airtop — 2 operation(s) for requests.
  name: Airtop Requests API
  slug: airtop-requests-api
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: The Sensitive Values API from Airtop — 3 operation(s) for sensitive values.
  name: Airtop Sensitive Values API
  slug: airtop-sensitive-values-api
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: The Services API from Airtop — 6 operation(s) for services.
  name: Airtop Services API
  slug: airtop-services-api
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: The Team Vault API from Airtop — 4 operation(s) for team vault.
  name: Airtop Team Vault API
  slug: airtop-team-vault-api
- baseURL: https://api.airtop.ai/api/v1
  baseurl_source: declared
  description: The Templates API from Airtop — 1 operation(s) for templates.
  name: Airtop Templates API
  slug: airtop-templates-api
artifact_total: 30
collections:
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
  href: https://artifacts.apis.io/airtop/agentic-access/airtop-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/airtop-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/airtop/security/airtop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airtop-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/airtop/authentication/airtop-authentication.yml
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
  href: https://artifacts.apis.io/airtop/plans/airtop-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/airtop-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/airtop/rate-limits/airtop-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/airtop-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/airtop/finops/airtop-finops.yml
  title: ''
  type: FinOps
  url: finops/airtop-finops.yml
created: '2026-06-20'
description: Airtop is a cloud-browser API for AI agents. It runs remote Chromium sessions in the cloud and exposes them through a REST API so agents can open windows, navigate pages, and interact with sites using natural-language instructions - clicking, typing, scraping, and querying pages with AI - without brittle selectors or self-hosted browser infrastructure.
finops:
- has_sources: true
  method: generated
  name: Airtop Finops
  primary_unit: ''
  service_category: Web and Application Services
  slug: airtop-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airtop.png
layout: provider
modified: '2026-06-20'
name: Airtop
nav: Providers
network: true
overview: 'Airtop publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Profiles API, Sessions API, Windows API, and 13 more. Tagged areas include Browser Automation, AI Agents, Cloud Browser, Web Scraping, and Headless Chrome.


  The Airtop catalog on APIs.io includes 1 Spectral governance ruleset.


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
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Airtop API Rules
  rule_count: 51
  severity_counts:
    error: 35
    hint: 0
    info: 2
    warn: 14
  slug: airtop-rules
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 54.7
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 29.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 69.6
      total: 23
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/airtop/airtop-2026-06-20T171435.png
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
