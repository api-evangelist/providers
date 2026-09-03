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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://{supplier_endpoint}/octo
  baseurl_source: declared
  description: The Availability API from Klook — 2 operation(s) for availability.
  name: Klook Availability API
  slug: klook-availability-api
- baseURL: https://{supplier_endpoint}/octo
  baseurl_source: declared
  description: The Bookings API from Klook — 5 operation(s) for bookings.
  name: Klook Bookings API
  slug: klook-bookings-api
- baseURL: https://{supplier_endpoint}/octo
  baseurl_source: declared
  description: The Products API from Klook — 2 operation(s) for products.
  name: Klook Products API
  slug: klook-products-api
- baseURL: https://{supplier_endpoint}/octo
  baseurl_source: declared
  description: The Supplier API from Klook — 1 operation(s) for supplier.
  name: Klook Supplier API
  slug: klook-supplier-api
artifact_total: 12
asyncapis:
- description: ''
  name: Klook Notifications Webhooks
  slug: klook-notifications-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OCTO API Specification Availability API
  slug: open-klook-availability-api
- collection_type: open
  name: OCTO API Specification Availability Bookings API
  slug: open-klook-bookings-api
- collection_type: open
  name: OCTO API Specification Availability Products API
  slug: open-klook-products-api
- collection_type: open
  name: OCTO API Specification Availability Supplier API
  slug: open-klook-supplier-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/klook-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.klook.com/en-US/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://klook.gitbook.io/openapi
- group: docs
  title: ''
  type: Documentation
  url: https://klook.gitbook.io/openapi
- group: docs
  title: ''
  type: APIReference
  url: https://klook.gitbook.io/openapi/getting-started/endpoint-and-capabilities.md
- group: start
  title: ''
  type: GettingStarted
  url: https://klook.gitbook.io/openapi/getting-started/integration-process.md
- group: company
  title: ''
  type: Partners
  url: https://www.klook.com/partner/
- group: other
  title: ''
  type: Affiliate
  url: https://affiliate.klook.com/home
- group: start
  title: ''
  type: MerchantPortal
  url: https://merchant.klook.com/
- group: start
  title: ''
  type: SignUp
  url: https://affiliate.klook.com/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.klook.com/conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.klook.com/en-US/policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.klook.com/en-US/cookiepolicy/
- group: operate
  title: ''
  type: Support
  url: https://www.klook.com/en-US/faq/
- group: company
  title: ''
  type: About
  url: https://www.klook.com/en-US/about/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/klook-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/klook-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/klook-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/klook-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/klook-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/klook-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/klook-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/klook-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/klook-octo-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/klook-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/klook-notifications-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/klook-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klook-domain-security.yml
created: '2026-07-17'
description: 'Klook is a Hong Kong-headquartered travel and experiences booking platform for the "things to do" sector — attractions, tours and activities, theme parks, food and beverage, WiFi and SIM cards, and transportation passes. Klook publishes an Open API specification for merchants, suppliers, reservation systems and channel managers who want to distribute their inventory through Klook''s website, app and partner channels. The specification is an implementation of OCTO (Open Connectivity for Tours, Activities and Attractions), the open standard for the in-destination experiences industry: the supplier implements the OCTO core endpoints (Supplier, Products, Availability, Bookings) at their own host and Klook consumes them as the reseller, with optional Capabilities negotiated through the Octo-Capabilities header. Klook additionally runs an affiliate program and a merchant portal.'
image: https://res.klook.com/image/upload/klook_logo.png
layout: provider
modified: '2026-07-19'
name: Klook
nav: Providers
network: true
overview: 'Klook publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Bookings API, Products API, and 1 more. Tagged areas include Company, Marketplaces, Travel, Tours and Activities, and Booking.


  The Klook catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Klook''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, changelog, and 22 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 58.9
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 43.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/klook/refs/heads/main/screenshots/klook-2026-08-17T123946.png
security:
- kind: authentication
  name: Klook Authentication
  slug: klook-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Klook Domain Security
  slug: klook-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: klook
tags:
- Company
- Marketplaces
- Travel
- Tours and Activities
- Booking
- Experience
- Distribution
- OCTO
- Hospitality
website: https://www.klook.com/en-US/
---
