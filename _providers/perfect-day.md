---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-08-03'
api_count: 16
apis:
- description: The WordPress REST `posts` resource behind perfectday.com — 71 published blog posts, with collection, single-item, revision and autosave routes. Read access is anonymous; writes require a WordPress ap
  name: Perfect Day posts API
  slug: perfect-day-posts-api
- description: The `news` custom post type behind the Perfect Day newsroom — 103 items covering partner launches, regulatory milestones and company announcements. Read access is anonymous.
  name: Perfect Day news API
  slug: perfect-day-news-api
- description: The `success_story` custom post type — Perfect Day's published partner/brand case studies, classified by the `success_story_category` taxonomy. Read access is anonymous.
  name: Perfect Day success stories API
  slug: perfect-day-success-stories-api
- description: The WordPress REST `pages` resource — 59 published marketing and information pages (ProFerm, applications, process, impact, health, FAQs). Read access is anonymous.
  name: Perfect Day pages API
  slug: perfect-day-pages-api
- description: The WordPress REST `search` resource — cross-content-type search across posts, pages, news and success stories on perfectday.com. Read access is anonymous.
  name: Perfect Day search API
  slug: perfect-day-search-api
- description: The WordPress REST `media` resource — the site's image and document library, including product photography and press assets. Read access is anonymous; uploads require authentication.
  name: Perfect Day media API
  slug: perfect-day-media-api
- description: The WordPress REST `categories` taxonomy for blog posts on perfectday.com.
  name: Perfect Day categories API
  slug: perfect-day-categories-api
- description: The `news_category` custom taxonomy that classifies Perfect Day newsroom items.
  name: Perfect Day news categories API
  slug: perfect-day-news-categories-api
- description: The `success_story_category` custom taxonomy that classifies Perfect Day case studies.
  name: Perfect Day success story categories API
  slug: perfect-day-success-story-categories-api
- description: The `leader_category` custom taxonomy that groups Perfect Day leadership profiles.
  name: Perfect Day leader categories API
  slug: perfect-day-leader-categories-api
- description: The WordPress REST `tags` taxonomy on perfectday.com.
  name: Perfect Day tags API
  slug: perfect-day-tags-api
- description: The WordPress REST `comments` resource on perfectday.com.
  name: Perfect Day comments API
  slug: perfect-day-comments-api
- description: The WordPress REST `taxonomies` resource — enumerates the seven taxonomies registered on perfectday.com, including the custom news, success-story and leader taxonomies.
  name: Perfect Day taxonomies API
  slug: perfect-day-taxonomies-api
- description: The WordPress REST `types` resource — enumerates the content types registered on perfectday.com, including the news, success_story and modal custom post types.
  name: Perfect Day types API
  slug: perfect-day-types-api
- description: The WordPress REST `statuses` resource on perfectday.com.
  name: Perfect Day statuses API
  slug: perfect-day-statuses-api
- description: The `modal` custom post type used for site interstitials on perfectday.com.
  name: Perfect Day modals API
  slug: perfect-day-modals-api
artifact_total: 19
common:
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
  title: ''
  type: Authentication
  url: authentication/perfect-day-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/perfect-day-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/perfect-day-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/perfect-day-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/perfect-day-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/perfect-day-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/perfect-day-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/perfect-day-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/perfect-day-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/perfect-day-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/perfect-day-domain-security.yml
created: '2026-08-02'
description: Perfect Day is a Berkeley, California food-technology company, founded in 2014, that makes animal-free dairy proteins with precision fermentation. Rather than farming cows, Perfect Day ferments microflora carrying milk's protein-coding genes to produce ProFerm, a non-animal whey protein with no lactose, cholesterol, hormones or antibiotics, which it sells business-to-business to consumer brands making ice cream, cream cheese, milk, yogurt, protein powders and bakery products. The company is a member of the Precision Fermentation Alliance. Perfect Day publishes no product or developer API; the single machine-readable surface it operates is the WordPress REST API (wp/v2) behind perfectday.com, which exposes anonymous read access to its blog posts, newsroom items, success stories, pages, media, taxonomies and site search, plus authenticated write operations via WordPress application passwords. This profile was enriched by the API Evangelist pipeline from that live surface.
image: https://perfectday.com/wp-content/uploads/2022/01/social-share-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: perfect-day-mcp.yml
  slug: perfect-day-mcpyml
modified: '2026-08-02'
name: Perfect Day
nav: Providers
network: true
overview: 'Perfect Day publishes 16 APIs on the [APIs.io](https://apis.io/) network, including posts API, news API, success stories API, and 13 more. Tagged areas include Company, Food Technology, Precision Fermentation, Alternative Protein, and Ingredients.


  Perfect Day''s developer surface includes documentation, API reference, engineering blog, support, FAQ, authentication, and 24 more developer resources.'
random_paper: 63
score:
  band: thin
  composite: 39.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 64.5
    developer_ergonomics: 42.9
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Perfect Day Authentication
  slug: perfect-day-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Perfect Day Domain Security
  slug: perfect-day-domain-security
  summary_line: TLSv1.3 · DMARC
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
- Content API
- WordPress
website: https://perfectday.com/
---
