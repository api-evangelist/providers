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
  band: human-only
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for DouxProcess automation platform.
  name: DouxProcess API
  slug: douxprocess-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/douxprocess-com/llms/douxprocess-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/douxprocess-com-llms.txt
- group: build
  href: https://artifacts.apis.io/douxprocess-com/mcp/douxprocess-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/douxprocess-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/douxprocess-com/mcp/douxprocess-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/douxprocess-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/douxprocess-com/hosts/douxprocess-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/douxprocess-com-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://douxprocess.com/blog
- group: auth
  href: https://artifacts.apis.io/douxprocess-com/security/douxprocess-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/douxprocess-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://douxprocess.com/
- group: docs
  title: ''
  type: Documentation
  url: https://douxprocess.com/stack
- group: docs
  title: ''
  type: APIReference
  url: https://douxprocess.com/api/live
- group: start
  title: ''
  type: GettingStarted
  url: https://douxprocess.com/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://douxprocess.com/connect
- group: commercial
  title: ''
  type: Pricing
  url: https://douxprocess.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://douxprocess.com/qualify
- group: commercial
  title: ''
  type: TermsOfService
  url: https://douxprocess.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://douxprocess.com/privacy
created: '2026-10-29'
description: DouxProcess provides agentic workflow automation for insurance agencies, handling inbox, certificates, endorsements, renewals, payments, and quoting. The platform runs 24/7, allowing agencies to approve actions while the system operates, priced at $2,500 per month for unlimited producers. It offers AI‑driven tools and a developer‑friendly API accessible via https://douxprocess.com/api/live. DouxProcess aims to streamline agency operations with intelligent automation.
image: https://douxprocess.com/assets/brand/favicon.svg?v=d28410affb
layout: provider
mcp_servers:
- description: Remote MCP server at douxprocess.com.
  name: douxprocess-com MCP Server
  slug: douxprocess-com-mcp-yml
modified: '2026-10-29'
name: douxprocess-com
nav: Providers
network: true
overview: 'douxprocess-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Automation, Artificial Intelligence, Software-as-a-Service, and Workflows.


  douxprocess-com''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, pricing, signup flow, and 8 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 75.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 8.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/douxprocess-com/douxprocess-com-2026-11-03T131002.png
security:
- kind: domain-security
  name: Douxprocess Com Domain Security
  slug: douxprocess-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: douxprocess-com
tags:
- Insurance
- Automation
- Artificial Intelligence
- Software-as-a-Service
- Workflows
website: https://douxprocess.com/
---
