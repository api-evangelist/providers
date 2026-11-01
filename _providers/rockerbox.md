---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://www.rockerbox.com/plans
  - https://data-foundation.rockerbox.com/warehousing/quickstart
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: 'Rockerbox''s server-side integration. A documented HTTP POST endpoint that accepts one conversion or marketing event per request as JSON, authenticated by a Rockerbox Advertiser ID passed in the query '
  name: Rockerbox Conversion & Marketing Event Ingestion
  slug: rockerbox-api
- description: Rockerbox's warehouse-share delivery surface and the documentation site that describes it. The contract here is a set of published dataset schemas — log_conversions, clickstream, log_mta, aggregate_mt
  name: Rockerbox Data Foundation
  slug: rockerbox-data-foundation
artifact_total: 11
asyncapis:
- description: ''
  name: Rockerbox Webhooks
  slug: rockerbox-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.rockerbox.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data-foundation.rockerbox.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.rockerbox.com/
- group: docs
  title: ''
  type: APIReference
  url: https://data-foundation.rockerbox.com/warehousing/schemas
- group: start
  title: ''
  type: GettingStarted
  url: https://data-foundation.rockerbox.com/warehousing/quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.rockerbox.com/article/ocjyw3jty7-rockerbox-support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rockerbox
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rockerbox
- group: other
  title: ''
  type: X
  url: https://x.com/rockerbox
- group: company
  title: ''
  type: Blog
  url: https://www.rockerbox.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.rockerbox.com/blog/rss.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rockerbox.com/plans
- group: start
  title: ''
  type: Login
  url: https://app.rockerbox.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rockerbox.com/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rockerbox.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.rockerbox.com/faq/how-does-rockerbox-provide-secure-marketing-measurement
- group: commercial
  href: https://artifacts.apis.io/rockerbox/plans/rockerbox-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rockerbox-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/rockerbox/rate-limits/rockerbox-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rockerbox-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/rockerbox/finops/rockerbox-finops.yml
  title: ''
  type: FinOps
  url: finops/rockerbox-finops.yml
- group: design
  href: https://artifacts.apis.io/rockerbox/json-ld/rockerbox-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rockerbox-context.jsonld
- group: auth
  href: https://artifacts.apis.io/rockerbox/security/rockerbox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rockerbox-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/rockerbox/mcp/rockerbox-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/rockerbox-mcp.yml
- group: other
  href: https://artifacts.apis.io/rockerbox/a2a/rockerbox-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/rockerbox-a2a.yml
- group: agent
  href: https://artifacts.apis.io/rockerbox/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/rockerbox/llms/rockerbox-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rockerbox-llms.txt
- group: agent
  href: https://artifacts.apis.io/rockerbox/well-known/rockerbox-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rockerbox-well-known.yml
- group: design
  href: https://artifacts.apis.io/rockerbox/asyncapi/rockerbox-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/rockerbox-webhooks.yml
- group: design
  href: https://artifacts.apis.io/rockerbox/data-model/rockerbox-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rockerbox-data-model.yml
- group: auth
  href: https://artifacts.apis.io/rockerbox/authentication/rockerbox-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rockerbox-authentication.yml
- group: design
  href: https://artifacts.apis.io/rockerbox/conventions/rockerbox-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rockerbox-conventions.yml
- group: design
  href: https://artifacts.apis.io/rockerbox/conventions/rockerbox-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/rockerbox-conventions.yml
- group: design
  href: https://artifacts.apis.io/rockerbox/conformance/rockerbox-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rockerbox-conformance.yml
- group: design
  href: https://artifacts.apis.io/rockerbox/lifecycle/rockerbox-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rockerbox-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://data-foundation.rockerbox.com/warehousing/aggregate-mta-partition-migration
- group: build
  href: https://artifacts.apis.io/rockerbox/packages/rockerbox-packages.yml
  title: ''
  type: Packages
  url: packages/rockerbox-packages.yml
created: 2026-06-13
description: 'Rockerbox is a New York-based unified marketing measurement platform that combines multi-touch attribution (MTA), marketing mix modeling (MMM) and incrementality testing on a single first-party data foundation spanning 100+ advertising integrations. Its developer surface is deliberately narrow and unusual: there is no public REST API and no OpenAPI. Data goes IN through a documented server-side conversion webhook, onsite tracking pixels, and batch files; results come OUT as warehouse shares into Snowflake, BigQuery or Redshift against published schemas, plus scheduled and ad hoc exports. Rockerbox does, however, run a genuinely modern agent surface on its Data Foundation documentation host — an anonymous remote MCP server, an A2A agent card, a provider-published Agent Skill, an llms.txt, and an explicit robots.txt Content-Signal grant.'
finops:
- has_sources: true
  method: derived
  name: Rockerbox Finops
  primary_unit: ''
  service_category: ''
  slug: rockerbox-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rockerbox.png
jsonld:
- class_count: 7
  name: Rockerbox Context
  property_count: 6
  slug: rockerbox-context
layout: provider
mcp_servers:
- description: 'Rockerbox publishes a live, anonymous, remote MCP server on its Data Foundation documentation host. It was reached directly: an MCP `initialize` handshake and a `tools/list` call both returned HTTP 20'
  name: Rockerbox Data Foundation Docs
  slug: rockerbox-data-foundation-docs
modified: 2026-08-13
name: Rockerbox
nav: Providers
network: true
overview: 'Rockerbox is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Marketing Attribution, Multi-Touch Attribution, Marketing Mix Modeling, Incrementality Testing, and Media Spend.


  The Rockerbox catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Rockerbox''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 28 more developer resources.'
plans:
- name: Rockerbox Plans Pricing
  plan_count: 0
  slug: rockerbox-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Rockerbox Rate Limits
  slug: rockerbox-rate-limits
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 0.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 49.4
    developer_ergonomics: 64.3
    discoverability: 65.0
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 53.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa-cpra
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rockerbox/rockerbox-2026-06-20T193150.png
security:
- kind: authentication
  name: Rockerbox Authentication
  slug: rockerbox-authentication
  summary_line: tenant-identifier/session-login/warehouse-grant · 5 schemes
- kind: domain-security
  name: Rockerbox Domain Security
  slug: rockerbox-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: Rockerbox
  slug: rockerbox-data-foundation
slug: rockerbox
tags:
- Marketing Attribution
- Multi-Touch Attribution
- Marketing Mix Modeling
- Incrementality Testing
- Media Spend
- Customer Journey
- Marketing Analytics
- Data Warehousing
- Conversion Tracking
- Webhook
- A2A
- Attribution
website: https://www.rockerbox.com/
---
