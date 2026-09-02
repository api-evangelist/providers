---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 27.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 57
  human_in_the_loop: 1
  name: Brushfire Agentic Access
  operation_count: 135
  slug: brushfire-agentic-access
  summary_line: 135 operations · 57 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The AccessCodes API from Brushfire — 3 operation(s) for accesscodes.
  name: Brushfire AccessCodes API
  slug: brushfire-accesscodes-api
- description: The Accounts API from Brushfire — 3 operation(s) for accounts.
  name: Brushfire Accounts API
  slug: brushfire-accounts-api
- description: The Attendees API from Brushfire — 18 operation(s) for attendees.
  name: Brushfire Attendees API
  slug: brushfire-attendees-api
- description: The Cart API from Brushfire — 11 operation(s) for cart.
  name: Brushfire Cart API
  slug: brushfire-cart-api
- description: The Clients API from Brushfire — 3 operation(s) for clients.
  name: Brushfire Clients API
  slug: brushfire-clients-api
- description: The Data API from Brushfire — 1 operation(s) for data.
  name: Brushfire Data API
  slug: brushfire-data-api
- description: The Events API from Brushfire — 27 operation(s) for events.
  name: Brushfire Events API
  slug: brushfire-events-api
- description: The Exchanges API from Brushfire — 2 operation(s) for exchanges.
  name: Brushfire Exchanges API
  slug: brushfire-exchanges-api
- description: The Groups API from Brushfire — 7 operation(s) for groups.
  name: Brushfire Groups API
  slug: brushfire-groups-api
- description: The Hooks API from Brushfire — 7 operation(s) for hooks.
  name: Brushfire Hooks API
  slug: brushfire-hooks-api
- description: The Lookups API from Brushfire — 6 operation(s) for lookups.
  name: Brushfire Lookups API
  slug: brushfire-lookups-api
- description: The Orders API from Brushfire — 11 operation(s) for orders.
  name: Brushfire Orders API
  slug: brushfire-orders-api
- description: The PaymentProfiles API from Brushfire — 4 operation(s) for paymentprofiles.
  name: Brushfire PaymentProfiles API
  slug: brushfire-paymentprofiles-api
- description: The Promotions API from Brushfire — 4 operation(s) for promotions.
  name: Brushfire Promotions API
  slug: brushfire-promotions-api
- description: The Regions API from Brushfire — 1 operation(s) for regions.
  name: Brushfire Regions API
  slug: brushfire-regions-api
- description: The Sessions API from Brushfire — 10 operation(s) for sessions.
  name: Brushfire Sessions API
  slug: brushfire-sessions-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 'Brushfire API: Version 2025-07-22 AccessCodes API'
  slug: open-brushfire-accesscodes-api
- collection_type: open
  name: 'Brushfire API: Version 2025-07-22 AccessCodes Accounts API'
  slug: open-brushfire-accounts-api
- collection_type: open
  name: 'Brushfire API: Version 2025-07-22 AccessCodes Attendees API'
  slug: open-brushfire-attendees-api
- collection_type: open
  name: 'Brushfire API: Version 2025-07-22 AccessCodes Cart API'
  slug: open-brushfire-cart-api
- collection_type: open
  name: 'Brushfire API: Version 2025-07-22 AccessCodes Clients API'
  slug: open-brushfire-clients-api
- collection_type: open
  name: 'Brushfire API: Version 2025-07-22 AccessCodes Data API'
  slug: open-brushfire-data-api
- collection_type: open
  name: 'Brushfire API: Version 2025-07-22 AccessCodes Events API'
  slug: open-brushfire-events-api
- collection_type: open
  name: 'Brushfire API: Version 2025-07-22 AccessCodes Exchanges API'
  slug: open-brushfire-exchanges-api
- collection_type: open
  name: 'Brushfire API: Version 2025-07-22 AccessCodes Groups API'
  slug: open-brushfire-groups-api
- collection_type: open
  name: 'Brushfire API: Version 2025-07-22 AccessCodes Hooks API'
  slug: open-brushfire-hooks-api
- collection_type: open
  name: 'Brushfire API: Version 2025-07-22 AccessCodes Lookups API'
  slug: open-brushfire-lookups-api
- collection_type: open
  name: 'Brushfire API: Version 2025-07-22 AccessCodes Orders API'
  slug: open-brushfire-orders-api
- collection_type: open
  name: 'Brushfire API: Version 2025-07-22 AccessCodes PaymentProfiles API'
  slug: open-brushfire-paymentprofiles-api
- collection_type: open
  name: 'Brushfire API: Version 2025-07-22 AccessCodes Promotions API'
  slug: open-brushfire-promotions-api
- collection_type: open
  name: 'Brushfire API: Version 2025-07-22 AccessCodes Regions API'
  slug: open-brushfire-regions-api
- collection_type: open
  name: 'Brushfire API: Version 2025-07-22 AccessCodes Sessions API'
  slug: open-brushfire-sessions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brushfire-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brushfire-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brushfire-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brushfire-technology
- group: company
  title: ''
  type: Website
  url: https://www.brushfire.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.brushfire.com
- group: docs
  title: ''
  type: APIReference
  url: https://api.brushfire.com/swagger/index.html
- group: start
  title: ''
  type: SignUp
  url: https://developer.brushfire.com/key
- group: commercial
  title: ''
  type: Plans
  url: plans/brushfire-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brushfire-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/brushfire-finops.yml
- group: other
  title: ''
  type: X
  url: https://twitter.com/BrushfireApp
created: '2026-07-05'
description: Brushfire is an event ticketing, registration, and virtual event platform used by churches, ministries, conferences, attractions, and large events. Alongside its hosted box office, embeddable event widgets, and mobile check-in apps, Brushfire publishes a documented REST API at api.brushfire.com covering events, ticket types, sections and seats, attendees, orders, the shopping cart and checkout flow, groups, sessions and check-in, promotions and access codes, payment profiles, and webhooks. The API is date-versioned through an api-version request header and authenticated with an App Key requested from developer.brushfire.com.
finops:
- name: Brushfire Finops
  service_category: Event Ticketing and Registration
  slug: brushfire-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brushfire.png
layout: provider
modified: '2026-07-05'
name: Brushfire
nav: Providers
network: true
overview: 'Brushfire publishes 16 APIs on the [APIs.io](https://apis.io/) network, including AccessCodes API, Accounts API, Attendees API, and 13 more. Tagged areas include Event Ticketing, Registration, Event, Ticketing, and Check-in.


  Brushfire''s developer surface includes authentication, documentation, API reference, signup flow, and 8 more developer resources.'
plans:
- name: Brushfire Plans Pricing
  plan_count: 5
  slug: brushfire-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Brushfire Rate Limits
  slug: brushfire-rate-limits
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.3
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brushfire/refs/heads/main/screenshots/brushfire-2026-07-25T204003.png
security:
- kind: authentication
  name: Brushfire Authentication
  slug: brushfire-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Brushfire Domain Security
  slug: brushfire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brushfire
tags:
- Event Ticketing
- Registration
- Event
- Ticketing
- Check-in
- Churches
- Payments
website: https://www.brushfire.com
---
