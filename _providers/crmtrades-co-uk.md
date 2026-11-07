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
- acting_count: 4
  human_in_the_loop: 0
  name: Crmtrades Co Uk Agentic Access
  operation_count: 5
  slug: crmtrades-co-uk-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- baseURL: https://crmtrades.co.uk
  baseurl_source: declared
  description: enquiry
  name: CRM for Trades Enquiry API
  slug: crmtrades-co-uk-enquiry-api
- baseURL: https://crmtrades.co.uk
  baseurl_source: declared
  description: The mcp API from CRM for Trades — 1 operation(s) for mcp.
  name: CRM for Trades MCP API
  slug: crmtrades-co-uk-mcp-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/crmtrades-co-uk/agentic-access/crmtrades-co-uk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crmtrades-co-uk-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/crmtrades-co-uk/rules/crmtrades-co-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/crmtrades-co-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/crmtrades-co-uk/vocabulary/crmtrades-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crmtrades-co-uk-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/crmtrades-co-uk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://crmtrades.co.uk/terms
- group: design
  href: https://artifacts.apis.io/crmtrades-co-uk/errors/crmtrades-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crmtrades-co-uk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/crmtrades-co-uk/conformance/crmtrades-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crmtrades-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crmtrades-co-uk/llms/crmtrades-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crmtrades-co-uk-llms.txt
- group: build
  href: https://artifacts.apis.io/crmtrades-co-uk/mcp/crmtrades-co-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/crmtrades-co-uk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/crmtrades-co-uk/mcp/crmtrades-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crmtrades-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/crmtrades-co-uk/well-known/crmtrades-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crmtrades-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/crmtrades-co-uk/well-known/crmtrades-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crmtrades-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/crmtrades-co-uk/hosts/crmtrades-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crmtrades-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/crmtrades-co-uk/vendors/crmtrades-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crmtrades-co-uk-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crmtrades.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crmtrades.co.uk/privacy/
- group: auth
  href: https://artifacts.apis.io/crmtrades-co-uk/authentication/crmtrades-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crmtrades-co-uk-authentication.yml
- group: auth
  href: https://artifacts.apis.io/crmtrades-co-uk/security/crmtrades-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/crmtrades-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/crmtrades-co-uk/security/crmtrades-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crmtrades-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crmtrades.co.uk/
created: '2026-11-04'
description: CRM for Trades provides a managed CRM and job management system tailored for trades businesses in the UK. They select a suitable job management platform, set up quoting, scheduling, reminders, and invoicing for a fixed price, handling configuration, training, and ongoing support. The service aims to streamline operations for sole traders and larger firms, offering flexible pricing and comprehensive setup to get businesses running quickly.
image: https://crmtrades.co.uk/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at crmtrades.co.uk.
  name: CRM for Trades MCP Server
  slug: crmtrades-co-uk-mcp-yml
modified: '2026-11-04'
name: CRM for Trades
nav: Providers
network: true
overview: 'CRM for Trades publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Enquiry API and MCP API. Tagged areas include CRM, Trade Software, Job Management, Quotes, and Scheduling.


  The CRM for Trades catalog on APIs.io includes 1 Spectral governance ruleset.


  CRM for Trades'' developer surface includes authentication and 19 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: CRM for Trades API Rules
  rule_count: 48
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 1
  slug: crmtrades-co-uk-rules
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 47.4
    developer_ergonomics: 13.7
    discoverability: 65.0
    operational_transparency: 10.5
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
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Crmtrades Co Uk Authentication
  slug: crmtrades-co-uk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Crmtrades Co Uk Domain Security
  slug: crmtrades-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Crmtrades Co Uk Vulnerability Disclosure
  slug: crmtrades-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: crmtrades-co-uk-enquiry-process
  slug: crmtrades-co-uk-enquiry-process
slug: crmtrades-co-uk
tags:
- CRM
- Trade Software
- Job Management
- Quotes
- Scheduling
website: https://crmtrades.co.uk/
---
