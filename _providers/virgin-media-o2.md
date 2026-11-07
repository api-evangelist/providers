---
access_model:
  confidence: low
  gated: partner
  gated_source:
  - tag:Partner Gated
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Virgin Media O2 website at news.virginmediao2.co.uk: the route index of the site''s content management system, catalogued as one site surface rather than '
  name: Virgin Media O2 Website (WordPress REST)
  slug: news-virginmediao2-co-uk-website-wordpress-rest
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/virgin-media-o2/security/virgin-media-o2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/virgin-media-o2-domain-security.yml
- group: design
  href: https://artifacts.apis.io/virgin-media-o2/conformance/virgin-media-o2-conformance.yml
  title: ''
  type: Conformance
  url: conformance/virgin-media-o2-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://news.virginmediao2.co.uk/wp-content/uploads/2026/01/Virgin-Media-O2-Security-Schedule-Version-7.0-Jan-2026.pdf
- group: design
  href: https://artifacts.apis.io/virgin-media-o2/lifecycle/virgin-media-o2-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/virgin-media-o2-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.o2.co.uk
- group: operate
  title: ''
  type: StatusPage
  url: https://www.virginmedia.com/help/service-status
- group: agent
  href: https://artifacts.apis.io/virgin-media-o2/llms/virgin-media-o2-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/virgin-media-o2-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://www.virginmediao2.co.uk/help
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.o2.co.uk/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.virginmediao2.co.uk/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.virginmediao2.co.uk/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.virginmediao2.co.uk/
- group: company
  title: ''
  type: Website
  url: https://www.virginmediao2business.co.uk/
- group: company
  title: ''
  type: Website
  url: https://www.o2.co.uk/
- group: company
  title: ''
  type: Blog
  url: https://news.virginmediao2.co.uk/news-views/
- group: company
  title: ''
  type: BlogRSS
  url: https://news.virginmediao2.co.uk/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VirginMediaO2
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/virgin-media-o2
- group: other
  href: https://artifacts.apis.io/virgin-media-o2/review.yml
  title: ''
  type: Review
  url: review.yml
- group: other
  href: https://artifacts.apis.io/virgin-media-o2/well-known/virgin-media-o2-newsroom-wp-json-index.json
  title: ''
  type: APICatalog
  url: well-known/virgin-media-o2-newsroom-wp-json-index.json
- group: docs
  href: https://artifacts.apis.io/virgin-media-o2/json-schema/virgin-media-o2-newsroom-category.json
  title: ''
  type: JSONSchema
  url: json-schema/virgin-media-o2-newsroom-category.json
- group: docs
  href: https://artifacts.apis.io/virgin-media-o2/json-schema/virgin-media-o2-newsroom-tag.json
  title: ''
  type: JSONSchema
  url: json-schema/virgin-media-o2-newsroom-tag.json
created: '2026-07-25'
description: 'Virgin Media O2 is the United Kingdom''s converged fixed and mobile network operator, formed in 2021 as a 50/50 joint venture between Telefonica and Liberty Global by merging Virgin Media''s cable broadband business with O2 UK''s mobile network. It serves roughly half the UK population across mobile, broadband, and fixed wholesale, and sits at the connectivity layer of the telecom value chain rather than the developer-tools layer. Its API posture is partner-gated and sales-led: probing developer.virginmediao2.co.uk, developers.virginmediao2.co.uk, docs.virginmediao2.co.uk, api.virginmediao2.co.uk, opengateway.virginmediao2.co.uk, developer.o2.co.uk and the virginmediao2business.co.uk equivalents returns DNS failure or HTTP 404 in every case, and neither the o2.co.uk sitemap nor the corporate site contains a developer or API section. Virgin Media O2 is a GSMA Open Gateway participant and on 23 September 2025 joined BT/EE, Vodafone and CK Hutchison (Three UK) in the commercial
  UK launch of CAMARA-standardised KYC Age Verification and KYC Tenure APIs, with SIM Swap already live and KYC Match committed; but developers reach that network-API surface only through third-party aggregators such as JT Group and TMT.ID, never through a Virgin Media O2 portal. There is no public self-serve signup, no downloadable OpenAPI, no sandbox, and no first-party SDK. Its GitHub organisation exists and is empty.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: category
  property_count: 10
  slug: virgin-media-o2-newsroom-category
- name: tag
  property_count: 8
  slug: virgin-media-o2-newsroom-tag
layout: provider
modified: '2026-07-25'
name: Virgin Media O2
nav: Providers
network: true
overview: 'Virgin Media O2 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, United Kingdom, Mobile Network Operator, Broadband, and Network APIs.


  Virgin Media O2''s developer surface includes support, engineering blog, and 20 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.3
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 20.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/virgin-media-o2/virgin-media-o2-2026-09-02T170000.png
security:
- kind: domain-security
  name: Virgin Media O2 Domain Security
  slug: virgin-media-o2-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: virgin-media-o2
tags:
- Telecommunications
- United Kingdom
- Mobile Network Operator
- Broadband
- Network APIs
- CAMARA
- Open Gateway
- Identity Verification
- SIM Swap
- Age Verification
- Converged Operator
website: https://www.virginmediao2.co.uk/
---
