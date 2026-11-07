---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
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
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Aient AI provides telemetry SDKs and server APIs as documented in the reference.
  name: Aient AI API
  slug: aient-ai-api
artifact_total: 8
asyncapis:
- description: ''
  name: Aient Ai Webhooks
  slug: aient-ai-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/aient-ai/plans/aient-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aient-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aient-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aient-ai/asyncapi/aient-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/aient-ai-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/aient-ai/changelog/aient-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aient-ai-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://aient.ai/security
- group: auth
  href: https://artifacts.apis.io/aient-ai/authentication/aient-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aient-ai-authentication.yml
- group: agent
  href: https://artifacts.apis.io/aient-ai/llms/aient-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aient-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/aient-ai/a2a/aient-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aient-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aient-ai/mcp/aient-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aient-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aient-ai/well-known/aient-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aient-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/aient-ai/well-known/aient-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aient-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/aient-ai/hosts/aient-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aient-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/aient-ai/vendors/aient-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aient-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/aient-ai/packages/aient-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/aient-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/aient-ai/packages/aient-ai-packages.yml
  title: ''
  type: Packages
  url: packages/aient-ai-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aient.ai/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://aient.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aient.ai/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://aient.ai/auth/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aient.ai/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aient.ai/llms-full.txt
- group: auth
  href: https://artifacts.apis.io/aient-ai/security/aient-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aient-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/aient-ai/security/aient-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aient-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aient-ai/security/aient-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aient-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aient.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aient.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://aient.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://aient.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aient.ai/quickstart/opentelemetry
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.aient.ai/mcp
  - status: 401
    url: https://aient.ai/mcp
  - status: 200
    url: https://aient.ai/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: 'aient-ai is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://aient.ai/opengraph-image
layout: provider
mcp_servers:
- description: Remote MCP server at docs.aient.ai.
  name: Aient MCP Server
  slug: aient-ai-mcp-yml
modified: '2026-11-01'
name: Aient
nav: Providers
network: true
overview: 'Aient is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI SRE, Automated Fixes, and DevOps.


  The Aient catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aient''s developer surface includes changelog, authentication, API reference, documentation, pricing, engineering blog, getting-started guide, and 22 more developer resources.'
plans:
- name: Aient Ai Plans Pricing
  plan_count: 3
  slug: aient-ai-plans-pricing
random_paper: 8
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.0
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 41.0
    discoverability: 40.0
    operational_transparency: 21.1
  previous_composite: 50.2
  provenance:
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aient Ai Authentication
  slug: aient-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Aient Ai Domain Security
  slug: aient-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aient Ai Vulnerability Disclosure
  slug: aient-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aient Ai Trust Center
  slug: aient-ai-trust-center
  summary_line: SOC 2, GDPR
slug: aient-ai
tags:
- AI SRE
- Automated Fixes
- DevOps
website: https://aient.ai/
---
