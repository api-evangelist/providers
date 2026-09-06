---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://scanverity.com
  baseurl_source: declared
  description: 'REST API (OpenAPI 3.1, contract v1.3.0-private-beta) for resolution-risk assessment on prediction markets. Versioned under /v1, JSON bodies, HTTP Bearer auth with reveal-once environment-bound tokens '
  name: Scanverity Resolution API
  slug: scanverity-resolution-api
artifact_total: 8
asyncapis:
- description: ''
  name: Scanverity Resolution Api Webhooks
  slug: scanverity-resolution-api-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scanverity-resolution-api-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://scanverity.com/en/resolution-api
- group: docs
  title: ''
  type: Documentation
  url: https://scanverity.com/resolution-api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://scanverity.com/resolution-api/docs
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scanverity-resolution-api-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/scanverity-resolution-api-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/scanverity-resolution-api-api-catalog.json
- group: other
  title: ''
  type: X-APIsJSON
  url: https://scanverity.com/apis.json
- group: commercial
  title: ''
  type: Pricing
  url: https://scanverity.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://scanverity.com/en/signup
- group: start
  title: ''
  type: Login
  url: https://scanverity.com/en/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scanverity.com/en/legal/resolution-api-addendum
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scanverity.com/en/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://scanverity.com/en/contact
- group: company
  title: ''
  type: Blog
  url: https://scanverity.com/research
- group: company
  title: ''
  type: BlogRSS
  url: https://scanverity.com/feed.xml
created: '2026-09-04'
description: An independent Polymarket intelligence platform, operated by KotIQ OÜ, providing resolution-risk assessments on prediction markets through a documented OpenAPI 3.1 REST API. Resolution risk is the chance a market settles in a way its title does not lead a reader to expect — ambiguous rule language, an unverifiable resolution source, or a title that diverges from the rules. The API is an async create-and-poll surface with signed webhooks, a deterministic sandbox fixture catalog, a reconciled usage ledger, four deny-by-default token scopes and a required Idempotency-Key on its only billable write. The contract, an APIs.json index and an RFC 9727 api-catalog are all publicly retrievable; runtime access is private beta and feature-gated, so live calls require an entitled, allowlisted account. Read-only research only — no order placement, no custody, no trading advice.
examples:
- key_count: 7
  name: Scanverity Resolution Api Examples
  slug: scanverity-resolution-api-examples
image: https://scanverity.com/icon-512.png
layout: provider
modified: '2026-09-04'
name: Scanverity Resolution API
nav: Providers
network: true
overview: 'Scanverity Resolution API publishes 1 API on the [APIs.io](https://apis.io/) network: Scanverity Resolution API. Tagged areas include Prediction Markets, Resolution Risk, Market Intelligence, Due Diligence, and Webhooks.


  The Scanverity Resolution API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Scanverity Resolution API''s developer surface includes documentation, API reference, pricing, signup flow, support, engineering blog, and 10 more developer resources.'
plans:
- name: Scanverity Resolution Api Plans Pricing
  plan_count: 6
  slug: scanverity-resolution-api-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Scanverity Resolution Api Rate Limits
  slug: scanverity-resolution-api-rate-limits
scopes:
- name: Scanverity Resolution Api Scopes
  scope_count: 0
  slug: scanverity-resolution-api-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 71.5
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 57.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Scanverity Resolution Api Authentication
  slug: scanverity-resolution-api-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Scanverity Resolution Api Domain Security
  slug: scanverity-resolution-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scanverity-resolution-api
tags:
- Prediction Markets
- Resolution Risk
- Market Intelligence
- Due Diligence
- Webhooks
- OpenAPI
- Fintech
- Risk Analytics
- Polymarket
- Event Contracts
- Agent Ready
website: https://scanverity.com/en/resolution-api
---
