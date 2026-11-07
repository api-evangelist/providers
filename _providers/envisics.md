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
  name: Envisics Agentic Access
  operation_count: 21
  slug: envisics-agentic-access
  summary_line: 21 operations
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Envisics website at envisics.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Envisics Website (WordPress REST)
  slug: envisics-com-website-wordpress-rest
artifact_total: 9
collections:
- collection_type: open
  name: Envisics Taxonomy API
  slug: open-envisics-taxonomy-api
common:
- group: other
  href: https://artifacts.apis.io/envisics/overlays/envisics-taxonomy-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/envisics-taxonomy-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/envisics/agentic-access/envisics-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/envisics-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/envisics/security/envisics-domain-security.yml
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
  href: https://artifacts.apis.io/envisics/authentication/envisics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/envisics-authentication.yml
- group: design
  href: https://artifacts.apis.io/envisics/conventions/envisics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/envisics-conventions.yml
- group: design
  href: https://artifacts.apis.io/envisics/errors/envisics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/envisics-problem-types.yml
- group: design
  href: https://artifacts.apis.io/envisics/lifecycle/envisics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/envisics-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/envisics/conformance/envisics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/envisics-conformance.yml
- group: design
  href: https://artifacts.apis.io/envisics/data-model/envisics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/envisics-data-model.yml
- group: operate
  href: https://artifacts.apis.io/envisics/rate-limits/envisics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/envisics-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/envisics/plans/envisics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/envisics-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/envisics/examples/envisics-examples.yml
  title: ''
  type: Examples
  url: examples/envisics-examples.yml
- group: agent
  href: https://artifacts.apis.io/envisics/llms/envisics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/envisics-llms.txt
- group: build
  href: https://artifacts.apis.io/envisics/mcp/envisics-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/envisics-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/envisics/skills/_index.yml
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
overview: 'Envisics is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Augmented Reality, Holography, and Head-Up Display.


  Envisics'' developer surface includes engineering blog, YouTube channel, authentication, code examples, and 27 more developer resources.'
plans:
- name: Envisics Plans Pricing
  plan_count: 0
  slug: envisics-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Envisics Rate Limits
  slug: envisics-rate-limits
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 7.3
    developer_ergonomics: 20.8
    discoverability: 65.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 19.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/envisics/envisics-2026-09-02T145408.png
security:
- kind: authentication
  name: Envisics Authentication
  slug: envisics-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Envisics Domain Security
  slug: envisics-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Harvest the Envisics company profile and brand assets
  slug: envisics-harvest-company-profile
- name: Read the Envisics newsroom archive
  slug: envisics-read-newsroom-archive
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
website: https://envisics.com/
---
