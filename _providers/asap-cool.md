---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
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
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 285
  human_in_the_loop: 15
  name: Asap Cool Agentic Access
  operation_count: 477
  slug: asap-cool-agentic-access
  summary_line: 477 operations · 285 acting · 15 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'Multi-tenant agents platform: agent CRUD plus per-agent knowledge base (Q&A, documents).'
  name: ASAP Agents API
  slug: asap-cool-agents-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: Programmatic credentials for the public API.
  name: ASAP API Keys API
  slug: asap-cool-api-keys-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: Per-org module activation and availability.
  name: ASAP Apps API
  slug: asap-cool-apps-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: Authentication, sessions, OAuth, TOTP, password reset.
  name: ASAP Auth API
  slug: asap-cool-auth-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: Automation proposals raised by the system, their journal, the autonomy settings per action kind and the org's safety state. Behind the `automation_proposals` flag; the settings, the global pause and t
  name: ASAP Automation API
  slug: asap-cool-automation-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: Stripe checkout, subscription state, customer portal, and webhook receiver.
  name: ASAP Billing API
  slug: asap-cool-billing-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'Agenda: native events (recurrence, attendees, invitations) and the read-only projection of every dated deadline of the suite.'
  name: ASAP Calendar API
  slug: asap-cool-calendar-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'Address book: clients and prospects, tenant-scoped.'
  name: ASAP Contacts API
  slug: asap-cool-contacts-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'Internal invoice copilot: streaming turns (SSE) with auto-executed reads/drafts and confirmation-gated regulated actions.'
  name: ASAP Copilot API
  slug: asap-cool-copilot-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'CRM substrate: deals, tasks, the day''s work queue, the append-only contact activity log and the merged cross-module contact timeline.'
  name: ASAP CRM API
  slug: asap-cool-crm-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'Outbound email journal: delivery history and the Resend delivery-event webhook.'
  name: ASAP Emails API
  slug: asap-cool-emails-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'Purchases: what the org paid, with VAT per rate. A draft counts for nothing until confirmed.'
  name: ASAP Expenses API
  slug: asap-cool-expenses-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'Media library: files and folders, tenant-scoped.'
  name: ASAP Files API
  slug: asap-cool-files-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'Micro-entrepreneur fiscal estimates: social-charge provision, VAT-franchise thresholds, declaration deadline (decision support, never an official declaration).'
  name: ASAP Fiscal API
  slug: asap-cool-fiscal-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: Feature flags evaluated for the active org.
  name: ASAP Flags API
  slug: asap-cool-flags-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'Unified inbox: WhatsApp and email channels, conversations, replies, attachments, and Meta''s webhook.'
  name: ASAP Inbox API
  slug: asap-cool-inbox-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'Quotes, invoices, credit notes and deposit invoices: draft CRUD, NF203 finalization, and per-org settings.'
  name: ASAP Invoice API
  slug: asap-cool-invoice-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: Web Push device subscriptions and the in-app notification feed.
  name: ASAP Notifications API
  slug: asap-cool-notifications-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: Organization-private MCP clients (session Admin/Owner only).
  name: ASAP OAUTH Clients API
  slug: asap-cool-oauth-clients-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: Inbound OAuth connections (connected apps) for the active org.
  name: ASAP OAUTH Grants API
  slug: asap-cool-oauth-grants-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: Organisations and memberships.
  name: ASAP Orgs API
  slug: asap-cool-orgs-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'Cold outreach prospection: campaign CRUD, sender pools, enrolment, reply intents, CNIL compliance, and sourcing.'
  name: ASAP Outreach API
  slug: asap-cool-outreach-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'Affiliation program: partner administration, the commission ledger, and monthly statements (read plus settle only — the ledger is fed exclusively by the accrual worker).'
  name: ASAP Partners API
  slug: asap-cool-partners-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'Payments hub reads: the connected account''s Stripe payouts (owner-only, read-only).'
  name: ASAP Payments API
  slug: asap-cool-payments-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'ASAP Payments connected account: platform-created Stripe account, embedded-component sessions and status (owner-only).'
  name: ASAP Payments Connect API
  slug: asap-cool-payments-connect-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'Cross-app search: one needle, results grouped by source, composed only from the apps the org can see.'
  name: ASAP Search API
  slug: asap-cool-search-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'User self-service: data export and account deletion.'
  name: ASAP Settings API
  slug: asap-cool-settings-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: 'Electronic signature (eIDAS simple): envelope CRUD, send, the session-less public signing flow, and the audit-trail proof.'
  name: ASAP Signature API
  slug: asap-cool-signature-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: The sourcing API from ASAP — 5 operation(s) for sourcing.
  name: ASAP Sourcing API
  slug: asap-cool-sourcing-api
- baseURL: https://api.asap.cool
  baseurl_source: declared
  description: Outbound signed webhook endpoints (subscriptions) for org events.
  name: ASAP Webhooks API
  slug: asap-cool-webhooks-api
artifact_total: 47
asyncapis:
- description: ''
  name: Asap Cool Webhooks
  slug: asap-cool-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/asap-cool/agentic-access/asap-cool-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/asap-cool-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/asap-cool/rate-limits/asap-cool-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/asap-cool-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/asap-cool/rules/asap-cool-rules.yml
  title: ''
  type: Spectral
  url: rules/asap-cool-rules.yml
- group: design
  href: https://artifacts.apis.io/asap-cool/json-ld/asap-cool-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/asap-cool-context.jsonld
- group: design
  href: https://artifacts.apis.io/asap-cool/vocabulary/asap-cool-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/asap-cool-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/asap-cool/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/asap-cool/asyncapi/asap-cool-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/asap-cool-webhooks.yml
- group: design
  href: https://artifacts.apis.io/asap-cool/data-model/asap-cool-data-model.yml
  title: ''
  type: DataModel
  url: data-model/asap-cool-data-model.yml
- group: design
  href: https://artifacts.apis.io/asap-cool/conventions/asap-cool-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/asap-cool-conventions.yml
- group: design
  href: https://artifacts.apis.io/asap-cool/conventions/asap-cool-conventions.yml
  title: ''
  type: Conventions
  url: conventions/asap-cool-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://asap.cool/fr/securite/#signaler-une-vulnerabilite
- group: auth
  href: https://artifacts.apis.io/asap-cool/authentication/asap-cool-authentication.yml
  title: ''
  type: Authentication
  url: authentication/asap-cool-authentication.yml
- group: operate
  href: https://artifacts.apis.io/asap-cool/lifecycle/asap-cool-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/asap-cool-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/asap-cool/lifecycle/asap-cool-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/asap-cool-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/asap-cool/errors/asap-cool-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/asap-cool-problem-types.yml
- group: design
  href: https://artifacts.apis.io/asap-cool/conformance/asap-cool-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asap-cool-conformance.yml
- group: agent
  href: https://artifacts.apis.io/asap-cool/llms/asap-cool-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asap-cool-llms.txt
- group: auth
  href: https://artifacts.apis.io/asap-cool/well-known/asap-cool-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/asap-cool-security.txt
- group: auth
  href: https://artifacts.apis.io/asap-cool/well-known/asap-cool-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/asap-cool-app-security.txt
- group: auth
  href: https://artifacts.apis.io/asap-cool/well-known/asap-cool-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/asap-cool-api-security.txt
- group: agent
  href: https://artifacts.apis.io/asap-cool/well-known/asap-cool-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asap-cool-well-known.yml
- group: other
  href: https://artifacts.apis.io/asap-cool/hosts/asap-cool-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asap-cool-hosts.yml
- group: other
  href: https://artifacts.apis.io/asap-cool/vendors/asap-cool-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asap-cool-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://asap.cool/fr/blog/
- group: auth
  href: https://artifacts.apis.io/asap-cool/security/asap-cool-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/asap-cool-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/asap-cool/security/asap-cool-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asap-cool-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asap.cool/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.asap.cool/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.asap.cool/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.asap.cool/guides/getting-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://asap.cool/fr/tarifs/
created: '2026-11-01'
description: ASAP provides an all‑in‑one management platform for freelancers, offering billing, electronic invoicing, electronic signature, client contacts, agenda scheduling, messaging via email and WhatsApp, AI‑driven assistance, and a suite of integrated apps under a single subscription. The service aims to streamline freelance business operations with modern tools and a public REST API for developers.
image: https://asap.cool/favicon.svg
json_schemas:
- name: CompanyProfileView
  property_count: 41
  slug: asap-cool-company-profile-view
- name: ContactView
  property_count: 32
  slug: asap-cool-contact-view
- name: DocumentView
  property_count: 47
  slug: asap-cool-document-view
- name: EnvelopeView
  property_count: 25
  slug: asap-cool-envelope-view
- name: InboundView
  property_count: 24
  slug: asap-cool-inbound-view
- name: UpdateCompanyProfileRequest
  property_count: 38
  slug: asap-cool-update-company-profile-request
jsonld:
- class_count: 120
  name: Asap Cool Context
  property_count: 386
  slug: asap-cool-context
layout: provider
modified: '2026-11-01'
name: ASAP
nav: Providers
network: true
overview: 'ASAP publishes 30 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, API Keys API, Apps API, and 27 more. Tagged areas include Freelance, Billing, CRM, and Productivity.


  The ASAP catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  ASAP''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, pricing, and 25 more developer resources.'
plans:
- name: Asap Cool Plans Pricing
  plan_count: 0
  slug: asap-cool-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Asap Cool Rate Limits
  slug: asap-cool-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: ASAP API Rules
  rule_count: 60
  severity_counts:
    error: 39
    hint: 0
    info: 2
    warn: 19
  slug: asap-cool-rules
scopes:
- name: Asap Cool Scopes
  scope_count: 0
  slug: asap-cool-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 66.8
    developer_ergonomics: 33.8
    discoverability: 57.1
    operational_transparency: 52.6
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Asap Cool Authentication
  slug: asap-cool-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Asap Cool Domain Security
  slug: asap-cool-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Asap Cool Vulnerability Disclosure
  slug: asap-cool-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: getting-started
  slug: asap-cool-getting-started
slug: asap-cool
tags:
- Freelance
- Billing
- CRM
- Productivity
website: https://asap.cool/
---
