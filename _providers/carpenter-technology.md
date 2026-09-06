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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carpenter-technology-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/carpenter-technology-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/carpenter-technology-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carpenter-technology-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carpenter-technology
- group: company
  title: ''
  type: Website
  url: https://www.carpentertechnology.com
- group: company
  title: ''
  type: About
  url: https://www.carpentertechnology.com/about
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.carpentertechnology.com
- group: other
  title: ''
  type: AlloyFinder
  url: https://www.carpentertechnology.com/alloy-finder
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://www.carpentertechnology.com/resources
- group: auth
  title: ''
  type: Certification
  url: https://www.carpentertechnology.com/quality-assurance-and-control
- group: other
  title: ''
  type: Sustainability
  url: https://www.carpentertechnology.com/sustainability/overview
- group: start
  title: ''
  type: Login
  url: https://www.carpentertechnology.com/_hcms/mem/login
- group: operate
  title: ''
  type: Contact
  url: https://www.carpentertechnology.com/contact-us
- group: company
  title: ''
  type: Careers
  url: https://www.carpentertechnology.com/careers
- group: company
  title: ''
  type: Blog
  url: https://www.carpentertechnology.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carpentertechnology.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carpentertechnology.com/privacy-policy
coverage:
  checked: '2026-09-05'
  detail: Carpenter Technology sells physical specialty alloys — its entire web estate is a HubSpot CMS marketing site whose only login is a HubSpot membership content gate, and every spec and /.well-known path probed on carpentertechnology.com, www.carpentertechnology.com, ir.carpentertechnology.com and www.carpenteradditive.com returned 404 or a "Invalid key" catch-all, with no developer portal, GitHub organization or SDK anywhere.
  evidence:
  - status: 404
    url: https://www.carpentertechnology.com/openapi.json
  - status: 404
    url: https://www.carpentertechnology.com/.well-known/api-catalog
  - status: 404
    url: https://www.carpentertechnology.com/developers
  - status: 404
    url: https://api.github.com/orgs/carpentertechnology
  reason: not-a-software-company
  state: none
created: '2026-03-23'
description: Carpenter Technology Corporation is a U.S.-based producer and distributor of premium specialty alloys — including titanium alloys, powder metals, high-temperature stainless steels, tool steels, and soft magnetic alloys — serving the aerospace, defense, medical, transportation, energy, and industrial end markets. The company supports customers through technical product resources such as its Alloy Finder, alloy technical data sheets, conversion tables, and a member-only Customer Portal for order and account self-service, but does not currently publish a public developer API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carpenter-technology.png
layout: provider
modified: '2026-09-05'
name: Carpenter Technology
nav: Providers
network: true
overview: 'Carpenter Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Specialty Alloys, Titanium, Stainless Steel, Aerospace, and Defense.


  Carpenter Technology''s developer surface includes engineering blog and 17 more developer resources.'
press:
- date: '2026-05-25'
  title: Carpenter Technology Vs Intelligent
  url: https://danelfin.com/stocks/CRS-carpenter-technology-vs-INTJ-intelligent-compare
- date: '2026-05-25'
  title: Carpenter Technology Corporation (CRS) reports earnings
  url: https://qz.com/carpenter-technology-corporation-crs-reports-earnings-1851752130
- date: '2026-05-25'
  title: 'Carpenter Technology: This Stock Will Melt Up'
  url: https://www.barrons.com/articles/carpenter-technology-stock-melt-up-b57d0b6e
- date: '2026-05-25'
  title: Carpenter Technology's New $500 Million Steel Alloy Mill ...
  url: https://www.industrialinfo.com/news/article/carpenter-technologys-new-500-million-steel-alloy-mill-takes-shape-in-alabama--231932
- date: '2026-05-25'
  title: A Look At Carpenter Technology (CRS) Valuation After ...
  url: https://finance.yahoo.com/news/look-carpenter-technology-crs-valuation-151330338.html
random_paper: 14
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 12.1
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 6.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/carpenter-technology/refs/heads/main/screenshots/carpenter-technology-2026-06-20T174016.png
security:
- kind: domain-security
  name: Carpenter Technology Domain Security
  slug: carpenter-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carpenter-technology
tags:
- Specialty Alloys
- Titanium
- Stainless Steel
- Aerospace
- Defense
- Medical
- Materials Science
- Fortune 1000
website: https://www.carpentertechnology.com
---
