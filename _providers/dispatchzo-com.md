---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Dispatchzo API providing dataset tools via MCP.
  name: Dispatchzo API
  slug: dispatchzo-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/dispatchzo-com/rules/dispatchzo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dispatchzo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dispatchzo-com/errors/dispatchzo-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dispatchzo-com-problem-types.yml
- group: commercial
  href: https://artifacts.apis.io/dispatchzo-com/plans/dispatchzo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dispatchzo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dispatchzo-com/vocabulary/dispatchzo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dispatchzo-com-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://dispatchzo.com/terms
- group: design
  href: https://artifacts.apis.io/dispatchzo-com/conformance/dispatchzo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dispatchzo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dispatchzo-com/llms/dispatchzo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dispatchzo-com-llms.txt
- group: build
  href: https://artifacts.apis.io/dispatchzo-com/mcp/dispatchzo-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dispatchzo-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dispatchzo-com/mcp/dispatchzo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dispatchzo-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/dispatchzo-com/well-known/dispatchzo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dispatchzo-com-security.txt
- group: auth
  href: https://artifacts.apis.io/dispatchzo-com/well-known/dispatchzo-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dispatchzo-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/dispatchzo-com/well-known/dispatchzo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dispatchzo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dispatchzo-com/hosts/dispatchzo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dispatchzo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dispatchzo-com/vendors/dispatchzo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dispatchzo-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dispatchzo-com/authentication/dispatchzo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dispatchzo-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dispatchzo-com/security/dispatchzo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dispatchzo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dispatchzo-com/security/dispatchzo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dispatchzo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dispatchzo.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://dispatchzo.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dispatchzo.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dispatchzo.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://dispatchzo.com/support/
- group: operate
  title: ''
  type: Contact
  url: https://dispatchzo.com/contact/
created: '2026-11-05'
description: Dispatchzo provides field service scheduling and dispatch software that helps businesses manage and coordinate on‑site work. The platform offers tools for scheduling service calls, managing field labor rates, and optimizing dispatch routes. It includes pricing information, datasets for benchmarking, and support resources, aiming to streamline operations for small to medium‑size service companies.
image: https://dispatchzo.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at dispatchzo.com.
  name: Dispatchzo MCP Server
  slug: dispatchzo-com-mcp-yml
modified: '2026-11-05'
name: Dispatchzo
nav: Providers
network: true
overview: 'Dispatchzo publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Field Service Scheduling, Dispatch Software, Small Business Software, and Pricing Tools.


  The Dispatchzo catalog on APIs.io includes 1 Spectral governance ruleset.


  Dispatchzo''s developer surface includes authentication, pricing, support, and 20 more developer resources.'
plans:
- name: Dispatchzo Com Plans Pricing
  plan_count: 1
  slug: dispatchzo-com-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Dispatchzo API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: dispatchzo-com-rules
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 56.7
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: first-party
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
  name: Dispatchzo Com Authentication
  slug: dispatchzo-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dispatchzo Com Domain Security
  slug: dispatchzo-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Dispatchzo Com Vulnerability Disclosure
  slug: dispatchzo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dispatchzo-com
tags:
- Field Service Scheduling
- Dispatch Software
- Small Business Software
- Pricing Tools
website: https://dispatchzo.com/
---
