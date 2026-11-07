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
    mcp_server: platform
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
  score: 6.3
  scored_at: '2026-11-06'
api_count: 18
apis:
- description: 'The public WordPress REST API (wp-json) of the Perfect Day website at perfectday.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate AP'
  name: Perfect Day Website (WordPress REST)
  slug: perfectday-com-website-wordpress-rest
artifact_total: 7
common:
- group: other
  href: https://artifacts.apis.io/perfect-day/overlays/perfect-day-media-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/perfect-day-media-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://perfectday.com/
- group: docs
  title: ''
  type: Documentation
  url: https://perfectday.com/wp-json/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.wordpress.org/rest-api/reference/
- group: company
  title: ''
  type: Blog
  url: https://perfectday.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://perfectday.com/blog/feed/
- group: company
  title: ''
  type: Newsroom
  url: https://perfectday.com/newsroom/
- group: operate
  title: ''
  type: Support
  url: https://perfectday.com/contact-us/
- group: operate
  title: ''
  type: FAQ
  url: https://perfectday.com/faqs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://perfectday.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://perfectday.com/privacy-policy/
- group: build
  title: ''
  type: CodeOfConduct
  url: https://perfectday.com/codes-of-conduct-supplier-responsibility/
- group: other
  title: ''
  type: Patents
  url: https://perfectday.com/patents/
- group: company
  title: ''
  type: Careers
  url: https://perfectday.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/perfectday/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/perfectdayfoods
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/perfectdayfoods
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/perfectdayfoods/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/perfect-day_stock/
- group: auth
  href: https://artifacts.apis.io/perfect-day/authentication/perfect-day-authentication.yml
  title: ''
  type: Authentication
  url: authentication/perfect-day-authentication.yml
- group: design
  href: https://artifacts.apis.io/perfect-day/conventions/perfect-day-conventions.yml
  title: ''
  type: Conventions
  url: conventions/perfect-day-conventions.yml
- group: design
  href: https://artifacts.apis.io/perfect-day/errors/perfect-day-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/perfect-day-problem-types.yml
- group: design
  href: https://artifacts.apis.io/perfect-day/data-model/perfect-day-data-model.yml
  title: ''
  type: DataModel
  url: data-model/perfect-day-data-model.yml
- group: design
  href: https://artifacts.apis.io/perfect-day/lifecycle/perfect-day-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/perfect-day-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/perfect-day/conformance/perfect-day-conformance.yml
  title: ''
  type: Conformance
  url: conformance/perfect-day-conformance.yml
- group: agent
  href: https://artifacts.apis.io/perfect-day/well-known/perfect-day-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/perfect-day-well-known.yml
- group: agent
  href: https://artifacts.apis.io/perfect-day/mcp/perfect-day-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/perfect-day-mcp.yml
- group: build
  href: https://artifacts.apis.io/perfect-day/mcp/perfect-day-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/perfect-day-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/perfect-day/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/perfect-day/llms/perfect-day-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/perfect-day-llms.txt
- group: auth
  href: https://artifacts.apis.io/perfect-day/security/perfect-day-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/perfect-day-domain-security.yml
created: '2026-08-02'
description: Perfect Day is a Berkeley, California food-technology company, founded in 2014, that makes animal-free dairy proteins with precision fermentation. Rather than farming cows, Perfect Day ferments microflora carrying milk's protein-coding genes to produce ProFerm, a non-animal whey protein with no lactose, cholesterol, hormones or antibiotics, which it sells business-to-business to consumer brands making ice cream, cream cheese, milk, yogurt, protein powders and bakery products. The company is a member of the Precision Fermentation Alliance. Perfect Day publishes no product or developer API; the single machine-readable surface it operates is the WordPress REST API (wp/v2) behind perfectday.com, which exposes anonymous read access to its blog posts, newsroom items, success stories, pages, media, taxonomies and site search, plus authenticated write operations via WordPress application passwords. This profile was enriched by the API Evangelist pipeline from that live surface.
image: https://perfectday.com/wp-content/uploads/2022/01/social-share-image.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at perfectday.com over HTTP.
  name: Perfect Day MCP Server
  slug: perfect-day-site
modified: '2026-08-02'
name: Perfect Day
nav: Providers
network: true
overview: 'Perfect Day publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Technology, Precision Fermentation, Alternative Protein, and Ingredients.


  Perfect Day''s developer surface includes documentation, API reference, engineering blog, support, FAQ, authentication, and 25 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 37.5
    discoverability: 72.5
    operational_transparency: 0.0
  previous_composite: 20.2
  provenance:
    conformance: derived
    mcp: site-plugin
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
screenshot: https://apis.io/screenshots/perfect-day/perfect-day-2026-09-02T151042.png
security:
- kind: authentication
  name: Perfect Day Authentication
  slug: perfect-day-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Perfect Day Domain Security
  slug: perfect-day-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Harvest Perfect Day partner success stories
  slug: perfect-day-harvest-success-stories
- name: Search Perfect Day site content
  slug: perfect-day-search-site-content
- name: Track the Perfect Day newsroom
  slug: perfect-day-track-newsroom
slug: perfect-day
tags:
- Company
- Food Technology
- Precision Fermentation
- Alternative Protein
- Ingredients
- Sustainability
- Biotechnology
- Consumer Packaged Goods
- content-api
- WordPress
website: https://perfectday.com/
---
