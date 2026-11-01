---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://gateway.ansvar.eu
  baseurl_source: declared
  description: 'ansvar-eu API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: ansvar-eu API
  slug: ansvar-eu-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/ansvar-eu/rules/ansvar-eu-rules.yml
  title: ''
  type: Spectral
  url: rules/ansvar-eu-rules.yml
- group: design
  href: https://artifacts.apis.io/ansvar-eu/json-ld/ansvar-eu-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ansvar-eu-context.jsonld
- group: design
  href: https://artifacts.apis.io/ansvar-eu/vocabulary/ansvar-eu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ansvar-eu-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ansvar-eu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ansvar-eu/data-model/ansvar-eu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ansvar-eu-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://ansvar.eu/trust
- group: auth
  title: ''
  type: Security
  url: https://ansvar.eu/trust#disclosure
- group: design
  href: https://artifacts.apis.io/ansvar-eu/conformance/ansvar-eu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ansvar-eu-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ansvar-eu/llms/ansvar-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ansvar-eu-llms.txt
- group: agent
  href: https://artifacts.apis.io/ansvar-eu/mcp/ansvar-eu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ansvar-eu-mcp.yml
- group: auth
  href: https://artifacts.apis.io/ansvar-eu/well-known/ansvar-eu-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ansvar-eu-security.txt
- group: auth
  href: https://artifacts.apis.io/ansvar-eu/well-known/ansvar-eu-gateway-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ansvar-eu-gateway-security.txt
- group: auth
  href: https://artifacts.apis.io/ansvar-eu/well-known/ansvar-eu-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ansvar-eu-app-security.txt
- group: agent
  href: https://artifacts.apis.io/ansvar-eu/well-known/ansvar-eu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ansvar-eu-well-known.yml
- group: other
  href: https://artifacts.apis.io/ansvar-eu/hosts/ansvar-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ansvar-eu-hosts.yml
- group: other
  href: https://artifacts.apis.io/ansvar-eu/vendors/ansvar-eu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ansvar-eu-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://ansvar.eu/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://ansvar.eu/docs/reference/tools
- group: auth
  href: https://artifacts.apis.io/ansvar-eu/security/ansvar-eu-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ansvar-eu-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/ansvar-eu/security/ansvar-eu-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ansvar-eu-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ansvar-eu/security/ansvar-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ansvar-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ansvar.eu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ansvar.eu/developers
- group: docs
  title: ''
  type: Documentation
  url: https://ansvar.eu/docs/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://ansvar.eu/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://ansvar.eu/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ansvar
- group: commercial
  title: ''
  type: Pricing
  url: https://ansvar.eu/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.ansvar.eu/account?intent=signup
- group: start
  title: ''
  type: Login
  url: https://app.ansvar.eu/account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ansvar.eu/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ansvar.eu/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://gateway.ansvar.eu/mcp
  - status: 200
    url: https://ansvar.eu/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Ansvar provides an AI‑powered compliance and legal intelligence platform that surfaces findings backed by law, standards, and security sources. Users can run gap analyses, DPIAs, and threat models directly against regulations such as NIS2, GDPR, and industry standards. The service runs in an EU‑hosted cloud or can be deployed on‑premises as a design partner, offering free tier access with one assessment per month. It integrates with major AI models like Claude, ChatGPT, and Copilot, and supplies detailed source citations for each claim.
image: https://ansvar.eu/ansvar-logo.svg
json_schemas:
- name: PostMcpRequest
  property_count: 3
  slug: ansvar-eu-post-mcp-request
jsonld:
- class_count: 1
  name: Ansvar Eu Context
  property_count: 3
  slug: ansvar-eu-context
layout: provider
mcp_servers:
- description: Remote MCP server at gateway.ansvar.eu.
  name: ansvar-eu MCP Server
  slug: ansvar-eu-mcp-yml
modified: '2026-10-29'
name: ansvar-eu
nav: Providers
network: true
overview: 'ansvar-eu is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Compliance, Legal, and Security.


  The ansvar-eu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ansvar-eu''s developer surface includes changelog, API reference, documentation, getting-started guide, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Ansvar Eu Plans Pricing
  plan_count: 0
  slug: ansvar-eu-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Ansvar Eu Rate Limits
  slug: ansvar-eu-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: ansvar-eu API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: ansvar-eu-rules
scopes:
- name: Ansvar Eu Scopes
  scope_count: 0
  slug: ansvar-eu-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 53.2
    catalog_earned_first_party: 0.0
    catalog_gap: 61.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 19.0
    developer_ergonomics: 46.9
    discoverability: 65.0
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ansvar Eu Authentication
  slug: ansvar-eu-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ansvar Eu Domain Security
  slug: ansvar-eu-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ansvar Eu Vulnerability Disclosure
  slug: ansvar-eu-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ansvar Eu Trust Center
  slug: ansvar-eu-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 2
skills:
- name: mcp
  slug: ansvar-eu-mcp
- name: token
  slug: ansvar-eu-token
slug: ansvar-eu
tags:
- Company
- AI
- Compliance
- Legal
- Security
- Data
website: https://ansvar.eu/
---
