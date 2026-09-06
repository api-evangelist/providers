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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'RESTful print-on-demand API that lets businesses integrate Blurb''s book, magazine, and notebook printing and fulfillment into their own platforms. Orders and real-time fulfillment updates are handled '
  name: Blurb Print API
  slug: blurb-print-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blurb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blurb.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.blurb.com/print-api-software
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.rpiprint.com/documentation/first-request
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.rpiprint.com/documentation/first-request
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blurb.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.blurb.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.blurb.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://www.blurb.com/my/account/register
- group: start
  title: ''
  type: Login
  url: https://www.blurb.com/my/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blurb.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blurb.com/privacy
created: '2026-07-17'
description: Blurb is an online self-publishing and print-on-demand platform that lets photographers, designers, businesses, and creative storytellers design, print, and distribute their own books, magazines, notebooks, and wall art. Founded in 2005 and headquartered in San Francisco, Blurb provides desktop and web design tools (BookWright, Bookify, and plugins for Adobe InDesign and Lightroom) alongside professional in-house printing, global fulfillment, and distribution through its own bookstore, Amazon, and Ingram. Blurb also offers a RESTful print-on-demand API — powered by its RPI Print fulfillment infrastructure — so businesses can programmatically submit print orders, upload print-ready PDFs, and receive real-time order tracking and fulfillment updates. It was surfaced as a portfolio company of Canaan Partners and enriched in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blurb.png
layout: provider
modified: '2026-07-18'
name: Blurb
nav: Providers
network: true
overview: 'Blurb publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Publishing, Printing, Print on Demand, and Books.


  Blurb''s developer surface includes documentation, getting-started guide, pricing, support, engineering blog, signup flow, and 6 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 3
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 23.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blurb/refs/heads/main/screenshots/blurb-2026-07-25T203511.png
security:
- kind: domain-security
  name: Blurb Domain Security
  slug: blurb-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: blurb
tags:
- Company
- Publishing
- Printing
- Print on Demand
- Books
- Self-Publishing
- Photo Books
- Fulfillment
- E-Commerce
website: https://www.blurb.com/
---
