---
access_model:
  confidence: medium
  label: Public read-only content API, no signup, no published pricing
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - plans
  - https://corporate.americangreetings.com/wp-json/wp/v2/products
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://corporate.americangreetings.com/wp-json
  baseurl_source: declared
  description: The WordPress REST API served by American Greetings from its corporate site. It advertises a self-describing route index at /wp-json/ carrying 586 routes across 23 namespaces, of which wp/v2 is the pu
  name: American Greetings Corporate WordPress REST API
  slug: american-greetings-corporate-wordpress-rest-api
- description: An api. host that resolves through Akamai but returns an identical "Access Denied" 403 HTML body to every non-browser client on every path, including the site root. No documentation, no contract and n
  name: American Greetings API
  slug: american-greetings-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/american-greetings-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/american-greetings-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/american-greetings-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/american-greetings-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/american-greetings-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/american-greetings-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/american-greetings-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/american-greetings-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/american-greetings-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/american-greetings-finops.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/american-greetings-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aginteractive
- group: company
  title: ''
  type: Blog
  url: https://corporate.americangreetings.com/latest-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://corporate.americangreetings.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://corporate.americangreetings.com/about-us/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/american-greetings
- group: company
  title: ''
  type: Website
  url: https://www.americangreetings.com
created: '2026-04-19'
description: 'American Greetings is a privately held American manufacturer and marketer of social expression products — greeting cards, gift packaging, party goods, stationery, stickers and decals, and digital greetings — headquartered in Westlake, Ohio, and selling through mass retail, grocery, drug and specialty channels in North America and internationally. Its brand portfolio includes American Greetings, Papyrus, Carlton Cards, Jacquie Lawson and Blue Mountain. The company operates no public developer programme: there is no developer portal, no published API documentation, no SDK in any package registry, and no API pricing. The one machine-readable API it serves in public is the WordPress REST API on its corporate site, which exposes the company''s own brand and product-line catalogue as custom post types alongside its press releases and media library, readable anonymously.'
finops:
- name: American Greetings Finops
  service_category: Consumer Goods / Retail
  slug: american-greetings-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/american-greetings.png
layout: provider
modified: '2026-09-02'
name: American Greetings
nav: Providers
network: true
overview: 'American Greetings publishes 1 API on the [APIs.io](https://apis.io/) network: Corporate WordPress REST API. Tagged areas include Greeting Cards, Gift Wrap, Celebration, Consumer Products, and Retail.


  American Greetings'' developer surface includes authentication, engineering blog, support, and 15 more developer resources.'
plans:
- name: American Greetings Plans Pricing
  plan_count: 1
  slug: american-greetings-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: American Greetings Rate Limits
  slug: american-greetings-rate-limits
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 43.0
    catalog_earned_first_party: 8.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 58.5
    developer_ergonomics: 20.8
    discoverability: 59.3
    governance: 4.5
    operational_transparency: 5.3
  previous_composite: 30.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/american-greetings/refs/heads/main/screenshots/american-greetings-2026-06-20T171917.png
security:
- kind: authentication
  name: American Greetings Authentication
  slug: american-greetings-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: American Greetings Domain Security
  slug: american-greetings-domain-security
  summary_line: TLSv1.3 · DMARC
slug: american-greetings
tags:
- Greeting Cards
- Gift Wrap
- Celebration
- Consumer Products
- Retail
- Stationery
- Party Supplies
- Digital Greetings
- Content API
- WordPress REST API
website: https://www.americangreetings.com
---
