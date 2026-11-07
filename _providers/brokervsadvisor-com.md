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
- acting_count: 7
  human_in_the_loop: 0
  name: Brokervsadvisor Com Agentic Access
  operation_count: 8
  slug: brokervsadvisor-com-agentic-access
  summary_line: 8 operations · 7 acting
api_count: 1
apis:
- baseURL: https://brokervsadvisor.com
  baseurl_source: declared
  description: enquiry
  name: Broker vs Advisor Enquiry API
  slug: brokervsadvisor-com-enquiry-api
- baseURL: https://brokervsadvisor.com
  baseurl_source: declared
  description: checker
  name: Broker vs Advisor Guide API
  slug: brokervsadvisor-com-guide-api
- baseURL: https://brokervsadvisor.com
  baseurl_source: declared
  description: The mcp API from Broker vs Advisor — 1 operation(s) for mcp.
  name: Broker vs Advisor MCP API
  slug: brokervsadvisor-com-mcp-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/brokervsadvisor-com/agentic-access/brokervsadvisor-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/brokervsadvisor-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/brokervsadvisor-com/rules/brokervsadvisor-com-rules.yml
  title: ''
  type: Spectral
  url: rules/brokervsadvisor-com-rules.yml
- group: design
  href: https://artifacts.apis.io/brokervsadvisor-com/vocabulary/brokervsadvisor-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/brokervsadvisor-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/brokervsadvisor-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://brokervsadvisor.com/terms
- group: design
  href: https://artifacts.apis.io/brokervsadvisor-com/errors/brokervsadvisor-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/brokervsadvisor-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/brokervsadvisor-com/conformance/brokervsadvisor-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brokervsadvisor-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brokervsadvisor-com/llms/brokervsadvisor-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brokervsadvisor-com-llms.txt
- group: build
  href: https://artifacts.apis.io/brokervsadvisor-com/mcp/brokervsadvisor-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/brokervsadvisor-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/brokervsadvisor-com/mcp/brokervsadvisor-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/brokervsadvisor-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/brokervsadvisor-com/well-known/brokervsadvisor-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/brokervsadvisor-com-security.txt
- group: agent
  href: https://artifacts.apis.io/brokervsadvisor-com/well-known/brokervsadvisor-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brokervsadvisor-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/brokervsadvisor-com/hosts/brokervsadvisor-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brokervsadvisor-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/brokervsadvisor-com/vendors/brokervsadvisor-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brokervsadvisor-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brokervsadvisor.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brokervsadvisor.com/privacy/
- group: auth
  href: https://artifacts.apis.io/brokervsadvisor-com/authentication/brokervsadvisor-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brokervsadvisor-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/brokervsadvisor-com/security/brokervsadvisor-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/brokervsadvisor-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/brokervsadvisor-com/security/brokervsadvisor-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brokervsadvisor-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brokervsadvisor.com/
- group: operate
  title: ''
  type: Contact
  url: https://brokervsadvisor.com/contact/
created: '2026-11-03'
description: Broker vs Advisor provides guidance on whether a business should use a broker or an M&A advisor to sell a business, explaining thresholds, asset vs stock sales, and regulatory considerations. The site offers FAQs, detailed comparisons, and contact information for professional advice, helping owners navigate the sale process and understand legal and financial implications.
image: https://brokervsadvisor.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at brokervsadvisor.com.
  name: Broker vs Advisor MCP Server
  slug: brokervsadvisor-com-mcp-yml
modified: '2026-11-03'
name: Broker vs Advisor
nav: Providers
network: true
overview: 'Broker vs Advisor publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Enquiry API, Guide API, and MCP API. Tagged areas include Business, Finance, Legal, Advisory, and M&A.


  The Broker vs Advisor catalog on APIs.io includes 1 Spectral governance ruleset.


  Broker vs Advisor''s developer surface includes authentication and 20 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Broker vs Advisor API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: brokervsadvisor-com-rules
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
  name: Brokervsadvisor Com Authentication
  slug: brokervsadvisor-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Brokervsadvisor Com Domain Security
  slug: brokervsadvisor-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Brokervsadvisor Com Vulnerability Disclosure
  slug: brokervsadvisor-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: enquiry
  slug: brokervsadvisor-com-enquiry-skill
slug: brokervsadvisor-com
tags:
- Business
- Finance
- Legal
- Advisory
- M&A
website: https://brokervsadvisor.com/
---
