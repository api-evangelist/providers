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
  score: 0.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP Registry API providing tools list, server lookup, and change events for PolicyLayer.
  name: PolicyLayer MCP Registry API
  slug: policylayer-mcp-registry-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: Compliance
  url: https://policylayer.com/compliance
- group: auth
  href: https://artifacts.apis.io/policylayer-com/security/policylayer-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/policylayer-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/policylayer-com/llms/policylayer-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/policylayer-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/policylayer-com/mcp/policylayer-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/policylayer-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/policylayer-com/hosts/policylayer-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/policylayer-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/policylayer-com/vendors/policylayer-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/policylayer-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.policylayer.com/login
- group: auth
  href: https://artifacts.apis.io/policylayer-com/security/policylayer-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/policylayer-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/policylayer-com/security/policylayer-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/policylayer-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/policylayer-com/security/policylayer-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/policylayer-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://policylayer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://policylayer.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://policylayer.com/docs
- group: company
  title: ''
  type: Blog
  url: https://policylayer.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://policylayer.com/pricing
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.policylayer.com/mcp
  - status: 401
    url: https://mcp.policylayer.com/mcp
  - status: 400
    url: https://app.policylayer.com/graphql
  - status: 400
    url: https://app.policylayer.com/mcp
  - status: 200
    url: https://policylayer.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: 'PolicyLayer turns your team’s decisions into a signed playbook every coding agent can use, and routes uncovered questions to the right person. PolicyLayer is the system of record for AI agent authority: it turns approved human decisions into reusable rules for every AI agent.'
image: https://policylayer.com/og/page/judgment-home.png?v=4
json_schemas:
- name: Policylayer Com Mcp
  property_count: 0
  slug: policylayer-com-mcp
layout: provider
mcp_servers:
- description: Remote MCP server at api.policylayer.com.
  name: policylayer-com MCP Server
  slug: policylayer-com-mcp-yml
modified: '2026-10-30'
name: policylayer-com
nav: Providers
network: true
overview: 'policylayer-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Agents, Policy, and Governance.


  policylayer-com''s developer surface includes documentation, engineering blog, pricing, and 12 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 75.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/policylayer-com/policylayer-com-2026-11-03T141338.png
security:
- kind: domain-security
  name: Policylayer Com Domain Security
  slug: policylayer-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Policylayer Com Vulnerability Disclosure
  slug: policylayer-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Policylayer Com Trust Center
  slug: policylayer-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: policylayer-com
tags:
- Company
- Artificial Intelligence
- Agents
- Policy
- Governance
- Automation
website: https://policylayer.com/
---
