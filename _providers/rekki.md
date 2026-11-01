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
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Rekki Agentic Access
  operation_count: 32
  slug: rekki-agentic-access
  summary_line: 32 operations · 23 acting
api_count: 1
apis:
- baseURL: https://api.rekki.com
  baseurl_source: declared
  description: The catalog API from REKKI — 12 operation(s) for catalog.
  name: REKKI Catalog API
  slug: rekki-catalog-api
- baseURL: https://api.rekki.com
  baseurl_source: declared
  description: The connect_customers API from REKKI — 2 operation(s) for connect_customers.
  name: REKKI Connect Customers API
  slug: rekki-connect-customers-api
- baseURL: https://api.rekki.com
  baseurl_source: declared
  description: The general API from REKKI — 2 operation(s) for general.
  name: REKKI General API
  slug: rekki-general-api
- baseURL: https://api.rekki.com
  baseurl_source: declared
  description: The order-guide API from REKKI — 1 operation(s) for order-guide.
  name: REKKI Order Guide API
  slug: rekki-order-guide-api
- baseURL: https://api.rekki.com
  baseurl_source: declared
  description: The orders API from REKKI — 11 operation(s) for orders.
  name: REKKI Orders API
  slug: rekki-orders-api
artifact_total: 15
collections:
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
  href: https://artifacts.apis.io/rekki/capabilities/rekki-capability-edges.yml
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
  href: https://artifacts.apis.io/rekki/authentication/rekki-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rekki-authentication.yml
- group: auth
  href: https://artifacts.apis.io/rekki/security/rekki-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rekki-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/rekki/agentic-access/rekki-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rekki-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/rekki/packages/rekki-packages.yml
  title: ''
  type: Packages
  url: packages/rekki-packages.yml
- group: build
  href: https://artifacts.apis.io/rekki/packages/rekki-packages.yml
  title: ''
  type: SDKs
  url: packages/rekki-packages.yml
- group: agent
  href: https://artifacts.apis.io/rekki/mcp/rekki-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rekki-mcp.yml
- group: agent
  href: https://artifacts.apis.io/rekki/llms/rekki-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rekki-llms.txt
- group: other
  href: https://artifacts.apis.io/rekki/overlays/rekki-supplier-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rekki-supplier-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/rekki/conformance/rekki-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rekki-conformance.yml
- group: design
  href: https://artifacts.apis.io/rekki/errors/rekki-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rekki-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rekki/lifecycle/rekki-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rekki-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/rekki/conventions/rekki-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rekki-conventions.yml
- group: design
  href: https://artifacts.apis.io/rekki/data-model/rekki-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rekki-data-model.yml
- group: agent
  href: https://artifacts.apis.io/rekki/skills/_index.yml
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
overview: 'REKKI publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Catalog API, Connect Customers API, General API, and 2 more. Tagged areas include Company, Food, Wholesale, Ordering, and Restaurant.


  REKKI''s developer surface includes getting-started guide, support, documentation, API reference, authentication, and 18 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 44.0
    developer_ergonomics: 54.2
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 35.3
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rekki/rekki-2026-09-02T153301.png
security:
- kind: authentication
  name: Rekki Authentication
  slug: rekki-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rekki Domain Security
  slug: rekki-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
skill_count: 2
skills:
- name: Process restaurant orders from REKKI
  slug: rekki-process-orders
- name: Sync a supplier catalog to REKKI
  slug: rekki-sync-catalog
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
