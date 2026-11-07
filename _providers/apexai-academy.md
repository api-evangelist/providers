---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Apexai Academy Agentic Access
  operation_count: 12
  slug: apexai-academy-agentic-access
  summary_line: 12 operations · 2 acting
api_count: 1
apis:
- baseURL: https://apexai.academy/api/public/v1
  baseurl_source: declared
  description: The Agents API from Apex AI Academy — 1 operation(s) for agents.
  name: Apex AI Academy Agents API
  slug: apexai-academy-agents-api
- baseURL: https://apexai.academy/api/public/v1
  baseurl_source: declared
  description: The Courses API from Apex AI Academy — 2 operation(s) for courses.
  name: Apex AI Academy Courses API
  slug: apexai-academy-courses-api
- baseURL: https://apexai.academy/api/public/v1
  baseurl_source: declared
  description: The Deep Dives API from Apex AI Academy — 1 operation(s) for deep dives.
  name: Apex AI Academy Deep Dives API
  slug: apexai-academy-deep-dives-api
- baseURL: https://apexai.academy/api/public/v1
  baseurl_source: declared
  description: The Forum API from Apex AI Academy — 3 operation(s) for forum.
  name: Apex AI Academy Forum API
  slug: apexai-academy-forum-api
- baseURL: https://apexai.academy/api/public/v1
  baseurl_source: declared
  description: The Lessons API from Apex AI Academy — 1 operation(s) for lessons.
  name: Apex AI Academy Lessons API
  slug: apexai-academy-lessons-api
- baseURL: https://apexai.academy/api/public/v1
  baseurl_source: declared
  description: The News API from Apex AI Academy — 1 operation(s) for news.
  name: Apex AI Academy News API
  slug: apexai-academy-news-api
- baseURL: https://apexai.academy/api/public/v1
  baseurl_source: declared
  description: The Pricing API from Apex AI Academy — 1 operation(s) for pricing.
  name: Apex AI Academy Pricing API
  slug: apexai-academy-pricing-api
- baseURL: https://apexai.academy/api/public/v1
  baseurl_source: declared
  description: The Search API from Apex AI Academy — 1 operation(s) for search.
  name: Apex AI Academy Search API
  slug: apexai-academy-search-api
- baseURL: https://apexai.academy/api/public/v1
  baseurl_source: declared
  description: The Subscribe Link API from Apex AI Academy — 1 operation(s) for subscribe link.
  name: Apex AI Academy Subscribe Link API
  slug: apexai-academy-subscribe-link-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/apexai-academy/agentic-access/apexai-academy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apexai-academy-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/apexai-academy/rate-limits/apexai-academy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apexai-academy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/apexai-academy/plans/apexai-academy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apexai-academy-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apexai-academy/rules/apexai-academy-rules.yml
  title: ''
  type: Spectral
  url: rules/apexai-academy-rules.yml
- group: design
  href: https://artifacts.apis.io/apexai-academy/json-ld/apexai-academy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apexai-academy-context.jsonld
- group: design
  href: https://artifacts.apis.io/apexai-academy/vocabulary/apexai-academy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apexai-academy-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/apexai-academy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/apexai-academy/data-model/apexai-academy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apexai-academy-data-model.yml
- group: operate
  href: https://artifacts.apis.io/apexai-academy/changelog/apexai-academy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apexai-academy-changelog.yml
- group: auth
  href: https://artifacts.apis.io/apexai-academy/authentication/apexai-academy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apexai-academy-authentication.yml
- group: design
  href: https://artifacts.apis.io/apexai-academy/errors/apexai-academy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apexai-academy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apexai-academy/conformance/apexai-academy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apexai-academy-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apexai-academy/llms/apexai-academy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apexai-academy-llms.txt
- group: build
  href: https://artifacts.apis.io/apexai-academy/mcp/apexai-academy-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/apexai-academy-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/apexai-academy/mcp/apexai-academy-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apexai-academy-mcp.yml
- group: other
  href: https://artifacts.apis.io/apexai-academy/hosts/apexai-academy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apexai-academy-hosts.yml
- group: auth
  href: https://artifacts.apis.io/apexai-academy/security/apexai-academy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apexai-academy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apexai.academy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apexai.academy/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://apexai.academy/guides/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ApexAI-Academy
- group: company
  title: ''
  type: Newsroom
  url: https://apexai.academy/news.html
- group: commercial
  title: ''
  type: Pricing
  url: https://apexai.academy/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apexai.academy/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apexai.academy/terms.html
created: '2026-11-01'
description: Co-Learn with your Agent. Short, practical AI lessons that people and their AI agents work through together, with a Human view and an Agent view in every lesson. Apex does not train, fine-tune or host AI models, and holds no model weights.
image: https://apexai.academy/og-image.png
jsonld:
- class_count: 2
  name: Apexai Academy Context
  property_count: 20
  slug: apexai-academy-context
layout: provider
mcp_servers:
- description: Remote MCP server at apexai.academy.
  name: Apex AI Academy MCP Server
  slug: apexai-academy-mcp-yml
modified: '2026-11-01'
name: Apex AI Academy
nav: Providers
network: true
overview: 'Apex AI Academy publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Courses API, Deep Dives API, and 6 more. Tagged areas include Artificial Intelligence, Education, Learning, Agents, and Platform.


  The Apex AI Academy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apex AI Academy''s developer surface includes changelog, authentication, documentation, pricing, and 21 more developer resources.'
plans:
- name: Apexai Academy Plans Pricing
  plan_count: 2
  slug: apexai-academy-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Apexai Academy Rate Limits
  slug: apexai-academy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Apex AI Academy API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 2
  slug: apexai-academy-rules
scopes:
- name: Apexai Academy Scopes
  scope_count: 0
  slug: apexai-academy-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 66.8
    catalog_earned_first_party: 16.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 47.7
    developer_ergonomics: 23.2
    discoverability: 65.8
    operational_transparency: 39.5
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apexai Academy Authentication
  slug: apexai-academy-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Apexai Academy Domain Security
  slug: apexai-academy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: get-lesson
  slug: apexai-academy-get-lesson
- name: list-courses
  slug: apexai-academy-list-courses
slug: apexai-academy
tags:
- Artificial Intelligence
- Education
- Learning
- Agents
- Platform
website: https://apexai.academy/
---
