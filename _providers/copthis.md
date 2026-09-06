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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.partner.example.com/v1
  baseurl_source: declared
  description: Order previews, creation, tracking, address updates, and cancellation.
  name: CopThis Orders API
  slug: copthis-orders-api
- baseURL: https://api.partner.example.com/v1
  baseurl_source: declared
  description: Partner stores (typically one per artist) and their merchandise.
  name: CopThis Stores API
  slug: copthis-stores-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Merchbar Partner Orders API
  slug: open-copthis-orders-api
- collection_type: open
  name: Merchbar Partner Orders Stores API
  slug: open-copthis-stores-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/copthis-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/copthis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://merchbar.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/CopThis/partner-api/blob/master/partner_api.md
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/CopThis/partner-api/blob/master/partner_api.md#api-endpoints
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CopThis
- group: auth
  title: ''
  type: Authentication
  url: authentication/copthis-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/copthis-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/copthis-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/copthis-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/copthis-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/copthis-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/copthis-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/copthis-partner-api-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/copthis-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/copthis-llms.txt
created: '2026-07-17'
description: CopThis is the company behind Merchbar, the official online merchandise retailer for musicians and artists, selling authenticated band and artist merch (vinyl, apparel, accessories) across thousands of artist stores. CopThis operates the Merchbar Partner API — a REST contract that merchandise and fulfillment partners implement so Merchbar can list a partner's stores and merchandise and place, track, update, and cancel orders on behalf of Merchbar customers. The API uses HTTP Basic authentication over HTTPS, a JSON envelope with a top-level data key and pagination for collections, URI-path versioning (v1), and an error envelope for 4xx/5xx responses. CopThis is a portfolio company of 500 Global.
image: https://merchbar.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: CopThis
nav: Providers
network: true
overview: 'CopThis publishes 2 APIs on the [APIs.io](https://apis.io/) network: Orders API and Stores API. Tagged areas include Company, Music, Merchandise, E-Commerce, and Retail.


  CopThis'' developer surface includes documentation, API reference, authentication, and 14 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 56.7
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 29.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/copthis/refs/heads/main/screenshots/copthis-2026-07-25T210411.png
security:
- kind: authentication
  name: Copthis Authentication
  slug: copthis-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Copthis Domain Security
  slug: copthis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: copthis
tags:
- Company
- Music
- Merchandise
- E-Commerce
- Retail
- Order
- Fulfillment
- Partner API
- Marketplace
website: https://merchbar.com
---
