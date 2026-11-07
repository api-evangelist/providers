---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Adopte Un Conteneur Fr Agentic Access
  operation_count: 1
  slug: adopte-un-conteneur-fr-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://adopte-un-conteneur.fr
  baseurl_source: declared
  description: The Delivery API from Adopte Un Conteneur — 1 operation(s) for delivery.
  name: Adopte Un Conteneur Delivery API
  slug: adopte-un-conteneur-fr-delivery-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/adopte-un-conteneur-fr/agentic-access/adopte-un-conteneur-fr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adopte-un-conteneur-fr-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/adopte-un-conteneur-fr/rules/adopte-un-conteneur-fr-rules.yml
  title: ''
  type: Spectral
  url: rules/adopte-un-conteneur-fr-rules.yml
- group: agent
  href: https://artifacts.apis.io/adopte-un-conteneur-fr/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/adopte-un-conteneur-fr/errors/adopte-un-conteneur-fr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adopte-un-conteneur-fr-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adopte-un-conteneur-fr/conformance/adopte-un-conteneur-fr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adopte-un-conteneur-fr-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adopte-un-conteneur-fr/llms/adopte-un-conteneur-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adopte-un-conteneur-fr-llms.txt
- group: agent
  href: https://artifacts.apis.io/adopte-un-conteneur-fr/well-known/adopte-un-conteneur-fr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adopte-un-conteneur-fr-well-known.yml
- group: other
  href: https://artifacts.apis.io/adopte-un-conteneur-fr/hosts/adopte-un-conteneur-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adopte-un-conteneur-fr-hosts.yml
- group: auth
  href: https://artifacts.apis.io/adopte-un-conteneur-fr/security/adopte-un-conteneur-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adopte-un-conteneur-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adopte-un-conteneur.fr/
- group: operate
  title: ''
  type: Support
  url: https://adopte-un-conteneur.fr/contact/
- group: company
  title: ''
  type: Blog
  url: https://adopte-un-conteneur.fr/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adopte-un-conteneur.fr/cgv/
created: '2026-10-31'
description: Adopte Un Conteneur is a French company that sells new and used maritime containers, modular bungalows, self‑storage boxes and accessories, delivering throughout France. Operating from 17 Rue de l'Isère, 31500 Toulouse under the legal name SAS BRYT DEVELOPPEMENT, it serves professionals, collectivités and private customers with a range of container sizes and options.
image: https://adopte-un-conteneur.fr/wp-content/uploads/2022/04/Adopte-un-conteneur-logo-Full-250-%C3%97-100-px.png
layout: provider
modified: '2026-10-31'
name: Adopte Un Conteneur
nav: Providers
network: true
overview: 'Adopte Un Conteneur publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Delivery API. Tagged areas include Containers, Maritime, Storage, Modular, and France.


  The Adopte Un Conteneur catalog on APIs.io includes 1 Spectral governance ruleset.


  Adopte Un Conteneur''s developer surface includes support, engineering blog, and 11 more developer resources.'
plans:
- name: Adopte Un Conteneur Fr Plans Pricing
  plan_count: 0
  slug: adopte-un-conteneur-fr-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Adopte Un Conteneur Fr Rate Limits
  slug: adopte-un-conteneur-fr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Adopte Un Conteneur API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: adopte-un-conteneur-fr-rules
scopes:
- name: Adopte Un Conteneur Fr Scopes
  scope_count: 0
  slug: adopte-un-conteneur-fr-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 5.3
    contract_governance: 18.2
    contract_quality: 49.6
    developer_ergonomics: 10.0
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 28.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adopte Un Conteneur Fr Authentication
  slug: adopte-un-conteneur-fr-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Adopte Un Conteneur Fr Domain Security
  slug: adopte-un-conteneur-fr-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: calculate-delivery-cost
  slug: adopte-un-conteneur-fr-calculate-delivery-cost
slug: adopte-un-conteneur-fr
tags:
- Containers
- Maritime
- Storage
- Modular
- France
website: https://adopte-un-conteneur.fr/
---
