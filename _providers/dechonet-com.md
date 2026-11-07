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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 9.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public domain diagnostics and private workspace ASM operations API.
  name: DechoNet API
  slug: dechonet-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/dechonet-com/plans/dechonet-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dechonet-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dechonet-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dechonet-com/conformance/dechonet-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dechonet-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dechonet-com/llms/dechonet-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dechonet-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dechonet-com/mcp/dechonet-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dechonet-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/dechonet-com/well-known/dechonet-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dechonet-com-security.txt
- group: agent
  href: https://artifacts.apis.io/dechonet-com/well-known/dechonet-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dechonet-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dechonet-com/hosts/dechonet-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dechonet-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dechonet-com/vendors/dechonet-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dechonet-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/dechonet-com/packages/dechonet-com-packages.yml
  title: ''
  type: SDKs
  url: packages/dechonet-com-packages.yml
- group: build
  href: https://artifacts.apis.io/dechonet-com/packages/dechonet-com-packages.yml
  title: ''
  type: Packages
  url: packages/dechonet-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dechonet.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://dechonet.com/status
- group: auth
  title: ''
  type: Security
  url: https://dechonet.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dechonet.com/privacy
- group: auth
  href: https://artifacts.apis.io/dechonet-com/authentication/dechonet-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dechonet-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dechonet-com/security/dechonet-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dechonet-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dechonet-com/security/dechonet-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dechonet-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dechonet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dechonet.com/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dechonet.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://dechonet.com/developers
- group: company
  title: ''
  type: Blog
  url: https://dechonet.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://dechonet.com/pro
- group: operate
  title: ''
  type: Support
  url: https://dechonet.com/account
created: '2026-11-05'
description: DechoNet provides a decentralized echo network platform offering tools for phishing link checks, domain security scoring, brand protection, and various security monitoring utilities. It offers an API for automated security assessments, including DNS, SSL, HTTP, and post‑quantum TLS checks, as well as brand impersonation detection and look‑alike domain analysis.
image: https://dechonet.com/og/default.png
layout: provider
mcp_servers:
- description: Remote MCP server at dechonet.com.
  name: DechoNet MCP Server
  slug: dechonet-com-mcp-yml
modified: '2026-11-05'
name: DechoNet
nav: Providers
network: true
overview: 'DechoNet is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Monitoring, and Phishing.


  DechoNet''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, support, and 19 more developer resources.'
plans:
- name: Dechonet Com Plans Pricing
  plan_count: 6
  slug: dechonet-com-plans-pricing
random_paper: 6
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 58.8
    discoverability: 56.7
    operational_transparency: 26.3
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dechonet Com Authentication
  slug: dechonet-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Dechonet Com Domain Security
  slug: dechonet-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dechonet Com Vulnerability Disclosure
  slug: dechonet-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dechonet-com
tags:
- Company
- Security
- Monitoring
- Phishing
website: https://dechonet.com/
---
