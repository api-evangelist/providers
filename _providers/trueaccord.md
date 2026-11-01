---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Trueaccord Agentic Access
  operation_count: 6
  slug: trueaccord-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://api.trueaccord.com/api/v1
  baseurl_source: declared
  description: Create, retrieve, and manage customers (consumers) and their debts.
  name: TrueAccord Customers API
  slug: trueaccord-customers-api
artifact_total: 6
collections:
- collection_type: open
  name: TrueAccord Recover Customers API
  slug: open-trueaccord-customers-api
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trueaccord.com/
- group: commercial
  href: https://artifacts.apis.io/trueaccord/plans/trueaccord-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trueaccord-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.trueaccord.com/press
- group: company
  title: ''
  type: BlogRSS
  url: https://www.trueaccord.com/feed/
- group: other
  href: https://artifacts.apis.io/trueaccord/capabilities/trueaccord-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/trueaccord-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.trueaccord.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.trueaccord.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trueaccord.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.trueaccord.com/recover/recover-api-reference
- group: company
  title: ''
  type: Blog
  url: https://blog.trueaccord.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trueaccord.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trueaccord.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.trueaccord.com/it-security
- group: auth
  href: https://artifacts.apis.io/trueaccord/authentication/trueaccord-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trueaccord-authentication.yml
- group: design
  href: https://artifacts.apis.io/trueaccord/conventions/trueaccord-conventions.yml
  title: ''
  type: Conventions
  url: conventions/trueaccord-conventions.yml
- group: design
  href: https://artifacts.apis.io/trueaccord/conventions/trueaccord-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/trueaccord-conventions.yml
- group: design
  href: https://artifacts.apis.io/trueaccord/errors/trueaccord-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trueaccord-problem-types.yml
- group: design
  href: https://artifacts.apis.io/trueaccord/lifecycle/trueaccord-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/trueaccord-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/trueaccord/conformance/trueaccord-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trueaccord-conformance.yml
- group: design
  href: https://artifacts.apis.io/trueaccord/data-model/trueaccord-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trueaccord-data-model.yml
- group: agent
  href: https://artifacts.apis.io/trueaccord/mcp/trueaccord-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/trueaccord-mcp.yml
- group: agent
  href: https://artifacts.apis.io/trueaccord/llms/trueaccord-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trueaccord-llms.txt
- group: other
  href: https://artifacts.apis.io/trueaccord/overlays/trueaccord-recover-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/trueaccord-recover-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/trueaccord/agentic-access/trueaccord-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trueaccord-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/trueaccord/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: TrueAccord is a digital-first, omnichannel debt collection agency that uses data science and machine learning to recover consumer debt with a consumer-friendly, self-service experience. Through its Recover API, creditors and debt buyers place consumers and their debts for collection and manage customer records — customers, their contact information (addresses, phones, emails), and the debts placed against them — over a simple HTTPS interface secured with HTTP Basic authentication (API key as username) plus an X-TA-CREDITOR header for multi-creditor accounts. TrueAccord also operates first-party collections through its Sentry Credit subsidiary and its HeartBeat and HumAIn platforms, and is ISO 27001 certified.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trueaccord.png
layout: provider
modified: '2026-10-06'
name: TrueAccord
nav: Providers
network: true
overview: 'TrueAccord publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Customers API. Tagged areas include Company, Debt Collection, Financial Services, Fintech, and Machine Learning.


  TrueAccord''s developer surface includes pricing, engineering blog, documentation, API reference, authentication, and 20 more developer resources.'
plans:
- name: Trueaccord Plans Pricing
  plan_count: 0
  slug: trueaccord-plans-pricing
random_paper: 12
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    contract_governance: 4.5
    contract_quality: 52.0
    developer_ergonomics: 42.3
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 37.5
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
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/trueaccord/trueaccord-2026-09-02T164334.png
security:
- kind: authentication
  name: Trueaccord Authentication
  slug: trueaccord-authentication
  summary_line: http · 1 scheme
skill_count: 1
skills:
- name: Place a customer and debt, then track it
  slug: trueaccord-place-and-track-debt
slug: trueaccord
tags:
- Company
- Debt Collection
- Financial Services
- Fintech
- Machine Learning
- Collection
- Consumer Finance
website: https://www.trueaccord.com
---
