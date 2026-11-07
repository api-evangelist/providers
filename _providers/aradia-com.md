---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Aradia Com Agentic Access
  operation_count: 1
  slug: aradia-com-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Turnkey private AI hardware appliances (NVIDIA DGX Spark, Station, and B200) with autonomous Agent-to-Agent procurement via Stripe Machine Payments Protocol (MPP Fiat) and BTCPay Server (Crypto).
  name: Aradia API
  slug: aradia-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/aradia-com/agentic-access/aradia-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aradia-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/aradia-com/plans/aradia-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aradia-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aradia-com/rules/aradia-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aradia-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/aradia-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://aradia.com/compliance/
- group: design
  href: https://artifacts.apis.io/aradia-com/conformance/aradia-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aradia-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aradia-com/llms/aradia-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aradia-com-llms.txt
- group: other
  href: https://artifacts.apis.io/aradia-com/a2a/aradia-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aradia-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/aradia-com/mcp/aradia-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aradia-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aradia-com/mcp/aradia-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aradia-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aradia-com/well-known/aradia-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aradia-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aradia-com/hosts/aradia-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aradia-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aradia-com/vendors/aradia-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aradia-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aradia-com/security/aradia-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aradia-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/aradia-com/security/aradia-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aradia-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aradia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aradia.com/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://aradia.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aradia.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aradia.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://aradia.com/contact/
created: '2026-11-01'
description: Aradia delivers turnkey on-premise private Agentic AI infrastructure on NVIDIA DGX hardware, offering sovereign compute with zero cloud lock‑in and uncapped token usage. Engineering DNA since 1991, Aradia LLC pioneers on‑premise private AI, deploying turnkey NVIDIA DGX hardware clusters and custom multi‑agent runtimes for sovereign enterprise computing. The platform includes comprehensive pricing, compliance, privacy, and terms documentation, and provides a contact portal for support and procurement.
image: https://aradia.com/assets/images/ARADIA-OG-card.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at aradia.com.
  name: Aradia Systems MCP Server
  slug: aradia-com-mcp-yml
modified: '2026-11-01'
name: Aradia Systems
nav: Providers
network: true
overview: 'Aradia Systems is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Private AI, Infrastructure, NVIDIA, and DGX.


  The Aradia Systems catalog on APIs.io includes 1 Spectral governance ruleset.


  Aradia Systems'' developer surface includes documentation, pricing, support, and 18 more developer resources.'
plans:
- name: Aradia Com Plans Pricing
  plan_count: 3
  slug: aradia-com-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 65
  extends:
  - spectral:oas
  name: Aradia Systems API Rules
  rule_count: 24
  severity_counts:
    error: 22
    hint: 0
    info: 1
    warn: 1
  slug: aradia-com-rules
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 59.2
    contract_governance: 31.8
    contract_quality: 0.0
    developer_ergonomics: 8.9
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: glba
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aradia Com Domain Security
  slug: aradia-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Aradia Com Trust Center
  slug: aradia-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
skill_count: 1
skills:
- name: create-mpp-stripe-session
  slug: aradia-com-create-mpp-stripe-session
slug: aradia-com
tags:
- Artificial Intelligence
- Private AI
- Infrastructure
- NVIDIA
- DGX
- Sovereign
- On-Prem
- AI Agents
website: https://aradia.com/
---
