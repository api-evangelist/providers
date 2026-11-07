---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.autopass.xyz
  baseurl_source: declared
  description: Partner parking locations (POIs)
  name: Autopass Locations API
  slug: autopass-locations-api
- baseURL: https://api.autopass.xyz
  baseurl_source: declared
  description: Completed parking transactions and invoices
  name: Autopass Orders API
  slug: autopass-orders-api
- baseURL: https://api.autopass.xyz
  baseurl_source: declared
  description: In-progress parking sessions
  name: Autopass Sessions API
  slug: autopass-sessions-api
artifact_total: 13
asyncapis:
- description: ''
  name: Autopass Webhooks
  slug: autopass-webhooks
collections:
- collection_type: open
  name: Autopass Service Authorization Locations API
  slug: open-autopass-locations-api
- collection_type: open
  name: Autopass Service Authorization Locations Orders API
  slug: open-autopass-orders-api
- collection_type: open
  name: Autopass Service Authorization Locations Sessions API
  slug: open-autopass-sessions-api
common:
- group: other
  href: https://artifacts.apis.io/autopass/overlays/autopass-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/autopass-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/autopass/security/autopass-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autopass-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.autopass.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.autopass.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.autopass.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.autopass.xyz/llms.txt
- group: auth
  href: https://artifacts.apis.io/autopass/authentication/autopass-authentication.yml
  title: ''
  type: Authentication
  url: authentication/autopass-authentication.yml
- group: auth
  href: https://artifacts.apis.io/autopass/scopes/autopass-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/autopass-scopes.yml
- group: agent
  href: https://artifacts.apis.io/autopass/well-known/autopass-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autopass-well-known.yml
- group: agent
  href: https://artifacts.apis.io/autopass/llms/autopass-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autopass-llms.txt
- group: design
  href: https://artifacts.apis.io/autopass/conventions/autopass-conventions.yml
  title: ''
  type: Conventions
  url: conventions/autopass-conventions.yml
- group: design
  href: https://artifacts.apis.io/autopass/data-model/autopass-data-model.yml
  title: ''
  type: DataModel
  url: data-model/autopass-data-model.yml
- group: design
  href: https://artifacts.apis.io/autopass/lifecycle/autopass-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/autopass-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/autopass/asyncapi/autopass-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/autopass-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/autopass/mcp/autopass-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/autopass-mcp.yml
- group: agent
  href: https://artifacts.apis.io/autopass/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autopass.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autopass.xyz/privacy
created: '2026-07-17'
description: 'Autopass ("快速通") is a Taiwan-based mobility financial-services platform that connects service locations, car-owner apps, payments and benefits so that every driver enjoys a fast, convenient driving experience. Through its "powered by Autopass" service-authorization program, channel brand partners embed license-plate-based parking payment into their own car-owner apps: they register user license plates, surface partner parking locations (POIs) with live rates and hours, read in-progress parking sessions and completed orders, and receive entry/exit/billing/refund notifications over an OAuth 2.0 / OpenID Connect secured API. Autopass aims to become Asia''s largest provider of mobility financial services. Backed by 500 Global.'
image: https://www.autopass.xyz/autopass_og.jpg
layout: provider
modified: '2026-07-18'
name: Autopass
nav: Providers
network: true
overview: 'Autopass publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Locations API, Orders API, and Sessions API. Tagged areas include Company, Mobility, Parking, Payments, and Automotive.


  The Autopass catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Autopass'' developer surface includes documentation, API reference, authentication, and 15 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Autopass API Rules
  rule_count: 61
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 1
  slug: autopass-rules
scopes:
- name: Autopass Scopes
  scope_count: 1
  slug: autopass-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 13.6
    contract_quality: 56.4
    developer_ergonomics: 39.9
    discoverability: 73.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - taiwan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 37.4
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/autopass/autopass-2026-07-25T201842.png
security:
- kind: authentication
  name: Autopass Authentication
  slug: autopass-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Autopass Domain Security
  slug: autopass-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Show Autopass partner parking locations
  slug: autopass-show-parking-locations
- name: Track an Autopass parking session and settle the order
  slug: autopass-track-session-and-order
slug: autopass
tags:
- Company
- Mobility
- Parking
- Payments
- Automotive
- Financial Services
- OAuth
- Taiwan
- Authentication
website: https://en.autopass.xyz
---
