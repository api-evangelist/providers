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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
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
  score: 25.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Oximy Agentic Access
  operation_count: 4
  slug: oximy-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.oximy.com
  baseurl_source: declared
  description: Project bootstrap — settings and policy configuration.
  name: Oximy Init API
  slug: oximy-init-api
- baseURL: https://api.oximy.com
  baseurl_source: declared
  description: Policy configuration and server-side rule evaluation.
  name: Oximy Policy API
  slug: oximy-policy-api
- baseURL: https://api.oximy.com
  baseurl_source: declared
  description: LLM request/response event ingestion.
  name: Oximy Telemetry API
  slug: oximy-telemetry-api
artifact_total: 13
collections:
- collection_type: open
  name: Oximy Public Init API
  slug: open-oximy-init-api
- collection_type: open
  name: Oximy Public Init Policy API
  slug: open-oximy-policy-api
- collection_type: open
  name: Oximy Public Init Telemetry API
  slug: open-oximy-telemetry-api
common:
- group: other
  href: https://artifacts.apis.io/oximy/capabilities/oximy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/oximy-capability-edges.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://oximy.com/pricing
- group: commercial
  href: https://artifacts.apis.io/oximy/plans/oximy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/oximy-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/oximy/overlays/oximy-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oximy-public-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://oximy.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.oximy.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oximy.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oximy.com/docs/developer/public-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oximy.com/docs/developer/public-api
- group: company
  title: ''
  type: Blog
  url: https://oximy.com/blog
- group: operate
  title: ''
  type: Support
  url: https://oximy.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oximy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oximy.com/privacy
- group: build
  href: https://artifacts.apis.io/oximy/packages/oximy-packages.yml
  title: ''
  type: Packages
  url: packages/oximy-packages.yml
- group: build
  href: https://artifacts.apis.io/oximy/packages/oximy-packages.yml
  title: ''
  type: SDKs
  url: packages/oximy-packages.yml
- group: agent
  href: https://artifacts.apis.io/oximy/mcp/oximy-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/oximy-mcp.yml
- group: agent
  href: https://artifacts.apis.io/oximy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/oximy/llms/oximy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/oximy-llms.txt
- group: agent
  href: https://artifacts.apis.io/oximy/well-known/oximy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/oximy-well-known.yml
- group: design
  href: https://artifacts.apis.io/oximy/conventions/oximy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/oximy-conventions.yml
- group: design
  href: https://artifacts.apis.io/oximy/errors/oximy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/oximy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/oximy/lifecycle/oximy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/oximy-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/oximy/changelog/oximy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/oximy-changelog.yml
- group: design
  href: https://artifacts.apis.io/oximy/conformance/oximy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/oximy-conformance.yml
- group: design
  href: https://artifacts.apis.io/oximy/data-model/oximy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/oximy-data-model.yml
- group: agent
  href: https://artifacts.apis.io/oximy/agentic-access/oximy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/oximy-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/oximy/security/oximy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oximy-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/oximy/authentication/oximy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/oximy-authentication.yml
created: '2026-07-17'
description: Oximy is an AI adoption and governance platform — "the AI adoption engine for every company." It gives organizations visibility into how their people and applications use AI tools across the enterprise (tracking thousands of AI tools across categories), surfaces risks and recommendations, and lets teams ask natural-language questions about their AI usage. For developers, Oximy ships a Public API (https://api.oximy.com) and an official TypeScript SDK that wrap any OpenAI-compatible client to capture zero-overhead LLM telemetry and enforce usage policy inline — PII detection and redaction, prompt-injection detection, deny/allow lists, and token/cost/rate limits. Backed by Y Combinator (W26) and Blume Ventures; founded by Naman Ambavi.
finops:
- has_sources: true
  method: derived
  name: Oximy Finops
  primary_unit: device
  service_category: ''
  slug: oximy-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oximy.png
layout: provider
modified: '2026-07-20'
name: Oximy
nav: Providers
network: true
overview: 'Oximy publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Init API, Policy API, and Telemetry API. Tagged areas include Company, AI Governance, LLM Observability, AI Adoption, and Telemetry.


  Oximy''s developer surface includes pricing, documentation, API reference, getting-started guide, engineering blog, support, changelog, and 21 more developer resources.'
plans:
- name: Oximy Plans Pricing
  plan_count: 3
  slug: oximy-plans-pricing
random_paper: 14
score:
  band: developing
  composite: 51.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 71.1
    contract_governance: 4.5
    contract_quality: 52.7
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 15.8
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/oximy/oximy-2026-08-07T191209.png
security:
- kind: authentication
  name: Oximy Authentication
  slug: oximy-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Oximy Domain Security
  slug: oximy-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Evaluate content against Oximy policy
  slug: oximy-evaluate-content-policy
- name: Instrument LLM telemetry with Oximy
  slug: oximy-instrument-llm-telemetry
slug: oximy
tags:
- Company
- AI Governance
- LLM Observability
- AI Adoption
- Telemetry
- Policy Enforcement
- Artificial Intelligence
- Developer Tools
website: https://oximy.com
---
