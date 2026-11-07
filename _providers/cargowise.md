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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.3
  scored_at: '2026-11-06'
api_count: 5
apis:
- description: 'The eAdaptor Inbound Service is a RESTful XML interface for pushing data into a CargoWise (CW1) instance and querying records. A single inbound endpoint accepts a Universal XML or Native XML payload; '
  name: CargoWise eAdaptor Inbound API
  slug: cargowise-eadaptor-inbound-api
- description: The eAdaptor Outbound Service is the webhook equivalent - CargoWise emits messages to a listening SOAP service when configured Workflow Template milestones or triggers fire. Actions are set to XUS (fu
  name: CargoWise eAdaptor Outbound API
  slug: cargowise-eadaptor-outbound-api
- description: The Universal Shipment (XUS) message is CargoWise's canonical XML model for a full logistics record - forwarding shipment, customs declaration, warehouse order, transport leg, and the associated organ
  name: CargoWise Universal Shipment API
  slug: cargowise-universal-shipment-api
- description: The Universal Event (XUE) message carries a minimal record identifier plus the event or milestone responsible for a notification - the basis for tracking and status integrations. XUE messages are emit
  name: CargoWise Universal Event API
  slug: cargowise-universal-event-api
- description: WiseTech's newer integration path (referred to as eAdaptor Next and xHub) adds REST access authenticated with OAuth 2.0 authorization-code flow, where a registered application receives a client ID and
  name: CargoWise REST Integration API
  slug: cargowise-rest-integration-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/cargowise/plans/cargowise-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cargowise-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/cargowise/security/cargowise-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cargowise-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cargowise/authentication/cargowise-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cargowise-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cargowise/well-known/cargowise-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cargowise-www-security.txt
- group: auth
  href: https://artifacts.apis.io/cargowise/well-known/cargowise-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cargowise-security.txt
- group: auth
  href: https://artifacts.apis.io/cargowise/well-known/cargowise-myaccount-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cargowise-myaccount-security.txt
- group: auth
  href: https://artifacts.apis.io/cargowise/well-known/cargowise-cargowise-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cargowise-cargowise-security.txt
- group: agent
  href: https://artifacts.apis.io/cargowise/well-known/cargowise-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cargowise-well-known.yml
- group: other
  href: https://artifacts.apis.io/cargowise/hosts/cargowise-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cargowise-hosts.yml
- group: build
  href: https://artifacts.apis.io/cargowise/integrations/cargowise-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/cargowise-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/cargowise/vendors/cargowise-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cargowise-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.cargowise.com/news/
- group: company
  title: ''
  type: Blog
  url: https://www.cargowise.com/news/
- group: auth
  href: https://artifacts.apis.io/cargowise/security/cargowise-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cargowise-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cargowise/security/cargowise-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cargowise-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wisetech-global
- group: company
  title: ''
  type: Website
  url: https://www.cargowise.com/
- group: docs
  title: ''
  type: Documentation
  url: https://wisetechacademy.com/explore/product-learning/
- group: company
  title: ''
  type: Partners
  url: https://www.cargowise.com/partners/become-a-partner/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cargowise.com/cargowise-value-pack/
- group: operate
  title: ''
  type: Support
  url: https://www.cargowise.com/support/
- group: operate
  title: ''
  type: Contact
  url: https://www.cargowise.com/contact/
- group: start
  title: ''
  type: Login
  url: https://myaccount.cargowise.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wisetechglobal.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wisetechglobal.com/legal/privacy-and-data-protection-notice/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WiseTechGlobal
- group: other
  title: ''
  type: Company
  url: https://www.wisetechglobal.com/
created: '2026-07-05'
description: CargoWise is WiseTech Global's logistics execution platform - a single-database ERP for international freight forwarding, customs, warehousing, transport, and landside logistics. Its integration surface is delivered primarily through eAdaptor, which pairs a RESTful XML inbound service (push, query, add, and update records) with a SOAP-based outbound service (a webhook equivalent that emits messages on milestones). Payloads use CargoWise's Universal XML schemas - Universal Shipment (XUS), Universal Event (XUE), and Universal Transaction - or the legacy Native XML format. Newer REST integration (eAdaptor Next / xHub) adds OAuth 2.0 authorization-code access. The integration API is real but heavily gated - the eAdaptor Developers Guide and endpoint details are released only after a customer purchases the eAdaptor modules, and partner access runs through WiseTech accreditation and certification. Endpoints below are modeled from public developer references; the authoritative specification
  is not publicly published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cargowise.png
layout: provider
modified: '2026-10-20'
name: CargoWise
nav: Providers
network: true
overview: 'CargoWise is listed with 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Freight Forwarding, Supply Chain, Customs, and Shipping.


  CargoWise''s developer surface includes authentication, engineering blog, documentation, pricing, support, and 22 more developer resources.'
plans:
- name: Cargowise Plans Pricing
  plan_count: 25
  slug: cargowise-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Cargowise Rate Limits
  slug: cargowise-rate-limits
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 63.4
    operational_transparency: 13.2
  previous_composite: 31.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cargowise/cargowise-2026-07-25T204615.png
security:
- kind: authentication
  name: Cargowise Authentication
  slug: cargowise-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Cargowise Domain Security
  slug: cargowise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cargowise Vulnerability Disclosure
  slug: cargowise-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cargowise
tags:
- Logistics
- Freight Forwarding
- Supply Chain
- Customs
- Shipping
- eAdaptor
- Universal XML
- EDI
- WiseTech Global
website: https://www.cargowise.com/
---
