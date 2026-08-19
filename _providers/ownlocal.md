---
access_model:
  confidence: medium
  label: Partner / contact required
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Partner-facing REST API (v1) for OwnLocal's automated print-to-digital advertising platform. Publishers and their systems create and list ads, upload the source print-ad PDF for conversion, create and
  name: OwnLocal API
  slug: ownlocal-api
artifact_total: 10
collections:
- collection_type: open
  name: OwnLocal API — Ads
  slug: open-ownlocal-ads
- collection_type: open
  name: OwnLocal API — Businesses
  slug: open-ownlocal-businesses
- collection_type: open
  name: OwnLocal API — Categories
  slug: open-ownlocal-categories
- collection_type: open
  name: OwnLocal API — Reports Data API
  slug: open-ownlocal-reports-data-api
common:
- group: company
  title: ''
  type: Website
  url: https://ownlocal.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.docs.ownlocal.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.docs.ownlocal.com/
- group: operate
  title: ''
  type: Support
  url: https://www.ownlocal.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.ownlocal.com/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OwnLocal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ownlocal.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ownlocal.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ownlocal-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ownlocal-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ownlocal-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ownlocal-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ownlocal-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ownlocal-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ownlocal-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ownlocal-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/ownlocal-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ownlocal-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ownlocal-domain-security.yml
created: '2026-07-17'
description: OwnLocal is an Austin, Texas based automated digital advertising platform for local media companies, founded in 2010 by Lloyd Armbrust and Jason Novek. It helps newspapers, local publishers and media companies power their digital services by automatically converting traditional print advertisements into online marketing campaigns — its AdForge and Origami products turn a submitted print ad PDF into a responsive digital ad unit, a business directory listing and an SEO/search presence, extending advertiser reach across search, social and display channels. OwnLocal publishes a partner-facing REST API (the OwnLocal API, v1) documented with Slate at api.docs.ownlocal.com and backed by a live Swagger 2.0 definition served from its own Swagger UI, covering ads, businesses, categories and performance reporting. API keys are issued by OwnLocal support rather than self-serve. OwnLocal was a 500 Global portfolio company and has acquired Whoosh Traffic, Sidengo, Inbound Press and Wanderful
  Media.
image: https://ucarecdn.com/0f20cb5b-5f4e-4207-be36-a5ee95dd54b5/ogimage1800optimized.png
layout: provider
mcp_servers:
- description: ''
  name: ownlocal-mcp.yml
  slug: ownlocal-mcpyml
modified: '2026-08-12'
name: OwnLocal
nav: Providers
network: true
overview: 'OwnLocal publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Local Media, Digital Advertising, and Marketing.


  OwnLocal''s developer surface includes documentation, API reference, support, authentication, and 16 more developer resources.'
plans:
- name: Ownlocal Plans Pricing
  plan_count: 0
  slug: ownlocal-plans-pricing
random_paper: 118
rate_limits:
- limit_count: 0
  name: Ownlocal Rate Limits
  slug: ownlocal-rate-limits
score:
  band: thin
  composite: 29.9
  delta: -0.5
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 16.7
    contract_quality: 35.2
    developer_ergonomics: 35.1
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 18.4
  previous_composite: 30.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ownlocal/refs/heads/main/screenshots/ownlocal-2026-08-07T191206.png
security:
- kind: authentication
  name: Ownlocal Authentication
  slug: ownlocal-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ownlocal Domain Security
  slug: ownlocal-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ownlocal
tags:
- Company
- Advertising
- Local Media
- Digital Advertising
- Marketing
- Newspapers
- AdTech
- Print to Digital
- Business Listings
- Local Business Data
- Ad Reporting
- Publishers
website: https://ownlocal.com
---
