---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 70.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Robase Dev Agentic Access
  operation_count: 9
  slug: robase-dev-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.robase.dev
  baseurl_source: declared
  description: Account endpoints used by the web app. Not part of the public SMS API.
  name: robase-dev Dashboard API
  slug: robase-dev-dashboard-api
- baseURL: https://api.robase.dev
  baseurl_source: declared
  description: Generate, deliver and verify one-time passwords.
  name: robase-dev OTP API
  slug: robase-dev-otp-api
- baseURL: https://api.robase.dev
  baseurl_source: declared
  description: Send arbitrary transactional messages.
  name: robase-dev SMS API
  slug: robase-dev-sms-api
- baseURL: https://api.robase.dev
  baseurl_source: declared
  description: Unauthenticated operational endpoints.
  name: robase-dev System API
  slug: robase-dev-system-api
artifact_total: 19
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://robase.dev/pricing
- group: agent
  href: https://artifacts.apis.io/robase-dev/agentic-access/robase-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/robase-dev-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/robase-dev/rate-limits/robase-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/robase-dev-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/robase-dev/rules/robase-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/robase-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/robase-dev/json-ld/robase-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/robase-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/robase-dev/vocabulary/robase-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/robase-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/robase-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/robase-dev/data-model/robase-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/robase-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/robase-dev/conventions/robase-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/robase-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/robase-dev/conventions/robase-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/robase-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/robase-dev/authentication/robase-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/robase-dev-authentication.yml
- group: auth
  href: https://artifacts.apis.io/robase-dev/scopes/robase-dev-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/robase-dev-scopes.yml
- group: design
  href: https://artifacts.apis.io/robase-dev/lifecycle/robase-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/robase-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/robase-dev/errors/robase-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/robase-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/robase-dev/conformance/robase-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/robase-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/robase-dev/llms/robase-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/robase-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/robase-dev/a2a/robase-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/robase-dev-a2a.yml
- group: build
  href: https://artifacts.apis.io/robase-dev/mcp/robase-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/robase-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/robase-dev/mcp/robase-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/robase-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/robase-dev/well-known/robase-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/robase-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/robase-dev/hosts/robase-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/robase-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/robase-dev/vendors/robase-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/robase-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/robase-dev/packages/robase-dev-packages.yml
  title: ''
  type: Packages
  url: packages/robase-dev-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://robase.dev/terms
- group: operate
  title: ''
  type: Support
  url: https://robase.dev/app/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.robase.dev/
- group: auth
  title: ''
  type: Security
  url: https://robase.dev/security
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@robasedev/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://robase.dev/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://robase.dev/changelog
- group: company
  title: ''
  type: Blog
  url: https://robase.dev/blog
- group: start
  title: ''
  type: SignUp
  url: https://robase.dev/signup
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.robase.dev/quickstart
- group: auth
  href: https://artifacts.apis.io/robase-dev/security/robase-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/robase-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://robase.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.robase.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.robase.dev/api-reference/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mantissatech
created: '2026-10-31'
description: Robase provides SMS OTP and transactional SMS services across Africa, enabling developers to integrate one‑time password verification and bulk messaging via a simple REST API. The platform offers prepaid credits, automatic failover across six markets (Nigeria, Kenya, Ghana, South Africa, etc.), and SDKs for Node.js, Go, and PHP. With a focus on reliability and low latency, Robase helps businesses secure user authentication and send transactional communications at scale.
image: https://mintcdn.com/kivatechnologies/k2GghN5nZfu1eiOu/logo/light.svg?fit=max&auto=format&n=k2GghN5nZfu1eiOu&q=85&s=193f7e31495ddf41cd16f40f06effd2b
json_schemas:
- name: OTPDetails
  property_count: 21
  slug: robase-dev-otpdetails
- name: SendOTPRequest
  property_count: 6
  slug: robase-dev-send-otprequest
- name: SendOTPResponse
  property_count: 9
  slug: robase-dev-send-otpresponse
- name: SendSMSRequest
  property_count: 3
  slug: robase-dev-send-smsrequest
- name: SendSMSResponse
  property_count: 9
  slug: robase-dev-send-smsresponse
- name: SMSDetails
  property_count: 9
  slug: robase-dev-smsdetails
jsonld:
- class_count: 20
  name: Robase Dev Context
  property_count: 59
  slug: robase-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.robase.dev.
  name: robase-dev MCP Server
  slug: robase-dev-mcp-yml
modified: '2026-10-31'
name: robase-dev
nav: Providers
network: true
overview: 'robase-dev publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dashboard API, OTP API, SMS API, and 1 more. Tagged areas include SMS, OTP, Africa, Messaging, and API.


  The robase-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  robase-dev''s developer surface includes pricing, authentication, support, changelog, engineering blog, signup flow, getting-started guide, and 31 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 8
  name: Robase Dev Rate Limits
  slug: robase-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: robase-dev API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: robase-dev-rules
scopes:
- name: Robase Dev Scopes
  scope_count: 5
  slug: robase-dev-scopes
  summary_line: 5 scopes
score:
  band: strong
  composite: 64.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 59.1
    developer_ergonomics: 61.2
    discoverability: 65.0
    operational_transparency: 75.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 35.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Robase Dev Authentication
  slug: robase-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Robase Dev Domain Security
  slug: robase-dev-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: robase-dev-otp-skill
  slug: robase-dev-otp-skill
slug: robase-dev
tags:
- SMS
- OTP
- Africa
- Messaging
- API
- Communications
website: https://robase.dev/
---
