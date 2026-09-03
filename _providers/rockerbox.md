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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: 'Rockerbox''s server-side integration. A documented HTTP POST endpoint that accepts one conversion or marketing event per request as JSON, authenticated by a Rockerbox Advertiser ID passed in the query '
  name: Rockerbox Conversion & Marketing Event Ingestion
  slug: rockerbox-api
- description: Rockerbox's warehouse-share delivery surface and the documentation site that describes it. The contract here is a set of published dataset schemas — log_conversions, clickstream, log_mta, aggregate_mt
  name: Rockerbox Data Foundation
  slug: rockerbox-data-foundation
artifact_total: 10
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
  title: ''
  type: Plans
  url: plans/rockerbox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rockerbox-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rockerbox-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/rockerbox-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rockerbox-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rockerbox-mcp.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/rockerbox-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rockerbox-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rockerbox-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rockerbox-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rockerbox-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rockerbox-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rockerbox-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/rockerbox-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rockerbox-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rockerbox-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://data-foundation.rockerbox.com/warehousing/aggregate-mta-partition-migration
- group: build
  title: ''
  type: Packages
  url: packages/rockerbox-packages.yml
created: 2026-06-13
description: 'Rockerbox is a New York-based unified marketing measurement platform that combines multi-touch attribution (MTA), marketing mix modeling (MMM) and incrementality testing on a single first-party data foundation spanning 100+ advertising integrations. Its developer surface is deliberately narrow and unusual: there is no public REST API and no OpenAPI. Data goes IN through a documented server-side conversion webhook, onsite tracking pixels, and batch files; results come OUT as warehouse shares into Snowflake, BigQuery or Redshift against published schemas, plus scheduled and ad hoc exports. Rockerbox does, however, run a genuinely modern agent surface on its Data Foundation documentation host — an anonymous remote MCP server, an A2A agent card, a provider-published Agent Skill, an llms.txt, and an explicit robots.txt Content-Signal grant.'
finops:
- name: Rockerbox Finops
  service_category: ''
  slug: rockerbox-finops
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
overview: 'Rockerbox publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Marketing Attribution, Multi-Touch Attribution, Marketing Mix Modeling, Incrementality Testing, and Media Spend.


  The Rockerbox catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Rockerbox''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 28 more developer resources.'
plans:
- name: Rockerbox Plans Pricing
  plan_count: 1
  slug: rockerbox-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Rockerbox Rate Limits
  slug: rockerbox-rate-limits
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 75.0
    commercial_clarity: 75.0
    contract_governance: 18.2
    contract_quality: 51.9
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 53.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rockerbox/refs/heads/main/screenshots/rockerbox-2026-06-20T193150.png
security:
- kind: authentication
  name: Rockerbox Authentication
  slug: rockerbox-authentication
  summary_line: tenant-identifier/session-login/warehouse-grant · 5 schemes
- kind: domain-security
  name: Rockerbox Domain Security
  slug: rockerbox-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: rockerbox
tags:
- Marketing Attribution
- Multi-Touch Attribution
- Marketing Mix Modeling
- Incrementality Testing
- Media Spend
- Customer Journeys
- Marketing Analytics
- Data Warehousing
- Conversion Tracking
- Webhook
website: https://www.rockerbox.com/
---
