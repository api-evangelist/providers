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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.cmc.com/
- group: operate
  title: ''
  type: Support
  url: https://www.cmc.com/en-us/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cmc.com/en-us/personal-data-protection
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cmcproduction.blob.core.windows.net/media/cmcmetals/media/pdf/cmctermsofuse.pdf
- group: start
  title: ''
  type: CustomerPortal
  url: https://mycmc.cmc.com/
- group: start
  title: ''
  type: PortalRequestAccess
  url: https://www.cmc.com/en-us/mycmc/request-access
- group: build
  title: ''
  type: SystemsIntegration
  url: https://www.cmc.com/en-us/mycmc/ecommerce
- group: docs
  title: ''
  type: SystemsIntegrationGuide
  url: https://www.cmc.com/getmedia/360ad30f-e318-468f-8792-6c78013aff52/CMC-myCMC_Systems-Integration.pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/inside-cmc
- group: other
  title: ''
  type: PerformanceSteel
  url: https://www.cmc.com/en-us/what-we-do/america/performance-steel
- group: build
  title: ''
  type: Recycling
  url: https://www.cmcrecycling.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.cmc.com/
- group: operate
  title: ''
  type: PressReleases
  url: https://ir.cmc.com/news-events/press-releases
- group: other
  title: ''
  type: Sustainability
  url: https://esg.cmc.com/
- group: company
  title: ''
  type: Careers
  url: https://www.cmc.com/en-us/cmc-careers
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commercial-metals-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/commercial-metals-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/commercial-metals-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/commercial-metals-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/commercial-metals-llms.txt
coverage:
  checked: '2026-09-05'
  detail: CMC's own Systems Integration one-pager names EDI and API as supported connection methods but routes every integration through a sales representative or ecommerce@cmc.com — there is no developer portal, signup or reference behind it; the myCMC portal at mycmc.cmc.com answers a Cloudflare 403 in front of a customer-only login, and api.cmc.com is a placeholder returning an identical 56-byte empty HTML document for every path including a random negative-control path.
  evidence:
  - status: 200
    url: https://www.cmc.com/en-us/mycmc/ecommerce
  - status: 200
    url: https://www.cmc.com/getmedia/360ad30f-e318-468f-8792-6c78013aff52/CMC-myCMC_Systems-Integration.pdf
  - status: 403
    url: https://mycmc.cmc.com/
  - status: 200
    url: https://api.cmc.com/openapi.json
  - status: 404
    url: https://www.cmc.com/.well-known/security.txt
  reason: sales-gate
  state: gated
created: '2026-03-21'
description: 'Commercial Metals Company (CMC) is a Fortune 500 manufacturer, recycler, fabricator and marketer of steel and metal products — rebar, merchant and structural bar, wire rod, performance steel, construction products and ground improvement solutions — running recycling centers, mini-mills, micro-mills and fabrication plants across the United States, Europe and Asia for the construction, infrastructure, energy and manufacturing markets. CMC was an early mover on customer self-service with myCMC, a portal for inventory, pricing, online ordering, material release, document search and real-time order and delivery status, and it runs a business-to-business Systems Integration program whose own one-pager names EDI, API, CSV, XML and flat file across the Quote-To-Cash process. None of it is self-service: no developer portal, no API reference and no machine-readable contract is published on any CMC host as of September 2026 — integration is arranged through a CMC sales rep or ecommerce@cmc.com.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/commercial-metals.png
layout: provider
modified: '2026-09-05'
name: Commercial Metals Company
nav: Providers
network: true
overview: 'Commercial Metals Company is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Fortune 500, Manufacturing, Metals, and Recycling.


  Commercial Metals Company''s developer surface includes support and 19 more developer resources.'
plans:
- name: Commercial Metals Plans Pricing
  plan_count: 0
  slug: commercial-metals-plans-pricing
press:
- date: '2026-05-25'
  title: Document
  url: https://www.sec.gov/Archives/edgar/data/0000022444/000002244425000091/cmc-05312025xearningsrelea.htm
- date: '2026-05-25'
  title: Commercial Metals Company (CMC) reports earnings - Quartz
  url: https://qz.com/commercial-metals-company-cmc-reports-earnings-1851733423
- date: '2026-05-25'
  title: Commercial Metals Company Announces Proposed ...
  url: https://www.prnewswire.com/news-releases/commercial-metals-company-announces-proposed-private-offering-of-2-000-million-senior-notes-302613037.html
- date: '2026-05-25'
  title: Peter Matt - Commercial Metals Company
  url: https://www.linkedin.com/in/petermatt
- date: '2026-05-25'
  title: Commercial Metals Company (CMC-N) Press Releases
  url: https://www.theglobeandmail.com/investing/markets/stocks/CMC/pressreleases/
random_paper: 0
rate_limits:
- limit_count: 0
  name: Commercial Metals Rate Limits
  slug: commercial-metals-rate-limits
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/commercial-metals/refs/heads/main/screenshots/commercial-metals-2026-06-20T174819.png
security:
- kind: domain-security
  name: Commercial Metals Domain Security
  slug: commercial-metals-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: commercial-metals
tags:
- Construction
- Fortune 500
- Manufacturing
- Metals
- Recycling
- Steel
website: https://www.cmc.com/
---
