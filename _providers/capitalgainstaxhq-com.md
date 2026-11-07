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
- acting_count: 10
  human_in_the_loop: 0
  name: Capitalgainstaxhq Com Agentic Access
  operation_count: 12
  slug: capitalgainstaxhq-com-agentic-access
  summary_line: 12 operations · 10 acting
api_count: 1
apis:
- baseURL: https://capitalgainstaxhq.com
  baseurl_source: declared
  description: dataset
  name: Capital Gains Tax HQ Dataset API
  slug: capitalgainstaxhq-com-dataset-api
- baseURL: https://capitalgainstaxhq.com
  baseurl_source: declared
  description: enquiry
  name: Capital Gains Tax HQ Enquiry API
  slug: capitalgainstaxhq-com-enquiry-api
- baseURL: https://capitalgainstaxhq.com
  baseurl_source: declared
  description: The mcp API from Capital Gains Tax HQ — 1 operation(s) for mcp.
  name: Capital Gains Tax HQ MCP API
  slug: capitalgainstaxhq-com-mcp-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/capitalgainstaxhq-com/agentic-access/capitalgainstaxhq-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/capitalgainstaxhq-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/capitalgainstaxhq-com/rules/capitalgainstaxhq-com-rules.yml
  title: ''
  type: Spectral
  url: rules/capitalgainstaxhq-com-rules.yml
- group: design
  href: https://artifacts.apis.io/capitalgainstaxhq-com/vocabulary/capitalgainstaxhq-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/capitalgainstaxhq-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/capitalgainstaxhq-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://capitalgainstaxhq.com/terms
- group: design
  href: https://artifacts.apis.io/capitalgainstaxhq-com/errors/capitalgainstaxhq-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/capitalgainstaxhq-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/capitalgainstaxhq-com/conformance/capitalgainstaxhq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/capitalgainstaxhq-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/capitalgainstaxhq-com/llms/capitalgainstaxhq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/capitalgainstaxhq-com-llms.txt
- group: build
  href: https://artifacts.apis.io/capitalgainstaxhq-com/mcp/capitalgainstaxhq-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/capitalgainstaxhq-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/capitalgainstaxhq-com/mcp/capitalgainstaxhq-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/capitalgainstaxhq-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/capitalgainstaxhq-com/well-known/capitalgainstaxhq-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/capitalgainstaxhq-com-security.txt
- group: agent
  href: https://artifacts.apis.io/capitalgainstaxhq-com/well-known/capitalgainstaxhq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/capitalgainstaxhq-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/capitalgainstaxhq-com/hosts/capitalgainstaxhq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capitalgainstaxhq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/capitalgainstaxhq-com/vendors/capitalgainstaxhq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capitalgainstaxhq-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capitalgainstaxhq.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capitalgainstaxhq.com/privacy/
- group: auth
  href: https://artifacts.apis.io/capitalgainstaxhq-com/authentication/capitalgainstaxhq-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/capitalgainstaxhq-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/capitalgainstaxhq-com/security/capitalgainstaxhq-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/capitalgainstaxhq-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/capitalgainstaxhq-com/security/capitalgainstaxhq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capitalgainstaxhq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capitalgainstaxhq.com/
created: '2026-11-04'
description: Capital Gains Tax HQ provides a calculator that quotes the IRS and six US taxing authorities word‑for‑word, publishing the source text and date for each capital gains question. The site aggregates official tax information, offering transparent, up‑to‑date guidance on capital gains across multiple states. It aims to help individuals understand tax liabilities with precise, sourced excerpts from government publications.
image: https://capitalgainstaxhq.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at capitalgainstaxhq.com requiring an API key.
  name: Capital Gains Tax HQ MCP Server
  slug: capitalgainstaxhq-com-mcp-yml
modified: '2026-11-04'
name: Capital Gains Tax HQ
nav: Providers
network: true
overview: 'Capital Gains Tax HQ publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Dataset API, Enquiry API, and MCP API. Tagged areas include Finance, Tax, Calculator, United States, and Capital Gains.


  The Capital Gains Tax HQ catalog on APIs.io includes 1 Spectral governance ruleset.


  Capital Gains Tax HQ''s developer surface includes authentication and 19 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Capital Gains Tax HQ API Rules
  rule_count: 53
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 6
  slug: capitalgainstaxhq-com-rules
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 17
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
  name: Capitalgainstaxhq Com Authentication
  slug: capitalgainstaxhq-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Capitalgainstaxhq Com Domain Security
  slug: capitalgainstaxhq-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Capitalgainstaxhq Com Vulnerability Disclosure
  slug: capitalgainstaxhq-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: capitalgainstaxhq-com-dataset-search
  slug: capitalgainstaxhq-com-dataset-search
- name: capitalgainstaxhq-com-enquiry-process
  slug: capitalgainstaxhq-com-enquiry-process
slug: capitalgainstaxhq-com
tags:
- Finance
- Tax
- Calculator
- United States
- Capital Gains
website: https://capitalgainstaxhq.com/
---
