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
- acting_count: 7
  human_in_the_loop: 0
  name: Calibvo Com Agentic Access
  operation_count: 9
  slug: calibvo-com-agentic-access
  summary_line: 9 operations · 7 acting
api_count: 1
apis:
- baseURL: https://calibvo.com
  baseurl_source: declared
  description: dataset
  name: Calibvo Dataset API
  slug: calibvo-com-dataset-api
- baseURL: https://calibvo.com
  baseurl_source: declared
  description: The mcp API from Calibvo — 1 operation(s) for mcp.
  name: Calibvo MCP API
  slug: calibvo-com-mcp-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/calibvo-com/agentic-access/calibvo-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/calibvo-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/calibvo-com/plans/calibvo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/calibvo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/calibvo-com/rules/calibvo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/calibvo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/calibvo-com/vocabulary/calibvo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/calibvo-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/calibvo-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://calibvo.com/terms
- group: design
  href: https://artifacts.apis.io/calibvo-com/errors/calibvo-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/calibvo-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/calibvo-com/conformance/calibvo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/calibvo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/calibvo-com/llms/calibvo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/calibvo-com-llms.txt
- group: build
  href: https://artifacts.apis.io/calibvo-com/mcp/calibvo-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/calibvo-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/calibvo-com/mcp/calibvo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/calibvo-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/calibvo-com/well-known/calibvo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/calibvo-com-security.txt
- group: auth
  href: https://artifacts.apis.io/calibvo-com/well-known/calibvo-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/calibvo-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/calibvo-com/well-known/calibvo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/calibvo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/calibvo-com/hosts/calibvo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calibvo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/calibvo-com/vendors/calibvo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calibvo-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calibvo.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://calibvo.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calibvo.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://calibvo.com/pricing/
- group: auth
  href: https://artifacts.apis.io/calibvo-com/authentication/calibvo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/calibvo-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/calibvo-com/security/calibvo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/calibvo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/calibvo-com/security/calibvo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calibvo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calibvo.com/
created: '2026-11-03'
description: Calibvo provides free AI‑powered literature review worksheets and tools to help researchers organize, extract, and synthesize data from academic papers. The site offers two worksheets, a matrix for extraction, and software that automates parts of the review process, aiming to make systematic reviews more transparent and reproducible. Founded in September 2026, Calibvo focuses on open‑science resources and supports users with contact support and documentation.
image: https://calibvo.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at calibvo.com.
  name: Calibvo MCP Server
  slug: calibvo-com-mcp-yml
modified: '2026-11-03'
name: Calibvo
nav: Providers
network: true
overview: 'Calibvo publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Dataset API and MCP API. Tagged areas include Artificial Intelligence, Literature Review, Open Science, Tools, and Education.


  The Calibvo catalog on APIs.io includes 1 Spectral governance ruleset.


  Calibvo''s developer surface includes support, pricing, authentication, and 21 more developer resources.'
plans:
- name: Calibvo Com Plans Pricing
  plan_count: 2
  slug: calibvo-com-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Calibvo API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: calibvo-com-rules
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 35.6
    contract_quality: 47.4
    developer_ergonomics: 16.1
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Calibvo Com Authentication
  slug: calibvo-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Calibvo Com Domain Security
  slug: calibvo-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Calibvo Com Vulnerability Disclosure
  slug: calibvo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dataset
  slug: calibvo-com-dataset
slug: calibvo-com
tags:
- Artificial Intelligence
- Literature Review
- Open Science
- Tools
- Education
website: https://calibvo.com/
---
