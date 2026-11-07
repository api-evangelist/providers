---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Imejis Io Agentic Access
  operation_count: 13
  slug: imejis-io-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.imejis.io
  baseurl_source: declared
  description: Render usage.
  name: imejis-io Analytics API
  slug: imejis-io-analytics-api
- baseURL: https://api.imejis.io
  baseurl_source: declared
  description: Read and list designs.
  name: imejis-io Designs API
  slug: imejis-io-designs-api
- baseURL: https://api.imejis.io
  baseurl_source: declared
  description: Render API keys.
  name: imejis-io Keys API
  slug: imejis-io-keys-api
- baseURL: https://api.imejis.io
  baseurl_source: declared
  description: Turn a design into a finished image.
  name: imejis-io Render API
  slug: imejis-io-render-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/imejis-io/agentic-access/imejis-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/imejis-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/imejis-io/plans/imejis-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/imejis-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/imejis-io/rules/imejis-io-rules.yml
  title: ''
  type: Spectral
  url: rules/imejis-io-rules.yml
- group: design
  href: https://artifacts.apis.io/imejis-io/json-ld/imejis-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/imejis-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/imejis-io/vocabulary/imejis-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/imejis-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/imejis-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/imejis-io/data-model/imejis-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/imejis-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/imejis-io/components/imejis-io-components.yml
  title: ''
  type: Components
  url: components/imejis-io-components.yml
- group: operate
  href: https://artifacts.apis.io/imejis-io/changelog/imejis-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/imejis-io-changelog.yml
- group: auth
  href: https://artifacts.apis.io/imejis-io/authentication/imejis-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/imejis-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/imejis-io/errors/imejis-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/imejis-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/imejis-io/conformance/imejis-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/imejis-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/imejis-io/llms/imejis-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/imejis-io-llms.txt
- group: other
  href: https://artifacts.apis.io/imejis-io/a2a/imejis-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/imejis-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/imejis-io/mcp/imejis-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/imejis-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/imejis-io/well-known/imejis-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/imejis-io-security.txt
- group: auth
  href: https://artifacts.apis.io/imejis-io/well-known/imejis-io-imejis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/imejis-io-imejis-security.txt
- group: auth
  href: https://artifacts.apis.io/imejis-io/well-known/imejis-io-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/imejis-io-api-security.txt
- group: agent
  href: https://artifacts.apis.io/imejis-io/well-known/imejis-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/imejis-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/imejis-io/hosts/imejis-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/imejis-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/imejis-io/vendors/imejis-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/imejis-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.imejis.io/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.imejis.io/help
- group: auth
  title: ''
  type: Security
  url: https://www.imejis.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.imejis.io/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.imejis.io/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/imejis
- group: auth
  href: https://artifacts.apis.io/imejis-io/security/imejis-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/imejis-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/imejis-io/security/imejis-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/imejis-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://imejis.io/
created: '2026-10-30'
description: 'imejis-io is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://www.imejis.io/og.png
json_schemas:
- name: ApiKey
  property_count: 3
  slug: imejis-io-api-key
- name: Design
  property_count: 3
  slug: imejis-io-design
- name: PaginatedDesigns
  property_count: 4
  slug: imejis-io-paginated-designs
- name: RenderConfig
  property_count: 3
  slug: imejis-io-render-config
jsonld:
- class_count: 6
  name: Imejis Io Context
  property_count: 14
  slug: imejis-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.imejis.io.
  name: imejis-io MCP Server
  slug: imejis-io-mcp-yml
modified: '2026-10-30'
name: imejis-io
nav: Providers
network: true
overview: 'imejis-io publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Designs API, Keys API, and 1 more. Tagged areas include Company.


  The imejis-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  imejis-io''s developer surface includes changelog, authentication, support, pricing, and 26 more developer resources.'
plans:
- name: Imejis Io Plans Pricing
  plan_count: 4
  slug: imejis-io-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Imejis Io Rate Limits
  slug: imejis-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: imejis-io API Rules
  rule_count: 18
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 2
  slug: imejis-io-rules
scopes:
- name: Imejis Io Scopes
  scope_count: 0
  slug: imejis-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 32
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 62.7
    developer_ergonomics: 20.7
    discoverability: 48.3
    operational_transparency: 23.7
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/imejis-io/imejis-io-2026-11-03T133704.png
security:
- kind: authentication
  name: Imejis Io Authentication
  slug: imejis-io-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Imejis Io Domain Security
  slug: imejis-io-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Imejis Io Vulnerability Disclosure
  slug: imejis-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: imejis-io
tags:
- Company
website: https://imejis.io/
---
