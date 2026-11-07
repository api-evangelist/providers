---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
  score: 25.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AI Implementation Cost API provides calculator and enquiry tools for estimating AI project costs.
  name: AI Implementation Cost API
  slug: ai-implementation-cost-api
- baseURL: https://aiimplementationcost.com
  baseurl_source: declared
  description: 'AI Implementation Cost (https://aiimplementationcost.com/): the site''s own MCP server, served from its domain. How much it costs to implement AI depends on data work and change, not licences. Model th'
  name: AI Implementation Cost API API
  slug: ai-implementation-cost-api-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/aiimplementationcost-com/rules/aiimplementationcost-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aiimplementationcost-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aiimplementationcost-com/vocabulary/aiimplementationcost-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aiimplementationcost-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aiimplementationcost-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://aiimplementationcost.com/terms
- group: design
  href: https://artifacts.apis.io/aiimplementationcost-com/errors/aiimplementationcost-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aiimplementationcost-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aiimplementationcost-com/conformance/aiimplementationcost-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiimplementationcost-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aiimplementationcost-com/llms/aiimplementationcost-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiimplementationcost-com-llms.txt
- group: build
  href: https://artifacts.apis.io/aiimplementationcost-com/mcp/aiimplementationcost-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aiimplementationcost-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aiimplementationcost-com/mcp/aiimplementationcost-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aiimplementationcost-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aiimplementationcost-com/well-known/aiimplementationcost-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aiimplementationcost-com-security.txt
- group: agent
  href: https://artifacts.apis.io/aiimplementationcost-com/well-known/aiimplementationcost-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aiimplementationcost-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aiimplementationcost-com/hosts/aiimplementationcost-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiimplementationcost-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiimplementationcost-com/vendors/aiimplementationcost-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiimplementationcost-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiimplementationcost.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiimplementationcost.com/privacy/
- group: auth
  href: https://artifacts.apis.io/aiimplementationcost-com/security/aiimplementationcost-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aiimplementationcost-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aiimplementationcost-com/security/aiimplementationcost-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiimplementationcost-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiimplementationcost.com/
created: '2026-11-01'
description: AIImplementationCost provides an informational site that helps businesses estimate the total cost of implementing AI projects. It offers a calculator that breaks down costs into licence fees, data preparation, integration, and change management, along with guides, data tables, and sources for figures. The site emphasizes measuring AI return, scoping first projects, and offers contact for enquiries. It is not affiliated with any vendor or agency and does not provide legal or financial advice.
image: https://aiimplementationcost.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at aiimplementationcost.com.
  name: AIImplementationCost MCP Server
  slug: aiimplementationcost-com-mcp-yml
modified: '2026-11-01'
name: AIImplementationCost
nav: Providers
network: true
overview: 'AIImplementationCost publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI Implementation Cost API API, and 1 more. Tagged areas include Artificial Intelligence, Cost, Implementation, Business, and Calculator.


  The AIImplementationCost catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AIImplementationCost API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: aiimplementationcost-com-rules
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 48.4
    developer_ergonomics: 1.8
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 28.3
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiimplementationcost Com Domain Security
  slug: aiimplementationcost-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aiimplementationcost Com Vulnerability Disclosure
  slug: aiimplementationcost-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: calculator
  slug: aiimplementationcost-com-calculator
slug: aiimplementationcost-com
tags:
- Artificial Intelligence
- Cost
- Implementation
- Business
- Calculator
website: https://aiimplementationcost.com/
---
