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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: 3Dvalley Com Agentic Access
  operation_count: 14
  slug: 3dvalley-com-agentic-access
  summary_line: 14 operations · 2 acting
api_count: 1
apis:
- baseURL: https://3dvalley.com/api/v1
  baseurl_source: declared
  description: The Account API from 3D Valley — 2 operation(s) for account.
  name: 3D Valley Account API
  slug: 3dvalley-com-account-api
- baseURL: https://3dvalley.com/api/v1
  baseurl_source: declared
  description: The Assets API from 3D Valley — 4 operation(s) for assets.
  name: 3D Valley Assets API
  slug: 3dvalley-com-assets-api
- baseURL: https://3dvalley.com/api/v1
  baseurl_source: declared
  description: The Categories API from 3D Valley — 1 operation(s) for categories.
  name: 3D Valley Categories API
  slug: 3dvalley-com-categories-api
- baseURL: https://3dvalley.com/api/v1
  baseurl_source: declared
  description: The Jobs API from 3D Valley — 4 operation(s) for jobs.
  name: 3D Valley Jobs API
  slug: 3dvalley-com-jobs-api
- baseURL: https://3dvalley.com/api/v1
  baseurl_source: declared
  description: The Tools API from 3D Valley — 1 operation(s) for tools.
  name: 3D Valley Tools API
  slug: 3dvalley-com-tools-api
- baseURL: https://3dvalley.com/api/v1
  baseurl_source: declared
  description: The Uploads API from 3D Valley — 1 operation(s) for uploads.
  name: 3D Valley Uploads API
  slug: 3dvalley-com-uploads-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/3dvalley-com/agentic-access/3dvalley-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/3dvalley-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/3dvalley-com/plans/3dvalley-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/3dvalley-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/3dvalley-com/rules/3dvalley-com-rules.yml
  title: ''
  type: Spectral
  url: rules/3dvalley-com-rules.yml
- group: design
  href: https://artifacts.apis.io/3dvalley-com/json-ld/3dvalley-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/3dvalley-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/3dvalley-com/vocabulary/3dvalley-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/3dvalley-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/3dvalley-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/3dvalley-com/data-model/3dvalley-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/3dvalley-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/3dvalley-com/conventions/3dvalley-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/3dvalley-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/3dvalley-com/conventions/3dvalley-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/3dvalley-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/3dvalley-com/errors/3dvalley-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/3dvalley-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/3dvalley-com/conformance/3dvalley-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/3dvalley-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/3dvalley-com/llms/3dvalley-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/3dvalley-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/3dvalley-com/mcp/3dvalley-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/3dvalley-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/3dvalley-com/well-known/3dvalley-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/3dvalley-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/3dvalley-com/hosts/3dvalley-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/3dvalley-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/3dvalley-com/vendors/3dvalley-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/3dvalley-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://3dvalley.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://3dvalley.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://3dvalley.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://3dvalley.com/blog
- group: auth
  href: https://artifacts.apis.io/3dvalley-com/authentication/3dvalley-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/3dvalley-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/3dvalley-com/security/3dvalley-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/3dvalley-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://3dvalley.com
- group: docs
  title: ''
  type: Documentation
  url: https://3dvalley.com/docs/api
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://3dvalley.com/mcp
  - status: 200
    url: https://3dvalley.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: 3D Valley provides free AI‑powered tools that turn a photo or text description into a textured 3D model, generate seamless textures, retexture, remesh, reduce polygon count, and access a library of over 10,000 CC0 models, textures and HDRIs. The tools run in the browser or via an MCP server and REST API, and the generated assets can be downloaded for printing, games or web use. Users retain ownership of the outputs and no attribution is required for the CC0 library assets.
image: https://3dvalley.com/opengraph-image?5a179b27d7b80c89
jsonld:
- class_count: 4
  name: 3Dvalley Com Context
  property_count: 26
  slug: 3dvalley-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at 3dvalley.com.
  name: 3D Valley MCP Server
  slug: 3dvalley-com-mcp-yml
modified: '2026-11-05'
name: 3D Valley
nav: Providers
network: true
overview: '3D Valley publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Assets API, Categories API, and 3 more. Tagged areas include AI Generation, Texture Generation, Asset Library, and Browser Tools.


  The 3D Valley catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  3D Valley''s developer surface includes pricing, engineering blog, authentication, documentation, and 20 more developer resources.'
plans:
- name: 3Dvalley Com Plans Pricing
  plan_count: 4
  slug: 3dvalley-com-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: 3D Valley API Rules
  rule_count: 47
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 2
  slug: 3dvalley-com-rules
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.8
    catalog_earned_first_party: 12.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 51.1
    developer_ergonomics: 25.6
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 3Dvalley Com Authentication
  slug: 3dvalley-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: 3Dvalley Com Domain Security
  slug: 3dvalley-com-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: 3dvalley-com-download-asset
  slug: 3dvalley-com-download-asset
slug: 3dvalley-com
tags:
- AI Generation
- Texture Generation
- Asset Library
- Browser Tools
website: https://3dvalley.com
---
