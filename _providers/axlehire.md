---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
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
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.gojitsu.com
  baseurl_source: declared
  description: Assignment specific calls
  name: AxleHire (Jitsu) Assignment Information API
  slug: axlehire-assignment-information-api
- baseURL: https://api.gojitsu.com
  baseurl_source: declared
  description: Driver specific calls
  name: AxleHire (Jitsu) Driver Information API
  slug: axlehire-driver-information-api
- baseURL: https://api.gojitsu.com
  baseurl_source: declared
  description: The Partner Information API from AxleHire (Jitsu) — 1 operation(s) for partner information.
  name: AxleHire (Jitsu) Partner Information API
  slug: axlehire-partner-information-api
- baseURL: https://api.gojitsu.com
  baseurl_source: declared
  description: Shipment specific calls
  name: AxleHire (Jitsu) Shipping Information API
  slug: axlehire-shipping-information-api
- baseURL: https://api.gojitsu.com
  baseurl_source: declared
  description: Tracking specific calls
  name: AxleHire (Jitsu) Tracking Information API
  slug: axlehire-tracking-information-api
artifact_total: 26
asyncapis:
- description: ''
  name: Axlehire Webhooks
  slug: axlehire-webhooks
collections:
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
- group: company
  title: ''
  type: BlogRSS
  url: https://gojitsu.com/news-insights/rss.xml
- group: other
  href: https://artifacts.apis.io/axlehire/capabilities/axlehire-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/axlehire-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/axlehire/security/axlehire-domain-security.yml
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
  href: https://artifacts.apis.io/axlehire/authentication/axlehire-authentication.yml
  title: ''
  type: Authentication
  url: authentication/axlehire-authentication.yml
- group: build
  href: https://artifacts.apis.io/axlehire/packages/axlehire-packages.yml
  title: ''
  type: SDKs
  url: packages/axlehire-packages.yml
- group: build
  href: https://artifacts.apis.io/axlehire/packages/axlehire-packages.yml
  title: ''
  type: Packages
  url: packages/axlehire-packages.yml
- group: start
  href: https://artifacts.apis.io/axlehire/sandbox/axlehire-sandbox.yml
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
  href: https://artifacts.apis.io/axlehire/lifecycle/axlehire-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/axlehire-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/axlehire/asyncapi/axlehire-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/axlehire-webhooks.yml
- group: design
  href: https://artifacts.apis.io/axlehire/errors/axlehire-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/axlehire-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/axlehire/rate-limits/axlehire-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/axlehire-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/axlehire/conventions/axlehire-conventions.yml
  title: ''
  type: Conventions
  url: conventions/axlehire-conventions.yml
- group: design
  href: https://artifacts.apis.io/axlehire/conformance/axlehire-conformance.yml
  title: ''
  type: Conformance
  url: conformance/axlehire-conformance.yml
- group: design
  href: https://artifacts.apis.io/axlehire/components/axlehire-components.yml
  title: ''
  type: Components
  url: components/axlehire-components.yml
- group: design
  href: https://artifacts.apis.io/axlehire/data-model/axlehire-data-model.yml
  title: ''
  type: DataModel
  url: data-model/axlehire-data-model.yml
- group: build
  href: https://artifacts.apis.io/axlehire/examples/axlehire-submit-shipment-example.json
  title: ''
  type: Examples
  url: examples/axlehire-submit-shipment-example.json
- group: agent
  href: https://artifacts.apis.io/axlehire/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/axlehire/llms/axlehire-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/axlehire-llms.txt
- group: other
  href: https://artifacts.apis.io/axlehire/overlays/axlehire-jitsu-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/axlehire-jitsu-rest-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gojitsu.com/
- group: auth
  href: https://artifacts.apis.io/axlehire/security/axlehire-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/axlehire-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/axlehire/security/axlehire-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/axlehire-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://gojitsu.com/security
- group: auth
  href: https://artifacts.apis.io/axlehire/security/axlehire-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/axlehire-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/axlehire/security/axlehire-trust-center.yml
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
modified: '2026-10-06'
name: AxleHire (Jitsu)
nav: Providers
network: true
overview: 'AxleHire (Jitsu) publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assignment Information API, Driver Information API, Partner Information API, and 2 more. Tagged areas include Company, Logistics, Last Mile Delivery, Shipping, and Parcel.


  The AxleHire (Jitsu) catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  AxleHire (Jitsu)''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, support, engineering blog, and 28 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 1
  name: Axlehire Rate Limits
  slug: axlehire-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: AxleHire (Jitsu) API Rules
  rule_count: 62
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 13
  slug: axlehire-rules
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    contract_governance: 31.8
    contract_quality: 60.9
    developer_ergonomics: 35.1
    discoverability: 66.1
    operational_transparency: 55.3
  previous_composite: 50.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/axlehire/axlehire-2026-08-07T162043.png
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
skill_count: 5
skills:
- name: Cancel or reschedule a shipment
  slug: axlehire-cancel-or-reschedule
- name: Retrieve and print a shipping label
  slug: axlehire-print-shipping-label
- name: Rate a delivery and mark it shipped
  slug: axlehire-rate-and-handoff
- name: Submit a shipment for last-mile delivery
  slug: axlehire-submit-shipment
- name: Track a delivery end to end
  slug: axlehire-track-delivery
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
