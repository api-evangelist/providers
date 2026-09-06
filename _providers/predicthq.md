---
access_model:
  confidence: medium
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
- acting_count: 1
  human_in_the_loop: 0
  name: Predicthq Agentic Access
  operation_count: 5
  slug: predicthq-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 4
apis:
- baseURL: https://api.predicthq.com/v1
  baseurl_source: spec
  description: The Events API from PredictHQ — 2 operation(s) for events.
  name: PredictHQ Events API
  slug: predicthq-events-api
- baseURL: https://api.predicthq.com/v1
  baseurl_source: spec
  description: The Features API from PredictHQ — 1 operation(s) for features.
  name: PredictHQ Features API
  slug: predicthq-features-api
- baseURL: https://api.predicthq.com/v1
  baseurl_source: spec
  description: The Places API from PredictHQ — 1 operation(s) for places.
  name: PredictHQ Places API
  slug: predicthq-places-api
- baseURL: https://api.predicthq.com/v1
  baseurl_source: spec
  description: The Suggested Radius API from PredictHQ — 1 operation(s) for suggested radius.
  name: PredictHQ Suggested Radius API
  slug: predicthq-suggested-radius-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PredictHQ Events API
  slug: open-predicthq-events-api
- collection_type: open
  name: PredictHQ Events Features API
  slug: open-predicthq-features-api
- collection_type: open
  name: PredictHQ Events Places API
  slug: open-predicthq-places-api
- collection_type: open
  name: PredictHQ Events Suggested Radius API
  slug: open-predicthq-suggested-radius-api
- collection_type: open
  name: PredictHQ API
  slug: open-predicthq
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/predicthq-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/predicthq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/predicthq-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/predicthq
- group: start
  title: ''
  type: Portal
  url: https://www.predicthq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.predicthq.com/
- group: start
  title: ''
  type: Signup
  url: https://control.predicthq.com/signup
- group: start
  title: ''
  type: Login
  url: https://control.predicthq.com/signin
- group: commercial
  title: ''
  type: Pricing
  url: https://www.predicthq.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.predicthq.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.predicthq.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.predicthq.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.predicthq.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.predicthq.com/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.predicthq.com/legal/data-security-and-availability
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/predicthq
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.predicthq.com/llms.txt
created: '2025-02-24'
description: PredictHQ is an AI-powered demand intelligence platform that predicts the impact of real-world events on business demand. The PredictHQ API delivers structured, deduplicated event data, machine learning features, demand forecasts, and impact analytics across categories such as concerts, sports, conferences, public holidays, school terms, severe weather, and more, helping enterprises make smarter decisions about staffing, inventory, pricing, and marketing.
finops:
- name: Predicthq Finops
  service_category: API
  slug: predicthq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/predicthq.png
layout: provider
modified: '2026-05-19'
name: PredictHQ
nav: Providers
network: true
overview: 'PredictHQ publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Events API, Features API, Places API, and 1 more. Tagged areas include Demand Intelligence, Event, Forecasting, Machine-Learning, and Real-World Events.


  PredictHQ''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, support, and 10 more developer resources.'
plans:
- name: Predicthq Plans Pricing
  plan_count: 3
  slug: predicthq-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Predicthq Rate Limits
  slug: predicthq-rate-limits
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 48.8
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 40.6
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
screenshot: https://raw.githubusercontent.com/api-evangelist/predicthq/refs/heads/main/screenshots/predicthq-2026-06-20T192049.png
security:
- kind: authentication
  name: Predicthq Authentication
  slug: predicthq-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Predicthq Domain Security
  slug: predicthq-domain-security
  summary_line: TLSv1.3 · DMARC
slug: predicthq
tags:
- Demand Intelligence
- Event
- Forecasting
- Machine-Learning
- Real-World Events
website: https://www.predicthq.com/
---
