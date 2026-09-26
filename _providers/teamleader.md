---
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Teamleader Agentic Access
  operation_count: 58
  slug: teamleader-agentic-access
  summary_line: 58 operations · 43 acting
api_count: 14
apis:
- baseURL: https://api.focus.teamleader.eu
  baseurl_source: declared
  description: The Contacts API from Teamleader — 11 operation(s) for contacts.
  name: Teamleader Contacts API
  slug: teamleader-contacts-api
- baseURL: https://api.focus.teamleader.eu
  baseurl_source: declared
  description: The Daysoff API from Teamleader — 1 operation(s) for daysoff.
  name: Teamleader Daysoff API
  slug: teamleader-daysoff-api
- baseURL: https://api.focus.teamleader.eu
  baseurl_source: declared
  description: The Deals API from Teamleader — 8 operation(s) for deals.
  name: Teamleader Deals API
  slug: teamleader-deals-api
- baseURL: https://api.focus.teamleader.eu
  baseurl_source: declared
  description: The Expenses API from Teamleader — 1 operation(s) for expenses.
  name: Teamleader Expenses API
  slug: teamleader-expenses-api
- baseURL: https://api.focus.teamleader.eu
  baseurl_source: declared
  description: The Files API from Teamleader — 5 operation(s) for files.
  name: Teamleader Files API
  slug: teamleader-files-api
- baseURL: https://api.focus.teamleader.eu
  baseurl_source: declared
  description: The Invoices API from Teamleader — 9 operation(s) for invoices.
  name: Teamleader Invoices API
  slug: teamleader-invoices-api
- baseURL: https://api.focus.teamleader.eu
  baseurl_source: declared
  description: The Leveltwoareas API from Teamleader — 1 operation(s) for leveltwoareas.
  name: Teamleader Leveltwoareas API
  slug: teamleader-leveltwoareas-api
- baseURL: https://api.focus.teamleader.eu
  baseurl_source: declared
  description: The Lostreasons API from Teamleader — 1 operation(s) for lostreasons.
  name: Teamleader Lostreasons API
  slug: teamleader-lostreasons-api
- baseURL: https://api.focus.teamleader.eu
  baseurl_source: declared
  description: The Tasks API from Teamleader — 8 operation(s) for tasks.
  name: Teamleader Tasks API
  slug: teamleader-tasks-api
- baseURL: https://api.focus.teamleader.eu
  baseurl_source: declared
  description: The Tickets API from Teamleader — 9 operation(s) for tickets.
  name: Teamleader Tickets API
  slug: teamleader-tickets-api
- baseURL: https://api.focus.teamleader.eu
  baseurl_source: declared
  description: The Ticketstatus API from Teamleader — 1 operation(s) for ticketstatus.
  name: Teamleader Ticketstatus API
  slug: teamleader-ticketstatus-api
- baseURL: https://api.focus.teamleader.eu
  baseurl_source: declared
  description: The Timers API from Teamleader — 1 operation(s) for timers.
  name: Teamleader Timers API
  slug: teamleader-timers-api
- baseURL: https://api.focus.teamleader.eu
  baseurl_source: declared
  description: The Useravailability API from Teamleader — 1 operation(s) for useravailability.
  name: Teamleader Useravailability API
  slug: teamleader-useravailability-api
- baseURL: https://api.focus.teamleader.eu
  baseurl_source: declared
  description: The Payment Methods API from Teamleader — 1 operation(s) for payment methods.
  name: Teamleader Payment Methods API
  slug: teamleader-payment-methods-api
artifact_total: 28
asyncapis:
- description: ''
  name: Teamleader Webhooks
  slug: teamleader-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/agentic-access/teamleader-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/teamleader-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/rules/teamleader-rules.yml
  title: ''
  type: Spectral
  url: rules/teamleader-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/json-ld/teamleader-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/teamleader-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/vocabulary/teamleader-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/teamleader-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/data-model/teamleader-data-model.yml
  title: ''
  type: DataModel
  url: data-model/teamleader-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/conformance/teamleader-conformance.yml
  title: ''
  type: Conformance
  url: conformance/teamleader-conformance.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.teamleader.eu/about/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/authentication/teamleader-authentication.yml
  title: ''
  type: Authentication
  url: authentication/teamleader-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/well-known/teamleader-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/teamleader-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/well-known/teamleader-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/teamleader-well-known.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.teamleader.eu/legal/terms-of-service-teamleader-focus
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/asyncapi/teamleader-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/teamleader-webhooks.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/changelog/teamleader-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/teamleader-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.teamleader.eu/legal/security-teamleader-focus
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/security/teamleader-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/teamleader-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/llms/teamleader-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/teamleader-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/packages/teamleader-packages.yml
  title: ''
  type: SDKs
  url: packages/teamleader-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/packages/teamleader-packages.yml
  title: ''
  type: Packages
  url: packages/teamleader-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.teamleader.eu/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/security/teamleader-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/teamleader-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/security/teamleader-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/teamleader-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/security/teamleader-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/teamleader-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.teamleader.eu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.focus.teamleader.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.focus.teamleader.eu/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.focus.teamleader.eu/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.focus.teamleader.eu/docs/introduction
- group: operate
  title: ''
  type: Support
  url: https://support.focus.teamleader.eu/hc/en-150
- group: company
  title: ''
  type: Blog
  url: https://www.teamleader.eu/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.teamleader.eu/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teamleader.eu/legal/privacy-statement
- group: start
  title: ''
  type: SignUp
  url: https://signup.focus.teamleader.eu/
coverage:
  checked: 2026-09-21
  detail: Developer docs provide markdown but no OpenAPI or other machine-readable contract was found.
  evidence:
  - status: 404
    url: https://api.teamleader.eu/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-21'
description: Teamleader provides an integrated CRM, invoicing, quotations, and project management platform for SMEs. Its Focus product offers a unified workspace to manage customers, sales, finances, and projects, with a marketplace for extensions and robust API access for developers.
image: https://cdn.craft.cloud/019c94d2-1a0c-72a9-9aeb-fca40a9cddd3/assets/general/SEO-images/Teamleader-SEO.jpg?fit=cover&height=630&width=1200&s=qRou8Ix0kelrG98e5NrDsPf-6SZBB_wNOxzMj9zJnug
json_schemas:
- name: PostContactsAddRequest
  property_count: 18
  slug: teamleader-post-contacts-add-request
- name: PostDealsCreateRequest
  property_count: 14
  slug: teamleader-post-deals-create-request
- name: PostInvoicesDraftRequest
  property_count: 16
  slug: teamleader-post-invoices-draft-request
- name: PostInvoicesUpdateRequest
  property_count: 15
  slug: teamleader-post-invoices-update-request
- name: PostTasksCreateRequest
  property_count: 12
  slug: teamleader-post-tasks-create-request
- name: PostTicketsCreateRequest
  property_count: 10
  slug: teamleader-post-tickets-create-request
jsonld:
- class_count: 92
  name: Teamleader Context
  property_count: 97
  slug: teamleader-context
layout: provider
modified: '2026-09-21'
name: Teamleader
nav: Providers
network: true
overview: 'Teamleader publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Daysoff API, Deals API, and 11 more. Tagged areas include CRM, Invoicing, Project Management, Software-as-a-Service, and Small Business.


  The Teamleader catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Teamleader''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 25 more developer resources.'
random_paper: 10
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Teamleader API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: teamleader-rules
score:
  band: developing
  composite: 52.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.6
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 33.4
    developer_ergonomics: 64.3
    discoverability: 80.4
    operational_transparency: 50.0
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 15
      marker_coverage: 100.0
      total: 15
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Teamleader Authentication
  slug: teamleader-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Teamleader Domain Security
  slug: teamleader-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Teamleader Vulnerability Disclosure
  slug: teamleader-vulnerability-disclosure
  summary_line: Intigriti
- kind: trust-center
  name: Teamleader Trust Center
  slug: teamleader-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: teamleader
tags:
- CRM
- Invoicing
- Project Management
- Software-as-a-Service
- Small Business
website: https://www.teamleader.eu/
---
