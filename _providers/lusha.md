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
- acting_count: 18
  human_in_the_loop: 0
  name: Lusha Agentic Access
  operation_count: 32
  slug: lusha-agentic-access
  summary_line: 32 operations · 18 acting
api_count: 10
apis:
- description: Search and filter contacts/companies by job title, seniority, industry, geography, and other firmographic/persona filters.
  name: Lusha Prospecting API
  slug: prospecting
- description: Real-world signals (job changes, hiring, momentum) that affect outreach timing.
  name: Lusha Signals API
  slug: signals
- description: Discover similar accounts and buyers based on a seed list.
  name: Lusha Lookalike API
  slug: lookalike
- description: Account usage, credits, and webhook-secret administration
  name: Lusha Account API
  slug: lusha-account-api
- description: Reveal contact and company details from identifiers
  name: Lusha Enrichment API
  slug: lusha-enrichment-api
- description: Filter discovery endpoints for prospecting and signals
  name: Lusha Filters API
  slug: lusha-filters-api
- description: AI-powered similar contact and company recommendations
  name: Lusha Lookalike API
  slug: lusha-lookalike-api
- description: Filter-based contact and company search
  name: Lusha Prospecting API
  slug: lusha-prospecting-api
- description: Buying-intent and account signals
  name: Lusha Signals API
  slug: lusha-signals-api
- description: Signal-subscription webhook management
  name: Lusha Webhooks API
  slug: lusha-webhooks-api
artifact_total: 18
collections:
- collection_type: open
  name: Lusha API
  slug: open-lusha
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lusha-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lusha-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lusha-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lusha-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lusha-oss
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lushadata
- group: company
  title: ''
  type: Website
  url: https://www.lusha.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lusha.com/
- group: docs
  title: ''
  type: OpenAPI
  url: https://docs.lusha.com/apis/openapi
- group: commercial
  title: ''
  type: Plans
  url: plans/lusha-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lusha-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lusha-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.lusha.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.lusha.com/blog/
created: '2026-05-08'
description: Lusha is a B2B sales intelligence platform offering verified contact and company data. It exposes four REST APIs (Enrichment, Prospecting, Signals, Lookalike) plus an OpenAPI specification. Authentication is via API key generated in the dashboard.
finops:
- name: Lusha Finops
  service_category: Sales Intelligence
  slug: lusha-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lusha.png
layout: provider
modified: '2026-05-08'
name: Lusha
nav: Providers
network: true
overview: 'Lusha publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Enrichment API, Filters API, and 4 more. Tagged areas include Sales Intelligence, B2B, Enrichment, Contact Data, and Prospecting.


  Lusha''s developer surface includes authentication, engineering blog, and 12 more developer resources.'
plans:
- name: Lusha Plans Pricing
  plan_count: 3
  slug: lusha-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 2
  name: Lusha Rate Limits
  slug: lusha-rate-limits
score:
  band: thin
  composite: 36.4
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/screenshots/lusha-2026-06-20T184813.png
security:
- kind: authentication
  name: Lusha Authentication
  slug: lusha-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lusha Domain Security
  slug: lusha-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Lusha Vulnerability Disclosure
  slug: lusha-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lusha
tags:
- Sales Intelligence
- B2B
- Enrichment
- Contact Data
- Prospecting
- Intent
website: https://www.lusha.com/
---
