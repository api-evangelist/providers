---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Belcome API accessed via MCP JSON-RPC endpoint. Provides salon and spa booking operations.
  name: Belcome API
  slug: belcome-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/belcome-app/plans/belcome-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/belcome-app-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/belcome-app/authentication/belcome-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/belcome-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/belcome-app/scopes/belcome-app-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/belcome-app-scopes.yml
- group: design
  href: https://artifacts.apis.io/belcome-app/errors/belcome-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/belcome-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/belcome-app/conformance/belcome-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/belcome-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/belcome-app/llms/belcome-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/belcome-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/belcome-app/mcp/belcome-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/belcome-app-mcp.yml
- group: other
  href: https://artifacts.apis.io/belcome-app/hosts/belcome-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/belcome-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/belcome-app/vendors/belcome-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/belcome-app-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.belcome.app/security/
- group: auth
  href: https://artifacts.apis.io/belcome-app/security/belcome-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/belcome-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://belcome.app/
- group: operate
  title: ''
  type: Support
  url: https://www.belcome.app/help/
- group: docs
  title: ''
  type: Documentation
  url: https://www.belcome.app/help/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.belcome.app/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.belcome.app/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.belcome.app/privacy/
created: '2026-11-02'
description: Belcome provides 24/7 online booking for salons, barbershops, spas, and med spas worldwide, supporting six languages. It offers a customizable booking page, client self‑service tools, automated waitlists, group bookings, and integration with existing websites via a simple embed. Users can start a 14‑day free trial, and pricing starts at $25 per location per month with additional team member fees. The platform is built by Design Master Solutions LLC and emphasizes HIPAA‑compliant handling of client data for med spas.
image: https://www.belcome.app/assets/icons/belcome-mark-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at belcome.app.
  name: Belcome MCP Server
  slug: belcome-app-mcp-yml
modified: '2026-11-02'
name: Belcome
nav: Providers
network: true
overview: 'Belcome is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Booking, Salon, Spa, Software-as-a-Service, and Healthcare.


  Belcome''s developer surface includes authentication, support, documentation, pricing, and 13 more developer resources.'
plans:
- name: Belcome App Plans Pricing
  plan_count: 2
  slug: belcome-app-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Belcome App Rate Limits
  slug: belcome-app-rate-limits
scopes:
- name: Belcome App Scopes
  scope_count: 0
  slug: belcome-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 29.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Belcome App Authentication
  slug: belcome-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Belcome App Domain Security
  slug: belcome-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: belcome-app
tags:
- Booking
- Salon
- Spa
- Software-as-a-Service
- Healthcare
website: https://belcome.app/
---
