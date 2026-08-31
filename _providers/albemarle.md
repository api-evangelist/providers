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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/albemarle-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/albemarle-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.albemarle.com
- group: company
  title: ''
  type: Blog
  url: https://www.albemarle.com/news
- group: other
  title: ''
  type: Products
  url: https://www.albemarle.com/us/en/what-we-offer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/albemarlecorp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.albemarle.com/us/en/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.albemarle.com/us/en/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.albemarle.com/us/en/contact-us
coverage:
  checked: '2026-08-30'
  detail: 'Albemarle is a lithium and bromine specialty-chemicals manufacturer selling physical product under negotiated supply agreements, and it operates no developer surface at all: api.albemarle.com resolves to an unconfigured vhost serving "Web Site Not Found", developer.albemarle.com and developers.albemarle.com both 404, and the Drupal corporate site returns its standard 404 page for /openapi.json, /swagger.json and /api-docs. The one machine-readable document Albemarle does publish is an llms.txt at the site root, which is agent context about the company, not an API contract.'
  evidence:
  - status: 404
    url: https://api.albemarle.com/
  - status: 404
    url: https://developer.albemarle.com/
  - status: 404
    url: https://www.albemarle.com/openapi.json
  - status: 200
    url: https://www.albemarle.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-03-23'
description: Albemarle Corporation is a global specialty chemicals company and leading provider of lithium, bromine, and other essential elements. Operating from its global headquarters in Charlotte, NC, Albemarle serves customers in approximately 70 countries with world-class hard-rock and brine lithium resources, state-of-the-art lithium conversion facilities, advanced lithium material and process development, bromine production facilities, and the US's only producing lithium resource in Silver Peak, NV. The company serves critical markets including electric vehicle batteries, energy storage, flame retardants, pharmaceutical ingredients, catalysts, and specialty chemicals, employing approximately 7,800 people and holding over 1,500 active patents worldwide.
features:
- description: World-class hard-rock and brine lithium resources, including the US's only producing lithium resource at Silver Peak, NV, supporting battery materials for electric vehicles and energy storage.
  name: Lithium Production
- description: Bromine production and specialty chemical formulations for flame retardants, pharmaceuticals, agriculture, and water treatment applications.
  name: Bromine Specialty Chemicals
- description: Advanced lithium materials and process development for battery-grade lithium hydroxide and carbonate serving energy storage and EV markets.
  name: Energy Storage Materials
- description: Active pharmaceutical ingredients (API), organometallics, and specialty reagents for drug synthesis and nutritional chemistry.
  name: Pharmaceutical Ingredients
- description: Annual sustainability reports tracking environmental footprint, resource management, and ESG metrics across global operations.
  name: Sustainability Reporting
- description: Geographic diversity across lithium and bromine production facilities providing reliable supply to customers in approximately 70 countries.
  name: Global Supply Chain
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/albemarle.png
integrations:
- description: Direct material supply partnerships with automotive manufacturers and battery cell producers in the EV supply chain.
  name: Electric Vehicle OEMs
- description: Integration with grid-scale battery storage project developers and utilities for long-term lithium supply agreements.
  name: Energy Storage Developers
- description: Supply agreements with pharmaceutical companies for specialty reagents and active pharmaceutical ingredients.
  name: Pharmaceutical Manufacturers
- description: Flame retardant chemical supply to PCB fabricators and electronics component manufacturers globally.
  name: Electronics Manufacturers
- description: Catalyst supply and technical service partnerships with refining and petrochemical customers worldwide.
  name: Petroleum Refiners
layout: provider
modified: '2026-08-30'
name: Albemarle
nav: Providers
network: true
overview: 'Albemarle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Chemicals, Lithium, Bromine, Energy Storage, and Electric Vehicles.


  Albemarle''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Albemarle Plans Pricing
  plan_count: 0
  slug: albemarle-plans-pricing
press:
- date: '2026-05-25'
  title: Albemarle Reports Fourth Quarter and Full Year 2025 ...
  url: https://www.prnewswire.com/news-releases/albemarle-reports-fourth-quarter-and-full-year-2025-results-302685449.html
- date: '2026-05-25'
  title: Press Statement December 11, 2025
  url: https://albemarle-cvillenaacp.org/news/press-statement-december-11-2025/
- date: '2026-05-25'
  title: Albemarle Corp. to Pay SEC More Than $103 Million ...
  url: https://www.sec.gov/newsroom/press-releases/2023-209
- date: '2026-05-25'
  title: Artificial Intelligence (AI)
  url: https://www.k12albemarle.org/our-departments/technology/ai
- date: '2026-05-25'
  title: Innovation
  url: https://www.albemarle.com/us/en/who-we-are/innovation
random_paper: 9
rate_limits:
- limit_count: 0
  name: Albemarle Rate Limits
  slug: albemarle-rate-limits
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 1.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/albemarle/refs/heads/main/screenshots/albemarle-2026-06-20T171503.png
security:
- kind: domain-security
  name: Albemarle Domain Security
  slug: albemarle-domain-security
  summary_line: TLSv1.3 · DMARC
slug: albemarle
tags:
- Chemicals
- Lithium
- Bromine
- Energy Storage
- Electric Vehicles
- Specialty Chemicals
- Pharmaceuticals
- Sustainability
- Materials Science
- Manufacturing
- Fortune 1000
use_cases:
- description: Lithium hydroxide and carbonate for cathode active materials in lithium-ion batteries powering passenger and commercial electric vehicles.
  name: Electric Vehicle Batteries
- description: Battery materials for stationary energy storage systems enabling grid reliability and renewable energy integration.
  name: Grid-Scale Energy Storage
- description: Bromine-based flame retardants providing fire safety for printed circuit boards, cables, and electronic enclosures.
  name: Flame Retardants for Electronics
- description: High-purity organometallics and specialty reagents supporting drug discovery and active pharmaceutical ingredient manufacturing.
  name: Pharmaceutical Synthesis
- description: Catalyst solutions for petroleum refining and petrochemical processing using proprietary alumina and zeolite technologies.
  name: Industrial Catalysts
- description: Bromine-based biocides and disinfectants for industrial cooling water, recreational water, and municipal treatment applications.
  name: Water Treatment
- description: Clear brine fluids and specialty chemicals for completion, drilling, and workover operations in oil and gas production.
  name: Oilfield Services
website: https://www.albemarle.com
---
