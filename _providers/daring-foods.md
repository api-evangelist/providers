---
access_model:
  confidence: high
  label: Public read-only content API, no signup
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Daring Foods Agentic Access
  operation_count: 31
  slug: daring-foods-agentic-access
  summary_line: 31 operations
api_count: 14
apis:
- description: 'Public, unauthenticated read access to the Daring recipe library via the site''s custom `recipes` WordPress post type. Verified live at 208 published recipes, each classified by cooking method through '
  name: Daring Foods Recipes API
  slug: daring-foods-recipes-api
- description: Public, unauthenticated read access to the Daring retail plant-chicken catalog via the custom `products` post type - Original Shredded and Diced Plant Chicken, the Plant Chicken Bowl line, Plant Chick
  name: Daring Foods Retail Products API
  slug: daring-foods-products-api
- description: Public, unauthenticated read access to the Daring foodservice (B2B) product line via the custom `foodservice-products` post type - the bulk and gluten-free product sold to restaurants, campus dining a
  name: Daring Foods Foodservice Products API
  slug: daring-foods-foodservice-api
- description: Public, unauthenticated read access to the 17 static marketing pages of daring.com - Our Mission, Ingredients, How To Cook, Locator, FAQ, Careers, Terms & Conditions and the Foodservice sub-tree. Unli
  name: Daring Foods Pages API
  slug: daring-foods-pages-api
- description: Public, unauthenticated read access to the media library behind daring.com - packaging and product photography, recipe imagery and site assets. Verified live at 749 attachments, each with every genera
  name: Daring Foods Media API
  slug: daring-foods-media-api
- description: Public, unauthenticated cross-content search over daring.com, returning lightweight id / title / url / type / subtype records spanning recipes, retail products, foodservice products, pages and posts i
  name: Daring Foods Search API
  slug: daring-foods-search-api
- description: The self-describing metadata layer - route index (222 routes across 10 namespaces), registered post types, taxonomies, statuses and authors - that makes the whole daring.com surface machine-readable w
  name: Daring Foods Discovery API
  slug: daring-foods-discovery-api
- description: Public, unauthenticated read access to the standard WordPress `post` collection and its comment thread. Daring Foods runs no editorial blog - the collection holds one post, the WordPress install defau
  name: Daring Foods Posts API
  slug: daring-foods-posts-api
- description: Public oEmbed 1.0 provider endpoint for daring.com URLs, returning embeddable rich metadata - title, author, thumbnail and iframe markup - for any recipe, product or marketing page in a single unauthe
  name: Daring Foods oEmbed API
  slug: daring-foods-oembed-api
- description: Public Yoast SEO head endpoint returning the rendered SEO metadata and full schema.org JSON-LD graph for any daring.com URL - the most structured description of a Daring recipe or product available fr
  name: Daring Foods SEO Metadata API
  slug: daring-foods-seo-api
- description: The `category` taxonomy - cooking methods for the recipe library.
  name: Daring Foods Categories API
  slug: daring-foods-categories-api
- description: Comments attached to posts. 41 approved, predominantly automated spam.
  name: Daring Foods Comments API
  slug: daring-foods-comments-api
- description: Post types, taxonomies, statuses and authors.
  name: Daring Foods Metadata API
  slug: daring-foods-metadata-api
- description: The `post_tag` taxonomy. Registered but empty on this site (0 terms).
  name: Daring Foods Tags API
  slug: daring-foods-tags-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Daring Foods Taxonomy Categories API
  slug: open-daring-foods-categories-api
- collection_type: open
  name: Daring Foods Posts Comments API
  slug: open-daring-foods-comments-api
- collection_type: open
  name: Daring Foods Discovery API
  slug: open-daring-foods-discovery-api
- collection_type: open
  name: Daring Foods Products Foodservice API
  slug: open-daring-foods-foodservice-api
- collection_type: open
  name: Daring Foods Media API
  slug: open-daring-foods-media-api
- collection_type: open
  name: Daring Foods Discovery Metadata API
  slug: open-daring-foods-metadata-api
- collection_type: open
  name: Daring Foods O Embed API
  slug: open-daring-foods-oembed-api
- collection_type: open
  name: Daring Foods Pages API
  slug: open-daring-foods-pages-api
- collection_type: open
  name: Daring Foods Posts API
  slug: open-daring-foods-posts-api
- collection_type: open
  name: Daring Foods Retail Products API
  slug: open-daring-foods-products-api
- collection_type: open
  name: Daring Foods Recipes API
  slug: open-daring-foods-recipes-api
- collection_type: open
  name: Daring Foods Search API
  slug: open-daring-foods-search-api
- collection_type: open
  name: Daring Foods Metadata SEO API
  slug: open-daring-foods-seo-api
- collection_type: open
  name: Daring Foods Taxonomy Tags API
  slug: open-daring-foods-tags-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/daring-foods-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/daring-foods-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://daring.com/
- group: company
  title: ''
  type: About
  url: https://daring.com/our-mission/
- group: operate
  title: ''
  type: Support
  url: https://daring.com/faq/
- group: operate
  title: ''
  type: FAQ
  url: https://daring.com/faq/
- group: company
  title: ''
  type: Careers
  url: https://daring.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://daring.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.daring.com/privacy-policy
- group: other
  title: ''
  type: Accessibility
  url: https://daring.com/accessibility-statement/
- group: company
  title: ''
  type: BlogRSS
  url: https://daring.com/feed/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/daringfoods/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/daringfoods/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/daringfoods
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@daringfoods
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/daringfoods
- group: auth
  title: ''
  type: Authentication
  url: authentication/daring-foods-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/daring-foods-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/daring-foods-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/daring-foods-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/daring-foods-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/daring-foods-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/daring-foods-well-known.yml
- group: build
  title: ''
  type: Examples
  url: examples/daring-foods-examples.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/daring-foods-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/daring-foods-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/daring-foods-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: 'Daring Foods is an American plant-based food company, founded in 2018 by Ross Mackay and Eliott Kessas, that makes 100% plant-based chicken from a deliberately short ingredient list with soy as the protein base. Trading simply as "Daring", it sells retail Plant Chicken in shredded, diced and breaded-pieces formats plus a line of ready-to-heat Plant Chicken Bowls and Plant Chicken Wings through more than 15,000 US grocery stores, and runs a separate foodservice business supplying bulk and gluten-free product to restaurants, campus dining and institutional kitchens. The company raised over $120 million across 2020-2021 during the plant-based protein boom and was acquired by the Australian plant-based meat manufacturer v2food in 2025, under which it retains its own brand. Daring Foods is a consumer packaged goods business, not a software vendor: it operates no developer program, publishes no product API, and offers no portal, SDKs or developer support. The only machine-readable
  interface it exposes is the WordPress REST content API behind daring.com, which is anonymously readable and unusually well-stocked for a CPG site - 208 recipes classified by cooking method, 14 retail products, 7 foodservice products, 17 marketing pages and a 749-item media library - captured here for discovery purposes.'
image: https://daring.com/wp-content/uploads/2023/06/cropped-favicon-6oi8ii-5-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: daring-foods-mcp.yml
  slug: daring-foods-mcpyml
modified: '2026-08-04'
name: Daring Foods
nav: Providers
network: true
overview: 'Daring Foods publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Recipes API, Retail Products API, Foodservice Products API, and 11 more. Tagged areas include Company, Food, Consumer Packaged Goods, Plant Based, and Alternative Protein.


  Daring Foods'' developer surface includes support, FAQ, authentication, code examples, and 24 more developer resources.'
random_paper: 21
score:
  band: thin
  composite: 32.6
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 60.0
    developer_ergonomics: 19.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/daring-foods/refs/heads/main/screenshots/daring-foods-2026-08-07T164036.png
security:
- kind: authentication
  name: Daring Foods Authentication
  slug: daring-foods-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Daring Foods Domain Security
  slug: daring-foods-domain-security
  summary_line: TLSv1.3 · DMARC
slug: daring-foods
tags:
- Company
- Food
- Consumer Packaged Goods
- Plant Based
- Alternative Protein
- Food and Beverage
- Recipes
- Foodservice
- Grocery
- Content
website: https://daring.com/
---
