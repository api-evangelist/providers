---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST API for managing collection records and triggering push notifications inside an Adalo no-code app. Authentication uses a per-app Bearer API key generated from the app's API settings.
  name: Adalo API
  slug: api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adalo-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdaloHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adalohq
- group: company
  title: ''
  type: Website
  url: https://www.adalo.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.adalo.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adalo.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.adalo.com/signup
- group: company
  title: ''
  type: Blog
  url: https://www.adalo.com/blog
created: '2026-05-11'
description: Adalo is a visual no-code app builder that lets users design, build, and publish native iOS, Android, and web applications without writing code, combining a drag-and-drop canvas with AI-assisted generation and hosted Postgres-backed collections. The platform supports external data sources, pre-built feature templates, and 2,000+ integrations via Zapier and Make, hosting over a million apps. The Adalo API provides REST access to app collections and push notifications, secured with a per-app Bearer API key.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adalo.png
layout: provider
modified: '2026-05-11'
name: Adalo
nav: Providers
network: true
overview: 'Adalo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include No-Code, App Builder, Mobile App Development, Web App Development, and Low-Code.


  Adalo''s developer surface includes documentation, pricing, signup flow, engineering blog, and 4 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 14.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adalo/refs/heads/main/screenshots/adalo-2026-06-20T164515.png
security:
- kind: domain-security
  name: Adalo Domain Security
  slug: adalo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adalo
tags:
- No-Code
- App Builder
- Mobile App Development
- Web App Development
- Low-Code
- Visual Development
website: https://www.adalo.com
---
