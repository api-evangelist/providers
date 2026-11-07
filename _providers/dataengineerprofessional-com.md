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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Read‑only guide registry providing metadata about guides, books and knowledge‑skill‑area objects. Documentation at https://dataengineerprofessional.com/guides.
  name: Guide Registry API
  slug: guide-registry-api
- description: 'Data Engineer Professional API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Data Engineer Professional API
  slug: dataengineerprofessional-com-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/dataengineerprofessional-com/rules/dataengineerprofessional-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dataengineerprofessional-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dataengineerprofessional-com/json-ld/dataengineerprofessional-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dataengineerprofessional-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dataengineerprofessional-com/vocabulary/dataengineerprofessional-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dataengineerprofessional-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dataengineerprofessional-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dataengineerprofessional-com/data-model/dataengineerprofessional-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dataengineerprofessional-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/dataengineerprofessional-com/conformance/dataengineerprofessional-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dataengineerprofessional-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dataengineerprofessional-com/llms/dataengineerprofessional-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dataengineerprofessional-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dataengineerprofessional-com/mcp/dataengineerprofessional-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dataengineerprofessional-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/dataengineerprofessional-com/hosts/dataengineerprofessional-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dataengineerprofessional-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dataengineerprofessional-com/vendors/dataengineerprofessional-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dataengineerprofessional-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dataengineerprofessional-com/security/dataengineerprofessional-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataengineerprofessional-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dataengineerprofessional.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dataengineerprofessional.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://dataengineerprofessional.com/openapi.json
- group: start
  title: ''
  type: Login
  url: https://dataengineerprofessional.com/account?next=%2F
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dataengineerprofessional.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dataengineerprofessional.com/terms
- group: operate
  title: ''
  type: Support
  url: https://dataengineerprofessional.com/help
coverage:
  checked: '2026-11-05'
  detail: OpenAPI spec at https://dataengineerprofessional.com/openapi.json describes a different service (bicycle.guide) and thus is not owned.
  evidence:
  - status: 200
    url: https://dataengineerprofessional.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Data Engineer Professional provides a platform for data engineering guides, books, and resources. It focuses on analytics, AI, and the myriad sub‑specialties of data pipelines, offering tutorials, curated content, and community support for building robust data platforms.
image: https://dataengineerprofessional.com/opengraph-image-1oy18k?29435694197f5727
json_schemas:
- name: GetApiV1GuidesResponse
  property_count: 3
  slug: dataengineerprofessional-com-get-api-v1-guides-response
jsonld:
- class_count: 1
  name: Dataengineerprofessional Com Context
  property_count: 0
  slug: dataengineerprofessional-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at dataengineerprofessional.com.
  name: Data Engineer Professional MCP Server
  slug: dataengineerprofessional-com-mcp-yml
modified: '2026-11-04'
name: Data Engineer Professional
nav: Providers
network: true
overview: 'Data Engineer Professional is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data Engineering, Guides, Books, Community, and Analytics.


  The Data Engineer Professional catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Data Engineer Professional''s developer surface includes documentation, API reference, support, and 15 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Data Engineer Professional API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: dataengineerprofessional-com-rules
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 17.4
    developer_ergonomics: 27.9
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
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
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dataengineerprofessional Com Domain Security
  slug: dataengineerprofessional-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dataengineerprofessional-com
tags:
- Data Engineering
- Guides
- Books
- Community
- Analytics
website: https://dataengineerprofessional.com/
---
