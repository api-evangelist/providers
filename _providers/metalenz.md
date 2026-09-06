---
access_model:
  confidence: medium
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Metalenz Agentic Access
  operation_count: 23
  slug: metalenz-agentic-access
  summary_line: 23 operations
api_count: 7
apis:
- baseURL: https://metalenz.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the Metalenz newsroom via the WordPress core REST API. The `post` content type on metalenz.com is registered with the label "Press Releases" and carries the comp
  name: Metalenz Press Releases API
  slug: metalenz-press-releases-api
- baseURL: https://metalenz.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the static page tree behind metalenz.com — the Polar ID, Polar 3D, PolarEyes, Orion and Gemini product pages, the meta-optics and foundational technology explain
  name: Metalenz Pages API
  slug: metalenz-pages-api
- baseURL: https://metalenz.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the media library behind metalenz.com — Polar ID and Polar 3D product imagery, metasurface and meta-optics diagrams, conference and event photography, leadership
  name: Metalenz Media API
  slug: metalenz-media-api
- baseURL: https://metalenz.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the classification layer over the Metalenz newsroom — the `category` taxonomy and the `post_tag` taxonomy, with their term records, counts and archive links. Ver
  name: Metalenz Taxonomy API
  slug: metalenz-taxonomy-api
- baseURL: https://metalenz.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated cross-content search over metalenz.com — press releases and static pages together — returning lightweight id / title / url / type / subtype records that link back to the full o
  name: Metalenz Search API
  slug: metalenz-search-api
- baseURL: https://metalenz.com/wp-json
  baseurl_source: declared
  description: The self-describing surface of the metalenz.com WordPress REST API — the route index, the per-namespace indexes, the registered content types and taxonomies, the publication statuses, the public autho
  name: Metalenz Discovery API
  slug: metalenz-discovery-api
- baseURL: https://metalenz.com/wp-json
  baseurl_source: declared
  description: Public oEmbed 1.0 provider endpoint for metalenz.com URLs, returning embeddable rich metadata — title, author, provider, thumbnail and iframe HTML — for any published post or page. The endpoint is adv
  name: Metalenz oEmbed API
  slug: metalenz-oembed-api
artifact_total: 12
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/metalenz-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://metalenz.com/
- group: company
  title: ''
  type: About
  url: https://metalenz.com/about-us/
- group: other
  title: ''
  type: Leadership
  url: https://metalenz.com/leadership/
- group: other
  title: ''
  type: Products
  url: https://metalenz.com/all-products/
- group: other
  title: ''
  type: Technology
  url: https://metalenz.com/our-technology/
- group: company
  title: ''
  type: Press
  url: https://metalenz.com/press-releases/
- group: company
  title: ''
  type: News
  url: https://metalenz.com/media-coverage/
- group: other
  title: ''
  type: Events
  url: https://metalenz.com/events/
- group: learn
  title: ''
  type: Videos
  url: https://metalenz.com/video-gallery/
- group: company
  title: ''
  type: BlogRSS
  url: https://metalenz.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://metalenz.com/contact-us/
- group: operate
  title: ''
  type: Contact
  url: https://metalenz.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://metalenz.com/careers/
- group: other
  title: ''
  type: SiteMap
  url: https://metalenz.com/sitemap_index.xml
- group: start
  title: ''
  type: DocumentationPortal
  url: https://docs.metalenz.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://metalenz.com/terms-and-conditions-of-sale/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Metalenz
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/metalenz/
- group: auth
  title: ''
  type: Authentication
  url: authentication/metalenz-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/metalenz-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/metalenz-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/metalenz-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/metalenz-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/metalenz-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/metalenz-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/metalenz-plans-pricing.yml
- group: build
  title: ''
  type: Examples
  url: examples/metalenz-examples.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metalenz-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/metalenz-agentic-access.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/metalenz-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/metalenz-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metalenz-domain-security.yml
created: '2026-08-25'
description: 'Metalenz is a fabless semiconductor optics company in Boston, Massachusetts that commercialises meta-optics — flat metasurface lenses that replace stacks of curved refractive elements with a single planar chip patterned by nanostructures and mass produced in a standard semiconductor foundry. The company was founded in 2016 by CEO Rob Devlin and Harvard professor Federico Capasso out of the Capasso Lab at the Harvard John A. Paulson School of Engineering and Applied Sciences, and holds the exclusive worldwide licence to that lab''s metasurface intellectual property, now more than 150 issued and pending patents. Its first-generation metasurfaces reached mass production in 2022 through a manufacturing partnership with STMicroelectronics and have since shipped in well over 100 million consumer devices. The current product line is built on the PolarEyes polarization imaging platform: Polar ID, a single-camera polarization face authentication system for smartphones that works under
  the display and uses the Samsung ISOCELL Vizion 931 sensor and Qualcomm Snapdragon imaging stack; Polar 3D, on-device relightable selfies and avatars from one image; and the Orion and Gemini dot-pattern projectors for structured-light 3D sensing. Metalenz sells optical components, licences and full-stack biometric solutions to device makers and foundries — UMC and STMicroelectronics are named manufacturing partners — and is backed by Neotribe Ventures, Intel Capital, TDK Ventures, 3M, Applied Ventures, M Ventures, Braemar Energy Ventures and Foothill Ventures. It sells silicon and IP, not software: it publishes no developer program, no developer portal, no SDK and no API documentation of any kind. The only machine-readable interface it exposes to the public is the WordPress REST content API behind metalenz.com, which is anonymously readable, read-only without credentials, and captured here for discovery purposes.'
image: https://metalenz.com/wp-content/uploads/2023/07/metalenz-logo.png
layout: provider
modified: '2026-08-25'
name: Metalenz
nav: Providers
network: true
overview: 'Metalenz publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Press Releases API, Pages API, Media API, and 4 more. Tagged areas include Company, Semiconductors, Optics, Meta-Optics, and Metasurface.


  Metalenz''s developer surface includes product news, support, authentication, code examples, and 30 more developer resources.'
plans:
- name: Metalenz Plans Pricing
  plan_count: 0
  slug: metalenz-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Metalenz Rate Limits
  slug: metalenz-rate-limits
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 16.1
    developer_ergonomics: 18.5
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 18.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metalenz/refs/heads/main/screenshots/metalenz-2026-09-02T150607.png
security:
- kind: authentication
  name: Metalenz Authentication
  slug: metalenz-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Metalenz Domain Security
  slug: metalenz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metalenz
tags:
- Company
- Semiconductors
- Optics
- Meta-Optics
- Metasurface
- Photonics
- Biometrics
- Face Authentication
- Polarization Imaging
- 3D Sensing
- Computer-Vision
- Consumer Electronics
- Automotive
- Robotics
- Hardware
- Content
website: https://metalenz.com/
---
