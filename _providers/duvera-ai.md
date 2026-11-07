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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public API enabling read‑only access to open data such as flight feeds, with no authentication required.
  name: Duvera API
  slug: duvera-api
- baseURL: https://app.duvera.ai
  baseurl_source: declared
  description: 'Duvera API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: Duvera API
  slug: duvera-ai-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/duvera-ai/plans/duvera-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/duvera-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/duvera-ai/rules/duvera-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/duvera-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/duvera-ai/vocabulary/duvera-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/duvera-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/duvera-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://duvera.ai/trust
- group: auth
  href: https://artifacts.apis.io/duvera-ai/authentication/duvera-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/duvera-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/duvera-ai/conformance/duvera-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/duvera-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/duvera-ai/llms/duvera-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/duvera-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/duvera-ai/mcp/duvera-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/duvera-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/duvera-ai/well-known/duvera-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/duvera-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/duvera-ai/well-known/duvera-ai-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/duvera-ai-app-security.txt
- group: agent
  href: https://artifacts.apis.io/duvera-ai/well-known/duvera-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/duvera-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/duvera-ai/hosts/duvera-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/duvera-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/duvera-ai/vendors/duvera-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/duvera-ai-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://app.duvera.ai/plans
- group: auth
  href: https://artifacts.apis.io/duvera-ai/security/duvera-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/duvera-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/duvera-ai/security/duvera-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/duvera-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/duvera-ai/security/duvera-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/duvera-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://duvera.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://duvera.ai/quickstart
- group: start
  title: ''
  type: GettingStarted
  url: https://duvera.ai/quickstart
- group: other
  title: ''
  type: AgentInstructions
  url: https://duvera.ai/agent-instructions.md
- group: agent
  title: ''
  type: LLMs
  url: https://duvera.ai/llms.txt
- group: auth
  title: ''
  type: Security
  url: https://duvera.ai/security.html
coverage:
  checked: '2026-11-06'
  detail: Provider documentation offers a public quickstart but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec is published.
  evidence:
  - status: 200
    url: https://duvera.ai/quickstart.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: Duvera provides audit‑ready governance for AI agents, acting as a policy enforcement layer that logs every action, produces cryptographically signed receipts, and offers searchable evidence for compliance. It supports both personal and enterprise use, integrates with popular AI tools like Claude, Cursor, and ChatGPT, and offers a free personal tier with spend caps and kill‑switches. The platform includes a live demo, detailed documentation, and a marketplace of policies, enabling organizations to control AI behavior, prevent unauthorized writes, and satisfy security audits.
layout: provider
mcp_servers:
- description: Remote MCP server at app.duvera.ai.
  name: Duvera MCP Server
  slug: duvera-ai-mcp-yml
modified: '2026-11-06'
name: Duvera
nav: Providers
network: true
overview: 'Duvera is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Governance, Audit, Compliance, and Enterprise.


  The Duvera catalog on APIs.io includes 1 Spectral governance ruleset.


  Duvera''s developer surface includes authentication, pricing, documentation, getting-started guide, and 20 more developer resources.'
plans:
- name: Duvera Ai Plans Pricing
  plan_count: 3
  slug: duvera-ai-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 72
  extends:
  - spectral:oas
  name: Duvera API Rules
  rule_count: 31
  severity_counts:
    error: 29
    hint: 0
    info: 1
    warn: 1
  slug: duvera-ai-rules
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 47.8
    catalog_earned_first_party: 12.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 57.9
    contract_governance: 35.6
    contract_quality: 11.9
    developer_ergonomics: 39.8
    discoverability: 53.3
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Duvera Ai Authentication
  slug: duvera-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Duvera Ai Domain Security
  slug: duvera-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Duvera Ai Vulnerability Disclosure
  slug: duvera-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Duvera Ai Trust Center
  slug: duvera-ai-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, GDPR
slug: duvera-ai
tags:
- Company
- AI Governance
- Audit
- Compliance
- Enterprise
- Personal
website: https://duvera.ai/
---
