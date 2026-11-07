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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Domainlab App Agentic Access
  operation_count: 25
  slug: domainlab-app-agentic-access
  summary_line: 25 operations · 8 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://www.domainlab.app/api/v1
  baseurl_source: declared
  description: The Account API from Domain Lab — 1 operation(s) for account.
  name: Domain Lab Account API
  slug: domainlab-app-account-api
- baseURL: https://www.domainlab.app/api/v1
  baseurl_source: declared
  description: The Alerts API from Domain Lab — 1 operation(s) for alerts.
  name: Domain Lab Alerts API
  slug: domainlab-app-alerts-api
- baseURL: https://www.domainlab.app/api/v1
  baseurl_source: declared
  description: The Domain Status API from Domain Lab — 1 operation(s) for domain status.
  name: Domain Lab Domain Status API
  slug: domainlab-app-domain-status-api
- baseURL: https://www.domainlab.app/api/v1
  baseurl_source: declared
  description: The Domains API from Domain Lab — 10 operation(s) for domains.
  name: Domain Lab Domains API
  slug: domainlab-app-domains-api
- baseURL: https://www.domainlab.app/api/v1
  baseurl_source: declared
  description: The Email API from Domain Lab — 1 operation(s) for email.
  name: Domain Lab Email API
  slug: domainlab-app-email-api
- baseURL: https://www.domainlab.app/api/v1
  baseurl_source: declared
  description: The Event Types API from Domain Lab — 1 operation(s) for event types.
  name: Domain Lab Event Types API
  slug: domainlab-app-event-types-api
- baseURL: https://www.domainlab.app/api/v1
  baseurl_source: declared
  description: The Events API from Domain Lab — 1 operation(s) for events.
  name: Domain Lab Events API
  slug: domainlab-app-events-api
- baseURL: https://www.domainlab.app/api/v1
  baseurl_source: declared
  description: The Inbox API from Domain Lab — 2 operation(s) for inbox.
  name: Domain Lab Inbox API
  slug: domainlab-app-inbox-api
- baseURL: https://www.domainlab.app/api/v1
  baseurl_source: declared
  description: The Notification Rules API from Domain Lab — 1 operation(s) for notification rules.
  name: Domain Lab Notification Rules API
  slug: domainlab-app-notification-rules-api
- baseURL: https://www.domainlab.app/api/v1
  baseurl_source: declared
  description: The Registrar Connections API from Domain Lab — 2 operation(s) for registrar connections.
  name: Domain Lab Registrar Connections API
  slug: domainlab-app-registrar-connections-api
artifact_total: 25
asyncapis:
- description: ''
  name: Domainlab App Webhooks
  slug: domainlab-app-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/domainlab-app/agentic-access/domainlab-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/domainlab-app-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/domainlab-app/plans/domainlab-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/domainlab-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/domainlab-app/rules/domainlab-app-rules.yml
  title: ''
  type: Spectral
  url: rules/domainlab-app-rules.yml
- group: design
  href: https://artifacts.apis.io/domainlab-app/json-ld/domainlab-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/domainlab-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/domainlab-app/vocabulary/domainlab-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/domainlab-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/domainlab-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/domainlab-app/asyncapi/domainlab-app-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/domainlab-app-webhooks.yml
- group: design
  href: https://artifacts.apis.io/domainlab-app/data-model/domainlab-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/domainlab-app-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://www.domainlab.app/help/articles/mcp-server
- group: auth
  href: https://artifacts.apis.io/domainlab-app/authentication/domainlab-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/domainlab-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/domainlab-app/errors/domainlab-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/domainlab-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/domainlab-app/conformance/domainlab-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/domainlab-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/domainlab-app/llms/domainlab-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/domainlab-app-llms.txt
- group: auth
  href: https://artifacts.apis.io/domainlab-app/well-known/domainlab-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/domainlab-app-security.txt
- group: auth
  href: https://artifacts.apis.io/domainlab-app/well-known/domainlab-app-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/domainlab-app-mcp-security.txt
- group: auth
  href: https://artifacts.apis.io/domainlab-app/well-known/domainlab-app-domainlab-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/domainlab-app-domainlab-security.txt
- group: agent
  href: https://artifacts.apis.io/domainlab-app/well-known/domainlab-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/domainlab-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/domainlab-app/hosts/domainlab-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/domainlab-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/domainlab-app/vendors/domainlab-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/domainlab-app-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.domainlab.app/help/articles/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.domainlab.app/terms
- group: operate
  title: ''
  type: Support
  url: https://www.domainlab.app/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.domainlab.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.domainlab.app/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://www.domainlab.app/help/articles/quick-start
- group: docs
  title: ''
  type: APIReference
  url: https://www.domainlab.app/help/articles/api-quick-start
- group: auth
  href: https://artifacts.apis.io/domainlab-app/security/domainlab-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/domainlab-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/domainlab-app/security/domainlab-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domainlab-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://domainlab.app/
created: '2026-11-05'
description: Domain Lab provides AI‑powered domain, DNS and SSL monitoring with smart alerts. It tracks changes to domains, records, certificates and explains events in plain English, offering automated integrations with tools like Claude, ChatGPT, n8n, Lindy and Zapier.
json_schemas:
- name: Alert
  property_count: 9
  slug: domainlab-app-alert
- name: DomainSummary
  property_count: 15
  slug: domainlab-app-domain-summary
- name: Event
  property_count: 8
  slug: domainlab-app-event
- name: InboxItem
  property_count: 9
  slug: domainlab-app-inbox-item
- name: RegistrarConnection
  property_count: 9
  slug: domainlab-app-registrar-connection
- name: Scan
  property_count: 20
  slug: domainlab-app-scan
jsonld:
- class_count: 12
  name: Domainlab App Context
  property_count: 72
  slug: domainlab-app-context
layout: provider
modified: '2026-11-05'
name: Domain Lab
nav: Providers
network: true
overview: 'Domain Lab publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Alerts API, Domain Status API, and 7 more. Tagged areas include Domain Monitoring, DNS Monitoring, SSL Monitoring, AI Alerts, and Automation Integration.


  The Domain Lab catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Domain Lab''s developer surface includes authentication, support, pricing, getting-started guide, API reference, and 24 more developer resources.'
plans:
- name: Domainlab App Plans Pricing
  plan_count: 3
  slug: domainlab-app-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Domain Lab API Rules
  rule_count: 52
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 3
  slug: domainlab-app-rules
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 69.9
    developer_ergonomics: 37.5
    discoverability: 62.5
    operational_transparency: 18.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Domainlab App Authentication
  slug: domainlab-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Domainlab App Domain Security
  slug: domainlab-app-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Domainlab App Vulnerability Disclosure
  slug: domainlab-app-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: domainlab-app-monitor-new-domain
  slug: domainlab-app-monitor-new-domain
slug: domainlab-app
tags:
- Domain Monitoring
- DNS Monitoring
- SSL Monitoring
- AI Alerts
- Automation Integration
- Webhook Notifications
website: https://domainlab.app/
---
