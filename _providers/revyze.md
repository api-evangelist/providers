---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.revyze.fr
  baseurl_source: declared
  description: The Admin API from Revyze — 2 operation(s) for admin.
  name: Revyze Admin API
  slug: revyze-admin-api
- baseURL: https://api.revyze.fr
  baseurl_source: declared
  description: The Coach API from Revyze — 1 operation(s) for coach.
  name: Revyze Coach API
  slug: revyze-coach-api
- baseURL: https://api.revyze.fr
  baseurl_source: declared
  description: The FastAPI API from Revyze — 1 operation(s) for fastapi.
  name: Revyze FastAPI API
  slug: revyze-fastapi-api
- baseURL: https://api.revyze.fr
  baseurl_source: declared
  description: The Force Upgrade App API from Revyze — 1 operation(s) for force upgrade app.
  name: Revyze Force Upgrade App API
  slug: revyze-force-upgrade-app-api
- baseURL: https://api.revyze.fr
  baseurl_source: declared
  description: The Graphql3 API from Revyze — 1 operation(s) for graphql3.
  name: Revyze Graphql3 API
  slug: revyze-graphql3-api
- baseURL: https://api.revyze.fr
  baseurl_source: declared
  description: The Health API from Revyze — 1 operation(s) for health.
  name: Revyze Health API
  slug: revyze-health-api
- baseURL: https://api.revyze.fr
  baseurl_source: declared
  description: The Multiplayer API from Revyze — 1 operation(s) for multiplayer.
  name: Revyze Multiplayer API
  slug: revyze-multiplayer-api
- baseURL: https://api.revyze.fr
  baseurl_source: declared
  description: The Privacy Policy API from Revyze — 1 operation(s) for privacy policy.
  name: Revyze Privacy Policy API
  slug: revyze-privacy-policy-api
- baseURL: https://api.revyze.fr
  baseurl_source: declared
  description: The Privacy Policy En API from Revyze — 1 operation(s) for privacy policy en.
  name: Revyze Privacy Policy En API
  slug: revyze-privacy-policy-en-api
- baseURL: https://api.revyze.fr
  baseurl_source: declared
  description: The Webhook API from Revyze — 2 operation(s) for webhook.
  name: Revyze Webhook API
  slug: revyze-webhook-api
artifact_total: 24
asyncapis:
- description: ''
  name: Revyze Webhooks
  slug: revyze-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fast Admin API
  slug: open-revyze-admin-api
- collection_type: open
  name: Fast Admin Coach API
  slug: open-revyze-coach-api
- collection_type: open
  name: Fast Admin FastAPI API
  slug: open-revyze-fastapi-api
- collection_type: open
  name: Fast Admin Force Upgrade App API
  slug: open-revyze-force-upgrade-app-api
- collection_type: open
  name: Fast Admin Graphql3 API
  slug: open-revyze-graphql3-api
- collection_type: open
  name: Fast Admin Health API
  slug: open-revyze-health-api
- collection_type: open
  name: Fast Admin Multiplayer API
  slug: open-revyze-multiplayer-api
- collection_type: open
  name: Fast Admin Privacy Policy API
  slug: open-revyze-privacy-policy-api
- collection_type: open
  name: Fast Admin Privacy Policy En API
  slug: open-revyze-privacy-policy-en-api
- collection_type: open
  name: Fast Admin Webhook API
  slug: open-revyze-webhook-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.revyze.fr
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://api.revyze.fr/privacy_policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.revyze.fr/privacy_policy
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/revyze-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/revyze-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/revyze-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/revyze-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/revyze-conventions.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/revyze-openapi-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/revyze-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revyze-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/revyze-llms.txt
created: '2026-07-17'
description: Revyze is a French EdTech mobile learning application that helps secondary and baccalaureate-level students revise by scrolling short-form educational videos and playing quizzes created by a community of young content creators. The app covers all school subjects and is oriented around exam preparation for the French brevet and baccalaureate, reporting more than two million users, a 4.8/5 app-store rating, and 15,000+ videos, all offered free of charge. Revyze is a portfolio company of Speedinvest. This profile also captures the app's publicly reachable backend at api.revyze.fr — a FastAPI service that fronts a GraphQL API, an AI study-coach streaming endpoint, and subscription/content-moderation webhooks — discovered and harvested by the API Evangelist enrichment pipeline. It is the application's own backend rather than a documented public developer program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revyze.png
layout: provider
modified: '2026-07-20'
name: Revyze
nav: Providers
network: true
overview: 'Revyze publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Coach API, FastAPI API, and 7 more. Tagged areas include Company, EdTech, Education, Mobile, and Video.


  The Revyze catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Revyze''s developer surface includes authentication and 11 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 51.9
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 29.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 37.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/revyze/refs/heads/main/screenshots/revyze-2026-09-02T153738.png
security:
- kind: authentication
  name: Revyze Authentication
  slug: revyze-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Revyze Domain Security
  slug: revyze-domain-security
  summary_line: TLSv1.3 · HSTS
slug: revyze
tags:
- Company
- EdTech
- Education
- Mobile
- Video
- Learning
- Quiz
- France
- GraphQL
website: https://www.revyze.fr
---
