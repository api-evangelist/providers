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
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 57.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 54
  human_in_the_loop: 4
  name: Groundmail Dev Agentic Access
  operation_count: 91
  slug: groundmail-dev-agentic-access
  summary_line: 91 operations · 54 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: Create and manage event-driven transactional automations
  name: groundmail-dev Automations API
  slug: groundmail-dev-automations-api
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: Best-effort metrics computed from stored email events
  name: groundmail-dev Deliverability API
  slug: groundmail-dev-deliverability-api
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: DMARC monitoring per domain (aggregate reports, sending sources, enforcement readiness)
  name: groundmail-dev Dmarc API
  slug: groundmail-dev-dmarc-api
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: The Domains API from groundmail-dev — 2 operation(s) for domains.
  name: groundmail-dev Domains API
  slug: groundmail-dev-domains-api
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: The Emails API from groundmail-dev — 5 operation(s) for emails.
  name: groundmail-dev Emails API
  slug: groundmail-dev-emails-api
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: Custom events that trigger transactional automations
  name: groundmail-dev Events API
  slug: groundmail-dev-events-api
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: Receive domains, inbound ingestion, and received email retrieval
  name: groundmail-dev Inbound API
  slug: groundmail-dev-inbound-api
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: The Integrations API from groundmail-dev — 3 operation(s) for integrations.
  name: groundmail-dev Integrations API
  slug: groundmail-dev-integrations-api
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: 'Beta. Import templates, suppressions, sending domains and webhooks from SendGrid, Postmark, Mailgun, Resend or Amazon SES. The provider key (Amazon SES: access key and secret) is used for the request '
  name: groundmail-dev Migrations API
  slug: groundmail-dev-migrations-api
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: OAuth 2.0 Device Authorization Grant (RFC 8628) for the CLI and agents, the authorization code grant with PKCE for the hosted MCP server, dynamic client registration (RFC 7591), token refresh with rot
  name: groundmail-dev OAuth API
  slug: groundmail-dev-oauth-api
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: The SmtpCredentials API from groundmail-dev — 2 operation(s) for smtpcredentials.
  name: groundmail-dev Smtp Credentials API
  slug: groundmail-dev-smtpcredentials-api
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: Account-level recipient suppressions (bounce/complaint/manual)
  name: groundmail-dev Suppressions API
  slug: groundmail-dev-suppressions-api
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: Email templates with `{{variable}}` interpolation
  name: groundmail-dev Templates API
  slug: groundmail-dev-templates-api
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: Your own customers inside one Groundmail account, each with its own domains, suppression list, stats, sending ramp and pause switch. Included on Scale and Dedicated.
  name: groundmail-dev Tenants API
  slug: groundmail-dev-tenants-api
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: A test domain per team. Mail sent to it from any email provider is caught and never delivered, so tests can wait for an email and read its code and links.
  name: groundmail-dev Test inbox API
  slug: groundmail-dev-test-inbox-api
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: Groundmail validation — check an address before you accept or send to it
  name: groundmail-dev Validation API
  slug: groundmail-dev-validation-api
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: The Webhooks API from groundmail-dev — 2 operation(s) for webhooks.
  name: groundmail-dev Webhooks API
  slug: groundmail-dev-webhooks-api
- baseURL: https://api.groundmail.dev
  baseurl_source: declared
  description: Manage API keys (list, create, revoke)
  name: groundmail-dev API Keys API
  slug: groundmail-dev-api-keys-api
artifact_total: 37
asyncapis:
- description: ''
  name: Groundmail Dev Webhooks
  slug: groundmail-dev-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/groundmail-dev/agentic-access/groundmail-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/groundmail-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/groundmail-dev/plans/groundmail-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/groundmail-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/groundmail-dev/rules/groundmail-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/groundmail-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/groundmail-dev/json-ld/groundmail-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/groundmail-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/groundmail-dev/vocabulary/groundmail-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/groundmail-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/groundmail-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/groundmail-dev/asyncapi/groundmail-dev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/groundmail-dev-webhooks.yml
- group: design
  href: https://artifacts.apis.io/groundmail-dev/data-model/groundmail-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/groundmail-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/groundmail-dev/cli/groundmail-dev-cli.yml
  title: ''
  type: CLI
  url: cli/groundmail-dev-cli.yml
- group: design
  href: https://artifacts.apis.io/groundmail-dev/conventions/groundmail-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/groundmail-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/groundmail-dev/conventions/groundmail-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/groundmail-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/groundmail-dev/security/groundmail-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/groundmail-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/groundmail-dev/authentication/groundmail-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/groundmail-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/groundmail-dev/errors/groundmail-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/groundmail-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/groundmail-dev/conformance/groundmail-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/groundmail-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/groundmail-dev/llms/groundmail-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/groundmail-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/groundmail-dev/well-known/groundmail-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/groundmail-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/groundmail-dev/well-known/groundmail-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/groundmail-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/groundmail-dev/hosts/groundmail-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/groundmail-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/groundmail-dev/vendors/groundmail-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/groundmail-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://groundmail.dev/legal/terms/
- group: operate
  title: ''
  type: Support
  url: https://groundmail.dev/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.groundmail.dev
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://groundmail.dev/legal/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://groundmail.dev/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://groundmail.dev/press/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Groundmail
- group: operate
  title: ''
  type: ChangeLog
  url: https://groundmail.dev/changelog/
- group: company
  title: ''
  type: Blog
  url: https://groundmail.dev/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.groundmail.dev/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.groundmail.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.groundmail.dev.\n-
- group: docs
  title: ''
  type: APIReference
  url: https://docs.groundmail.dev/api-explorer
- group: auth
  href: https://artifacts.apis.io/groundmail-dev/security/groundmail-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/groundmail-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/groundmail-dev/security/groundmail-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/groundmail-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://groundmail.dev/
created: '2026-10-30'
description: Groundmail provides a transactional email API and SMTP service designed for developers to send password resets, receipts, alerts, and other automated messages. The platform separates transactional mail from marketing campaigns, offering dedicated IPs, automation features, and a free tier of 3,000 emails per month. It aims to simplify email integration for applications while ensuring deliverability and compliance.
image: https://groundmail.dev/opengraph-image
json_schemas:
- name: CreateMigrationRequest
  property_count: 11
  slug: groundmail-dev-create-migration-request
- name: Domain
  property_count: 16
  slug: groundmail-dev-domain
- name: EmailListItem
  property_count: 25
  slug: groundmail-dev-email-list-item
- name: EmailWebhookEventPayload
  property_count: 3
  slug: groundmail-dev-email-webhook-event-payload
- name: RemoteApplyDnsCredentials
  property_count: 17
  slug: groundmail-dev-remote-apply-dns-credentials
- name: SendEmailRequest
  property_count: 24
  slug: groundmail-dev-send-email-request
jsonld:
- class_count: 120
  name: Groundmail Dev Context
  property_count: 335
  slug: groundmail-dev-context
layout: provider
modified: '2026-10-30'
name: groundmail-dev
nav: Providers
network: true
overview: 'groundmail-dev publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Automations API, Deliverability API, Dmarc API, and 15 more. Tagged areas include Email, Transactional, SMTP, and Developers.


  The groundmail-dev catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  groundmail-dev''s developer surface includes CLI, authentication, support, pricing, changelog, engineering blog, getting-started guide, and 29 more developer resources.'
plans:
- name: Groundmail Dev Plans Pricing
  plan_count: 2
  slug: groundmail-dev-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: groundmail-dev API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 2
  slug: groundmail-dev-rules
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.6
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 69.5
    developer_ergonomics: 43.5
    discoverability: 58.0
    operational_transparency: 36.8
  previous_composite: 60.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/groundmail-dev/groundmail-dev-2026-11-03T133105.png
security:
- kind: authentication
  name: Groundmail Dev Authentication
  slug: groundmail-dev-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Groundmail Dev Domain Security
  slug: groundmail-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Groundmail Dev Vulnerability Disclosure
  slug: groundmail-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: groundmail-dev-create-and-activate-automation
  slug: groundmail-dev-create-and-activate-automation
- name: groundmail-dev-create-and-test-template
  slug: groundmail-dev-create-and-test-template
- name: groundmail-dev-manage-tenant-domain
  slug: groundmail-dev-manage-tenant-domain
- name: groundmail-dev-manage-webhooks
  slug: groundmail-dev-manage-webhooks
- name: groundmail-dev-send-transactional-email
  slug: groundmail-dev-send-transactional-email
slug: groundmail-dev
tags:
- Email
- Transactional
- SMTP
- Developers
website: https://groundmail.dev/
---
