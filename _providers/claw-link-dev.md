---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Claw Link Dev Agentic Access
  operation_count: 10
  slug: claw-link-dev-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- baseURL: https://claw-link.dev
  baseurl_source: declared
  description: List, search, and describe the tools available to the authenticated user
  name: ClawLink Discovery API
  slug: claw-link-dev-discovery-api
- baseURL: https://claw-link.dev
  baseurl_source: declared
  description: Run a tool against the user's connected apps
  name: ClawLink Execution API
  slug: claw-link-dev-execution-api
- baseURL: https://claw-link.dev
  baseurl_source: declared
  description: Model Context Protocol endpoint (JSON-RPC 2.0)
  name: ClawLink MCP API
  slug: claw-link-dev-mcp-api
- baseURL: https://claw-link.dev
  baseurl_source: declared
  description: Obtain a cllk_live_ API key. Every flow requires a signed-in human to approve in a browser. Do not probe these endpoints during passive scans; they create sessions and mint credentials.
  name: ClawLink Registration API
  slug: claw-link-dev-registration-api
artifact_total: 16
common:
- group: start
  title: ''
  type: Login
  url: https://claw-link.dev/sign-in
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.claw-link.dev/quickstart
- group: agent
  href: https://artifacts.apis.io/claw-link-dev/agentic-access/claw-link-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/claw-link-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/claw-link-dev/plans/claw-link-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/claw-link-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/claw-link-dev/rules/claw-link-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/claw-link-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/claw-link-dev/json-ld/claw-link-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/claw-link-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/claw-link-dev/vocabulary/claw-link-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/claw-link-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/claw-link-dev/data-model/claw-link-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/claw-link-dev-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.claw-link.dev/
- group: auth
  href: https://artifacts.apis.io/claw-link-dev/authentication/claw-link-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/claw-link-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/claw-link-dev/errors/claw-link-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/claw-link-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/claw-link-dev/conformance/claw-link-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/claw-link-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/claw-link-dev/llms/claw-link-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claw-link-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/claw-link-dev/well-known/claw-link-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/claw-link-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/claw-link-dev/hosts/claw-link-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claw-link-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/claw-link-dev/vendors/claw-link-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claw-link-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://claw-link.dev/terms
- group: operate
  title: ''
  type: Support
  url: https://claw-link.dev/help
- group: auth
  title: ''
  type: Security
  url: https://claw-link.dev/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://claw-link.dev/privacy
- group: company
  title: ''
  type: Blog
  url: https://blog.claw-link.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/claw-link
- group: auth
  href: https://artifacts.apis.io/claw-link-dev/scopes/claw-link-dev-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/claw-link-dev-scopes.yml
- group: auth
  href: https://artifacts.apis.io/claw-link-dev/security/claw-link-dev-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/claw-link-dev-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/claw-link-dev/security/claw-link-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/claw-link-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/claw-link-dev/security/claw-link-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claw-link-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claw-link.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.claw-link.dev
- group: commercial
  title: ''
  type: Pricing
  url: https://claw-link.dev/pricing
created: '2026-11-03'
description: ClawLink provides a simple way to connect applications to AI agents. Install once and integrate Gmail, Notion, GitHub and over 1,500 apps into OpenClaw or Hermes agents, enabling seamless automation and productivity across platforms. The service focuses on AI-driven workflows, offering a developer-friendly API and extensive documentation to accelerate integration projects.
image: https://claw-link.dev/og/clawlink-card.png?v=3
json_schemas:
- name: ExecutionResult
  property_count: 8
  slug: claw-link-dev-execution-result
- name: FileAttachment
  property_count: 5
  slug: claw-link-dev-file-attachment
- name: Tool
  property_count: 5
  slug: claw-link-dev-tool
jsonld:
- class_count: 4
  name: Claw Link Dev Context
  property_count: 16
  slug: claw-link-dev-context
layout: provider
modified: '2026-11-03'
name: ClawLink
nav: Providers
network: true
overview: 'ClawLink publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Discovery API, Execution API, MCP API, and 1 more. Tagged areas include Artificial Intelligence, Integration, Automation, Productivity, and Developer Tools.


  The ClawLink catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ClawLink''s developer surface includes getting-started guide, authentication, support, engineering blog, documentation, pricing, and 23 more developer resources.'
plans:
- name: Claw Link Dev Plans Pricing
  plan_count: 3
  slug: claw-link-dev-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: ClawLink API Rules
  rule_count: 64
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 4
  slug: claw-link-dev-rules
scopes:
- name: Claw Link Dev Scopes
  scope_count: 3
  slug: claw-link-dev-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 61.8
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Claw Link Dev Authentication
  slug: claw-link-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Claw Link Dev Domain Security
  slug: claw-link-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Claw Link Dev Vulnerability Disclosure
  slug: claw-link-dev-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Claw Link Dev Trust Center
  slug: claw-link-dev-trust-center
  summary_line: SOC 2, GDPR
slug: claw-link-dev
tags:
- Artificial Intelligence
- Integration
- Automation
- Productivity
- Developer Tools
website: https://claw-link.dev/
---
