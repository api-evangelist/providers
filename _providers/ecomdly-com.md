---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for ecomdly skills and raw markdown endpoints as documented in the developer docs.
  name: ecomdly API
  slug: ecomdly-api
- description: 'ecomdly API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: ecomdly API
  slug: ecomdly-com-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/ecomdly-com/rules/ecomdly-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ecomdly-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ecomdly-com/json-ld/ecomdly-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ecomdly-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ecomdly-com/vocabulary/ecomdly-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ecomdly-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ecomdly-com/data-model/ecomdly-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ecomdly-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/ecomdly-com/authentication/ecomdly-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ecomdly-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/ecomdly-com/conformance/ecomdly-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ecomdly-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ecomdly-com/llms/ecomdly-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ecomdly-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ecomdly-com/mcp/ecomdly-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ecomdly-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ecomdly-com/well-known/ecomdly-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ecomdly-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ecomdly-com/hosts/ecomdly-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ecomdly-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ecomdly-com/vendors/ecomdly-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ecomdly-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ecomdly.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ecomdly.com/privacy
- group: auth
  href: https://artifacts.apis.io/ecomdly-com/security/ecomdly-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ecomdly-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ecomdly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ecomdly.com/docs
- group: operate
  title: ''
  type: APIStatus
  url: https://ecomdly.com/status
- group: company
  title: ''
  type: Blog
  url: https://ecomdly.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ecomdly
coverage:
  checked: '2026-11-06'
  detail: Documentation is provided as markdown files without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://ecomdly.com/docs.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: ecomdly provides AI agents and skills for online stores, offering reviewed Markdown skills for product feeds, Google Shopping, GA4, catalog translation, and checkout automation. Hosted in Slack or Discord, the service is free for a month and includes a range of e‑commerce integrations.
image: https://ecomdly.com/img/brand/og-share.png
json_schemas:
- name: GetRawOwnerSkillMdResponse
  property_count: 3
  slug: ecomdly-com-get-raw-owner-skill-md-response
- name: GetRawOwnerSkillSkillMdResponse
  property_count: 3
  slug: ecomdly-com-get-raw-owner-skill-skill-md-response
- name: PostV1SkillsRequest
  property_count: 3
  slug: ecomdly-com-post-v1-skills-request
- name: PutV1SkillsOwnerSkillRequest
  property_count: 2
  slug: ecomdly-com-put-v1-skills-owner-skill-request
jsonld:
- class_count: 4
  name: Ecomdly Com Context
  property_count: 7
  slug: ecomdly-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at ecomdly.com.
  name: ecomdly MCP Server
  slug: ecomdly-com-mcp-yml
modified: '2026-11-06'
name: ecomdly
nav: Providers
network: true
overview: 'ecomdly is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Artificial Intelligence, Agents, and Skills.


  The ecomdly catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ecomdly''s developer surface includes authentication, documentation, engineering blog, and 16 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: ecomdly API Rules
  rule_count: 37
  severity_counts:
    error: 34
    hint: 0
    info: 2
    warn: 1
  slug: ecomdly-com-rules
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 23.8
    discoverability: 56.7
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ecomdly Com Authentication
  slug: ecomdly-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ecomdly Com Domain Security
  slug: ecomdly-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ecomdly-com
tags:
- Company
- E-Commerce
- Artificial Intelligence
- Agents
- Skills
- Integration
website: https://ecomdly.com/
---
