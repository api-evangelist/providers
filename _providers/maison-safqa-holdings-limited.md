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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Maison Safqa Holdings Limited Agentic Access
  operation_count: 6
  slug: maison-safqa-holdings-limited-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.maisonsafqa.com/v1
  baseurl_source: declared
  description: Update inventory quantities for product variants. Changes are stored locally and periodically synced to Shopify.
  name: Maison Safqa Holdings Limited Inventory API
  slug: maison-safqa-holdings-limited-inventory-api
- baseURL: https://api.maisonsafqa.com/v1
  baseurl_source: declared
  description: Create, retrieve, and update products. Products are created in draft status and synced to Shopify when activated.
  name: Maison Safqa Holdings Limited Products API
  slug: maison-safqa-holdings-limited-products-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Maison Safqa Brand Developer Inventory API
  slug: open-maison-safqa-holdings-limited-inventory-api
- collection_type: open
  name: Maison Safqa Brand Developer Inventory Products API
  slug: open-maison-safqa-holdings-limited-products-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/capabilities/maison-safqa-holdings-limited-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/maison-safqa-holdings-limited-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/overlays/maison-safqa-holdings-limited-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/maison-safqa-holdings-limited-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.maisonsafqa.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.maisonsafqa.com
- group: operate
  title: ''
  type: Support
  url: mailto:itsupport@maisonsafqa.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.maisonsafqa.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://maisonsafqa.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/authentication/maison-safqa-holdings-limited-authentication.yml
  title: ''
  type: Authentication
  url: authentication/maison-safqa-holdings-limited-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/conventions/maison-safqa-holdings-limited-conventions.yml
  title: ''
  type: Conventions
  url: conventions/maison-safqa-holdings-limited-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/errors/maison-safqa-holdings-limited-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/maison-safqa-holdings-limited-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/rate-limits/maison-safqa-holdings-limited-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/maison-safqa-holdings-limited-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/lifecycle/maison-safqa-holdings-limited-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/maison-safqa-holdings-limited-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/sandbox/maison-safqa-holdings-limited-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/maison-safqa-holdings-limited-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/data-model/maison-safqa-holdings-limited-data-model.yml
  title: ''
  type: DataModel
  url: data-model/maison-safqa-holdings-limited-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/conformance/maison-safqa-holdings-limited-conformance.yml
  title: ''
  type: Conformance
  url: conformance/maison-safqa-holdings-limited-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/well-known/maison-safqa-holdings-limited-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/maison-safqa-holdings-limited-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/llms/maison-safqa-holdings-limited-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/maison-safqa-holdings-limited-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/mcp/maison-safqa-holdings-limited-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/maison-safqa-holdings-limited-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/agentic-access/maison-safqa-holdings-limited-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/maison-safqa-holdings-limited-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/security/maison-safqa-holdings-limited-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/maison-safqa-holdings-limited-domain-security.yml
created: '2026-07-17'
description: Maison Safqa Holdings Limited operates Maison Safqa, a members-only luxury flash-sale marketplace (built on Shopify) offering exclusive time-limited sales on high-end brands. For its partner brands it publishes the Maison Safqa Brand Developer API — an API-key-authenticated REST interface for creating products (single and bulk) and updating inventory levels, which the platform then syncs into Shopify with brand data taking precedence on conflict and prices converted to SAR on ingestion. Surfaced originally as a 500 Global portfolio lead and enriched from the provider's public developer portal.
image: https://cdn.shopify.com/s/files/1/0865/0224/4663/files/logo-ms.svg?v=1763809309
layout: provider
modified: '2026-07-20'
name: Maison Safqa
nav: Providers
network: true
overview: 'Maison Safqa publishes 2 APIs on the [APIs.io](https://apis.io/) network: Holdings Limited Inventory API and Holdings Limited Products API. Tagged areas include Company, Retail, E-Commerce, Luxury, and Marketplace.


  Maison Safqa''s developer surface includes documentation, support, authentication, sandbox, and 17 more developer resources.'
random_paper: 2
rate_limits:
- limit_count: 2
  name: Maison Safqa Holdings Limited Rate Limits
  slug: maison-safqa-holdings-limited-rate-limits
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 50.8
    developer_ergonomics: 63.7
    discoverability: 73.2
    operational_transparency: 21.1
  previous_composite: 39.1
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/screenshots/maison-safqa-holdings-limited-2026-07-25T225926.png
security:
- kind: authentication
  name: Maison Safqa Holdings Limited Authentication
  slug: maison-safqa-holdings-limited-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Maison Safqa Holdings Limited Domain Security
  slug: maison-safqa-holdings-limited-domain-security
  summary_line: TLSv1.3 · DMARC
slug: maison-safqa-holdings-limited
tags:
- Company
- Retail
- E-Commerce
- Luxury
- Marketplace
- Product Catalog
- Inventory
- Shopify
website: https://maisonsafqa.com
---
