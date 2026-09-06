---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
- acting_count: 4
  human_in_the_loop: 0
  name: Gupshup Agentic Access
  operation_count: 6
  slug: gupshup-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- description: 'Broadcast SMS to a single number or many numbers programmatically via POST /msg on the /sm surface. Note - Gupshup has announced end-of-life for the /sm endpoints and recommends migrating SMS traffic '
  name: Gupshup SMS API
  slug: gupshup-sms-api
- description: Send RCS (Rich Communication Services) business messages - rich cards, carousels, suggested replies, and media. RCS is onboarding-gated (username / password issued by Gupshup) and served through the G
  name: Gupshup RCS API
  slug: gupshup-rcs-api
- description: Token-authenticated Partner surface (partner.gupshup.io) for BSPs and resellers - manage apps, templates, subscriptions/callbacks, and send messages through Meta-format passthrough endpoints (e.g. POS
  name: Gupshup Partner API
  slug: gupshup-partner-api
- baseURL: https://api.gupshup.io/wa/api/v1
  baseurl_source: declared
  description: Send WhatsApp session messages.
  name: Gupshup Messaging API
  slug: gupshup-messaging-api
- baseURL: https://api.gupshup.io/wa/api/v1
  baseurl_source: declared
  description: Manage user opt-in / opt-out and list interacted users.
  name: Gupshup Opt-In API
  slug: gupshup-opt-in-api
- baseURL: https://api.gupshup.io/wa/api/v1
  baseurl_source: declared
  description: Send and list WhatsApp template (HSM) messages.
  name: Gupshup Templates API
  slug: gupshup-templates-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gupshup WhatsApp Business Messaging API
  slug: open-gupshup-messaging-api
- collection_type: open
  name: Gupshup WhatsApp Business Messaging Opt-In API
  slug: open-gupshup-opt-in-api
- collection_type: open
  name: Gupshup WhatsApp Business Messaging Templates API
  slug: open-gupshup-templates-api
- collection_type: open
  name: Gupshup WhatsApp Business API
  slug: open-gupshup
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gupshup-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gupshup-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gupshup-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gupshup
- group: company
  title: ''
  type: Website
  url: https://www.gupshup.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gupshup.io
- group: commercial
  title: ''
  type: Plans
  url: plans/gupshup-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gupshup-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gupshup-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.gupshup.io/resources/blog
created: '2026-07-12'
description: Gupshup is a conversational messaging and CPaaS platform (headquartered in India) that lets businesses send and receive messages across WhatsApp, SMS, RCS, and other channels, plus build chatbots and conversational AI journeys. The developer platform exposes REST APIs on api.gupshup.io - most prominently the WhatsApp Business API (send session and template messages, opt-in management, templates, media, and inbound webhooks) - authenticated with an apikey header and scoped to a registered app. Separate SMS, RCS, and Partner API surfaces are also documented.
finops:
- name: Gupshup Finops
  service_category: Conversational Messaging and CPaaS
  slug: gupshup-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gupshup.png
layout: provider
modified: '2026-07-12'
name: Gupshup
nav: Providers
network: true
overview: 'Gupshup publishes 3 APIs on the [APIs.io](https://apis.io/) network: Messaging API, Opt-In API, and Templates API. Tagged areas include Messaging, WhatsApp, Conversational AI, CPaaS, and SMS.


  Gupshup''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Gupshup Plans Pricing
  plan_count: 4
  slug: gupshup-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Gupshup Rate Limits
  slug: gupshup-rate-limits
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 20.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gupshup/refs/heads/main/screenshots/gupshup-2026-07-25T220436.png
security:
- kind: authentication
  name: Gupshup Authentication
  slug: gupshup-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gupshup Domain Security
  slug: gupshup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gupshup
tags:
- Messaging
- WhatsApp
- Conversational AI
- CPaaS
- SMS
- RCS
- India
- Chatbots
- Business Messaging
- Communications
website: https://www.gupshup.io
---
