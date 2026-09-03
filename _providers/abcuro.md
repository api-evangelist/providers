---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Abcuro Agentic Access
  operation_count: 30
  slug: abcuro-agentic-access
  summary_line: 30 operations
api_count: 1
apis:
- baseURL: https://abcuro.com/wp-json/
  baseurl_source: declared
  description: Job postings.
  name: Abcuro Careers API
  slug: abcuro-careers-api
- baseURL: https://abcuro.com/wp-json/
  baseurl_source: declared
  description: Comment records.
  name: Abcuro Comments API
  slug: abcuro-comments-api
- baseURL: https://abcuro.com/wp-json/
  baseurl_source: declared
  description: Route, type, taxonomy, status and oEmbed discovery.
  name: Abcuro Discovery API
  slug: abcuro-discovery-api
- baseURL: https://abcuro.com/wp-json/
  baseurl_source: declared
  description: Investor records.
  name: Abcuro Investors API
  slug: abcuro-investors-api
- baseURL: https://abcuro.com/wp-json/
  baseurl_source: declared
  description: Media library assets including clinical presentation PDFs.
  name: Abcuro Media API
  slug: abcuro-media-api
- baseURL: https://abcuro.com/wp-json/
  baseurl_source: declared
  description: Static site pages.
  name: Abcuro Pages API
  slug: abcuro-pages-api
- baseURL: https://abcuro.com/wp-json/
  baseurl_source: declared
  description: Leadership, team and board-of-directors records.
  name: Abcuro People API
  slug: abcuro-people-api
- baseURL: https://abcuro.com/wp-json/
  baseurl_source: declared
  description: Abcuro corporate and clinical press releases.
  name: Abcuro Press Releases API
  slug: abcuro-press-releases-api
- baseURL: https://abcuro.com/wp-json/
  baseurl_source: declared
  description: Scientific publications.
  name: Abcuro Publications API
  slug: abcuro-publications-api
- baseURL: https://abcuro.com/wp-json/
  baseurl_source: declared
  description: Cross-type site search.
  name: Abcuro Search API
  slug: abcuro-search-api
- baseURL: https://abcuro.com/wp-json/
  baseurl_source: declared
  description: Categories, tags and the person_role taxonomy.
  name: Abcuro Taxonomy API
  slug: abcuro-taxonomy-api
- baseURL: https://abcuro.com/wp-json/
  baseurl_source: declared
  description: Site author accounts.
  name: Abcuro Users API
  slug: abcuro-users-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Abcuro Content API (WordPress REST) Careers API
  slug: open-abcuro-careers-api
- collection_type: open
  name: Abcuro Content API (WordPress REST) Comments API
  slug: open-abcuro-comments-api
- collection_type: open
  name: Abcuro Content API (WordPress REST) Discovery API
  slug: open-abcuro-discovery-api
- collection_type: open
  name: Abcuro Content API (WordPress REST) Investors API
  slug: open-abcuro-investors-api
- collection_type: open
  name: Abcuro Content API (WordPress REST) Media API
  slug: open-abcuro-media-api
- collection_type: open
  name: Abcuro Content API (WordPress REST) Pages API
  slug: open-abcuro-pages-api
- collection_type: open
  name: Abcuro Content API (WordPress REST) People API
  slug: open-abcuro-people-api
- collection_type: open
  name: Abcuro Content API (WordPress REST) Press Releases API
  slug: open-abcuro-press-releases-api
- collection_type: open
  name: Abcuro Content API (WordPress REST) Publications API
  slug: open-abcuro-publications-api
- collection_type: open
  name: Abcuro Content API (WordPress REST) Search API
  slug: open-abcuro-search-api
- collection_type: open
  name: Abcuro Content API (WordPress REST) Taxonomy API
  slug: open-abcuro-taxonomy-api
- collection_type: open
  name: Abcuro Content API (WordPress REST) Users API
  slug: open-abcuro-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/abcuro-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://abcuro.com/
- group: other
  title: ''
  type: CompanyProfile
  url: https://forgeglobal.com/abcuro_stock/
- group: company
  title: ''
  type: About
  url: https://abcuro.com/about/
- group: company
  title: ''
  type: Blog
  url: https://abcuro.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://abcuro.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://abcuro.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://abcuro.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://abcuro.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abcuro.com/privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wordpress.org/rest-api/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.wordpress.org/rest-api/reference/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/abcuro-content-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/abcuro-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/abcuro-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/abcuro-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/abcuro-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/abcuro-content-overlay.yaml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/abcuro-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/abcuro-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/abcuro-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abcuro-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/abcuro-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/abcuro-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abcuro-llms.txt
created: '2026-08-02'
description: Abcuro is a clinical-stage biotechnology company headquartered in Newton, Massachusetts, developing first-in-class immunotherapies that precisely modulate highly cytotoxic T cells for autoimmune disease and cancer. Its lead candidate, ulviprubart (ABC008), is a monoclonal antibody targeting KLRG1 that selectively depletes highly cytotoxic T cells, evaluated in the registrational Phase 2/3 MUSCLE study in inclusion body myositis (IBM) and in T cell large granular lymphocytic leukemia (T-LGLL) and mature T and NK cell lymphomas. Abcuro publishes no commercial developer platform or product API; its only machine-readable surface is the public WordPress REST API behind abcuro.com, which anonymously serves the corporate content graph — press releases, pipeline and science pages, scientific publications, leadership and board people records, investor records, and media assets — and is catalogued here as a read-only content API rather than a product API.
image: https://abcuro.com/wp-content/uploads/Abcuro_logo.png
layout: provider
mcp_servers:
- description: ''
  name: Abcuro MCP Server
  slug: abcuro-mcp-server
modified: '2026-08-02'
name: Abcuro
nav: Providers
network: true
overview: 'Abcuro publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Careers API, Comments API, Discovery API, and 9 more. Tagged areas include Biotechnology, Pharmaceuticals, Immunology, Autoimmune Disease, and Oncology.


  Abcuro''s developer surface includes engineering blog, support, documentation, API reference, authentication, and 21 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 14.3
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 25.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abcuro/refs/heads/main/screenshots/abcuro-2026-08-07T160734.png
security:
- kind: authentication
  name: Abcuro Authentication
  slug: abcuro-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Abcuro Domain Security
  slug: abcuro-domain-security
  summary_line: TLSv1.2 · DMARC
slug: abcuro
tags:
- Biotechnology
- Pharmaceuticals
- Immunology
- Autoimmune Disease
- Oncology
- Clinical Trials
- Life Sciences
- Drug Development
- Healthcare
- content-api
- WordPress
website: https://abcuro.com/
---
