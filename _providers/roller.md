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
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: General-purpose real-time REST API for the ROLLER platform. Retrieve products, sessions and availability, and create and manage real-time bookings to power external checkout and booking journeys. Auth
  name: ROLLER REST API
  slug: roller-rest-api
- description: Read-only Data/Reporting API that gives venues a mechanism to extract a copy of their ROLLER data and syndicate it to an external database, data warehouse or BI/analytics platform. Designed for period
  name: ROLLER Reporting API
  slug: roller-reporting-api
artifact_total: 7
asyncapis:
- description: ''
  name: Roller Webhooks
  slug: roller-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/roller-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.roller.software/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.roller.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.roller.app/docs/api/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.roller.app/docs/api/rest
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.roller.app/docs/api/getting-api-access
- group: auth
  title: ''
  type: Authentication
  url: authentication/roller-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/roller-webhooks.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/roller-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/roller-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.roller.app/docs/api/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.roller.app/
- group: operate
  title: ''
  type: Roadmap
  url: https://launchpad.roller.app/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/roller-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/roller-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/roller-trust-center.yml
- group: build
  title: ''
  type: Postman
  url: https://docs.roller.app/docs/api/postman-collection
- group: operate
  title: ''
  type: Support
  url: https://mysupport.roller.software/
- group: operate
  title: ''
  type: HelpCenter
  url: https://mysupport.roller.software/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.roller.software/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.roller.software/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.roller.software/request-a-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.roller.software/master-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.roller.software/legal/privacy-policy/
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/roller-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/roller-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/roller-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/roller-llms.txt
created: '2026-07-17'
description: ROLLER is a cloud-based venue management platform for the attractions and leisure industry — trampoline parks, family entertainment centers, museums, zoos, aquariums, water parks and amusement venues. It unifies ticketing and online bookings, point of sale, memberships and passes, digital waivers, integrated payments, a CRM and guest experience score, self-serve kiosks and gift cards in a single system. ROLLER exposes two public APIs — a real-time REST API for products, sessions, availability and bookings, and a Reporting (Data) API for extracting venue data to external warehouses and BI tools — plus webhooks for event-driven integrations and OCTO API compatibility for channel/distribution partners. API access is an add-on to a ROLLER subscription and is authenticated with OAuth2 client credentials.
image: https://cdn.rollerdigital.com/assets/logos/roller-logo.svg
layout: provider
modified: '2026-07-21'
name: ROLLER
nav: Providers
network: true
overview: 'ROLLER publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Venue Management, Attractions, Ticketing, and Bookings.


  The ROLLER catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ROLLER''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 21 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 1
  name: Roller Rate Limits
  slug: roller-rate-limits
score:
  band: strong
  composite: 54.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 54.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/roller/refs/heads/main/screenshots/roller-2026-08-17T081633.png
security:
- kind: authentication
  name: Roller Authentication
  slug: roller-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Roller Domain Security
  slug: roller-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Roller Trust Center
  slug: roller-trust-center
  summary_line: SOC 2, PCI DSS
slug: roller
tags:
- Company
- Venue Management
- Attractions
- Ticketing
- Bookings
- Point-of-Sale
- Payments
- Leisure
- Reservations
- Webhook
website: https://www.roller.software/
---
