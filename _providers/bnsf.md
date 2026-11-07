---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 35
  human_in_the_loop: 3
  name: Bnsf Agentic Access
  operation_count: 59
  slug: bnsf-agentic-access
  summary_line: 59 operations · 35 acting · 3 human-in-the-loop
api_count: 16
apis:
- baseURL: https://api.bnsf.com:6443
  baseurl_source: declared
  description: The AUTOMOTIVE API from BNSF — 4 operation(s) for automotive.
  name: BNSF AUTOMOTIVE API
  slug: bnsf-automotive-api
- baseURL: https://api.bnsf.com:6443
  baseurl_source: declared
  description: The CARLOAD API from BNSF — 3 operation(s) for carload.
  name: BNSF CARLOAD API
  slug: bnsf-carload-api
- baseURL: https://api.bnsf.com:6443
  baseurl_source: declared
  description: The INTERMODAL API from BNSF — 2 operation(s) for intermodal.
  name: BNSF INTERMODAL API
  slug: bnsf-intermodal-api
- baseURL: https://api.bnsf.com:6443
  baseurl_source: declared
  description: The Requests API from BNSF — 41 operation(s) for requests.
  name: BNSF Requests API
  slug: bnsf-requests-api
- baseURL: https://api.bnsf.com:6443
  baseurl_source: declared
  description: The TRAINS API from BNSF — 4 operation(s) for trains.
  name: BNSF TRAINS API
  slug: bnsf-trains-api
artifact_total: 19
asyncapis:
- description: ''
  name: Bnsf Webhooks
  slug: bnsf-webhooks
common:
- group: other
  href: https://artifacts.apis.io/bnsf/capabilities/bnsf-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bnsf-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/bnsf/overlays/bnsf-trace-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bnsf-trace-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bnsf/overlays/bnsf-intermodal-hub-operations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bnsf-intermodal-hub-operations-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bnsf/overlays/bnsf-automotive-hub-operations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bnsf-automotive-hub-operations-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bnsf/overlays/bnsf-prices-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bnsf-prices-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bnsf/overlays/bnsf-schedules-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bnsf-schedules-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bnsf/overlays/bnsf-waybill-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bnsf-waybill-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bnsf/overlays/bnsf-reference-files-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bnsf-reference-files-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bnsf/overlays/bnsf-diagnostics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bnsf-diagnostics-overlay.yaml
- group: docs
  href: https://artifacts.apis.io/bnsf/openapi/_original/bnsf-trace-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/bnsf-trace-openapi.yml
- group: auth
  href: https://artifacts.apis.io/bnsf/authentication/bnsf-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bnsf-authentication.yml
- group: design
  href: https://artifacts.apis.io/bnsf/conventions/bnsf-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bnsf-conventions.yml
- group: design
  href: https://artifacts.apis.io/bnsf/errors/bnsf-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bnsf-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bnsf/lifecycle/bnsf-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bnsf-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bnsf/conformance/bnsf-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bnsf-conformance.yml
- group: design
  href: https://artifacts.apis.io/bnsf/data-model/bnsf-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bnsf-data-model.yml
- group: operate
  href: https://artifacts.apis.io/bnsf/rate-limits/bnsf-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bnsf-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bnsf/plans/bnsf-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bnsf-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/bnsf/sandbox/bnsf-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/bnsf-sandbox.yml
- group: design
  href: https://artifacts.apis.io/bnsf/asyncapi/bnsf-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bnsf-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/bnsf/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/bnsf/llms/bnsf-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bnsf-llms.txt
- group: agent
  href: https://artifacts.apis.io/bnsf/mcp/bnsf-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bnsf-mcp.yml
- group: build
  href: https://artifacts.apis.io/bnsf/packages/bnsf-packages.yml
  title: ''
  type: Packages
  url: packages/bnsf-packages.yml
- group: auth
  href: https://artifacts.apis.io/bnsf/security/bnsf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bnsf-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/bnsf/agentic-access/bnsf-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bnsf-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/bnsf/finops/bnsf-finops.yml
  title: ''
  type: FinOps
  url: finops/bnsf-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.bnsf.com
- group: start
  title: ''
  type: Portal
  url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/catalog/
- group: docs
  title: ''
  type: APIReference
  url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/developers-console/
- group: start
  title: ''
  type: Console
  url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/developers-console/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/getting-started/
- group: start
  title: ''
  type: SignUp
  url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/registration/
- group: operate
  title: ''
  type: Support
  url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/support/
- group: start
  title: ''
  type: Login
  url: https://customer2.bnsf.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bnsf.com/news-media/railtalk/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bnsf.com/site-terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bnsf.com/privacy-policy.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bnsf-railway
created: '2025-02-06'
description: 'BNSF Railway, a subsidiary of Berkshire Hathaway Inc., operates one of the largest freight rail networks in North America — more than 32,000 route miles across 28 states and three Canadian provinces, connecting to Mexico through rail lines in Texas. BNSF publishes a genuine customer-facing API programme: eight OpenAPI 3.0 documents totalling 59 operations covering shipment tracing, intermodal and automotive hub gate operations, freight pricing and invoices, intermodal schedules, waybill management, rail reference data and diagnostics, plus a six-event webhook push surface. Every call is authenticated with certificate-based mutual TLS on port 6443; there is no API key and no OAuth, and 27 of the 59 operations are Restricted Services requiring separate authorisation.'
finops:
- has_sources: true
  method: derived
  name: Bnsf Finops
  primary_unit: ''
  service_category: ''
  slug: bnsf-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bnsf.png
layout: provider
modified: '2026-09-16'
name: BNSF
nav: Providers
network: true
overview: 'BNSF publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including AUTOMOTIVE API, CARLOAD API, INTERMODAL API, and 2 more. Tagged areas include Freight, Railroad, Rail, Shipping, and Trains.


  The BNSF catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  BNSF''s developer surface includes authentication, sandbox, developer portal, documentation, API reference, developer console, getting-started guide, and 34 more developer resources.'
plans:
- name: Bnsf Plans Pricing
  plan_count: 0
  slug: bnsf-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Bnsf Rate Limits
  slug: bnsf-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: BNSF API Rules
  rule_count: 51
  severity_counts:
    error: 39
    hint: 0
    info: 2
    warn: 10
  slug: bnsf-rules
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 34.2
    contract_governance: 31.8
    contract_quality: 50.0
    developer_ergonomics: 66.1
    discoverability: 78.6
    operational_transparency: 39.5
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 80.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bnsf/bnsf-2026-06-20T173544.png
security:
- kind: authentication
  name: Bnsf Authentication
  slug: bnsf-authentication
  summary_line: mutualTLS · 2 schemes
- kind: domain-security
  name: Bnsf Domain Security
  slug: bnsf-domain-security
  summary_line: TLSv1.2 · DMARC
skill_count: 6
skills:
- name: bnsf-intermodal-gate-flow
  slug: bnsf-intermodal-gate-flow
- name: bnsf-price-rate-and-invoice-lookup
  slug: bnsf-price-rate-and-invoice-lookup
- name: bnsf-resolve-rail-reference-codes
  slug: bnsf-resolve-rail-reference-codes
- name: bnsf-submit-and-retrieve-a-waybill
  slug: bnsf-submit-and-retrieve-a-waybill
- name: bnsf-trace-a-carload-shipment
  slug: bnsf-trace-a-carload-shipment
- name: bnsf-trace-intermodal-and-automotive
  slug: bnsf-trace-intermodal-and-automotive
slug: bnsf
tags:
- Freight
- Railroad
- Rail
- Shipping
- Trains
- Intermodal
- Logistics
- Supply Chain
- Transportation
website: https://www.bnsf.com
---
