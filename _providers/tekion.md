---
access_model:
  confidence: low
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 6
apis:
- description: Near real-time access to a dealership's sales and deal data - deal jackets, desking, F&I products, and sold-vehicle records - through the Automotive Partner Cloud. Concrete paths and schemas are publi
  name: Tekion Sales and Deals API
  slug: tekion-sales-deals-api
- description: Access to new and used vehicle inventory - stock, VIN-level detail, pricing, and availability - exposed to approved partners via APC standard open APIs and webhooks. Exact endpoints live behind the pa
  name: Tekion Inventory API
  slug: tekion-inventory-api
- description: Fixed-operations and service data - repair orders, service appointments, labor operations, and status updates - available to approved partners through APC APIs and webhooks for near real-time sync. En
  name: Tekion Service API
  slug: tekion-service-api
- description: Parts inventory, catalog lookup, pricing, and ordering data (including electronic parts catalog / EPC integration) exposed to approved partners via APC. Concrete endpoints are published in the gated p
  name: Tekion Parts API
  slug: tekion-parts-api
- description: Customer and CRM records - contact, ownership, and relationship data tied to sales and service activity - made available to approved partners through APC, subject to the dealer's data-sharing authoriz
  name: Tekion Customers API
  slug: tekion-customers-api
- description: Server-to-endpoint webhooks that keep partner systems in sync as dealership data changes across sales, service, inventory, and parts. Webhooks POST event payloads to a partner-registered HTTP endpoint
  name: Tekion Webhooks
  slug: tekion-webhooks-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.tekion.com/
- group: agent
  href: https://artifacts.apis.io/tekion/llms/tekion-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tekion-llms.txt
- group: auth
  href: https://artifacts.apis.io/tekion/well-known/tekion-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tekion-status-security.txt
- group: agent
  href: https://artifacts.apis.io/tekion/well-known/tekion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tekion-well-known.yml
- group: other
  href: https://artifacts.apis.io/tekion/hosts/tekion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tekion-hosts.yml
- group: other
  href: https://artifacts.apis.io/tekion/vendors/tekion-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tekion-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://tekion.com/trust-portal/security
- group: company
  title: ''
  type: Blog
  url: https://tekion.com/blog
- group: auth
  href: https://artifacts.apis.io/tekion/security/tekion-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tekion-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/tekion/security/tekion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tekion-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tekion
- group: company
  title: ''
  type: Website
  url: https://tekion.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tekion.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tekion.com/trust-portal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tekion.com/refer/terms
- group: company
  title: ''
  type: Newsroom
  url: https://tekion.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://tekion.com/products/apc
- group: start
  title: ''
  type: Portal
  url: https://apc.tekioncloud.com
- group: start
  title: ''
  type: SignUp
  url: https://apc.tekioncloud.com/user/register
- group: commercial
  href: https://artifacts.apis.io/tekion/plans/tekion-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tekion-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/tekion/rate-limits/tekion-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tekion-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tekion/finops/tekion-finops.yml
  title: ''
  type: FinOps
  url: finops/tekion-finops.yml
coverage:
  checked: '2026-10-20'
  detail: Tekion's Automotive Partner Cloud API reference sits behind partner registration at apc.tekioncloud.com/user/register with use-case review; no public OpenAPI is served at api.tekioncloud.com or apc.tekioncloud.com.
  evidence:
  - status: 200
    url: https://apc.tekioncloud.com/user/register
  - status: 404
    url: https://api.tekioncloud.com/openapi.json
  - status: 404
    url: https://apc.tekioncloud.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-07-10'
description: 'Tekion is a cloud-native, AI-native automotive retail platform whose flagship Automotive Retail Cloud (ARC) is a modern dealer management system (DMS) spanning sales, service, parts, inventory, F&I, accounting, and CRM for franchise dealerships and OEMs. Tekion exposes its data and workflows to technology partners through the Automotive Partner Cloud (APC) - an open, OpenAPI-standard partner API program with REST APIs and webhooks that give approved partners near real-time access to a dealership''s sales, service, inventory, and parts data. APC is partner-gated: developers register at the APC portal, submit a use case, and are reviewed (typically within ~48 hours) before the API documentation dashboard, credentials, and endpoints are unlocked. Access is tiered (Standard, Enterprise/Elevated, Premium/Strategic) with different API scopes, rate limits, and read/write capabilities. Because the technical reference is behind partner authentication, the APIs below are honestly modeled
  by data domain rather than transcribed from a public spec.'
finops:
- has_sources: true
  method: generated
  name: Tekion Finops
  primary_unit: ''
  service_category: Automotive Software and Integration
  slug: tekion-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tekion.png
layout: provider
modified: '2026-10-06'
name: Tekion
nav: Providers
network: true
overview: 'Tekion is listed with 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Dealership, DMS, Automotive Retail Cloud, and Partner API.


  Tekion''s developer surface includes engineering blog, documentation, developer portal, signup flow, and 18 more developer resources.'
plans:
- name: Tekion Plans Pricing
  plan_count: 3
  slug: tekion-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Tekion Rate Limits
  slug: tekion-rate-limits
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 79.5
    operational_transparency: 21.1
  previous_composite: 28.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tekion/tekion-2026-09-02T162726.png
security:
- kind: domain-security
  name: Tekion Domain Security
  slug: tekion-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Tekion Trust Center
  slug: tekion-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: tekion
tags:
- Automotive
- Dealership
- DMS
- Automotive Retail Cloud
- Partner API
- Sales
- Services
- Inventory
- Parts
- Webhook
- Gated
website: https://tekion.com
---
