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
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Query address-level storm forecasts for ten perils and reported storm history across 11 event categories. Pay per address, free previews.
  name: Atlas United API
  slug: atlas-united-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/atlasunited-io/rules/atlasunited-io-rules.yml
  title: ''
  type: Spectral
  url: rules/atlasunited-io-rules.yml
- group: design
  href: https://artifacts.apis.io/atlasunited-io/json-ld/atlasunited-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/atlasunited-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/atlasunited-io/vocabulary/atlasunited-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/atlasunited-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/atlasunited-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/atlasunited-io/data-model/atlasunited-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/atlasunited-io-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://atlasunited.io/trust
- group: auth
  href: https://artifacts.apis.io/atlasunited-io/authentication/atlasunited-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/atlasunited-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/atlasunited-io/errors/atlasunited-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/atlasunited-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/atlasunited-io/conformance/atlasunited-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atlasunited-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/atlasunited-io/llms/atlasunited-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atlasunited-io-llms.txt
- group: other
  href: https://artifacts.apis.io/atlasunited-io/hosts/atlasunited-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlasunited-io-hosts.yml
- group: auth
  href: https://artifacts.apis.io/atlasunited-io/security/atlasunited-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/atlasunited-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/atlasunited-io/security/atlasunited-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlasunited-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlasunited.io/
- group: docs
  title: ''
  type: Documentation
  url: https://atlasunited.io/data.html
- group: start
  title: ''
  type: GettingStarted
  url: https://atlasunited.io/get-started.html
- group: commercial
  title: ''
  type: Pricing
  url: https://atlasunited.io/get-started.html
- group: operate
  title: ''
  type: Support
  url: https://atlasunited.io/contact.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atlasunited.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atlasunited.io/terms
coverage:
  checked: '2026-11-02'
  detail: The provider's API documentation does not publish an owned OpenAPI spec; the available spec at https://api.atlasunited.io/openapi.json appears generic and lacks identifying information.
  evidence:
  - status: 200
    url: https://api.atlasunited.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Atlas United provides address-level storm forecast data through its AtlasCast engine. It offers forecasts for ten storm perils, including tornadoes, hail, wind, flash floods, heavy rain, winter storms, ice, coastal surge, hurricanes, and wildfires. Users can query forecasts up to ten days in advance for any address, with pay‑per‑address pricing and no contracts. The platform also supplies historical storm data and leads. The service is delivered via a public API and integrates with AI agents.
image: https://atlasunited.io/images/og-atlasunited.jpg
jsonld:
- class_count: 5
  name: Atlasunited Io Context
  property_count: 17
  slug: atlasunited-io-context
layout: provider
modified: '2026-11-01'
name: Atlas United
nav: Providers
network: true
overview: 'Atlas United publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Forecast, Storm, and Geolocation.


  The Atlas United catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Atlas United''s developer surface includes authentication, documentation, getting-started guide, pricing, support, and 15 more developer resources.'
plans:
- name: Atlasunited Io Plans Pricing
  plan_count: 0
  slug: atlasunited-io-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Atlasunited Io Rate Limits
  slug: atlasunited-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: Atlas United API Rules
  rule_count: 33
  severity_counts:
    error: 30
    hint: 0
    info: 1
    warn: 2
  slug: atlasunited-io-rules
scopes:
- name: Atlasunited Io Scopes
  scope_count: 0
  slug: atlasunited-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 27.6
    contract_governance: 22.0
    contract_quality: 14.7
    developer_ergonomics: 31.4
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 34.9
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atlasunited Io Authentication
  slug: atlasunited-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Atlasunited Io Domain Security
  slug: atlasunited-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Atlasunited Io Trust Center
  slug: atlasunited-io-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, FedRAMP, GDPR
skill_count: 1
skills:
- name: stormcast
  slug: atlasunited-io-stormcast
slug: atlasunited-io
tags:
- Company
- Weather
- Forecast
- Storm
- Geolocation
website: https://atlasunited.io/
---
