---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Origin Agentic Access
  operation_count: 3
  slug: origin-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://airbrush.originmarkets.com/v3
  baseurl_source: declared
  description: The Trades API from Origin — 3 operation(s) for trades.
  name: Origin Trades API
  slug: origin-trades-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trades API
  slug: open-origin-trades-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/origin-capability-edges.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/origin-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/origin-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/origin-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/origin-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/origin-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/origin-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/origin-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/origin-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/origin-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/origin-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/origin-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/origin-airbrush-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://originmarkets.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://login2.originmarkets.com/api/v1/
- group: docs
  title: ''
  type: Documentation
  url: https://airbrush.originmarkets.com/v3/
- group: docs
  title: ''
  type: APIReference
  url: https://airbrush.originmarkets.com/v3/
- group: company
  title: ''
  type: Blog
  url: https://originmarkets.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OriginMarkets/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.originmarkets.com/
- group: operate
  title: ''
  type: Support
  url: https://originmarkets.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://originmarkets.com/privacy-policy
- group: company
  title: ''
  type: About
  url: https://originmarkets.com/about
created: '2026-07-17'
description: Origin (Origin Markets) is a digital debt capital markets (DCM) platform that automates bond issuance from front to back, connecting issuers, dealers, lawyers, and market infrastructure on a single platform. Its products cover automated transaction Documentation (termsheets and final terms with collaborative review and e-signing), Structured Notes, and a Marketplace database of 1,000+ issuers. Origin publishes a read-only Trades API and the open Airbrush "universal data language" (an ISO 20022-aligned OpenAPI specification) for post-trade straight-through processing across the ecosystem.
examples:
- key_count: 41
  name: Origin Termsheet Fixed_Rate
  slug: origin-termsheet-fixed_rate
- key_count: 41
  name: Origin Termsheet Floating_Rate
  slug: origin-termsheet-floating_rate
- key_count: 35
  name: Origin Termsheet Zero_Coupon
  slug: origin-termsheet-zero_coupon
image: https://originmarkets.com/universal/svg/social-accounts.svg
layout: provider
modified: '2026-07-20'
name: Origin
nav: Providers
network: true
overview: 'Origin publishes 1 API on the [APIs.io](https://apis.io/) network: Trades API. Tagged areas include Company, Financial-Services, Capital Markets, Bond Issuance, and Debt Capital Markets.


  Origin''s developer surface includes authentication, changelog, documentation, API reference, engineering blog, support, and 18 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.6
    commercial_clarity: 28.6
    contract_governance: 4.5
    contract_quality: 44.9
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 38.9
  provenance:
    agentic_access: derived
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
screenshot: https://raw.githubusercontent.com/api-evangelist/origin/refs/heads/main/screenshots/origin-2026-08-07T190930.png
security:
- kind: authentication
  name: Origin Authentication
  slug: origin-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Origin Domain Security
  slug: origin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: origin
tags:
- Company
- Financial-Services
- Capital Markets
- Bond Issuance
- Debt Capital Markets
- Fixed Income
- Post-Trade
- ISO 20022
- Fintech
- Straight-Through Processing
website: https://originmarkets.com/
---
