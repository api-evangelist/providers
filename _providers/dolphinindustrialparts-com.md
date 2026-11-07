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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dolphinindustrialparts Com Agentic Access
  operation_count: 6
  slug: dolphinindustrialparts-com-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 1
apis:
- description: Read-only parts data. Compatible alternatives, not OEM parts. No prices.
  name: Dolphin Industrial Parts API
  slug: dolphin-industrial-parts-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/dolphinindustrialparts-com/agentic-access/dolphinindustrialparts-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dolphinindustrialparts-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dolphinindustrialparts-com/rules/dolphinindustrialparts-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dolphinindustrialparts-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/dolphinindustrialparts-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dolphinindustrialparts-com/errors/dolphinindustrialparts-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dolphinindustrialparts-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dolphinindustrialparts-com/conformance/dolphinindustrialparts-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dolphinindustrialparts-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dolphinindustrialparts-com/llms/dolphinindustrialparts-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dolphinindustrialparts-com-llms.txt
- group: build
  href: https://artifacts.apis.io/dolphinindustrialparts-com/mcp/dolphinindustrialparts-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dolphinindustrialparts-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dolphinindustrialparts-com/mcp/dolphinindustrialparts-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dolphinindustrialparts-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dolphinindustrialparts-com/well-known/dolphinindustrialparts-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dolphinindustrialparts-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dolphinindustrialparts-com/hosts/dolphinindustrialparts-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dolphinindustrialparts-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dolphinindustrialparts-com/vendors/dolphinindustrialparts-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dolphinindustrialparts-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dolphinindustrialparts.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dolphinindustrialparts.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/dolphinindustrialparts-com/security/dolphinindustrialparts-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dolphinindustrialparts-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dolphinindustrialparts.com/
created: '2026-11-05'
description: Dolphin Industrial Parts supplies EU‑made compatible spare parts for marine and industrial equipment, including pumps, fresh water generators, filters, UV sterilizers, heat exchangers, tank cleaning machines, and compressors. They quote in USD, ship from Michigan, and serve engineers in the United States, Canada, and Mexico. The company offers a broad catalog of non‑OEM parts sourced from leading manufacturers, providing alternatives for pumps, fresh water generators, self‑cleaning filters, UV sterilizers, re‑hardening filters, plate heat exchanger gaskets, and more.
image: https://dolphinindustrialparts.com/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at dolphinindustrialparts.com.
  name: Dolphin Industrial Parts MCP Server
  slug: dolphinindustrialparts-com-mcp-yml
modified: '2026-11-05'
name: Dolphin Industrial Parts
nav: Providers
network: true
overview: 'Dolphin Industrial Parts is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Marine, Industrial, Spare Parts, Engineering, and USA.


  The Dolphin Industrial Parts catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 69
  extends:
  - spectral:oas
  name: Dolphin Industrial Parts API Rules
  rule_count: 28
  severity_counts:
    error: 26
    hint: 0
    info: 1
    warn: 1
  slug: dolphinindustrialparts-com-rules
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 1.8
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dolphinindustrialparts Com Domain Security
  slug: dolphinindustrialparts-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: dolphinindustrialparts-com-browse-catalog
  slug: dolphinindustrialparts-com-browse-catalog
slug: dolphinindustrialparts-com
tags:
- Marine
- Industrial
- Spare Parts
- Engineering
- USA
website: https://dolphinindustrialparts.com/
---
