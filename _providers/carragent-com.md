---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Carragent Com Agentic Access
  operation_count: 1
  slug: carragent-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://carragent.com
  baseurl_source: declared
  description: The AI agents Carragent runs for a business.
  name: carragent-com Agents API
  slug: carragent-com-agents-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/carragent-com/data-model/carragent-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carragent-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/carragent-com/agentic-access/carragent-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/carragent-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/carragent-com/plans/carragent-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/carragent-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/carragent-com/rules/carragent-com-rules.yml
  title: ''
  type: Spectral
  url: rules/carragent-com-rules.yml
- group: design
  href: https://artifacts.apis.io/carragent-com/vocabulary/carragent-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/carragent-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/carragent-com/conventions/carragent-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/carragent-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/carragent-com/conventions/carragent-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/carragent-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/carragent-com/security/carragent-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/carragent-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/carragent-com/authentication/carragent-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/carragent-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/carragent-com/errors/carragent-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/carragent-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/carragent-com/conformance/carragent-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carragent-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/carragent-com/llms/carragent-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carragent-com-llms.txt
- group: other
  href: https://artifacts.apis.io/carragent-com/a2a/carragent-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/carragent-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/carragent-com/mcp/carragent-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/carragent-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/carragent-com/well-known/carragent-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carragent-com-security.txt
- group: agent
  href: https://artifacts.apis.io/carragent-com/well-known/carragent-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carragent-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/carragent-com/hosts/carragent-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carragent-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/carragent-com/vendors/carragent-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carragent-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/carragent-com/packages/carragent-com-packages.yml
  title: ''
  type: SDKs
  url: packages/carragent-com-packages.yml
- group: build
  href: https://artifacts.apis.io/carragent-com/packages/carragent-com-packages.yml
  title: ''
  type: Packages
  url: packages/carragent-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carragent.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carragent.com/en/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://carragent.com/en/pricing
- group: docs
  title: ''
  type: APIReference
  url: https://carragent.com/en/developers
- group: auth
  href: https://artifacts.apis.io/carragent-com/security/carragent-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/carragent-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/carragent-com/security/carragent-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carragent-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carragent.com/
created: '2026-11-03'
description: Carragent provides AI agents that automate post‑closing administrative tasks for small businesses such as cafés, clinics, salons, shops and trades. The agents connect to existing tools like Stripe, Google Sheets, Outlook and HubSpot to handle supplier bills, stock orders, bookings, reviews and invoice follow‑ups, requiring user approval only for actions that exceed set limits.
image: https://carragent.com/en/opengraph-image-1yhjss/card?597f21948a7ae9d9
json_schemas:
- name: AgentList
  property_count: 0
  slug: carragent-com-agent-list
layout: provider
mcp_servers:
- description: Remote MCP server at carragent.com.
  name: carragent-com MCP Server
  slug: carragent-com-mcp-yml
modified: '2026-11-03'
name: carragent-com
nav: Providers
network: true
overview: 'carragent-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Agents API. Tagged areas include AI Agents and Business tools integration.


  The carragent-com catalog on APIs.io includes 1 Spectral governance ruleset.


  carragent-com''s developer surface includes authentication, pricing, API reference, and 24 more developer resources.'
plans:
- name: Carragent Com Plans Pricing
  plan_count: 3
  slug: carragent-com-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: carragent-com API Rules
  rule_count: 57
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 1
  slug: carragent-com-rules
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 55.2
    catalog_earned_first_party: 12.0
    catalog_gap: 59.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 52.7
    developer_ergonomics: 22.6
    discoverability: 56.7
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
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
  name: Carragent Com Authentication
  slug: carragent-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Carragent Com Domain Security
  slug: carragent-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Carragent Com Vulnerability Disclosure
  slug: carragent-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: carragent-com
tags:
- AI Agents
- Business tools integration
website: https://carragent.com/
---
