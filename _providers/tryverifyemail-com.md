---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.tryverifyemail.com
  baseurl_source: declared
  description: 'tryverifyemail-com API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: tryverifyemail-com API
  slug: tryverifyemail-com-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/tryverifyemail-com/rate-limits/tryverifyemail-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tryverifyemail-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tryverifyemail-com/plans/tryverifyemail-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tryverifyemail-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/tryverifyemail-com/rules/tryverifyemail-com-rules.yml
  title: ''
  type: Spectral
  url: rules/tryverifyemail-com-rules.yml
- group: design
  href: https://artifacts.apis.io/tryverifyemail-com/json-ld/tryverifyemail-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tryverifyemail-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/tryverifyemail-com/vocabulary/tryverifyemail-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tryverifyemail-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tryverifyemail-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tryverifyemail-com/data-model/tryverifyemail-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tryverifyemail-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/tryverifyemail-com/changelog/tryverifyemail-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tryverifyemail-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/tryverifyemail-com/authentication/tryverifyemail-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tryverifyemail-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/tryverifyemail-com/errors/tryverifyemail-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tryverifyemail-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tryverifyemail-com/conformance/tryverifyemail-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tryverifyemail-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tryverifyemail-com/llms/tryverifyemail-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tryverifyemail-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/tryverifyemail-com/mcp/tryverifyemail-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tryverifyemail-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/tryverifyemail-com/well-known/tryverifyemail-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tryverifyemail-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/tryverifyemail-com/hosts/tryverifyemail-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tryverifyemail-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/tryverifyemail-com/vendors/tryverifyemail-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tryverifyemail-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://tryverifyemail.com/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://tryverifyemail.com/docs/api/changelog/
- group: auth
  href: https://artifacts.apis.io/tryverifyemail-com/security/tryverifyemail-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tryverifyemail-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tryverifyemail.com/
- group: docs
  title: ''
  type: Documentation
  url: https://tryverifyemail.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://tryverifyemail.com/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://tryverifyemail.com/docs/help/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://tryverifyemail.com/contact
- group: company
  title: ''
  type: Blog
  url: https://tryverifyemail.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://tryverifyemail.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tryverifyemail.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tryverifyemail.com/legal/privacy
created: '2026-10-31'
description: Verify email addresses in seconds with VerifyEmail. Use the free email checker for real-time syntax, domain and MX validation, then clean whole lists in bulk with 99% accuracy at a fraction of the price. GDPR compliant.
image: https://tryverifyemail.com/docs/_astro/logo-3d.DYYIHY8v_260x3g.webp
json_schemas:
- name: GetV1MeResponse
  property_count: 4
  slug: tryverifyemail-com-get-v1-me-response
- name: PostV1BlacklistTargetsIdCheckResponse
  property_count: 2
  slug: tryverifyemail-com-post-v1-blacklist-targets-id-check-response
- name: PostV1BlacklistTargetsResponse
  property_count: 2
  slug: tryverifyemail-com-post-v1-blacklist-targets-response
- name: PostV1BulkVerificationsResponse
  property_count: 4
  slug: tryverifyemail-com-post-v1-bulk-verifications-response
- name: PostV1DmarcDomainsIdVerifyResponse
  property_count: 6
  slug: tryverifyemail-com-post-v1-dmarc-domains-id-verify-response
- name: PostV1DmarcDomainsResponse
  property_count: 3
  slug: tryverifyemail-com-post-v1-dmarc-domains-response
jsonld:
- class_count: 6
  name: Tryverifyemail Com Context
  property_count: 17
  slug: tryverifyemail-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.tryverifyemail.com.
  name: tryverifyemail-com MCP Server
  slug: tryverifyemail-com-mcp-yml
modified: '2026-10-31'
name: tryverifyemail-com
nav: Providers
network: true
overview: 'tryverifyemail-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email Verification, Data Validation, Deliverability, and Bulk.


  The tryverifyemail-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tryverifyemail-com''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 21 more developer resources.'
plans:
- name: Tryverifyemail Com Plans Pricing
  plan_count: 4
  slug: tryverifyemail-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Tryverifyemail Com Rate Limits
  slug: tryverifyemail-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: tryverifyemail-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: tryverifyemail-com-rules
scopes:
- name: Tryverifyemail Com Scopes
  scope_count: 0
  slug: tryverifyemail-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 31
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 26.5
    developer_ergonomics: 36.2
    discoverability: 65.0
    operational_transparency: 47.4
  previous_composite: 50.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tryverifyemail-com/tryverifyemail-com-2026-11-03T145211.png
security:
- kind: authentication
  name: Tryverifyemail Com Authentication
  slug: tryverifyemail-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tryverifyemail Com Domain Security
  slug: tryverifyemail-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: tryverifyemail-com-email-verification
  slug: tryverifyemail-com-email-verification-skill
slug: tryverifyemail-com
tags:
- Company
- Email Verification
- Data Validation
- Deliverability
- Bulk
website: https://tryverifyemail.com/
---
