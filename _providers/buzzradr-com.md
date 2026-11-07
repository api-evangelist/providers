---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Anonymous read-only public trend API for BuzzRadr.
  name: BuzzRadr Public HOT API
  slug: buzzradr-public-hot-api
- baseURL: https://buzzradr.com
  baseurl_source: declared
  description: Anonymous read-only public trend API for BuzzRadr. No API key, no signup. Responses are CDN-cached for 1-5 minutes depending on the endpoint; abusive traffic may receive 429 with a retry-after header.
  name: BuzzRadr Public HOT API API
  slug: buzzradr-public-hot-api-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/buzzradr-com/rules/buzzradr-com-rules.yml
  title: ''
  type: Spectral
  url: rules/buzzradr-com-rules.yml
- group: design
  href: https://artifacts.apis.io/buzzradr-com/json-ld/buzzradr-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/buzzradr-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/buzzradr-com/vocabulary/buzzradr-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buzzradr-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/buzzradr-com/conformance/buzzradr-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buzzradr-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/buzzradr-com/plans/buzzradr-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buzzradr-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/buzzradr-com/data-model/buzzradr-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buzzradr-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/buzzradr-com/errors/buzzradr-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/buzzradr-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/buzzradr-com/mcp/buzzradr-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/buzzradr-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/buzzradr-com/hosts/buzzradr-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buzzradr-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/buzzradr-com/vendors/buzzradr-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buzzradr-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buzzradr.com/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://buzzradr.com/status
- group: auth
  title: ''
  type: Security
  url: https://buzzradr.com/settings/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buzzradr.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://buzzradr.com/pricing
- group: start
  title: ''
  type: Login
  url: https://buzzradr.com/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://buzzradr.com/docs
- group: company
  title: ''
  type: Blog
  url: https://buzzradr.com/blog
- group: auth
  href: https://artifacts.apis.io/buzzradr-com/security/buzzradr-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buzzradr-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buzzradr.com/
created: '2026-11-03'
description: BuzzRadr provides a platform that aggregates public trend channels, keyword radars, and team briefs, enabling content teams to discover, monitor, and share important market trends. The service turns market heat into actionable topic signals, helping organizations stay ahead of emerging topics and make data‑driven decisions. It offers customizable dashboards, alerts, and collaborative tools for efficient trend analysis across industries.
image: https://buzzradr.com/preview.png
json_schemas:
- name: PublicSource
  property_count: 9
  slug: buzzradr-com-public-source
- name: PublicTopic
  property_count: 22
  slug: buzzradr-com-public-topic
jsonld:
- class_count: 4
  name: Buzzradr Com Context
  property_count: 43
  slug: buzzradr-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at buzzradr.com.
  name: BuzzRadr MCP Server
  slug: buzzradr-com-mcp-yml
modified: '2026-11-03'
name: BuzzRadr
nav: Providers
network: true
overview: 'BuzzRadr publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Public HOT API API, and 1 more. Tagged areas include Company, Trend Monitoring, Content Analytics, Market Intelligence, and Artificial Intelligence.


  The BuzzRadr catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BuzzRadr''s developer surface includes pricing, documentation, engineering blog, and 17 more developer resources.'
plans:
- name: Buzzradr Com Plans Pricing
  plan_count: 3
  slug: buzzradr-com-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: BuzzRadr API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: buzzradr-com-rules
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 47.1
    developer_ergonomics: 6.0
    discoverability: 65.0
    operational_transparency: 13.2
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buzzradr Com Domain Security
  slug: buzzradr-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: buzzradr-com
tags:
- Company
- Trend Monitoring
- Content Analytics
- Market Intelligence
- Artificial Intelligence
website: https://buzzradr.com/
---
