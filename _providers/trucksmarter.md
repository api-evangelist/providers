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
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Trucksmarter Agentic Access
  operation_count: 2
  slug: trucksmarter-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.trucksmarter.com
  baseurl_source: declared
  description: Post, update, and remove freight loads on the TruckSmarter load board.
  name: TruckSmarter Loads API
  slug: trucksmarter-loads-api
arazzos:
- description: Post a batch of freight loads to the TruckSmarter load board via the partner Load Posting API, then remove them by loadId once they are covered or cancelled.
  name: Post loads to TruckSmarter and remove them once covered
  slug: trucksmarter-post-and-remove-loads
artifact_total: 7
collections:
- collection_type: open
  name: TruckSmarter Load Posting Loads API
  slug: open-trucksmarter-loads-api
common:
- group: other
  href: https://artifacts.apis.io/trucksmarter/overlays/trucksmarter-load-posting-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/trucksmarter-load-posting-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.trucksmarter.com/
- group: docs
  title: ''
  type: Documentation
  url: https://trucksmarter.notion.site/TruckSmarter-API-Load-Posting-Documentation-2014aa4e9bc580fe80cfe87e18516dea
- group: docs
  title: ''
  type: APIReference
  url: https://trucksmarter.notion.site/TruckSmarter-API-Load-Posting-Documentation-2014aa4e9bc580fe80cfe87e18516dea
- group: operate
  title: ''
  type: Support
  url: https://help.trucksmarter.com/
- group: company
  title: ''
  type: Blog
  url: https://www.trucksmarter.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trucksmarter.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trucksmarter.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trucksmarter.com/legal/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://app.trucksmarter.com/auth/signup
- group: start
  title: ''
  type: Login
  url: https://app.trucksmarter.com/auth/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TruckSmarter
- group: auth
  href: https://artifacts.apis.io/trucksmarter/authentication/trucksmarter-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trucksmarter-authentication.yml
- group: agent
  href: https://artifacts.apis.io/trucksmarter/llms/trucksmarter-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trucksmarter-llms.txt
- group: agent
  href: https://artifacts.apis.io/trucksmarter/mcp/trucksmarter-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/trucksmarter-mcp.yml
- group: design
  href: https://artifacts.apis.io/trucksmarter/conventions/trucksmarter-conventions.yml
  title: ''
  type: Conventions
  url: conventions/trucksmarter-conventions.yml
- group: design
  href: https://artifacts.apis.io/trucksmarter/conventions/trucksmarter-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/trucksmarter-conventions.yml
- group: design
  href: https://artifacts.apis.io/trucksmarter/errors/trucksmarter-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trucksmarter-problem-types.yml
- group: design
  href: https://artifacts.apis.io/trucksmarter/data-model/trucksmarter-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trucksmarter-data-model.yml
- group: design
  href: https://artifacts.apis.io/trucksmarter/conformance/trucksmarter-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trucksmarter-conformance.yml
- group: design
  href: https://artifacts.apis.io/trucksmarter/lifecycle/trucksmarter-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/trucksmarter-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/trucksmarter/packages/trucksmarter-packages.yml
  title: ''
  type: Packages
  url: packages/trucksmarter-packages.yml
- group: agent
  href: https://artifacts.apis.io/trucksmarter/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/trucksmarter/arazzo/trucksmarter-post-and-remove-loads.yml
  title: ''
  type: Arazzo
  url: arazzo/trucksmarter-post-and-remove-loads.yml
- group: agent
  href: https://artifacts.apis.io/trucksmarter/agentic-access/trucksmarter-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trucksmarter-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/trucksmarter/security/trucksmarter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trucksmarter-domain-security.yml
created: '2026-07-17'
description: TruckSmarter is a free load board and AI dispatch platform for truck drivers and owner operators, surfacing 100K+ daily available loads with no subscription fees, alongside fuel savings and factoring services and a chat-based AI dispatcher (Dispatch). Brokers post loads and book carriers through a broker portal, CSV/Excel upload, or the partner Load Posting API, which lets partners programmatically create, update, and remove freight loads using a Bearer API key.
image: https://framerusercontent.com/images/NWzlselGeh333d7PEqt7C8Ap9Mg.png
layout: provider
modified: '2026-07-21'
name: TruckSmarter
nav: Providers
network: true
overview: 'TruckSmarter publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Loads API. Tagged areas include Trucking, Freight, Logistics, Load Board, and Transportation.


  TruckSmarter''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 19 more developer resources.'
random_paper: 23
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 15.1
    developer_ergonomics: 37.5
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/trucksmarter/trucksmarter-2026-08-17T082446.png
security:
- kind: authentication
  name: Trucksmarter Authentication
  slug: trucksmarter-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Trucksmarter Domain Security
  slug: trucksmarter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Post and manage loads on TruckSmarter
  slug: trucksmarter-post-and-manage-loads
slug: trucksmarter
tags:
- Trucking
- Freight
- Logistics
- Load Board
- Transportation
- Dispatch
- Fuel
- Factoring
website: https://www.trucksmarter.com/
---
