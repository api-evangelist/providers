---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 149
  human_in_the_loop: 0
  name: Lanzatech Agentic Access
  operation_count: 264
  slug: lanzatech-agentic-access
  summary_line: 264 operations · 149 acting
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the LanzaTech website at lanzatech.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: LanzaTech Website (WordPress REST)
  slug: lanzatech-com-website-wordpress-rest
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/lanzatech/overlays/lanzatech-wordpress-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lanzatech-wordpress-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/lanzatech/agentic-access/lanzatech-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lanzatech-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://lanzatech.com/
- group: company
  title: ''
  type: About
  url: https://lanzatech.com/about/
- group: company
  title: ''
  type: Blog
  url: https://lanzatech.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://lanzatech.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://lanzatech.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lanzatech.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lanzatech.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LanzaTech
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.lanzatech.com/
- group: other
  title: ''
  type: Sitemap
  url: https://lanzatech.com/wp-sitemap.xml
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/lanzatech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lanzatech
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/LanzaTech/videos
- group: auth
  href: https://artifacts.apis.io/lanzatech/authentication/lanzatech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lanzatech-authentication.yml
- group: design
  href: https://artifacts.apis.io/lanzatech/conventions/lanzatech-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lanzatech-conventions.yml
- group: design
  href: https://artifacts.apis.io/lanzatech/errors/lanzatech-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lanzatech-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lanzatech/data-model/lanzatech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lanzatech-data-model.yml
- group: design
  href: https://artifacts.apis.io/lanzatech/lifecycle/lanzatech-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lanzatech-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/lanzatech/conformance/lanzatech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lanzatech-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lanzatech/well-known/lanzatech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lanzatech-well-known.yml
- group: agent
  href: https://artifacts.apis.io/lanzatech/mcp/lanzatech-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/lanzatech-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lanzatech/llms/lanzatech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lanzatech-llms.txt
- group: agent
  href: https://artifacts.apis.io/lanzatech/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/lanzatech/security/lanzatech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lanzatech-domain-security.yml
created: '2026-07-17'
description: LanzaTech is a carbon recycling company (Nasdaq LNZA) that uses gas fermentation to convert waste carbon into fuels and chemicals. Its technology retrofits an industrial site such as a steel mill, a ferroalloy plant or a landfill with a bioreactor in which proprietary bacteria consume carbon-rich off-gases and produce ethanol and other intermediates, marketed as CarbonSmart products and used by brands including Unilever, Coty and Zara. The company operates commercial plants in China, India and Belgium, is building the LanzaTech Porsgrunn CCUS project in Norway with Eramet, and works with LanzaJet on sustainable aviation fuel. LanzaTech publishes no developer program, but lanzatech.com runs on WordPress and exposes a fully public, unauthenticated WordPress REST API whose custom content types (news, employee, board-member, download, testimonial) model the company itself.
image: https://lanzatech.com/wp-content/uploads/2022/02/LT-Logo-Navy.svg
layout: provider
modified: '2026-07-19'
name: LanzaTech
nav: Providers
network: true
overview: 'LanzaTech is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Carbon Capture, Climate Tech, Sustainability, and Synthetic Biology.


  LanzaTech''s developer surface includes engineering blog, support, YouTube channel, authentication, and 22 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 1.7
    developer_ergonomics: 25.6
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 18.4
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
screenshot: https://apis.io/screenshots/lanzatech/lanzatech-2026-07-25T224527.png
security:
- kind: authentication
  name: Lanzatech Authentication
  slug: lanzatech-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lanzatech Domain Security
  slug: lanzatech-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Map LanzaTech leadership and board
  slug: lanzatech-people-and-governance
- name: Research LanzaTech from its own content API
  slug: lanzatech-research-company
slug: lanzatech
tags:
- Company
- Carbon Capture
- Climate Tech
- Sustainability
- Synthetic Biology
- Energy
- Chemicals
- Sustainable Aviation Fuel
- Manufacturing
- Content
website: https://lanzatech.com/
---
