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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Churnkey Agentic Access
  operation_count: 9
  slug: churnkey-agentic-access
  summary_line: 9 operations · 7 acting
api_count: 1
apis:
- description: Client-side embed surface for personalized Cancel Flows. The JavaScript SDK is initialized with window.churnkey.init(), passing an appId, customerId, subscriptionId, provider, and a server-computed HM
  name: Churnkey Cancel Flow Embed
  slug: churnkey-cancel-flow-embed
- description: Reactivation (win-back) campaigns that re-engage churned or paused customers with targeted offers. Reactivations are a documented Churnkey product, but a dedicated public REST endpoint set is not publ
  name: Churnkey Reactivation API
  slug: churnkey-reactivation-api
- baseURL: https://api.churnkey.co/v1/data
  baseurl_source: declared
  description: Billing-contact management for Failed Payment Recovery.
  name: Churnkey Billing Contacts API
  slug: churnkey-billing-contacts-api
- baseURL: https://api.churnkey.co/v1/data
  baseurl_source: declared
  description: Customer and B2B user attribute updates.
  name: Churnkey Customers API
  slug: churnkey-customers-api
- baseURL: https://api.churnkey.co/v1/data
  baseurl_source: declared
  description: GDPR access and deletion requests (Data API).
  name: Churnkey Data Subject Requests API
  slug: churnkey-data-subject-requests-api
- baseURL: https://api.churnkey.co/v1/data
  baseurl_source: declared
  description: Customer event tracking and passive data enrichment.
  name: Churnkey Events API
  slug: churnkey-events-api
- baseURL: https://api.churnkey.co/v1/data
  baseurl_source: declared
  description: Cancel Flow session data and aggregations (Data API).
  name: Churnkey Sessions API
  slug: churnkey-sessions-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Churnkey Billing Contacts API
  slug: open-churnkey-billing-contacts-api
- collection_type: open
  name: Churnkey Billing Contacts Customers API
  slug: open-churnkey-customers-api
- collection_type: open
  name: Churnkey Billing Contacts Data Subject Requests API
  slug: open-churnkey-data-subject-requests-api
- collection_type: open
  name: Churnkey Billing Contacts Events API
  slug: open-churnkey-events-api
- collection_type: open
  name: Churnkey Billing Contacts Sessions API
  slug: open-churnkey-sessions-api
- collection_type: open
  name: Churnkey API
  slug: open-churnkey
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/churnkey-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/churnkey-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/churnkey-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/churnkey-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/churnkey
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/churnkey
- group: company
  title: ''
  type: Website
  url: https://churnkey.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.churnkey.co
- group: commercial
  title: ''
  type: Plans
  url: plans/churnkey-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/churnkey-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/churnkey-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://churnkey.co/pricing
created: '2026-07-10'
description: Churnkey is retention and growth infrastructure for subscription companies. It provides personalized Cancel Flows that intercept subscription cancellations with pauses, discounts, plan changes and surveys; Failed Payment Recovery (dunning) that recovers involuntary churn; and Reactivation campaigns that win back churned customers. Churnkey embeds via a JavaScript SDK authenticated with a server-computed HMAC authHash, and exposes REST APIs for session/analytics data, event tracking, customer updates, billing-contact management, and GDPR data-subject requests, plus signed webhooks. It integrates with Stripe, Chargebee, Paddle, Braintree, and Maxio.
finops:
- name: Churnkey Finops
  service_category: Retention and Subscription Management
  slug: churnkey-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/churnkey.png
layout: provider
modified: '2026-07-10'
name: Churnkey
nav: Providers
network: true
overview: 'Churnkey publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Billing Contacts API, Customers API, Data Subject Requests API, and 2 more. Tagged areas include Churn Prevention, Retention, Cancellation Flows, Failed Payment Recovery, and Dunning.


  Churnkey''s developer surface includes authentication, documentation, pricing, and 9 more developer resources.'
plans:
- name: Churnkey Plans Pricing
  plan_count: 4
  slug: churnkey-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Churnkey Rate Limits
  slug: churnkey-rate-limits
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 44.6
    developer_ergonomics: 22.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/churnkey/refs/heads/main/screenshots/churnkey-2026-07-25T205328.png
security:
- kind: authentication
  name: Churnkey Authentication
  slug: churnkey-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Churnkey Domain Security
  slug: churnkey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Churnkey Trust Center
  slug: churnkey-trust-center
  summary_line: SOC 2, GDPR
slug: churnkey
tags:
- Churn Prevention
- Retention
- Cancellation Flows
- Failed Payment Recovery
- Dunning
- Reactivation
- Subscription
- Software-as-a-Service
website: https://churnkey.co
---
