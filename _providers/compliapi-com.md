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
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 56.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Compliapi Com Agentic Access
  operation_count: 8
  slug: compliapi-com-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- baseURL: https://api.compliapi.com/api/v1
  baseurl_source: declared
  description: The screen API from compliapi-com — 8 operation(s) for screen.
  name: compliapi-com Screen API
  slug: compliapi-com-screen-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/compliapi-com/data-model/compliapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/compliapi-com-data-model.yml
- group: start
  title: ''
  type: Login
  url: https://app.compliapi.com/account/login
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.compliapi.com/quickstart
- group: agent
  href: https://artifacts.apis.io/compliapi-com/agentic-access/compliapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/compliapi-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/compliapi-com/rules/compliapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/compliapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/compliapi-com/vocabulary/compliapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/compliapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/compliapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/compliapi-com/conventions/compliapi-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/compliapi-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://compliapi.com/trust
- group: auth
  title: ''
  type: Security
  url: https://compliapi.com/trust
- group: auth
  href: https://artifacts.apis.io/compliapi-com/authentication/compliapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/compliapi-com-authentication.yml
- group: operate
  href: https://artifacts.apis.io/compliapi-com/lifecycle/compliapi-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/compliapi-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/compliapi-com/lifecycle/compliapi-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/compliapi-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/compliapi-com/errors/compliapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/compliapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/compliapi-com/conformance/compliapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/compliapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/compliapi-com/llms/compliapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/compliapi-com-llms.txt
- group: other
  href: https://artifacts.apis.io/compliapi-com/a2a/compliapi-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/compliapi-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/compliapi-com/mcp/compliapi-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/compliapi-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/compliapi-com/mcp/compliapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/compliapi-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/compliapi-com/well-known/compliapi-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/compliapi-com-security.txt
- group: agent
  href: https://artifacts.apis.io/compliapi-com/well-known/compliapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/compliapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/compliapi-com/hosts/compliapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/compliapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/compliapi-com/vendors/compliapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/compliapi-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://compliapi.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://compliapi.com/legal/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://compliapi.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://compliapi.com/blog
- group: auth
  href: https://artifacts.apis.io/compliapi-com/security/compliapi-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/compliapi-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/compliapi-com/security/compliapi-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/compliapi-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/compliapi-com/security/compliapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/compliapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://compliapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://compliapi.com/openapi.json
- group: docs
  title: ''
  type: APIReference
  url: https://compliapi.com/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://compliapi.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Compli-API
- group: commercial
  title: ''
  type: Pricing
  url: https://compliapi.com/pricing
created: '2026-10-30'
description: CompliAPI provides a real‑time sanctions screening API that lets developers screen cryptocurrency addresses, email addresses, website URLs, government identification numbers and country codes against the U.S. Treasury OFAC SDN list and over ten additional global sanctions, crime and risk lists. The service also includes VPN detection and IP geolocation to help prevent evasion. All checks are performed via a single GET request with an API key, delivering fast, reliable compliance data for fintech, crypto, and other regulated applications.
image: https://compliapi.com/compliapi-logo-dark.svg
json_schemas:
- name: ListEntitiesResponse
  property_count: 0
  slug: compliapi-com-list-entities-response
- name: ListInfo
  property_count: 0
  slug: compliapi-com-list-info
- name: PepScreenResponse
  property_count: 0
  slug: compliapi-com-pep-screen-response
- name: ScreenResponse
  property_count: 0
  slug: compliapi-com-screen-response
layout: provider
mcp_servers:
- description: Remote MCP server at api.compliapi.com.
  name: compliapi-com MCP Server
  slug: compliapi-com-mcp-yml
modified: '2026-10-30'
name: compliapi-com
nav: Providers
network: true
overview: 'compliapi-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Screen API. Tagged areas include Compliance, Sanctions, Screening, Fintech, and Cryptocurrency.


  The compliapi-com catalog on APIs.io includes 1 Spectral governance ruleset.


  compliapi-com''s developer surface includes getting-started guide, authentication, changelog, engineering blog, documentation, API reference, support, and 29 more developer resources.'
random_paper: 2
rate_limits:
- limit_count: 0
  name: Compliapi Com Rate Limits
  slug: compliapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: compliapi-com API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: compliapi-com-rules
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.8
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 52.0
    developer_ergonomics: 36.2
    discoverability: 65.0
    operational_transparency: 23.7
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/compliapi-com/compliapi-com-2026-11-03T125014.png
security:
- kind: authentication
  name: Compliapi Com Authentication
  slug: compliapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Compliapi Com Domain Security
  slug: compliapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Compliapi Com Vulnerability Disclosure
  slug: compliapi-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Compliapi Com Trust Center
  slug: compliapi-com-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 1
skills:
- name: compliapi-screening
  slug: compliapi-com-screening
slug: compliapi-com
tags:
- Compliance
- Sanctions
- Screening
- Fintech
- Cryptocurrency
website: https://compliapi.com/
---
