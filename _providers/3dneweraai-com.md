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
    agent_card: false
    agent_skills: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for 3D New Era AI platform, documented at the developer docs.
  name: 3D New Era AI API
  slug: 3d-new-era-ai-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/3dneweraai-com/llms/3dneweraai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/3dneweraai-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/3dneweraai-com/mcp/3dneweraai-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/3dneweraai-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/3dneweraai-com/well-known/3dneweraai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/3dneweraai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/3dneweraai-com/hosts/3dneweraai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/3dneweraai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/3dneweraai-com/vendors/3dneweraai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/3dneweraai-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://3dneweraai.com/press/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/leandrodaf/3d-new-era-ai/releases/latest
- group: auth
  href: https://artifacts.apis.io/3dneweraai-com/security/3dneweraai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/3dneweraai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://3dneweraai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://3dneweraai.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://3dneweraai.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://3dneweraai.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://3dneweraai.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://3dneweraai.com/privacy/
coverage:
  checked: '2026-10-31'
  detail: Docs are rendered client‑side JavaScript, no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://3dneweraai.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: 3D New Era AI offers an open-source architecture and interiors editor powered by a multi‑modal conversational AI. Users can design homes by speaking to the AI, which draws, furnishes, lights, and renders realistic images in real time. The platform runs on Windows, macOS, and Linux, and includes an MCP server for extensibility. It aims to democratize high‑quality interior design through accessible AI tools.
image: https://3dneweraai.com/og.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.3dneweraai.com requiring OAuth.
  name: 3D New Era AI MCP Server
  slug: 3dneweraai-com-mcp-yml
modified: '2026-10-31'
name: 3D New Era AI
nav: Providers
network: true
overview: '3D New Era AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Architecture, Interior Design, Open Source, and Multi-Modal.


  3D New Era AI''s developer surface includes changelog, documentation, API reference, pricing, and 10 more developer resources.'
plans:
- name: 3Dneweraai Com Plans Pricing
  plan_count: 0
  slug: 3dneweraai-com-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 57.5
    operational_transparency: 7.9
  previous_composite: 17.6
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 3Dneweraai Com Domain Security
  slug: 3dneweraai-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 3dneweraai-com
tags:
- Artificial Intelligence
- Architecture
- Interior Design
- Open Source
- Multi-Modal
website: https://3dneweraai.com/
---
