---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Attestvio API provides endpoints for compliance sheet data.
  name: Attestvio API
  slug: attestvio-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/attestvio-com/plans/attestvio-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/attestvio-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/attestvio-com/vocabulary/attestvio-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/attestvio-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/attestvio-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://attestvio.com/terms
- group: design
  href: https://artifacts.apis.io/attestvio-com/conformance/attestvio-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/attestvio-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/attestvio-com/llms/attestvio-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/attestvio-com-llms.txt
- group: build
  href: https://artifacts.apis.io/attestvio-com/mcp/attestvio-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/attestvio-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/attestvio-com/mcp/attestvio-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/attestvio-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/attestvio-com/well-known/attestvio-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/attestvio-com-security.txt
- group: auth
  href: https://artifacts.apis.io/attestvio-com/well-known/attestvio-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/attestvio-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/attestvio-com/well-known/attestvio-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/attestvio-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/attestvio-com/hosts/attestvio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/attestvio-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/attestvio-com/vendors/attestvio-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/attestvio-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/attestvio-com/security/attestvio-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/attestvio-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/attestvio-com/security/attestvio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/attestvio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://attestvio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://attestvio.com/tools/
- group: commercial
  title: ''
  type: Pricing
  url: https://attestvio.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://attestvio.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://attestvio.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://attestvio.com/support/
- group: start
  title: ''
  type: Login
  url: https://app.attestvio.com/?tab=account
created: '2026-10-29'
description: Free compliance sheets that work the obligations register, the audit scope, the evidence load, the risk analysis, the data map, the control tests, the incident log, the case backlog and the HR report from the compliance officer's own figures, with a paid plan that keeps every obligation, control, evidence item, incident, case and attestation against the record and exports it. Attestvio offers HR compliance consulting and a suite of compliance software tools for HIPAA, PCI, GDPR and other regulatory frameworks, helping organizations manage compliance documentation, audits, and reporting efficiently.
image: https://attestvio.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at attestvio.com.
  name: attestvio-com MCP Server
  slug: attestvio-com-mcp-yml
modified: '2026-10-29'
name: attestvio-com
nav: Providers
network: true
overview: 'attestvio-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HR, Compliance, SaaS, and Software.


  attestvio-com''s developer surface includes documentation, pricing, support, and 19 more developer resources.'
plans:
- name: Attestvio Com Plans Pricing
  plan_count: 2
  slug: attestvio-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Attestvio Com Rate Limits
  slug: attestvio-com-rate-limits
scopes:
- name: Attestvio Com Scopes
  scope_count: 0
  slug: attestvio-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 46.3
    catalog_earned_first_party: 8.0
    catalog_gap: 68.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 20.7
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Attestvio Com Authentication
  slug: attestvio-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Attestvio Com Domain Security
  slug: attestvio-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Attestvio Com Vulnerability Disclosure
  slug: attestvio-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dataset-tools
  slug: attestvio-com-dataset-tools
slug: attestvio-com
tags:
- Company
- HR
- Compliance
- SaaS
- Software
- API
website: https://attestvio.com/
---
