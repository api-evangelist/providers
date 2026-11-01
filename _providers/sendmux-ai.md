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
    error_semantics: verified
    event_surface_described: unknown
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
  score: 77.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 50
  human_in_the_loop: 2
  name: Sendmux Ai Agentic Access
  operation_count: 119
  slug: sendmux-ai-agentic-access
  summary_line: 119 operations · 50 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.sendmux.ai/api/v1
  baseurl_source: declared
  description: The Billing API from sendmux-ai — 3 operation(s) for billing.
  name: sendmux-ai Billing API
  slug: sendmux-ai-billing-api
- baseURL: https://app.sendmux.ai/api/v1
  baseurl_source: declared
  description: The Connection API from sendmux-ai — 1 operation(s) for connection.
  name: sendmux-ai Connection API
  slug: sendmux-ai-connection-api
- baseURL: https://app.sendmux.ai/api/v1
  baseurl_source: declared
  description: The Domain Filters API from sendmux-ai — 1 operation(s) for domain filters.
  name: sendmux-ai Domain Filters API
  slug: sendmux-ai-domain-filters-api
- baseURL: https://app.sendmux.ai/api/v1
  baseurl_source: declared
  description: The Domains API from sendmux-ai — 4 operation(s) for domains.
  name: sendmux-ai Domains API
  slug: sendmux-ai-domains-api
- baseURL: https://app.sendmux.ai/api/v1
  baseurl_source: declared
  description: The Emails API from sendmux-ai — 3 operation(s) for emails.
  name: sendmux-ai Emails API
  slug: sendmux-ai-emails-api
- baseURL: https://app.sendmux.ai/api/v1
  baseurl_source: declared
  description: The Inboxes API from sendmux-ai — 2 operation(s) for inboxes.
  name: sendmux-ai Inboxes API
  slug: sendmux-ai-inboxes-api
- baseURL: https://app.sendmux.ai/api/v1
  baseurl_source: declared
  description: The Mailbox API API from sendmux-ai — 48 operation(s) for mailbox api.
  name: sendmux-ai Mailbox API
  slug: sendmux-ai-mailbox-api-api
- baseURL: https://app.sendmux.ai/api/v1
  baseurl_source: declared
  description: The Mailbox Filters API from sendmux-ai — 1 operation(s) for mailbox filters.
  name: sendmux-ai Mailbox Filters API
  slug: sendmux-ai-mailbox-filters-api
- baseURL: https://app.sendmux.ai/api/v1
  baseurl_source: declared
  description: The Mailboxes API from sendmux-ai — 9 operation(s) for mailboxes.
  name: sendmux-ai Mailboxes API
  slug: sendmux-ai-mailboxes-api
- baseURL: https://app.sendmux.ai/api/v1
  baseurl_source: declared
  description: The Sending accounts API from sendmux-ai — 11 operation(s) for sending accounts.
  name: sendmux-ai Sending accounts API
  slug: sendmux-ai-sending-accounts-api
- baseURL: https://app.sendmux.ai/api/v1
  baseurl_source: declared
  description: The Webhooks API from sendmux-ai — 6 operation(s) for webhooks.
  name: sendmux-ai Webhooks API
  slug: sendmux-ai-webhooks-api
artifact_total: 30
asyncapis:
- description: ''
  name: Sendmux Ai Webhooks
  slug: sendmux-ai-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/sendmux-ai/agentic-access/sendmux-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sendmux-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/sendmux-ai/plans/sendmux-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sendmux-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/sendmux-ai/rules/sendmux-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/sendmux-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/sendmux-ai/json-ld/sendmux-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sendmux-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/sendmux-ai/vocabulary/sendmux-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sendmux-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sendmux-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sendmux-ai/asyncapi/sendmux-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sendmux-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/sendmux-ai/data-model/sendmux-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sendmux-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/sendmux-ai/cli/sendmux-ai-cli.yml
  title: ''
  type: CLI
  url: cli/sendmux-ai-cli.yml
- group: design
  href: https://artifacts.apis.io/sendmux-ai/conventions/sendmux-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/sendmux-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/sendmux-ai/conventions/sendmux-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sendmux-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/sendmux-ai/authentication/sendmux-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sendmux-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/sendmux-ai/errors/sendmux-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sendmux-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sendmux-ai/conformance/sendmux-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sendmux-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sendmux-ai/llms/sendmux-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sendmux-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/sendmux-ai/a2a/sendmux-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/sendmux-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/sendmux-ai/well-known/sendmux-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sendmux-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/sendmux-ai/hosts/sendmux-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sendmux-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/sendmux-ai/vendors/sendmux-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sendmux-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/sendmux-ai/packages/sendmux-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/sendmux-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/sendmux-ai/packages/sendmux-ai-packages.yml
  title: ''
  type: Packages
  url: packages/sendmux-ai-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sendmux.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://sendmux.ai/docs/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.youragent.app/sendmux&quot;</span
- group: auth
  href: https://artifacts.apis.io/sendmux-ai/scopes/sendmux-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sendmux-ai-scopes.yml
- group: auth
  href: https://artifacts.apis.io/sendmux-ai/security/sendmux-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sendmux-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sendmux.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://sendmux.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://sendmux.ai/docs/api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://sendmux.ai/docs/getting-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://sendmux.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://sendmux.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sendmux
- group: commercial
  title: ''
  type: Pricing
  url: https://sendmux.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.sendmux.ai/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sendmux.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sendmux.ai/privacy/
- group: build
  title: ''
  type: Postman
  url: https://sendmux.ai/docs/developer-tools/postman
created: '2026-10-31'
description: Sendmux AI provides an Email API designed for AI agents, offering unified endpoints to send and receive emails, manage calendars, and store files. The platform includes inboxes for agents, developer tools, SDKs, and a CLI, enabling seamless integration of email capabilities into AI-driven applications across various use cases such as customer support, sales outreach, and scheduling.
image: https://sendmux.ai/og-image.jpg
json_schemas:
- name: CreateCalendarEventBody
  property_count: 7
  slug: sendmux-ai-create-calendar-event-body
- name: CreateMailboxDraft
  property_count: 12
  slug: sendmux-ai-create-mailbox-draft
- name: ProviderCreateBody
  property_count: 14
  slug: sendmux-ai-provider-create-body
- name: ProviderUpdateBody
  property_count: 14
  slug: sendmux-ai-provider-update-body
- name: SendMailboxMessageBody
  property_count: 10
  slug: sendmux-ai-send-mailbox-message-body
- name: UpdateMailboxDraft
  property_count: 11
  slug: sendmux-ai-update-mailbox-draft
jsonld:
- class_count: 120
  name: Sendmux Ai Context
  property_count: 319
  slug: sendmux-ai-context
layout: provider
modified: '2026-10-31'
name: sendmux-ai
nav: Providers
network: true
overview: 'sendmux-ai publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Connection API, Domain Filters API, and 8 more. Tagged areas include Company, Email, AI, Agents, and Integration.


  The sendmux-ai catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  sendmux-ai''s developer surface includes CLI, authentication, changelog, documentation, API reference, getting-started guide, support, and 31 more developer resources.'
plans:
- name: Sendmux Ai Plans Pricing
  plan_count: 3
  slug: sendmux-ai-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: sendmux-ai API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: sendmux-ai-rules
scopes:
- name: Sendmux Ai Scopes
  scope_count: 52
  slug: sendmux-ai-scopes
  summary_line: 52 scopes · authorizationCode
score:
  band: exemplar
  composite: 72.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 68.9
    developer_ergonomics: 82.6
    discoverability: 66.1
    operational_transparency: 44.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sendmux Ai Authentication
  slug: sendmux-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Sendmux Ai Domain Security
  slug: sendmux-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 5
skills:
- name: sendmux-ai-create-and-activate-sending-account
  slug: sendmux-ai-create-and-activate-sending-account
- name: sendmux-ai-create-and-send-draft-with-attachment
  slug: sendmux-ai-create-and-send-draft-with-attachment
- name: sendmux-ai-create-mailbox
  slug: sendmux-ai-create-mailbox
- name: sendmux-ai-manage-domain
  slug: sendmux-ai-manage-domain
- name: sendmux-ai-manage-webhooks
  slug: sendmux-ai-manage-webhooks
slug: sendmux-ai
tags:
- Company
- Email
- AI
- Agents
- Integration
website: https://sendmux.ai/
---
