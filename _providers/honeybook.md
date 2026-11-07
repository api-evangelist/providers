---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Honeybook Agentic Access
  operation_count: 25
  slug: honeybook-agentic-access
  summary_line: 25 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.honeybook.com/v1
  baseurl_source: declared
  description: The visual project pipeline - bookings and pipeline stage.
  name: HoneyBook Projects API
  slug: honeybook-projects-api
- baseURL: https://api.honeybook.com/v1
  baseurl_source: declared
  description: Operations about Contacts
  name: HoneyBook Contacts API
  slug: honeybook-contacts-api
- baseURL: https://api.honeybook.com/v1
  baseurl_source: declared
  description: Operations about Pipelines
  name: HoneyBook Pipeline API
  slug: honeybook-pipeline-api
- baseURL: https://api.honeybook.com/v1
  baseurl_source: declared
  description: Operations about Workspaces
  name: HoneyBook Workspaces API
  slug: honeybook-workspaces-api
artifact_total: 22
collections:
- collection_type: open
  name: HoneyBook API (Modeled) Clients API
  slug: open-honeybook-clients-api
- collection_type: open
  name: HoneyBook API (Modeled) Clients Contracts API
  slug: open-honeybook-contracts-api
- collection_type: open
  name: HoneyBook API (Modeled) Clients Invoices API
  slug: open-honeybook-invoices-api
- collection_type: open
  name: HoneyBook API (Modeled) Clients Payments API
  slug: open-honeybook-payments-api
- collection_type: open
  name: HoneyBook API (Modeled) Clients Projects API
  slug: open-honeybook-projects-api
- collection_type: open
  name: HoneyBook API (Modeled) Clients Proposals API
  slug: open-honeybook-proposals-api
- collection_type: open
  name: HoneyBook API (Modeled) Clients Scheduler API
  slug: open-honeybook-scheduler-api
- collection_type: open
  name: HoneyBook API (Modeled) Clients Webhooks API
  slug: open-honeybook-webhooks-api
- collection_type: open
  name: HoneyBook API (Modeled)
  slug: open-honeybook
common:
- group: other
  href: https://artifacts.apis.io/honeybook/capabilities/honeybook-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/honeybook-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/honeybook/agentic-access/honeybook-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/honeybook-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/honeybook/security/honeybook-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/honeybook-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/honeybook/authentication/honeybook-authentication.yml
  title: ''
  type: Authentication
  url: authentication/honeybook-authentication.yml
- group: auth
  href: https://artifacts.apis.io/honeybook/scopes/honeybook-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/honeybook-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/honeybook
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/honeybook
- group: company
  title: ''
  type: Website
  url: https://www.honeybook.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.honeybook.com/en/collections/68941-integrations-and-partnerships
- group: commercial
  href: https://artifacts.apis.io/honeybook/plans/honeybook-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/honeybook-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/honeybook/rate-limits/honeybook-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/honeybook-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/honeybook/finops/honeybook-finops.yml
  title: ''
  type: FinOps
  url: finops/honeybook-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.honeybook.com/blog
created: '2026-07-04'
description: HoneyBook is an all-in-one clientflow management platform for independent, service-based businesses - photographers, event planners, designers, consultants, coaches, and similar creative entrepreneurs. It combines CRM/lead capture, proposals, contracts and e-signature, invoicing and payments, scheduling, automations, and client communication in one product. HoneyBook does not publish a self-serve public developer API or a developer portal; third-party connectivity is offered through a limited set of native integrations (QuickBooks Online, Zoom, Calendly, Flodesk, Canva, Meta Leads, Slack, Asana, monday.com) and, most broadly, through Zapier. An internal API host (api.honeybook.com) is live and clearly powers the Zapier integration and native connectors, but HoneyBook has never published a self-serve technical reference, OAuth client registration flow, or endpoint documentation for outside developers, and community requests for direct API access date back to at least January
  2024 with no roadmap commitment as of this review.
finops:
- has_sources: true
  method: generated
  name: Honeybook Finops
  primary_unit: ''
  service_category: Business Applications - Clientflow / CRM
  slug: honeybook-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/honeybook.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.api.honeybook.com over HTTP.
  name: HoneyBook MCP Server
  slug: honeybook
modified: '2026-07-04'
name: HoneyBook
nav: Providers
network: true
overview: 'HoneyBook publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Projects API, Contacts API, Pipeline API, and 1 more. Tagged areas include CRM, Clientflow, Proposals, Contracts, and Invoicing.


  The HoneyBook catalog on APIs.io includes 1 Spectral governance ruleset.


  HoneyBook''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Honeybook Plans Pricing
  plan_count: 4
  slug: honeybook-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Honeybook Rate Limits
  slug: honeybook-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: HoneyBook API Rules
  rule_count: 64
  severity_counts:
    error: 57
    hint: 0
    info: 2
    warn: 5
  slug: honeybook-rules
scopes:
- name: Honeybook Scopes
  scope_count: 14
  slug: honeybook-scopes
  summary_line: 14 scopes · authorizationCode
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 34.2
    developer_ergonomics: 23.8
    discoverability: 68.3
    operational_transparency: 10.5
  previous_composite: 23.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 30.8
      total: 13
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/honeybook/honeybook-2026-07-25T221358.png
security:
- kind: authentication
  name: Honeybook Authentication
  slug: honeybook-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Honeybook Domain Security
  slug: honeybook-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: honeybook
tags:
- CRM
- Clientflow
- Proposals
- Contracts
- Invoicing
- Payments
- Scheduling
- Creative Entrepreneurs
- Small Business
website: https://www.honeybook.com
---
