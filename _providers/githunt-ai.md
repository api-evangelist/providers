---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Githunt Ai Agentic Access
  operation_count: 11
  slug: githunt-ai-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.githunt.ai
  baseurl_source: declared
  description: The Briefs API from githunt-ai — 2 operation(s) for briefs.
  name: githunt-ai Briefs API
  slug: githunt-ai-briefs-api
- baseURL: https://api.githunt.ai
  baseurl_source: declared
  description: The Lists API from githunt-ai — 3 operation(s) for lists.
  name: githunt-ai Lists API
  slug: githunt-ai-lists-api
- baseURL: https://api.githunt.ai
  baseurl_source: declared
  description: The Profile API from githunt-ai — 1 operation(s) for profile.
  name: githunt-ai Profile API
  slug: githunt-ai-profile-api
- baseURL: https://api.githunt.ai
  baseurl_source: declared
  description: The Search API from githunt-ai — 1 operation(s) for search.
  name: githunt-ai Search API
  slug: githunt-ai-search-api
- baseURL: https://api.githunt.ai
  baseurl_source: declared
  description: The Users API from githunt-ai — 2 operation(s) for users.
  name: githunt-ai Users API
  slug: githunt-ai-users-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/githunt-ai/agentic-access/githunt-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/githunt-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/githunt-ai/rules/githunt-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/githunt-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/githunt-ai/json-ld/githunt-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/githunt-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/githunt-ai/vocabulary/githunt-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/githunt-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/githunt-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/githunt-ai/data-model/githunt-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/githunt-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/githunt-ai/conventions/githunt-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/githunt-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/githunt-ai/authentication/githunt-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/githunt-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/githunt-ai/errors/githunt-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/githunt-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/githunt-ai/conformance/githunt-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/githunt-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/githunt-ai/llms/githunt-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/githunt-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/githunt-ai/hosts/githunt-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/githunt-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/githunt-ai/vendors/githunt-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/githunt-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://githunt.ai/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.githunt.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.githunt.ai/api-docs
- group: auth
  href: https://artifacts.apis.io/githunt-ai/security/githunt-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/githunt-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://githunt.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://githunt.ai/api-docs
- group: company
  title: ''
  type: Blog
  url: https://githunt.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://githunt.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://githunt.ai/terms
created: '2026-10-30'
description: GitHunt AI is a platform that leverages AI to help companies find hidden developer talent on GitHub. By scanning over 100 million profiles in under five minutes, it matches developers to job requirements using stack‑matched criteria and natural‑language queries. Users can search via a web UI or integrate with AI assistants like Claude and ChatGPT to retrieve shortlists of top‑tier engineers across roles such as full‑stack, backend, frontend, DevOps, and mobile development. The service also offers hiring pages, talent reports, and a developer portal for API access.
image: https://githunt.ai/githunt-og-image.png
json_schemas:
- name: BriefRequest
  property_count: 3
  slug: githunt-ai-brief-request
- name: BriefStatusResponse
  property_count: 3
  slug: githunt-ai-brief-status-response
- name: ProfileAnalyzeResponse
  property_count: 2
  slug: githunt-ai-profile-analyze-response
- name: SearchRequest
  property_count: 21
  slug: githunt-ai-search-request
- name: SearchResponse
  property_count: 3
  slug: githunt-ai-search-response
- name: UserResponse
  property_count: 2
  slug: githunt-ai-user-response
jsonld:
- class_count: 32
  name: Githunt Ai Context
  property_count: 146
  slug: githunt-ai-context
layout: provider
modified: '2026-10-30'
name: githunt-ai
nav: Providers
network: true
overview: 'githunt-ai publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Briefs API, Lists API, Profile API, and 2 more. Tagged areas include Company, AI, Talent, Recruitment, and Developer.


  The githunt-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  githunt-ai''s developer surface includes authentication, getting-started guide, documentation, engineering blog, and 18 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: githunt-ai API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: githunt-ai-rules
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 77.7
    catalog_earned_first_party: 0.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 79.1
    contract_quality: 61.7
    developer_ergonomics: 51.7
    discoverability: 66.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Githunt Ai Authentication
  slug: githunt-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Githunt Ai Domain Security
  slug: githunt-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: search-developers
  slug: githunt-ai-search-developers
slug: githunt-ai
tags:
- Company
- AI
- Talent
- Recruitment
- Developer
website: https://githunt.ai/
---
