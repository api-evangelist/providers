---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
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
  score: 61.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 81
  human_in_the_loop: 8
  name: Honkio Ca Agentic Access
  operation_count: 135
  slug: honkio-ca-agentic-access
  summary_line: 135 operations · 81 acting · 8 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: Account management and API keys
  name: honkio-ca Accounts API
  slug: honkio-ca-accounts-api
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: Dashboard login and password management
  name: honkio-ca Auth API
  slug: honkio-ca-auth-api
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: CASL consent and opt-out management
  name: honkio-ca Compliance / CASL API
  slug: honkio-ca-compliance-casl-api
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: CRTC Do Not Call List lookups (coming soon)
  name: honkio-ca Compliance / DNCL API
  slug: honkio-ca-compliance-dncl-api
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: Privacy compliance and right to erasure
  name: honkio-ca Compliance / PIPEDA API
  slug: honkio-ca-compliance-pipeda-api
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: Group contacts and send group broadcasts
  name: honkio-ca Contact Groups API
  slug: honkio-ca-contact-groups-api
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: Manage contact phone numbers and metadata
  name: honkio-ca Contacts API
  slug: honkio-ca-contacts-api
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: Verify sending domains for email
  name: honkio-ca Email Domains API
  slug: honkio-ca-email-domains-api
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: Manage email suppression lists
  name: honkio-ca Email Suppressions API
  slug: honkio-ca-email-suppressions-api
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: Store email templates and publish versions to send by id or alias
  name: honkio-ca Email Templates API
  slug: honkio-ca-email-templates-api
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: Send and read email
  name: honkio-ca Emails API
  slug: honkio-ca-emails-api
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: Allow/deny contact lists assignable to API keys
  name: honkio-ca Lists API
  slug: honkio-ca-lists-api
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: Send and receive SMS messages
  name: honkio-ca Messages API
  slug: honkio-ca-messages-api
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: 'OAuth 2.1 authorization server used by MCP clients (Claude, ChatGPT, Gemini) to sign in instead of carrying an API key. Discovery: /.well-known/oauth-authorization-server'
  name: honkio-ca OAuth API
  slug: honkio-ca-oauth-api
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: Provision and manage Canadian phone numbers
  name: honkio-ca Phone Numbers API
  slug: honkio-ca-phone-numbers-api
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: Current per-send prices, so an integrator can quote a cost before sending
  name: honkio-ca Pricing API
  slug: honkio-ca-pricing-api
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: Phone number verification (SMS OTP) with per-verification upcharge
  name: honkio-ca Verify API
  slug: honkio-ca-verify-api
- baseURL: https://api.honkio.ca
  baseurl_source: declared
  description: Register endpoints to receive event notifications
  name: honkio-ca Webhooks API
  slug: honkio-ca-webhooks-api
artifact_total: 32
common:
- group: agent
  href: https://artifacts.apis.io/honkio-ca/agentic-access/honkio-ca-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/honkio-ca-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/honkio-ca/rate-limits/honkio-ca-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/honkio-ca-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/honkio-ca/plans/honkio-ca-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/honkio-ca-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/honkio-ca/rules/honkio-ca-rules.yml
  title: ''
  type: Spectral
  url: rules/honkio-ca-rules.yml
- group: design
  href: https://artifacts.apis.io/honkio-ca/json-ld/honkio-ca-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/honkio-ca-context.jsonld
- group: design
  href: https://artifacts.apis.io/honkio-ca/vocabulary/honkio-ca-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/honkio-ca-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/honkio-ca/data-model/honkio-ca-data-model.yml
  title: ''
  type: DataModel
  url: data-model/honkio-ca-data-model.yml
- group: design
  href: https://artifacts.apis.io/honkio-ca/conventions/honkio-ca-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/honkio-ca-conventions.yml
- group: design
  href: https://artifacts.apis.io/honkio-ca/conventions/honkio-ca-conventions.yml
  title: ''
  type: Conventions
  url: conventions/honkio-ca-conventions.yml
- group: auth
  href: https://artifacts.apis.io/honkio-ca/authentication/honkio-ca-authentication.yml
  title: ''
  type: Authentication
  url: authentication/honkio-ca-authentication.yml
- group: design
  href: https://artifacts.apis.io/honkio-ca/errors/honkio-ca-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/honkio-ca-problem-types.yml
- group: design
  href: https://artifacts.apis.io/honkio-ca/conformance/honkio-ca-conformance.yml
  title: ''
  type: Conformance
  url: conformance/honkio-ca-conformance.yml
- group: agent
  href: https://artifacts.apis.io/honkio-ca/llms/honkio-ca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/honkio-ca-llms.txt
- group: agent
  href: https://artifacts.apis.io/honkio-ca/mcp/honkio-ca-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/honkio-ca-mcp.yml
- group: agent
  href: https://artifacts.apis.io/honkio-ca/well-known/honkio-ca-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/honkio-ca-well-known.yml
- group: other
  href: https://artifacts.apis.io/honkio-ca/hosts/honkio-ca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/honkio-ca-hosts.yml
- group: build
  href: https://artifacts.apis.io/honkio-ca/packages/honkio-ca-packages.yml
  title: ''
  type: SDKs
  url: packages/honkio-ca-packages.yml
- group: build
  href: https://artifacts.apis.io/honkio-ca/packages/honkio-ca-packages.yml
  title: ''
  type: Packages
  url: packages/honkio-ca-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://honkio.ca/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://honkio.ca/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://honkio.ca/legal/privacy
- group: auth
  href: https://artifacts.apis.io/honkio-ca/security/honkio-ca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/honkio-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://honkio.ca/
- group: docs
  title: ''
  type: Documentation
  url: https://honkio.ca/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://honkio.ca/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://honkio.ca/pricing
- group: start
  title: ''
  type: SignUp
  url: https://honkio.ca/signup
- group: start
  title: ''
  type: Login
  url: https://honkio.ca/login
- group: company
  title: ''
  type: Blog
  url: https://honkio.ca/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/honkio
created: '2026-10-30'
description: HonkIO provides a Canadian‑focused SMS and email API that includes built‑in CASL compliance, PIPEDA‑ready data residency, and upcoming CRTC DNCL checking. The service stores all data in Montréal, offers pay‑per‑message pricing in CAD, and supports features such as consent management, STOP handling, bounce suppression, phone verification, email templates, batch sending, scheduling, and HMAC‑signed webhooks. Developers can access SDKs for Node.js and an MCP server, and a sandbox environment is available for testing.
image: https://honkio.ca/logo.png
json_schemas:
- name: AccountDocument
  property_count: 4
  slug: honkio-ca-account-document
- name: AccountMeDocument
  property_count: 5
  slug: honkio-ca-account-me-document
- name: Message
  property_count: 19
  slug: honkio-ca-message
- name: SendLimit
  property_count: 14
  slug: honkio-ca-send-limit
- name: SentMessage
  property_count: 20
  slug: honkio-ca-sent-message
- name: TollFreeVerification
  property_count: 15
  slug: honkio-ca-toll-free-verification
jsonld:
- class_count: 33
  name: Honkio Ca Context
  property_count: 208
  slug: honkio-ca-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.honkio.ca requiring an API key.
  name: honkio-ca MCP Server
  slug: honkio-ca-mcp-yml
modified: '2026-10-30'
name: honkio-ca
nav: Providers
network: true
overview: 'honkio-ca publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Auth API, Compliance / CASL API, and 15 more. Tagged areas include SMS, Email, Canada, CASL, and PIPEDA.


  The honkio-ca catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  honkio-ca''s developer surface includes authentication, documentation, getting-started guide, pricing, signup flow, engineering blog, and 24 more developer resources.'
plans:
- name: Honkio Ca Plans Pricing
  plan_count: 1
  slug: honkio-ca-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Honkio Ca Rate Limits
  slug: honkio-ca-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: honkio-ca API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 5
  slug: honkio-ca-rules
score:
  band: strong
  composite: 58.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 92.1
    catalog_earned_first_party: 0.0
    catalog_gap: 22.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.7
    contract_governance: 79.1
    contract_quality: 59.2
    developer_ergonomics: 50.0
    discoverability: 65.0
    operational_transparency: 40.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 20.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Honkio Ca Authentication
  slug: honkio-ca-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Honkio Ca Domain Security
  slug: honkio-ca-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: honkio-ca
tags:
- SMS
- Email
- Canada
- CASL
- PIPEDA
- Company
website: https://honkio.ca/
---
