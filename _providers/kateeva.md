---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Kateeva Agentic Access
  operation_count: 21
  slug: kateeva-agentic-access
  summary_line: 21 operations
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Kateeva website at kateeva.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Kateeva Website (WordPress REST)
  slug: kateeva-com-website-wordpress-rest
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/kateeva/security/kateeva-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kateeva-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kateeva.com/
- group: company
  title: ''
  type: About
  url: https://kateeva.com/company/about/overview/
- group: other
  title: ''
  type: Leadership
  url: https://kateeva.com/company/about/leadership/
- group: other
  title: ''
  type: History
  url: https://kateeva.com/company/about/history-awards/
- group: other
  title: ''
  type: Regions
  url: https://kateeva.com/company/about/regions/
- group: other
  title: ''
  type: Sustainability
  url: https://kateeva.com/company/sustainability/
- group: other
  title: ''
  type: Products
  url: https://kateeva.com/solutions/products/
- group: other
  title: ''
  type: Technology
  url: https://kateeva.com/solutions/technology/yieldjet-platform/
- group: other
  title: ''
  type: Applications
  url: https://kateeva.com/solutions/applications/
- group: company
  title: ''
  type: Partners
  url: https://kateeva.com/solutions/collaborations/
- group: other
  title: ''
  type: Services
  url: https://kateeva.com/services/
- group: company
  title: ''
  type: Blog
  url: https://kateeva.com/company/newsroom/kateeva-blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://kateeva.com/feed/
- group: company
  title: ''
  type: Press
  url: https://kateeva.com/company/newsroom/press-releases/
- group: company
  title: ''
  type: News
  url: https://kateeva.com/company/newsroom/in-the-news/
- group: other
  title: ''
  type: Events
  url: https://kateeva.com/company/newsroom/events/
- group: operate
  title: ''
  type: Contact
  url: https://kateeva.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://kateeva.com/careers/job-openings/
- group: other
  title: ''
  type: SiteMap
  url: https://kateeva.com/site-map/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kateeva.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kateeva.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kateeva
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/KateevaInc
- group: auth
  href: https://artifacts.apis.io/kateeva/authentication/kateeva-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kateeva-authentication.yml
- group: design
  href: https://artifacts.apis.io/kateeva/errors/kateeva-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kateeva-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kateeva/conventions/kateeva-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kateeva-conventions.yml
- group: design
  href: https://artifacts.apis.io/kateeva/data-model/kateeva-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kateeva-data-model.yml
- group: design
  href: https://artifacts.apis.io/kateeva/conformance/kateeva-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kateeva-conformance.yml
- group: design
  href: https://artifacts.apis.io/kateeva/lifecycle/kateeva-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kateeva-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/kateeva/rate-limits/kateeva-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kateeva-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kateeva/plans/kateeva-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kateeva-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/kateeva/examples/kateeva-examples.yml
  title: ''
  type: Examples
  url: examples/kateeva-examples.yml
- group: agent
  href: https://artifacts.apis.io/kateeva/llms/kateeva-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kateeva-llms.txt
- group: build
  href: https://artifacts.apis.io/kateeva/mcp/kateeva-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/kateeva-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/kateeva/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/kateeva/agentic-access/kateeva-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kateeva-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/kateeva/packages/kateeva-packages.yml
  title: ''
  type: Packages
  url: packages/kateeva-packages.yml
created: '2026-08-23'
description: 'Kateeva is a Silicon Valley capital-equipment company that builds inkjet printing systems for manufacturing advanced displays. It was co-founded in 2008 by Conor Madigan, PhD, Valerie Gassend, PhD, and Gerry Chen, PhD, on the conviction that precision inkjet deposition could make OLED displays mass-producible at cost. The company introduced its YIELDjet platform in 2013 — the display industry''s first inkjet equipment solution for depositing the organic thin film encapsulation (TFE) layer of an OLED panel — and shipped the first commercial YIELDjet FLEX system a year later, which became the market-leading tool for flexible mobile OLED mass production. Its current product line is the YIELDjet Lassen, Jarvis, Tioga and Kuna printers, spanning substrate sizes and applications from TFE to OLED RGB pixel deposition and microlens planarization. Kateeva moved its global headquarters to Newark, California in 2015 and operates in China, Korea, Japan and Taiwan; it raised roughly $200
  million through a 2016 Series E backed by BOE, TCL Capital, Redview Capital, Samsung Venture Investment, Sigma Partners, Spark Capital, Madrone Capital Partners, DBL Partners and Veeco. Kateeva sells machines to display panel makers, not software: it publishes no developer program, no developer portal, no SDKs and no API documentation of any kind. The only machine-readable interface it exposes is the WordPress REST content API behind its corporate website at kateeva.com, which is captured here for discovery purposes and is anonymously readable but read-only.'
image: https://kateeva.com/wp-content/uploads/2021/10/Kateeva_Logo_RGB.svg
layout: provider
modified: '2026-08-23'
name: Kateeva
nav: Providers
network: true
overview: 'Kateeva is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Display Manufacturing, OLED, Semiconductor Equipment, and Capital Equipment.


  Kateeva''s developer surface includes engineering blog, product news, authentication, code examples, and 34 more developer resources.'
plans:
- name: Kateeva Plans Pricing
  plan_count: 0
  slug: kateeva-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Kateeva Rate Limits
  slug: kateeva-rate-limits
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 6.5
    developer_ergonomics: 20.8
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 19.5
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kateeva/kateeva-2026-09-02T150024.png
security:
- kind: authentication
  name: Kateeva Authentication
  slug: kateeva-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Kateeva Domain Security
  slug: kateeva-domain-security
  summary_line: TLSv1.2 · DMARC
skill_count: 2
skills:
- name: Map the Kateeva site, products and company facts
  slug: kateeva-map-company-and-products
- name: Read the Kateeva newsroom archive
  slug: kateeva-read-newsroom-archive
slug: kateeva
tags:
- Company
- Display Manufacturing
- OLED
- Semiconductor Equipment
- Capital Equipment
- Inkjet Printing
- Thin Film Encapsulation
- Advanced Manufacturing
- Materials Deposition
- Consumer Electronics
- Hardware
website: https://kateeva.com/
---
