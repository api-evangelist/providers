---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 67.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 48
  human_in_the_loop: 6
  name: Apier No Agentic Access
  operation_count: 156
  slug: apier-no-agentic-access
  summary_line: 156 operations · 48 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://www.apier.no
  baseurl_source: declared
  description: 'Consumer self-serve account management — sign-up, magic-link request, key issuance. The /api/v1/account/signup endpoint is `security: []` on purpose: an unauthenticated visitor can request a magic lin'
  name: Apier.no Account API
  slug: apier-no-account-api
- baseURL: https://www.apier.no
  baseurl_source: declared
  description: Withdrawn (2026-10-21). The filing-action surface (`POST /api/v1/actions/execute` in dry-run and live mode, the pending-action approve / reject / status routes) answers HTTP 410 `CAPABILITY_WITHDRAWN`
  name: Apier.no Actions API
  slug: apier-no-actions-api
- baseURL: https://www.apier.no
  baseurl_source: declared
  description: Administrative endpoints for managing consumers and API keys. Requires ADMIN_API_KEY.
  name: Apier.no Admin API
  slug: apier-no-admin-api
- baseURL: https://www.apier.no
  baseurl_source: declared
  description: Withdrawn (2026-10-21). The Altinn-sourced authorisation surface (acting-capacity resolution over Altinn roles and delegations) answers HTTP 410 `CAPABILITY_WITHDRAWN`; its paths and schemas stay publ
  name: Apier.no Altinn API
  slug: apier-no-altinn-api
- baseURL: https://www.apier.no
  baseurl_source: declared
  description: Withdrawn (2026-10-21). The delegation endpoints that used to arrange Maskinporten and Altinn access on the consumer's behalf answer HTTP 410 `CAPABILITY_WITHDRAWN` on every call; the paths stay publi
  name: Apier.no Auth Gateway API
  slug: apier-no-auth-gateway-api
- baseURL: https://www.apier.no
  baseurl_source: declared
  description: Brønnøysund Enhetsregisteret context surface — agent-shaped company profile reads. NLOD-licensed public data; role codes only, never personal identifiers (two-layer defense).
  name: Apier.no Brreg API
  slug: apier-no-brreg-api
- baseURL: https://www.apier.no
  baseurl_source: declared
  description: Cross-source change archive — detected archive events from Brreg, Altinn, DigDir, Norges Bank, NAV Aa-registeret, and Skatteetaten Tier 2 sub-results (MVA-register + Skatteoppgjør). Each row's derived
  name: Apier.no Changes API
  slug: apier-no-changes-api
- baseURL: https://www.apier.no
  baseurl_source: declared
  description: Reads over the Registry Engine's two-tier company model (Tier 1 public Brønnøysund data + Tier 2 gated commercial metrics).
  name: Apier.no Company API
  slug: apier-no-company-api
- baseURL: https://www.apier.no
  baseurl_source: declared
  description: Agent-first discovery manifest. `/v1/capabilities` is the machine-readable menu of every callable capability; `llms.txt` and `workflows.json` are the prose and recipe counterparts.
  name: Apier.no Discovery API
  slug: apier-no-discovery-api
- baseURL: https://www.apier.no
  baseurl_source: declared
  description: Withdrawn (2026-10-21). The fullmakt line (agent principals, brokered Altinn systembruker delegations, their receipts and revocation) answers HTTP 410 `CAPABILITY_WITHDRAWN` on every call; the paths a
  name: Apier.no Fullmakt API
  slug: apier-no-fullmakt-api
- baseURL: https://www.apier.no
  baseurl_source: declared
  description: Non-product endpoints (health checks, discovery).
  name: Apier.no Infrastructure API
  slug: apier-no-infrastructure-api
- baseURL: https://www.apier.no
  baseurl_source: declared
  description: The Knowledge Catalog — canonical, machine-readable topic records answering what an agent needs to KNOW about Norwegian company authority and government-integration subjects (Altinn System Users, Mask
  name: Apier.no Knowledge API
  slug: apier-no-knowledge-api
- baseURL: https://www.apier.no
  baseurl_source: declared
  description: Zero-auth GDPR transparency endpoints — Article 15 access requests via DSR. Rate-limited per IP (10/min, lower than Category A's 1000/min) so the surface cannot be used as a name-enumeration bulk-expo
  name: Apier.no Privacy API
  slug: apier-no-privacy-api
- baseURL: https://www.apier.no
  baseurl_source: declared
  description: Free, zero-auth endpoints. Rate-limited per-IP (soft cap 1000/min). Distribution infrastructure, not revenue — these exist so agents can discover the API surface and answer baseline regulatory questio
  name: Apier.no Public API
  slug: apier-no-public-api
- baseURL: https://www.apier.no
  baseurl_source: declared
  description: Zero-auth, deterministic, CORS-open mirrors of every Category B company endpoint. Returns synthetic Norwegian company fixtures so agents can test failure-flows without provisioning an Apier API key, w
  name: Apier.no Sandbox API
  slug: apier-no-sandbox-api
- baseURL: https://www.apier.no
  baseurl_source: declared
  description: Pro-tier change-detection webhook subscriptions. Consumers register a webhook URL + filter; Apier fires HMAC-SHA256-signed deliveries when matching change-archive events appear. SSRF-resistant (privat
  name: Apier.no Subscriptions API
  slug: apier-no-subscriptions-api
artifact_total: 34
asyncapis:
- description: ''
  name: Apier No Webhooks
  slug: apier-no-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/apier-no/agentic-access/apier-no-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apier-no-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/apier-no/rate-limits/apier-no-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apier-no-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/apier-no/plans/apier-no-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apier-no-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apier-no/rules/apier-no-rules.yml
  title: ''
  type: Spectral
  url: rules/apier-no-rules.yml
- group: design
  href: https://artifacts.apis.io/apier-no/json-ld/apier-no-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apier-no-context.jsonld
- group: design
  href: https://artifacts.apis.io/apier-no/vocabulary/apier-no-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apier-no-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/apier-no/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/apier-no/asyncapi/apier-no-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/apier-no-webhooks.yml
- group: design
  href: https://artifacts.apis.io/apier-no/data-model/apier-no-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apier-no-data-model.yml
- group: design
  href: https://artifacts.apis.io/apier-no/conventions/apier-no-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/apier-no-conventions.yml
- group: design
  href: https://artifacts.apis.io/apier-no/conventions/apier-no-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apier-no-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.apier.no/trust
- group: auth
  href: https://artifacts.apis.io/apier-no/authentication/apier-no-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apier-no-authentication.yml
- group: design
  href: https://artifacts.apis.io/apier-no/lifecycle/apier-no-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apier-no-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/apier-no/errors/apier-no-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apier-no-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apier-no/conformance/apier-no-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apier-no-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apier-no/llms/apier-no-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apier-no-llms.txt
- group: agent
  href: https://artifacts.apis.io/apier-no/mcp/apier-no-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apier-no-mcp.yml
- group: auth
  href: https://artifacts.apis.io/apier-no/well-known/apier-no-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apier-no-security.txt
- group: auth
  href: https://artifacts.apis.io/apier-no/well-known/apier-no-apier-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apier-no-apier-security.txt
- group: agent
  href: https://artifacts.apis.io/apier-no/well-known/apier-no-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apier-no-well-known.yml
- group: other
  href: https://artifacts.apis.io/apier-no/hosts/apier-no-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apier-no-hosts.yml
- group: other
  href: https://artifacts.apis.io/apier-no/vendors/apier-no-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apier-no-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.apier.no/security
- group: start
  title: ''
  type: Sandbox
  url: https://www.apier.no/sandbox
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.apier.no/docs/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.apier.no/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/apier-no/security/apier-no-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/apier-no-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/apier-no/security/apier-no-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/apier-no-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/apier-no/security/apier-no-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apier-no-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apier.no/
- group: docs
  title: ''
  type: Documentation
  url: https://www.apier.no/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.apier.no/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://www.apier.no/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.apier.no/blog
- group: operate
  title: ''
  type: Support
  url: https://www.apier.no/support
- group: operate
  title: ''
  type: Roadmap
  url: https://www.apier.no/roadmap
- group: start
  title: ''
  type: Login
  url: https://www.apier.no/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apier.no/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apier.no/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://apier.betteruptime.com/
created: '2026-11-01'
description: Apier.no provides machine‑verifiable Norwegian company authority data via an API. It offers status, roles, and coded signing authority directly from Brønnøysundregistrene, with source, history, and signed receipts. The service is self‑serve, with no sales call, and supports AI agents through MCP tools and OpenAPI specifications.
image: https://www.apier.no/logo.svg
json_schemas:
- name: CompanyContext
  property_count: 22
  slug: apier-no-company-context
- name: CompanyVerification
  property_count: 15
  slug: apier-no-company-verification
- name: ErrorCode
  property_count: 0
  slug: apier-no-error-code
- name: SandboxMeta
  property_count: 15
  slug: apier-no-sandbox-meta
- name: SignedReceipt
  property_count: 12
  slug: apier-no-signed-receipt
- name: TrustMetadata
  property_count: 25
  slug: apier-no-trust-metadata
jsonld:
- class_count: 113
  name: Apier No Context
  property_count: 363
  slug: apier-no-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.apier.no.
  name: Apier.no MCP Server
  slug: apier-no-mcp-yml
modified: '2026-11-01'
name: Apier.no
nav: Providers
network: true
overview: 'Apier.no publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Actions API, Admin API, and 13 more. Tagged areas include Norwegian, Company Data, MCP, and Verification.


  The Apier.no catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Apier.no''s developer surface includes authentication, sandbox, changelog, getting-started guide, documentation, API reference, pricing, and 34 more developer resources.'
plans:
- name: Apier No Plans Pricing
  plan_count: 1
  slug: apier-no-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Apier No Rate Limits
  slug: apier-no-rate-limits
rules:
- authorship: generated
  effective_rule_count: 119
  extends:
  - spectral:oas
  name: Apier.no API Rules
  rule_count: 78
  severity_counts:
    error: 61
    hint: 0
    info: 1
    warn: 16
  slug: apier-no-rules
scopes:
- name: Apier No Scopes
  scope_count: 0
  slug: apier-no-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -14.4
  facets:
    access_clarity: 55.3
    contract_governance: 35.6
    contract_quality: 73.9
    developer_ergonomics: 39.8
    discoverability: 56.7
    operational_transparency: 63.2
  previous_composite: 73.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apier No Authentication
  slug: apier-no-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Apier No Domain Security
  slug: apier-no-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Apier No Vulnerability Disclosure
  slug: apier-no-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Apier No Trust Center
  slug: apier-no-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: apier-no
tags:
- Norwegian
- Company Data
- MCP
- Verification
website: https://apier.no/
---
