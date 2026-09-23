---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.8
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 9
  human_in_the_loop: 2
  name: Enfuce Agentic Access
  operation_count: 12
  slug: enfuce-agentic-access
  summary_line: 12 operations · 9 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.{{tenant}}.eu.live.prod.mycore.enfuce.com/issuer
  baseurl_source: declared
  description: The Authorisation Request API API from Enfuce — 1 operation(s) for authorisation request api.
  name: Enfuce Authorisation Request API
  slug: enfuce-authorisation-request-api-api
- baseURL: https://api.{{tenant}}.eu.live.prod.mycore.enfuce.com/issuer
  baseurl_source: declared
  description: Endpoints for creating a card
  name: Enfuce Create Card API
  slug: enfuce-create-card-api
- baseURL: https://api.{{tenant}}.eu.live.prod.mycore.enfuce.com/issuer
  baseurl_source: declared
  description: The Create PIN Control access token API from Enfuce — 1 operation(s) for create pin control access token.
  name: Enfuce Create PIN Control access token API
  slug: enfuce-create-pin-control-access-token-api
- baseURL: https://api.{{tenant}}.eu.live.prod.mycore.enfuce.com/issuer
  baseurl_source: declared
  description: Endpoints for fetching a card
  name: Enfuce Get card API
  slug: enfuce-get-card-api
- baseURL: https://api.{{tenant}}.eu.live.prod.mycore.enfuce.com/issuer
  baseurl_source: declared
  description: The Get Card Payment Info API from Enfuce — 1 operation(s) for get card payment info.
  name: Enfuce Get Card Payment Info API
  slug: enfuce-get-card-payment-info-api
- baseURL: https://api.{{tenant}}.eu.live.prod.mycore.enfuce.com/issuer
  baseurl_source: declared
  description: The Get plastic manufacturing history API from Enfuce — 1 operation(s) for get plastic manufacturing history.
  name: Enfuce Get plastic manufacturing history API
  slug: enfuce-get-plastic-manufacturing-history-api
- baseURL: https://api.{{tenant}}.eu.live.prod.mycore.enfuce.com/issuer
  baseurl_source: declared
  description: Endpoints for updating a card
  name: Enfuce Update card API
  slug: enfuce-update-card-api
artifact_total: 11
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/enfuce/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/enfuce/refs/heads/main/agentic-access/enfuce-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/enfuce-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/enfuce/refs/heads/main/rate-limits/enfuce-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/enfuce-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/enfuce/refs/heads/main/data-model/enfuce-data-model.yml
  title: ''
  type: DataModel
  url: data-model/enfuce-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/enfuce/refs/heads/main/changelog/enfuce-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/enfuce-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/enfuce/refs/heads/main/conventions/enfuce-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/enfuce-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/enfuce/refs/heads/main/conventions/enfuce-conventions.yml
  title: ''
  type: Conventions
  url: conventions/enfuce-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/enfuce/refs/heads/main/errors/enfuce-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/enfuce-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/enfuce/refs/heads/main/conformance/enfuce-conformance.yml
  title: ''
  type: Conformance
  url: conformance/enfuce-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/enfuce/refs/heads/main/overlays/enfuce-advanced-spend-control-v1-overlay.yml
  title: ''
  type: Overlay
  url: overlays/enfuce-advanced-spend-control-v1-overlay.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/enfuce/refs/heads/main/llms/enfuce-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/enfuce-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/enfuce/refs/heads/main/a2a/enfuce-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/enfuce-a2a.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.enfuce.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://enfuce.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://enfuce.com/who-we-are/newsroom
- group: start
  title: ''
  type: Login
  url: https://console.myedge.enfuce.com/signin
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.enfuce.com/updates/release-notes
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/enfuce/refs/heads/main/authentication/enfuce-authentication.yml
  title: ''
  type: Authentication
  url: authentication/enfuce-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/enfuce/refs/heads/main/security/enfuce-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/enfuce-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://enfuce.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.enfuce.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.enfuce.com/payment/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.enfuce.com/guides/start-developing-with-enfuce.md
- group: company
  title: ''
  type: Blog
  url: https://enfuce.com/blog
- group: operate
  title: ''
  type: Support
  url: https://enfuce.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://enfuce.com/privacy-and-data-protection
- group: commercial
  title: ''
  type: TermsOfService
  url: https://enfuce.com/website-terms-of-use
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/enfuce
created: '2026-09-21'
description: Enfuce provides a cloud‑native, tenant‑isolated, API‑first platform for card issuing, processing, licensing, ledger, fraud & dispute management, and data analytics. It serves banks, fintechs, fleet providers and enterprises, offering real‑time decisioning at scale, modular services, and compliance with PSD3, DORA and AMLA standards.
image: https://enfuce.com/uploads/Product-images/_1200x630_crop_center-center_82_none/resized_2552x1436.png?mtime=1788270445
layout: provider
modified: '2026-09-21'
name: Enfuce
nav: Providers
network: true
overview: 'Enfuce publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authorisation Request API, Create Card API, Create PIN Control access token API, and 4 more. Tagged areas include Company, Payments, Card Issuing, Fintech, and API Platform.


  Enfuce''s developer surface includes changelog, pricing, authentication, documentation, API reference, getting-started guide, engineering blog, and 21 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 2
  name: Enfuce Rate Limits
  slug: enfuce-rate-limits
score:
  band: developing
  composite: 52.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 55.5
    developer_ergonomics: 49.4
    discoverability: 75.9
    operational_transparency: 57.9
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 51.6
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Enfuce Authentication
  slug: enfuce-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Enfuce Domain Security
  slug: enfuce-domain-security
  summary_line: TLSv1.3 · DMARC
slug: enfuce
tags:
- Company
- Payments
- Card Issuing
- Fintech
- API Platform
website: https://enfuce.com/
---
