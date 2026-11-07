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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 306
  human_in_the_loop: 10
  name: Sendly Now Agentic Access
  operation_count: 550
  slug: sendly-now-agentic-access
  summary_line: 550 operations · 306 acting · 10 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: 'The signed-in person''s own account: profile, notification channels, data export, deletion, and the project the dashboard opens on. For a session or an agent acting for the person, never an API key. De'
  name: sendly-now Account API
  slug: sendly-now-account-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: Aggregate sending and engagement metrics. Every read is bounded to a window of at most 90 days and cached for 15 minutes.
  name: sendly-now Analytics API
  slug: sendly-now-analytics-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: Project-scoped sending/API credentials. All four operations are documented; minting and rotation answer with a one-time reveal link rather than the secret, so a delegated caller never receives a key i
  name: sendly-now API Keys API
  slug: sendly-now-api-keys-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: The project's plan, its metered Stripe subscription, and the two Stripe-hosted pages (Checkout and the billing portal). An agent gets a single-use `/go/` link to a hosted page rather than its URL.
  name: sendly-now Billing API
  slug: sendly-now-billing-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: Bulk sends to a list, segment, or filtered audience. Served by the `/api/v1` surface (bare payloads, RFC 9457 errors).
  name: sendly-now Campaigns API
  slug: sendly-now-campaigns-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: 'Drop-in endpoints for the Resend, SendGrid, Postmark, Mailgun and Plunk send APIs, so an existing integration can switch by changing its base URL and key. They are NOT the native API: each speaks its '
  name: sendly-now Compatibility API
  slug: sendly-now-compatibility-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: 'The services a project or a person is connected to: the project''s Slack workspace, the domains whose DNS DoDomain manages, and the AI apps connected to a person''s account. A connection starts in the p'
  name: sendly-now Connections API
  slug: sendly-now-connections-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: Manage subscribers and per-contact custom data.
  name: sendly-now Contacts API
  slug: sendly-now-contacts-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: 'Why mail from one of your domains is or is not arriving: DNS identity, recent delivery outcomes, and one recipient''s suppression state, composed into findings.'
  name: sendly-now Deliverability API
  slug: sendly-now-deliverability-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: Register sending domains and manage SES verification.
  name: sendly-now Domains API
  slug: sendly-now-domains-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: Send transactional email and inspect deliveries.
  name: sendly-now Emails API
  slug: sendly-now-emails-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: Track custom contact events from your application.
  name: sendly-now Events API
  slug: sendly-now-events-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: Self-serve list membership. These two endpoints accept sending-only keys so they can back a public subscribe/unsubscribe form; list management itself is dashboard-only.
  name: sendly-now Lists API
  slug: sendly-now-lists-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: Real receiving mailboxes on your verified domains. Creating one changes how that domain's mail is routed; the messages a mailbox receives are not part of this API.
  name: sendly-now Mailboxes API
  slug: sendly-now-mailboxes-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: 'A project''s members and their roles. A project is the team: a member is added by the email of an existing Sendly account and joins at once, so there are no pending invitations. For a session or an age'
  name: sendly-now Members API
  slug: sendly-now-members-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: 'The organizations a person belongs to, each a group of projects: their overview and the merged inbox across their mailboxes. An organization never widens project access; every figure covers only the p'
  name: sendly-now Organizations API
  slug: sendly-now-organizations-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: The project a credential is scoped to, and creating new ones. Configuring an existing project stays a dashboard action.
  name: sendly-now Projects API
  slug: sendly-now-projects-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: Saved audiences — a `DYNAMIC` filter re-evaluated on read, or a `STATIC` membership list. Served by the `/api/v1` surface (bare payloads, RFC 9457 errors).
  name: sendly-now Segments API
  slug: sendly-now-segments-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: Write to Sendly's support team and list what was written, and appeal a project's sending suspension. A ticket reaches the same inbox as the dashboard's support form.
  name: sendly-now Support API
  slug: sendly-now-support-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: Project-scoped suppression list. Hard bounces and complaints land here automatically.
  name: sendly-now Suppression API
  slug: sendly-now-suppression-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: Reusable email templates referenced by send operations.
  name: sendly-now Templates API
  slug: sendly-now-templates-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: 'The subjects you mail about, and what each contact has said about them. A topic answer is a standing decision rather than an audience filter: it applies whatever audience a campaign selects, so it can'
  name: sendly-now Topics API
  slug: sendly-now-topics-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: Current email usage against the monthly and daily limits the platform enforces.
  name: sendly-now Usage API
  slug: sendly-now-usage-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: 'Bulk email validation, billed per address: a bounded synchronous batch, and background runs over a whole list. Distinct from `Verify`, which is the one open, unauthenticated, single-address endpoint t'
  name: sendly-now Validation API
  slug: sendly-now-validation-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: Open email-validation endpoint (no auth required). Used by the marketing-site verifier.
  name: sendly-now Verify API
  slug: sendly-now-verify-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: User-managed outbound webhooks for email and contact events.
  name: sendly-now Webhooks API
  slug: sendly-now-webhooks-api
- baseURL: https://api.sendly.now
  baseurl_source: declared
  description: Event-triggered automations and the contact runs through them. Served by the `/api/v1` surface (bare payloads, RFC 9457 errors).
  name: sendly-now Workflows API
  slug: sendly-now-workflows-api
artifact_total: 47
asyncapis:
- description: ''
  name: Sendly Now Webhooks
  slug: sendly-now-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/sendly-now/agentic-access/sendly-now-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sendly-now-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/sendly-now/plans/sendly-now-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sendly-now-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/sendly-now/rules/sendly-now-rules.yml
  title: ''
  type: Spectral
  url: rules/sendly-now-rules.yml
- group: design
  href: https://artifacts.apis.io/sendly-now/json-ld/sendly-now-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sendly-now-context.jsonld
- group: design
  href: https://artifacts.apis.io/sendly-now/vocabulary/sendly-now-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sendly-now-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sendly-now/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sendly-now/asyncapi/sendly-now-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sendly-now-webhooks.yml
- group: design
  href: https://artifacts.apis.io/sendly-now/data-model/sendly-now-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sendly-now-data-model.yml
- group: design
  href: https://artifacts.apis.io/sendly-now/conventions/sendly-now-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/sendly-now-conventions.yml
- group: design
  href: https://artifacts.apis.io/sendly-now/conventions/sendly-now-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sendly-now-conventions.yml
- group: auth
  href: https://artifacts.apis.io/sendly-now/security/sendly-now-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/sendly-now-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sendly-now/authentication/sendly-now-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sendly-now-authentication.yml
- group: design
  href: https://artifacts.apis.io/sendly-now/errors/sendly-now-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sendly-now-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sendly-now/conformance/sendly-now-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sendly-now-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sendly-now/llms/sendly-now-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sendly-now-llms.txt
- group: auth
  href: https://artifacts.apis.io/sendly-now/well-known/sendly-now-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sendly-now-security.txt
- group: auth
  href: https://artifacts.apis.io/sendly-now/well-known/sendly-now-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sendly-now-chatgpt-security.txt
- group: auth
  href: https://artifacts.apis.io/sendly-now/well-known/sendly-now-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sendly-now-app-security.txt
- group: auth
  href: https://artifacts.apis.io/sendly-now/well-known/sendly-now-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sendly-now-api-security.txt
- group: agent
  href: https://artifacts.apis.io/sendly-now/well-known/sendly-now-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sendly-now-well-known.yml
- group: other
  href: https://artifacts.apis.io/sendly-now/hosts/sendly-now-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sendly-now-hosts.yml
- group: other
  href: https://artifacts.apis.io/sendly-now/vendors/sendly-now-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sendly-now-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://sendly.now/trust
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sendly.now/
- group: start
  title: ''
  type: Login
  url: https://app.sendly.now/auth/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DevinoSolutions
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sendly.now\\\
- group: docs
  title: ''
  type: APIReference
  url: https://sendly.now/changelog
- group: auth
  href: https://artifacts.apis.io/sendly-now/scopes/sendly-now-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sendly-now-scopes.yml
- group: auth
  href: https://artifacts.apis.io/sendly-now/security/sendly-now-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sendly-now-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sendly-now/security/sendly-now-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sendly-now-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sendly.now/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sendly.now/
- group: commercial
  title: ''
  type: Pricing
  url: https://sendly.now/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sendly.now/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sendly.now/privacy
- group: operate
  title: ''
  type: Support
  url: https://app.sendly.now/support
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://sendly.now/openapi.json
  - status: null
    url: https://docs.sendly.now/openapi.json
  - status: 401
    url: https://api.sendly.now/api/mcp
  - status: 401
    url: https://app.sendly.now/api/mcp
  - status: 200
    url: https://sendly.now/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Sendly provides an Email API enhanced with AI capabilities for both transactional and marketing communications. It offers features such as scoped API keys, phishing screening, visual workflow builders, and integrations with Claude AI. Developers can send emails, manage campaigns, and verify domains through a unified API platform.
image: https://sendly.now/og-image.png
json_schemas:
- name: ComposeMailboxMessage
  property_count: 6
  slug: sendly-now-compose-mailbox-message
- name: DomainLogoReadinessV1
  property_count: 5
  slug: sendly-now-domain-logo-readiness-v1
- name: Domain
  property_count: 19
  slug: sendly-now-domain
- name: MailboxConversationReplyBody
  property_count: 2
  slug: sendly-now-mailbox-conversation-reply-body
- name: SendEmail
  property_count: 15
  slug: sendly-now-send-email
- name: SendEmailV1
  property_count: 15
  slug: sendly-now-send-email-v1
jsonld:
- class_count: 120
  name: Sendly Now Context
  property_count: 246
  slug: sendly-now-context
layout: provider
modified: '2026-10-31'
name: sendly-now
nav: Providers
network: true
overview: 'sendly-now publishes 27 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Analytics API, API Keys API, and 24 more. Tagged areas include Email, Transactional Email, Marketing Campaigns, Workflow Automation, and AI Integration.


  The sendly-now catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  sendly-now''s developer surface includes authentication, API reference, documentation, pricing, support, and 32 more developer resources.'
plans:
- name: Sendly Now Plans Pricing
  plan_count: 2
  slug: sendly-now-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: sendly-now API Rules
  rule_count: 18
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 4
  slug: sendly-now-rules
scopes:
- name: Sendly Now Scopes
  scope_count: 50
  slug: sendly-now-scopes
  summary_line: 50 scopes · authorizationCode
score:
  band: developing
  composite: 50.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 73.7
    developer_ergonomics: 29.2
    discoverability: 66.1
    operational_transparency: 28.9
  previous_composite: 61.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: derived
    skills: derived
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
screenshot: https://apis.io/screenshots/sendly-now/sendly-now-2026-11-03T143027.png
security:
- kind: authentication
  name: Sendly Now Authentication
  slug: sendly-now-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sendly Now Domain Security
  slug: sendly-now-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sendly Now Vulnerability Disclosure
  slug: sendly-now-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: sendly-now-billing-summary
  slug: sendly-now-billing-summary
- name: sendly-now-create-and-retrieve-contact
  slug: sendly-now-create-and-retrieve-contact
- name: sendly-now-create-configure-webhook
  slug: sendly-now-create-configure-webhook
- name: sendly-now-export-account-data
  slug: sendly-now-export-account-data
- name: sendly-now-org-overview
  slug: sendly-now-org-overview
slug: sendly-now
tags:
- Email
- Transactional Email
- Marketing Campaigns
- Workflow Automation
- AI Integration
- Developer Platform
website: https://sendly.now/
---
