---
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.9
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Addis Energy Agentic Access
  operation_count: 21
  slug: addis-energy-agentic-access
  summary_line: 21 operations
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Addis Energy website at addisenergy.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate '
  name: Addis Energy Website (WordPress REST)
  slug: addisenergy-com-website-wordpress-rest
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://addisenergy.com/
- group: company
  title: ''
  type: About
  url: https://addisenergy.com/technology/
- group: other
  title: ''
  type: x-team
  url: https://addisenergy.com/team/
- group: company
  title: ''
  type: Blog
  url: https://addisenergy.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://addisenergy.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://addisenergy.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://addisenergy.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://addisenergy.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://addisenergy.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/addisenergy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/addis-energy/refs/heads/main/authentication/addis-energy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/addis-energy-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/addis-energy/refs/heads/main/conventions/addis-energy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/addis-energy-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/addis-energy/refs/heads/main/errors/addis-energy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/addis-energy-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/addis-energy/refs/heads/main/data-model/addis-energy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/addis-energy-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/addis-energy/refs/heads/main/conformance/addis-energy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/addis-energy-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/addis-energy/refs/heads/main/lifecycle/addis-energy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/addis-energy-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/addis-energy/refs/heads/main/rate-limits/addis-energy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/addis-energy-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/addis-energy/refs/heads/main/plans/addis-energy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/addis-energy-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/addis-energy/refs/heads/main/llms/addis-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/addis-energy-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/addis-energy/refs/heads/main/examples/addis-energy-examples.yml
  title: ''
  type: Examples
  url: examples/addis-energy-examples.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/addis-energy/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/addis-energy/refs/heads/main/security/addis-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/addis-energy-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/addis-energy/refs/heads/main/agentic-access/addis-energy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/addis-energy-agentic-access.yml
created: '2026-09-07'
description: 'Addis Energy is a Somerville, Massachusetts deep-tech energy company founded in January 2025 out of research in the MIT Department of Materials Science and Engineering. It is developing Stimulated Geologic Ammonia — injecting nitrogen, water and engineered fluids into iron-rich subsurface rock and using the earth''s own heat and pressure as the reactor to produce ammonia underground rather than in a Haber-Bosch plant. Founded by Michael Alexander (CEO), Charlie Mitchell (COO), Iwnetim Abate (Chief Science Officer) and Yet-Ming Chiang (Chief Strategy Officer), it has raised an $8.3M seed round plus a $4.5M ARPA-E award, backed by Engine Ventures, At One Ventures, Pillar VC, Voyager VC, Blindspot Ventures and Emerson Collective. It is not a software vendor: no developer program, portal, SDKs or product API. The only machine-readable interface it exposes is the WordPress core REST content API behind addisenergy.com, captured here for discovery and anonymously readable but read-only.'
image: https://addisenergy.com/wp-content/uploads/fbrfg/apple-touch-icon.png
layout: provider
modified: '2026-09-07'
name: Addis Energy
nav: Providers
network: true
overview: 'Addis Energy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Clean Energy, Ammonia, and Climate Tech.


  Addis Energy''s developer surface includes engineering blog, authentication, code examples, and 20 more developer resources.'
plans:
- name: Addis Energy Plans Pricing
  plan_count: 0
  slug: addis-energy-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Addis Energy Rate Limits
  slug: addis-energy-rate-limits
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 6.5
    developer_ergonomics: 25.6
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 19.9
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Addis Energy Authentication
  slug: addis-energy-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Addis Energy Domain Security
  slug: addis-energy-domain-security
  summary_line: TLSv1.2
slug: addis-energy
tags:
- Company
- Energy
- Clean Energy
- Ammonia
- Climate Tech
- Deep Tech
- Geoscience
- Subsurface
- Materials Science
- Hydrogen
- Fertilizer
website: https://addisenergy.com/
---
