---
access_model:
  confidence: high
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Trainingpeaks Agentic Access
  operation_count: 49
  slug: trainingpeaks-agentic-access
  summary_line: 49 operations · 15 acting
api_count: 10
apis:
- description: Authenticated athlete profile and (deprecated) training zones.
  name: TrainingPeaks Athlete API
  slug: trainingpeaks-athlete-api
- description: Coach profile, athletes, and assistant management.
  name: TrainingPeaks Coach API
  slug: trainingpeaks-coach-api
- description: Athlete events.
  name: TrainingPeaks Events API
  slug: trainingpeaks-events-api
- description: Asynchronous activity file uploads.
  name: TrainingPeaks File API
  slug: trainingpeaks-file-api
- description: Service information and version.
  name: TrainingPeaks Info API
  slug: trainingpeaks-info-api
- description: Athlete wellness and body metrics.
  name: TrainingPeaks Metrics API
  slug: trainingpeaks-metrics-api
- description: Athlete nutrition log entries.
  name: TrainingPeaks Nutrition API
  slug: trainingpeaks-nutrition-api
- description: Athlete GPS routes.
  name: TrainingPeaks Routes API
  slug: trainingpeaks-routes-api
- description: Workout webhook subscriptions (Early Access).
  name: TrainingPeaks Webhooks API
  slug: trainingpeaks-webhooks-api
- description: Planned and completed workouts, changes, details, and analytics.
  name: TrainingPeaks Workouts API
  slug: trainingpeaks-workouts-api
artifact_total: 18
collections:
- collection_type: open
  name: TrainingPeaks Partners API
  slug: open-trainingpeaks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trainingpeaks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trainingpeaks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trainingpeaks-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/trainingpeaks-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TrainingPeaks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trainingpeaks
- group: company
  title: ''
  type: Website
  url: https://www.trainingpeaks.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/TrainingPeaks/PartnersAPI/wiki
- group: commercial
  title: ''
  type: Plans
  url: plans/trainingpeaks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trainingpeaks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/trainingpeaks-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.trainingpeaks.com/feed/
created: '2026-07-03'
description: TrainingPeaks is an endurance-athlete training platform for cyclists, runners, triathletes, and their coaches - used to plan structured workouts, track completed activities, analyze fitness with TSS/CTL/ATL and power/heart-rate/pace zones, log metrics, and manage coach-athlete relationships. The TrainingPeaks Partners API (Public API) is an OAuth 2.0, JSON/HTTPS REST API at api.trainingpeaks.com (sandbox at api.sandbox.trainingpeaks.com) that lets approved third parties read and write athlete profiles, planned and completed workouts, structured workout files, metrics, nutrition, events, routes, and coach data on behalf of a user. API access is partner-gated - developers must apply for credentials and are not accepting requests for personal use - but the API surface is publicly documented on the PartnersAPI GitHub wiki.
finops:
- name: Trainingpeaks Finops
  service_category: Fitness and Endurance Training
  slug: trainingpeaks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trainingpeaks.png
layout: provider
modified: '2026-07-03'
name: TrainingPeaks
nav: Providers
network: true
overview: 'TrainingPeaks publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Athlete API, Coach API, Events API, and 7 more. Tagged areas include Fitness, Endurance Training, Workouts, Coaching, and Sports.


  TrainingPeaks'' developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Trainingpeaks Plans Pricing
  plan_count: 6
  slug: trainingpeaks-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 4
  name: Trainingpeaks Rate Limits
  slug: trainingpeaks-rate-limits
scopes:
- name: Trainingpeaks Scopes
  scope_count: 17
  slug: trainingpeaks-scopes
  summary_line: 17 scopes · authorizationCode
score:
  band: thin
  composite: 39.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 36.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Trainingpeaks Authentication
  slug: trainingpeaks-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Trainingpeaks Domain Security
  slug: trainingpeaks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trainingpeaks
tags:
- Fitness
- Endurance Training
- Workouts
- Coaching
- Sports
- Health
- Wearables
website: https://www.trainingpeaks.com
---
