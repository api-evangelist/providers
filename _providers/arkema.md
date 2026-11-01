---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 20
common:
- group: start
  title: ''
  type: SignUp
  url: https://www.arkema.com/global/en/investor-relations/individual-shareholder/registered-shares/
- group: agent
  href: https://artifacts.apis.io/arkema/llms/arkema-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arkema-llms.txt
- group: other
  href: https://artifacts.apis.io/arkema/hosts/arkema-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arkema-hosts.yml
- group: other
  href: https://artifacts.apis.io/arkema/vendors/arkema-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arkema-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.arkema.com/global/en/social-responsibility/documentation/
- group: commercial
  href: https://artifacts.apis.io/arkema/plans/arkema-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/arkema-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/arkema/rate-limits/arkema-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/arkema-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/arkema/finops/arkema-finops.yml
  title: ''
  type: FinOps
  url: finops/arkema-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.arkema.com/global/en/media/newsroom/
- group: auth
  href: https://artifacts.apis.io/arkema/security/arkema-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arkema-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arkema.com
- group: start
  title: ''
  type: Portal
  url: https://www.arkema.com/global/en/products/product-finder/
- group: other
  title: ''
  type: Bostik
  url: https://www.bostik.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.arkema.com/global/en/investor-relations/
- group: company
  title: ''
  type: News
  url: https://www.arkema.com/global/en/media/newslist/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arkema
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Arkema
- group: other
  title: ''
  type: Segments
  url: ''
- group: other
  title: ''
  type: Strategy
  url: ''
- group: other
  title: ''
  type: ProductPage
  url: https://www.arkema.com/global/en/products/product-safety/
coverage:
  checked: '2026-10-20'
  detail: Arkema is a specialty chemicals manufacturer whose web estate (www.arkema.com, my.arkema.com customer login) serves product finders and SDS downloads; contract discovery on api.arkema.com and www.arkema.com found no OpenAPI, GraphQL, MCP or agent card.
  evidence:
  - status: 200
    url: https://www.arkema.com
  - status: 200
    url: https://my.arkema.com/
  - status: 403
    url: https://www.arkema.com/mcp
  reason: not-a-software-company
  state: none
created: '2026-05-23'
description: Arkema S.A. is a French specialty materials company headquartered in La Defense, Paris and listed on Euronext Paris under ticker AKE. The group is organized around three Specialty Materials segments — Adhesive Solutions (anchored by the Bostik brand), Advanced Materials (high-performance polymers including Kynar PVDF, Rilsan polyamides, Pebax elastomers, Sartomer photocurable resins) and Coating Solutions (acrylic monomers, waterborne and solvent-borne resins, additives) — plus a smaller Intermediates business. Arkema employs roughly 21,000 people across 55 countries with about 154 production plants and 17 R&D centers, generating around EUR 9.1 billion in 2025 revenue. Strategy is anchored in materials science, decarbonization and a validated 1.5 degree SBTi pathway toward Net-Zero by 2050. Arkema does not publish a public developer portal or REST API; customer integrations and product data are exchanged through commercial sales channels, the Product Finder web UI and Safety
  Data Sheet downloads.
features:
- description: '"Building on its unique set of expertise in materials science, Arkema designs materials to address the ever-growing demand for innovative and sustainable materials."'
  name: Materials Science Platform
- description: Branded technology platforms including Bostik adhesives, Kynar PVDF, Rilsan and Rilsamid bio-based polyamides, Pebax elastomers, Sartomer photocurables, Coatex rheology modifiers and Altuglas / Plexiglas PMMA.
  name: Flagship Brand Portfolio
- description: About 154 production plants and 17 R&D centers across 55 countries, enabling regional supply for global and local customers.
  name: Global Manufacturing Footprint
- description: A-Z index and criteria-based product search across 27 product families covering fluoropolymers, acrylics, amines, adhesives, coating resins, peroxides, PEKK, UV/LED/EB resins and polyimides.
  name: Product Finder
- description: Product Safety portal providing regulatory documentation and SDS downloads for Arkema chemical products.
  name: Safety Data Sheets
- description: Annual disclosure of Scope 1/2/3 emissions, SBTi-validated 1.5 degree trajectory, Net-Zero by 2050 ambition and Sustainable Solutions portfolio metrics in the Universal Registration Document.
  name: Sustainability Reporting
finops:
- has_sources: true
  method: generated
  name: Arkema Finops
  primary_unit: ''
  service_category: Industrial / Chemicals
  slug: arkema-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arkema.png
integrations:
- description: Adhesive Solutions products distributed through construction merchants, industrial distributors and direct OEM contracts globally.
  name: Bostik Customer Network
- description: Kynar, Rilsan, Pebax, Kepstan and Sartomer product lines delivered to OEMs and formulators via Arkema regional sales and authorized distributors.
  name: Specialty Polymer Distribution
- description: Strategic acquisitions and joint ventures expanding the Adhesive Solutions and Advanced Materials platforms, including Bostik (2015), Den Braven, ArrMaz, Ashland Performance Adhesives and PIAM.
  name: Joint Ventures and Acquisitions
- description: Alignment with the Science Based Targets initiative (SBTi), Responsible Care, EcoVadis and CDP for emissions, water and supply-chain disclosure.
  name: Sustainability Frameworks
layout: provider
modified: '2026-10-06'
name: Arkema
nav: Providers
network: true
overview: 'Arkema is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Chemicals, Specialty Materials, Adhesives, Polymers, and Coatings.


  Arkema''s developer surface includes signup flow, documentation, engineering blog, developer portal, product news, GitHub presence, and 12 more developer resources.'
plans:
- name: Arkema Plans Pricing
  plan_count: 1
  slug: arkema-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Arkema Rate Limits
  slug: arkema-rate-limits
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 50.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 12.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/arkema/arkema-2026-06-20T172433.png
security:
- kind: domain-security
  name: Arkema Domain Security
  slug: arkema-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arkema
tags:
- Chemicals
- Specialty Materials
- Adhesives
- Polymers
- Coatings
- Manufacturing
- Sustainability
use_cases:
- description: Kynar PVDF binders and separators for lithium-ion batteries, plus fluoropolymer membranes for hydrogen electrolysis and fuel cells.
  name: Battery and Hydrogen Materials
- description: Rilsan polyamide 11 fuel and brake lines, Pebax elastomers for sporting goods and automotive components, and PEKK composites for aerospace.
  name: Lightweight Mobility
- description: Bostik tile adhesives, sealants and roofing systems, plus acrylic coating resins for low-VOC architectural paints.
  name: Sustainable Building
- description: Bostik packaging adhesives for flexible lamination, labels, reclosable packaging and absorbent hygiene products.
  name: Consumer Goods Packaging
- description: Photocurable Sartomer resins, fluoropolymer films and high-purity intermediates for semiconductor manufacturing, displays and printed electronics.
  name: Advanced Electronics
- description: Medical-grade Pebax, Rilsan and Kynar polymers for catheters, drug delivery, prosthetics and medical packaging.
  name: Healthcare and Wellness
website: https://www.arkema.com
---
