---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Emailconnect Agentic Access
  operation_count: 25
  slug: emailconnect-agentic-access
  summary_line: 25 operations · 14 acting
api_count: 1
apis:
- baseURL: https://app.emailconnect.eu
  baseurl_source: declared
  description: 'Look up one email and its stored attachments with their fetch counts, or delete it after processing. Looking up requires the `logs:read` API key scope, which includes stored message content. Deleting '
  name: EmailConnect by XADI API v1 - Emails API
  slug: emailconnect-api-v1-emails-api
- baseURL: https://app.emailconnect.eu
  baseurl_source: declared
  description: Programmatic access to email processing logs with filtering and retry capabilities. Requires `logs:read` or `logs:retry` API key scope. `logs:read` reads delivery logs, including stored message conten
  name: EmailConnect by XADI API v1 - Logs API
  slug: emailconnect-api-v1-logs-api
- baseURL: https://app.emailconnect.eu
  baseurl_source: declared
  description: Programmatic access to usage metrics and statistics. Requires `metrics:read` API key scope.
  name: EmailConnect by XADI API v1 - Metrics API
  slug: emailconnect-api-v1-metrics-api
- baseURL: https://app.emailconnect.eu
  baseurl_source: declared
  description: Create and manage email aliases for your verified domains. Route specific email addresses to different webhooks.
  name: EmailConnect by XADI User Aliases API
  slug: emailconnect-user-aliases-api
- baseURL: https://app.emailconnect.eu
  baseurl_source: declared
  description: Manage your email domains. Add domains, verify ownership, and configure email routing.
  name: EmailConnect by XADI User Domains API
  slug: emailconnect-user-domains-api
- baseURL: https://app.emailconnect.eu
  baseurl_source: declared
  description: Configure webhook endpoints to receive email data. Set up multiple webhooks per domain for different processing needs.
  name: EmailConnect by XADI User Webhooks API
  slug: emailconnect-user-webhooks-api
- baseURL: https://app.emailconnect.eu
  baseurl_source: declared
  description: Atomic operations for creating webhooks and aliases together. Ideal for n8n integrations and simplified setup workflows.
  name: EmailConnect by XADI Webhook Alias API
  slug: emailconnect-webhook-alias-api
artifact_total: 23
asyncapis:
- description: ''
  name: Emailconnect Webhooks
  slug: emailconnect-webhooks
common:
- group: other
  href: https://artifacts.apis.io/emailconnect/capabilities/emailconnect-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/emailconnect-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/emailconnect/agentic-access/emailconnect-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/emailconnect-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/emailconnect/plans/emailconnect-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/emailconnect-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/emailconnect/rules/emailconnect-rules.yml
  title: ''
  type: Spectral
  url: rules/emailconnect-rules.yml
- group: design
  href: https://artifacts.apis.io/emailconnect/json-ld/emailconnect-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/emailconnect-context.jsonld
- group: design
  href: https://artifacts.apis.io/emailconnect/vocabulary/emailconnect-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/emailconnect-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/emailconnect/asyncapi/emailconnect-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/emailconnect-webhooks.yml
- group: design
  href: https://artifacts.apis.io/emailconnect/data-model/emailconnect-data-model.yml
  title: ''
  type: DataModel
  url: data-model/emailconnect-data-model.yml
- group: operate
  href: https://artifacts.apis.io/emailconnect/changelog/emailconnect-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/emailconnect-changelog.yml
- group: auth
  href: https://artifacts.apis.io/emailconnect/authentication/emailconnect-authentication.yml
  title: ''
  type: Authentication
  url: authentication/emailconnect-authentication.yml
- group: design
  href: https://artifacts.apis.io/emailconnect/errors/emailconnect-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/emailconnect-problem-types.yml
- group: design
  href: https://artifacts.apis.io/emailconnect/conformance/emailconnect-conformance.yml
  title: ''
  type: Conformance
  url: conformance/emailconnect-conformance.yml
- group: agent
  href: https://artifacts.apis.io/emailconnect/llms/emailconnect-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/emailconnect-llms.txt
- group: auth
  href: https://artifacts.apis.io/emailconnect/well-known/emailconnect-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/emailconnect-security.txt
- group: auth
  href: https://artifacts.apis.io/emailconnect/well-known/emailconnect-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/emailconnect-app-security.txt
- group: agent
  href: https://artifacts.apis.io/emailconnect/well-known/emailconnect-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/emailconnect-well-known.yml
- group: other
  href: https://artifacts.apis.io/emailconnect/hosts/emailconnect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/emailconnect-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.emailconnect.eu/
- group: auth
  title: ''
  type: Security
  url: https://emailconnect.eu/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://emailconnect.eu/changelog/
- group: auth
  href: https://artifacts.apis.io/emailconnect/security/emailconnect-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/emailconnect-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/emailconnect/security/emailconnect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/emailconnect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://emailconnect.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://emailconnect.eu/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://emailconnect.eu/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://emailconnect.eu/learn/guides/
- group: operate
  title: ''
  type: Support
  url: https://emailconnect.eu/help/
- group: company
  title: ''
  type: Blog
  url: https://emailconnect.eu/learn/
- group: commercial
  title: ''
  type: Pricing
  url: https://emailconnect.eu/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://emailconnect.eu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emailconnect.eu/privacy-promise/
created: '2026-10-16'
description: EmailConnect by XADI provides EU‑hosted inbound email processing that forwards messages to webhooks. It offers use‑case specific solutions such as enterprise calendar integration, centralized issue tracking, financial document automation, HOA support, and insurance claims intake. The platform emphasizes data residency, AI‑assisted ticket handling, and compliance with EU digital‑sovereignty regulations. Users can try the service for free, explore pricing, and access extensive guides, comparisons, and security documentation.
finops:
- has_sources: true
  method: derived
  name: Emailconnect Finops
  primary_unit: seat
  service_category: ''
  slug: emailconnect-finops
  template: false
image: https://emailconnect.eu/og-image.png
json_schemas:
- name: Alias
  property_count: 10
  slug: emailconnect-alias
- name: AttachmentInfo
  property_count: 13
  slug: emailconnect-attachment-info
- name: CreateDomainPayload
  property_count: 7
  slug: emailconnect-create-domain-payload
- name: CreateWebhookAliasRequest
  property_count: 7
  slug: emailconnect-create-webhook-alias-request
- name: Domain
  property_count: 20
  slug: emailconnect-domain
- name: EmailLog
  property_count: 18
  slug: emailconnect-email-log
jsonld:
- class_count: 15
  name: Emailconnect Context
  property_count: 73
  slug: emailconnect-context
layout: provider
modified: '2026-10-16'
name: EmailConnect by XADI
nav: Providers
network: true
overview: 'EmailConnect by XADI publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including API v1 - Emails API, API v1 - Logs API, API v1 - Metrics API, and 4 more. Tagged areas include Company, Email, Webhook, EU, and Compliance.


  The EmailConnect by XADI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  EmailConnect by XADI''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 24 more developer resources.'
plans:
- name: Emailconnect Plans Pricing
  plan_count: 4
  slug: emailconnect-plans-pricing
- name: Emailconnect Price Estimates
  plan_count: 0
  slug: emailconnect-price-estimates
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: EmailConnect by XADI API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 1
  slug: emailconnect-rules
score:
  band: strong
  composite: 61.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 73.7
    contract_governance: 35.6
    contract_quality: 72.2
    developer_ergonomics: 47.6
    discoverability: 66.1
    operational_transparency: 50.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 59.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Emailconnect Authentication
  slug: emailconnect-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Emailconnect Domain Security
  slug: emailconnect-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Emailconnect Vulnerability Disclosure
  slug: emailconnect-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: emailconnect
tags:
- Company
- Email
- Webhook
- EU
- Compliance
website: https://emailconnect.eu/
---
