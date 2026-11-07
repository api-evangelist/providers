---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 3
  name: Lastscanned Com Agentic Access
  operation_count: 25
  slug: lastscanned-com-agentic-access
  summary_line: 25 operations · 10 acting · 3 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.lastscanned.com
  baseurl_source: declared
  description: The Account API from lastscanned — 5 operation(s) for account.
  name: lastscanned Account API
  slug: lastscanned-com-account-api
- baseURL: https://api.lastscanned.com
  baseurl_source: declared
  description: The Carriers API from lastscanned — 1 operation(s) for carriers.
  name: lastscanned Carriers API
  slug: lastscanned-com-carriers-api
- baseURL: https://api.lastscanned.com
  baseurl_source: declared
  description: The Track API from lastscanned — 2 operation(s) for track.
  name: lastscanned Track API
  slug: lastscanned-com-track-api
- baseURL: https://api.lastscanned.com
  baseurl_source: declared
  description: The Tracking API from lastscanned — 3 operation(s) for tracking.
  name: lastscanned Tracking API
  slug: lastscanned-com-tracking-api
- baseURL: https://api.lastscanned.com
  baseurl_source: declared
  description: The Watches API from lastscanned — 2 operation(s) for watches.
  name: lastscanned Watches API
  slug: lastscanned-com-watches-api
- baseURL: https://api.lastscanned.com
  baseurl_source: declared
  description: The Webhooks API from lastscanned — 6 operation(s) for webhooks.
  name: lastscanned Webhooks API
  slug: lastscanned-com-webhooks-api
artifact_total: 15
asyncapis:
- description: ''
  name: Lastscanned Com Webhooks
  slug: lastscanned-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/lastscanned-com/agentic-access/lastscanned-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lastscanned-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/lastscanned-com/plans/lastscanned-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lastscanned-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/lastscanned-com/rules/lastscanned-com-rules.yml
  title: ''
  type: Spectral
  url: rules/lastscanned-com-rules.yml
- group: design
  href: https://artifacts.apis.io/lastscanned-com/json-ld/lastscanned-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lastscanned-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/lastscanned-com/vocabulary/lastscanned-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lastscanned-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/lastscanned-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/lastscanned-com/asyncapi/lastscanned-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lastscanned-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/lastscanned-com/data-model/lastscanned-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lastscanned-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/lastscanned-com/authentication/lastscanned-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lastscanned-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/lastscanned-com/errors/lastscanned-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lastscanned-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lastscanned-com/conformance/lastscanned-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lastscanned-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lastscanned-com/llms/lastscanned-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lastscanned-com-llms.txt
- group: other
  href: https://artifacts.apis.io/lastscanned-com/a2a/lastscanned-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/lastscanned-com-a2a.yml
- group: other
  href: https://artifacts.apis.io/lastscanned-com/hosts/lastscanned-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lastscanned-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/lastscanned-com/vendors/lastscanned-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lastscanned-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lastscanned.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://lastscanned.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lastscanned.com/privacy
- group: start
  title: ''
  type: Login
  url: https://app.lastscanned.com/login
- group: auth
  href: https://artifacts.apis.io/lastscanned-com/security/lastscanned-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lastscanned-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lastscanned.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lastscanned.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lastscanned.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lastscanned.com
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.lastscanned.com/#pricing
created: '2026-10-29'
description: lastscanned provides a Package Tracking API and an MCP server that supports integration with 542 carriers worldwide. It offers real‑time tracking number lookup, bulk CSV and batch tracking, webhook notifications, and AI‑agent enabled tracking with keyless Stripe MPP 402 support. The service includes detailed carrier auto‑detection, pricing plans, and extensive documentation for developers.
image: https://lastscanned.com/opengraph-image.png?opengraph-image.34e8ufk3hu7w5.png
jsonld:
- class_count: 11
  name: Lastscanned Com Context
  property_count: 42
  slug: lastscanned-com-context
layout: provider
modified: '2026-10-29'
name: lastscanned
nav: Providers
network: true
overview: 'lastscanned publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Carriers API, Track API, and 3 more. Tagged areas include Company, Tracking, Logistics, and MCP.


  The lastscanned catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  lastscanned''s developer surface includes authentication, documentation, API reference, pricing, and 21 more developer resources.'
plans:
- name: Lastscanned Com Plans Pricing
  plan_count: 2
  slug: lastscanned-com-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: lastscanned API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: lastscanned-com-rules
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 56.8
    catalog_earned_first_party: 8.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 63.6
    developer_ergonomics: 26.8
    discoverability: 64.3
    operational_transparency: 15.8
  previous_composite: 50.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/lastscanned-com/lastscanned-com-2026-11-03T134657.png
security:
- kind: authentication
  name: Lastscanned Com Authentication
  slug: lastscanned-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Lastscanned Com Domain Security
  slug: lastscanned-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 2
skills:
- name: lastscanned-com-manage-keys
  slug: lastscanned-com-manage-keys
- name: lastscanned-com-set-webhook
  slug: lastscanned-com-set-webhook
slug: lastscanned-com
tags:
- Company
- Tracking
- Logistics
- MCP
website: https://lastscanned.com
---
