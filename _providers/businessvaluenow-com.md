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
- acting_count: 7
  human_in_the_loop: 0
  name: Businessvaluenow Com Agentic Access
  operation_count: 8
  slug: businessvaluenow-com-agentic-access
  summary_line: 8 operations · 7 acting
api_count: 1
apis:
- baseURL: https://businessvaluenow.com
  baseurl_source: declared
  description: enquiry
  name: Business Value Now Enquiry API
  slug: businessvaluenow-com-enquiry-api
- baseURL: https://businessvaluenow.com
  baseurl_source: declared
  description: checker
  name: Business Value Now Guide API
  slug: businessvaluenow-com-guide-api
- baseURL: https://businessvaluenow.com
  baseurl_source: declared
  description: The mcp API from Business Value Now — 1 operation(s) for mcp.
  name: Business Value Now MCP API
  slug: businessvaluenow-com-mcp-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/businessvaluenow-com/agentic-access/businessvaluenow-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/businessvaluenow-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/businessvaluenow-com/rules/businessvaluenow-com-rules.yml
  title: ''
  type: Spectral
  url: rules/businessvaluenow-com-rules.yml
- group: design
  href: https://artifacts.apis.io/businessvaluenow-com/vocabulary/businessvaluenow-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/businessvaluenow-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/businessvaluenow-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://businessvaluenow.com/terms
- group: design
  href: https://artifacts.apis.io/businessvaluenow-com/errors/businessvaluenow-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/businessvaluenow-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/businessvaluenow-com/conformance/businessvaluenow-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/businessvaluenow-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/businessvaluenow-com/llms/businessvaluenow-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/businessvaluenow-com-llms.txt
- group: build
  href: https://artifacts.apis.io/businessvaluenow-com/mcp/businessvaluenow-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/businessvaluenow-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/businessvaluenow-com/mcp/businessvaluenow-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/businessvaluenow-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/businessvaluenow-com/well-known/businessvaluenow-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/businessvaluenow-com-security.txt
- group: agent
  href: https://artifacts.apis.io/businessvaluenow-com/well-known/businessvaluenow-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/businessvaluenow-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/businessvaluenow-com/hosts/businessvaluenow-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/businessvaluenow-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/businessvaluenow-com/vendors/businessvaluenow-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/businessvaluenow-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://businessvaluenow.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://businessvaluenow.com/privacy/
- group: auth
  href: https://artifacts.apis.io/businessvaluenow-com/authentication/businessvaluenow-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/businessvaluenow-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/businessvaluenow-com/security/businessvaluenow-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/businessvaluenow-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/businessvaluenow-com/security/businessvaluenow-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/businessvaluenow-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://businessvaluenow.com/
created: '2026-11-03'
description: Business Value Now provides educational content and tools to help entrepreneurs and investors understand how to value a business. It covers asset‑based, market and income approaches, explains key concepts like EBITDA, SDE, and offers practical guidance on valuation methods, financial statements, and deal structuring. The site includes FAQs, detailed articles, and free resources aimed at simplifying business valuation for a broad audience.
image: https://businessvaluenow.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at businessvaluenow.com.
  name: Business Value Now MCP Server
  slug: businessvaluenow-com-mcp-yml
modified: '2026-11-03'
name: Business Value Now
nav: Providers
network: true
overview: 'Business Value Now publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Enquiry API, Guide API, and MCP API. Tagged areas include Business Valuation, Finance, Education, Entrepreneurship, and Small Business.


  The Business Value Now catalog on APIs.io includes 1 Spectral governance ruleset.


  Business Value Now''s developer surface includes authentication and 19 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Business Value Now API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: businessvaluenow-com-rules
score:
  band: thin
  composite: 29.0
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
    developer_ergonomics: 18.3
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
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Businessvaluenow Com Authentication
  slug: businessvaluenow-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Businessvaluenow Com Domain Security
  slug: businessvaluenow-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Businessvaluenow Com Vulnerability Disclosure
  slug: businessvaluenow-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: enquiry
  slug: businessvaluenow-com-enquiry
slug: businessvaluenow-com
tags:
- Business Valuation
- Finance
- Education
- Entrepreneurship
- Small Business
website: https://businessvaluenow.com/
---
