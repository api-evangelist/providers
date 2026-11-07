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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Frends iPaaS provides integration and automation capabilities through REST APIs.
  name: Frends API
  slug: frends
- description: The Reference API from Frends — 6 operation(s) for reference.
  name: Frends Reference API
  slug: frends-reference-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/frends/plans/frends-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/frends-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/frends/rate-limits/frends-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/frends-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/frends/finops/frends-finops.yml
  title: ''
  type: FinOps
  url: finops/frends-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://frends.com/insights
- group: company
  title: ''
  type: BlogRSS
  url: https://frends.com/insights/rss.xml
- group: auth
  href: https://artifacts.apis.io/frends/security/frends-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/frends-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FrendsPlatform
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/frends-app
- group: company
  title: ''
  type: Website
  url: https://www.frends.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.frends.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.frends.com/llms.txt
created: '2026-03-16'
description: Frends is an integration platform as a service (iPaaS) that provides enterprise-grade API and integration capabilities.
finops:
- has_sources: false
  method: generated
  name: Frends Finops
  primary_unit: request
  service_category: API
  slug: frends-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/frends.png
json_schemas:
- name: GetReferenceTriggersTriggeridResponse
  property_count: 1
  slug: frends-get-reference-triggers-triggerid-response
jsonld:
- class_count: 1
  name: Frends Context
  property_count: 1
  slug: frends-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.frends.com over HTTP; 4 tools listed.
  name: Frends MCP Server
  slug: frends
modified: '2026-10-06'
name: Frends
nav: Providers
network: true
overview: 'Frends is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Reference API, and 1 more. Tagged areas include Integration and iPaaS.


  The Frends catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Frends'' developer surface includes engineering blog, documentation, and 9 more developer resources.'
plans:
- name: Frends Plans Pricing
  plan_count: 3
  slug: frends-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Frends Rate Limits
  slug: frends-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Frends API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: frends-rules
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 37.5
    catalog_earned_first_party: 0.0
    catalog_gap: 77.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 31.8
    contract_quality: 15.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 10.5
  previous_composite: 18.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/frends/frends-2026-06-20T181542.png
security:
- kind: authentication
  name: Frends Authentication
  slug: frends-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Frends Domain Security
  slug: frends-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: frends
tags:
- Integration
- iPaaS
website: https://www.frends.com/
---
