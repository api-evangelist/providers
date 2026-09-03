---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sunfire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sunfire.de/en/
- group: company
  title: ''
  type: About
  url: https://sunfire.de/en/about/
- group: other
  title: ''
  type: Products
  url: https://sunfire.de/en/products/portfolio/
- group: company
  title: ''
  type: Blog
  url: https://sunfire.de/en/newsroom/
- group: other
  title: ''
  type: MediaCenter
  url: https://sunfire.de/en/newsroom/media-center/
- group: operate
  title: ''
  type: Contact
  url: https://sunfire.de/en/contact/
- group: company
  title: ''
  type: Careers
  url: https://sunfire.de/en/career/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sunfire.de/en/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sunfire.de/en/general-conditions-of-delivery-and-purchase/
- group: other
  title: ''
  type: Imprint
  url: https://sunfire.de/en/imprint/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sunfire-gmbh/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/sunfire-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sunfire-llms.txt
coverage:
  checked: '2026-08-29'
  detail: Sunfire SE manufactures physical electrolyzer plant (HyLink Alkaline and HyLink SOEC modules) and sells it through a product-enquiry form; the site has 341 sitemap URLs and not one of them is a developer, docs or API page, and api./developer./docs./portal./status.sunfire.de do not resolve in DNS.
  evidence:
  - status: 404
    url: https://sunfire.de/openapi.json
  - status: 404
    url: https://sunfire.de/.well-known/api-catalog
  - status: 404
    url: https://sunfire.de/llms.txt
  - status: 200
    url: https://sunfire.de/en/products/service/
  - status: 200
    url: https://www.sunfire.de/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-29'
description: 'Sunfire SE is a German hydrogen technology manufacturer headquartered in Dresden, Saxony, with additional sites in Berlin and Solingen. Founded in 2010 by Carl Berninghausen, Christian von Olshausen and Nils Aldag, and converted to a European stock corporation (SE) in 2025, the company builds industrial-scale electrolyzers and power-to-X plants that convert renewable electricity into green hydrogen and synthetic fuels. Its Sunfire-HyLink portfolio spans pressurized alkaline electrolysis (HyLink Alkaline 22 at 10 MW and HyLink Alkaline 23 at 50 MW per module, operating at 30 bar(g)) and high-temperature solid oxide electrolysis (HyLink SOEC, 10 MW modules, a claimed world-record 37.5 kWh/kg H2 efficiency), alongside FEED engineering, project delivery, maintenance and remote data-driven monitoring services. Customers and projects include RWE, Salzgitter, Neste, TotalEnergies, BASF, P2X Solutions, Nordic Ren-Gas and the Bad Lauchstaedt Energy Park. Sunfire is an industrial equipment
  manufacturer: it publishes no developer program, public API, SDK or machine-readable API contract of any kind.'
image: https://sunfire.de/logo.png
layout: provider
modified: '2026-08-29'
name: Sunfire
nav: Providers
network: true
overview: 'Sunfire is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Green Hydrogen, Electrolysis, and Power-to-X.


  Sunfire''s developer surface includes engineering blog and 13 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sunfire/refs/heads/main/screenshots/sunfire-2026-09-02T161139.png
security:
- kind: domain-security
  name: Sunfire Domain Security
  slug: sunfire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sunfire
tags:
- Company
- Energy
- Green Hydrogen
- Electrolysis
- Power-to-X
- Renewable Energy
- Industrial Manufacturing
- Hydrogen Technology
- Synthetic Fuels
- Germany
website: https://sunfire.de/en/
---
