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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.2
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Accelsius Agentic Access
  operation_count: 23
  slug: accelsius-agentic-access
  summary_line: 23 operations
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Accelsius website at accelsius.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Accelsius Website (WordPress REST)
  slug: accelsius-com-website-wordpress-rest
artifact_total: 5
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accelsius/refs/heads/main/mcp/accelsius-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/accelsius-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/accelsius/refs/heads/main/authentication/accelsius-authentication.yml
  title: ''
  type: Authentication
  url: authentication/accelsius-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/accelsius/refs/heads/main/security/accelsius-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accelsius-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accelsius.com/
- group: company
  title: ''
  type: About
  url: https://accelsius.com/company/
- group: operate
  title: ''
  type: Contact
  url: https://accelsius.com/contact/
- group: operate
  title: ''
  type: Support
  url: https://accelsius.com/customer-support/
- group: operate
  title: ''
  type: FAQ
  url: https://accelsius.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://accelsius.com/resources/
- group: company
  title: ''
  type: BlogFeeds
  url: https://accelsius.com/feed/
- group: company
  title: ''
  type: Newsroom
  url: https://accelsius.com/in-the-news/
- group: other
  title: ''
  type: WhitePapers
  url: https://accelsius.com/papers-studies/
- group: company
  title: ''
  type: Partners
  url: https://accelsius.com/our-partners/
- group: company
  title: ''
  type: Careers
  url: https://accelsius.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/accelsius
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accelsius.com/privacy-policy/
- group: other
  title: ''
  type: Sitemap
  url: https://accelsius.com/sitemap_index.xml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accelsius/refs/heads/main/agentic-access/accelsius-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/accelsius-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accelsius/refs/heads/main/errors/accelsius-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/accelsius-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accelsius/refs/heads/main/conventions/accelsius-conventions.yml
  title: ''
  type: Conventions
  url: conventions/accelsius-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accelsius/refs/heads/main/data-model/accelsius-data-model.yml
  title: ''
  type: DataModel
  url: data-model/accelsius-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accelsius/refs/heads/main/conformance/accelsius-conformance.yml
  title: ''
  type: Conformance
  url: conformance/accelsius-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accelsius/refs/heads/main/lifecycle/accelsius-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/accelsius-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accelsius/refs/heads/main/well-known/accelsius-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/accelsius-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accelsius/refs/heads/main/llms/accelsius-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accelsius-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/accelsius/refs/heads/main/mcp/accelsius-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/accelsius-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accelsius/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/accelsius/refs/heads/main/examples/accelsius-examples.yml
  title: ''
  type: Examples
  url: examples/accelsius-examples.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/accelsius/refs/heads/main/well-known/accelsius-robots.txt
  title: ''
  type: Robots
  url: well-known/accelsius-robots.txt
created: '2026-08-06'
description: 'Accelsius LLC is an Austin, Texas thermal-management company founded in 2022 by Innventure to commercialize two-phase, direct-to-chip liquid cooling for AI, HPC and mission-critical data centers. Its NeuCool platform circulates a non-conductive dielectric refrigerant through cold plates mounted directly on CPUs and GPUs, removing heat by evaporation rather than by bringing water into the IT rack, and supports 4,500W+ per socket and rack densities up to 250kW. The product line includes the IR150 in-rack CDU, the MR250 medium-rack CDU, the NeuCool Thermal Simulation Rack and Liquid Simulation System used for evaluation and deployment planning, and multi-GPU cold plate assemblies, backed by professional services spanning system architecture, integration, deployment and maintenance. Accelsius is a hardware manufacturer, not a software or data company: it publishes no developer program, product API, SDK or machine-readable product specification. The only machine-readable interface
  on its public surface is the WordPress core REST API behind accelsius.com, which serves the company''s own blog, news, white-paper, case-study, podcast and video content anonymously and read-only.'
image: https://accelsius.com/wp-content/uploads/Accelsius_Logo_Footer-1.svg
layout: provider
modified: '2026-08-06'
name: Accelsius
nav: Providers
network: true
overview: 'Accelsius publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Center, Liquid Cooling, Thermal Management, and Direct-to-Chip Cooling.


  Accelsius'' developer surface includes authentication, support, FAQ, engineering blog, code examples, and 24 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 6.5
    developer_ergonomics: 30.4
    discoverability: 58.0
    operational_transparency: 0.0
  previous_composite: 16.9
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/accelsius/refs/heads/main/screenshots/accelsius-2026-08-07T160754.png
security:
- kind: authentication
  name: Accelsius Authentication
  slug: accelsius-authentication
  summary_line: none/http/cookie · 3 schemes
- kind: domain-security
  name: Accelsius Domain Security
  slug: accelsius-domain-security
  summary_line: TLSv1.3 · DMARC
slug: accelsius
tags:
- Company
- Data Center
- Liquid Cooling
- Thermal Management
- Direct-to-Chip Cooling
- Two-Phase Cooling
- Artificial Intelligence Infrastructure
- High Performance Computing
- Hardware
- Manufacturing
- WordPress
website: https://accelsius.com/
---
