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
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cruz Foam Agentic Access
  operation_count: 23
  slug: cruz-foam-agentic-access
  summary_line: 23 operations
api_count: 9
apis:
- description: Public, unauthenticated read access to the Cruz Foam news and blog archive via the WordPress core REST API. Verified live at 139 published posts.
  name: Cruz Foam Posts API
  slug: cruz-foam-posts-api
- description: Public, unauthenticated read access to the static marketing and policy pages of cruzfoam.com — Products, Science, Impact, About Us, Partners, Customers, Careers, Press, Contact, Terms and Privacy. Ver
  name: Cruz Foam Pages API
  slug: cruz-foam-pages-api
- description: Public, unauthenticated read access to the Cruz Foam customer showcase — the site-specific `customers` custom post type behind cruzfoam.com/customers/, listing the brands that ship in Cruz Foam materi
  name: Cruz Foam Customers API
  slug: cruz-foam-customers-api
- description: 'Public, unauthenticated read access to the media library behind cruzfoam.com — product photography, material and science imagery, and press assets with their generated size variants. Verified live at '
  name: Cruz Foam Media API
  slug: cruz-foam-media-api
- description: 'Public, unauthenticated read access to the classification vocabularies behind cruzfoam.com: post categories, post tags, and the site-specific portfolio-categories taxonomy that groups the customer sho'
  name: Cruz Foam Taxonomy API
  slug: cruz-foam-taxonomy-api
- description: Public, unauthenticated cross-content search over cruzfoam.com — posts, pages and the customer showcase — returning lightweight id / title / url / type / subtype records. Verified live at 142 searchab
  name: Cruz Foam Search API
  slug: cruz-foam-search-api
- description: Public, unauthenticated discovery metadata for cruzfoam.com — the self-describing route index (487 routes across 18 namespaces at capture), the registered content types and taxonomies, the publication
  name: Cruz Foam Discovery API
  slug: cruz-foam-discovery-api
- description: Public oEmbed 1.0 provider endpoint for cruzfoam.com URLs, returning embeddable rich metadata — title, author, thumbnail and iframe HTML — for any post, page or customer showcase entry.
  name: Cruz Foam oEmbed API
  slug: cruz-foam-oembed-api
- description: Public Yoast SEO head endpoint returning the rendered head metadata and its parsed JSON-LD schema.org graph for any cruzfoam.com URL — a structured-data view of every page without scraping the HTML.
  name: Cruz Foam SEO Metadata API
  slug: cruz-foam-seo-api
artifact_total: 23
collections:
- collection_type: open
  name: Cruz Foam Customers API
  slug: open-cruz-foam-customers-api
- collection_type: open
  name: Cruz Foam Discovery API
  slug: open-cruz-foam-discovery-api
- collection_type: open
  name: Cruz Foam Media API
  slug: open-cruz-foam-media-api
- collection_type: open
  name: Cruz Foam oEmbed API
  slug: open-cruz-foam-oembed-api
- collection_type: open
  name: Cruz Foam Pages API
  slug: open-cruz-foam-pages-api
- collection_type: open
  name: Cruz Foam Posts API
  slug: open-cruz-foam-posts-api
- collection_type: open
  name: Cruz Foam Search API
  slug: open-cruz-foam-search-api
- collection_type: open
  name: Cruz Foam SEO Metadata API
  slug: open-cruz-foam-seo-api
- collection_type: open
  name: Cruz Foam Taxonomy API
  slug: open-cruz-foam-taxonomy-api
common:
- group: company
  title: ''
  type: Website
  url: https://cruzfoam.com/
- group: company
  title: ''
  type: About
  url: https://cruzfoam.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://cruzfoam.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://cruzfoam.com/feed/
- group: company
  title: ''
  type: Press
  url: https://cruzfoam.com/press/
- group: operate
  title: ''
  type: Contact
  url: https://cruzfoam.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://cruzfoam.com/careers/
- group: company
  title: ''
  type: Partners
  url: https://cruzfoam.com/partners/
- group: other
  title: ''
  type: Customers
  url: https://cruzfoam.com/customers/
- group: other
  title: ''
  type: Products
  url: https://cruzfoam.com/products/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cruzfoam.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cruzfoam.com/privacy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cruz-foam/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/CruzFoam
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/cruzfoam/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/CruzFoam/
- group: auth
  title: ''
  type: Authentication
  url: authentication/cruz-foam-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cruz-foam-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cruz-foam-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cruz-foam-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cruz-foam-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cruz-foam-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cruz-foam-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cruz-foam-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cruz-foam-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cruz-foam-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/cruz-foam-examples.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cruz-foam-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cruz-foam-domain-security.yml
created: '2026-08-11'
description: Cruz Foam is a circular materials company founded in 2017 in Santa Cruz, California by John Felts and Marco Rolandi out of research at the UC Santa Cruz Baskin School of Engineering. It makes a certified compostable replacement for expanded polystyrene, built from chitin recovered from shrimp and crustacean shells that would otherwise go to landfill, combined with starches and fibers diverted from agricultural waste streams. Its products include Cruz Foam protective packaging, Cruz Cool insulated cold-chain shippers, and EcoVino wine shippers, sold to consumer brands, appliance manufacturers, seafood and cold-chain shippers, and direct-to-consumer retailers. The company was named to TIME's Best Inventions of 2023 and Fast Company's Most Innovative Companies in 2024. Cruz Foam is a materials manufacturer rather than a software vendor, and publishes no commercial or developer-facing product API, no developer portal, and no SDKs. The only machine-readable interface it exposes is
  the WordPress REST content API behind its corporate website at cruzfoam.com, which is captured here for discovery purposes and is anonymously readable but read-only.
image: https://cruzfoam.com/wp-content/uploads/2024/09/cropped-cruz-foam-favicon-192x192.png
layout: provider
modified: '2026-08-11'
name: Cruz Foam
nav: Providers
network: true
overview: 'Cruz Foam publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Customers API, and 6 more. Tagged areas include Company, Materials Science, Sustainable Packaging, Compostable Materials, and Biomaterials.


  Cruz Foam''s developer surface includes engineering blog, authentication, code examples, and 27 more developer resources.'
plans:
- name: Cruz Foam Plans Pricing
  plan_count: 0
  slug: cruz-foam-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Cruz Foam Rate Limits
  slug: cruz-foam-rate-limits
score:
  band: thin
  composite: 31.3
  delta: -0.9
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 54.8
    developer_ergonomics: 16.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Cruz Foam Authentication
  slug: cruz-foam-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cruz Foam Domain Security
  slug: cruz-foam-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cruz-foam
tags:
- Company
- Materials Science
- Sustainable Packaging
- Compostable Materials
- Biomaterials
- Circular Economy
- Manufacturing
- Consumer Packaged Goods
- Cold Chain
- Sustainability
- Content
website: https://cruzfoam.com/
---
