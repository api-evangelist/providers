---
access_model:
  confidence: high
  label: Public read-only content API, no signup
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Burger Singh Agentic Access
  operation_count: 15
  slug: burger-singh-agentic-access
  summary_line: 15 operations
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Burger Singh website at www.burgersinghonline.com: the route index of the site''s content management system, catalogued as one site surface rather than as'
  name: Burger Singh Website (WordPress REST)
  slug: burgersinghonline-com-website-wordpress-rest
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.burgersinghonline.com/
- group: company
  title: ''
  type: About
  url: https://www.burgersinghonline.com/about-us/
- group: operate
  title: ''
  type: Support
  url: https://www.burgersinghonline.com/feedback/
- group: operate
  title: ''
  type: Contact
  url: https://www.burgersinghonline.com/complaint/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.burgersinghonline.com/terms-and-conditions/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/BurgerSinghs
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/BurgerSinghIndia
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/burgersinghofficial/
- group: auth
  href: https://artifacts.apis.io/burger-singh/authentication/burger-singh-authentication.yml
  title: ''
  type: Authentication
  url: authentication/burger-singh-authentication.yml
- group: design
  href: https://artifacts.apis.io/burger-singh/errors/burger-singh-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/burger-singh-problem-types.yml
- group: design
  href: https://artifacts.apis.io/burger-singh/conventions/burger-singh-conventions.yml
  title: ''
  type: Conventions
  url: conventions/burger-singh-conventions.yml
- group: design
  href: https://artifacts.apis.io/burger-singh/data-model/burger-singh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/burger-singh-data-model.yml
- group: design
  href: https://artifacts.apis.io/burger-singh/conformance/burger-singh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/burger-singh-conformance.yml
- group: design
  href: https://artifacts.apis.io/burger-singh/lifecycle/burger-singh-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/burger-singh-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/burger-singh/well-known/burger-singh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/burger-singh-well-known.yml
- group: auth
  href: https://artifacts.apis.io/burger-singh/security/burger-singh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/burger-singh-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/burger-singh/llms/burger-singh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/burger-singh-llms.txt
- group: agent
  href: https://artifacts.apis.io/burger-singh/mcp/burger-singh-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/burger-singh-mcp.yml
- group: build
  href: https://artifacts.apis.io/burger-singh/mcp/burger-singh-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/burger-singh-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/burger-singh/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/burger-singh/agentic-access/burger-singh-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/burger-singh-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/burger-singh/examples/burger-singh-examples.yml
  title: ''
  type: Examples
  url: examples/burger-singh-examples.yml
created: '2026-08-08'
description: 'Burger Singh is an Indian quick-service restaurant chain founded in 2014 by Kabir Jeet Singh with co-founders Nitin Rana and Rahul Seth, and operated by Tipping Mr Pink Private Limited out of Gurugram, Haryana. It sells Indian-flavoured "craft" burgers - regional recipes built on Indian spices and chutneys - alongside fries and sides, desserts and beverages, through a hybrid estate of company-owned and franchised outlets that spans high-street, food-court, express and dine-in formats across India and into the United Kingdom. The business grows primarily through franchising, and its public web surface is organised around that motion: a menu, a store locator, franchise investment brackets, property-partner and bulk-order intake, and a complaint and feedback channel. Burger Singh is a restaurant operator rather than a software vendor and publishes no developer program, no API documentation and no commercial or partner-facing API. The only machine-readable interface it exposes
  is the WordPress REST content API behind its corporate site at burgersinghonline.com, captured here for discovery purposes.'
image: https://www.burgersinghonline.com/wp-content/uploads/2024/04/cropped-logo-v0.1-2.png
layout: provider
modified: '2026-08-08'
name: Burger Singh
nav: Providers
network: true
overview: 'Burger Singh is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Quick Service Restaurant, Food and Beverage, and Franchising.


  Burger Singh''s developer surface includes support, authentication, code examples, and 19 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 6.5
    developer_ergonomics: 23.2
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 16.4
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/burger-singh/burger-singh-2026-09-02T144958.png
security:
- kind: authentication
  name: Burger Singh Authentication
  slug: burger-singh-authentication
  summary_line: none/cookie/http-basic · 3 schemes
- kind: domain-security
  name: Burger Singh Domain Security
  slug: burger-singh-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: Find and read Burger Singh brand content
  slug: burger-singh-find-brand-content
- name: Harvest Burger Singh site content and media
  slug: burger-singh-harvest-site-content
- name: Read the Burger Singh franchise taxonomy
  slug: burger-singh-read-franchise-taxonomy
slug: burger-singh
tags:
- Company
- Restaurant
- Quick Service Restaurant
- Food and Beverage
- Franchising
- Consumer
- India
- Retail
- WordPress
website: https://www.burgersinghonline.com/
---
