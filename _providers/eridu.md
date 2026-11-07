---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
  name: Eridu Agentic Access
  operation_count: 20
  slug: eridu-agentic-access
  summary_line: 20 operations
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Eridu website at eridu.ai: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Eridu Website (WordPress REST)
  slug: eridu-ai-website-wordpress-rest
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://eridu.ai/
- group: company
  title: ''
  type: About
  url: https://eridu.ai/company/
- group: other
  title: ''
  type: Leadership
  url: https://eridu.ai/company/leadership/
- group: company
  title: ''
  type: Blog
  url: https://eridu.ai/resources/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://eridu.ai/feed/
- group: company
  title: ''
  type: Press
  url: https://eridu.ai/resources/press-releases/
- group: company
  title: ''
  type: News
  url: https://eridu.ai/resources/
- group: operate
  title: ''
  type: Contact
  url: https://eridu.ai/contact/
- group: company
  title: ''
  type: Careers
  url: https://ats.rippling.com/eridu-ai/jobs
- group: company
  title: ''
  type: Newsletter
  url: https://eridu.ai/newsletter/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eridu.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eridu.ai/privacy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eridu-ai/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/EriduAI
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/watch?v=ouGlu_Xdggg
- group: other
  title: ''
  type: Sitemap
  url: https://eridu.ai/wp-sitemap.xml
- group: auth
  href: https://artifacts.apis.io/eridu/authentication/eridu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/eridu-authentication.yml
- group: design
  href: https://artifacts.apis.io/eridu/errors/eridu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/eridu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/eridu/conventions/eridu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/eridu-conventions.yml
- group: design
  href: https://artifacts.apis.io/eridu/data-model/eridu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/eridu-data-model.yml
- group: design
  href: https://artifacts.apis.io/eridu/conformance/eridu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eridu-conformance.yml
- group: design
  href: https://artifacts.apis.io/eridu/lifecycle/eridu-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/eridu-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/eridu/rate-limits/eridu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/eridu-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/eridu/plans/eridu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eridu-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/eridu/packages/eridu-packages.yml
  title: ''
  type: Packages
  url: packages/eridu-packages.yml
- group: agent
  href: https://artifacts.apis.io/eridu/llms/eridu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eridu-llms.txt
- group: build
  href: https://artifacts.apis.io/eridu/mcp/eridu-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/eridu-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/eridu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/eridu/examples/eridu-examples.yml
  title: ''
  type: Examples
  url: examples/eridu-examples.yml
- group: agent
  href: https://artifacts.apis.io/eridu/agentic-access/eridu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/eridu-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/eridu/security/eridu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eridu-domain-security.yml
created: '2026-08-12'
description: 'Eridu is an AI networking infrastructure company founded in 2024 and headquartered at 12900 Saratoga Ave in Saratoga, California. It is building a clean-sheet network switch architecture — silicon, systems and software together — aimed at the interconnect bottleneck that limits how efficiently GPUs exchange data inside large AI training clusters and data centers. The company was co-founded by CEO Drew Perkins, who previously co-founded Lightera Networks (acquired by Ciena) and Infinera, alongside Chief Product Officer Omar Hassen, and emerged from stealth in March 2026 with an oversubscribed Series A of more than $200M led by Socratic Partners, bringing total funding to approximately $230M with participation from John Doerr, Kleiner Perkins, Hudson River Trading, Capricorn Investment Group, Matter Venture Partners and Fusion Fund. Eridu is a semiconductor and systems company rather than a software vendor: it publishes no developer program, no developer portal, no product API,
  no SDKs and no pricing. The only machine-readable interface it serves is the WordPress core REST API behind its corporate site at eridu.ai, captured here for discovery purposes and anonymously readable but effectively read-only.'
image: https://eridu.ai/apple-touch-icon.png
layout: provider
modified: '2026-08-12'
name: Eridu
nav: Providers
network: true
overview: 'Eridu publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Infrastructure, Networking, and Semiconductors.


  Eridu''s developer surface includes engineering blog, product news, YouTube channel, authentication, code examples, and 26 more developer resources.'
plans:
- name: Eridu Plans Pricing
  plan_count: 0
  slug: eridu-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Eridu Rate Limits
  slug: eridu-rate-limits
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 6.5
    developer_ergonomics: 20.8
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 19.3
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
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/eridu/eridu-2026-09-02T145417.png
security:
- kind: authentication
  name: Eridu Authentication
  slug: eridu-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Eridu Domain Security
  slug: eridu-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: Discover the Eridu API surface
  slug: eridu-discover-the-surface
- name: Harvest Eridu media assets
  slug: eridu-harvest-media
- name: Read the Eridu company profile
  slug: eridu-read-company-profile
- name: Track Eridu announcements and press
  slug: eridu-track-announcements
slug: eridu
tags:
- Company
- Artificial Intelligence
- AI Infrastructure
- Networking
- Semiconductors
- Data Center
- Silicon
- Network Switching
- Interconnect
- Hardware
website: https://eridu.ai/
---
