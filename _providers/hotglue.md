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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Hotglue Agentic Access
  operation_count: 12
  slug: hotglue-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- description: The Hotglue API v1 provides the original REST API for managing integration flows, linked sources, linked targets, source state, and job execution.
  name: Hotglue API V1
  slug: hotglue-api-v1
- baseURL: https://api.hotglue.com
  baseurl_source: declared
  description: Run jobs for linked connectors.
  name: Hotglue Jobs API
  slug: hotglue-jobs-api
- baseURL: https://api.hotglue.com
  baseurl_source: declared
  description: The AvailableConnectors API from Hotglue — 1 operation(s) for availableconnectors.
  name: Hotglue Available Connectors API
  slug: hotglue-availableconnectors-api
- baseURL: https://api.hotglue.com
  baseurl_source: declared
  description: The AvailableSources API from Hotglue — 1 operation(s) for availablesources.
  name: Hotglue Available Sources API
  slug: hotglue-availablesources-api
- baseURL: https://api.hotglue.com
  baseurl_source: declared
  description: The AvailableTargets API from Hotglue — 1 operation(s) for availabletargets.
  name: Hotglue Available Targets API
  slug: hotglue-availabletargets-api
- baseURL: https://api.hotglue.com
  baseurl_source: declared
  description: The Connectors API from Hotglue — 6 operation(s) for connectors.
  name: Hotglue Connectors API
  slug: hotglue-connectors-api
- baseURL: https://api.hotglue.com
  baseurl_source: declared
  description: The Flows API from Hotglue — 2 operation(s) for flows.
  name: Hotglue Flows API
  slug: hotglue-flows-api
- baseURL: https://api.hotglue.com
  baseurl_source: declared
  description: The Jupyter API from Hotglue — 1 operation(s) for jupyter.
  name: Hotglue Jupyter API
  slug: hotglue-jupyter-api
- baseURL: https://api.hotglue.com
  baseurl_source: declared
  description: The LinkedConnectors API from Hotglue — 4 operation(s) for linkedconnectors.
  name: Hotglue Linked Connectors API
  slug: hotglue-linkedconnectors-api
- baseURL: https://api.hotglue.com
  baseurl_source: declared
  description: The LinkedSources API from Hotglue — 5 operation(s) for linkedsources.
  name: Hotglue Linked Sources API
  slug: hotglue-linkedsources-api
- baseURL: https://api.hotglue.com
  baseurl_source: declared
  description: The LinkedTargets API from Hotglue — 3 operation(s) for linkedtargets.
  name: Hotglue Linked Targets API
  slug: hotglue-linkedtargets-api
- baseURL: https://api.hotglue.com
  baseurl_source: declared
  description: The McpToken API from Hotglue — 1 operation(s) for mcptoken.
  name: Hotglue MCP Token API
  slug: hotglue-mcptoken-api
- baseURL: https://api.hotglue.com
  baseurl_source: declared
  description: The SupportedConnectors API from Hotglue — 1 operation(s) for supportedconnectors.
  name: Hotglue Supported Connectors API
  slug: hotglue-supportedconnectors-api
- baseURL: https://api.hotglue.com
  baseurl_source: declared
  description: The SupportedSources API from Hotglue — 1 operation(s) for supportedsources.
  name: Hotglue Supported Sources API
  slug: hotglue-supportedsources-api
- baseURL: https://api.hotglue.com
  baseurl_source: declared
  description: The SupportedTargets API from Hotglue — 1 operation(s) for supportedtargets.
  name: Hotglue Supported Targets API
  slug: hotglue-supportedtargets-api
- baseURL: https://api.hotglue.com
  baseurl_source: declared
  description: The Tenant API from Hotglue — 5 operation(s) for tenant.
  name: Hotglue Tenant API
  slug: hotglue-tenant-api
- baseURL: https://api.hotglue.com
  baseurl_source: declared
  description: The Tenants API from Hotglue — 2 operation(s) for tenants.
  name: Hotglue Tenants API
  slug: hotglue-tenants-api
- baseURL: https://api.hotglue.com
  baseurl_source: declared
  description: The Magic Link API from Hotglue — 1 operation(s) for magic link.
  name: Hotglue Magic Link API
  slug: hotglue-magic-link-api
artifact_total: 34
collections:
- collection_type: open
  name: Hotglue API V2 Connector Metadata API
  slug: open-hotglue-connector-metadata-api
- collection_type: open
  name: Hotglue API V2 Connector Metadata Connector State API
  slug: open-hotglue-connector-state-api
- collection_type: open
  name: Hotglue API V2 Connector Metadata Discover API
  slug: open-hotglue-discover-api
- collection_type: open
  name: Hotglue API V2 Connector Metadata Jobs API
  slug: open-hotglue-jobs-api
- collection_type: open
  name: Hotglue API V2 Connector Metadata Linked Connectors API
  slug: open-hotglue-linked-connectors-api
- collection_type: open
  name: Hotglue API V2
  slug: open-hotglue
common:
- group: other
  href: https://artifacts.apis.io/hotglue/capabilities/hotglue-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hotglue-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/hotglue/plans/hotglue-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hotglue-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/hotglue/rate-limits/hotglue-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hotglue-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/hotglue/finops/hotglue-finops.yml
  title: ''
  type: FinOps
  url: finops/hotglue-finops.yml
- group: agent
  href: https://artifacts.apis.io/hotglue/agentic-access/hotglue-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hotglue-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/hotglue/security/hotglue-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hotglue-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/hotglue/security/hotglue-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hotglue-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hotglue/security/hotglue-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hotglue-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/hotglue/authentication/hotglue-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hotglue-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hotgluexyz
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hotglue
- group: company
  title: ''
  type: Website
  url: https://hotglue.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hotglue.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://hotglue.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://hotglue.com/blog/
- group: start
  title: ''
  type: Signup
  url: https://hotglue.com/signup
- group: start
  title: ''
  type: Login
  url: https://hotglue.com/login
- group: agent
  title: ''
  type: LlmsText
  url: https://hotglue.com/llms.txt
created: '2026-03-16'
description: Hotglue is an embedded iPaaS platform that enables SaaS products to offer native integrations to their customers. Built on the Python ecosystem, it provides a code-first approach with over 600 open-source connectors, a CLI for programmatic configuration management, detailed job logs, webhooks, and observability integrations. Hotglue allows developers to build flexible, scalable integrations without the lock-in of traditional iPaaS tools.
finops:
- has_sources: false
  method: generated
  name: Hotglue Finops
  primary_unit: request
  service_category: API
  slug: hotglue-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hotglue.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.hotglue.com over HTTP.
  name: Hotglue MCP Server
  slug: hotglue
modified: '2026-05-19'
name: Hotglue
nav: Providers
network: true
overview: 'Hotglue publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Jobs API, Available Connectors API, Available Sources API, and 15 more. Tagged areas include Connectors, Embedded Integrations, ETL, Integration Platform, and iPaaS.


  The Hotglue catalog on APIs.io includes 1 Spectral governance ruleset.


  Hotglue''s developer surface includes authentication, documentation, pricing, engineering blog, signup flow, and 13 more developer resources.'
plans:
- name: Hotglue Plans Pricing
  plan_count: 3
  slug: hotglue-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Hotglue Rate Limits
  slug: hotglue-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Hotglue API Rules
  rule_count: 57
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 14
  slug: hotglue-rules
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 32.9
    contract_governance: 13.6
    contract_quality: 55.3
    developer_ergonomics: 31.0
    discoverability: 75.0
    operational_transparency: 21.1
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 73.9
      total: 23
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hotglue/hotglue-2026-06-20T182845.png
security:
- kind: authentication
  name: Hotglue Authentication
  slug: hotglue-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hotglue Domain Security
  slug: hotglue-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Hotglue Vulnerability Disclosure
  slug: hotglue-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Hotglue Trust Center
  slug: hotglue-trust-center
  summary_line: ISO 27001, GDPR
slug: hotglue
tags:
- Connectors
- Embedded Integrations
- ETL
- Integration Platform
- iPaaS
website: https://hotglue.com/
---
