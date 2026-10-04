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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.1
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Abcuro Agentic Access
  operation_count: 30
  slug: abcuro-agentic-access
  summary_line: 30 operations
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Abcuro website at abcuro.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Abcuro Website (WordPress REST)
  slug: abcuro-com-website-wordpress-rest
artifact_total: 5
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/abcuro/refs/heads/main/agentic-access/abcuro-agentic-access.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/abcuro/refs/heads/main/openapi/_original/abcuro-content-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/abcuro-content-openapi.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/abcuro/refs/heads/main/authentication/abcuro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/abcuro-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/abcuro/refs/heads/main/conventions/abcuro-conventions.yml
  title: ''
  type: Conventions
  url: conventions/abcuro-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/abcuro/refs/heads/main/errors/abcuro-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/abcuro-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/abcuro/refs/heads/main/data-model/abcuro-data-model.yml
  title: ''
  type: DataModel
  url: data-model/abcuro-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/abcuro/refs/heads/main/overlays/abcuro-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/abcuro-content-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/abcuro/refs/heads/main/lifecycle/abcuro-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/abcuro-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/abcuro/refs/heads/main/conformance/abcuro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/abcuro-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/abcuro/refs/heads/main/well-known/abcuro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/abcuro-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/abcuro/refs/heads/main/security/abcuro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/abcuro-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/abcuro/refs/heads/main/mcp/abcuro-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/abcuro-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/abcuro/refs/heads/main/mcp/abcuro-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/abcuro-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/abcuro/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/abcuro/refs/heads/main/llms/abcuro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/abcuro-llms.txt
created: '2026-08-02'
description: Abcuro is a clinical-stage biotechnology company headquartered in Newton, Massachusetts, developing first-in-class immunotherapies that precisely modulate highly cytotoxic T cells for autoimmune disease and cancer. Its lead candidate, ulviprubart (ABC008), is a monoclonal antibody targeting KLRG1 that selectively depletes highly cytotoxic T cells, evaluated in the registrational Phase 2/3 MUSCLE study in inclusion body myositis (IBM) and in T cell large granular lymphocytic leukemia (T-LGLL) and mature T and NK cell lymphomas. Abcuro publishes no commercial developer platform or product API; its only machine-readable surface is the public WordPress REST API behind abcuro.com, which anonymously serves the corporate content graph — press releases, pipeline and science pages, scientific publications, leadership and board people records, investor records, and media assets — and is catalogued here as a read-only content API rather than a product API.
image: https://abcuro.com/wp-content/uploads/Abcuro_logo.png
layout: provider
modified: '2026-08-02'
name: Abcuro
nav: Providers
network: true
overview: 'Abcuro publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Pharmaceuticals, Immunology, Autoimmune Disease, and Oncology.


  Abcuro''s developer surface includes engineering blog, support, documentation, API reference, authentication, and 21 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 1.7
    developer_ergonomics: 37.5
    discoverability: 64.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 20.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
