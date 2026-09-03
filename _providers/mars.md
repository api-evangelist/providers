---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Mars exposes a public Azure-API-Management developer portal at developer.mars.com that hosts APIs and API Products for partners, suppliers, and B2B integrations. The catalog itself sits behind a regis
  name: Mars Developer Portal
  slug: developer-portal
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mars-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mars
- group: company
  title: ''
  type: Website
  url: https://www.mars.com/
- group: company
  title: ''
  type: AboutUs
  url: https://www.mars.com/about
- group: other
  title: ''
  type: Brands
  url: https://www.mars.com/made-by-mars
- group: company
  title: ''
  type: News
  url: https://www.mars.com/news-and-stories
- group: other
  title: ''
  type: Sustainability
  url: https://www.mars.com/sustainability-plan
- group: company
  title: ''
  type: Careers
  url: https://www.mars.com/careers
- group: other
  title: ''
  type: SupplierGateway
  url: https://www.mars.com/suppliers
- group: other
  title: ''
  type: PetCare
  url: https://www.marspetcare.com/
- group: other
  title: ''
  type: RoyalCanin
  url: https://www.royalcanin.com/
- group: other
  title: ''
  type: Banfield
  url: https://www.banfield.com/
- group: other
  title: ''
  type: VCAAnimalHospitals
  url: https://vcahospitals.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mars.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mars.com/news-and-stories
created: '2026-05-05'
description: Mars, Incorporated is one of the world's largest privately held companies, producing confectionery, pet food, food, and providing veterinary care. The company owns iconic brands including M&M's, Snickers, Twix, Milky Way, Skittles, Wrigley, Orbit, Extra, Pedigree, Whiskas, Royal Canin, IAMS, and Sheba, and operates Mars Petcare clinical brands including Banfield Pet Hospital, VCA Animal Hospitals, BluePearl, and Antech Diagnostics. Mars operates in over 80 countries. Mars operates a public Azure-API-Management developer portal at developer.mars.com for partner and B2B integrations, alongside closed channels such as the Mars Supplier Gateway.
finops:
- name: Mars Finops
  service_category: API
  slug: mars-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mars.png
layout: provider
modified: '2026-05-16'
name: Mars
nav: Providers
network: true
overview: 'Mars publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Confectionery, Consumer Packaged Goods, Food, Pet Care, and Pet Food.


  Mars'' developer surface includes product news, engineering blog, and 13 more developer resources.'
plans:
- name: Mars Plans Pricing
  plan_count: 1
  slug: mars-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Mars Rate Limits
  slug: mars-rate-limits
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mars/refs/heads/main/screenshots/mars-2026-06-20T185004.png
security:
- kind: domain-security
  name: Mars Domain Security
  slug: mars-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mars
tags:
- Confectionery
- Consumer Packaged Goods
- Food
- Pet Care
- Pet Food
- Veterinary
website: https://www.mars.com/
---
