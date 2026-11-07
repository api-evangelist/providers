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
    agent_card: flavored
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agentsgetpaidmore Com Agentic Access
  operation_count: 1
  slug: agentsgetpaidmore-com-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- description: Sales site API for Agents Get Paid Kit providing MCP tools and payment concepts.
  name: Agents Get Paid Kit API
  slug: agents-get-paid-kit-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/agentsgetpaidmore-com/agentic-access/agentsgetpaidmore-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentsgetpaidmore-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentsgetpaidmore-com/rules/agentsgetpaidmore-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agentsgetpaidmore-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agentsgetpaidmore-com/conformance/agentsgetpaidmore-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentsgetpaidmore-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentsgetpaidmore-com/llms/agentsgetpaidmore-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentsgetpaidmore-com-llms.txt
- group: other
  href: https://artifacts.apis.io/agentsgetpaidmore-com/a2a/agentsgetpaidmore-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentsgetpaidmore-com-a2a.yml
- group: other
  href: https://artifacts.apis.io/agentsgetpaidmore-com/hosts/agentsgetpaidmore-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentsgetpaidmore-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentsgetpaidmore-com/vendors/agentsgetpaidmore-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentsgetpaidmore-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentsgetpaidmore-com/security/agentsgetpaidmore-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentsgetpaidmore-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentsgetpaidmore.com/
- group: docs
  title: ''
  type: APIReference
  url: https://agentsgetpaidmore.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://agentsgetpaidmore.com/
- group: operate
  title: ''
  type: FAQ
  url: https://agentsgetpaidmore.com/
- group: operate
  title: ''
  type: Support
  url: https://agentsgetpaidmore.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agentsgetpaidmore.com/mcp
created: '2026-11-01'
description: Agents Get Paid More provides a monetization kit for external agents, enabling them to implement x402 MCP capabilities with a $49 handoff. The service includes guidance on wallet setup, spend caps, rate limits, and an acceptable use policy, plus optional metered tools like CAPTCHA solving. It targets developers building agent-based services on Base network, offering a compliant, human‑administered solution.
image: https://agentsgetpaidmore.com/logo.png
layout: provider
modified: '2026-11-01'
name: Agents Get Paid More
nav: Providers
network: true
overview: 'Agents Get Paid More publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Payments, Monetization, x402, and MCP.


  The Agents Get Paid More catalog on APIs.io includes 1 Spectral governance ruleset.


  Agents Get Paid More''s developer surface includes API reference, pricing, FAQ, support, and 10 more developer resources.'
plans:
- name: Agentsgetpaidmore Com Plans Pricing
  plan_count: 2
  slug: agentsgetpaidmore-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Agentsgetpaidmore Com Rate Limits
  slug: agentsgetpaidmore-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 46
  extends:
  - spectral:oas
  name: Agents Get Paid More API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 1
  slug: agentsgetpaidmore-com-rules
scopes:
- name: Agentsgetpaidmore Com Scopes
  scope_count: 0
  slug: agentsgetpaidmore-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 6.0
    developer_ergonomics: 10.7
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 20.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentsgetpaidmore Com Authentication
  slug: agentsgetpaidmore-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agentsgetpaidmore Com Domain Security
  slug: agentsgetpaidmore-com-domain-security
  summary_line: TLSv1.3
slug: agentsgetpaidmore-com
tags:
- Fintech
- Payments
- Monetization
- x402
- MCP
website: https://agentsgetpaidmore.com/
---
