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
    error_semantics: derived
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
  score: 9.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 62
  human_in_the_loop: 0
  name: Iggenix Agentic Access
  operation_count: 97
  slug: iggenix-agentic-access
  summary_line: 97 operations · 62 acting
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the IgGenix website at iggenix.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: IgGenix Website (WordPress REST)
  slug: iggenix-com-website-wordpress-rest
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/iggenix/agentic-access/iggenix-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/iggenix-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://iggenix.com/
- group: company
  title: ''
  type: Press
  url: https://iggenix.com/pressreleases/
- group: other
  title: ''
  type: Publications
  url: https://iggenix.com/publications/
- group: other
  title: ''
  type: Abstracts
  url: https://iggenix.com/abstracts/
- group: company
  title: ''
  type: BlogRSS
  url: https://iggenix.com/feed/
- group: operate
  title: ''
  type: Support
  url: mailto:info@IgGenix.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iggenix-inc/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
- group: other
  href: https://artifacts.apis.io/iggenix/overlays/iggenix-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/iggenix-content-overlay.yaml
- group: build
  href: https://artifacts.apis.io/iggenix/packages/iggenix-packages.yml
  title: ''
  type: Packages
  url: packages/iggenix-packages.yml
- group: agent
  href: https://artifacts.apis.io/iggenix/llms/iggenix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/iggenix-llms.txt
- group: auth
  href: https://artifacts.apis.io/iggenix/authentication/iggenix-authentication.yml
  title: ''
  type: Authentication
  url: authentication/iggenix-authentication.yml
- group: design
  href: https://artifacts.apis.io/iggenix/conventions/iggenix-conventions.yml
  title: ''
  type: Conventions
  url: conventions/iggenix-conventions.yml
- group: design
  href: https://artifacts.apis.io/iggenix/conformance/iggenix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/iggenix-conformance.yml
- group: design
  href: https://artifacts.apis.io/iggenix/errors/iggenix-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/iggenix-problem-types.yml
- group: design
  href: https://artifacts.apis.io/iggenix/lifecycle/iggenix-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/iggenix-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/iggenix/data-model/iggenix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/iggenix-data-model.yml
- group: build
  href: https://artifacts.apis.io/iggenix/examples/iggenix-examples.yml
  title: ''
  type: Examples
  url: examples/iggenix-examples.yml
- group: operate
  href: https://artifacts.apis.io/iggenix/rate-limits/iggenix-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/iggenix-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/iggenix/plans/iggenix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iggenix-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/iggenix/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/iggenix/security/iggenix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iggenix-domain-security.yml
created: '2026-08-22'
description: IgGenix, Inc. is a clinical-stage antibody discovery and development company in South San Francisco, California, founded in 2019 on work from Stephen Quake's laboratory at Stanford in collaboration with allergy clinician-researcher Kari Nadeau. Its SEQ SIFTER platform uses single-cell RNA sequencing to capture the rare IgE-producing B cells circulating in allergic patients' blood, then re-engineers those sequences into fully human, high-affinity, allergen-specific IgG antibodies designed to block the allergic cascade before it starts. Lead program IGNX001 is a human IgG4 monoclonal antibody for peanut allergy, in the Phase 1 ACCELERATE Peanut trial, with discovery programs against alpha-gal syndrome, nsLTP allergens and atopic dermatitis autoantigens. The company has raised roughly $75M across seed, Series A and a $40M Series B. IgGenix publishes no product or developer API and no developer program; the only machine-readable surface on iggenix.com is the WordPress REST API (wp/v2)
  served at https://iggenix.com/wp-json/, which returns the company's press releases, peer-reviewed publications, conference abstracts, careers post type, pages, media library, taxonomies and site search as anonymous JSON. The OpenAPI definitions in this repository were derived mechanically from that route index; IgGenix publishes none of its own.
image: https://iggenix.com/wp-content/themes/iggenix/img/logo-nav.svg
layout: provider
modified: '2026-08-22'
name: IgGenix
nav: Providers
network: true
overview: 'IgGenix is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Immunology, and Allergy.


  IgGenix''s developer surface includes support, authentication, code examples, and 20 more developer resources.'
plans:
- name: Iggenix Plans Pricing
  plan_count: 0
  slug: iggenix-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Iggenix Rate Limits
  slug: iggenix-rate-limits
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 7.3
    developer_ergonomics: 23.2
    discoverability: 58.0
    operational_transparency: 0.0
  previous_composite: 13.9
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
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/iggenix/iggenix-2026-09-02T145832.png
security:
- kind: authentication
  name: Iggenix Authentication
  slug: iggenix-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Iggenix Domain Security
  slug: iggenix-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: iggenix-read-pages-and-media
  slug: iggenix-read-pages-and-media
- name: iggenix-read-the-record
  slug: iggenix-read-the-record
slug: iggenix
tags:
- Company
- Biotechnology
- Life Sciences
- Immunology
- Allergy
- Antibodies
- Drug Discovery
- Therapeutics
- Clinical Trials
- Pharmaceuticals
- Research
website: https://iggenix.com/
---
