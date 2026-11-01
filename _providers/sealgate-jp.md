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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.8
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API reference for SealGate authentication platform.
  name: SealGate API
  slug: sealgate-api
- baseURL: https://app.sealgate.jp
  baseurl_source: declared
  description: 'sealgate-jp API as documented publicly: 23 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: sealgate-jp API
  slug: sealgate-jp-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/sealgate-jp/rate-limits/sealgate-jp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sealgate-jp-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/sealgate-jp/plans/sealgate-jp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sealgate-jp-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/sealgate-jp/rules/sealgate-jp-rules.yml
  title: ''
  type: Spectral
  url: rules/sealgate-jp-rules.yml
- group: design
  href: https://artifacts.apis.io/sealgate-jp/json-ld/sealgate-jp-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sealgate-jp-context.jsonld
- group: design
  href: https://artifacts.apis.io/sealgate-jp/vocabulary/sealgate-jp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sealgate-jp-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sealgate-jp/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sealgate-jp/data-model/sealgate-jp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sealgate-jp-data-model.yml
- group: design
  href: https://artifacts.apis.io/sealgate-jp/conventions/sealgate-jp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sealgate-jp-conventions.yml
- group: auth
  href: https://artifacts.apis.io/sealgate-jp/authentication/sealgate-jp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sealgate-jp-authentication.yml
- group: design
  href: https://artifacts.apis.io/sealgate-jp/errors/sealgate-jp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sealgate-jp-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sealgate-jp/conformance/sealgate-jp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sealgate-jp-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sealgate-jp/llms/sealgate-jp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sealgate-jp-llms.txt
- group: agent
  href: https://artifacts.apis.io/sealgate-jp/mcp/sealgate-jp-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sealgate-jp-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sealgate-jp/well-known/sealgate-jp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sealgate-jp-well-known.yml
- group: other
  href: https://artifacts.apis.io/sealgate-jp/hosts/sealgate-jp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sealgate-jp-hosts.yml
- group: other
  href: https://artifacts.apis.io/sealgate-jp/vendors/sealgate-jp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sealgate-jp-vendors.yml
- group: build
  href: https://artifacts.apis.io/sealgate-jp/packages/sealgate-jp-packages.yml
  title: ''
  type: SDKs
  url: packages/sealgate-jp-packages.yml
- group: build
  href: https://artifacts.apis.io/sealgate-jp/packages/sealgate-jp-packages.yml
  title: ''
  type: Packages
  url: packages/sealgate-jp-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sealgate.jp/terms
- group: start
  title: ''
  type: SignUp
  url: https://sealgate.jp/app/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sealgate.jp/privacy
- group: auth
  href: https://artifacts.apis.io/sealgate-jp/security/sealgate-jp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sealgate-jp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sealgate.jp/
- group: docs
  title: ''
  type: Documentation
  url: https://sealgate.jp/docs
- group: company
  title: ''
  type: Blog
  url: https://sealgate.jp/blog
- group: operate
  title: ''
  type: Support
  url: https://sealgate.jp/contact
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are rendered via JavaScript and provide no machine‑readable OpenAPI/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://sealgate.jp/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: SealGate は日本で開発・運用しているパスキー認証基盤です。WebAuthn (FIDO2) の登録・認証・失効・復旧を API と SDK で提供します。秘密鍵は利用者の端末の中にとどまり、SealGate が保存するのは公開鍵だけです。これにより、パスキー認証の安全性とプライバシーを確保し、企業や開発者が簡単に認証機能を統合できるプラットフォームを提供します。
image: https://sealgate.jp/opengraph-image.png
json_schemas:
- name: GetV1AppsAppidResponse
  property_count: 9
  slug: sealgate-jp-get-v1-apps-appid-response
- name: PatchV1AppsAppidRequest
  property_count: 2
  slug: sealgate-jp-patch-v1-apps-appid-request
- name: PatchV1CredentialsCredentialidResponse
  property_count: 9
  slug: sealgate-jp-patch-v1-credentials-credentialid-response
- name: PatchV1UsersExternalidCredentialsCredentialidResponse
  property_count: 9
  slug: sealgate-jp-patch-v1-users-externalid-credentials-credentialid-response
- name: PostV1LoginVerifyResponse
  property_count: 5
  slug: sealgate-jp-post-v1-login-verify-response
- name: PostV1RegisterOptionsRequest
  property_count: 4
  slug: sealgate-jp-post-v1-register-options-request
jsonld:
- class_count: 23
  name: Sealgate Jp Context
  property_count: 44
  slug: sealgate-jp-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.sealgate.jp requiring OAuth.
  name: sealgate-jp MCP Server
  slug: sealgate-jp-mcp-yml
modified: '2026-10-31'
name: sealgate-jp
nav: Providers
network: true
overview: 'sealgate-jp is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Authentication, WebAuthn, FIDO2, Security, and Japan.


  The sealgate-jp catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  sealgate-jp''s developer surface includes authentication, signup flow, documentation, engineering blog, support, and 21 more developer resources.'
plans:
- name: Sealgate Jp Plans Pricing
  plan_count: 5
  slug: sealgate-jp-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 4
  name: Sealgate Jp Rate Limits
  slug: sealgate-jp-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: sealgate-jp API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: sealgate-jp-rules
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 91.6
    catalog_earned_first_party: 0.0
    catalog_gap: 23.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 62.6
    contract_governance: 70.9
    contract_quality: 55.2
    developer_ergonomics: 42.1
    discoverability: 56.7
    operational_transparency: 28.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sealgate Jp Authentication
  slug: sealgate-jp-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sealgate Jp Domain Security
  slug: sealgate-jp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: sealgate
  slug: sealgate-jp-integration
slug: sealgate-jp
tags:
- Authentication
- WebAuthn
- FIDO2
- Security
- Japan
website: https://sealgate.jp/
---
