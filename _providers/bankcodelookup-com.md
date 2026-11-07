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
- acting_count: 10
  human_in_the_loop: 0
  name: Bankcodelookup Com Agentic Access
  operation_count: 12
  slug: bankcodelookup-com-agentic-access
  summary_line: 12 operations · 10 acting
api_count: 1
apis:
- baseURL: https://bankcodelookup.com
  baseurl_source: declared
  description: dataset
  name: Bank Code Lookup Dataset API
  slug: bankcodelookup-com-dataset-api
- baseURL: https://bankcodelookup.com
  baseurl_source: declared
  description: enquiry
  name: Bank Code Lookup Enquiry API
  slug: bankcodelookup-com-enquiry-api
- baseURL: https://bankcodelookup.com
  baseurl_source: declared
  description: The mcp API from Bank Code Lookup — 1 operation(s) for mcp.
  name: Bank Code Lookup MCP API
  slug: bankcodelookup-com-mcp-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/bankcodelookup-com/agentic-access/bankcodelookup-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bankcodelookup-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bankcodelookup-com/rules/bankcodelookup-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bankcodelookup-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bankcodelookup-com/vocabulary/bankcodelookup-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bankcodelookup-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bankcodelookup-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://bankcodelookup.com/terms
- group: design
  href: https://artifacts.apis.io/bankcodelookup-com/errors/bankcodelookup-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bankcodelookup-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bankcodelookup-com/conformance/bankcodelookup-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bankcodelookup-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bankcodelookup-com/llms/bankcodelookup-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bankcodelookup-com-llms.txt
- group: build
  href: https://artifacts.apis.io/bankcodelookup-com/mcp/bankcodelookup-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bankcodelookup-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bankcodelookup-com/mcp/bankcodelookup-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bankcodelookup-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/bankcodelookup-com/well-known/bankcodelookup-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bankcodelookup-com-security.txt
- group: agent
  href: https://artifacts.apis.io/bankcodelookup-com/well-known/bankcodelookup-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bankcodelookup-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bankcodelookup-com/hosts/bankcodelookup-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bankcodelookup-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bankcodelookup-com/vendors/bankcodelookup-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bankcodelookup-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bankcodelookup-com/authentication/bankcodelookup-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bankcodelookup-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bankcodelookup-com/security/bankcodelookup-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bankcodelookup-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bankcodelookup-com/security/bankcodelookup-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bankcodelookup-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bankcodelookup.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://bankcodelookup.com/what-is-a-sort-code/
- group: operate
  title: ''
  type: Support
  url: https://bankcodelookup.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bankcodelookup.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bankcodelookup.com/privacy/
created: '2026-11-02'
description: Bank Code Lookup provides UK and US bank identifiers read directly from banks' own published pages. Covering 14 banks, it offers sort codes, SWIFT/BIC codes, IBAN formats and ABA routing numbers, each quoted verbatim with source and date. The service lets users look up codes, verify account numbers, and access detailed guides on bank identification.
image: https://bankcodelookup.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at bankcodelookup.com.
  name: Bank Code Lookup MCP Server
  slug: bankcodelookup-com-mcp-yml
modified: '2026-11-02'
name: Bank Code Lookup
nav: Providers
network: true
overview: 'Bank Code Lookup publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Dataset API, Enquiry API, and MCP API. Tagged areas include Banking, Finance, Lookup, and Codes.


  The Bank Code Lookup catalog on APIs.io includes 1 Spectral governance ruleset.


  Bank Code Lookup''s developer surface includes authentication, getting-started guide, support, and 19 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Bank Code Lookup API Rules
  rule_count: 53
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 6
  slug: bankcodelookup-com-rules
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 48.8
    developer_ergonomics: 26.7
    discoverability: 56.7
    operational_transparency: 5.3
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 21.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bankcodelookup Com Authentication
  slug: bankcodelookup-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bankcodelookup Com Domain Security
  slug: bankcodelookup-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Bankcodelookup Com Vulnerability Disclosure
  slug: bankcodelookup-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dataset-search
  slug: bankcodelookup-com-dataset-search-skill
slug: bankcodelookup-com
tags:
- Banking
- Finance
- Lookup
- Codes
website: https://bankcodelookup.com/
---
