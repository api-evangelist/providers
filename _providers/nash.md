---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 116
  human_in_the_loop: 16
  name: Nash Agentic Access
  operation_count: 173
  slug: nash-agentic-access
  summary_line: 173 operations · 116 acting · 16 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: LLM-backed domain tools
  name: Nash AI Functions API
  slug: nash-ai-functions-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Annotate
  name: Nash Annotate API
  slug: nash-annotate-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Batch Job
  name: Nash Batch Job API
  slug: nash-batch-job-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Provider contract pricing and version listings
  name: Nash Contracts API
  slug: nash-contracts-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Couriers
  name: Nash Couriers API
  slug: nash-couriers-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Delivery Windows
  name: Nash Delivery Windows API
  slug: nash-delivery-windows-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Dispatch Strategies
  name: Nash Dispatch Strategies API
  slug: nash-dispatch-strategies-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Feedback
  name: Nash Feedback API
  slug: nash-feedback-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Inbound endpoints fleets call to update in-flight deliveries.
  name: Nash Fleet API
  slug: nash-fleet-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Job
  name: Nash Job API
  slug: nash-job-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Messaging
  name: Nash Messaging API
  slug: nash-messaging-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Miscellaneous
  name: Nash Miscellaneous API
  slug: nash-miscellaneous-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Notifications
  name: Nash Notifications API
  slug: nash-notifications-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Create, read, update, and delete route optimization strategies.
  name: Nash Optimization Strategies API
  slug: nash-optimization-strategies-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Order
  name: Nash Order API
  slug: nash-order-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Organizations
  name: Nash Organizations API
  slug: nash-organizations-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Provider
  name: Nash Provider API
  slug: nash-provider-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Route
  name: Nash Route API
  slug: nash-route-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Org-scoped geographic areas the route optimizer must avoid traversing.
  name: Nash Route Restrictions API
  slug: nash-route-restrictions-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Shifts
  name: Nash Shifts API
  slug: nash-shifts-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Shipping operations
  name: Nash Shipping API
  slug: nash-shipping-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Store Catalog
  name: Nash Store Catalog API
  slug: nash-store-catalog-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Store Locations
  name: Nash Store Locations API
  slug: nash-store-locations-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Templates
  name: Nash Templates API
  slug: nash-templates-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: User, role, and organization-membership management.
  name: Nash Users API
  slug: nash-users-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Vehicles
  name: Nash Vehicles API
  slug: nash-vehicles-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Webhook delivery inspection
  name: Nash Webhooks API
  slug: nash-webhooks-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Workflow automation management
  name: Nash Workflow API
  slug: nash-workflow-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Workflow execution history and monitoring
  name: Nash Workflow Execution API
  slug: nash-workflow-execution-api
- baseURL: https://api.usenash.com/v1
  baseurl_source: declared
  description: Zones
  name: Nash Zones API
  slug: nash-zones-api
artifact_total: 75
asyncapis:
- description: Real-time delivery events Nash pushes to subscriber endpoints over HTTP, delivered and signed via Svix. Each message carries `type`, `event`, and `data`. Endpoints are registered per event type in the
  name: Nash Webhooks
  slug: nash-webhooks-asyncapi
- description: ''
  name: Nash Webhooks
  slug: nash-webhooks
collections:
- collection_type: open
  name: Nash AI Functions API
  slug: open-nash-ai-functions-api
- collection_type: open
  name: Nash AI Functions Annotate API
  slug: open-nash-annotate-api
- collection_type: open
  name: Nash AI Functions Batch Job API
  slug: open-nash-batch-job-api
- collection_type: open
  name: Nash AI Functions Contracts API
  slug: open-nash-contracts-api
- collection_type: open
  name: Nash AI Functions Couriers API
  slug: open-nash-couriers-api
- collection_type: open
  name: Nash AI Functions Delivery Windows API
  slug: open-nash-delivery-windows-api
- collection_type: open
  name: Nash AI Functions Dispatch Strategies API
  slug: open-nash-dispatch-strategies-api
- collection_type: open
  name: Nash AI Functions Feedback API
  slug: open-nash-feedback-api
- collection_type: open
  name: Nash AI Functions Fleet API
  slug: open-nash-fleet-api
- collection_type: open
  name: Nash AI Functions Job API
  slug: open-nash-job-api
- collection_type: open
  name: Nash AI Functions Messaging API
  slug: open-nash-messaging-api
- collection_type: open
  name: Nash AI Functions Miscellaneous API
  slug: open-nash-miscellaneous-api
- collection_type: open
  name: Nash AI Functions Notifications API
  slug: open-nash-notifications-api
- collection_type: open
  name: Nash AI Functions Optimization Strategies API
  slug: open-nash-optimization-strategies-api
- collection_type: open
  name: Nash AI Functions Order API
  slug: open-nash-order-api
- collection_type: open
  name: Nash AI Functions Organizations API
  slug: open-nash-organizations-api
- collection_type: open
  name: Nash AI Functions Provider API
  slug: open-nash-provider-api
- collection_type: open
  name: Nash AI Functions Route API
  slug: open-nash-route-api
- collection_type: open
  name: Nash AI Functions Route Restrictions API
  slug: open-nash-route-restrictions-api
- collection_type: open
  name: Nash AI Functions Shifts API
  slug: open-nash-shifts-api
- collection_type: open
  name: Nash AI Functions Shipping API
  slug: open-nash-shipping-api
- collection_type: open
  name: Nash AI Functions Store Catalog API
  slug: open-nash-store-catalog-api
- collection_type: open
  name: Nash AI Functions Store Locations API
  slug: open-nash-store-locations-api
- collection_type: open
  name: Nash AI Functions Templates API
  slug: open-nash-templates-api
- collection_type: open
  name: Nash AI Functions Users API
  slug: open-nash-users-api
- collection_type: open
  name: Nash AI Functions Vehicles API
  slug: open-nash-vehicles-api
- collection_type: open
  name: Nash AI Functions Webhooks API
  slug: open-nash-webhooks-api
- collection_type: open
  name: Nash AI Functions Workflow API
  slug: open-nash-workflow-api
- collection_type: open
  name: Nash AI Functions Workflow Execution API
  slug: open-nash-workflow-execution-api
- collection_type: open
  name: Nash AI Functions Zones API
  slug: open-nash-zones-api
common:
- group: operate
  href: https://artifacts.apis.io/nash/rate-limits/nash-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nash-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/nash/plans/nash-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nash-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/nash/capabilities/nash-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/nash-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/nash/overlays/nash-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nash-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.nash.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.usenash.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usenash.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usenash.com/api-reference/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.usenash.com/reference/plan-your-integration
- group: start
  title: ''
  type: Quickstart
  url: https://docs.usenash.com/reference/generating-api-key-and-org-id
- group: operate
  title: ''
  type: Support
  url: https://help.usenash.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.usenash.com
- group: company
  title: ''
  type: Blog
  url: https://www.nash.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.usenash.com/release-notes/change
- group: operate
  title: ''
  type: StatusPage
  url: https://status.usenash.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usenash
- group: start
  title: ''
  type: SignUp
  url: https://portal.usenash.com
- group: start
  title: ''
  type: Login
  url: https://portal.usenash.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nash.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nash.ai/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nash.ai/legal/privacy-policy
- group: agent
  href: https://artifacts.apis.io/nash/mcp/nash-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/nash-mcp.yml
- group: agent
  href: https://artifacts.apis.io/nash/llms/nash-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nash-llms.txt
- group: agent
  href: https://artifacts.apis.io/nash/well-known/nash-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nash-well-known.yml
- group: design
  href: https://artifacts.apis.io/nash/lifecycle/nash-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nash-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/nash/changelog/nash-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/nash-changelog.yml
- group: design
  href: https://artifacts.apis.io/nash/conformance/nash-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nash-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.nash.ai/legal/security
- group: auth
  href: https://artifacts.apis.io/nash/security/nash-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/nash-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/nash/security/nash-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/nash-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/nash/security/nash-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/nash-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/nash/security/nash-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nash-domain-security.yml
- group: design
  href: https://artifacts.apis.io/nash/components/nash-components.yml
  title: ''
  type: Components
  url: components/nash-components.yml
- group: agent
  href: https://artifacts.apis.io/nash/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Nash is an AI-powered last-mile delivery orchestration platform that lets retailers, restaurants, grocers, pharmacies, and logistics teams quote, dispatch, and track deliveries across a network of third-party couriers and their own internal fleets from a single API. The Nash Platform API covers orders, jobs (deliveries), quoting, dispatch strategies, route optimization, delivery windows, zones, store locations, shifts, store catalog, notifications, and signed webhooks, alongside a Fleet API for owned-fleet delivery reporting and a Nash Agent copilot exposed over a Model Context Protocol (MCP) server for agent-driven delivery operations. Backed by a16z.
finops:
- has_sources: true
  method: derived
  name: Nash Finops
  primary_unit: ''
  service_category: ''
  slug: nash-finops
  template: true
image: https://www.nash.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Nash MCP Server
  slug: nash
modified: '2026-07-20'
name: Nash
nav: Providers
network: true
overview: 'Nash publishes 30 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI Functions API, Annotate API, Batch Job API, and 27 more. Tagged areas include Company, Delivery, Last Mile Delivery, Logistics, and Dispatch.


  The Nash catalog on APIs.io includes 2 event-driven AsyncAPI specifications and 1 Spectral governance ruleset.


  Nash''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, changelog, and 27 more developer resources.'
plans:
- name: Nash Plans Pricing
  plan_count: 0
  slug: nash-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Nash Rate Limits
  slug: nash-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Nash API Rules
  rule_count: 59
  severity_counts:
    error: 44
    hint: 0
    info: 2
    warn: 13
  slug: nash-rules
score:
  band: strong
  composite: 63.1
  coverage:
    artifact_dirs: 33
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 56.9
    developer_ergonomics: 66.1
    discoverability: 71.7
    operational_transparency: 44.7
  previous_composite: 63.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: first-party
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
    score: 61.1
screenshot: https://apis.io/screenshots/nash/nash-2026-08-07T184639.png
security:
- kind: authentication
  name: Nash Authentication
  slug: nash-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nash Domain Security
  slug: nash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nash Vulnerability Disclosure
  slug: nash-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Nash Trust Center
  slug: nash-trust-center
  summary_line: SOC 2
skill_count: 3
skills:
- name: Create and dispatch a Nash delivery order
  slug: nash-create-and-dispatch-order
- name: Report a Nash delivery incident and track a refund
  slug: nash-report-incident-and-refund
- name: Schedule a Nash order into a delivery window
  slug: nash-schedule-delivery-window
slug: nash
tags:
- Company
- Delivery
- Last Mile Delivery
- Logistics
- Dispatch
- Route Optimization
- Fleet Management
- Couriers
- Shipping
- Order
- Webhook
- AI Agents
website: https://www.nash.ai
---
