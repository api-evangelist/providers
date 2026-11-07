---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Pay-per-call LLM chat completions and packages API.
  name: OmniProvider API
  slug: omniprovider-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/omnidev-tech/plans/omnidev-tech-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/omnidev-tech-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/omnidev-tech/changelog/omnidev-tech-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/omnidev-tech-changelog.yml
- group: design
  href: https://artifacts.apis.io/omnidev-tech/conventions/omnidev-tech-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/omnidev-tech-conventions.yml
- group: design
  href: https://artifacts.apis.io/omnidev-tech/conventions/omnidev-tech-conventions.yml
  title: ''
  type: Conventions
  url: conventions/omnidev-tech-conventions.yml
- group: auth
  href: https://artifacts.apis.io/omnidev-tech/authentication/omnidev-tech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/omnidev-tech-authentication.yml
- group: design
  href: https://artifacts.apis.io/omnidev-tech/conformance/omnidev-tech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/omnidev-tech-conformance.yml
- group: agent
  href: https://artifacts.apis.io/omnidev-tech/llms/omnidev-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/omnidev-tech-llms.txt
- group: other
  href: https://artifacts.apis.io/omnidev-tech/a2a/omnidev-tech-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/omnidev-tech-a2a.yml
- group: build
  href: https://artifacts.apis.io/omnidev-tech/mcp/omnidev-tech-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/omnidev-tech-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/omnidev-tech/mcp/omnidev-tech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/omnidev-tech-mcp.yml
- group: auth
  href: https://artifacts.apis.io/omnidev-tech/well-known/omnidev-tech-provider-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/omnidev-tech-provider-security.txt
- group: auth
  href: https://artifacts.apis.io/omnidev-tech/well-known/omnidev-tech-pay-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/omnidev-tech-pay-security.txt
- group: agent
  href: https://artifacts.apis.io/omnidev-tech/well-known/omnidev-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/omnidev-tech-well-known.yml
- group: other
  href: https://artifacts.apis.io/omnidev-tech/hosts/omnidev-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/omnidev-tech-hosts.yml
- group: other
  href: https://artifacts.apis.io/omnidev-tech/vendors/omnidev-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/omnidev-tech-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://provider.omnidev.tech/security
- group: auth
  href: https://artifacts.apis.io/omnidev-tech/security/omnidev-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/omnidev-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://omnidev.tech/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://provider.omnidev.tech/docs
- group: docs
  title: ''
  type: Documentation
  url: https://provider.omnidev.tech/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://provider.omnidev.tech/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://provider.omnidev.tech/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://provider.omnidev.tech/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://provider.omnidev.tech/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://provider.omnidev.tech/status
created: '2026-10-30'
description: OmniProvider, operating under the omnidev.tech brand, offers a pay-per-call LLM API for AI agents. It provides a model catalog and cited briefs, billed in USDC with flexible pricing tiers (Base and Tempo). No account or API key is required, enabling seamless integration for developers seeking on-demand AI capabilities. The platform emphasizes transparency, open access, and developer-friendly documentation.
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.omnidev.tech.
  name: omnidev-tech MCP Server
  slug: omnidev-tech-mcp-yml
modified: '2026-10-30'
name: omnidev-tech
nav: Providers
network: true
overview: 'omnidev-tech is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, LLM, Pay-per-call, and Company.


  omnidev-tech''s developer surface includes changelog, authentication, documentation, getting-started guide, support, and 20 more developer resources.'
plans:
- name: Omnidev Tech Plans Pricing
  plan_count: 34
  slug: omnidev-tech-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 53.3
    operational_transparency: 28.9
  previous_composite: 33.4
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/omnidev-tech/omnidev-tech-2026-11-03T140538.png
security:
- kind: authentication
  name: Omnidev Tech Authentication
  slug: omnidev-tech-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Omnidev Tech Domain Security
  slug: omnidev-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: omnidev-tech
tags:
- Artificial Intelligence
- LLM
- Pay-per-call
- Company
website: https://omnidev.tech/
---
