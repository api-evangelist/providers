---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
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
  score: 5.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Uncle Nearest Agentic Access
  operation_count: 47
  slug: uncle-nearest-agentic-access
  summary_line: 47 operations · 25 acting
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the Uncle Nearest website at unclenearest.com: the route index of the site''s content management system, catalogued as one site surface rather than as separat'
  name: Uncle Nearest Website (WordPress REST)
  slug: unclenearest-com-website-wordpress-rest
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/uncle-nearest/mcp/uncle-nearest-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/uncle-nearest-mcp.yml
- group: other
  href: https://artifacts.apis.io/uncle-nearest/overlays/uncle-nearest-events-calendar-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/uncle-nearest-events-calendar-v1-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/uncle-nearest/agentic-access/uncle-nearest-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/uncle-nearest-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://unclenearest.com/
- group: company
  title: ''
  type: Investors
  url: https://forgeglobal.com/uncle-nearest_stock/
- group: company
  title: ''
  type: About
  url: https://unclenearest.com/history
- group: company
  title: ''
  type: Press
  url: https://unclenearest.com/press/
- group: operate
  title: ''
  type: Contact
  url: https://unclenearest.com/contact-us/
- group: operate
  title: ''
  type: Support
  url: https://unclenearest.com/contact-us/
- group: operate
  title: ''
  type: FAQ
  url: https://unclenearest.com/nearest-green-distillery-faqs/
- group: other
  title: ''
  type: Events
  url: https://unclenearest.com/live/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unclenearest.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unclenearest.com/privacy/
- group: other
  title: ''
  type: Accessibility
  url: https://unclenearest.com/accessibility/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/unclenearest
- group: company
  title: ''
  type: Facebook
  url: https://facebook.com/unclenearest
- group: company
  title: ''
  type: Instagram
  url: https://instagram.com/unclenearest
- group: learn
  title: ''
  type: Youtube
  url: https://www.youtube.com/channel/UCcfM0XBsHSQRB18ssOImb_g
- group: auth
  href: https://artifacts.apis.io/uncle-nearest/authentication/uncle-nearest-authentication.yml
  title: ''
  type: Authentication
  url: authentication/uncle-nearest-authentication.yml
- group: design
  href: https://artifacts.apis.io/uncle-nearest/conventions/uncle-nearest-conventions.yml
  title: ''
  type: Conventions
  url: conventions/uncle-nearest-conventions.yml
- group: design
  href: https://artifacts.apis.io/uncle-nearest/errors/uncle-nearest-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/uncle-nearest-problem-types.yml
- group: design
  href: https://artifacts.apis.io/uncle-nearest/data-model/uncle-nearest-data-model.yml
  title: ''
  type: DataModel
  url: data-model/uncle-nearest-data-model.yml
- group: design
  href: https://artifacts.apis.io/uncle-nearest/conformance/uncle-nearest-conformance.yml
  title: ''
  type: Conformance
  url: conformance/uncle-nearest-conformance.yml
- group: design
  href: https://artifacts.apis.io/uncle-nearest/lifecycle/uncle-nearest-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/uncle-nearest-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/uncle-nearest/security/uncle-nearest-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uncle-nearest-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/uncle-nearest/llms/uncle-nearest-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/uncle-nearest-llms.txt
- group: agent
  href: https://artifacts.apis.io/uncle-nearest/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: Uncle Nearest, Inc. is an American whiskey company headquartered in Shelbyville, Tennessee, founded in 2017 by Fawn Weaver and Keith Weaver and named for Nathan "Nearest" Green, the formerly enslaved master distiller who taught Jack Daniel the craft. The company produces the Uncle Nearest 1856 Premium Aged, 1884 Small Batch, Master Blend, Single Barrel, Straight Rye and Uncut/Unfiltered Rye expressions, and operates the Nearest Green Distillery visitor destination in Shelbyville with tours, tastings, private events and a retail shop. Uncle Nearest is a privately held, consumer-facing brand with no developer program and no product API; its only public machine-readable surfaces are the WordPress REST API and the two OpenAPI-documented Events Calendar REST APIs served from its own web host at unclenearest.com, which expose the brand's published events, venues and organizers as read-only JSON.
image: https://unclenearest.com/wp-content/themes/unclenearest/lib/img/un-logo-2022.svg
layout: provider
modified: '2026-08-02'
name: Uncle Nearest
nav: Providers
network: true
overview: 'Uncle Nearest publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Whiskey, Spirits, Beverage Alcohol, and Consumer Packaged Goods.


  Uncle Nearest''s developer surface includes support, FAQ, YouTube channel, authentication, and 23 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 23.2
    discoverability: 65.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 15.7
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
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/uncle-nearest/uncle-nearest-2026-09-02T164843.png
security:
- kind: authentication
  name: Uncle Nearest Authentication
  slug: uncle-nearest-authentication
  summary_line: http/none · 2 schemes
- kind: domain-security
  name: Uncle Nearest Domain Security
  slug: uncle-nearest-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Find upcoming Uncle Nearest events
  slug: uncle-nearest-find-upcoming-events
- name: Map Uncle Nearest venues and organizers
  slug: uncle-nearest-map-venues-and-organizers
slug: uncle-nearest
tags:
- Company
- Whiskey
- Spirits
- Beverage Alcohol
- Consumer Packaged Goods
- Distillery
- Hospitality
- Event
- Tennessee
- WordPress
website: https://unclenearest.com/
---
