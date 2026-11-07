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
  name: Dataroompicker Com Agentic Access
  operation_count: 8
  slug: dataroompicker-com-agentic-access
  summary_line: 8 operations · 7 acting
api_count: 1
apis:
- baseURL: https://dataroompicker.com
  baseurl_source: declared
  description: enquiry
  name: Data Room Picker Enquiry API
  slug: dataroompicker-com-enquiry-api
- baseURL: https://dataroompicker.com
  baseurl_source: declared
  description: compare
  name: Data Room Picker Guide API
  slug: dataroompicker-com-guide-api
- baseURL: https://dataroompicker.com
  baseurl_source: declared
  description: The mcp API from Data Room Picker — 1 operation(s) for mcp.
  name: Data Room Picker MCP API
  slug: dataroompicker-com-mcp-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/dataroompicker-com/agentic-access/dataroompicker-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dataroompicker-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dataroompicker-com/rules/dataroompicker-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dataroompicker-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dataroompicker-com/vocabulary/dataroompicker-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dataroompicker-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dataroompicker-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://dataroompicker.com/terms
- group: design
  href: https://artifacts.apis.io/dataroompicker-com/errors/dataroompicker-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dataroompicker-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dataroompicker-com/conformance/dataroompicker-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dataroompicker-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dataroompicker-com/llms/dataroompicker-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dataroompicker-com-llms.txt
- group: build
  href: https://artifacts.apis.io/dataroompicker-com/mcp/dataroompicker-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dataroompicker-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dataroompicker-com/mcp/dataroompicker-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dataroompicker-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/dataroompicker-com/well-known/dataroompicker-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dataroompicker-com-security.txt
- group: agent
  href: https://artifacts.apis.io/dataroompicker-com/well-known/dataroompicker-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dataroompicker-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dataroompicker-com/hosts/dataroompicker-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dataroompicker-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dataroompicker-com/vendors/dataroompicker-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dataroompicker-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dataroompicker.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dataroompicker.com/privacy/
- group: auth
  href: https://artifacts.apis.io/dataroompicker-com/authentication/dataroompicker-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dataroompicker-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dataroompicker-com/security/dataroompicker-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dataroompicker-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dataroompicker-com/security/dataroompicker-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataroompicker-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dataroompicker.com/
created: '2026-11-05'
description: Data Room Picker provides a curated comparison and pricing analysis of virtual data room software vendors. It aggregates pricing models, billing units, and feature details across providers, offering insights into cost structures such as flat monthly fees, data volume pricing, and deal‑based pricing. The site also includes FAQs, a pricing guide, and links to vendor resources, helping users understand and compare data room solutions for M&A due diligence and other secure document sharing needs.
image: https://dataroompicker.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at dataroompicker.com requiring an API key.
  name: Data Room Picker MCP Server
  slug: dataroompicker-com-mcp-yml
modified: '2026-11-05'
name: Data Room Picker
nav: Providers
network: true
overview: 'Data Room Picker publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Enquiry API, Guide API, and MCP API. Tagged areas include Data, Pricing, Virtual Data Room, Comparison, and M&A.


  The Data Room Picker catalog on APIs.io includes 1 Spectral governance ruleset.


  Data Room Picker''s developer surface includes authentication and 19 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Data Room Picker API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: dataroompicker-com-rules
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 48.8
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
      total: 3
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
  name: Dataroompicker Com Authentication
  slug: dataroompicker-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dataroompicker Com Domain Security
  slug: dataroompicker-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dataroompicker Com Vulnerability Disclosure
  slug: dataroompicker-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dataroompicker-com-enquiry-workflow
  slug: dataroompicker-com-enquiry-workflow
slug: dataroompicker-com
tags:
- Data
- Pricing
- Virtual Data Room
- Comparison
- M&A
website: https://dataroompicker.com/
---
