---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 19
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alcoa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alcoa.com
- group: other
  title: ''
  type: Products
  url: https://www.alcoa.com/global/en/what-we-do
- group: company
  title: ''
  type: Blog
  url: https://news.alcoa.com/
- group: operate
  title: ''
  type: PressReleases
  url: https://news.alcoa.com/press-releases/default.aspx
- group: operate
  title: ''
  type: Contact
  url: https://www.alcoa.com/global/en/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alcoa.com/global/en/general/legal-notices
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alcoa.com/global/en/general/privacy
- group: other
  title: ''
  type: Sustainability
  url: https://www.alcoa.com/sustainability/en/
- group: other
  title: ''
  type: AnnualReport
  url: https://investors.alcoa.com/financials/annual-reports-and-proxy-statements/default.aspx
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.alcoa.com/home/default.aspx
- group: auth
  title: ''
  type: Compliance
  url: https://www.alcoa.com/global/en/who-we-are/ethics-compliance
- group: design
  title: ''
  type: Conformance
  url: conformance/alcoa-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alcoa-llms.txt
- group: other
  title: ''
  type: Locations
  url: https://www.alcoa.com/global/en/who-we-are/locations
- group: other
  title: ''
  type: Suppliers
  url: https://www.alcoa.com/global/en/contact/supplier
- group: company
  title: ''
  type: Careers
  url: https://www.alcoa.com/careers/en/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alcoa
coverage:
  checked: '2026-08-30'
  detail: 'Alcoa is a bauxite, alumina and aluminum producer with no developer program: the corporate site 404s /openapi.json, /llms.txt and every /.well-known/ path, developer.alcoa.com and apis.alcoa.com do not resolve, and the one live API host, api.alcoa.com, is an internal Azure APIM gateway that answers 401 "Access denied due to missing subscription key" on its only routed path and 404s every discovery path.'
  evidence:
  - status: 401
    url: https://api.alcoa.com/echo/resource
  - status: 404
    url: https://api.alcoa.com/openapi.json
  - status: 404
    url: https://www.alcoa.com/openapi.json
  - status: 404
    url: https://www.alcoa.com/llms.txt
  - status: 404
    url: https://www.alcoa.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/alcoa
  reason: not-a-software-company
  state: none
created: '2026-03-21'
description: Alcoa Corporation is a global industry leader in bauxite, alumina, and aluminum production. Founded in 1888, Alcoa operates mines, refineries, and smelters across Australia, Brazil, Canada, Iceland, Norway, Saudi Arabia, and the United States. The company is a Fortune 500 member and one of the world's largest aluminum producers, supplying lightweight, high-strength materials to automotive, aerospace, packaging, construction, and industrial markets. Alcoa is committed to sustainability through low-carbon aluminum production, responsible bauxite mining, and advancing aluminum recycling.
features:
- description: World-scale bauxite mining operations in Australia and Brazil supplying the global alumina supply chain.
  name: Bauxite Mining
- description: Large-scale alumina (aluminum oxide) refining operations that convert bauxite to the precursor for aluminum smelting.
  name: Alumina Refining
- description: Primary aluminum production using proprietary smelting technology, including low-carbon ELYSIS process development.
  name: Aluminum Smelting
- description: Joint venture with Rio Tinto developing ELYSIS technology for carbon-free aluminum smelting using inert anodes.
  name: ELYSIS Zero-Carbon Technology
- description: Recycled aluminum products and closed-loop supply chain programs with automotive and packaging customers.
  name: Aluminum Recycling
- description: Annual sustainability reports tracking greenhouse gas emissions, water use, land rehabilitation, and biodiversity commitments.
  name: Sustainability Reporting
- description: Engineered aluminum billet, slab, and foundry alloy products for downstream rolling and extrusion customers.
  name: Cast Products
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alcoa.png
integrations:
- description: Supply agreements with major automotive manufacturers for aluminum sheet, castings, and engineered components.
  name: Automotive OEMs
- description: Long-term supply relationships with commercial and defense aerospace prime contractors and tier-1 suppliers.
  name: Aerospace Manufacturers
- description: Aluminum sheet supply to beverage can manufacturers and food packaging converters globally.
  name: Packaging Companies
- description: Aluminum billet supply to extrusion companies serving the building and construction market.
  name: Construction and Architecture
- description: Joint venture with Rio Tinto to commercialize carbon-free aluminum smelting technology via the ELYSIS partnership.
  name: Rio Tinto - ELYSIS JV
layout: provider
modified: '2026-08-30'
name: Alcoa
nav: Providers
network: true
overview: 'Alcoa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Aluminum, Mining, Manufacturing, Metals, and Sustainability.


  Alcoa''s developer surface includes engineering blog and 17 more developer resources.'
press:
- date: '2026-05-25'
  title: Aluminium maker Alcoa seeks to sell 10 sites to data centres
  url: https://www.reuters.com/business/energy/aluminium-maker-alcoa-seeks-sell-10-sites-data-centres-2026-02-24/
- date: '2026-05-25'
  title: Alcoa
  url: https://www.fairmarkit.com/case-studies/alcoa
- date: '2026-05-25'
  title: Alcoa Intermediate School Students win AI award, set ...
  url: https://www.wbir.com/article/news/local/maryville-blount/alcoa-intermediate-school-students-win-ai-award/51-f7786fcb-5511-4f4e-a17a-21f4616646ce
- date: '2026-05-25'
  title: Alcoa CEO Bill Oplinger joined CNBC in an exclusive ...
  url: https://www.facebook.com/alcoa/posts/alcoa-ceo-bill-oplinger-joined-cnbc-in-an-exclusive-interview-ahead-of-the-compa/1463003409197778/
- date: '2026-05-25'
  title: Alcoa Stock Jumps. How Its CEO Plans to Cash in on the AI ...
  url: https://www.barrons.com/articles/alcoa-stock-price-ai-electricity-ceo-875a9f7a
random_paper: 8
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 1.8
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alcoa/refs/heads/main/screenshots/alcoa-2026-06-20T171511.png
security:
- kind: domain-security
  name: Alcoa Domain Security
  slug: alcoa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alcoa
tags:
- Aluminum
- Mining
- Manufacturing
- Metals
- Sustainability
- Fortune 500
- Materials
use_cases:
- description: High-strength aluminum sheet and castings for vehicle body structures, hoods, doors, and structural components reducing vehicle weight.
  name: Automotive Lightweighting
- description: Aerospace-grade aluminum alloys for airframe structures, fuselage panels, and wing components with stringent certification requirements.
  name: Aerospace Structures
- description: Aluminum sheet for the packaging industry including beverage cans, foil, and food container stock.
  name: Packaging and Beverage Cans
- description: Architectural aluminum extrusions and sheet for windows, curtain walls, roofing, and structural construction applications.
  name: Building and Construction
- description: Aluminum for solar panel frames, wind turbine components, and electric vehicle battery enclosures supporting the energy transition.
  name: Energy Transition Infrastructure
- description: High-purity alumina and specialty aluminum products for industrial processes, refractories, and abrasive applications.
  name: Industrial Applications
website: https://www.alcoa.com
---
