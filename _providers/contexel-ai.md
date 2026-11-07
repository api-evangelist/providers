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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Contexel provides AI memory APIs for storing and retrieving shared context across AI assistants. Documentation is at https://contexel.ai/docs.
  name: Contexel API
  slug: contexel-api
- description: 'Contexel API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Contexel API
  slug: contexel-ai-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/contexel-ai/plans/contexel-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contexel-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/contexel-ai/rules/contexel-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/contexel-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/contexel-ai/vocabulary/contexel-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/contexel-ai-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/contexel-ai/cli/contexel-ai-cli.yml
  title: ''
  type: CLI
  url: cli/contexel-ai-cli.yml
- group: operate
  href: https://artifacts.apis.io/contexel-ai/changelog/contexel-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/contexel-ai-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://contexel.ai/security
- group: design
  href: https://artifacts.apis.io/contexel-ai/conformance/contexel-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contexel-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/contexel-ai/llms/contexel-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contexel-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/contexel-ai/mcp/contexel-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/contexel-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/contexel-ai/well-known/contexel-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/contexel-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/contexel-ai/well-known/contexel-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contexel-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/contexel-ai/hosts/contexel-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contexel-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/contexel-ai/vendors/contexel-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contexel-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contexel.ai/terms
- group: auth
  title: ''
  type: Security
  url: https://contexel.ai/security
- group: start
  title: ''
  type: Sandbox
  url: https://contexel.ai/console
- group: operate
  title: ''
  type: ChangeLog
  url: https://contexel.ai/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contexel
- group: auth
  href: https://artifacts.apis.io/contexel-ai/security/contexel-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/contexel-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/contexel-ai/security/contexel-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/contexel-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/contexel-ai/security/contexel-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contexel-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contexel.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://contexel.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://contexel.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contexel.ai/privacy
coverage:
  checked: '2026-11-04'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://contexel.ai/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Contexel provides AI memory for teams, enabling shared context across multiple AI assistants such as ChatGPT, Claude, Cursor, and others. Users can store information once and have it remembered by all connected AI tools, facilitating seamless collaboration within teams, families, or personal workflows. The platform emphasizes privacy, data portability, and easy integration via the MCP standard, allowing users to download their memories or manage access controls across shared workspaces.
image: https://contexel.ai/og/home.png?v=d37ee49aa34c
layout: provider
mcp_servers:
- description: Remote MCP server at contexel.ai requiring OAuth.
  name: Contexel MCP Server
  slug: contexel-ai-mcp-yml
modified: '2026-11-04'
name: Contexel
nav: Providers
network: true
overview: 'Contexel is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI memory, Family workspace, Personal workspace, ChatGPT, and Claude.


  The Contexel catalog on APIs.io includes 1 Spectral governance ruleset.


  Contexel''s developer surface includes CLI, changelog, sandbox, documentation, pricing, and 20 more developer resources.'
plans:
- name: Contexel Ai Plans Pricing
  plan_count: 4
  slug: contexel-ai-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 62
  extends:
  - spectral:oas
  name: Contexel API Rules
  rule_count: 21
  severity_counts:
    error: 19
    hint: 0
    info: 1
    warn: 1
  slug: contexel-ai-rules
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 23.8
    discoverability: 56.7
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contexel Ai Domain Security
  slug: contexel-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Contexel Ai Vulnerability Disclosure
  slug: contexel-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Contexel Ai Trust Center
  slug: contexel-ai-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: contexel-ai
tags:
- AI memory
- Family workspace
- Personal workspace
- ChatGPT
- Claude
- Cursor
website: https://contexel.ai/
---
