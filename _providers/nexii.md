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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nexii-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nexii.com/
- group: company
  title: ''
  type: About
  url: https://www.nexii.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.nexii.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.nexii.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nexii.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nexii.com/terms-of-service
- group: other
  title: ''
  type: Resources
  url: https://www.nexii.com/resources
- group: company
  title: ''
  type: Careers
  url: https://nexii.bamboohr.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/nexii-building-solutions
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/nexii_stock/
coverage:
  checked: '2026-08-04'
  detail: Nexii manufactures prefabricated Nexiite wall and roof panels for commercial construction; www.nexii.com is a marketing site whose entire sitemap is verticals, project case studies, PDF resources and news, with no developer, API or documentation section, and api./developer./docs.nexii.com do not resolve.
  evidence:
  - status: 200
    url: https://www.nexii.com/sitemap.xml
  - status: 404
    url: https://www.nexii.com/developers
  - status: 404
    url: https://www.nexii.com/openapi.json
  - status: 404
    url: https://www.nexii.com/.well-known/agent-card.json
  - status: 0
    url: https://api.nexii.com/
  reason: not-a-software-company
  state: none
created: '2026-08-04'
description: 'Nexii is a green construction technology company that designs and manufactures prefabricated wall and roof panel systems for commercial and industrial buildings. Its panels are made from Nexiite, a proprietary low-carbon building material the company says is up to 80% lighter than conventional concrete, and bolt together on site to cut build times by as much as five times while producing near-zero construction waste. Nexii serves retail, residential, warehouse, data center, cold storage, healthcare, office and education verticals, with projects for Starbucks, McDonald''s, Pizza Hut, Popeyes, Dutch Bros, Walmart and Marriott. The original Vancouver-based Nexii Building Solutions entered creditor protection in January 2024; Dallas-based 3 Gates acquired its assets in a court-approved sale completed 28 June 2024 and relaunched the business as NEXII, Inc., headquartered in Dallas, Texas with manufacturing in Squamish, British Columbia. Nucor Corporation subsequently made a strategic
  equity investment. Nexii is a manufacturer, not a software vendor: it publishes no developer portal, API documentation, or machine-readable API contract.'
image: https://cdn.prod.website-files.com/67b3630fc38baa7c9cc153ff/67c5cc70a876f4a2d84fd323_Nexii_OG.png
layout: provider
modified: '2026-08-04'
name: Nexii
nav: Providers
network: true
overview: 'Nexii is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Building Materials, Green Building, and Sustainability.


  Nexii''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 10.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nexii/refs/heads/main/screenshots/nexii-2026-08-07T185151.png
security:
- kind: domain-security
  name: Nexii Domain Security
  slug: nexii-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nexii
tags:
- Company
- Construction
- Building Materials
- Green Building
- Sustainability
- Manufacturing
- Prefabrication
- Real-Estate
website: https://www.nexii.com/
---
