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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Harbinger Agentic Access
  operation_count: 22
  slug: harbinger-agentic-access
  summary_line: 22 operations
api_count: 9
apis:
- baseURL: https://harbingermotors.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the Harbinger Motors newsroom — press releases, funding and partnership announcements, product launches and fleet-operations articles — via the WordPress core RE
  name: Harbinger Motors Posts API
  slug: harbinger-posts-api
- baseURL: https://harbingermotors.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the static pages of harbingermotors.com — the electric and plug-in hybrid stripped chassis, HC Series cab chassis, Sevna cab, step van and Industria product page
  name: Harbinger Motors Pages API
  slug: harbinger-pages-api
- baseURL: https://harbingermotors.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the Harbinger Motors event calendar — the site-specific `event` custom post type behind harbingermotors.com/events/, listing the trade shows and industry summits
  name: Harbinger Motors Events API
  slug: harbinger-events-api
- baseURL: https://harbingermotors.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the Harbinger Motors media library — vehicle photography, chassis renderings, spec sheets and brochure PDFs, logos and newsroom imagery, each with its source URL
  name: Harbinger Motors Media API
  slug: harbinger-media-api
- baseURL: https://harbingermotors.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the classification layer behind the harbingermotors.com newsroom — the three live post categories (Press Release 25, News 7, Blogs 2), the post_tag vocabulary (r
  name: Harbinger Motors Taxonomy API
  slug: harbinger-taxonomy-api
- baseURL: https://harbingermotors.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated keyword search across every searchable content type on harbingermotors.com — posts, pages and events in one result set, each row reduced to id, title, url, type and subtype. Ve
  name: Harbinger Motors Search API
  slug: harbinger-search-api
- baseURL: https://harbingermotors.com/wp-json
  baseurl_source: declared
  description: The self-describing layer of the harbingermotors.com WordPress REST API — the root index that enumerates all 362 routes across 14 namespaces with their argument schemas, plus the post-type and publica
  name: Harbinger Motors Discovery API
  slug: harbinger-discovery-api
- baseURL: https://harbingermotors.com/wp-json
  baseurl_source: declared
  description: 'The oEmbed 1.0 provider endpoint for harbingermotors.com. Given the URL of any Harbinger Motors page, post or event it returns a rich-embed descriptor — provider name, author, title, thumbnail and an '
  name: Harbinger Motors oEmbed API
  slug: harbinger-oembed-api
- baseURL: https://harbingermotors.com/wp-json
  baseurl_source: declared
  description: The Yoast SEO `get_head` endpoint on harbingermotors.com. For any site URL it returns the fully rendered head block — canonical URL, robots directives, Open Graph and Twitter card metadata, and the sc
  name: Harbinger Motors SEO Metadata API
  slug: harbinger-seo-api
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://harbingermotors.com/
- group: company
  title: ''
  type: About
  url: https://harbingermotors.com/our-company/
- group: company
  title: ''
  type: Blog
  url: https://harbingermotors.com/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://harbingermotors.com/feed/
- group: other
  title: ''
  type: Products
  url: https://harbingermotors.com/our-products/
- group: other
  title: ''
  type: Technology
  url: https://harbingermotors.com/technology/
- group: other
  title: ''
  type: Downloads
  url: https://harbingermotors.com/downloads/
- group: operate
  title: ''
  type: Support
  url: https://harbingermotors.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://harbingermotors.com/careers/
- group: company
  title: ''
  type: Partners
  url: https://harbingermotors.com/dealers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://harbingermotors.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://harbingermotors.com/legal/privacy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/harbingermotors
- group: company
  title: ''
  type: Twitter
  url: https://x.com/harbingermotors
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@harbingermotors
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/harbingermotorsinc/
- group: auth
  title: ''
  type: Authentication
  url: authentication/harbinger-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/harbinger-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/harbinger-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/harbinger-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/harbinger-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/harbinger-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/harbinger-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/harbinger-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/harbinger-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/harbinger-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/harbinger-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/harbinger-examples.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/harbinger-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harbinger-domain-security.yml
created: '2026-08-22'
description: Harbinger (Harbinger Motors Inc.) is an American commercial-vehicle manufacturer founded in July 2021 and headquartered in Garden Grove, California. It builds a purpose-designed medium-duty platform — Class 4-6 stripped chassis in all-electric and plug-in hybrid range-extended configurations, the HC Series low-cab-forward cab chassis, the Sevna cab chassis and a step van — around in-house motors, battery packs, power electronics and vehicle software, and sells into last-mile delivery, work-truck, mobile-healthcare, RV and motorhome, and government fleets. Its Harbinger Industria line packages the same drivetrain as off-grid and jobsite power systems. The company has announced serial production of an American-made medium-duty EV, a $160 million Series C co-led by FedEx, Capricorn and THOR Industries, the acquisition of autonomous-driving company Phantom AI alongside a ZF licensing agreement, and a robotics partnership with American Rheinmetall. Harbinger is a vehicle manufacturer
  rather than a software vendor, and publishes no developer program, no developer portal, no API documentation, no SDKs and no partner API. The only machine-readable interface it exposes to the public is the WordPress REST content API behind harbingermotors.com, which is captured here for discovery purposes and is anonymously readable but read-only.
image: https://harbingermotors.com/wp-content/uploads/2025/02/cropped-Harbinger-Bird-02-192x192.png
layout: provider
modified: '2026-08-22'
name: Harbinger
nav: Providers
network: true
overview: 'Harbinger publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Motors Posts API, Motors Pages API, Motors Events API, and 6 more. Tagged areas include Company, Automotive, Electric Vehicles, Commercial Vehicles, and Medium Duty Trucks.


  Harbinger''s developer surface includes engineering blog, support, YouTube channel, authentication, code examples, and 26 more developer resources.'
plans:
- name: Harbinger Plans Pricing
  plan_count: 0
  slug: harbinger-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Harbinger Rate Limits
  slug: harbinger-rate-limits
score:
  band: emerging
  composite: 24.9
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
    contract_quality: 16.0
    developer_ergonomics: 20.8
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 24.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 44.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harbinger/refs/heads/main/screenshots/harbinger-2026-09-02T145704.png
security:
- kind: authentication
  name: Harbinger Authentication
  slug: harbinger-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Harbinger Domain Security
  slug: harbinger-domain-security
  summary_line: TLSv1.3 · DMARC
slug: harbinger
tags:
- Company
- Automotive
- Electric Vehicles
- Commercial Vehicles
- Medium Duty Trucks
- Manufacturing
- Fleet Management
- Transportation
- Logistics
- Energy Storage
- Content
website: https://harbingermotors.com/
---
