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
  score: 24.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Cheap409A Com Agentic Access
  operation_count: 8
  slug: cheap409a-com-agentic-access
  summary_line: 8 operations · 7 acting
api_count: 1
apis:
- description: API providing valuation comparison and enquiry tools as described in the OpenAPI spec.
  name: Cheap 409A API
  slug: cheap-409a-api
- baseURL: https://cheap409a.com
  baseurl_source: declared
  description: enquiry
  name: Cheap 409A Enquiry API
  slug: cheap409a-com-enquiry-api
- baseURL: https://cheap409a.com
  baseurl_source: declared
  description: compare
  name: Cheap 409A Guide API
  slug: cheap409a-com-guide-api
- baseURL: https://cheap409a.com
  baseurl_source: declared
  description: The mcp API from Cheap 409A — 1 operation(s) for mcp.
  name: Cheap 409A MCP API
  slug: cheap409a-com-mcp-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/cheap409a-com/agentic-access/cheap409a-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cheap409a-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cheap409a-com/rules/cheap409a-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cheap409a-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cheap409a-com/vocabulary/cheap409a-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cheap409a-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cheap409a-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://cheap409a.com/terms
- group: design
  href: https://artifacts.apis.io/cheap409a-com/errors/cheap409a-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cheap409a-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cheap409a-com/conformance/cheap409a-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cheap409a-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cheap409a-com/llms/cheap409a-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cheap409a-com-llms.txt
- group: build
  href: https://artifacts.apis.io/cheap409a-com/mcp/cheap409a-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cheap409a-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cheap409a-com/mcp/cheap409a-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cheap409a-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/cheap409a-com/well-known/cheap409a-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cheap409a-com-security.txt
- group: agent
  href: https://artifacts.apis.io/cheap409a-com/well-known/cheap409a-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cheap409a-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cheap409a-com/hosts/cheap409a-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cheap409a-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cheap409a-com/vendors/cheap409a-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cheap409a-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cheap409a.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cheap409a.com/privacy/
- group: auth
  href: https://artifacts.apis.io/cheap409a-com/authentication/cheap409a-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cheap409a-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cheap409a-com/security/cheap409a-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cheap409a-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cheap409a-com/security/cheap409a-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cheap409a-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cheap409a.com/
created: '2026-11-04'
description: Cheap 409A provides 409A valuation services with transparent pricing ranging from $990 to $3,500. The site offers detailed comparisons of providers, pricing tiers, and guidance on valuation frequency, turnaround times, and regulatory considerations. It serves startups and growing companies seeking compliant valuation solutions.
image: https://cheap409a.com/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at cheap409a.com.
  name: Cheap 409A MCP Server
  slug: cheap409a-com-mcp-yml
modified: '2026-11-04'
name: Cheap 409A
nav: Providers
network: true
overview: 'Cheap 409A publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Enquiry API, Guide API, MCP API, and 1 more. Tagged areas include Company, Valuation, Startups, Finance, and Pricing.


  The Cheap 409A catalog on APIs.io includes 1 Spectral governance ruleset.


  Cheap 409A''s developer surface includes authentication and 19 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Cheap 409A API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: cheap409a-com-rules
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 48.8
    developer_ergonomics: 13.7
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
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
  name: Cheap409A Com Authentication
  slug: cheap409a-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cheap409A Com Domain Security
  slug: cheap409a-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cheap409A Com Vulnerability Disclosure
  slug: cheap409a-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: cheap409a-com-compare
  slug: cheap409a-com-compare
- name: cheap409a-com-enquiry-process
  slug: cheap409a-com-enquiry-process
slug: cheap409a-com
tags:
- Company
- Valuation
- Startups
- Finance
- Pricing
website: https://cheap409a.com/
---
