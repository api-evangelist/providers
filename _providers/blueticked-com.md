---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 64.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 75
  human_in_the_loop: 2
  name: Blueticked Com Agentic Access
  operation_count: 140
  slug: blueticked-com-agentic-access
  summary_line: 140 operations · 75 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Operations for ai_agents.
  name: Blueticked AI Agents API
  slug: blueticked-com-ai-agents-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Operations for automations.
  name: Blueticked Automations API
  slug: blueticked-com-automations-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Operations for businesses.
  name: Blueticked Businesses API
  slug: blueticked-com-businesses-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Create and dispatch bulk campaigns to an audience.
  name: Blueticked Campaigns API
  slug: blueticked-com-campaigns-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Inspect connected channels and check WhatsApp readiness.
  name: Blueticked Channels API
  slug: blueticked-com-channels-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Operations for commerce.
  name: Blueticked Commerce API
  slug: blueticked-com-commerce-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Manage contacts, groups, segments and their custom fields.
  name: Blueticked Contacts API
  slug: blueticked-com-contacts-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Read and update the unified inbox.
  name: Blueticked Conversations API
  slug: blueticked-com-conversations-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Operations for conversions.
  name: Blueticked Conversions API
  slug: blueticked-com-conversions-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Fire an event that triggers your configured flows.
  name: Blueticked Events API
  slug: blueticked-com-events-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Manage and publish WhatsApp Flows (forms).
  name: Blueticked Flows API
  slug: blueticked-com-flows-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Operations for forms.
  name: Blueticked Forms API
  slug: blueticked-com-forms-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Manage outbound integrations and inspect their deliveries.
  name: Blueticked Integrations API
  slug: blueticked-com-integrations-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Operations for journeys.
  name: Blueticked Journeys API
  slug: blueticked-com-journeys-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Send messages across WhatsApp, SMS and email, and read delivery status.
  name: Blueticked Messages API
  slug: blueticked-com-messages-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Operations for sites.
  name: Blueticked Sites API
  slug: blueticked-com-sites-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Manage the opt-out / suppression list.
  name: Blueticked Suppression API
  slug: blueticked-com-suppression-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: 'Customer-shaped records on a contact (prescriptions, orders, bookings): read tables, add and move rows.'
  name: Blueticked Tables API
  slug: blueticked-com-tables-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Manage WhatsApp message templates.
  name: Blueticked Templates API
  slug: blueticked-com-templates-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: 'The work queue: raise, list and work tickets.'
  name: Blueticked Tickets API
  slug: blueticked-com-tickets-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Read the prepaid credit balance and ledger.
  name: Blueticked Wallet API
  slug: blueticked-com-wallet-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: 'Subscribe to and manage outbound event webhooks. Every delivery is a POST of a JSON envelope signed with the webhook''s secret: x-blueticked-signature is sha256=<hex HMAC-SHA256 of the raw body>, and x'
  name: Blueticked Webhooks API
  slug: blueticked-com-webhooks-api
- baseURL: https://app.blueticked.com
  baseurl_source: declared
  description: Operations for workspace.
  name: Blueticked Workspace API
  slug: blueticked-com-workspace-api
artifact_total: 35
asyncapis:
- description: ''
  name: Blueticked Com Webhooks
  slug: blueticked-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/blueticked-com/agentic-access/blueticked-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blueticked-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/blueticked-com/plans/blueticked-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blueticked-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/blueticked-com/rules/blueticked-com-rules.yml
  title: ''
  type: Spectral
  url: rules/blueticked-com-rules.yml
- group: design
  href: https://artifacts.apis.io/blueticked-com/json-ld/blueticked-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blueticked-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/blueticked-com/vocabulary/blueticked-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blueticked-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/blueticked-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/blueticked-com/asyncapi/blueticked-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/blueticked-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/blueticked-com/data-model/blueticked-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blueticked-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/blueticked-com/changelog/blueticked-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/blueticked-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/blueticked-com/conventions/blueticked-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/blueticked-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/blueticked-com/conventions/blueticked-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/blueticked-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/blueticked-com/authentication/blueticked-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blueticked-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/blueticked-com/errors/blueticked-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blueticked-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blueticked-com/conformance/blueticked-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blueticked-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blueticked-com/llms/blueticked-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blueticked-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/blueticked-com/well-known/blueticked-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blueticked-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/blueticked-com/hosts/blueticked-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blueticked-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/blueticked-com/vendors/blueticked-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blueticked-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blueticked.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.blueticked.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blueticked.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blueticked.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.blueticked.com/sign-in
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.blueticked.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.blueticked.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.blueticked.com/docs/changelog
- group: auth
  href: https://artifacts.apis.io/blueticked-com/security/blueticked-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blueticked-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blueticked.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://app.blueticked.com/api/mcp
  - status: 200
    url: https://blueticked.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Blueticked provides WhatsApp, SMS and email communication services for South African businesses, offering campaigns, Flow Studio automation, AI agents, and integrated website/shop solutions. Built in South Africa, priced in rand, and POPIA-aligned, it operates under Sinosa Trading (Pty) Ltd, aiming to keep no customer left on grey.
image: https://blueticked.com/og.png
jsonld:
- class_count: 1
  name: Blueticked Com Context
  property_count: 3
  slug: blueticked-com-context
layout: provider
modified: '2026-11-02'
name: Blueticked
nav: Providers
network: true
overview: 'Blueticked publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI Agents API, Automations API, Businesses API, and 20 more. Tagged areas include Communications, South Africa, WhatsApp, SMS, and Email.


  The Blueticked catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Blueticked''s developer surface includes changelog, authentication, support, pricing, getting-started guide, API reference, and 22 more developer resources.'
plans:
- name: Blueticked Com Plans Pricing
  plan_count: 6
  slug: blueticked-com-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 114
  extends:
  - spectral:oas
  name: Blueticked API Rules
  rule_count: 73
  severity_counts:
    error: 67
    hint: 0
    info: 2
    warn: 4
  slug: blueticked-com-rules
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 59.8
    catalog_earned_first_party: 12.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 64.6
    developer_ergonomics: 30.4
    discoverability: 66.1
    operational_transparency: 23.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 17.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blueticked Com Authentication
  slug: blueticked-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Blueticked Com Domain Security
  slug: blueticked-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: blueticked-com-create-and-test-webhook
  slug: blueticked-com-create-and-test-webhook
- name: blueticked-com-create-contact-workflow
  slug: blueticked-com-create-contact-workflow
- name: blueticked-com-create-integration-with-action
  slug: blueticked-com-create-integration-with-action
- name: blueticked-com-create-product-with-image
  slug: blueticked-com-create-product-with-image
- name: blueticked-com-onboard-and-issue-credential
  slug: blueticked-com-onboard-and-issue-credential
slug: blueticked-com
tags:
- Communications
- South Africa
- WhatsApp
- SMS
- Email
- Automation
website: https://blueticked.com/
---
