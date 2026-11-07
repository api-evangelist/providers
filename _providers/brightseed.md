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
- acting_count: 51
  human_in_the_loop: 0
  name: Brightseed Agentic Access
  operation_count: 84
  slug: brightseed-agentic-access
  summary_line: 84 operations · 51 acting
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Brightseed website at www.brightseedbio.com: the route index of the site''s content management system, catalogued as one site surface rather than as separ'
  name: Brightseed Website (WordPress REST)
  slug: brightseedbio-com-website-wordpress-rest
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/brightseed/capabilities/brightseed-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/brightseed-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/brightseed/authentication/brightseed-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brightseed-authentication.yml
- group: design
  href: https://artifacts.apis.io/brightseed/conventions/brightseed-conventions.yml
  title: ''
  type: Conventions
  url: conventions/brightseed-conventions.yml
- group: design
  href: https://artifacts.apis.io/brightseed/errors/brightseed-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/brightseed-problem-types.yml
- group: design
  href: https://artifacts.apis.io/brightseed/data-model/brightseed-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brightseed-data-model.yml
- group: design
  href: https://artifacts.apis.io/brightseed/lifecycle/brightseed-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/brightseed-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/brightseed/conformance/brightseed-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brightseed-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brightseed/well-known/brightseed-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brightseed-well-known.yml
- group: agent
  href: https://artifacts.apis.io/brightseed/mcp/brightseed-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/brightseed-mcp.yml
- group: agent
  href: https://artifacts.apis.io/brightseed/skills/brightseed-browse-site-content.md
  title: ''
  type: AgentSkill
  url: skills/brightseed-browse-site-content.md
- group: agent
  href: https://artifacts.apis.io/brightseed/skills/brightseed-search-site-content.md
  title: ''
  type: AgentSkill
  url: skills/brightseed-search-site-content.md
- group: agent
  href: https://artifacts.apis.io/brightseed/agentic-access/brightseed-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/brightseed-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/brightseed/llms/brightseed-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brightseed-llms.txt
- group: auth
  href: https://artifacts.apis.io/brightseed/security/brightseed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brightseed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brightseedbio.com/
- group: company
  title: ''
  type: About
  url: https://www.brightseedbio.com/team/
- group: other
  title: ''
  type: Team
  url: https://www.brightseedbio.com/team/
- group: company
  title: ''
  type: Blog
  url: https://resources.brightseedbio.com/knowledgebase
- group: company
  title: ''
  type: BlogFeeds
  url: https://www.brightseedbio.com/feed/
- group: company
  title: ''
  type: Newsroom
  url: https://www.brightseedbio.com/newsroom/
- group: company
  title: ''
  type: Careers
  url: https://www.brightseedbio.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.brightseedbio.com/contact-us/
- group: other
  title: ''
  type: Patents
  url: https://www.brightseedbio.com/patents/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Brightseed
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brightseedinc
- group: company
  title: ''
  type: Twitter
  url: https://x.com/brightseedbio
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brightseedbio.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brightseedbio.com/terms-of-use/
created: '2026-07-31'
description: Brightseed is a bioactives and AI company founded in 2017 (San Francisco, CA, with operations in Durham, NC) that uses its Forager AI platform to map the compounds in plants to human biological pathways and health benefits. Forager draws on a proprietary dataset the company describes as the world's largest — 21 million bioactive compounds and hundreds of biological receptors spanning 23 health areas — combining high-resolution omics, high-throughput robotics and machine learning to predict which natural compounds confer a benefit and where to source them at commercial scale. Hummingbird, launched in 2026, layers an agentic AI system on top of Forager to carry partners from discovery through development. Brightseed sells discovery services (Bioactive Profiler, Bioactive Ingredient Finder) and market-ready ingredients (Bio Gut Fiber, Bio Meta Control, Bio Gut Core) to food, supplement and health-science companies. Brightseed publishes no product or developer API for Forager or
  Hummingbird — those are sold as enterprise engagements through a contact form. The single machine-readable surface the company operates is the WordPress REST API (wp/v2) behind its corporate site at www.brightseedbio.com, which exposes anonymous read access to posts, pages, categories, tags, users, media, comments, search, taxonomies, types and statuses, plus authenticated write operations via WordPress application passwords. This profile was enriched by the API Evangelist pipeline from that live surface.
image: https://www.brightseedbio.com/wp-content/uploads/2025/07/cropped-Logo-1-270x270.png
layout: provider
modified: '2026-07-31'
name: Brightseed
nav: Providers
network: true
overview: 'Brightseed is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bioactives, Artificial Intelligence, Life Sciences, and Nutrition.


  Brightseed''s developer surface includes authentication, engineering blog, and 26 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 65.2
    operational_transparency: 2.6
  previous_composite: 17.7
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/brightseed/brightseed-2026-08-07T162813.png
security:
- kind: authentication
  name: Brightseed Authentication
  slug: brightseed-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Brightseed Domain Security
  slug: brightseed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: brightseed-browse-site-content
  slug: brightseed-browse-site-content
- name: brightseed-search-site-content
  slug: brightseed-search-site-content
slug: brightseed
tags:
- Company
- Bioactives
- Artificial Intelligence
- Life Sciences
- Nutrition
- Ingredients
- Drug Discovery
- Agrifood
- content-api
- WordPress
website: https://www.brightseedbio.com/
---
