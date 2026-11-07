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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Veho Agentic Access
  operation_count: 26
  slug: veho-agentic-access
  summary_line: 26 operations · 14 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.shipveho.com/v2
  baseurl_source: declared
  description: Labels
  name: Veho Labels API
  slug: veho-labels-api
- baseURL: https://api.shipveho.com/v2
  baseurl_source: declared
  description: Manifests
  name: Veho Manifests API
  slug: veho-manifests-api
- baseURL: https://api.shipveho.com/v2
  baseurl_source: declared
  description: Merchants
  name: Veho Merchants API
  slug: veho-merchants-api
- baseURL: https://api.shipveho.com/v2
  baseurl_source: declared
  description: Orders
  name: Veho Orders API
  slug: veho-orders-api
- baseURL: https://api.shipveho.com/v2
  baseurl_source: declared
  description: Packages
  name: Veho Packages API
  slug: veho-packages-api
- baseURL: https://api.shipveho.com/v2
  baseurl_source: declared
  description: Quotes
  name: Veho Quotes API
  slug: veho-quotes-api
- baseURL: https://api.shipveho.com/v2
  baseurl_source: declared
  description: Webhooks
  name: Veho Webhooks API
  slug: veho-webhooks-api
- baseURL: https://api.shipveho.com/v2
  baseurl_source: declared
  description: Serviceable Zips
  name: Veho Zips API
  slug: veho-zips-api
artifact_total: 36
asyncapis:
- description: ''
  name: Veho Webhooks
  slug: veho-webhooks
collections:
- collection_type: open
  name: Veho labels API
  slug: open-veho-labels-api
- collection_type: open
  name: Veho labels manifests API
  slug: open-veho-manifests-api
- collection_type: open
  name: Veho labels merchants API
  slug: open-veho-merchants-api
- collection_type: open
  name: Veho labels orders API
  slug: open-veho-orders-api
- collection_type: open
  name: Veho labels packages API
  slug: open-veho-packages-api
- collection_type: open
  name: Veho labels quotes API
  slug: open-veho-quotes-api
- collection_type: open
  name: Veho labels webhooks API
  slug: open-veho-webhooks-api
- collection_type: open
  name: Veho labels zips API
  slug: open-veho-zips-api
common:
- group: other
  href: https://artifacts.apis.io/veho/capabilities/veho-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/veho-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.shipveho.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.shipveho.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.shipveho.com/docs/veho-api/j2rbld9w9jm76-introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.shipveho.com/docs/veho-api/e777wryv1msks-veho-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.shipveho.com/docs/veho-api/j2rbld9w9jm76-introduction
- group: operate
  title: ''
  type: Support
  url: https://www.shipveho.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.shipveho.com/resource-center
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/veho-technologies
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shipveho.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shipveho.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.shipveho.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.shipveho.com/security
- group: operate
  href: https://artifacts.apis.io/veho/changelog/veho-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/veho-changelog.yml
- group: design
  href: https://artifacts.apis.io/veho/lifecycle/veho-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/veho-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/veho/lifecycle/veho-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/veho-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/veho/asyncapi/veho-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/veho-webhooks.yml
- group: design
  href: https://artifacts.apis.io/veho/conventions/veho-conventions.yml
  title: ''
  type: Conventions
  url: conventions/veho-conventions.yml
- group: design
  href: https://artifacts.apis.io/veho/errors/veho-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/veho-problem-types.yml
- group: start
  href: https://artifacts.apis.io/veho/sandbox/veho-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/veho-sandbox.yml
- group: design
  href: https://artifacts.apis.io/veho/conformance/veho-conformance.yml
  title: ''
  type: Conformance
  url: conformance/veho-conformance.yml
- group: build
  href: https://artifacts.apis.io/veho/packages/veho-packages.yml
  title: ''
  type: Packages
  url: packages/veho-packages.yml
- group: agent
  href: https://artifacts.apis.io/veho/mcp/veho-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/veho-mcp.yml
- group: agent
  href: https://artifacts.apis.io/veho/llms/veho-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/veho-llms.txt
- group: other
  href: https://artifacts.apis.io/veho/overlays/veho-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/veho-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/veho/data-model/veho-data-model.yml
  title: ''
  type: DataModel
  url: data-model/veho-data-model.yml
- group: design
  href: https://artifacts.apis.io/veho/components/veho-components.yml
  title: ''
  type: Components
  url: components/veho-components.yml
- group: agent
  href: https://artifacts.apis.io/veho/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/veho/agentic-access/veho-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/veho-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/veho/security/veho-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/veho-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/veho/security/veho-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/veho-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/veho/security/veho-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/veho-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/veho/authentication/veho-authentication.yml
  title: ''
  type: Authentication
  url: authentication/veho-authentication.yml
created: '2026-07-17'
description: Veho is a US last-mile delivery and returns carrier built for e-commerce brands, pairing a crowdsourced driver network with purpose-built logistics software. The Veho API (Version 2) is a REST/JSON API for shippers and 3PLs to create delivery orders, manage packages and shipping labels (PDF/PNG/ZPL), quote rates, check serviceable ZIP codes, manage merchants under a client account, and subscribe to 22 package milestone webhook event types, with a full sandbox environment and bulk manifest uploads over S3 or SFTP.
image: https://cdn.prod.website-files.com/64a643946cb644441bae82c9/64a652f0e51e8362078cfd2e_Group%2055.svg
json_schemas:
- name: ErrorResponse
  property_count: 3
  slug: veho-error-response
- name: MerchantResponse
  property_count: 3
  slug: veho-merchant
- name: OrderRequest
  property_count: 16
  slug: veho-order-request
- name: OrderResponse
  property_count: 21
  slug: veho-order
- name: PackageResponse
  property_count: 34
  slug: veho-package
- name: SimpleQuoteRequest
  property_count: 5
  slug: veho-quote-request
- name: WebhookConfigurationRequest
  property_count: 4
  slug: veho-webhook-configuration-request
- name: WebhookEvent
  property_count: 14
  slug: veho-webhook-event
layout: provider
modified: '2026-07-21'
name: Veho
nav: Providers
network: true
overview: 'Veho publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Labels API, Manifests API, Merchants API, and 5 more. Tagged areas include Company, Logistics, Shipping, Last Mile Delivery, and Package Tracking.


  The Veho catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Veho''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, sandbox, and 26 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Veho API Rules
  rule_count: 66
  severity_counts:
    error: 55
    hint: 0
    info: 3
    warn: 8
  slug: veho-rules
score:
  band: strong
  composite: 57.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    contract_governance: 31.8
    contract_quality: 63.4
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 44.7
  previous_composite: 57.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
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
    score: 27.8
screenshot: https://apis.io/screenshots/veho/veho-2026-08-17T082724.png
security:
- kind: authentication
  name: Veho Authentication
  slug: veho-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Veho Domain Security
  slug: veho-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Veho Vulnerability Disclosure
  slug: veho-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Veho Trust Center
  slug: veho-trust-center
  summary_line: ISO 27001
skill_count: 5
skills:
- name: Create a Veho order and download its shipping label
  slug: veho-create-order-and-label
- name: Quote a Veho shipment and check serviceability
  slug: veho-quote-and-serviceability
- name: Subscribe to Veho package events via webhooks
  slug: veho-subscribe-to-package-events
- name: Subscribe to Veho package-milestone webhooks
  slug: veho-subscribe-to-webhooks
- name: Track a Veho package
  slug: veho-track-a-package
slug: veho
tags:
- Company
- Logistics
- Shipping
- Last Mile Delivery
- Package Tracking
- E-Commerce
- Webhook
- Delivery
website: https://www.shipveho.com/
---
