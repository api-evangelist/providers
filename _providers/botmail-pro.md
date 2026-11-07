---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://botmail.pro
  baseurl_source: declared
  description: The signed-in account, identities, usage, deletion and export.
  name: Botmail Account API
  slug: botmail-pro-account-api
- baseURL: https://botmail.pro
  baseurl_source: declared
  description: Plans, checkout and the billing portal. Changes need a signed-in human.
  name: Botmail Billing API
  slug: botmail-pro-billing-api
- baseURL: https://botmail.pro
  baseurl_source: declared
  description: Agent claim flow. 1) `GET /v1/claim/challenge` and solve the proof of work. 2) `POST /v1/claim` → address + pending key + `claim_url`. 3) Give the human `claim_url` (or `POST /v1/claim/notify`). 4) Po
  name: Botmail Claim API
  slug: botmail-pro-claim-api
- baseURL: https://botmail.pro
  baseurl_source: declared
  description: Per-mailbox event stream (long-poll).
  name: Botmail Events API
  slug: botmail-pro-events-api
- baseURL: https://botmail.pro
  baseurl_source: declared
  description: API keys. Secrets are shown once at creation.
  name: Botmail Keys API
  slug: botmail-pro-keys-api
- baseURL: https://botmail.pro
  baseurl_source: declared
  description: Threads, messages, attachments and labels.
  name: Botmail Mail API
  slug: botmail-pro-mail-api
- baseURL: https://botmail.pro
  baseurl_source: declared
  description: Mailboxes and name availability.
  name: Botmail Mailboxes API
  slug: botmail-pro-mailboxes-api
- baseURL: https://botmail.pro
  baseurl_source: declared
  description: This document.
  name: Botmail Meta API
  slug: botmail-pro-meta-api
- baseURL: https://botmail.pro
  baseurl_source: declared
  description: Send, reply and forward. Sends are queued (202) and classified before delivery; watch `message.status` events for the outcome. Pass an `Idempotency-Key` header (or `idempotency_key` in the body, which
  name: Botmail Send API
  slug: botmail-pro-send-api
- baseURL: https://botmail.pro
  baseurl_source: declared
  description: 'Push events to your HTTPS endpoint. **Delivery**: `POST` with a JSON `WebhookEvent` body (`{id: "evt_<seq>", type, mailbox_id, thread_id, message_id, created_at, data}`). **Headers**: - `Botmail-Event'
  name: Botmail Webhooks API
  slug: botmail-pro-webhooks-api
artifact_total: 15
asyncapis:
- description: ''
  name: Botmail Pro Webhooks
  slug: botmail-pro-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/botmail-pro/plans/botmail-pro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/botmail-pro-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/botmail-pro/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/botmail-pro/asyncapi/botmail-pro-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/botmail-pro-webhooks.yml
- group: design
  href: https://artifacts.apis.io/botmail-pro/data-model/botmail-pro-data-model.yml
  title: ''
  type: DataModel
  url: data-model/botmail-pro-data-model.yml
- group: build
  href: https://artifacts.apis.io/botmail-pro/cli/botmail-pro-cli.yml
  title: ''
  type: CLI
  url: cli/botmail-pro-cli.yml
- group: operate
  href: https://artifacts.apis.io/botmail-pro/changelog/botmail-pro-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/botmail-pro-changelog.yml
- group: auth
  href: https://artifacts.apis.io/botmail-pro/authentication/botmail-pro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/botmail-pro-authentication.yml
- group: design
  href: https://artifacts.apis.io/botmail-pro/errors/botmail-pro-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/botmail-pro-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/botmail-pro/llms/botmail-pro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/botmail-pro-llms.txt
- group: agent
  href: https://artifacts.apis.io/botmail-pro/well-known/botmail-pro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/botmail-pro-well-known.yml
- group: other
  href: https://artifacts.apis.io/botmail-pro/hosts/botmail-pro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botmail-pro-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://botmail.pro/changelog
- group: auth
  href: https://artifacts.apis.io/botmail-pro/security/botmail-pro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botmail-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botmail.pro/
- group: docs
  title: ''
  type: Documentation
  url: https://botmail.pro/docs
- group: docs
  title: ''
  type: APIReference
  url: https://botmail.pro/v1/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://botmail.pro/skill.md
- group: commercial
  title: ''
  type: Pricing
  url: https://botmail.pro/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://botmail.pro/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://botmail.pro/privacy
- group: operate
  title: ''
  type: Support
  url: https://botmail.pro/contact
created: '2026-11-02'
description: Botmail provides AI agents with unique email addresses, enabling them to send, receive, and reply via a simple REST API or MCP. Users claim an address in one step, approve via a single click, and can manage mailboxes across free and paid plans. The service offers tiered pricing, storage limits, and daily send caps, with a focus on security and spam protection.
image: https://botmail.pro/static/og.jpg
layout: provider
modified: '2026-11-02'
name: Botmail
nav: Providers
network: true
overview: 'Botmail publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Billing API, Claim API, and 7 more. Tagged areas include Artificial Intelligence, Email, Messaging, Automation, and Botmail.


  The Botmail catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Botmail''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, pricing, and 14 more developer resources.'
plans:
- name: Botmail Pro Plans Pricing
  plan_count: 6
  slug: botmail-pro-plans-pricing
random_paper: 22
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 56.6
    developer_ergonomics: 37.5
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Botmail Pro Authentication
  slug: botmail-pro-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Botmail Pro Domain Security
  slug: botmail-pro-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: get-email
  slug: botmail-pro-get-email
slug: botmail-pro
tags:
- Artificial Intelligence
- Email
- Messaging
- Automation
- Botmail
website: https://botmail.pro/
---
