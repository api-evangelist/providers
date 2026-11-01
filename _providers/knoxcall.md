---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 63.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 126
  human_in_the_loop: 14
  name: Knoxcall Agentic Access
  operation_count: 199
  slug: knoxcall-agentic-access
  summary_line: 199 operations · 126 acting · 14 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Retrieve account information and usage metrics.
  name: KnoxCall Account API
  slug: knoxcall-account-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Manage BYO server agents (self-hosted data-plane / tunnel agents).
  name: KnoxCall Agents API
  slug: knoxcall-agents-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Manage AI egress gateways, their agents, and capability (phantom) tokens, plus cost/token spend rollups and FinOps exports.
  name: KnoxCall AI Gateway API
  slug: knoxcall-ai-gateway-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Create and revoke API keys for programmatic access.
  name: KnoxCall API Keys API
  slug: knoxcall-api-keys-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Query the immutable audit trail of all API actions.
  name: KnoxCall Audit Logs API
  slug: knoxcall-audit-logs-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Single-use client-side capability tokens (`kct_` prefix) that let a browser exchange one bound ciphertext or vault token for its plaintext.
  name: KnoxCall Client Tokens API
  slug: knoxcall-client-tokens-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Manage authorized clients (users or servers) with IP-based access control.
  name: KnoxCall Clients API
  slug: knoxcall-clients-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Transit encryption keys — encrypt, decrypt, rewrap, sign, verify, and issue JWTs without key material ever leaving KnoxCall.
  name: KnoxCall Crypto Keys API
  slug: knoxcall-crypto-keys-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Just-in-time database credentials — register connections and roles, then mint short-lived leased users on demand.
  name: KnoxCall Dynamic DB Credentials API
  slug: knoxcall-dynamic-db-credentials-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Portable structure-preserving encryption — encrypt any JSON into storable `kc:` ciphertext strings and decrypt them later.
  name: KnoxCall Encryption API
  slug: knoxcall-encryption-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Manage deployment environments (e.g. production, staging) for route configuration overrides.
  name: KnoxCall Environments API
  slug: knoxcall-environments-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: One-shot proxy that resolves vault-token template expressions on the wire — no pre-configured route required.
  name: KnoxCall Ephemeral Proxy API
  slug: knoxcall-ephemeral-proxy-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Manage OAuth 2.1 clients used to mint access tokens for the API.
  name: KnoxCall OAuth Clients API
  slug: knoxcall-oauth-clients-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Suggestions to turn detected outbound API usage (agent-observed or gateway-traffic) into a durable route; accept promotes to a route + secret binding.
  name: KnoxCall Opportunities API
  slug: knoxcall-opportunities-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Private certificate authority — roots, issuing roles, leaf certificates, revocation, and CRLs.
  name: KnoxCall PKI API
  slug: knoxcall-pki-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: The per-call proxy request log, and Merkle inclusion proofs that make an anchored entry provable to a third party.
  name: KnoxCall Request Logs API
  slug: knoxcall-request-logs-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Manage proxy routes that forward API requests to upstream targets.
  name: KnoxCall Routes API
  slug: knoxcall-routes-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Manage encrypted secrets injected into route headers and bodies.
  name: KnoxCall Secrets API
  slug: knoxcall-secrets-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Headless account creation — the only unauthenticated endpoint, designed so scripts and AI agents can onboard without a browser.
  name: KnoxCall Signup API
  slug: knoxcall-signup-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Data tokenization vaults — swap sensitive values for format-preserving tokens and detokenize them under audit.
  name: KnoxCall Vaults API
  slug: knoxcall-vaults-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: The Webhook Events API from KnoxCall — 0 operation(s) for webhook events.
  name: KnoxCall Webhook Events API
  slug: knoxcall-webhook-events-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Manage webhook subscriptions for real-time event notifications.
  name: KnoxCall Webhooks API
  slug: knoxcall-webhooks-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Create, manage, and run workflows. Executions are asynchronous; poll executions or subscribe a webhook to workflow.execution.completed|failed.
  name: KnoxCall Workflows API
  slug: knoxcall-workflows-api
- baseURL: https://api.knoxcall.com/v1
  baseurl_source: declared
  description: Escrow a third-party provider key into KnoxCall custody so it leaves your codebase, host-pinned; the ephemeral proxy injects it under X-Knox-Upstream-Auth-Secret.
  name: KnoxCall Wrap Credentials API
  slug: knoxcall-wrap-credentials-api
artifact_total: 45
asyncapis:
- description: ''
  name: Knoxcall Webhooks
  slug: knoxcall-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/knoxcall/agentic-access/knoxcall-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/knoxcall-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/knoxcall/rate-limits/knoxcall-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/knoxcall-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/knoxcall/plans/knoxcall-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/knoxcall-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/knoxcall/rules/knoxcall-rules.yml
  title: ''
  type: Spectral
  url: rules/knoxcall-rules.yml
- group: design
  href: https://artifacts.apis.io/knoxcall/json-ld/knoxcall-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/knoxcall-context.jsonld
- group: design
  href: https://artifacts.apis.io/knoxcall/vocabulary/knoxcall-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/knoxcall-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/knoxcall/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/knoxcall/asyncapi/knoxcall-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/knoxcall-webhooks.yml
- group: design
  href: https://artifacts.apis.io/knoxcall/data-model/knoxcall-data-model.yml
  title: ''
  type: DataModel
  url: data-model/knoxcall-data-model.yml
- group: design
  href: https://artifacts.apis.io/knoxcall/conventions/knoxcall-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/knoxcall-conventions.yml
- group: design
  href: https://artifacts.apis.io/knoxcall/conventions/knoxcall-conventions.yml
  title: ''
  type: Conventions
  url: conventions/knoxcall-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://knoxcall.com/trust
- group: auth
  href: https://artifacts.apis.io/knoxcall/authentication/knoxcall-authentication.yml
  title: ''
  type: Authentication
  url: authentication/knoxcall-authentication.yml
- group: design
  href: https://artifacts.apis.io/knoxcall/errors/knoxcall-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/knoxcall-problem-types.yml
- group: design
  href: https://artifacts.apis.io/knoxcall/conformance/knoxcall-conformance.yml
  title: ''
  type: Conformance
  url: conformance/knoxcall-conformance.yml
- group: agent
  href: https://artifacts.apis.io/knoxcall/llms/knoxcall-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/knoxcall-llms.txt
- group: other
  href: https://artifacts.apis.io/knoxcall/a2a/knoxcall-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/knoxcall-a2a.yml
- group: auth
  href: https://artifacts.apis.io/knoxcall/well-known/knoxcall-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/knoxcall-security.txt
- group: auth
  href: https://artifacts.apis.io/knoxcall/well-known/knoxcall-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/knoxcall-api-security.txt
- group: agent
  href: https://artifacts.apis.io/knoxcall/well-known/knoxcall-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/knoxcall-well-known.yml
- group: other
  href: https://artifacts.apis.io/knoxcall/hosts/knoxcall-hosts.yml
  title: ''
  type: Hosts
  url: hosts/knoxcall-hosts.yml
- group: other
  href: https://artifacts.apis.io/knoxcall/vendors/knoxcall-vendors.yml
  title: ''
  type: Vendors
  url: vendors/knoxcall-vendors.yml
- group: build
  href: https://artifacts.apis.io/knoxcall/packages/knoxcall-packages.yml
  title: ''
  type: Packages
  url: packages/knoxcall-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://knoxcall.com/security
- group: build
  title: ''
  type: SDKs
  url: https://knoxcall.com/sdk
- group: auth
  href: https://artifacts.apis.io/knoxcall/scopes/knoxcall-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/knoxcall-scopes.yml
- group: auth
  href: https://artifacts.apis.io/knoxcall/security/knoxcall-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/knoxcall-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/knoxcall/security/knoxcall-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/knoxcall-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/knoxcall/security/knoxcall-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/knoxcall-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://knoxcall.com/
- group: company
  title: ''
  type: Blog
  url: https://knoxcall.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://knoxcall.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://knoxcall.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://knoxcall.com/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.knoxcall.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knoxcall.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.knoxcall.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.knoxcall.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.knoxcall.com/support
- group: operate
  title: ''
  type: Roadmap
  url: https://knoxcall.com/roadmap
- group: start
  title: ''
  type: SignUp
  url: https://knoxcall.com/register
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/knoxcall/workspace
created: '2026-10-18'
description: KnoxCall provides a secure API key management platform that stores third‑party API keys (such as Stripe, OpenAI, and many others) and injects them at egress. This enables applications, CI pipelines, and AI agents to use revocable tokens instead of permanent credentials, reducing risk of key leakage. The service offers features like token revocation, usage monitoring, and integration with popular developer tools, helping teams protect their secret keys while maintaining seamless access to external services.
image: https://knoxcall.com/og-image.png
json_schemas:
- name: AiGatewayAgent
  property_count: 48
  slug: knoxcall-ai-gateway-agent
- name: AiGatewayMcpServer
  property_count: 24
  slug: knoxcall-ai-gateway-mcp-server
- name: CreateAiGatewayAgentRequest
  property_count: 41
  slug: knoxcall-create-ai-gateway-agent-request
- name: CreateWebhookRequest
  property_count: 19
  slug: knoxcall-create-webhook-request
- name: RequestLog
  property_count: 23
  slug: knoxcall-request-log
- name: UpdateAiGatewayAgentRequest
  property_count: 38
  slug: knoxcall-update-ai-gateway-agent-request
jsonld:
- class_count: 120
  name: Knoxcall Context
  property_count: 404
  slug: knoxcall-context
layout: provider
modified: '2026-10-18'
name: KnoxCall
nav: Providers
network: true
overview: 'KnoxCall publishes 24 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agents API, AI Gateway API, and 21 more. Tagged areas include Company, API Management, Security, DevOps, and AI Agents.


  The KnoxCall catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  KnoxCall''s developer surface includes authentication, engineering blog, pricing, documentation, API reference, getting-started guide, support, and 35 more developer resources.'
plans:
- name: Knoxcall Plans Pricing
  plan_count: 4
  slug: knoxcall-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 9
  name: Knoxcall Rate Limits
  slug: knoxcall-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: KnoxCall API Rules
  rule_count: 16
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 5
  slug: knoxcall-rules
scopes:
- name: Knoxcall Scopes
  scope_count: 13
  slug: knoxcall-scopes
  summary_line: 13 scopes · clientCredentials/authorizationCode
score:
  band: exemplar
  composite: 73.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 74.0
    developer_ergonomics: 70.8
    discoverability: 66.1
    operational_transparency: 55.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Knoxcall Authentication
  slug: knoxcall-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Knoxcall Domain Security
  slug: knoxcall-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Knoxcall Vulnerability Disclosure
  slug: knoxcall-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Knoxcall Trust Center
  slug: knoxcall-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, GDPR
skill_count: 4
skills:
- name: knoxcall-create-and-test-webhook
  slug: knoxcall-create-and-test-webhook
- name: knoxcall-create-client
  slug: knoxcall-create-client
- name: knoxcall-process-opportunities
  slug: knoxcall-process-opportunities
- name: knoxcall-signup
  slug: knoxcall-signup
slug: knoxcall
tags:
- Company
- API Management
- Security
- DevOps
- AI Agents
website: https://knoxcall.com/
---
