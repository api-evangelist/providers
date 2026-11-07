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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Xgs Energy Agentic Access
  operation_count: 17
  slug: xgs-energy-agentic-access
  summary_line: 17 operations
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the XGS Energy website at www.xgsenergy.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate '
  name: XGS Energy Website (WordPress REST)
  slug: xgsenergy-com-website-wordpress-rest
artifact_total: 9
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.xgsenergy.com/feed/
- group: company
  title: ''
  type: Website
  url: https://www.xgsenergy.com/
- group: company
  title: ''
  type: About
  url: https://www.xgsenergy.com/team/
- group: company
  title: ''
  type: Blog
  url: https://www.xgsenergy.com/news-and-insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.xgsenergy.com/news-and-insights/feed/
- group: company
  title: ''
  type: Careers
  url: https://www.xgsenergy.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.xgsenergy.com/contact/
- group: operate
  title: ''
  type: Support
  url: https://www.xgsenergy.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.xgsenergy.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xgsenergy.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xgs-energy
- group: build
  href: https://artifacts.apis.io/xgs-energy/packages/xgs-energy-packages.yml
  title: ''
  type: Packages
  url: packages/xgs-energy-packages.yml
- group: agent
  href: https://artifacts.apis.io/xgs-energy/mcp/xgs-energy-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/xgs-energy-mcp.yml
- group: build
  href: https://artifacts.apis.io/xgs-energy/mcp/xgs-energy-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/xgs-energy-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/xgs-energy/llms/xgs-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xgs-energy-llms.txt
- group: agent
  href: https://artifacts.apis.io/xgs-energy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/xgs-energy/agentic-access/xgs-energy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/xgs-energy-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/xgs-energy/security/xgs-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xgs-energy-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/xgs-energy/plans/xgs-energy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/xgs-energy-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/xgs-energy/conformance/xgs-energy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xgs-energy-conformance.yml
- group: design
  href: https://artifacts.apis.io/xgs-energy/lifecycle/xgs-energy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/xgs-energy-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/xgs-energy/authentication/xgs-energy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xgs-energy-authentication.yml
- group: design
  href: https://artifacts.apis.io/xgs-energy/errors/xgs-energy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/xgs-energy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/xgs-energy/conventions/xgs-energy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/xgs-energy-conventions.yml
- group: design
  href: https://artifacts.apis.io/xgs-energy/data-model/xgs-energy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/xgs-energy-data-model.yml
- group: operate
  href: https://artifacts.apis.io/xgs-energy/rate-limits/xgs-energy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/xgs-energy-rate-limits.yml
created: '2026-09-04'
description: 'XGS Energy is a next-generation geothermal power developer founded in 2008 and headquartered in Palo Alto, California, formerly Geothermic Solution. Its patented Thermal Reach Enhancement technology packs a thermally conductive material around a closed-loop wellbore so heat is drawn from the surrounding rock without relying on natural permeability or produced water, siting geothermal in geology conventional hydrothermal and EGS cannot use. It is developing a 150 MW round-the-clock project in New Mexico with Meta and utility PNM, and in 2025 acquired drilling firm Capuano Engineering. XGS Energy is an energy infrastructure developer, not a software vendor: it publishes no developer program, product API, SDKs or API documentation. The only machine-readable interface it exposes is the WordPress REST content API behind www.xgsenergy.com, captured here for discovery — anonymously readable, read-only, and undocumented by the company.'
image: https://www.xgsenergy.com/wp-content/uploads/2024/08/cropped-favicon-192x192.png
layout: provider
modified: '2026-10-06'
name: XGS Energy
nav: Providers
network: true
overview: 'XGS Energy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Geothermal, Renewable Energy, and Clean Energy.


  XGS Energy''s developer surface includes engineering blog, support, authentication, and 23 more developer resources.'
plans:
- name: Xgs Energy Plans Pricing
  plan_count: 0
  slug: xgs-energy-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Xgs Energy Rate Limits
  slug: xgs-energy-rate-limits
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 25.6
    discoverability: 64.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 18.4
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
screenshot: https://apis.io/screenshots/xgs-energy/xgs-energy-2026-10-11T195758.png
security:
- kind: authentication
  name: Xgs Energy Authentication
  slug: xgs-energy-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Xgs Energy Domain Security
  slug: xgs-energy-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: xgs-energy-inventory-site-structure
  slug: xgs-energy-inventory-site-structure
- name: xgs-energy-read-news-archive
  slug: xgs-energy-read-news-archive
- name: xgs-energy-search-site-content
  slug: xgs-energy-search-site-content
slug: xgs-energy
tags:
- Company
- Energy
- Geothermal
- Renewable Energy
- Clean Energy
- Power Generation
- Energy Infrastructure
- Data Center Power
- Climate Tech
website: https://www.xgsenergy.com/
---
