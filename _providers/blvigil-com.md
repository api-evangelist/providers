---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Blvigil Com Agentic Access
  operation_count: 16
  slug: blvigil-com-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 1
apis:
- baseURL: https://blvigil.com
  baseurl_source: declared
  description: The Agent API from Vigil — 13 operation(s) for agent.
  name: Vigil Agent API
  slug: blvigil-com-agent-api
- baseURL: https://blvigil.com
  baseurl_source: declared
  description: The Mcp API from Vigil — 1 operation(s) for mcp.
  name: Vigil MCP API
  slug: blvigil-com-mcp-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/blvigil-com/agentic-access/blvigil-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blvigil-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/blvigil-com/rules/blvigil-com-rules.yml
  title: ''
  type: Spectral
  url: rules/blvigil-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/blvigil-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/blvigil-com/conventions/blvigil-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/blvigil-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/blvigil-com/conventions/blvigil-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/blvigil-com-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://blvigil.com/privacy
- group: auth
  href: https://artifacts.apis.io/blvigil-com/authentication/blvigil-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blvigil-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/blvigil-com/errors/blvigil-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blvigil-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blvigil-com/conformance/blvigil-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blvigil-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blvigil-com/llms/blvigil-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blvigil-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/blvigil-com/mcp/blvigil-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/blvigil-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/blvigil-com/well-known/blvigil-com-tryacee-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blvigil-com-tryacee-security.txt
- group: auth
  href: https://artifacts.apis.io/blvigil-com/well-known/blvigil-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blvigil-com-security.txt
- group: agent
  href: https://artifacts.apis.io/blvigil-com/well-known/blvigil-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blvigil-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/blvigil-com/hosts/blvigil-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blvigil-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/blvigil-com/vendors/blvigil-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blvigil-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blvigil.com/terms
- group: operate
  title: ''
  type: Support
  url: https://blvigil.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blvigil.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/black-label-tec
- group: docs
  title: ''
  type: Documentation
  url: https://blvigil.com/guides/
- group: start
  title: ''
  type: GettingStarted
  url: https://blvigil.com/resources/topics/setup/
- group: docs
  title: ''
  type: APIReference
  url: https://blvigil.com/developers
- group: auth
  href: https://artifacts.apis.io/blvigil-com/security/blvigil-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blvigil-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/blvigil-com/security/blvigil-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blvigil-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blvigil.com/
created: '2026-11-02'
description: Vigil provides local smart‑home and self‑monitored security software for Mac and Windows. It offers private room sensing, customizable scenes, and optional sensor hardware, enabling users to monitor and secure their homes without relying on cloud services.
image: https://blvigil.com/og-card.png
layout: provider
mcp_servers:
- description: Remote MCP server at blvigil.com.
  name: Vigil MCP Server
  slug: blvigil-com-mcp-yml
modified: '2026-11-02'
name: Vigil
nav: Providers
network: true
overview: 'Vigil publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Agent API and MCP API. Tagged areas include Home Automation, Security, Smart Home, Software, and Mac.


  The Vigil catalog on APIs.io includes 1 Spectral governance ruleset.


  Vigil''s developer surface includes authentication, support, documentation, getting-started guide, API reference, and 21 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Vigil API Rules
  rule_count: 36
  severity_counts:
    error: 31
    hint: 0
    info: 3
    warn: 2
  slug: blvigil-com-rules
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 39.8
    developer_ergonomics: 30.4
    discoverability: 65.0
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blvigil Com Authentication
  slug: blvigil-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Blvigil Com Domain Security
  slug: blvigil-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Blvigil Com Vulnerability Disclosure
  slug: blvigil-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: blvigil-com-create-and-complete-ucp-checkout
  slug: blvigil-com-create-and-complete-ucp-checkout
slug: blvigil-com
tags:
- Home Automation
- Security
- Smart Home
- Software
- Mac
- Windows
website: https://blvigil.com/
---
