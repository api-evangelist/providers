---
access_model:
  confidence: high
  label: Enterprise, contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.noosh.com/pricing/
  - https://nooshauth.noosh.com/login
  - https://www.noosh.com/contact/
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Noosh Agentic Access
  operation_count: 107
  slug: noosh-agentic-access
  summary_line: 107 operations · 29 acting
api_count: 1
apis:
- description: The Noosh API is the integration surface behind Noosh's marketing-execution platform — the API Noosh's own partners page credits for "over 60 integrations to enterprise software systems". It is publis
  name: Noosh API
  slug: noosh-api
artifact_total: 6
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/noosh-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/noosh-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://noosh.com/
- group: operate
  title: ''
  type: Support
  url: https://noosh.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://stats.pingdom.com/qcecd0tzzhpr/667653
- group: company
  title: ''
  type: Blog
  url: https://www.noosh.com/resources/
- group: start
  title: ''
  type: Login
  url: https://nooshauth.noosh.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.noosh.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.noosh.com/terms-of-service/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/noosh-domain-security.yml
- group: docs
  title: ''
  type: APIReference
  url: https://api.noosh.com/api/developer/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://api.noosh.com/api/developer/index.html
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.noosh.com/hc/en-us
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/noosh-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/noosh-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/noosh-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/noosh-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/noosh-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/noosh-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/noosh-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/noosh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/noosh-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/noosh-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/noosh-openapi-overlay.yaml
created: '2026-07-17'
description: Noosh is a marketing execution and print/procurement management platform that gives enterprise marketing teams visibility and control over campaigns spanning direct mail, print, and point-of-sale (POS) materials. The software coordinates collaborative marketing workflows, agency and supplier performance tracking, vendor diversity management, and cost, quality, time, and sustainability data, and integrates with procurement and other enterprise systems. Noosh publishes a public, machine-readable Swagger 2.0 contract for the Noosh API at api.noosh.com — 86 paths, 107 operations and 214 schema definitions covering projects, specs, RFQs, quotes, estimates, buy and sell orders, shipments, invoices, files, tasks, time cards and workgroups — with a Swagger UI as its only documentation surface. There is no developer portal, no SDK in any registry, no published pricing and no rate limits; authentication is HTTP Basic and every route is customer-credentialed. Noosh was surfaced as a portfolio
  company of Accel and profiled in the API Evangelist network.
image: https://www.noosh.com/wp-content/uploads/2021/03/noosh-logo.png
layout: provider
modified: '2026-08-13'
name: Noosh
nav: Providers
network: true
overview: 'Noosh publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Marketing Execution, Procurement, and Print.


  Noosh''s developer surface includes authentication, support, engineering blog, API reference, documentation, changelog, and 19 more developer resources.'
plans:
- name: Noosh Plans Pricing
  plan_count: 0
  slug: noosh-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Noosh Rate Limits
  slug: noosh-rate-limits
score:
  band: thin
  composite: 38.1
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 16.7
    contract_quality: 48.3
    developer_ergonomics: 37.5
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 31.6
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/noosh/refs/heads/main/screenshots/noosh-2026-08-07T185512.png
security:
- kind: authentication
  name: Noosh Authentication
  slug: noosh-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Noosh Domain Security
  slug: noosh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: noosh
tags:
- Company
- Marketing
- Marketing Execution
- Procurement
- Print
- Direct Mail
- Workflows
- Sourcing
- Print Procurement
- Project Management
- Supplier Management
- Quotes
- Purchase Orders
- Shipments
- Invoicing
website: https://noosh.com/
---
