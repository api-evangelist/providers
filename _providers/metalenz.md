---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
  name: Metalenz Agentic Access
  operation_count: 23
  slug: metalenz-agentic-access
  summary_line: 23 operations
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Metalenz website at metalenz.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Metalenz Website (WordPress REST)
  slug: metalenz-com-website-wordpress-rest
artifact_total: 8
common:
- group: other
  href: https://artifacts.apis.io/metalenz/capabilities/metalenz-capability-edges.yml
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
  href: https://artifacts.apis.io/metalenz/authentication/metalenz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/metalenz-authentication.yml
- group: design
  href: https://artifacts.apis.io/metalenz/errors/metalenz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/metalenz-problem-types.yml
- group: design
  href: https://artifacts.apis.io/metalenz/conventions/metalenz-conventions.yml
  title: ''
  type: Conventions
  url: conventions/metalenz-conventions.yml
- group: design
  href: https://artifacts.apis.io/metalenz/data-model/metalenz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/metalenz-data-model.yml
- group: design
  href: https://artifacts.apis.io/metalenz/conformance/metalenz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/metalenz-conformance.yml
- group: design
  href: https://artifacts.apis.io/metalenz/lifecycle/metalenz-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/metalenz-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/metalenz/rate-limits/metalenz-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/metalenz-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/metalenz/plans/metalenz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/metalenz-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/metalenz/examples/metalenz-examples.yml
  title: ''
  type: Examples
  url: examples/metalenz-examples.yml
- group: agent
  href: https://artifacts.apis.io/metalenz/llms/metalenz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/metalenz-llms.txt
- group: agent
  href: https://artifacts.apis.io/metalenz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/metalenz/agentic-access/metalenz-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/metalenz-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/metalenz/mcp/metalenz-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/metalenz-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/metalenz/packages/metalenz-packages.yml
  title: ''
  type: Packages
  url: packages/metalenz-packages.yml
- group: auth
  href: https://artifacts.apis.io/metalenz/security/metalenz-domain-security.yml
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
overview: 'Metalenz is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Optics, Meta-Optics, and Metasurface.


  Metalenz''s developer surface includes product news, support, authentication, code examples, and 30 more developer resources.'
plans:
- name: Metalenz Plans Pricing
  plan_count: 0
  slug: metalenz-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Metalenz Rate Limits
  slug: metalenz-rate-limits
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 6.5
    developer_ergonomics: 23.2
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 16.9
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 18.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/metalenz/metalenz-2026-09-02T150607.png
security:
- kind: authentication
  name: Metalenz Authentication
  slug: metalenz-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Metalenz Domain Security
  slug: metalenz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Map the Metalenz product line, technology and company facts
  slug: metalenz-map-products-and-company
- name: Track Metalenz Polar ID and meta-optics announcements
  slug: metalenz-track-polar-id-announcements
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
- Computer Vision
- Consumer Electronics
- Automotive
- Robotics
- Hardware
website: https://metalenz.com/
---
