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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Rekki Agentic Access
  operation_count: 32
  slug: rekki-agentic-access
  summary_line: 32 operations · 27 acting
api_count: 1
apis:
- baseURL: https://api.rekki.com
  baseurl_source: declared
  description: The catalog API from REKKI — 12 operation(s) for catalog.
  name: REKKI catalog API
  slug: rekki-catalog-api
- baseURL: https://api.rekki.com
  baseurl_source: declared
  description: The connect_customers API from REKKI — 2 operation(s) for connect_customers.
  name: REKKI connect_customers API
  slug: rekki-connect-customers-api
- baseURL: https://api.rekki.com
  baseurl_source: declared
  description: The general API from REKKI — 2 operation(s) for general.
  name: REKKI general API
  slug: rekki-general-api
- baseURL: https://api.rekki.com
  baseurl_source: declared
  description: The order-guide API from REKKI — 1 operation(s) for order-guide.
  name: REKKI order-guide API
  slug: rekki-order-guide-api
- baseURL: https://api.rekki.com
  baseurl_source: declared
  description: The orders API from REKKI — 11 operation(s) for orders.
  name: REKKI orders API
  slug: rekki-orders-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rekki.com Supplier catalog API
  slug: open-rekki-catalog-api
- collection_type: open
  name: Rekki.com Supplier catalog connect_customers API
  slug: open-rekki-connect-customers-api
- collection_type: open
  name: Rekki.com Supplier catalog general API
  slug: open-rekki-general-api
- collection_type: open
  name: Rekki.com Supplier catalog order-guide API
  slug: open-rekki-order-guide-api
- collection_type: open
  name: Rekki.com Supplier catalog orders API
  slug: open-rekki-orders-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/rekki-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://rekki.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://rekki.com/suppliers
- group: operate
  title: ''
  type: Support
  url: https://rekki.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rekki.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tandc.rekki.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rekki
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/rekki/supplier-api
- group: docs
  title: ''
  type: APIReference
  url: https://api.rekki.com/swagger/index.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/rekki-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rekki-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rekki-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/rekki-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rekki-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rekki-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rekki-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/rekki-supplier-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/rekki-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rekki-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rekki-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rekki-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rekki-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: REKKI is a food wholesale ordering platform that connects restaurants and chefs (buyers) with their suppliers. Restaurants place orders through the REKKI app, and suppliers receive, confirm, and fulfil them. REKKI publishes a public Supplier API that lets suppliers programmatically manage their product catalog (items, inventory, price lists), receive and confirm orders, report integration status back to REKKI, and manage REKKI Connect customers and their order guides. Authentication uses a supplier bearer token plus an X-REKKI-Authorization-Type header. REKKI's current product suite also includes AI agents for wholesale distributors (OrderAI, InboxAI, MenuAI) and a Marketplace. REKKI was surfaced as a portfolio company of Creandum and Point Nine.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rekki.png
layout: provider
modified: '2026-07-21'
name: REKKI
nav: Providers
network: true
overview: 'REKKI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including catalog API, connect_customers API, general API, and 2 more. Tagged areas include Company, Food, Wholesale, Ordering, and Restaurant.


  REKKI''s developer surface includes getting-started guide, support, documentation, API reference, authentication, and 18 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 51.6
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rekki/refs/heads/main/screenshots/rekki-2026-09-02T153301.png
security:
- kind: authentication
  name: Rekki Authentication
  slug: rekki-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rekki Domain Security
  slug: rekki-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: rekki
tags:
- Company
- Food
- Wholesale
- Ordering
- Restaurant
- Supply Chain
- Catalog
- Order
- E-Commerce
website: https://rekki.com/
---
