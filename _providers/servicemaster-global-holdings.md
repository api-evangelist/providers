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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/servicemaster-global-holdings-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/servicemasterbrands
- group: company
  title: ''
  type: Website
  url: https://www.servicemaster.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/servicemaster-global-holdings-llms.txt
coverage:
  checked: '2026-08-29'
  detail: 'ServiceMaster Global Holdings ceased to exist as a company: it sold ServiceMaster Brands to Roark Capital in October 2020, renamed itself Terminix Global Holdings, and was absorbed by Rentokil Initial in October 2022 — its own registered domain www.servicemaster-global-holdings.com no longer resolves, and the surviving ServiceMaster Brands site publishes only 14 pages with no developer, API or integration page among them.'
  evidence:
  - status: 0
    url: https://www.servicemaster-global-holdings.com
  - status: 200
    url: https://www.servicemaster.com/page-sitemap.xml
  - status: 404
    url: https://www.servicemaster.com/openapi.json
  - status: 404
    url: https://www.servicemaster.com/llms.txt
  - status: 404
    url: https://www.servicemaster.com/.well-known/api-catalog
  - status: 404
    url: https://www.servicemasterclean.com/.well-known/agent-card.json
  - status: 404
    url: https://www.servicemasterrestore.com/openapi.json
  reason: defunct
  state: none
created: '2026-03-24'
description: 'ServiceMaster Global Holdings, Inc. (NYSE: SERV) was the Memphis-based parent company behind Terminix, ServiceMaster Restore, ServiceMaster Clean, Merry Maids, AmeriSpec and Furniture Medic — termite and pest control, disaster restoration, commercial and residential cleaning, home inspection and furniture repair, delivered largely through a franchise network. The company no longer exists under this name. On 1 October 2020 it sold the ServiceMaster Brands franchise business to Roark Capital for $1.553 billion, and later that month renamed itself Terminix Global Holdings, Inc., changing its NYSE ticker to TMX. Rentokil Initial plc completed its acquisition of Terminix Global Holdings in October 2022, absorbing the remaining pest-control business. The ServiceMaster brand itself continues under the independent, Roark-owned ServiceMaster Brands at servicemaster.com. Neither the historic holding company nor its successors publish a public developer program, API documentation, or
  a machine-readable contract of any kind.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/servicemaster-global-holdings.png
layout: provider
modified: '2026-08-29'
name: ServiceMaster Global Holdings
nav: Providers
network: true
overview: ServiceMaster Global Holdings is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 1000, Home Services, Pest Control, Facilities Management, and Disaster Restoration.
press:
- date: '2026-05-25'
  title: ServiceMaster Invests in Salesforce, Differentiates Itself to ...
  url: https://news.terminix.com/press-releases/press-release-details/2018/ServiceMaster-Invests-in-Salesforce-Differentiates-Itself-to-Deliver-Exceptional-Customer-Experiences/default.aspx
- date: '2026-05-25'
  title: Janitorial Services Market Set to Witness Massive Growth
  url: https://www.openpr.com/news/4297892/janitorial-services-market-set-to-witness-massive-growth
- date: '2026-05-25'
  title: Led by 10% year-over-year revenue growth in its Terminix ...
  url: https://www.facebook.com/DailyMemphian/posts/led-by-10-year-over-year-revenue-growth-in-its-terminix-pest-control-business-se/2321945131356511/
- date: '2026-05-25'
  title: XBRL Viewer
  url: https://www.sec.gov/ix?doc=/Archives/edgar/data/1428875/000110465920101633/tm2029976-1_8k.htm
- date: '2026-05-25'
  title: 'Shareholder Alert: Robbins LLP Announces It Is Investigating ...'
  url: https://www.businesswire.com/news/home/20200611005774/en/Shareholder-Alert-Robbins-LLP-Announces-It-Is-Investigating-ServiceMaster-Global-Holdings-Inc.-SERV-for-Misleading-Shareholders
random_paper: 15
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Servicemaster Global Holdings Domain Security
  slug: servicemaster-global-holdings-domain-security
  summary_line: TLSv1.3 · DMARC
slug: servicemaster-global-holdings
tags:
- Fortune 1000
- Home Services
- Pest Control
- Facilities Management
- Disaster Restoration
- Cleaning Services
- Franchising
- Acquired
website: https://www.servicemaster.com/
---
