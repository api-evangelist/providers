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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://sandbox.nory.ai/app/v1
  baseurl_source: declared
  description: The Authorization API from Nory — 1 operation(s) for authorization.
  name: Nory Authorization API
  slug: nory-authorization-api
- baseURL: https://sandbox.nory.ai/app/v1
  baseurl_source: declared
  description: The Branch API from Nory — 1 operation(s) for branch.
  name: Nory Branch API
  slug: nory-branch-api
- baseURL: https://sandbox.nory.ai/app/v1
  baseurl_source: declared
  description: The Brands API from Nory — 1 operation(s) for brands.
  name: Nory Brands API
  slug: nory-brands-api
- baseURL: https://sandbox.nory.ai/app/v1
  baseurl_source: declared
  description: The Employee Punch API from Nory — 2 operation(s) for employee punch.
  name: Nory Employee Punch API
  slug: nory-employee-punch-api
- baseURL: https://sandbox.nory.ai/app/v1
  baseurl_source: declared
  description: The Integration API from Nory — 1 operation(s) for integration.
  name: Nory Integration API
  slug: nory-integration-api
- baseURL: https://sandbox.nory.ai/app/v1
  baseurl_source: declared
  description: The Inventory API from Nory — 4 operation(s) for inventory.
  name: Nory Inventory API
  slug: nory-inventory-api
- baseURL: https://sandbox.nory.ai/app/v1
  baseurl_source: declared
  description: The Inventory Orders API from Nory — 2 operation(s) for inventory orders.
  name: Nory Inventory Orders API
  slug: nory-inventory-orders-api
- baseURL: https://sandbox.nory.ai/app/v1
  baseurl_source: declared
  description: The Location Settings API from Nory — 1 operation(s) for location settings.
  name: Nory Location Settings API
  slug: nory-location-settings-api
- baseURL: https://sandbox.nory.ai/app/v1
  baseurl_source: declared
  description: The Refresh token API from Nory — 1 operation(s) for refresh token.
  name: Nory Refresh token API
  slug: nory-refresh-token-api
- baseURL: https://sandbox.nory.ai/app/v1
  baseurl_source: declared
  description: The Templates API from Nory — 5 operation(s) for templates.
  name: Nory Templates API
  slug: nory-templates-api
artifact_total: 15
common:
- group: other
  href: https://artifacts.apis.io/nory/capabilities/nory-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/nory-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://nory.ai/
- group: start
  title: ''
  type: Login
  url: https://app.nory.ai/
- group: company
  title: ''
  type: Blog
  url: https://nory.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://nory.ai/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nory.ai/legal/terms-privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nory.ai/legal/terms-and-conditions
- group: docs
  href: https://artifacts.apis.io/nory/openapi/_original/nory-middleware-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/nory-middleware-openapi.json
- group: other
  href: https://artifacts.apis.io/nory/overlays/nory-middleware-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nory-middleware-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/nory/authentication/nory-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nory-authentication.yml
- group: design
  href: https://artifacts.apis.io/nory/errors/nory-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nory-problem-types.yml
- group: design
  href: https://artifacts.apis.io/nory/conventions/nory-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nory-conventions.yml
- group: design
  href: https://artifacts.apis.io/nory/data-model/nory-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nory-data-model.yml
- group: agent
  href: https://artifacts.apis.io/nory/mcp/nory-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nory-mcp.yml
- group: design
  href: https://artifacts.apis.io/nory/conformance/nory-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nory-conformance.yml
- group: design
  href: https://artifacts.apis.io/nory/lifecycle/nory-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nory-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/nory/sandbox/nory-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/nory-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/nory/well-known/nory-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nory-well-known.yml
- group: auth
  href: https://artifacts.apis.io/nory/security/nory-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nory-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/nory/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/nory/llms/nory-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nory-llms.txt
created: '2026-07-17'
description: Nory is an AI-powered restaurant management platform (an "agentic AI restaurant operating system") founded in Ireland in 2019 by Conor Sheridan. It unifies business intelligence, inventory, workforce scheduling and payroll into one control centre, using real-time data and predictive AI (demand-based ordering, live P&L, labour forecasting) to cut food waste and labour cost across single-site and multi-location restaurant groups. Nory connects to POS and hospitality systems such as Toast, Lightspeed, Square, SumUp, Vita Mojo, Clover, Zonal, Revel, Oracle Micros and Shift4, and exposes a partner-facing Middleware API (published as a Swagger 2.0 sandbox definition) covering brands, branches, inventory counts/deliveries/suppliers, AI recommended purchase orders, employee punch/labour data, location settings and scheduling templates. Nory raised a $37M Series B in 2025 and is backed by Accel.
image: https://nory.ai/favicon.ico
layout: provider
modified: '2026-07-20'
name: Nory
nav: Providers
network: true
overview: 'Nory publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authorization API, Branch API, Brands API, and 7 more. Tagged areas include Company, Restaurant, Hospitality, Inventory, and Workforce.


  The Nory catalog on APIs.io includes 1 Spectral governance ruleset.


  Nory''s developer surface includes engineering blog, support, authentication, sandbox, and 17 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Nory API Rules
  rule_count: 51
  severity_counts:
    error: 45
    hint: 0
    info: 4
    warn: 2
  slug: nory-rules
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 43.5
    developer_ergonomics: 35.1
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 31.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/nory/nory-2026-08-07T185535.png
security:
- kind: authentication
  name: Nory Authentication
  slug: nory-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nory Domain Security
  slug: nory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Ingest items and record an inventory count
  slug: nory-inventory-count
- name: Generate and accept a recommended purchase order
  slug: nory-recommended-order
slug: nory
tags:
- Company
- Restaurant
- Hospitality
- Inventory
- Workforce
- Payroll
- Point-of-Sale
- Artificial Intelligence
- Food and Beverage
website: https://nory.ai/
---
