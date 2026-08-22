---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/storagepug-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.storagepug.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/storagepug
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.storagepug.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://www.storagepug.com/blog/tag/api-integration
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/storagepug
- group: commercial
  title: ''
  type: Plans
  url: plans/storagepug-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.storagepug.com/blog/rss.xml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/storagepug-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/storagepug-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.storagepug.com/partnership
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.storagepug.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.storagepug.com/privacy
- group: start
  title: ''
  type: Login
  url: https://app.storagepug.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.storagepug.com/contact
- group: company
  title: ''
  type: About
  url: https://www.storagepug.com/about
coverage:
  checked: '2026-08-14'
  detail: StoragePug sells self-storage websites and the Insights dashboard as an end-user product only - the live backend at api.storagepug.com answers every path with a custom application 404 and serves no spec, no /.well-known/ document and no docs, and the whole 130-article help center indexed by its own llms.txt is operator-facing with no developer or API section.
  evidence:
  - status: 404
    url: https://api.storagepug.com/openapi.json
  - status: 404
    url: https://api.storagepug.com/graphql
  - status: 404
    url: https://www.storagepug.com/developers
  - status: 404
    url: https://www.storagepug.com/.well-known/agent-card.json
  - status: 200
    url: https://help.storagepug.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-07-03'
description: 'StoragePug builds marketing websites, online rental/reservation flows, and lead-management dashboards for self-storage facility operators. StoragePug has no public, self-service developer portal, no published REST/GraphQL API reference, and no OpenAPI specification of its own. Its documented programmatic surface runs the other direction: StoragePug is a licensed integration partner that consumes property-management-system APIs - primarily SiteLink''s API, with additional PMS partners such as CallPotential and OpenTech Alliance/StorageTreasures - to pull unit rates, availability, and tenant data into the facility websites it builds, and to push back online rentals, reservations, and payments. No webhook system, API key management screen, or Zapier app for StoragePug itself was found. Contract discovery on 2026-08-14 did find a live first-party backend host, api.storagepug.com, which serves the Insights dashboard at app.storagepug.com; it is undocumented, publishes no OpenAPI,
  GraphQL, MCP or /.well-known/ document, and is not offered to third-party developers. This entry is documented as a stub because there is no public API to catalog.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/storagepug.png
layout: provider
modified: '2026-08-14'
name: StoragePug
nav: Providers
network: true
overview: 'StoragePug is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Self Storage, Marketing Websites, Lead Generation, Property Management Software, and SiteLink Integration.


  StoragePug''s developer surface includes documentation, engineering blog, pricing, support, and 12 more developer resources.'
plans:
- name: Storagepug Plans Pricing
  plan_count: 4
  slug: storagepug-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Storagepug Rate Limits
  slug: storagepug-rate-limits
score:
  band: emerging
  composite: 23.4
  delta: -1.3
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 24.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Storagepug Domain Security
  slug: storagepug-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: storagepug
tags:
- Self Storage
- Marketing Websites
- Lead Generation
- Property Management Software
- SiteLink Integration
- No Public API
website: https://www.storagepug.com
---
