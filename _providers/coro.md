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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Coro's REST API (v1) for managing workspaces, subscriptions, tickets, devices, protected users, portal users, usage, audit logs, and webhooks across the Coro cybersecurity platform. OAuth 2.0 client-c
  name: Coro Public REST API
  slug: coro-public-rest-api
artifact_total: 8
asyncapis:
- description: ''
  name: Coro Webhooks
  slug: coro-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/coro/plans/coro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coro-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.coro.net/feed
- group: company
  title: ''
  type: Website
  url: https://www.coro.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.coro.net/developer-portal/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coro.net/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.coro.net/developer-portal/authentication/
- group: auth
  href: https://artifacts.apis.io/coro/authentication/coro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coro-authentication.yml
- group: agent
  href: https://artifacts.apis.io/coro/mcp/coro-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/coro-mcp.yml
- group: design
  href: https://artifacts.apis.io/coro/asyncapi/coro-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/coro-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/coro/changelog/coro-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/coro-changelog.yml
- group: design
  href: https://artifacts.apis.io/coro/lifecycle/coro-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/coro-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/coro/conventions/coro-conventions.yml
  title: ''
  type: Conventions
  url: conventions/coro-conventions.yml
- group: design
  href: https://artifacts.apis.io/coro/data-model/coro-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coro-data-model.yml
- group: design
  href: https://artifacts.apis.io/coro/conformance/coro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coro-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.coro.net/compliance
- group: auth
  href: https://artifacts.apis.io/coro/security/coro-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/coro-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/coro/security/coro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coro-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/coro/well-known/coro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coro-well-known.yml
- group: agent
  href: https://artifacts.apis.io/coro/llms/coro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coro-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://docs.coro.net/
- group: company
  title: ''
  type: Blog
  url: https://www.coro.net/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coro.net/platform/pricing
- group: start
  title: ''
  type: SignUp
  url: https://secure.coro.net/login
- group: start
  title: ''
  type: Login
  url: https://secure.coro.net/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coro.net/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coro.net/legal/privacy
created: '2026-07-17'
description: Coro is a cybersecurity company that consolidates endpoint protection, email security, network protection (ZTNA, VPN, encryption), cloud app security, data protection, and security awareness training into a single AI-driven platform built for lean IT teams, growing organizations, and managed service providers (MSPs). Coro's public REST API (v1) exposes the same workspace security data through region-specific hosts (US, Canada, Germany), organized around workspaces as tenant containers with subscriptions, tickets, devices, protected users, portal users, usage metrics, audit logs, and webhook configurations. It authenticates with OAuth 2.0 client credentials and offers real-time webhooks and an official MCP server so AI tools can query Coro securely. Coro was surfaced as a portfolio company of Balderton Capital.
finops:
- has_sources: true
  method: derived
  name: Coro Finops
  primary_unit: ''
  service_category: ''
  slug: coro-finops
  template: true
image: https://www.coro.net/wp-content/uploads/coro-opengraph.png
layout: provider
mcp_servers:
- description: Coro publishes an official, hosted MCP (Model Context Protocol) server that acts as a secure intermediary between an organization's AI tools and Coro's workspace security data. The MCP server authenti
  name: Coro MCP Server
  slug: coro
modified: '2026-10-06'
name: Coro
nav: Providers
network: true
overview: 'Coro is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Security, Endpoint Security, and Email Security.


  The Coro catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coro''s developer surface includes documentation, getting-started guide, authentication, changelog, support, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Coro Plans Pricing
  plan_count: 4
  slug: coro-plans-pricing
random_paper: 3
score:
  band: developing
  composite: 52.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.3
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 50.0
    discoverability: 65.0
    operational_transparency: 23.7
  previous_composite: 45.8
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/coro/coro-2026-07-25T210437.png
security:
- kind: authentication
  name: Coro Authentication
  slug: coro-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Coro Domain Security
  slug: coro-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Coro Trust Center
  slug: coro-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: coro
tags:
- Company
- Cybersecurity
- Security
- Endpoint Security
- Email Security
- Cloud Security
- Data Protection
- MSP
- Webhook
- MCP
website: https://www.coro.net/
---
