---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
- acting_count: 19
  human_in_the_loop: 0
  name: Trainerize Agentic Access
  operation_count: 19
  slug: trainerize-agentic-access
  summary_line: 19 operations · 19 acting
api_count: 5
apis:
- description: Retrieve and modify client goals, habits, body stats, nutrition, and appointments.
  name: ABC Trainerize Client Data API
  slug: trainerize-client-data-api
- description: Create, update, find, and manage clients, trainer assignment, tags, and groups.
  name: ABC Trainerize Clients API
  slug: trainerize-clients-api
- description: Send in-app messages and upload attachments / meal-plan PDFs to clients.
  name: ABC Trainerize Messaging API
  slug: trainerize-messaging-api
- description: Assign programs and workouts to clients - copy master programs, subscribe to main/add-on programs, and add training phases.
  name: ABC Trainerize Training API
  slug: trainerize-training-api
- description: Register and manage webhook subscriptions for ABC Trainerize business events.
  name: ABC Trainerize Webhooks API
  slug: trainerize-webhooks-api
artifact_total: 12
collections:
- collection_type: open
  name: ABC Trainerize API
  slug: open-trainerize
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trainerize-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trainerize-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trainerize-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trainerize
- group: company
  title: ''
  type: Website
  url: https://www.trainerize.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.trainerize.com/hc/en-us/articles/37082084919060-Using-API-and-Webhooks-With-ABC-Trainerize
- group: commercial
  title: ''
  type: Plans
  url: plans/trainerize-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trainerize-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/trainerize-finops.yml
created: '2026-07-12'
description: ABC Trainerize is a personal-training and fitness-coaching software platform for trainers, studios, and gyms - online training, workout programming, nutrition and meal planning, habit and goal tracking, in-app messaging, and a custom-branded client app. Its partner API (Studio and Enterprise plans) lets integrators add, modify, and retrieve client data - clients, programs and workouts, goals, habits, body stats, nutrition, appointments, tags, and groups - and register webhooks for business events. ABC Trainerize is a product of ABC Fitness Solutions, which acquired Trainerize in 2021.
finops:
- name: Trainerize Finops
  service_category: Fitness and Coaching Software (SaaS)
  slug: trainerize-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trainerize.png
layout: provider
modified: '2026-07-12'
name: ABC Trainerize
nav: Providers
network: true
overview: 'ABC Trainerize publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Client Data API, Clients API, Messaging API, and 2 more. Tagged areas include Fitness, Personal Training, Coaching, Fitness Software, and Client Management.


  ABC Trainerize''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Trainerize Plans Pricing
  plan_count: 4
  slug: trainerize-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 3
  name: Trainerize Rate Limits
  slug: trainerize-rate-limits
score:
  band: thin
  composite: 39.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Trainerize Authentication
  slug: trainerize-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Trainerize Domain Security
  slug: trainerize-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trainerize
tags:
- Fitness
- Personal Training
- Coaching
- Fitness Software
- Client Management
- SaaS
website: https://www.trainerize.com
---
