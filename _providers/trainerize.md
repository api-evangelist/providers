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
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Trainerize Agentic Access
  operation_count: 19
  slug: trainerize-agentic-access
  summary_line: 19 operations · 19 acting
api_count: 1
apis:
- baseURL: https://api.trainerize.com/v03
  baseurl_source: declared
  description: Retrieve and modify client goals, habits, body stats, nutrition, and appointments.
  name: ABC Trainerize Client Data API
  slug: trainerize-client-data-api
- baseURL: https://api.trainerize.com/v03
  baseurl_source: declared
  description: Create, update, find, and manage clients, trainer assignment, tags, and groups.
  name: ABC Trainerize Clients API
  slug: trainerize-clients-api
- baseURL: https://api.trainerize.com/v03
  baseurl_source: declared
  description: Send in-app messages and upload attachments / meal-plan PDFs to clients.
  name: ABC Trainerize Messaging API
  slug: trainerize-messaging-api
- baseURL: https://api.trainerize.com/v03
  baseurl_source: declared
  description: Assign programs and workouts to clients - copy master programs, subscribe to main/add-on programs, and add training phases.
  name: ABC Trainerize Training API
  slug: trainerize-training-api
- baseURL: https://api.trainerize.com/v03
  baseurl_source: declared
  description: Register and manage webhook subscriptions for ABC Trainerize business events.
  name: ABC Trainerize Webhooks API
  slug: trainerize-webhooks-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ABC Trainerize Client Data API
  slug: open-trainerize-client-data-api
- collection_type: open
  name: ABC Trainerize Client Data Clients API
  slug: open-trainerize-clients-api
- collection_type: open
  name: ABC Trainerize Client Data Messaging API
  slug: open-trainerize-messaging-api
- collection_type: open
  name: ABC Trainerize Client Data Training API
  slug: open-trainerize-training-api
- collection_type: open
  name: ABC Trainerize Client Data Webhooks API
  slug: open-trainerize-webhooks-api
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
random_paper: 14
rate_limits:
- limit_count: 3
  name: Trainerize Rate Limits
  slug: trainerize-rate-limits
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 45.0
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trainerize/refs/heads/main/screenshots/trainerize-2026-09-02T164110.png
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
- Software-as-a-Service
website: https://www.trainerize.com
---
