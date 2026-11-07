---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Enterprise Wikimedia Com Agentic Access
  operation_count: 79
  slug: enterprise-wikimedia-com-agentic-access
  summary_line: 79 operations · 7 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.enterprise.wikimedia.com
  baseurl_source: declared
  description: On-demand article lookup.
  name: Wikimedia Enterprise Articles API
  slug: enterprise-wikimedia-com-articles-api
- baseURL: https://api.enterprise.wikimedia.com
  baseurl_source: declared
  description: Login, token refresh/revoke, and password management. Tokens are JWTs.
  name: Wikimedia Enterprise Authentication API
  slug: enterprise-wikimedia-com-authentication-api
- baseURL: https://api.enterprise.wikimedia.com
  baseurl_source: declared
  description: Hourly batch files of project updates (Realtime Batch).
  name: Wikimedia Enterprise Batches API
  slug: enterprise-wikimedia-com-batches-api
- baseURL: https://api.enterprise.wikimedia.com
  baseurl_source: declared
  description: Project code metadata.
  name: Wikimedia Enterprise Codes API
  slug: enterprise-wikimedia-com-codes-api
- baseURL: https://api.enterprise.wikimedia.com
  baseurl_source: declared
  description: Language metadata.
  name: Wikimedia Enterprise Languages API
  slug: enterprise-wikimedia-com-languages-api
- baseURL: https://api.enterprise.wikimedia.com
  baseurl_source: declared
  description: Namespace metadata.
  name: Wikimedia Enterprise Namespaces API
  slug: enterprise-wikimedia-com-namespaces-api
- baseURL: https://api.enterprise.wikimedia.com
  baseurl_source: declared
  description: Project metadata.
  name: Wikimedia Enterprise Projects API
  slug: enterprise-wikimedia-com-projects-api
- baseURL: https://api.enterprise.wikimedia.com
  baseurl_source: declared
  description: Streaming article updates over SSE / NDJSON.
  name: Wikimedia Enterprise Realtime Articles API
  slug: enterprise-wikimedia-com-realtime-articles-api
- baseURL: https://api.enterprise.wikimedia.com
  baseurl_source: declared
  description: Streaming Wikidata updates over SSE / NDJSON (Beta).
  name: Wikimedia Enterprise Realtime Wikidata API
  slug: enterprise-wikimedia-com-realtime-wikidata-api
- baseURL: https://api.enterprise.wikimedia.com
  baseurl_source: declared
  description: Bulk project snapshots (compressed NDJSON) and chunked downloads.
  name: Wikimedia Enterprise Snapshots API
  slug: enterprise-wikimedia-com-snapshots-api
- baseURL: https://api.enterprise.wikimedia.com
  baseurl_source: declared
  description: On-demand Structured Contents article lookup (Beta).
  name: Wikimedia Enterprise Structured Contents API
  slug: enterprise-wikimedia-com-structured-contents-api
- baseURL: https://api.enterprise.wikimedia.com
  baseurl_source: declared
  description: Structured Contents snapshots (Beta).
  name: Wikimedia Enterprise Structured Snapshots API
  slug: enterprise-wikimedia-com-structured-snapshots-api
- baseURL: https://api.enterprise.wikimedia.com
  baseurl_source: declared
  description: On-demand Wikidata item, property, and label lookup (Beta).
  name: Wikimedia Enterprise Wikidata API
  slug: enterprise-wikimedia-com-wikidata-api
- baseURL: https://api.enterprise.wikimedia.com
  baseurl_source: declared
  description: Hourly batch files of Wikidata item and property updates (Realtime Batch, Beta).
  name: Wikimedia Enterprise Wikidata Batches API
  slug: enterprise-wikimedia-com-wikidata-batches-api
- baseURL: https://api.enterprise.wikimedia.com
  baseurl_source: declared
  description: Wikidata snapshots (items and properties) and chunked downloads (Beta).
  name: Wikimedia Enterprise Wikidata Snapshots API
  slug: enterprise-wikimedia-com-wikidata-snapshots-api
artifact_total: 31
common:
- group: agent
  href: https://artifacts.apis.io/enterprise-wikimedia-com/agentic-access/enterprise-wikimedia-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/enterprise-wikimedia-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/enterprise-wikimedia-com/plans/enterprise-wikimedia-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/enterprise-wikimedia-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/enterprise-wikimedia-com/rules/enterprise-wikimedia-com-rules.yml
  title: ''
  type: Spectral
  url: rules/enterprise-wikimedia-com-rules.yml
- group: design
  href: https://artifacts.apis.io/enterprise-wikimedia-com/json-ld/enterprise-wikimedia-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/enterprise-wikimedia-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/enterprise-wikimedia-com/vocabulary/enterprise-wikimedia-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/enterprise-wikimedia-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/enterprise-wikimedia-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/enterprise-wikimedia-com/data-model/enterprise-wikimedia-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/enterprise-wikimedia-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/enterprise-wikimedia-com/changelog/enterprise-wikimedia-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/enterprise-wikimedia-com-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://www.mediawiki.org/wiki/Reporting_security_bugs
- group: auth
  href: https://artifacts.apis.io/enterprise-wikimedia-com/authentication/enterprise-wikimedia-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/enterprise-wikimedia-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/enterprise-wikimedia-com/errors/enterprise-wikimedia-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/enterprise-wikimedia-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/enterprise-wikimedia-com/conformance/enterprise-wikimedia-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/enterprise-wikimedia-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/enterprise-wikimedia-com/llms/enterprise-wikimedia-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/enterprise-wikimedia-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/enterprise-wikimedia-com/well-known/enterprise-wikimedia-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/enterprise-wikimedia-com-security.txt
- group: agent
  href: https://artifacts.apis.io/enterprise-wikimedia-com/well-known/enterprise-wikimedia-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/enterprise-wikimedia-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/enterprise-wikimedia-com/hosts/enterprise-wikimedia-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/enterprise-wikimedia-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/enterprise-wikimedia-com/vendors/enterprise-wikimedia-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/enterprise-wikimedia-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://enterprise.wikimedia.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://enterprise.wikimedia.com/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://enterprise.wikimedia.com/blog/releases/
- group: company
  title: ''
  type: Blog
  url: https://enterprise.wikimedia.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.enterprise.wikimedia.com/signup/?utm_source=website&utm_medium=cta&utm_campaign=signup&utm_content=docs-start
- group: commercial
  title: ''
  type: Pricing
  url: https://enterprise.wikimedia.com/pricing.md
- group: start
  title: ''
  type: GettingStarted
  url: https://enterprise.wikimedia.com/docs/agents
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.enterprise.wikimedia.com</span
- group: auth
  href: https://artifacts.apis.io/enterprise-wikimedia-com/security/enterprise-wikimedia-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/enterprise-wikimedia-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/enterprise-wikimedia-com/security/enterprise-wikimedia-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/enterprise-wikimedia-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://enterprise.wikimedia.com
- group: docs
  title: ''
  type: Documentation
  url: https://enterprise.wikimedia.com/docs/
created: '2026-11-04'
description: Wikimedia Enterprise is a product of the Wikimedia Foundation that provides enterprise‑grade APIs for Wikipedia, Wikidata and all Wikimedia projects. It offers structured content snapshots, real‑time data streams, and on‑demand article retrieval, enabling developers, researchers and companies to build AI, search and data‑science applications at scale while supporting the sustainability of free knowledge.
image: https://enterprise.wikimedia.com/_astro/social-default.d0U8cLPp.png
json_schemas:
- name: article
  property_count: 24
  slug: enterprise-wikimedia-com-article
- name: batch
  property_count: 8
  slug: enterprise-wikimedia-com-batch
- name: RealtimeArticle
  property_count: 24
  slug: enterprise-wikimedia-com-realtime-article
- name: snapshot
  property_count: 9
  slug: enterprise-wikimedia-com-snapshot
- name: structured_content
  property_count: 20
  slug: enterprise-wikimedia-com-structured-content
- name: wikidata_article
  property_count: 16
  slug: enterprise-wikimedia-com-wikidata-article
jsonld:
- class_count: 41
  name: Enterprise Wikimedia Com Context
  property_count: 95
  slug: enterprise-wikimedia-com-context
layout: provider
modified: '2026-11-04'
name: Wikimedia Enterprise
nav: Providers
network: true
overview: 'Wikimedia Enterprise publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Articles API, Authentication API, Batches API, and 12 more. Tagged areas include Company, Data, Enterprise, and Wikimedia.


  The Wikimedia Enterprise catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Wikimedia Enterprise''s developer surface includes changelog, authentication, engineering blog, signup flow, pricing, getting-started guide, documentation, and 22 more developer resources.'
plans:
- name: Enterprise Wikimedia Com Plans Pricing
  plan_count: 2
  slug: enterprise-wikimedia-com-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 115
  extends:
  - spectral:oas
  name: Wikimedia Enterprise API Rules
  rule_count: 74
  severity_counts:
    error: 61
    hint: 0
    info: 1
    warn: 12
  slug: enterprise-wikimedia-com-rules
score:
  band: strong
  composite: 55.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 68.7
    developer_ergonomics: 47.0
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
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
  name: Enterprise Wikimedia Com Authentication
  slug: enterprise-wikimedia-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Enterprise Wikimedia Com Domain Security
  slug: enterprise-wikimedia-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Enterprise Wikimedia Com Vulnerability Disclosure
  slug: enterprise-wikimedia-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: enterprise-wikimedia-com-article-lookup
  slug: enterprise-wikimedia-com-article-lookup
- name: enterprise-wikimedia-com-projects-retrieve
  slug: enterprise-wikimedia-com-projects-retrieve
- name: enterprise-wikimedia-com-structured-contents-lookup
  slug: enterprise-wikimedia-com-structured-contents-lookup
slug: enterprise-wikimedia-com
tags:
- Company
- Data
- Enterprise
- Wikimedia
website: https://enterprise.wikimedia.com
---
