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
- acting_count: 14
  human_in_the_loop: 0
  name: Citizenshipdescentchecker Com Agentic Access
  operation_count: 16
  slug: citizenshipdescentchecker-com-agentic-access
  summary_line: 16 operations · 14 acting
api_count: 1
apis:
- baseURL: https://citizenshipdescentchecker.com
  baseurl_source: declared
  description: enquiry
  name: Citizenship Descent Checker Enquiry API
  slug: citizenshipdescentchecker-com-enquiry-api
- baseURL: https://citizenshipdescentchecker.com
  baseurl_source: declared
  description: checker
  name: Citizenship Descent Checker Guide API
  slug: citizenshipdescentchecker-com-guide-api
- baseURL: https://citizenshipdescentchecker.com
  baseurl_source: declared
  description: The mcp API from Citizenship Descent Checker — 1 operation(s) for mcp.
  name: Citizenship Descent Checker MCP API
  slug: citizenshipdescentchecker-com-mcp-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/citizenshipdescentchecker-com/agentic-access/citizenshipdescentchecker-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/citizenshipdescentchecker-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/citizenshipdescentchecker-com/rules/citizenshipdescentchecker-com-rules.yml
  title: ''
  type: Spectral
  url: rules/citizenshipdescentchecker-com-rules.yml
- group: design
  href: https://artifacts.apis.io/citizenshipdescentchecker-com/vocabulary/citizenshipdescentchecker-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/citizenshipdescentchecker-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/citizenshipdescentchecker-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://citizenshipdescentchecker.com/terms
- group: design
  href: https://artifacts.apis.io/citizenshipdescentchecker-com/errors/citizenshipdescentchecker-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/citizenshipdescentchecker-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/citizenshipdescentchecker-com/conformance/citizenshipdescentchecker-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/citizenshipdescentchecker-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/citizenshipdescentchecker-com/llms/citizenshipdescentchecker-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/citizenshipdescentchecker-com-llms.txt
- group: build
  href: https://artifacts.apis.io/citizenshipdescentchecker-com/mcp/citizenshipdescentchecker-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/citizenshipdescentchecker-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/citizenshipdescentchecker-com/mcp/citizenshipdescentchecker-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/citizenshipdescentchecker-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/citizenshipdescentchecker-com/well-known/citizenshipdescentchecker-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/citizenshipdescentchecker-com-security.txt
- group: agent
  href: https://artifacts.apis.io/citizenshipdescentchecker-com/well-known/citizenshipdescentchecker-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/citizenshipdescentchecker-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/citizenshipdescentchecker-com/hosts/citizenshipdescentchecker-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citizenshipdescentchecker-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/citizenshipdescentchecker-com/vendors/citizenshipdescentchecker-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/citizenshipdescentchecker-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://citizenshipdescentchecker.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://citizenshipdescentchecker.com/privacy/
- group: auth
  href: https://artifacts.apis.io/citizenshipdescentchecker-com/authentication/citizenshipdescentchecker-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/citizenshipdescentchecker-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/citizenshipdescentchecker-com/security/citizenshipdescentchecker-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/citizenshipdescentchecker-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/citizenshipdescentchecker-com/security/citizenshipdescentchecker-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citizenshipdescentchecker-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citizenshipdescentchecker.com/
created: '2026-11-03'
description: Citizenship Descent Checker provides an online tool to determine eligibility for Canadian citizenship by descent under the updated Bill C-3, which removed the first‑generation limit as of 15 December 2025. The site offers detailed guides for Canada, Ireland, Italy, Germany and other jurisdictions, explaining residency requirements, documentation, costs and legal nuances. It also supplies FAQs, data sets and contact information for further assistance.
image: https://citizenshipdescentchecker.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at citizenshipdescentchecker.com.
  name: Citizenship Descent Checker MCP Server
  slug: citizenshipdescentchecker-com-mcp-yml
modified: '2026-11-03'
name: Citizenship Descent Checker
nav: Providers
network: true
overview: 'Citizenship Descent Checker publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Enquiry API, Guide API, and MCP API. Tagged areas include Citizenship, Descent, Canada, Immigration, and Guides.


  The Citizenship Descent Checker catalog on APIs.io includes 1 Spectral governance ruleset.


  Citizenship Descent Checker''s developer surface includes authentication and 19 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Citizenship Descent Checker API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: citizenshipdescentchecker-com-rules
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 18
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Citizenshipdescentchecker Com Authentication
  slug: citizenshipdescentchecker-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Citizenshipdescentchecker Com Domain Security
  slug: citizenshipdescentchecker-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Citizenshipdescentchecker Com Vulnerability Disclosure
  slug: citizenshipdescentchecker-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: citizenshipdescentchecker-com-enquiry-process
  slug: citizenshipdescentchecker-com-enquiry-process
- name: citizenshipdescentchecker-com-guide-checker-flow
  slug: citizenshipdescentchecker-com-guide-checker-flow
slug: citizenshipdescentchecker-com
tags:
- Citizenship
- Descent
- Canada
- Immigration
- Guides
website: https://citizenshipdescentchecker.com/
---
