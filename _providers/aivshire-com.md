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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Aivshire Com Agentic Access
  operation_count: 7
  slug: aivshire-com-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 1
apis:
- baseURL: https://aivshire.com
  baseurl_source: declared
  description: calculator
  name: AI vs Hire Calculator API
  slug: aivshire-com-calculator-api
- baseURL: https://aivshire.com
  baseurl_source: declared
  description: enquiry
  name: AI vs Hire Enquiry API
  slug: aivshire-com-enquiry-api
- baseURL: https://aivshire.com
  baseurl_source: declared
  description: The mcp API from AI vs Hire — 1 operation(s) for mcp.
  name: AI vs Hire MCP API
  slug: aivshire-com-mcp-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/aivshire-com/agentic-access/aivshire-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aivshire-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aivshire-com/rules/aivshire-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aivshire-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aivshire-com/vocabulary/aivshire-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aivshire-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aivshire-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://aivshire.com/terms
- group: design
  href: https://artifacts.apis.io/aivshire-com/errors/aivshire-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aivshire-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aivshire-com/conformance/aivshire-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aivshire-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aivshire-com/llms/aivshire-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aivshire-com-llms.txt
- group: build
  href: https://artifacts.apis.io/aivshire-com/mcp/aivshire-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aivshire-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aivshire-com/mcp/aivshire-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aivshire-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aivshire-com/well-known/aivshire-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aivshire-com-security.txt
- group: agent
  href: https://artifacts.apis.io/aivshire-com/well-known/aivshire-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aivshire-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aivshire-com/hosts/aivshire-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aivshire-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aivshire-com/vendors/aivshire-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aivshire-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aivshire-com/authentication/aivshire-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aivshire-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aivshire-com/security/aivshire-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aivshire-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aivshire-com/security/aivshire-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aivshire-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aivshire.com/
- group: operate
  title: ''
  type: Support
  url: https://aivshire.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aivshire.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aivshire.com/terms/
- group: start
  title: ''
  type: GettingStarted
  url: https://aivshire.com/about/
created: '2026-11-01'
description: AI vs Hire compares the cost of AI tools versus human hiring, highlighting that salary comparisons alone are misleading. It explains that a hire incurs additional employer costs, equipment, recruitment, and management time, while AI tools add costs for data preparation, integration, and ongoing supervision. By evaluating both sides on the same basis, the site helps businesses decide when AI tools are truly cheaper and when human expertise is essential.
image: https://aivshire.com/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at aivshire.com.
  name: AI vs Hire MCP Server
  slug: aivshire-com-mcp-yml
modified: '2026-11-01'
name: AI vs Hire
nav: Providers
network: true
overview: 'AI vs Hire publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Calculator API, Enquiry API, and MCP API. Tagged areas include Artificial Intelligence, Hiring, Cost Comparison, Finance, and Automation.


  The AI vs Hire catalog on APIs.io includes 1 Spectral governance ruleset.


  AI vs Hire''s developer surface includes authentication, support, getting-started guide, and 19 more developer resources.'
plans:
- name: Aivshire Com Plans Pricing
  plan_count: 0
  slug: aivshire-com-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Aivshire Com Rate Limits
  slug: aivshire-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AI vs Hire API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: aivshire-com-rules
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 48.8
    developer_ergonomics: 26.7
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 35.9
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aivshire Com Authentication
  slug: aivshire-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aivshire Com Domain Security
  slug: aivshire-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aivshire Com Vulnerability Disclosure
  slug: aivshire-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: calculate
  slug: aivshire-com-calculate
- name: calculator-describe
  slug: aivshire-com-calculator-describe
- name: enquiry-describe
  slug: aivshire-com-enquiry-describe
- name: enquiry-fields
  slug: aivshire-com-enquiry-fields
- name: submit-enquiry
  slug: aivshire-com-submit-enquiry
slug: aivshire-com
tags:
- Artificial Intelligence
- Hiring
- Cost Comparison
- Finance
- Automation
website: https://aivshire.com/
---
