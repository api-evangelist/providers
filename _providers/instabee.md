---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Budbee's public REST API for e-commerce merchants and integration partners to create delivery orders, book home and locker delivery intervals, validate serviceable postal codes, discover parcel locker
  name: Budbee Delivery API
  slug: budbee-delivery-api
artifact_total: 5
asyncapis:
- description: ''
  name: Instabee Webhooks
  slug: instabee-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://instabee.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.budbee.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.budbee.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.budbee.com/
- group: company
  title: ''
  type: Blog
  url: https://press.instabee.com/
- group: company
  title: ''
  type: Careers
  url: https://career.instabee.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://instabee.com/legal/general-terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://instabee.com/legal/external-privacy-notice
- group: start
  title: ''
  type: Login
  url: https://partner.instabee.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/instabee-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/instabee-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/instabee-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/instabee-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/instabee-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/instabee-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/instabee-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/instabee-sandbox.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/instabee-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instabee-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/instabee-llms.txt
created: '2026-07-17'
description: Instabee is a European last-mile logistics technology company formed by the 2022 merger of Instabox and Budbee, operating consumer delivery brands Instabox (Sweden, Denmark, Norway), Budbee (Sweden, Denmark, Finland, the Netherlands, Belgium) and Porterbuddy (Norway). It moves tens of millions of parcels a year across parcel lockers, home delivery and returns for 1,150+ merchant clients through 45+ parcel terminals, serving 10M+ active users. Instabee exposes a public REST developer API under the Budbee brand for creating and managing delivery orders, booking delivery intervals, discovering lockers/boxes and serviceable postal codes, generating shipping labels, booking returns, and subscribing to parcel-status webhooks across its Nordic and Benelux network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instabee.png
layout: provider
modified: '2026-07-19'
name: Instabee
nav: Providers
network: true
overview: 'Instabee publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Logistics, Last Mile Delivery, and Shipping.


  The Instabee catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Instabee''s developer surface includes documentation, API reference, engineering blog, authentication, sandbox, and 15 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 3
  name: Instabee Rate Limits
  slug: instabee-rate-limits
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 39.2
  provenance:
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instabee/refs/heads/main/screenshots/instabee-2026-07-25T222557.png
security:
- kind: authentication
  name: Instabee Authentication
  slug: instabee-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Instabee Domain Security
  slug: instabee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: instabee
tags:
- Company
- Retail
- Logistics
- Last Mile Delivery
- Shipping
- E-Commerce
- Parcel Lockers
- Returns
- Nordics
website: https://instabee.com/
---
