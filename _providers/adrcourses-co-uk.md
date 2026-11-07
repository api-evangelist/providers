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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Adrcourses Co Uk Agentic Access
  operation_count: 5
  slug: adrcourses-co-uk-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- baseURL: https://adrcourses.co.uk
  baseurl_source: declared
  description: enquiry
  name: ADR Courses Enquiry API
  slug: adrcourses-co-uk-enquiry-api
- baseURL: https://adrcourses.co.uk
  baseurl_source: declared
  description: The mcp API from ADR Courses — 1 operation(s) for mcp.
  name: ADR Courses MCP API
  slug: adrcourses-co-uk-mcp-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/adrcourses-co-uk/agentic-access/adrcourses-co-uk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adrcourses-co-uk-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/adrcourses-co-uk/rules/adrcourses-co-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/adrcourses-co-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/adrcourses-co-uk/vocabulary/adrcourses-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adrcourses-co-uk-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/adrcourses-co-uk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://adrcourses.co.uk/terms
- group: design
  href: https://artifacts.apis.io/adrcourses-co-uk/errors/adrcourses-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adrcourses-co-uk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adrcourses-co-uk/conformance/adrcourses-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adrcourses-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adrcourses-co-uk/llms/adrcourses-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adrcourses-co-uk-llms.txt
- group: build
  href: https://artifacts.apis.io/adrcourses-co-uk/mcp/adrcourses-co-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/adrcourses-co-uk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/adrcourses-co-uk/mcp/adrcourses-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adrcourses-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/adrcourses-co-uk/well-known/adrcourses-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adrcourses-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/adrcourses-co-uk/well-known/adrcourses-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adrcourses-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/adrcourses-co-uk/hosts/adrcourses-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adrcourses-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/adrcourses-co-uk/vendors/adrcourses-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adrcourses-co-uk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/adrcourses-co-uk/authentication/adrcourses-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adrcourses-co-uk-authentication.yml
- group: auth
  href: https://artifacts.apis.io/adrcourses-co-uk/security/adrcourses-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/adrcourses-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/adrcourses-co-uk/security/adrcourses-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adrcourses-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adrcourses.co.uk/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adrcourses.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adrcourses.co.uk/privacy/
- group: operate
  title: ''
  type: Support
  url: https://adrcourses.co.uk/contact/
- group: docs
  title: ''
  type: Documentation
  url: https://adrcourses.co.uk/about/
created: '2026-10-31'
description: ADR Courses provides comprehensive ADR (Accord Dangerous Goods) training in the UK, offering core modules, class and tank modules, and a 5‑year driver card. Prices vary per module and are quoted individually. The site references official training times from gov.uk and offers free quotes. Training helps drivers meet HGV licence and CPC requirements.
image: https://adrcourses.co.uk/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at adrcourses.co.uk.
  name: ADR Courses MCP Server
  slug: adrcourses-co-uk-mcp-yml
modified: '2026-10-31'
name: ADR Courses
nav: Providers
network: true
overview: 'ADR Courses publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Enquiry API and MCP API. Tagged areas include ADR, Training, United Kingdom, Transportation, and Safety.


  The ADR Courses catalog on APIs.io includes 1 Spectral governance ruleset.


  ADR Courses'' developer surface includes authentication, support, documentation, and 19 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: ADR Courses API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: adrcourses-co-uk-rules
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 47.4
    developer_ergonomics: 25.5
    discoverability: 65.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adrcourses Co Uk Authentication
  slug: adrcourses-co-uk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Adrcourses Co Uk Domain Security
  slug: adrcourses-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adrcourses Co Uk Vulnerability Disclosure
  slug: adrcourses-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: enquiry
  slug: adrcourses-co-uk-enquiry
slug: adrcourses-co-uk
tags:
- ADR
- Training
- United Kingdom
- Transportation
- Safety
website: https://adrcourses.co.uk/
---
