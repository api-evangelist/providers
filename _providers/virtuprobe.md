---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for VirtuProbe monitoring platform providing probes for various protocols.
  name: VirtuProbe API
  slug: virtuprobe-api-2
- description: 'VirtuProbe Studio API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: VirtuProbe Studio API
  slug: virtuprobe-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/virtuprobe/plans/virtuprobe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/virtuprobe-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/virtuprobe/rules/virtuprobe-rules.yml
  title: ''
  type: Spectral
  url: rules/virtuprobe-rules.yml
- group: design
  href: https://artifacts.apis.io/virtuprobe/json-ld/virtuprobe-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/virtuprobe-context.jsonld
- group: design
  href: https://artifacts.apis.io/virtuprobe/vocabulary/virtuprobe-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/virtuprobe-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/virtuprobe/data-model/virtuprobe-data-model.yml
  title: ''
  type: DataModel
  url: data-model/virtuprobe-data-model.yml
- group: operate
  href: https://artifacts.apis.io/virtuprobe/changelog/virtuprobe-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/virtuprobe-changelog.yml
- group: auth
  href: https://artifacts.apis.io/virtuprobe/authentication/virtuprobe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/virtuprobe-authentication.yml
- group: design
  href: https://artifacts.apis.io/virtuprobe/conformance/virtuprobe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/virtuprobe-conformance.yml
- group: other
  href: https://artifacts.apis.io/virtuprobe/hosts/virtuprobe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/virtuprobe-hosts.yml
- group: other
  href: https://artifacts.apis.io/virtuprobe/vendors/virtuprobe-vendors.yml
  title: ''
  type: Vendors
  url: vendors/virtuprobe-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.virtuprobe.studio/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.virtuprobe.studio/getting-started/introduction/
- group: auth
  href: https://artifacts.apis.io/virtuprobe/security/virtuprobe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/virtuprobe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://virtuprobe.studio/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.virtuprobe.studio/
- group: company
  title: ''
  type: Blog
  url: https://virtuprobe.studio/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://virtuprobe.studio/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://virtuprobe.studio/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://virtuprobe.studio/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://virtuprobe.studio/faq
coverage:
  checked: '2026-10-19'
  detail: Docs site returns HTML and no OpenAPI/Swagger files were found at common endpoints.
  evidence:
  - status: 404
    url: https://docs.virtuprobe.studio/openapi.json
  - status: 522
    url: https://api.virtuprobe.studio/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: VirtuProbe Studio provides advanced monitoring and probing solutions for APIs, enabling developers to gain deep insights into performance, reliability, and security. Their platform offers real-time analytics, customizable dashboards, and automated alerts to help teams quickly identify and resolve issues. With a focus on ease of integration, VirtuProbe supports multiple protocols and environments, catering to both small startups and large enterprises seeking robust API observability.
image: https://virtuprobe.studio/og.png
json_schemas:
- name: GetSrvEventsSubscribersResponse
  property_count: 1
  slug: virtuprobe-get-srv-events-subscribers-response
jsonld:
- class_count: 1
  name: Virtuprobe Context
  property_count: 1
  slug: virtuprobe-context
layout: provider
modified: '2026-10-19'
name: VirtuProbe Studio
nav: Providers
network: true
overview: 'VirtuProbe Studio is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Monitoring, API Observability, Analytics, and Alerts.


  The VirtuProbe Studio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  VirtuProbe Studio''s developer surface includes changelog, authentication, getting-started guide, documentation, engineering blog, pricing, support, and 13 more developer resources.'
plans:
- name: Virtuprobe Plans Pricing
  plan_count: 4
  slug: virtuprobe-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: VirtuProbe Studio API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: virtuprobe-rules
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 17.6
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 37.0
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/virtuprobe/virtuprobe-2026-11-03T145845.png
security:
- kind: authentication
  name: Virtuprobe Authentication
  slug: virtuprobe-authentication
  summary_line: 10 schemes
- kind: domain-security
  name: Virtuprobe Domain Security
  slug: virtuprobe-domain-security
  summary_line: TLSv1.3
slug: virtuprobe
tags:
- Company
- Monitoring
- API Observability
- Analytics
- Alerts
website: https://virtuprobe.studio/
---
