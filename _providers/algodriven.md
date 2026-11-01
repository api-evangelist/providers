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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
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
  score: 24.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Algodriven Agentic Access
  operation_count: 2
  slug: algodriven-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://algodriven.io/v1
  baseurl_source: declared
  description: Generate and retrieve GCC/UAE vehicle history reports as PDF.
  name: AlgoDriven Vehicle History Report API
  slug: algodriven-vehicle-history-report-api
arazzos:
- description: Generate a GCC/UAE vehicle history report for a VIN, then poll until the PDF report URL is available.
  name: AlgoDriven — generate and retrieve a UAE vehicle history report
  slug: algodriven-vehicle-history-report
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-algodriven-vehicle-history-postman
- collection_type: open
  name: AlgoDriven - UAE Vehicle History Report API
  slug: open-algodriven-vehicle-history-report-api
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://algodriven.xyz/insights/
- group: commercial
  href: https://artifacts.apis.io/algodriven/plans/algodriven-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/algodriven-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://algodriven.xyz/insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://algodriven.xyz/feed.xml
- group: other
  href: https://artifacts.apis.io/algodriven/overlays/algodriven-vehicle-history-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/algodriven-vehicle-history-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/algodriven/security/algodriven-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/algodriven-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/algodriven/agentic-access/algodriven-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/algodriven-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/algodriven/authentication/algodriven-authentication.yml
  title: ''
  type: Authentication
  url: authentication/algodriven-authentication.yml
- group: design
  href: https://artifacts.apis.io/algodriven/conventions/algodriven-conventions.yml
  title: ''
  type: Conventions
  url: conventions/algodriven-conventions.yml
- group: design
  href: https://artifacts.apis.io/algodriven/lifecycle/algodriven-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/algodriven-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/algodriven/conformance/algodriven-conformance.yml
  title: ''
  type: Conformance
  url: conformance/algodriven-conformance.yml
- group: design
  href: https://artifacts.apis.io/algodriven/data-model/algodriven-data-model.yml
  title: ''
  type: DataModel
  url: data-model/algodriven-data-model.yml
- group: agent
  href: https://artifacts.apis.io/algodriven/mcp/algodriven-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/algodriven-mcp.yml
- group: agent
  href: https://artifacts.apis.io/algodriven/llms/algodriven-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/algodriven-llms.txt
- group: agent
  href: https://artifacts.apis.io/algodriven/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: https://api.algodriven.xyz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://algodriven.xyz/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://algodriven.xyz/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://api.algodriven.xyz/
- group: company
  title: ''
  type: Blog
  url: https://algodriven.xyz/resources/
- group: operate
  title: ''
  type: Support
  url: https://algodriven.xyz/contact-us/
- group: start
  title: ''
  type: Login
  url: https://dashboard.algodriven.co
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://algodriven.xyz/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/algodriven
- group: company
  title: ''
  type: Website
  url: https://algodriven.xyz
created: '2026-07-17'
description: AlgoDriven is an automotive AI company that helps car dealerships, banks, insurers, fleet operators, marketplaces, and OEMs appraise, inspect, and price used vehicles using proprietary data-driven applications. Its products include EvalExpert (automated car valuation and price guide built on millions of data points), DriveExpert (test-drive, loan-car, and staff-car management with analytics), and InspectExpert (customised vehicle inspection software), backed by developer APIs for vehicle search and data, valuations, specifications, and vehicle history reports. Founded in 2017 and expanded across the MENA region, New Zealand, and beyond, AlgoDriven runs offices in Australia, the UAE, and Egypt, and is a portfolio company of 500 Global.
image: https://algodriven.xyz/wp-content/uploads/2022/04/cropped-algodriven-favicon-192x192.png
layout: provider
modified: '2026-10-06'
name: AlgoDriven
nav: Providers
network: true
overview: 'AlgoDriven publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Vehicle History Report API. Tagged areas include Company, Automotive, Vehicle Data, Car Valuation, and Vehicle Inspection.


  AlgoDriven''s developer surface includes pricing, engineering blog, authentication, documentation, API reference, support, and 19 more developer resources.'
plans:
- name: Algodriven Plans Pricing
  plan_count: 0
  slug: algodriven-plans-pricing
random_paper: 11
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 49.0
    developer_ergonomics: 51.8
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/algodriven/algodriven-2026-07-25T195602.png
security:
- kind: authentication
  name: Algodriven Authentication
  slug: algodriven-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Algodriven Domain Security
  slug: algodriven-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Generate and retrieve a UAE vehicle history report
  slug: algodriven-generate-vehicle-history-report
slug: algodriven
tags:
- Company
- Automotive
- Vehicle Data
- Car Valuation
- Vehicle Inspection
- Artificial Intelligence
- Vehicle History
- Automotive Data Intelligence
website: https://algodriven.xyz
---
