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
  name: Hydrostor Agentic Access
  operation_count: 26
  slug: hydrostor-agentic-access
  summary_line: 26 operations
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Hydrostor website at hydrostor.ca: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Hydrostor Website (WordPress REST)
  slug: hydrostor-ca-website-wordpress-rest
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/hydrostor/security/hydrostor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hydrostor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hydrostor.ca/
- group: company
  title: ''
  type: About
  url: https://hydrostor.ca/our-company/
- group: other
  title: ''
  type: Team
  url: https://hydrostor.ca/our-company/
- group: other
  title: ''
  type: Technology
  url: https://hydrostor.ca/technology/
- group: other
  title: ''
  type: Projects
  url: https://hydrostor.ca/projects/
- group: company
  title: ''
  type: Blog
  url: https://hydrostor.ca/media/
- group: company
  title: ''
  type: BlogRSS
  url: https://hydrostor.ca/feed/
- group: company
  title: ''
  type: Newsletter
  url: https://hydrostor.ca/newsletter/
- group: other
  title: ''
  type: MediaKit
  url: https://hydrostor.ca/media-kit/
- group: operate
  title: ''
  type: Contact
  url: https://hydrostor.ca/contact/
- group: company
  title: ''
  type: Careers
  url: https://hydrostor.ca/careers/
- group: other
  title: ''
  type: Suppliers
  url: https://hydrostor.ca/vendor-interest-form/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hydrostor.ca/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hydrostor.ca/privacy-policy/
- group: auth
  title: ''
  type: Disclosure
  url: https://hydrostor.ca/ab1305-disclosure/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hydrostor-inc-
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Hydrostor
- group: auth
  href: https://artifacts.apis.io/hydrostor/authentication/hydrostor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hydrostor-authentication.yml
- group: design
  href: https://artifacts.apis.io/hydrostor/errors/hydrostor-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hydrostor-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hydrostor/conventions/hydrostor-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hydrostor-conventions.yml
- group: design
  href: https://artifacts.apis.io/hydrostor/data-model/hydrostor-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hydrostor-data-model.yml
- group: design
  href: https://artifacts.apis.io/hydrostor/conformance/hydrostor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hydrostor-conformance.yml
- group: design
  href: https://artifacts.apis.io/hydrostor/lifecycle/hydrostor-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hydrostor-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/hydrostor/rate-limits/hydrostor-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hydrostor-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/hydrostor/plans/hydrostor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hydrostor-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/hydrostor/examples/hydrostor-examples.yml
  title: ''
  type: Examples
  url: examples/hydrostor-examples.yml
- group: agent
  href: https://artifacts.apis.io/hydrostor/llms/hydrostor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hydrostor-llms.txt
- group: agent
  href: https://artifacts.apis.io/hydrostor/agentic-access/hydrostor-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hydrostor-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/hydrostor/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/hydrostor/mcp/hydrostor-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/hydrostor-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/hydrostor/packages/hydrostor-packages.yml
  title: ''
  type: Packages
  url: packages/hydrostor-packages.yml
created: '2026-08-22'
description: 'Hydrostor is a Canadian long-duration energy storage developer founded in 2010 and headquartered in Toronto, with offices in Denver, Colorado and Melbourne and Adelaide, Australia. It builds and operates Advanced Compressed Air Energy Storage (A-CAES) facilities: surplus grid electricity runs a compressor, the heat of compression is captured and stored, and the cooled compressed air is sent into a purpose-built underground cavern held at constant pressure by a water column. On discharge the water weight pushes the air back to surface, where it is recombined with the stored heat and expanded through a turbine, giving eight or more hours of emissions-free storage from a plant with a multi-decade asset life. The company is backed by Goldman Sachs Alternatives, CPP Investments, the Canada Growth Fund, Canoe Financial and Arctern Ventures, operates a commercially contracted utility-scale facility in Goderich, Ontario, and is advancing a roughly 7 GW pipeline including the Willow
  Rock and Copper Valley centers in California, Silver City in New South Wales, and Quinte and Wellington in Ontario. Hydrostor is an energy infrastructure developer rather than a software vendor: it publishes no developer portal, no SDKs, no product API and no machine-readable specification of its own. The only machine-readable interface it exposes is the WordPress core REST content API behind hydrostor.ca, which is anonymously readable, read-only without credentials, and carries the project portfolio, the newsroom archive and the media library. That surface is profiled here for discovery purposes and is described from the site''s own self-describing route index.'
image: https://hydrostor.ca/wp-content/uploads/2026/06/cropped-HDS-Favicon-2026.png
layout: provider
modified: '2026-08-22'
name: Hydrostor
nav: Providers
network: true
overview: 'Hydrostor is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Energy Storage, Long Duration Energy Storage, and Compressed Air Energy Storage.


  Hydrostor''s developer surface includes engineering blog, YouTube channel, authentication, code examples, and 28 more developer resources.'
plans:
- name: Hydrostor Plans Pricing
  plan_count: 0
  slug: hydrostor-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Hydrostor Rate Limits
  slug: hydrostor-rate-limits
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 6.5
    developer_ergonomics: 20.8
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 18.3
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hydrostor/hydrostor-2026-09-02T145804.png
security:
- kind: authentication
  name: Hydrostor Authentication
  slug: hydrostor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hydrostor Domain Security
  slug: hydrostor-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Browse the Hydrostor A-CAES project portfolio
  slug: hydrostor-browse-project-portfolio
- name: Track the Hydrostor newsroom
  slug: hydrostor-track-newsroom
slug: hydrostor
tags:
- Company
- Energy
- Energy Storage
- Long Duration Energy Storage
- Compressed Air Energy Storage
- Grid Infrastructure
- Renewable Energy
- Clean Energy
- Utilities
- Climate Tech
- Canada
website: https://hydrostor.ca/
---
