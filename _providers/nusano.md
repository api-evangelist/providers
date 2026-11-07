---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
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
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: A Model Context Protocol server endpoint advertised in the nusano.com WordPress REST route index under the "mcp" namespace and served at /wp-json/mcp/mcp-adapter-default-server. The endpoint is live b
  name: Nusano MCP Server (WordPress MCP Adapter)
  slug: mcp
- description: 'The public WordPress REST API (wp-json) of the Nusano website at nusano.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Nusano Website (WordPress REST)
  slug: nusano-com-website-wordpress-rest
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://nusano.com/
- group: company
  title: ''
  type: About
  url: https://nusano.com/company/
- group: other
  title: ''
  type: Technology
  url: https://nusano.com/technology/
- group: company
  title: ''
  type: Blog
  url: https://nusano.com/news/nu-blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://nusano.com/feed/
- group: company
  title: ''
  type: News
  url: https://nusano.com/news/
- group: operate
  title: ''
  type: Support
  url: https://nusano.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://nusano.com/careers/
- group: other
  title: ''
  type: MediaKit
  url: https://nusano.com/news/nusano-media-kit/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nusano
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nusano/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@nusano
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nusano.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nusano.com/privacy-policy/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/nusano_stock/
- group: agent
  href: https://artifacts.apis.io/nusano/llms/nusano-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nusano-llms.txt
- group: auth
  href: https://artifacts.apis.io/nusano/security/nusano-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nusano-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/nusano/authentication/nusano-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nusano-authentication.yml
- group: design
  href: https://artifacts.apis.io/nusano/conventions/nusano-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nusano-conventions.yml
- group: design
  href: https://artifacts.apis.io/nusano/errors/nusano-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nusano-problem-types.yml
- group: design
  href: https://artifacts.apis.io/nusano/lifecycle/nusano-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nusano-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/nusano/conformance/nusano-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nusano-conformance.yml
- group: design
  href: https://artifacts.apis.io/nusano/data-model/nusano-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nusano-data-model.yml
- group: operate
  href: https://artifacts.apis.io/nusano/rate-limits/nusano-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nusano-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/nusano/plans/nusano-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nusano-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/nusano/packages/nusano-packages.yml
  title: ''
  type: Packages
  url: packages/nusano-packages.yml
- group: build
  href: https://artifacts.apis.io/nusano/examples/nusano-examples.yml
  title: ''
  type: Examples
  url: examples/nusano-examples.yml
- group: other
  href: https://artifacts.apis.io/nusano/overlays/nusano-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nusano-content-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/nusano/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: 'Nusano is a privately held physics company headquartered in West Valley City, Utah, that is rebuilding radioisotope production around a proprietary high-current ion source and linear accelerator platform. Founded by nuclear cardiologist Dr. Howard Lewin and nuclear physicist Dr. Glenn Rosenthal and led by CEO Chris Lowe, the company cut the ribbon in August 2025 on a custom-built 190,000-square-foot production facility capable of producing more than 40 different radioisotopes, and has raised over $115M in a Series C to commercialize them. Its platform can generate up to twelve isotopes simultaneously and serves three markets: medical radioisotopes as active pharmaceutical ingredients for radiotherapeutic and diagnostic oncology (with multi-isotope supply agreements signed with Ratio Therapeutics, Ariceum Therapeutics and Clarity Pharmaceuticals), high-assay low-enriched uranium (HALEU) for next-generation nuclear fuel, and long-lived radioisotope nuclear batteries for aerospace,
  maritime and terrestrial use, alongside mass-separation work on North American critical mineral refining. Nusano is a manufacturer of physical radioisotope products, not a software vendor: it operates no developer program, publishes no product API, SDK or developer portal, and the only machine-readable surfaces on nusano.com are a published llms.txt and the WordPress content REST API (wp/v2) that serves the newsroom, Nu Blog, pages and media library as JSON, plus a WordPress MCP Adapter endpoint that is live but authentication-gated.'
image: https://nusano.com/wp-content/uploads/2025/07/logo-graphic-full-color.jpeg
layout: provider
mcp_servers:
- description: 'The nusano.com WordPress REST route index advertises an "mcp" namespace with a single MCP server route at /wp-json/mcp/mcp-adapter-default-server accepting POST, GET and DELETE. This is the WordPress '
  name: Nusano MCP Server (WordPress MCP Adapter)
  slug: nusano-mcp-server-wordpress-mcp-adapter
modified: '2026-08-26'
name: Nusano
nav: Providers
network: true
overview: 'Nusano is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Radioisotopes, Nuclear Medicine, Life Sciences, and Healthcare.


  Nusano''s developer surface includes engineering blog, product news, support, YouTube channel, authentication, code examples, and 23 more developer resources.'
plans:
- name: Nusano Plans Pricing
  plan_count: 0
  slug: nusano-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Nusano Rate Limits
  slug: nusano-rate-limits
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 6.5
    developer_ergonomics: 25.6
    discoverability: 67.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 20.7
  provenance:
    conformance: derived
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nusano/nusano-2026-09-02T150818.png
security:
- kind: authentication
  name: Nusano Authentication
  slug: nusano-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nusano Domain Security
  slug: nusano-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: nusano-read-newsroom
  slug: nusano-read-newsroom
- name: nusano-search-and-media
  slug: nusano-search-and-media
slug: nusano
tags:
- Company
- Radioisotopes
- Nuclear Medicine
- Life Sciences
- Healthcare
- Oncology
- Radiopharmaceuticals
- Physics
- Advanced Manufacturing
- Nuclear Energy
- HALEU
- Critical Minerals
website: https://nusano.com/
---
