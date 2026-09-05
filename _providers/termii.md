---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Termii Agentic Access
  operation_count: 24
  slug: termii-agentic-access
  summary_line: 24 operations · 16 acting
api_count: 1
apis:
- baseURL: https://api.ng.termii.com/api
  baseurl_source: declared
  description: Send, list, and manage SMS campaigns.
  name: Termii Campaigns API
  slug: termii-campaigns-api
- baseURL: https://api.ng.termii.com/api
  baseurl_source: declared
  description: Manage phonebooks and the contacts within them.
  name: Termii Contacts API
  slug: termii-contacts-api
- baseURL: https://api.ng.termii.com/api
  baseurl_source: declared
  description: Account balance, message history, and number status.
  name: Termii Insights API
  slug: termii-insights-api
- baseURL: https://api.ng.termii.com/api
  baseurl_source: declared
  description: Send single, bulk, and number-based messages.
  name: Termii Messaging API
  slug: termii-messaging-api
- baseURL: https://api.ng.termii.com/api
  baseurl_source: declared
  description: Fetch and request alphanumeric sender IDs.
  name: Termii Sender IDs API
  slug: termii-sender-ids-api
- baseURL: https://api.ng.termii.com/api
  baseurl_source: declared
  description: Generate, deliver, and verify one-time passwords.
  name: Termii Token API
  slug: termii-token-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Termii Campaigns API
  slug: open-termii-campaigns-api
- collection_type: open
  name: Termii Campaigns Contacts API
  slug: open-termii-contacts-api
- collection_type: open
  name: Termii Campaigns Insights API
  slug: open-termii-insights-api
- collection_type: open
  name: Termii Campaigns Messaging API
  slug: open-termii-messaging-api
- collection_type: open
  name: Termii Campaigns Sender IDs API
  slug: open-termii-sender-ids-api
- collection_type: open
  name: Termii Campaigns Token API
  slug: open-termii-token-api
- collection_type: open
  name: Termii API
  slug: open-termii
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/termii-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/termii-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/termii-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/termii
- group: company
  title: ''
  type: Website
  url: https://termii.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.termii.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/termii-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/termii-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/termii-finops.yml
created: '2026-06-20'
description: Termii is an African multichannel messaging platform whose REST API lets businesses send SMS, voice, WhatsApp, and email; generate and verify one-time passwords (OTP) for customer verification; manage sender IDs, campaigns, and contact phonebooks; and pull insights such as account balance, message reports, and number status. All requests authenticate with an api_key passed in the request body or query string.
finops:
- name: Termii Finops
  service_category: Communications and Messaging
  slug: termii-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/termii.png
layout: provider
modified: '2026-06-20'
name: Termii
nav: Providers
network: true
overview: 'Termii publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Contacts API, Insights API, and 3 more. Tagged areas include Messaging, SMS, OTP, WhatsApp, and Verification.


  Termii''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Termii Plans Pricing
  plan_count: 2
  slug: termii-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Termii Rate Limits
  slug: termii-rate-limits
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 55.7
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/termii/refs/heads/main/screenshots/termii-2026-06-20T195127.png
security:
- kind: authentication
  name: Termii Authentication
  slug: termii-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Termii Domain Security
  slug: termii-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: termii
tags:
- Messaging
- SMS
- OTP
- WhatsApp
- Verification
website: https://termii.com
---
