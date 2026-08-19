---
access_model:
  confidence: medium
  label: Self-serve signup, free tier
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - https://www.optimyzee.com/pricing
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.9
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The REST API behind the Optimyzee web application. Covers Google Ads campaign creation (search creation, AI search creation, keyword planner, RSA builder, sitelink builder), analysis (account audit, a
  name: Optimyzee Application API
  slug: optimyzee-application-api
artifact_total: 6
collections:
- collection_type: open
  name: Optimyzee Application API
  slug: open-optimyzee
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optimyzee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://optimyzee.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.optimyzee.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.optimyzee.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.optimyzee.com/auth/register
- group: start
  title: ''
  type: Login
  url: https://app.optimyzee.com/auth
- group: operate
  title: ''
  type: Support
  url: https://www.optimyzee.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.optimyzee.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.optimyzee.com/policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/optimyzee
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/optimyzee-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/optimyzee-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/optimyzee-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/optimyzee-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/optimyzee-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/optimyzee-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/optimyzee-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/optimyzee-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/optimyzee-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/optimyzee-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Optimyzee is an AI-powered ad management platform that structures and optimizes Google Ads search campaigns in minutes, acting like a senior PPC specialist. It analyzes a website and its keywords to generate an optimized campaign structure, keyword plans, and responsive search ad copy, then validates ads against Google Ads standards in real time to improve click-through rate, conversion rate, and Quality Score while lowering cost-per-click. Beyond Google Ads it links Meta and Yelp Ads accounts and Google Merchant Center, runs account audits and health scoring, cleans wasted search terms, builds Performance Max, RSA and sitelink assets, and automates recurring optimization tasks. It targets business owners, marketing agencies, and individual marketers, and is backed by 500 Global and Triple S Ventures. The web application is driven by a REST API at api.optimyzee.com whose OpenAPI 3.0 description is served publicly and anonymously at /docs (184 operations across 151 paths), though
  Optimyzee publishes no developer portal, API reference, SDK, or public API program around it.
image: https://optimyzee.com/og-image.png
layout: provider
modified: '2026-08-12'
name: Optimyzee
nav: Providers
network: true
overview: 'Optimyzee publishes 1 API on the [APIs.io](https://apis.io/) network: Application API. Tagged areas include Company, Advertising, Google Ads, PPC, and Marketing.


  Optimyzee''s developer surface includes pricing, engineering blog, signup flow, support, authentication, and 16 more developer resources.'
plans:
- name: Optimyzee Plans Pricing
  plan_count: 3
  slug: optimyzee-plans-pricing
random_paper: 104
rate_limits:
- limit_count: 0
  name: Optimyzee Rate Limits
  slug: optimyzee-rate-limits
score:
  band: developing
  composite: 41.4
  delta: -1.9
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 16.7
    contract_quality: 49.0
    developer_ergonomics: 20.8
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 43.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/optimyzee/refs/heads/main/screenshots/optimyzee-2026-08-07T190810.png
security:
- kind: authentication
  name: Optimyzee Authentication
  slug: optimyzee-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Optimyzee Domain Security
  slug: optimyzee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: optimyzee
tags:
- Company
- Advertising
- Google Ads
- PPC
- Marketing
- Automation
- Artificial Intelligence
- SaaS
- Campaign Management
- Search Advertising
- Yelp Ads
- Meta Ads
- Keyword Research
- Reporting
website: https://optimyzee.com
---
