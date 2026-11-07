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
    agent_skills: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Classqchecker Co Uk Agentic Access
  operation_count: 1
  slug: classqchecker-co-uk-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: API for Class Q Checker MCP tools
  name: Class Q Checker API
  slug: class-q-checker-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/classqchecker-co-uk/agentic-access/classqchecker-co-uk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/classqchecker-co-uk-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/classqchecker-co-uk/rules/classqchecker-co-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/classqchecker-co-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/classqchecker-co-uk/vocabulary/classqchecker-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/classqchecker-co-uk-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://classqchecker.co.uk/terms
- group: design
  href: https://artifacts.apis.io/classqchecker-co-uk/errors/classqchecker-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/classqchecker-co-uk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/classqchecker-co-uk/conformance/classqchecker-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/classqchecker-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/classqchecker-co-uk/llms/classqchecker-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/classqchecker-co-uk-llms.txt
- group: build
  href: https://artifacts.apis.io/classqchecker-co-uk/mcp/classqchecker-co-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/classqchecker-co-uk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/classqchecker-co-uk/mcp/classqchecker-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/classqchecker-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/classqchecker-co-uk/well-known/classqchecker-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/classqchecker-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/classqchecker-co-uk/well-known/classqchecker-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/classqchecker-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/classqchecker-co-uk/hosts/classqchecker-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/classqchecker-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/classqchecker-co-uk/vendors/classqchecker-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/classqchecker-co-uk-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://classqchecker.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://classqchecker.co.uk/privacy/
- group: auth
  href: https://artifacts.apis.io/classqchecker-co-uk/authentication/classqchecker-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/classqchecker-co-uk-authentication.yml
- group: auth
  href: https://artifacts.apis.io/classqchecker-co-uk/security/classqchecker-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/classqchecker-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/classqchecker-co-uk/security/classqchecker-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/classqchecker-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://classqchecker.co.uk/
- group: operate
  title: ''
  type: Support
  url: https://classqchecker.co.uk/contact/
created: '2026-11-03'
description: Class Q Checker provides a free online tool to determine whether a barn conversion in England qualifies under Class Q permitted development. It offers detailed guidance, statutory tests, cost indexes, and links to legislation, helping users assess eligibility, required approvals, and planning considerations for converting agricultural buildings into dwellings.
image: https://classqchecker.co.uk/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at classqchecker.co.uk requiring an API key.
  name: Class Q Checker MCP Server
  slug: classqchecker-co-uk-mcp-yml
modified: '2026-11-03'
name: Class Q Checker
nav: Providers
network: true
overview: 'Class Q Checker is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Class Q, Planning, United Kingdom, Real Estate, and Permitted Development.


  The Class Q Checker catalog on APIs.io includes 1 Spectral governance ruleset.


  Class Q Checker''s developer surface includes authentication, support, and 18 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Class Q Checker API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: classqchecker-co-uk-rules
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
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
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Classqchecker Co Uk Authentication
  slug: classqchecker-co-uk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Classqchecker Co Uk Domain Security
  slug: classqchecker-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Classqchecker Co Uk Vulnerability Disclosure
  slug: classqchecker-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: classqchecker-co-uk
tags:
- Class Q
- Planning
- United Kingdom
- Real Estate
- Permitted Development
website: https://classqchecker.co.uk/
---
