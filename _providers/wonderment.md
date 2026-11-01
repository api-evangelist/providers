---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - '{''url'': ''https://www.wonderment.com/'', ''status'': 302, ''note'': ''declared website redirects to https://www.loopreturns.com/wonderment-is-now-loop-tracking/ — a different registrable domain (wonderment.com -> loopreturns.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wonderment Agentic Access
  operation_count: 4
  slug: wonderment-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://api.wonderment.com
  baseurl_source: declared
  description: Delivery-date predictions for shipping methods.
  name: Wonderment Delivery Promise API
  slug: wonderment-delivery-promise-api
- baseURL: https://api.wonderment.com
  baseurl_source: declared
  description: List and download shipment report exports.
  name: Wonderment Reports API
  slug: wonderment-reports-api
- baseURL: https://api.wonderment.com
  baseurl_source: declared
  description: Search shipments and tracking events for the authenticated shop.
  name: Wonderment Shipments API
  slug: wonderment-shipments-api
arazzos:
- description: List the authenticated shop's shipment report exports and download the most recent finished, non-expired report.
  name: Wonderment — export and download a shipment report
  slug: wonderment-report-export
artifact_total: 14
asyncapis:
- description: ''
  name: Wonderment Webhooks
  slug: wonderment-webhooks
collections:
- collection_type: open
  name: Wonderment Delivery Promise API
  slug: open-wonderment-delivery-promise-api
- collection_type: open
  name: Wonderment Delivery Promise Reports API
  slug: open-wonderment-reports-api
- collection_type: open
  name: Wonderment Delivery Promise Shipments API
  slug: open-wonderment-shipments-api
common:
- group: company
  title: ''
  type: Blog
  url: https://www.loopreturns.com/blog/
- group: other
  href: https://artifacts.apis.io/wonderment/capabilities/wonderment-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/wonderment-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/wonderment/overlays/wonderment-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/wonderment-openapi-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://wonderment.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://wonderment.readme.io/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://help.wonderment.com/en/categories/1026689-getting-started-with-track
- group: operate
  title: ''
  type: Support
  url: https://help.wonderment.com/
- group: start
  title: ''
  type: Login
  url: https://app.wonderment.com/
- group: agent
  href: https://artifacts.apis.io/wonderment/llms/wonderment-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wonderment-llms.txt
- group: agent
  href: https://artifacts.apis.io/wonderment/mcp/wonderment-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/wonderment-mcp.yml
- group: auth
  href: https://artifacts.apis.io/wonderment/authentication/wonderment-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wonderment-authentication.yml
- group: agent
  href: https://artifacts.apis.io/wonderment/agentic-access/wonderment-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wonderment-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/wonderment/conventions/wonderment-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wonderment-conventions.yml
- group: design
  href: https://artifacts.apis.io/wonderment/errors/wonderment-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wonderment-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wonderment/lifecycle/wonderment-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wonderment-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/wonderment/conformance/wonderment-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wonderment-conformance.yml
- group: design
  href: https://artifacts.apis.io/wonderment/data-model/wonderment-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wonderment-data-model.yml
- group: design
  href: https://artifacts.apis.io/wonderment/components/wonderment-components.yml
  title: ''
  type: Components
  url: components/wonderment-components.yml
- group: design
  href: https://artifacts.apis.io/wonderment/asyncapi/wonderment-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/wonderment-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/wonderment/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/wonderment/arazzo/wonderment-report-export.yml
  title: ''
  type: Arazzo
  url: arazzo/wonderment-report-export.yml
- group: auth
  href: https://artifacts.apis.io/wonderment/security/wonderment-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wonderment-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wonderment.com/
created: '2026-07-17'
description: Wonderment is a post-purchase order-tracking and shipment-visibility platform for ecommerce brands (built for Shopify), now part of Loop as Loop Tracking. It ingests carrier tracking data, surfaces proactive delivery updates, powers branded self-serve tracking pages, and reports on shipment performance. The public REST API (versioned 2022-10, hosted at api.wonderment.com) lets merchants search shipments by order name or tracking code, list and download shipment report exports, and fetch delivery-date predictions for shipping methods, plus webhooks for shipping events. Originally a CRV-backed company, added to the API Evangelist network and enriched from its ReadMe developer hub.
image: https://www.wonderment.com/
layout: provider
modified: '2026-10-06'
name: Wonderment
nav: Providers
network: true
overview: 'Wonderment publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Delivery Promise API, Reports API, and Shipments API. Tagged areas include Company, E-Commerce, Order Tracking, Post-Purchase, and Shipping.


  The Wonderment catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wonderment''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, authentication, and 17 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 58.0
    developer_ergonomics: 49.4
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/wonderment/wonderment-2026-09-02T170915.png
security:
- kind: authentication
  name: Wonderment Authentication
  slug: wonderment-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wonderment Domain Security
  slug: wonderment-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Quote a delivery date
  slug: wonderment-delivery-promise
- name: Export and download a shipment report
  slug: wonderment-export-report
- name: Track a shipment
  slug: wonderment-track-shipment
slug: wonderment
tags:
- Company
- E-Commerce
- Order Tracking
- Post-Purchase
- Shipping
- Logistics
- Shopify
- Webhook
website: https://www.wonderment.com/
---
