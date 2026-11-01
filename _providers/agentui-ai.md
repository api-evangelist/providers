---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://cdn.agentui.ai
  baseurl_source: declared
  description: 'agentui-ai API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: agentui-ai API
  slug: agentui-ai-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/agentui-ai/rules/agentui-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/agentui-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/agentui-ai/vocabulary/agentui-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentui-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentui-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/agentui-ai/cli/agentui-ai-cli.yml
  title: ''
  type: CLI
  url: cli/agentui-ai-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.agentui.ai/en/security/
- group: design
  href: https://artifacts.apis.io/agentui-ai/conformance/agentui-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentui-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentui-ai/llms/agentui-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentui-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentui-ai/mcp/agentui-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentui-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentui-ai/well-known/agentui-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentui-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentui-ai/hosts/agentui-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentui-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentui-ai/vendors/agentui-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentui-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/agentui-ai/packages/agentui-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/agentui-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/agentui-ai/packages/agentui-ai-packages.yml
  title: ''
  type: Packages
  url: packages/agentui-ai-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.agentui.ai/en/security/
- group: auth
  href: https://artifacts.apis.io/agentui-ai/security/agentui-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/agentui-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/agentui-ai/security/agentui-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentui-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentui-ai/security/agentui-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentui-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentui.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.agentui.ai/en/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.agentui.ai/en/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://www.agentui.ai/en/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.agentui.ai/en/developers/
- group: operate
  title: ''
  type: Support
  url: https://help.agentui.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.agentui.ai/en/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agentui.ai/en/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.agentui.ai/chat
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agentui.ai/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agentui.ai/en/privacy/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.agentui.ai/mcp
  - status: 401
    url: https://help.agentui.ai/mcp
  - status: 403
    url: https://agentui.ai/mcp
  - status: 403
    url: https://app.agentui.ai/mcp
  - status: 200
    url: https://agentui.ai/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Agent UI (agentui.ai) provides an AI‑plus‑human internal‑tool builder for operations teams. It lets businesses create dashboards, inventory management, approval workflows, and multi‑location applications without writing code. Users describe their needs in natural language and the platform generates functional tools, with a human support team ready to intervene. Free white‑glove onboarding ensures rapid adoption.
image: https://www.agentui.ai/blog/home-en.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.agentui.ai requiring OAuth.
  name: agentui-ai MCP Server
  slug: agentui-ai-mcp-yml
modified: '2026-10-30'
name: agentui-ai
nav: Providers
network: true
overview: 'agentui-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Internal-Tools, Automation, No-code, and LLM.


  The agentui-ai catalog on APIs.io includes 1 Spectral governance ruleset.


  agentui-ai''s developer surface includes CLI, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Agentui Ai Plans Pricing
  plan_count: 0
  slug: agentui-ai-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Agentui Ai Rate Limits
  slug: agentui-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: agentui-ai API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: agentui-ai-rules
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.7
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 79.1
    contract_quality: 35.5
    developer_ergonomics: 66.0
    discoverability: 65.0
    operational_transparency: 10.5
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentui Ai Domain Security
  slug: agentui-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Agentui Ai Vulnerability Disclosure
  slug: agentui-ai-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Agentui Ai Trust Center
  slug: agentui-ai-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: agentui-ai
tags:
- AI
- Internal-Tools
- Automation
- No-code
- LLM
- Company
website: https://agentui.ai/
---
