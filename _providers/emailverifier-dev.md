---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Emailverifier Dev Agentic Access
  operation_count: 3
  slug: emailverifier-dev-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://emailverifier.dev
  baseurl_source: declared
  description: Classify email domains.
  name: emailverifier-dev Domains API
  slug: emailverifier-dev-domains-api
- baseURL: https://emailverifier.dev
  baseurl_source: declared
  description: Monitor project credit usage.
  name: emailverifier-dev Usage API
  slug: emailverifier-dev-usage-api
- baseURL: https://emailverifier.dev
  baseurl_source: declared
  description: Verify complete email addresses.
  name: emailverifier-dev Verification API
  slug: emailverifier-dev-verification-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/emailverifier-dev/agentic-access/emailverifier-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/emailverifier-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/emailverifier-dev/plans/emailverifier-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/emailverifier-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/emailverifier-dev/rules/emailverifier-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/emailverifier-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/emailverifier-dev/json-ld/emailverifier-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/emailverifier-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/emailverifier-dev/vocabulary/emailverifier-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/emailverifier-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/emailverifier-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/emailverifier-dev/data-model/emailverifier-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/emailverifier-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/emailverifier-dev/authentication/emailverifier-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/emailverifier-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/emailverifier-dev/errors/emailverifier-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/emailverifier-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/emailverifier-dev/conformance/emailverifier-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/emailverifier-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/emailverifier-dev/llms/emailverifier-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/emailverifier-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/emailverifier-dev/mcp/emailverifier-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/emailverifier-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/emailverifier-dev/mcp/emailverifier-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/emailverifier-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/emailverifier-dev/well-known/emailverifier-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/emailverifier-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/emailverifier-dev/hosts/emailverifier-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/emailverifier-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/emailverifier-dev/vendors/emailverifier-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/emailverifier-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/emailverifier-dev/packages/emailverifier-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/emailverifier-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/emailverifier-dev/packages/emailverifier-dev-packages.yml
  title: ''
  type: Packages
  url: packages/emailverifier-dev-packages.yml
- group: auth
  href: https://artifacts.apis.io/emailverifier-dev/security/emailverifier-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/emailverifier-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://emailverifier.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://emailverifier.dev/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://emailverifier.dev/docs/api
- group: operate
  title: ''
  type: Support
  url: https://emailverifier.dev/contact
- group: company
  title: ''
  type: Blog
  url: https://emailverifier.dev/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://emailverifier.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://emailverifier.dev/register
- group: start
  title: ''
  type: Login
  url: https://emailverifier.dev/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emailverifier.dev/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emailverifier.dev/legal/privacy
created: '2026-10-30'
description: emailverifier.dev provides a real‑time email verification API that helps developers detect invalid, disposable, or mistyped email addresses at signup, login, or any point of contact collection. The service returns structured risk signals, mailbox existence, and actionable recommendations, with a free tier of 1,000 checks and transparent pricing for higher volumes.
image: https://emailverifier.dev/brand/logo-light.svg
json_schemas:
- name: DomainClassification
  property_count: 4
  slug: emailverifier-dev-domain-classification
- name: UsageSummary
  property_count: 4
  slug: emailverifier-dev-usage-summary
- name: VerificationResult
  property_count: 6
  slug: emailverifier-dev-verification-result
jsonld:
- class_count: 8
  name: Emailverifier Dev Context
  property_count: 17
  slug: emailverifier-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at emailverifier.dev.
  name: emailverifier-dev MCP Server
  slug: emailverifier-dev-mcp-yml
modified: '2026-10-30'
name: emailverifier-dev
nav: Providers
network: true
overview: 'emailverifier-dev publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Domains API, Usage API, and Verification API. Tagged areas include Email, Verification, API, SaaS, and DataQuality.


  The emailverifier-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  emailverifier-dev''s developer surface includes authentication, documentation, API reference, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Emailverifier Dev Plans Pricing
  plan_count: 2
  slug: emailverifier-dev-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Emailverifier Dev Rate Limits
  slug: emailverifier-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: emailverifier-dev API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: emailverifier-dev-rules
scopes:
- name: Emailverifier Dev Scopes
  scope_count: 0
  slug: emailverifier-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 84.9
    catalog_earned_first_party: 0.0
    catalog_gap: 30.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.7
    contract_governance: 79.1
    contract_quality: 61.6
    developer_ergonomics: 49.3
    discoverability: 65.0
    operational_transparency: 0.0
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
  name: Emailverifier Dev Authentication
  slug: emailverifier-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Emailverifier Dev Domain Security
  slug: emailverifier-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: classify-domain
  slug: emailverifier-dev-classify-domain
- name: get-usage
  slug: emailverifier-dev-get-usage
- name: verify-email
  slug: emailverifier-dev-verify-email
slug: emailverifier-dev
tags:
- Email
- Verification
- API
- SaaS
- DataQuality
website: https://emailverifier.dev/
---
