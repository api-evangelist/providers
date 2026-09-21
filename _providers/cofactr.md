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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.3
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Cofactr Agentic Access
  operation_count: 4
  slug: cofactr-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- description: 'REST API for the Cofactr platform: BOMs, purchase orders, kits, invoices, and inventory, scoped per organization via org_id, with outbound webhooks for created/updated events.'
  name: Cofactr Platform API
  slug: cofactr-platform-api
- baseURL: https://graph.cofactr.com
  baseurl_source: declared
  description: Execute multiple product queries in a single request. Each batch member is an operation against the products API expressed as a relative URL; members are fulfilled concurrently and returned in order.
  name: Cofactr batch API
  slug: cofactr-batch-api
- baseURL: https://graph.cofactr.com
  baseurl_source: declared
  description: Search, view, and autocomplete electronic component products. Every product is a unique combination of manufacturer (`mfr`) and manufacturer part number (`mpn`), identified by a Cofactr ID (CPID). Pro
  name: Cofactr products API
  slug: cofactr-products-api
arazzos:
- description: Search the Cofactr Knowledge Graph for a part, then view its full detail.
  name: Cofactr — search and view a component
  slug: cofactr-search-and-view-product
artifact_total: 13
asyncapis:
- description: ''
  name: Cofactr Platform Webhooks
  slug: cofactr-platform-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cofactr Knowledge Graph batch API
  slug: open-cofactr-batch-api
- collection_type: open
  name: Cofactr Knowledge Graph batch products API
  slug: open-cofactr-products-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.cofactr.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cofactr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.cofactr.com/collections/5590442793-developer_resources
- group: docs
  title: ''
  type: APIReference
  url: https://graph.cofactr.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://support.cofactr.com/articles/8047618750-developer-center
- group: operate
  title: ''
  type: Support
  url: https://support.cofactr.com/
- group: start
  title: ''
  type: SignUp
  url: https://platform.cofactr.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cofactr.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cofactr.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cofactr
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/authentication/cofactr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cofactr-authentication.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/openapi/_original/cofactr-knowledge-graph-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/cofactr-knowledge-graph-openapi-original.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/overlays/cofactr-knowledge-graph-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cofactr-knowledge-graph-overlay.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/packages/cofactr-packages.yml
  title: ''
  type: Packages
  url: packages/cofactr-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/packages/cofactr-packages.yml
  title: ''
  type: SDKs
  url: packages/cofactr-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/asyncapi/cofactr-platform-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cofactr-platform-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/mcp/cofactr-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cofactr-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/llms/cofactr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cofactr-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/errors/cofactr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cofactr-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/conventions/cofactr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cofactr-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/lifecycle/cofactr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cofactr-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/rate-limits/cofactr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cofactr-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/conformance/cofactr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cofactr-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/data-model/cofactr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cofactr-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/sandbox/cofactr-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cofactr-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/arazzo/cofactr-search-and-view-product.yml
  title: ''
  type: Arazzo
  url: arazzo/cofactr-search-and-view-product.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/agentic-access/cofactr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cofactr-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/security/cofactr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cofactr-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/security/cofactr-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cofactr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cofactr.com/cofactrs-bug-bounty
created: '2026-07-17'
description: 'Cofactr provides electronics supply chain infrastructure for hardware manufacturers — component intelligence, procurement execution, and ITAR-registered warehousing and kitting — so teams avoid shortages and production delays with full traceability. Its developer surface exposes two REST APIs: the Knowledge Graph (Component Cloud) API for searching parts, offers, pricing, and specs, and the Platform API for BOMs, purchase orders, kits, invoices, and inventory, plus outbound webhooks and integrations with NetSuite, SAP, Arena, Altium 365, QuickBooks, and more.'
image: https://cdn.sanity.io/images/fdrwu6gi/production/4ecf7716c98de655cbae16fedb06c8142e446975-600x592.jpg?w=1200&fm=webp
layout: provider
modified: '2026-07-18'
name: Cofactr
nav: Providers
network: true
overview: 'Cofactr publishes 2 APIs on the [APIs.io](https://apis.io/) network: batch API and products API. Tagged areas include Company, Physical AI, Component Intelligence, Electronics, and Supply Chain.


  The Cofactr catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cofactr''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, sandbox, and 24 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 0
  name: Cofactr Rate Limits
  slug: cofactr-rate-limits
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 66.4
    developer_ergonomics: 70.8
    discoverability: 75.9
    operational_transparency: 21.1
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/cofactr/refs/heads/main/screenshots/cofactr-2026-07-25T205951.png
security:
- kind: authentication
  name: Cofactr Authentication
  slug: cofactr-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Cofactr Domain Security
  slug: cofactr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cofactr Vulnerability Disclosure
  slug: cofactr-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: cofactr
tags:
- Company
- Physical AI
- Component Intelligence
- Electronics
- Supply Chain
- Procurement
- Manufacturing
- Hardware
- Bill of Materials
website: https://www.cofactr.com/
---
