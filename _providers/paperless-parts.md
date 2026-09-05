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
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-09-04'
api_count: 4
apis:
- baseURL: https://api.paperlessparts.com/v2
  baseurl_source: declared
  description: Paperless Parts includes Customer Relationship Management (CRM) functionality to make it easy to send quotes to new and existing customers, while keeping data consistent with third-party CRM and ERP s
  name: Paperless Parts Contacts API
  slug: paperless-parts-contacts-api
- baseURL: https://api.paperlessparts.com/v2
  baseurl_source: declared
  description: Endpoints for managing custom tables used by Operations to compute pricing.
  name: Paperless Parts Custom Tables API
  slug: paperless-parts-custom-tables-api
- baseURL: https://api.paperlessparts.com/v2
  baseurl_source: declared
  description: Paperless Parts includes Customer Relationship Management (CRM) functionality to make it easy to send quotes to new and existing customers, while keeping data consistent with third-party CRM and ERP s
  name: Paperless Parts Customers API
  slug: paperless-parts-customers-api
- baseURL: https://api.paperlessparts.com/v2
  baseurl_source: declared
  description: Endpoints for viewing communications between Paperless Parts and ERP integrations
  name: Paperless Parts Events API
  slug: paperless-parts-events-api
- baseURL: https://api.paperlessparts.com/v2
  baseurl_source: declared
  description: Endpoints for interacting with ERP integrations
  name: Paperless Parts Integration Actions API
  slug: paperless-parts-integration-actions-api
- baseURL: https://api.paperlessparts.com/v2
  baseurl_source: declared
  description: Endpoints for managing Jobs
  name: Paperless Parts Jobs API
  slug: paperless-parts-jobs-api
- baseURL: https://api.paperlessparts.com/v2
  baseurl_source: declared
  description: Endpoints for identifying newly placed orders and pulling all information related to a particular order. Also, a new order can be created via open API to turn an existing quote into order.
  name: Paperless Parts Orders API
  slug: paperless-parts-orders-api
- baseURL: https://api.paperlessparts.com/v2
  baseurl_source: declared
  description: Endpoints for managing Parts
  name: Paperless Parts Parts API
  slug: paperless-parts-parts-api
- baseURL: https://api.paperlessparts.com/v2
  baseurl_source: declared
  description: Endpoints for managing Processes, Operation Definitions, and Add on Definitions
  name: Paperless Parts Processes API
  slug: paperless-parts-processes-api
- baseURL: https://api.paperlessparts.com/v2
  baseurl_source: declared
  description: Endpoints for managing purchased components and purchased components columns.
  name: Paperless Parts Purchased Components API
  slug: paperless-parts-purchased-components-api
- baseURL: https://api.paperlessparts.com/v2
  baseurl_source: declared
  description: Endpoints for creating and managing line items on a quote.
  name: Paperless Parts Quote Items API
  slug: paperless-parts-quote-items-api
- baseURL: https://api.paperlessparts.com/v2
  baseurl_source: declared
  description: Endpoints for identifying newly sent quotes, pulling all information related to a particular quote, and updating a quote's status.
  name: Paperless Parts Quotes API
  slug: paperless-parts-quotes-api
artifact_total: 18
asyncapis:
- description: ''
  name: Paperless Parts Events
  slug: paperless-parts-events
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/part-os/core-python/blob/master/LICENSE
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/paperless-parts-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/paperless-parts-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/paperless-parts-v1-overlay.yaml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/paperless-parts-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.paperlessparts.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.paperlessparts.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paperlessparts.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.paperlessparts.com/v2
- group: start
  title: ''
  type: GettingStarted
  url: https://help.paperlessparts.com/s/article/integration-development-guide
- group: operate
  title: ''
  type: Support
  url: https://help.paperlessparts.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.paperlessparts.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/part-os
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paperlessparts.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.paperlessparts.com/demo/
- group: start
  title: ''
  type: Login
  url: https://app.paperlessparts.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.paperlessparts.com/s/article/general-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paperlessparts.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.paperlessparts.com/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.paperlessparts.com/product-updates/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paperless-parts-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/paperless-parts-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/paperless-parts-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/paperless-parts-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paperless-parts-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/paperless-parts-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/paperless-parts-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paperless-parts-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/paperless-parts-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/paperless-parts-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paperless-parts-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/paperless-parts-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paperless-parts-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://www.paperlessparts.com/vulnerability-disclosure-policy/
- group: other
  title: ''
  type: Events
  url: asyncapi/paperless-parts-events.yml
- group: agent
  title: ''
  type: MCP
  url: mcp/paperless-parts-mcp.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/part-os/core-python
created: '2026-08-26'
description: Paperless Parts, Inc. is a Boston-based manufacturing software company founded in 2017 that builds a secure, ITAR-compliant cloud quoting and sales platform for custom part manufacturers — job shops, contract manufacturers and rapid-prototype businesses working in CNC machining, sheet metal fabrication, Swiss screw machining, wire EDM, waterjet and additive manufacturing. A patented geometry engine analyses uploaded CAD to automate costing, and the P3L pricing language lets a shop encode its own pricing logic. The company publishes a public REST API in two live versions (v1 and v2) at api.paperlessparts.com, covering quotes, quote items, orders, jobs, parts, processes, contacts and accounts, custom pricing tables, purchased components, and a managed integrations framework with a poll-based Streaming API for reacting to platform events. A first-party Python SDK is published on GitHub under the part-os organization.
image: https://paperlessparts.com/wp-content/uploads/paperless-parts-full-logo-2022.svg
layout: provider
modified: '2026-08-26'
name: Paperless Parts
nav: Providers
network: true
overview: 'Paperless Parts publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Custom Tables API, Customers API, and 9 more. Tagged areas include Company, Manufacturing, Quoting, CNC Machining, and Sheet Metal.


  The Paperless Parts catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Paperless Parts'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Paperless Parts Plans Pricing
  plan_count: 0
  slug: paperless-parts-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Paperless Parts Rate Limits
  slug: paperless-parts-rate-limits
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 64.1
    developer_ergonomics: 49.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 50.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paperless-parts/refs/heads/main/screenshots/paperless-parts-2026-09-02T150907.png
security:
- kind: authentication
  name: Paperless Parts Authentication
  slug: paperless-parts-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Paperless Parts Domain Security
  slug: paperless-parts-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Paperless Parts Vulnerability Disclosure
  slug: paperless-parts-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: paperless-parts
tags:
- Company
- Manufacturing
- Quoting
- CNC Machining
- Sheet Metal
- ERP
- CRM
- Job Shops
- Aerospace and Defense
- Pricing
- Estimating
- Industrial
website: https://www.paperlessparts.com/
---
