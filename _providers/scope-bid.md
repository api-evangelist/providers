---
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 12
  human_in_the_loop: 6
  name: Scope Bid Agentic Access
  operation_count: 23
  slug: scope-bid-agentic-access
  summary_line: 23 operations · 12 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://scope.bid
  baseurl_source: declared
  description: The Carrier Feed API from scope-bid — 1 operation(s) for carrier feed.
  name: scope-bid Carrier Feed API
  slug: scope-bid-carrier-feed-api
- baseURL: https://scope.bid
  baseurl_source: declared
  description: The Deliverables API from scope-bid — 1 operation(s) for deliverables.
  name: scope-bid Deliverables API
  slug: scope-bid-deliverables-api
- baseURL: https://scope.bid
  baseurl_source: declared
  description: The Dispatches API from scope-bid — 3 operation(s) for dispatches.
  name: scope-bid Dispatches API
  slug: scope-bid-dispatches-api
- baseURL: https://scope.bid
  baseurl_source: declared
  description: The Exports API from scope-bid — 2 operation(s) for exports.
  name: scope-bid Exports API
  slug: scope-bid-exports-api
- baseURL: https://scope.bid
  baseurl_source: declared
  description: The Insights API from scope-bid — 1 operation(s) for insights.
  name: scope-bid Insights API
  slug: scope-bid-insights-api
- baseURL: https://scope.bid
  baseurl_source: declared
  description: The Matters API from scope-bid — 1 operation(s) for matters.
  name: scope-bid Matters API
  slug: scope-bid-matters-api
- baseURL: https://scope.bid
  baseurl_source: declared
  description: The Partner Authorizations API from scope-bid — 1 operation(s) for partner authorizations.
  name: scope-bid Partner Authorizations API
  slug: scope-bid-partner-authorizations-api
- baseURL: https://scope.bid
  baseurl_source: declared
  description: The Scopes API from scope-bid — 2 operation(s) for scopes.
  name: scope-bid Scopes API
  slug: scope-bid-scopes-api
- baseURL: https://scope.bid
  baseurl_source: declared
  description: The Vendors API from scope-bid — 2 operation(s) for vendors.
  name: scope-bid Vendors API
  slug: scope-bid-vendors-api
- baseURL: https://scope.bid
  baseurl_source: declared
  description: The Webhooks API from scope-bid — 2 operation(s) for webhooks.
  name: scope-bid Webhooks API
  slug: scope-bid-webhooks-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/scope-bid/agentic-access/scope-bid-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/scope-bid-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/scope-bid/plans/scope-bid-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scope-bid-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/scope-bid/rules/scope-bid-rules.yml
  title: ''
  type: Spectral
  url: rules/scope-bid-rules.yml
- group: auth
  title: ''
  type: Compliance
  url: https://scope.bid/trust
- group: design
  href: https://artifacts.apis.io/scope-bid/errors/scope-bid-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scope-bid-problem-types.yml
- group: design
  href: https://artifacts.apis.io/scope-bid/conformance/scope-bid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scope-bid-conformance.yml
- group: agent
  href: https://artifacts.apis.io/scope-bid/llms/scope-bid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scope-bid-llms.txt
- group: agent
  href: https://artifacts.apis.io/scope-bid/well-known/scope-bid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scope-bid-well-known.yml
- group: other
  href: https://artifacts.apis.io/scope-bid/hosts/scope-bid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scope-bid-hosts.yml
- group: other
  href: https://artifacts.apis.io/scope-bid/vendors/scope-bid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scope-bid-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://scope.bid/status
- group: auth
  title: ''
  type: Security
  url: https://scope.bid/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scope.bid/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://scope.bid/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://scope.bid/press
- group: start
  title: ''
  type: Login
  url: https://scope.bid/login
- group: docs
  title: ''
  type: Documentation
  url: https://scope.bid/docs
- group: docs
  title: ''
  type: APIReference
  url: https://scope.bid/developers/api
- group: auth
  href: https://artifacts.apis.io/scope-bid/authentication/scope-bid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scope-bid-authentication.yml
- group: auth
  href: https://artifacts.apis.io/scope-bid/security/scope-bid-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/scope-bid-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/scope-bid/security/scope-bid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scope-bid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scope.bid/
created: '2026-10-29'
description: Scope Bid is a technology company that provides a platform for managing construction bids and contracts. The service enables contractors, subcontractors, and owners to streamline the bidding process, track bid submissions, and collaborate on project documentation. By offering real-time analytics, secure document storage, and integration with popular construction management tools, Scope Bid aims to improve transparency, reduce administrative overhead, and accelerate project delivery across the construction industry.
image: https://scope.bid/opengraph-image?ffa207befa59053c
layout: provider
modified: '2026-10-29'
name: scope-bid
nav: Providers
network: true
overview: 'scope-bid publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Carrier Feed API, Deliverables API, Dispatches API, and 7 more. Tagged areas include Construction, Bidding, SaaS, Collaboration, and Analytics.


  The scope-bid catalog on APIs.io includes 1 Spectral governance ruleset.


  scope-bid''s developer surface includes pricing, documentation, API reference, authentication, and 18 more developer resources.'
plans:
- name: Scope Bid Plans Pricing
  plan_count: 1
  slug: scope-bid-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: scope-bid API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: scope-bid-rules
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 31.8
    contract_quality: 47.8
    developer_ergonomics: 28.6
    discoverability: 67.9
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Scope Bid Authentication
  slug: scope-bid-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Scope Bid Domain Security
  slug: scope-bid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Scope Bid Trust Center
  slug: scope-bid-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: scope-bid
tags:
- Construction
- Bidding
- SaaS
- Collaboration
- Analytics
website: https://scope.bid/
---
