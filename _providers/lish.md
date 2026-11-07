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
  band: human-only
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
  score: 4.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Lish website at www.lishfood.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Lish Website (WordPress REST)
  slug: lishfood-com-website-wordpress-rest
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/lish/mcp/lish-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/lish-mcp.yml
- group: other
  href: https://artifacts.apis.io/lish/overlays/lish-wordpress-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lish-wordpress-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/lish/authentication/lish-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lish-authentication.yml
- group: auth
  href: https://artifacts.apis.io/lish/security/lish-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lish-domain-security.yml
- group: design
  href: https://artifacts.apis.io/lish/conventions/lish-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lish-conventions.yml
- group: design
  href: https://artifacts.apis.io/lish/errors/lish-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lish-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lish/lifecycle/lish-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lish-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/lish/conformance/lish-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lish-conformance.yml
- group: design
  href: https://artifacts.apis.io/lish/data-model/lish-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lish-data-model.yml
- group: agent
  href: https://artifacts.apis.io/lish/llms/lish-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lish-llms.txt
- group: agent
  href: https://artifacts.apis.io/lish/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.lishfood.com
- group: company
  title: ''
  type: Blog
  url: https://www.lishfood.com/blog
- group: company
  title: ''
  type: About
  url: https://www.lishfood.com/pages/about
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.lishfood.com/pages/faq
- group: operate
  title: ''
  type: Support
  url: https://www.lishfood.com/pages/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.lishfood.com/pages/get-started
- group: start
  title: ''
  type: Login
  url: https://www.lishfood.com/account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lishfood.com/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lishfood.com/pages/privacy
created: '2026-07-17'
description: 'Lish is a corporate catering and workplace food service company serving Seattle and the Bellevue/Eastside area of Washington, including Redmond and Kirkland. It connects employers with a curated roster of local partner chefs and runs the whole workplace meal program — menu curation, ordering, delivery and setup — across four service lines: subscription catering, PopUp restaurants that employees buy from directly, on-demand one-off catering, and occasion catering for breakfast, lunch, box lunches, happy hours, meetings and events. The company reports more than 3,000,000 meals served, 100+ curated menus from dozens of partner chefs, an average meal rating of 4.6 stars, and 97.8% of orders delivered on time within a 20-minute window, with dietary accommodation (gluten-free, vegetarian, vegan, dairy-free) as a stated focus. Lish describes an admin dashboard, budget tracking, GPS delivery tracking, Google Calendar and Outlook menu visibility and Slack feedback notifications, but
  these are end-user product integrations — Lish operates no developer program and publishes no product API. The only public, self-describing HTTP API is the WordPress REST API behind its marketing site, profiled here.'
image: https://www.lishfood.com/wp-content/uploads/2024/05/Lish-Hero-Lish_part_two_finals080jpghalf.jpg
layout: provider
modified: '2026-07-19'
name: Lish
nav: Providers
network: true
overview: 'Lish publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Catering, Food and Beverage, Food Delivery, and Workplace.


  Lish''s developer surface includes authentication, engineering blog, support, signup flow, and 16 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 25.6
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 21.3
  provenance:
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
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/lish/lish-2026-07-25T225325.png
security:
- kind: authentication
  name: Lish Authentication
  slug: lish-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lish Domain Security
  slug: lish-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: lish-blog-harvest
  slug: lish-blog-harvest
- name: lish-content-search
  slug: lish-content-search
slug: lish
tags:
- Company
- Catering
- Food and Beverage
- Food Delivery
- Workplace
- Corporate Services
- Content
website: https://www.lishfood.com
---
