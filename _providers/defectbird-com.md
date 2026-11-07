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
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Defectbird MCP dataset API
  name: Defectbird API
  slug: defectbird-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/defectbird-com/plans/defectbird-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/defectbird-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/defectbird-com/vocabulary/defectbird-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/defectbird-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/defectbird-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://defectbird.com/terms
- group: design
  href: https://artifacts.apis.io/defectbird-com/conformance/defectbird-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/defectbird-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/defectbird-com/llms/defectbird-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/defectbird-com-llms.txt
- group: build
  href: https://artifacts.apis.io/defectbird-com/mcp/defectbird-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/defectbird-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/defectbird-com/mcp/defectbird-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/defectbird-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/defectbird-com/well-known/defectbird-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/defectbird-com-security.txt
- group: auth
  href: https://artifacts.apis.io/defectbird-com/well-known/defectbird-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/defectbird-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/defectbird-com/well-known/defectbird-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/defectbird-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/defectbird-com/hosts/defectbird-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/defectbird-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/defectbird-com/vendors/defectbird-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/defectbird-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://defectbird.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://defectbird.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://defectbird.com/privacy/
- group: auth
  href: https://artifacts.apis.io/defectbird-com/authentication/defectbird-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/defectbird-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/defectbird-com/security/defectbird-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/defectbird-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/defectbird-com/security/defectbird-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/defectbird-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://defectbird.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://defectbird.com/pricing/
created: '2026-11-05'
description: Defectbird provides software for US auto repair shops, mobile mechanics, and RV inspectors to run vehicle inspection checklists and generate defect lists. It offers a free checklist service and a paid Defectbird Pro plan at $29 per seat per month, storing inspections, photos, and authorizations. The platform aims to streamline multi‑point inspections for independent repair shops, mobile services, and fleet workshops, without handling state inspection laws or vehicle history data.
image: https://defectbird.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at defectbird.com.
  name: Defectbird MCP Server
  slug: defectbird-com-mcp-yml
modified: '2026-11-05'
name: Defectbird
nav: Providers
network: true
overview: 'Defectbird is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Inspection, Software, Software-as-a-Service, and US.


  Defectbird''s developer surface includes support, authentication, pricing, and 18 more developer resources.'
plans:
- name: Defectbird Com Plans Pricing
  plan_count: 2
  slug: defectbird-com-plans-pricing
random_paper: 8
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 46.3
    catalog_earned_first_party: 8.0
    catalog_gap: 68.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 23.1
    discoverability: 65.0
    operational_transparency: 10.5
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
  name: Defectbird Com Authentication
  slug: defectbird-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Defectbird Com Domain Security
  slug: defectbird-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Defectbird Com Vulnerability Disclosure
  slug: defectbird-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: defectbird-com
tags:
- Automotive
- Inspection
- Software
- Software-as-a-Service
- US
website: https://defectbird.com/
---
