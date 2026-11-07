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
  score: 26.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Accountancyvaluation Com Agentic Access
  operation_count: 10
  slug: accountancyvaluation-com-agentic-access
  summary_line: 10 operations · 8 acting
api_count: 2
apis:
- baseURL: https://accountancyvaluation.com
  baseurl_source: declared
  description: enquiry
  name: Accountancy Valuation Enquiry API
  slug: accountancyvaluation-com-enquiry-api
- baseURL: https://accountancyvaluation.com
  baseurl_source: declared
  description: The mcp API from Accountancy Valuation — 1 operation(s) for mcp.
  name: Accountancy Valuation MCP API
  slug: accountancyvaluation-com-mcp-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/accountancyvaluation-com/agentic-access/accountancyvaluation-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/accountancyvaluation-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/accountancyvaluation-com/rules/accountancyvaluation-com-rules.yml
  title: ''
  type: Spectral
  url: rules/accountancyvaluation-com-rules.yml
- group: design
  href: https://artifacts.apis.io/accountancyvaluation-com/vocabulary/accountancyvaluation-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/accountancyvaluation-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/accountancyvaluation-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://accountancyvaluation.com/terms
- group: design
  href: https://artifacts.apis.io/accountancyvaluation-com/errors/accountancyvaluation-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/accountancyvaluation-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/accountancyvaluation-com/conformance/accountancyvaluation-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/accountancyvaluation-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/accountancyvaluation-com/llms/accountancyvaluation-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accountancyvaluation-com-llms.txt
- group: build
  href: https://artifacts.apis.io/accountancyvaluation-com/mcp/accountancyvaluation-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/accountancyvaluation-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/accountancyvaluation-com/mcp/accountancyvaluation-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/accountancyvaluation-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/accountancyvaluation-com/well-known/accountancyvaluation-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/accountancyvaluation-com-security.txt
- group: agent
  href: https://artifacts.apis.io/accountancyvaluation-com/well-known/accountancyvaluation-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/accountancyvaluation-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/accountancyvaluation-com/hosts/accountancyvaluation-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/accountancyvaluation-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/accountancyvaluation-com/vendors/accountancyvaluation-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/accountancyvaluation-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/accountancyvaluation-com/authentication/accountancyvaluation-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/accountancyvaluation-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/accountancyvaluation-com/security/accountancyvaluation-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/accountancyvaluation-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/accountancyvaluation-com/security/accountancyvaluation-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accountancyvaluation-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accountancyvaluation.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accountancyvaluation.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://accountancyvaluation.com/terms/
- group: company
  title: ''
  type: About
  url: https://accountancyvaluation.com/about/
created: '2026-10-31'
description: Accountancy Valuation provides valuation services for accounting and CPA practices in the United States. The site offers guidance on practice valuation multiples, retention clauses, earn-outs, and allocation methods, along with data tables and broker quotes. It includes a quote form for practice owners to receive valuation estimates, and publishes articles, guides, and datasets related to practice sales and financial metrics. Contact is available via enquiries@accountancyvaluation.com, with terms and privacy policies linked.
image: https://accountancyvaluation.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at accountancyvaluation.com.
  name: Accountancy Valuation MCP Server
  slug: accountancyvaluation-com-mcp-yml
modified: '2026-10-31'
name: Accountancy Valuation
nav: Providers
network: true
overview: 'Accountancy Valuation publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Enquiry API and MCP API. Tagged areas include Accounting, Valuation, CPA, Practice, and US.


  The Accountancy Valuation catalog on APIs.io includes 1 Spectral governance ruleset.


  Accountancy Valuation''s developer surface includes authentication and 20 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Accountancy Valuation API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: accountancyvaluation-com-rules
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 47.4
    developer_ergonomics: 13.7
    discoverability: 65.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Accountancyvaluation Com Authentication
  slug: accountancyvaluation-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Accountancyvaluation Com Domain Security
  slug: accountancyvaluation-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Accountancyvaluation Com Vulnerability Disclosure
  slug: accountancyvaluation-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: accountancyvaluation-com-enquiry-process
  slug: accountancyvaluation-com-enquiry-process
slug: accountancyvaluation-com
tags:
- Accounting
- Valuation
- CPA
- Practice
- US
website: https://accountancyvaluation.com/
---
