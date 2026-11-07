---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Citevana API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Citevana API
  slug: citevana-com-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/citevana-com/plans/citevana-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/citevana-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/citevana-com/rules/citevana-com-rules.yml
  title: ''
  type: Spectral
  url: rules/citevana-com-rules.yml
- group: design
  href: https://artifacts.apis.io/citevana-com/json-ld/citevana-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/citevana-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/citevana-com/vocabulary/citevana-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/citevana-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/citevana-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/citevana-com/data-model/citevana-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/citevana-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/citevana-com/conformance/citevana-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/citevana-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/citevana-com/llms/citevana-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/citevana-com-llms.txt
- group: other
  href: https://artifacts.apis.io/citevana-com/hosts/citevana-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citevana-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://citevana.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://citevana.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://citevana.com/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://citevana.com/developers
- group: auth
  href: https://artifacts.apis.io/citevana-com/security/citevana-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citevana-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citevana.com/
- group: company
  title: ''
  type: Blog
  url: https://citevana.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://citevana.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://citevana.com/about
- group: other
  title: ''
  type: SignIn
  url: https://citevana.com/login
created: '2026-11-03'
description: Citevana provides a free AI-powered search visibility and SEO platform that audits websites, identifies AI citation blocks, and offers fixes. It offers tools like AI crawler checker, llms.txt generator, page audit, and AI visibility check, all without agency services. The platform aims to improve AI citation of sites and enhance discoverability.
json_schemas:
- name: GetApiV1ToolsAiCrawlersResponse
  property_count: 2
  slug: citevana-com-get-api-v1-tools-ai-crawlers-response
- name: GetSitesResponse
  property_count: 2
  slug: citevana-com-get-sites-response
- name: GetSitesSiteidAuditsLatestResponse
  property_count: 2
  slug: citevana-com-get-sites-siteid-audits-latest-response
- name: PostToolsAiCrawlersResponse
  property_count: 2
  slug: citevana-com-post-tools-ai-crawlers-response
- name: PostToolsLlmsTxtResponse
  property_count: 2
  slug: citevana-com-post-tools-llms-txt-response
- name: PostToolsPageAuditResponse
  property_count: 2
  slug: citevana-com-post-tools-page-audit-response
jsonld:
- class_count: 10
  name: Citevana Com Context
  property_count: 5
  slug: citevana-com-context
layout: provider
modified: '2026-11-03'
name: Citevana
nav: Providers
network: true
overview: 'Citevana is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, SEO, SearchVisibility, and Free Tools.


  The Citevana catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Citevana''s developer surface includes API reference, engineering blog, pricing, documentation, and 15 more developer resources.'
plans:
- name: Citevana Com Plans Pricing
  plan_count: 5
  slug: citevana-com-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Citevana API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: citevana-com-rules
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 22.6
    developer_ergonomics: 16.0
    discoverability: 53.6
    operational_transparency: 7.9
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
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Citevana Com Domain Security
  slug: citevana-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: list-sites
  slug: citevana-com-list-sites
slug: citevana-com
tags:
- Company
- Artificial Intelligence
- SEO
- SearchVisibility
- Free Tools
website: https://citevana.com/
---
