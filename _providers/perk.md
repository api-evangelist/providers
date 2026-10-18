---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Perk Agentic Access
  operation_count: 42
  slug: perk-agentic-access
  summary_line: 42 operations · 15 acting
api_count: 8
apis:
- description: 'REST API for Perk travel, expense, invoice, trip, cost-center, event, and card data. Authenticate with an account API key (customers) or OAuth 2.0 (partners); send Api-Version: 1.'
  name: Perk Travel & Spend API
  slug: perk-travel-spend-api
- description: SCIM 2.0 user-provisioning API for creating, updating, and deactivating Perk users from identity providers (Okta, Microsoft Entra ID), including an expense extension schema.
  name: Perk SCIM API
  slug: perk-scim-api
- baseURL: https://api.perk.com
  baseurl_source: declared
  description: Create, retrieve, modify, and archive cost objects (cost centers) in your Perk organization. For more information, see [Cost objects in Perk](https://support.perk.com/hc/en-us/articles/21926030522908-
  name: Perk Cost centers API
  slug: perk-cost-centers-api
- baseURL: https://api.perk.com
  baseurl_source: declared
  description: Retrieve select options for custom fields in your Perk account.
  name: Perk Custom fields API
  slug: perk-custom-fields-api
- baseURL: https://api.perk.com
  baseurl_source: declared
  description: The Bookings API from Perk — 1 operation(s) for bookings.
  name: Perk Bookings API
  slug: perk-bookings-api
- baseURL: https://api.perk.com
  baseurl_source: declared
  description: The Companies API from Perk — 1 operation(s) for companies.
  name: Perk Companies API
  slug: perk-companies-api
- baseURL: https://api.perk.com
  baseurl_source: declared
  description: The Invoices API from Perk — 4 operation(s) for invoices.
  name: Perk Invoices API
  slug: perk-invoices-api
- baseURL: https://api.perk.com
  baseurl_source: declared
  description: The Profiles API from Perk — 1 operation(s) for profiles.
  name: Perk Profiles API
  slug: perk-profiles-api
- baseURL: https://api.perk.com
  baseurl_source: declared
  description: The Schemas API from Perk — 5 operation(s) for schemas.
  name: Perk Schemas API
  slug: perk-schemas-api
- baseURL: https://api.perk.com
  baseurl_source: declared
  description: The Suppliers API from Perk — 1 operation(s) for suppliers.
  name: Perk Suppliers API
  slug: perk-suppliers-api
- baseURL: https://api.perk.com
  baseurl_source: declared
  description: The Trips API from Perk — 3 operation(s) for trips.
  name: Perk Trips API
  slug: perk-trips-api
- baseURL: https://api.perk.com
  baseurl_source: declared
  description: The Users API from Perk — 3 operation(s) for users.
  name: Perk Users API
  slug: perk-users-api
- baseURL: https://api.perk.com
  baseurl_source: declared
  description: The Webhooks API from Perk — 4 operation(s) for webhooks.
  name: Perk Webhooks API
  slug: perk-webhooks-api
- baseURL: https://api.perk.com
  baseurl_source: declared
  description: The Resource Types API from Perk — 1 operation(s) for resource types.
  name: Perk Resource Types API
  slug: perk-resource-types-api
- baseURL: https://api.perk.com
  baseurl_source: declared
  description: The Service Provider Config API from Perk — 1 operation(s) for service provider config.
  name: Perk Service Provider Config API
  slug: perk-service-provider-config-api
artifact_total: 23
asyncapis:
- description: ''
  name: Perk Webhooks
  slug: perk-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/agentic-access/perk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/perk-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/rules/perk-rules.yml
  title: ''
  type: Spectral
  url: rules/perk-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/vocabulary/perk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/perk-vocabulary.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/hosts/perk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/perk-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/vendors/perk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/perk-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.perk.com/legal/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.perk.com/news/
- group: company
  title: ''
  type: Blog
  url: https://www.perk.com/blog/
- group: company
  title: ''
  type: Website
  url: https://www.perk.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.perk.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.perk.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.perk.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.perk.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://support.perk.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.perk.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.perk.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.perk.com/docs/travelperk-marketplace-and-api-terms-of-use
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/26205026-08341f0b-356a-460b-b386-54f8c30b9bad
- group: operate
  title: ''
  type: StatusPage
  url: https://status.perk.com
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/mcp/perk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/perk-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/llms/perk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/perk-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/authentication/perk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/perk-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/scopes/perk-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/perk-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/conventions/perk-conventions.yml
  title: ''
  type: Conventions
  url: conventions/perk-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/errors/perk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/perk-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/lifecycle/perk-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/perk-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/lifecycle/perk-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/perk-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/changelog/perk-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/perk-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/sandbox/perk-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/perk-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/asyncapi/perk-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/perk-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/conformance/perk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/perk-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/data-model/perk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/perk-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/security/perk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/perk-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/well-known/perk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/perk-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/well-known/perk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/perk-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/security/perk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/perk-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/security/perk-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/perk-vulnerability-disclosure.yml
created: '2026-07-17'
description: Perk (formerly TravelPerk) is the intelligent platform for corporate travel and spend management, combining travel booking with expense, invoice, and card controls for finance teams. Founded in Barcelona in 2015, Perk serves thousands of global teams and is backed by General Catalyst, SoftBank Vision Fund, Speedinvest and others. Its developer platform exposes a Travel & Spend REST API, a SCIM 2.0 user-provisioning API, webhooks, a sandbox, a public Postman collection, and an official hosted Model Context Protocol (MCP) server for AI clients.
image: https://d2balr5nj4353r.cloudfront.net/favicon-192x192.png
layout: provider
mcp_servers:
- description: Perk's official hosted Model Context Protocol (MCP) server. Connects MCP-compatible AI clients (Claude Code, Cursor, Codex, MCP Inspector) to Perk travel, spend, invoice, event, policy, and card data.
  name: Perk MCP Server
  slug: perk-mcp-server
modified: '2026-10-06'
name: Perk
nav: Providers
network: true
overview: 'Perk publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cost centers API, Custom fields API, Bookings API, and 12 more. Tagged areas include Company, Corporate Travel, Expense Management, Spend Management, and Travel.


  The Perk catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Perk''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, pricing, signup flow, and 31 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Perk API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 3
  slug: perk-rules
scopes:
- name: Perk Scopes
  scope_count: 5
  slug: perk-scopes
  summary_line: 5 scopes
score:
  band: strong
  composite: 56.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 45.8
    catalog_earned_first_party: 0.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 11.0
  facets:
    access_clarity: 39.5
    contract_governance: 35.6
    contract_quality: 61.9
    developer_ergonomics: 51.8
    discoverability: 78.3
    operational_transparency: 57.9
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/screenshots/perk-2026-08-17T081158.png
security:
- kind: authentication
  name: Perk Authentication
  slug: perk-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Perk Domain Security
  slug: perk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Perk Vulnerability Disclosure
  slug: perk-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: perk
tags:
- Company
- Corporate Travel
- Expense Management
- Spend Management
- Travel
- Invoices
- Fintech
- Software-as-a-Service
website: https://www.perk.com/
---
