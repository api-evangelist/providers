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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Membrane is an AI-first integration platform that enables building product integrations using natural language. It offers 282+ pre-built packages and is compatible with AI coding assistants via MCP pr
  name: Membrane Integration Platform
  slug: membrane-platform
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/membrane/plans/membrane-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/membrane-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/membrane/rate-limits/membrane-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/membrane-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/membrane/finops/membrane-finops.yml
  title: ''
  type: FinOps
  url: finops/membrane-finops.yml
- group: auth
  href: https://artifacts.apis.io/membrane/security/membrane-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/membrane-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/membrane/security/membrane-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/membrane-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://getmembrane.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.membrane.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/membrane-io
- group: commercial
  title: ''
  type: Pricing
  url: https://getmembrane.com/pricing
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.membrane.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://getmembrane.com/articles/all
created: '2026-03-16'
description: Membrane is an AI-powered platform for building product integrations using natural language. It connects to any API with 282+ pre-built packages and is compatible with AI coding assistants via MCP. There is also a separate open source Membrane API Gateway for REST, SOAP, and GraphQL.
finops:
- has_sources: false
  method: generated
  name: Membrane Finops
  primary_unit: request
  service_category: API
  slug: membrane-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/membrane.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.getmembrane.com over HTTP; 3 tools listed.
  name: Membrane MCP Server
  slug: membrane
modified: '2026-04-28'
name: Membrane
nav: Providers
network: true
overview: 'Membrane is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, API Gateway, Automation, Integration, and No-Code.


  Membrane''s developer surface includes developer portal, documentation, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Membrane Plans Pricing
  plan_count: 3
  slug: membrane-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Membrane Rate Limits
  slug: membrane-rate-limits
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 66.7
    operational_transparency: 10.5
  previous_composite: 19.2
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/membrane/membrane-2026-06-20T185134.png
security:
- kind: domain-security
  name: Membrane Domain Security
  slug: membrane-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Membrane Trust Center
  slug: membrane-trust-center
  summary_line: SOC 2, GDPR
slug: membrane
tags:
- Artificial Intelligence
- API Gateway
- Automation
- Integration
- No-Code
website: https://getmembrane.com/
---
