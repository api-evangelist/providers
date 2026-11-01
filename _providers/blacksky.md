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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Blacksky Agentic Access
  operation_count: 57
  slug: blacksky-agentic-access
  summary_line: 57 operations · 19 acting
api_count: 1
apis:
- description: Access-controlled API behind BlackSky's Spectra platform for satellite tasking, imagery delivery and analytics. The API host api.blacksky.com answers anonymous requests with 403 and the tasking portal
  name: BlackSky Spectra Tasking and Imagery API
  slug: spectra-api
- baseURL: https://api.blacksky.com
  baseurl_source: declared
  description: The Budgets API from BlackSky — 4 operation(s) for budgets.
  name: BlackSky Budgets API
  slug: blacksky-budgets-api
- baseURL: https://api.blacksky.com
  baseurl_source: declared
  description: The Catalog API from BlackSky — 3 operation(s) for catalog.
  name: BlackSky Catalog API
  slug: blacksky-catalog-api
- baseURL: https://api.blacksky.com
  baseurl_source: declared
  description: The Data management API from BlackSky — 8 operation(s) for data management.
  name: BlackSky Data management API
  slug: blacksky-data-management-api
- baseURL: https://api.blacksky.com
  baseurl_source: declared
  description: The EULAs API from BlackSky — 4 operation(s) for eulas.
  name: BlackSky EULAs API
  slug: blacksky-eulas-api
- baseURL: https://api.blacksky.com
  baseurl_source: declared
  description: The Geometries API from BlackSky — 2 operation(s) for geometries.
  name: BlackSky Geometries API
  slug: blacksky-geometries-api
- baseURL: https://api.blacksky.com
  baseurl_source: declared
  description: The Glossary API from BlackSky — 6 operation(s) for glossary.
  name: BlackSky Glossary API
  slug: blacksky-glossary-api
- baseURL: https://api.blacksky.com
  baseurl_source: declared
  description: The Orders API from BlackSky — 6 operation(s) for orders.
  name: BlackSky Orders API
  slug: blacksky-orders-api
- baseURL: https://api.blacksky.com
  baseurl_source: declared
  description: The Processing API from BlackSky — 7 operation(s) for processing.
  name: BlackSky Processing API
  slug: blacksky-processing-api
- baseURL: https://api.blacksky.com
  baseurl_source: declared
  description: The Tasking API from BlackSky — 8 operation(s) for tasking.
  name: BlackSky Tasking API
  slug: blacksky-tasking-api
artifact_total: 16
common:
- group: other
  href: https://artifacts.apis.io/blacksky/capabilities/blacksky-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/blacksky-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/blacksky/agentic-access/blacksky-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blacksky-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/blacksky/rules/blacksky-rules.yml
  title: ''
  type: Spectral
  url: rules/blacksky-rules.yml
- group: design
  href: https://artifacts.apis.io/blacksky/json-ld/blacksky-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blacksky-context.jsonld
- group: design
  href: https://artifacts.apis.io/blacksky/vocabulary/blacksky-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blacksky-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/blacksky/data-model/blacksky-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blacksky-data-model.yml
- group: auth
  href: https://artifacts.apis.io/blacksky/authentication/blacksky-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blacksky-authentication.yml
- group: auth
  href: https://artifacts.apis.io/blacksky/scopes/blacksky-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/blacksky-scopes.yml
- group: design
  href: https://artifacts.apis.io/blacksky/errors/blacksky-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blacksky-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blacksky/conformance/blacksky-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blacksky-conformance.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sa.up42.com/getting-started/account-management
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sa.up42.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.up42.com/reference/overview
- group: agent
  href: https://artifacts.apis.io/blacksky/well-known/blacksky-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blacksky-well-known.yml
- group: other
  href: https://artifacts.apis.io/blacksky/hosts/blacksky-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blacksky-hosts.yml
- group: other
  href: https://artifacts.apis.io/blacksky/vendors/blacksky-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blacksky-vendors.yml
- group: auth
  href: https://artifacts.apis.io/blacksky/security/blacksky-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blacksky-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blacksky.com
- group: other
  title: ''
  type: Technology
  url: https://blacksky.com/technology/
- group: other
  title: ''
  type: Offerings
  url: https://blacksky.com/offerings/
- group: other
  title: ''
  type: Spectra
  url: https://blacksky.com/technology/
- group: start
  title: ''
  type: TaskingPortal
  url: https://tasking.blacksky.com
- group: other
  title: ''
  type: Company
  url: https://blacksky.com/company/
- group: company
  title: ''
  type: Newsroom
  url: https://blacksky.com/news/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.blacksky.com/
- group: company
  title: ''
  type: Careers
  url: https://blacksky.com/company/careers/
- group: operate
  title: ''
  type: Contact
  url: https://blacksky.com/company/contact-us/
- group: company
  title: ''
  type: Newsletter
  url: https://info.blacksky.com/subscribe
- group: company
  title: ''
  type: Partner
  url: https://docs.up42.com/data/blacksky
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/blackskyinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blackskyinc
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@BlackSkyInc
- group: company
  title: ''
  type: Blog
  url: https://blacksky.com/insights/
- group: other
  title: ''
  type: Leadership
  url: https://blacksky.com/company/leadership/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blacksky.com/privacy-statement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blacksky.com/blacksky-terms-of-use/
- group: start
  title: ''
  type: Login
  url: https://login.blacksky.com/
coverage:
  checked: '2026-10-20'
  detail: The Spectra API host api.blacksky.com returns 403 to anonymous requests and tasking.blacksky.com 302s to login.blacksky.com; BlackSky publishes no developer docs or contract, and the only public spec found (developer.up42.com) is UP42's own reseller API, not BlackSky's.
  evidence:
  - status: 403
    url: https://api.blacksky.com/
  - status: 302
    url: https://tasking.blacksky.com/
  - status: 404
    url: https://blacksky.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-05-24'
description: 'BlackSky Technology (NYSE: BKSY) is a Herndon, Virginia headquartered real-time space-based intelligence company that operates a high-revisit Earth observation constellation and delivers AI-enhanced tactical ISR (intelligence, surveillance, and reconnaissance) imagery and analytics to defense, intelligence, and global security customers. BlackSky''s flagship product is the Spectra platform — a cloud-based intelligence hub that provides on-demand satellite tasking, sub-90-minute imagery delivery, automated AI-driven object detection and change monitoring, archived imagery access, and a secure tasking and delivery API. The company operates Gen-2 satellites at 83 cm resolution and a newer Gen-3 constellation delivering 35 cm class very-high-resolution imagery with infrared sensors, inter-satellite links, and on-board AI processing, manufactured at BlackSky''s facility in Tukwila, Washington. Commercial offerings include BlackSky ON-DEMAND (flexible global tasking) and BlackSky
  ASSURED (dedicated, contracted persistent monitoring capacity). BlackSky''s Spectra tasking and imagery API is integrated into partner platforms including Esri ArcGIS, UP42, and the STAT (Satellite Tasking API) community spec, however the API is access-controlled for vetted defense, intelligence, and enterprise customers and is not exposed as a public self-service developer portal — there is no public Spectra developer documentation site, OpenAPI specification, or open SDKs at the time of this entry. The customer revenue model is subscription-based Spectra ON-DEMAND and ASSURED contracts, Mission Solutions custom engagements, and through marketplace partners.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blacksky.png
jsonld:
- class_count: 120
  name: Blacksky Context
  property_count: 164
  slug: blacksky-context
layout: provider
modified: '2026-05-24'
name: BlackSky
nav: Providers
network: true
overview: 'BlackSky publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Budgets API, Catalog API, Data management API, and 7 more. Tagged areas include Earth Observation, Satellite Imagery, Remote Sensing, Geospatial Intelligence, and Space.


  The BlackSky catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BlackSky''s developer surface includes authentication, getting-started guide, documentation, API reference, YouTube channel, engineering blog, and 31 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: BlackSky API Rules
  rule_count: 16
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 3
  slug: blacksky-rules
scopes:
- name: Blacksky Scopes
  scope_count: 3
  slug: blacksky-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 57.5
    developer_ergonomics: 42.9
    discoverability: 69.6
    operational_transparency: 0.0
  previous_composite: 42.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/blacksky/blacksky-2026-06-20T173337.png
security:
- kind: authentication
  name: Blacksky Authentication
  slug: blacksky-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Blacksky Domain Security
  slug: blacksky-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blacksky
tags:
- Earth Observation
- Satellite Imagery
- Remote Sensing
- Geospatial Intelligence
- Space
- ISR
- Intelligence Surveillance Reconnaissance
- Tasking
- AI Analytics
- Object Detection
- Defense
- Monitoring
- Spectra
- Gen-3
- NYSE BKSY
website: https://blacksky.com
---
