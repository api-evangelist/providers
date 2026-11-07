---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 70
  human_in_the_loop: 0
  name: Cosmic Ephemeris Agentic Access
  operation_count: 78
  slug: cosmic-ephemeris-agentic-access
  summary_line: 78 operations · 70 acting
api_count: 1
apis:
- baseURL: https://api.cosmicephemeris.com
  baseurl_source: declared
  description: The Calculations API from Cosmic Ephemeris — 76 operation(s) for calculations.
  name: Cosmic Ephemeris Calculations API
  slug: cosmic-ephemeris-calculations-api
- baseURL: https://api.cosmicephemeris.com
  baseurl_source: declared
  description: Deterministic rule-based output, distinct from raw calculation data.
  name: Cosmic Ephemeris Interpretation API
  slug: cosmic-ephemeris-interpretation-api
- baseURL: https://api.cosmicephemeris.com
  baseurl_source: declared
  description: The Pro timeline API from Cosmic Ephemeris — 1 operation(s) for pro timeline.
  name: Cosmic Ephemeris Pro timeline API
  slug: cosmic-ephemeris-pro-timeline-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/cosmic-ephemeris/agentic-access/cosmic-ephemeris-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cosmic-ephemeris-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/cosmic-ephemeris/plans/cosmic-ephemeris-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cosmic-ephemeris-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cosmic-ephemeris/rules/cosmic-ephemeris-rules.yml
  title: ''
  type: Spectral
  url: rules/cosmic-ephemeris-rules.yml
- group: design
  href: https://artifacts.apis.io/cosmic-ephemeris/json-ld/cosmic-ephemeris-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cosmic-ephemeris-context.jsonld
- group: design
  href: https://artifacts.apis.io/cosmic-ephemeris/vocabulary/cosmic-ephemeris-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cosmic-ephemeris-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cosmic-ephemeris/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cosmic-ephemeris/data-model/cosmic-ephemeris-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cosmic-ephemeris-data-model.yml
- group: design
  href: https://artifacts.apis.io/cosmic-ephemeris/conventions/cosmic-ephemeris-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cosmic-ephemeris-conventions.yml
- group: design
  href: https://artifacts.apis.io/cosmic-ephemeris/conventions/cosmic-ephemeris-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cosmic-ephemeris-conventions.yml
- group: auth
  href: https://artifacts.apis.io/cosmic-ephemeris/security/cosmic-ephemeris-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cosmic-ephemeris-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cosmic-ephemeris/authentication/cosmic-ephemeris-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cosmic-ephemeris-authentication.yml
- group: design
  href: https://artifacts.apis.io/cosmic-ephemeris/errors/cosmic-ephemeris-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cosmic-ephemeris-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cosmic-ephemeris/conformance/cosmic-ephemeris-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cosmic-ephemeris-conformance.yml
- group: build
  href: https://artifacts.apis.io/cosmic-ephemeris/mcp/cosmic-ephemeris-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cosmic-ephemeris-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cosmic-ephemeris/mcp/cosmic-ephemeris-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cosmic-ephemeris-mcp.yml
- group: auth
  href: https://artifacts.apis.io/cosmic-ephemeris/well-known/cosmic-ephemeris-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cosmic-ephemeris-security.txt
- group: agent
  href: https://artifacts.apis.io/cosmic-ephemeris/well-known/cosmic-ephemeris-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cosmic-ephemeris-well-known.yml
- group: other
  href: https://artifacts.apis.io/cosmic-ephemeris/hosts/cosmic-ephemeris-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cosmic-ephemeris-hosts.yml
- group: build
  href: https://artifacts.apis.io/cosmic-ephemeris/packages/cosmic-ephemeris-packages.yml
  title: ''
  type: SDKs
  url: packages/cosmic-ephemeris-packages.yml
- group: build
  href: https://artifacts.apis.io/cosmic-ephemeris/packages/cosmic-ephemeris-packages.yml
  title: ''
  type: Packages
  url: packages/cosmic-ephemeris-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cosmicephemeris.com/terms.html
- group: start
  title: ''
  type: SignUp
  url: https://cosmicephemeris.com/signup.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cosmicephemeris.com/privacy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://cosmicephemeris.com/pricing.html
- group: start
  title: ''
  type: GettingStarted
  url: https://cosmicephemeris.com/docs-onboarding-context.html
- group: auth
  href: https://artifacts.apis.io/cosmic-ephemeris/security/cosmic-ephemeris-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cosmic-ephemeris-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cosmic-ephemeris/security/cosmic-ephemeris-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cosmic-ephemeris-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cosmicephemeris.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cosmicephemeris.com/docs.html
created: '2026-10-20'
description: Cosmic Ephemeris provides a comprehensive suite of astrology calculation APIs, offering 78 live endpoints covering Western, Sidereal, and Vedic astrology, symbolic readings, Tarot interpretations, and Hindu calendar data. The service supports up to 500 free monthly requests and includes SDK and MCP guides for developers.
image: https://cosmicephemeris.com/images/cosmic-ephemeris-social.png
json_schemas:
- name: BirthChartResponse
  property_count: 3
  slug: cosmic-ephemeris-birth-chart-response
- name: ConnectedElectionalCriterionRepairHardeningParetoAuditElectionalCriterionRepairHardeningParetoAuditResponse
  property_count: 0
  slug: cosmic-ephemeris-connected-electional-criterion-repair-hardening-pareto-audit-electional-criterion-repair-hardening-pareto-audit-response
- name: ConnectedElectionalCriterionRepairHardeningParetoHierarchyAuditElectionalCriterionRepairHardeningParetoHierarchyAuditResponse
  property_count: 0
  slug: cosmic-ephemeris-connected-electional-criterion-repair-hardening-pareto-hierarchy-audit-electional-criterion-repair-hardening-pareto-hierarchy-audit-response
- name: ConnectedVimshottariResponse
  property_count: 0
  slug: cosmic-ephemeris-connected-vimshottari-response
- name: PlaceSearchRequest
  property_count: 3
  slug: cosmic-ephemeris-place-search-request
- name: PlaceSearchResponse
  property_count: 6
  slug: cosmic-ephemeris-place-search-response
jsonld:
- class_count: 120
  name: Cosmic Ephemeris Context
  property_count: 328
  slug: cosmic-ephemeris-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.cosmicephemeris.com requiring an API key.
  name: Cosmic Ephemeris MCP Server
  slug: cosmic-ephemeris-mcp-yml
modified: '2026-10-20'
name: Cosmic Ephemeris
nav: Providers
network: true
overview: 'Cosmic Ephemeris publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Calculations API, Interpretation API, and Pro timeline API. Tagged areas include Astrology, Developers, Data, and U.S.-based.


  The Cosmic Ephemeris catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cosmic Ephemeris'' developer surface includes authentication, signup flow, pricing, getting-started guide, documentation, and 24 more developer resources.'
plans:
- name: Cosmic Ephemeris Plans Pricing
  plan_count: 3
  slug: cosmic-ephemeris-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Cosmic Ephemeris API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: cosmic-ephemeris-rules
score:
  band: developing
  composite: 45.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 69.3
    developer_ergonomics: 31.5
    discoverability: 60.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cosmic-ephemeris/cosmic-ephemeris-2026-11-03T125411.png
security:
- kind: authentication
  name: Cosmic Ephemeris Authentication
  slug: cosmic-ephemeris-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cosmic Ephemeris Domain Security
  slug: cosmic-ephemeris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cosmic Ephemeris Vulnerability Disclosure
  slug: cosmic-ephemeris-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: cosmic-ephemeris-calculate-full-birth-chart
  slug: cosmic-ephemeris-calculate-full-birth-chart
slug: cosmic-ephemeris
tags:
- Astrology
- Developers
- Data
- U.S.-based
website: https://cosmicephemeris.com/
---
