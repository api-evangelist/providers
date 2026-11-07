---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Alloy Automation Agentic Access
  operation_count: 27
  slug: alloy-automation-agentic-access
  summary_line: 27 operations · 9 acting
api_count: 1
apis:
- baseURL: https://embedded.runalloy.com/2024-03
  baseurl_source: declared
  description: Third-party connections held by a user, plus credential metadata.
  name: Alloy Automation Credentials API
  slug: alloy-automation-credentials-api
- baseURL: https://embedded.runalloy.com/2024-03
  baseurl_source: declared
  description: Execution events and observability.
  name: Alloy Automation Events API
  slug: alloy-automation-events-api
- baseURL: https://embedded.runalloy.com/2024-03
  baseurl_source: declared
  description: Available connectors and a user's enabled integrations.
  name: Alloy Automation Integrations API
  slug: alloy-automation-integrations-api
- baseURL: https://embedded.runalloy.com/2024-03
  baseurl_source: declared
  description: Raw proxied requests to a provider via a stored credential.
  name: Alloy Automation Passthrough API
  slug: alloy-automation-passthrough-api
- baseURL: https://embedded.runalloy.com/2024-03
  baseurl_source: declared
  description: End-user records that scope credentials, integrations, and executions.
  name: Alloy Automation Users API
  slug: alloy-automation-users-api
- baseURL: https://embedded.runalloy.com/2024-03
  baseurl_source: declared
  description: The Analytics API from Alloy Automation — 4 operation(s) for analytics.
  name: Alloy Automation Analytics API
  slug: alloy-automation-analytics-api
- baseURL: https://embedded.runalloy.com/2024-03
  baseurl_source: declared
  description: The Headless API from Alloy Automation — 5 operation(s) for headless.
  name: Alloy Automation Headless API
  slug: alloy-automation-headless-api
- baseURL: https://embedded.runalloy.com/2024-03
  baseurl_source: declared
  description: The Installations API from Alloy Automation — 6 operation(s) for installations.
  name: Alloy Automation Installations API
  slug: alloy-automation-installations-api
- baseURL: https://embedded.runalloy.com/2024-03
  baseurl_source: declared
  description: The Logs API from Alloy Automation — 2 operation(s) for logs.
  name: Alloy Automation Logs API
  slug: alloy-automation-logs-api
- baseURL: https://embedded.runalloy.com/2024-03
  baseurl_source: declared
  description: The Metadata API from Alloy Automation — 3 operation(s) for metadata.
  name: Alloy Automation Metadata API
  slug: alloy-automation-metadata-api
- baseURL: https://embedded.runalloy.com/2024-03
  baseurl_source: declared
  description: The Run API from Alloy Automation — 2 operation(s) for run.
  name: Alloy Automation Run API
  slug: alloy-automation-run-api
- baseURL: https://embedded.runalloy.com/2024-03
  baseurl_source: declared
  description: The Workflows API from Alloy Automation — 12 operation(s) for workflows.
  name: Alloy Automation Workflows API
  slug: alloy-automation-workflows-api
artifact_total: 31
collections:
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity API
  slug: open-alloy-automation-connectivity-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity Credentials API
  slug: open-alloy-automation-credentials-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity Events API
  slug: open-alloy-automation-events-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity Integrations API
  slug: open-alloy-automation-integrations-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity Passthrough API
  slug: open-alloy-automation-passthrough-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity Unified Accounting API
  slug: open-alloy-automation-unified-accounting-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity Unified Commerce API
  slug: open-alloy-automation-unified-commerce-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity Unified CRM API
  slug: open-alloy-automation-unified-crm-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity User Tokens API
  slug: open-alloy-automation-user-tokens-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity Users API
  slug: open-alloy-automation-users-api
- collection_type: open
  name: Alloy Automation Embedded & Unified API
  slug: open-alloy-automation
common:
- group: company
  title: ''
  type: Blog
  url: https://runalloy.com/blog/
- group: other
  href: https://artifacts.apis.io/alloy-automation/capabilities/alloy-automation-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/alloy-automation-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/alloy-automation/agentic-access/alloy-automation-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/alloy-automation-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/alloy-automation/security/alloy-automation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alloy-automation-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/alloy-automation/authentication/alloy-automation-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alloy-automation-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alloy-automation
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alloy-automation
- group: company
  title: ''
  type: Website
  url: https://runalloy.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.runalloy.com
- group: commercial
  href: https://artifacts.apis.io/alloy-automation/plans/alloy-automation-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alloy-automation-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/alloy-automation/rate-limits/alloy-automation-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/alloy-automation-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/alloy-automation/finops/alloy-automation-finops.yml
  title: ''
  type: FinOps
  url: finops/alloy-automation-finops.yml
created: '2026-07-01'
description: Alloy Automation (runalloy.com) is an embedded integration platform (iPaaS) and Unified API for SaaS products. Its Embedded product lets you drop white-labeled, end-user-facing integrations into your app, while the Connectivity and Unified API provide a single REST interface for connecting to hundreds of third-party platforms across commerce, CRM, and accounting. All APIs use dated versioning (2024-03), a Bearer API key, and per-user credentials/tokens.
finops:
- has_sources: true
  method: generated
  name: Alloy Automation Finops
  primary_unit: ''
  service_category: Integration Platform
  slug: alloy-automation-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alloy-automation.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.runalloy.com over HTTP.
  name: Alloy Automation MCP Server
  slug: alloy-automation
modified: '2026-10-06'
name: Alloy Automation
nav: Providers
network: true
overview: 'Alloy Automation publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Credentials API, Events API, Integrations API, and 9 more. Tagged areas include iPaaS, Integration, Unified API, Embedded, and Software-as-a-Service.


  The Alloy Automation catalog on APIs.io includes 1 Spectral governance ruleset.


  Alloy Automation''s developer surface includes engineering blog, authentication, documentation, and 9 more developer resources.'
plans:
- name: Alloy Automation Plans Pricing
  plan_count: 3
  slug: alloy-automation-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 4
  name: Alloy Automation Rate Limits
  slug: alloy-automation-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Alloy Automation API Rules
  rule_count: 45
  severity_counts:
    error: 35
    hint: 0
    info: 3
    warn: 7
  slug: alloy-automation-rules
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 49.9
    developer_ergonomics: 32.1
    discoverability: 68.3
    operational_transparency: 10.5
  previous_composite: 28.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 52.2
      total: 23
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/alloy-automation/alloy-automation-2026-07-25T195811.png
security:
- kind: authentication
  name: Alloy Automation Authentication
  slug: alloy-automation-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Alloy Automation Domain Security
  slug: alloy-automation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alloy-automation
tags:
- iPaaS
- Integration
- Unified API
- Embedded
- Software-as-a-Service
- Automation
website: https://runalloy.com
---
