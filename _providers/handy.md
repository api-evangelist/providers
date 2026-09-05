---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Handy Agentic Access
  operation_count: 10
  slug: handy-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
apis:
- baseURL: https://partners.services.handy.com/api/v1
  baseurl_source: declared
  description: The Bookings API from handy — 1 operation(s) for bookings.
  name: handy Bookings API
  slug: handy-bookings-api
- baseURL: https://partners.services.handy.com/api/v1
  baseurl_source: declared
  description: The Order Products API from handy — 2 operation(s) for order products.
  name: handy Order Products API
  slug: handy-order-products-api
- baseURL: https://partners.services.handy.com/api/v1
  baseurl_source: declared
  description: The Orders API from handy — 2 operation(s) for orders.
  name: handy Orders API
  slug: handy-orders-api
- baseURL: https://partners.services.handy.com/api/v1
  baseurl_source: declared
  description: The Testing API from handy — 1 operation(s) for testing.
  name: handy Testing API
  slug: handy-testing-api
artifact_total: 14
asyncapis:
- description: ''
  name: Handy Webhooks
  slug: handy-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Handy’s Partner Bookings API
  slug: open-handy-bookings-api
- collection_type: open
  name: Handy’s Partner Bookings Order Products API
  slug: open-handy-order-products-api
- collection_type: open
  name: Handy’s Partner Bookings Orders API
  slug: open-handy-orders-api
- collection_type: open
  name: Handy’s Partner Bookings Testing API
  slug: open-handy-testing-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/handy-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/handy-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partners.services.handy.com/docs/orders_api
- group: docs
  title: ''
  type: Documentation
  url: https://partners.services.handy.com/docs/orders_api
- group: docs
  title: ''
  type: APIReference
  url: https://partners.services.handy.com/docs/orders_api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Handybook
- group: operate
  title: ''
  type: Support
  url: https://help.handy.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.handy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.handy.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/handy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/handy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/handy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/handy-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/handy-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/handy-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/handy-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/handy-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/handy-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/handy-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/handy-orders-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/handy-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/handy-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.handy.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/handy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/handy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://handy.com
created: '2026-07-17'
description: 'Handy is a home-services marketplace, now part of Angi (ANGI Homeservices), that connects customers with pre-screened independent professionals for house cleaning, handyman work, furniture assembly, and in-home installations. Handy''s Partner API lets retailers offer fixed-price installation and service bookings at eCommerce or in-store checkout: partners create and manage orders, products, and line items, retrieve bookings and their assigned providers, and receive booking-lifecycle webhooks. Requests are authenticated with a custom RSA-SHA256 signed-request scheme.'
image: https://www.handy.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: handy
nav: Providers
network: true
overview: 'handy publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Bookings API, Order Products API, Orders API, and 1 more. Tagged areas include Company, Home Services, Marketplace, Cleaning, and Handyman.


  The handy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  handy''s developer surface includes documentation, API reference, support, authentication, sandbox, and 22 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 56.9
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/handy/refs/heads/main/screenshots/handy-2026-07-25T220617.png
security:
- kind: authentication
  name: Handy Authentication
  slug: handy-authentication
  summary_line: signed-request · 1 scheme
- kind: domain-security
  name: Handy Domain Security
  slug: handy-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Handy Vulnerability Disclosure
  slug: handy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: handy
tags:
- Company
- Home Services
- Marketplace
- Cleaning
- Handyman
- Installations
- On-Demand
- Gig Economy
- Order
- Webhook
- Retail
- Angi
website: https://handy.com
---
