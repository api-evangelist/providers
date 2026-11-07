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
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Assay Systems Com Agentic Access
  operation_count: 7
  slug: assay-systems-com-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://assay-systems.com
  baseurl_source: declared
  description: The Free API from Assay Systems — 2 operation(s) for free.
  name: Assay Systems Free API
  slug: assay-systems-com-free-api
- baseURL: https://assay-systems.com
  baseurl_source: declared
  description: The Paid API from Assay Systems — 5 operation(s) for paid.
  name: Assay Systems Paid API
  slug: assay-systems-com-paid-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/assay-systems-com/agentic-access/assay-systems-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/assay-systems-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/assay-systems-com/rules/assay-systems-com-rules.yml
  title: ''
  type: Spectral
  url: rules/assay-systems-com-rules.yml
- group: design
  href: https://artifacts.apis.io/assay-systems-com/vocabulary/assay-systems-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/assay-systems-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/assay-systems-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/assay-systems-com/errors/assay-systems-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/assay-systems-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/assay-systems-com/conformance/assay-systems-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/assay-systems-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/assay-systems-com/llms/assay-systems-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/assay-systems-com-llms.txt
- group: other
  href: https://artifacts.apis.io/assay-systems-com/hosts/assay-systems-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/assay-systems-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/assay-systems-com/vendors/assay-systems-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/assay-systems-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://assay-systems.com/register/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/assay-systems
- group: auth
  href: https://artifacts.apis.io/assay-systems-com/security/assay-systems-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assay-systems-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://assay-systems.com/
- group: commercial
  title: ''
  type: Terms
  url: https://assay-systems.com/terms/
- group: commercial
  title: ''
  type: Privacy
  url: https://assay-systems.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://assay-systems.com/support/
created: '2026-11-01'
description: Assay Systems provides government contract intelligence by aggregating public register data to identify excluded firms, grants, contract end dates, and contract holders. Based in Ottawa, Canada, the service offers searchable data to help organizations monitor federal contracting activity.
image: https://assay-systems.com/assets/mark.png
layout: provider
modified: '2026-11-01'
name: Assay Systems
nav: Providers
network: true
overview: 'Assay Systems publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Free API and Paid API. Tagged areas include Company, Government, Contracts, Intelligence, and Data.


  The Assay Systems catalog on APIs.io includes 1 Spectral governance ruleset.


  Assay Systems'' developer surface includes signup flow, terms of service, privacy policy, support, and 12 more developer resources.'
plans:
- name: Assay Systems Com Plans Pricing
  plan_count: 0
  slug: assay-systems-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Assay Systems Com Rate Limits
  slug: assay-systems-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Assay Systems API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: assay-systems-com-rules
scopes:
- name: Assay Systems Com Scopes
  scope_count: 0
  slug: assay-systems-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 44.7
    developer_ergonomics: 8.8
    discoverability: 66.1
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 29.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Assay Systems Com Authentication
  slug: assay-systems-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Assay Systems Com Domain Security
  slug: assay-systems-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: search
  slug: assay-systems-com-search-skill
slug: assay-systems-com
tags:
- Company
- Government
- Contracts
- Intelligence
- Data
- Canada
website: https://assay-systems.com/
---
