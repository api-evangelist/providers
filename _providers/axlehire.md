---
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
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Assignment specific calls
  name: AxleHire (Jitsu) Assignment Information API
  slug: axlehire-assignment-information-api
- description: Driver specific calls
  name: AxleHire (Jitsu) Driver Information API
  slug: axlehire-driver-information-api
- description: The Partner Information API from AxleHire (Jitsu) — 1 operation(s) for partner information.
  name: AxleHire (Jitsu) Partner Information API
  slug: axlehire-partner-information-api
- description: Shipment specific calls
  name: AxleHire (Jitsu) Shipping Information API
  slug: axlehire-shipping-information-api
- description: Tracking specific calls
  name: AxleHire (Jitsu) Tracking Information API
  slug: axlehire-tracking-information-api
artifact_total: 21
asyncapis:
- description: ''
  name: Axlehire Webhooks
  slug: axlehire-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Jitsu REST Assignment Information API
  slug: open-axlehire-assignment-information-api
- collection_type: open
  name: Jitsu REST Driver Information API
  slug: open-axlehire-driver-information-api
- collection_type: open
  name: Jitsu REST Partner Information API
  slug: open-axlehire-partner-information-api
- collection_type: open
  name: Jitsu REST Shipping Information API
  slug: open-axlehire-shipping-information-api
- collection_type: open
  name: Jitsu REST Tracking Information API
  slug: open-axlehire-tracking-information-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/axlehire-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/axlehire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gojitsu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gojitsu.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gojitsu.com/#/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gojitsu.com/#/docs/QuickStart.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/axlehire-authentication.yml
- group: build
  title: ''
  type: SDKs
  url: packages/axlehire-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/axlehire-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/axlehire-sandbox.yml
- group: start
  title: ''
  type: Login
  url: https://client.gojitsu.com/
- group: operate
  title: ''
  type: Support
  url: https://gojitsu.com/support
- group: company
  title: ''
  type: Blog
  url: https://gojitsu.com/news-insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gojitsu.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gojitsu.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gojitsu.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/axlehire-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/axlehire-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/axlehire-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/axlehire-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/axlehire-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/axlehire-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/axlehire-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/axlehire-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/axlehire-submit-shipment-example.json
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/axlehire-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/axlehire-jitsu-rest-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gojitsu.com/
- group: auth
  title: ''
  type: Security
  url: security/axlehire-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/axlehire-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://gojitsu.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/axlehire-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/axlehire-trust-center.yml
created: '2026-08-06'
description: AxleHire is a US last-mile delivery carrier founded in 2015 that rebranded as Jitsu in April 2024 and now operates at gojitsu.com. It runs an asset-light, gig-driver network with a proprietary routing and tracking platform serving e-commerce, meal-kit and subscription-box shippers across 23 of the 25 largest US metros, seven days a week. The Jitsu REST API (v3) lets shippers submit shipments, retrieve ZPL/PNG/PDF labels, manage parcels, cancel and re-window deliveries, pull rating estimates and proof-of-delivery, and read the full tracking event history. A documented webhook surface pushes ~33 lifecycle events — planning, inbound scan, outbound pickup/dropoff, proof-of-delivery and exceptions — to a registered endpoint. Jitsu publishes an OpenAPI 3.0.1 contract, nine first-party SDKs, a staging environment with a lifecycle simulation API, and a public status page.
examples:
- key_count: 8
  name: Axlehire Retrieve Shipment Example
  slug: axlehire-retrieve-shipment-example
- key_count: 9
  name: Axlehire Shipment Label Example
  slug: axlehire-shipment-label-example
- key_count: 9
  name: Axlehire Submit Shipment Example
  slug: axlehire-submit-shipment-example
- key_count: 8
  name: Axlehire Tracking Events Example
  slug: axlehire-tracking-events-example
image: https://docs.gojitsu.com/static/images/logo-jitsu.svg
layout: provider
modified: '2026-08-06'
name: AxleHire (Jitsu)
nav: Providers
network: true
overview: 'AxleHire (Jitsu) publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Assignment Information API, Driver Information API, Partner Information API, and 2 more. Tagged areas include Company, Logistics, Last Mile Delivery, Shipping, and Parcel.


  The AxleHire (Jitsu) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AxleHire (Jitsu)''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, support, engineering blog, and 27 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 1
  name: Axlehire Rate Limits
  slug: axlehire-rate-limits
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 22
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 66.4
    developer_ergonomics: 35.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 55.3
  previous_composite: 48.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/axlehire/refs/heads/main/screenshots/axlehire-2026-08-07T162043.png
security:
- kind: authentication
  name: Axlehire Authentication
  slug: axlehire-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Axlehire Domain Security
  slug: axlehire-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Axlehire Vulnerability Disclosure
  slug: axlehire-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Axlehire Trust Center
  slug: axlehire-trust-center
  summary_line: SOC 2 Type 2
slug: axlehire
tags:
- Company
- Logistics
- Last Mile Delivery
- Shipping
- Parcel
- Transportation
- Supply Chain
- E-Commerce
- Tracking
- Webhook
website: https://gojitsu.com/
---
