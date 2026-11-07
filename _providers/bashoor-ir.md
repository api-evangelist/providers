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
    agent_skills: derived
    agentic_access: false
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
  score: 5.1
  scored_at: '2026-11-06'
api_count: 1
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/bashoor-ir/rules/bashoor-ir-rules.yml
  title: ''
  type: Spectral
  url: rules/bashoor-ir-rules.yml
- group: design
  href: https://artifacts.apis.io/bashoor-ir/json-ld/bashoor-ir-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bashoor-ir-context.jsonld
- group: design
  href: https://artifacts.apis.io/bashoor-ir/vocabulary/bashoor-ir-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bashoor-ir-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bashoor-ir/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bashoor-ir/data-model/bashoor-ir-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bashoor-ir-data-model.yml
- group: design
  href: https://artifacts.apis.io/bashoor-ir/errors/bashoor-ir-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bashoor-ir-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bashoor-ir/conformance/bashoor-ir-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bashoor-ir-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bashoor-ir/llms/bashoor-ir-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bashoor-ir-llms.txt
- group: build
  href: https://artifacts.apis.io/bashoor-ir/mcp/bashoor-ir-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bashoor-ir-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bashoor-ir/mcp/bashoor-ir-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bashoor-ir-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bashoor-ir/well-known/bashoor-ir-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bashoor-ir-well-known.yml
- group: other
  href: https://artifacts.apis.io/bashoor-ir/hosts/bashoor-ir-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bashoor-ir-hosts.yml
- group: auth
  href: https://artifacts.apis.io/bashoor-ir/security/bashoor-ir-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bashoor-ir-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bashoor.ir/
- group: docs
  title: ''
  type: Documentation
  url: https://bashoor.ir/about
- group: company
  title: ''
  type: Blog
  url: https://bashoor.ir/blog
coverage:
  checked: '2026-11-02'
  detail: The provider is a café with no public API surface.
  evidence:
  - status: 200
    url: https://bashoor.ir/
  reason: not-a-software-company
  state: none
created: '2026-11-02'
description: کافه باشور یک کافه و کافی‌شاپ در بلوار پیروزی مشهد است که با ارائه منوهای متنوع از صبحانه تا دسرهای روزانه، فضای داخلی بدون دود و حیاط باز، خدمات رزرو میز و تحویل آنلاین را فراهم می‌کند. هدف این کافه ارائه تجربه‌ای صمیمی و آرام برای مهمانان است و به‌صورت شفاف درباره منو، قیمت و ساعات کاری اطلاعات را در وب‌سایت خود منتشر می‌کند.
image: https://bashoor.ir/og-image.jpg
jsonld:
- class_count: 8
  name: Bashoor Ir Context
  property_count: 57
  slug: bashoor-ir-context
layout: provider
mcp_servers:
- description: Remote MCP server at bashoor.ir.
  name: کافه باشور MCP Server
  slug: bashoor-ir-mcp-yml
modified: '2026-11-02'
name: کافه باشور
nav: Providers
network: true
overview: 'کافه باشور publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Coffee Shop, Cafe, and Mashhad.


  The کافه باشور catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  کافه باشور''s developer surface includes documentation, engineering blog, and 14 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: کافه باشور API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: bashoor-ir-rules
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 38.8
    catalog_earned_first_party: 0.0
    catalog_gap: 76.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 14.7
    developer_ergonomics: 7.7
    discoverability: 40.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bashoor Ir Domain Security
  slug: bashoor-ir-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: bashoor-ir-retrieve-menu
  slug: bashoor-ir-retrieve-menu
slug: bashoor-ir
tags:
- Coffee Shop
- Cafe
- Mashhad
website: https://bashoor.ir/
---
