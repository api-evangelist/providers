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
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
  score: 15.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Authichain Com Agentic Access
  operation_count: 6
  slug: authichain-com-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- description: API for verification services as documented in the AuthiChain docs.
  name: AuthiChain API
  slug: authichain-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/authichain-com/agentic-access/authichain-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/authichain-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/authichain-com/plans/authichain-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/authichain-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/authichain-com/rules/authichain-com-rules.yml
  title: ''
  type: Spectral
  url: rules/authichain-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/authichain-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/authichain-com/errors/authichain-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/authichain-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/authichain-com/conformance/authichain-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/authichain-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/authichain-com/llms/authichain-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/authichain-com-llms.txt
- group: other
  href: https://artifacts.apis.io/authichain-com/a2a/authichain-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/authichain-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/authichain-com/mcp/authichain-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/authichain-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/authichain-com/mcp/authichain-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/authichain-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/authichain-com/well-known/authichain-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/authichain-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/authichain-com/hosts/authichain-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/authichain-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/authichain-com/vendors/authichain-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/authichain-com-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://authichain.com/blog/eu-dpp-manufacturer
- group: auth
  href: https://artifacts.apis.io/authichain-com/security/authichain-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/authichain-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://authichain.com/
- group: docs
  title: ''
  type: Documentation
  url: https://authichain.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://authichain.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://authichain.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://authichain.com/privacy
created: '2026-11-02'
description: AuthiChain provides verification infrastructure for the physical world, enabling authentic agentic economy solutions. Their platform offers QR-based product identity, digital signatures, and anchor hashes to verify claims, supporting digital product passports, battery passports, and compliance with upcoming regulations. The service includes documentation, pricing plans, and APIs for developers, manufacturers, and regulators to integrate verification into products and supply chains.
image: https://authichain.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at authichain.com.
  name: AuthiChain MCP Server
  slug: authichain-com-mcp-yml
modified: '2026-11-02'
name: AuthiChain
nav: Providers
network: true
overview: 'AuthiChain is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Verification, QR, Digital Product Passport, and Supply Chain.


  The AuthiChain catalog on APIs.io includes 1 Spectral governance ruleset.


  AuthiChain''s developer surface includes engineering blog, documentation, pricing, and 17 more developer resources.'
plans:
- name: Authichain Com Plans Pricing
  plan_count: 5
  slug: authichain-com-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: AuthiChain API Rules
  rule_count: 33
  severity_counts:
    error: 30
    hint: 0
    info: 2
    warn: 1
  slug: authichain-com-rules
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 12.4
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 25.5
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Authichain Com Domain Security
  slug: authichain-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: verification
  slug: authichain-com-verification
slug: authichain-com
tags:
- Company
- Verification
- QR
- Digital Product Passport
- Supply Chain
website: https://authichain.com/
---
