---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 15.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/boim-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/boim-io/conformance/boim-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boim-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/boim-io/llms/boim-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boim-io-llms.txt
- group: other
  href: https://artifacts.apis.io/boim-io/a2a/boim-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/boim-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/boim-io/mcp/boim-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/boim-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/boim-io/well-known/boim-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boim-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/boim-io/hosts/boim-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boim-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/boim-io/vendors/boim-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boim-io-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://boim.io/vendors/register/
- group: auth
  href: https://artifacts.apis.io/boim-io/security/boim-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boim-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boim.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://boim.io/connect/
- group: operate
  title: ''
  type: Support
  url: https://boim.io/status/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boim.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boim.io/privacy/
created: '2026-11-02'
description: 보임(BOIM)은 AI 에이전트와 봇이 날마다 들르는 한국 업체 정보 통로입니다. 우리 가게를 무료로 등록하면 AI가 읽는 업체 카드가 됩니다. 전국 전 업종 업체 2,750,939곳과 공공 실적 업체 카드 76,053장을 출처·기준일과 함께 엽니다. AEO·GEO의 첫걸음. This platform serves as a gateway for AI agents to discover Korean businesses, offering free registration for companies to appear in AI-read cards, covering millions of enterprises across various sectors with sourced and dated data.
image: https://boim.io/assets/og.png?v=20261102
layout: provider
mcp_servers:
- description: Remote MCP server at boim.io.
  name: 보임 (BOIM) MCP Server
  slug: boim-io-mcp-yml
modified: '2026-11-02'
name: 보임 (BOIM)
nav: Providers
network: true
overview: '보임 (BOIM) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Korean, Business Directory, Artificial Intelligence, FreeRegistration, and Data Portal.


  보임 (BOIM)''s developer surface includes signup flow, support, and 13 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 13.6
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boim Io Domain Security
  slug: boim-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boim-io
tags:
- Korean
- Business Directory
- Artificial Intelligence
- FreeRegistration
- Data Portal
website: https://boim.io/
---
