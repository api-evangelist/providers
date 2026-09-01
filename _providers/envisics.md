---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Envisics Agentic Access
  operation_count: 21
  slug: envisics-agentic-access
  summary_line: 21 operations
api_count: 10
apis:
- description: Public, unauthenticated read access to the Envisics newsroom archive — press releases, news items, tech-shorts and did-you-know posts — via the WordPress core REST API. Verified live at 34 published p
  name: Envisics Posts API
  slug: envisics-posts-api
- description: 'Public, unauthenticated read access to the static pages of envisics.com — Products, Technology, Company, Newsroom, Multi Media, Careers, Contact, Terms of Use, Supplier Terms & Conditions and Privacy '
  name: Envisics Pages API
  slug: envisics-pages-api
- description: Public, unauthenticated read access to the media library behind envisics.com — AR HUD product imagery, holographic waveguide renders, press photography and brand assets with their generated size varia
  name: Envisics Media API
  slug: envisics-media-api
- description: Public, unauthenticated cross-content search over envisics.com — posts and pages — returning lightweight id / title / url / type / subtype records. Verified live at 62 searchable objects on 2026-08-12
  name: Envisics Search API
  slug: envisics-search-api
- description: Public, unauthenticated discovery metadata for envisics.com — the registered content types and taxonomies, the publication statuses, and the public author records. This is the surface that makes the r
  name: Envisics Discovery API
  slug: envisics-discovery-api
- description: Public oEmbed 1.0 provider endpoint for envisics.com URLs, returning embeddable rich metadata — title, author, dimensions and iframe HTML — for any post or page on the site.
  name: Envisics oEmbed API
  slug: envisics-oembed-api
- description: Public Yoast SEO head endpoint returning the rendered head metadata and its parsed JSON-LD schema.org graph for any envisics.com URL — a structured-data view of every page without scraping the HTML.
  name: Envisics SEO Metadata API
  slug: envisics-seo-api
- description: Newsroom categories.
  name: Envisics Categories API
  slug: envisics-categories-api
- description: Newsroom tags.
  name: Envisics Tags API
  slug: envisics-tags-api
- description: Public author records.
  name: Envisics Users API
  slug: envisics-users-api
artifact_total: 23
collections:
- collection_type: open
  name: Envisics Discovery API
  slug: open-envisics-discovery-api
- collection_type: open
  name: Envisics Media API
  slug: open-envisics-media-api
- collection_type: open
  name: Envisics oEmbed API
  slug: open-envisics-oembed-api
- collection_type: open
  name: Envisics Pages API
  slug: open-envisics-pages-api
- collection_type: open
  name: Envisics Posts API
  slug: open-envisics-posts-api
- collection_type: open
  name: Envisics Search API
  slug: open-envisics-search-api
- collection_type: open
  name: Envisics SEO Metadata API
  slug: open-envisics-seo-api
- collection_type: open
  name: Envisics Taxonomy API
  slug: open-envisics-taxonomy-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/envisics-taxonomy-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/envisics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/envisics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://envisics.com/
- group: company
  title: ''
  type: About
  url: https://envisics.com/company/
- group: other
  title: ''
  type: Products
  url: https://envisics.com/products/
- group: other
  title: ''
  type: Technology
  url: https://envisics.com/technology/
- group: company
  title: ''
  type: Blog
  url: https://envisics.com/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://envisics.com/feed/
- group: company
  title: ''
  type: Press
  url: https://envisics.com/press/
- group: other
  title: ''
  type: Media
  url: https://envisics.com/multi-media/
- group: operate
  title: ''
  type: Contact
  url: https://envisics.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://envisics.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://envisics.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://envisics.com/privacy-policy/
- group: commercial
  title: ''
  type: SupplierTerms
  url: https://envisics.com/supplier-terms-conditions/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/envisics-limited/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/envisics
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Envisics
- group: auth
  title: ''
  type: Authentication
  url: authentication/envisics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/envisics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/envisics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/envisics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/envisics-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/envisics-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/envisics-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/envisics-plans-pricing.yml
- group: build
  title: ''
  type: Examples
  url: examples/envisics-examples.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/envisics-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/envisics-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-12'
description: 'Envisics is a British deep-technology company headquartered in Milton Keynes, United Kingdom, that pioneers dynamic holography for automotive augmented-reality head-up displays (AR HUD). The work began with Dr Jamieson Christmas'' PhD at Cambridge University in 2004, continued through Two Trees Photonics (founded 2010, acquired by DAQRI in 2015) which built the world''s first laser holographic HUD for Jaguar Land Rover, and was spun out as the independent company Envisics on 1 January 2018. Its Dynamic Holography Platform and next-generation Holographic Waveguide Technology combine proprietary algorithms with simpler, fewer and more robust optics to deliver multi-plane AR imagery at under 10% of the optical power of conventional systems; first-generation technology shipped in over 150,000 Jaguar and Land Rover vehicles and second-generation technology was slated for the Cadillac LYRIQ-V and 2026 Cadillac VISTIQ. Investors included Hyundai Mobis, General Motors Ventures, Stellantis,
  InMotion Ventures (Jaguar Land Rover) and Tarsadia Investments. Envisics is an automotive hardware and optics supplier rather than a software vendor: it publishes no commercial or developer-facing product API, no developer portal, and no SDKs. The only machine-readable interface it exposes is the WordPress REST content API behind its corporate website at envisics.com, captured here for discovery purposes and anonymously readable but read-only. Envisics Ltd. entered administration on 22 April 2026 under the Insolvency Act 1986, with Geoff Rowley and Simon Carvill-Biggs of FRP Advisory Trading Limited appointed as Joint Administrators.'
image: https://envisics.com/wp-content/uploads/2024/11/logomark.svg
layout: provider
modified: '2026-08-12'
name: Envisics
nav: Providers
network: true
overview: 'Envisics publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Media API, and 7 more. Tagged areas include Company, Automotive, Augmented Reality, Holography, and Head-Up Display.


  Envisics'' developer surface includes engineering blog, YouTube channel, authentication, code examples, and 27 more developer resources.'
plans:
- name: Envisics Plans Pricing
  plan_count: 0
  slug: envisics-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Envisics Rate Limits
  slug: envisics-rate-limits
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 20
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 55.8
    developer_ergonomics: 16.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 30.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Envisics Authentication
  slug: envisics-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Envisics Domain Security
  slug: envisics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: envisics
tags:
- Company
- Automotive
- Augmented Reality
- Holography
- Head-Up Display
- Photonics
- Optics
- Deep Technology
- Hardware
- Advanced Manufacturing
- Content
website: https://envisics.com/
---
