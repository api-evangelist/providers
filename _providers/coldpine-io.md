---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Coldpine API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Coldpine API
  slug: coldpine-io-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/coldpine-io/rules/coldpine-io-rules.yml
  title: ''
  type: Spectral
  url: rules/coldpine-io-rules.yml
- group: design
  href: https://artifacts.apis.io/coldpine-io/json-ld/coldpine-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coldpine-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/coldpine-io/vocabulary/coldpine-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coldpine-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/coldpine-io/data-model/coldpine-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coldpine-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/coldpine-io/conformance/coldpine-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coldpine-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coldpine-io/llms/coldpine-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coldpine-io-llms.txt
- group: other
  href: https://artifacts.apis.io/coldpine-io/hosts/coldpine-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coldpine-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/coldpine-io/vendors/coldpine-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coldpine-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coldpine.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coldpine.io/privacy
- group: other
  title: ''
  type: Leadership
  url: https://coldpine.io/stocks/TEAM
- group: start
  title: ''
  type: DeveloperPortal
  url: https://coldpine.io/developers
- group: auth
  href: https://artifacts.apis.io/coldpine-io/security/coldpine-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coldpine-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coldpine.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://coldpine.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://coldpine.io/sign-up
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found despite probing known spec URLs and the developer portal.
  evidence:
  - status: 0
    url: https://api.coldpine.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Coldpine is a publisher of intelligence on public U.S. Congressional stock‑trade disclosures. It parses filings within hours of disclosure, scores the trades, and provides free early‑access tools for tracking members of Congress, their holdings, and market impact. The platform offers leaderboards, research, and pricing plans for deeper analytics, aiming to increase transparency in government‑related financial activity.
image: https://coldpine.io/brand/og/og-ink-1200x630.png
json_schemas:
- name: PostApiMcpRequest
  property_count: 4
  slug: coldpine-io-post-api-mcp-request
jsonld:
- class_count: 1
  name: Coldpine Io Context
  property_count: 4
  slug: coldpine-io-context
layout: provider
modified: '2026-11-04'
name: Coldpine
nav: Providers
network: true
overview: 'Coldpine is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Congress, Finance, Transparency, and Data.


  The Coldpine catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Coldpine''s developer surface includes pricing, signup flow, and 14 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Coldpine API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: coldpine-io-rules
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 17.6
    developer_ergonomics: 9.5
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coldpine Io Domain Security
  slug: coldpine-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coldpine-io
tags:
- Company
- Congress
- Finance
- Transparency
- Data
- Analytics
website: https://coldpine.io/
---
