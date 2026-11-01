---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Actablesite Com Agentic Access
  operation_count: 3
  slug: actablesite-com-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- baseURL: https://actablesite.com
  baseurl_source: declared
  description: The Ai Crawler Check API from actablesite-com — 1 operation(s) for ai crawler check.
  name: actablesite-com Ai Crawler Check API
  slug: actablesite-com-ai-crawler-check-api
- baseURL: https://actablesite.com
  baseurl_source: declared
  description: The Audit API from actablesite-com — 1 operation(s) for audit.
  name: actablesite-com Audit API
  slug: actablesite-com-audit-api
- baseURL: https://actablesite.com
  baseurl_source: declared
  description: The Health API from actablesite-com — 1 operation(s) for health.
  name: actablesite-com Health API
  slug: actablesite-com-health-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/actablesite-com/vocabulary/actablesite-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/actablesite-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/actablesite-com/data-model/actablesite-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/actablesite-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/actablesite-com/agentic-access/actablesite-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/actablesite-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/actablesite-com/rules/actablesite-com-rules.yml
  title: ''
  type: Spectral
  url: rules/actablesite-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/actablesite-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/actablesite-com/errors/actablesite-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/actablesite-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/actablesite-com/conformance/actablesite-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/actablesite-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/actablesite-com/llms/actablesite-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/actablesite-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/actablesite-com/well-known/actablesite-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/actablesite-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/actablesite-com/hosts/actablesite-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/actablesite-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/actablesite-com/vendors/actablesite-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/actablesite-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/actablesite-com/security/actablesite-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/actablesite-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://actablesite.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://actablesite.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://actablesite.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unitedideas
created: '2026-10-29'
description: ActableSite.com provides a platform for creating and managing interactive, data‑driven web experiences. It offers tools for building dynamic sites, integrating APIs, and customizing user interfaces without extensive coding. The service targets developers, marketers, and businesses seeking rapid deployment of feature‑rich web applications, with support for analytics, SEO, and third‑party integrations. ActableSite emphasizes scalability, security, and performance, delivering a robust solution for modern digital presence.
image: https://actablesite.com/og.png
json_schemas:
- name: AuditResponse
  property_count: 0
  slug: actablesite-com-audit-response
- name: HealthResponse
  property_count: 0
  slug: actablesite-com-health-response
- name: WebsiteRequest
  property_count: 0
  slug: actablesite-com-website-request
layout: provider
modified: '2026-10-29'
name: actablesite-com
nav: Providers
network: true
overview: 'actablesite-com publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Ai Crawler Check API, Audit API, and Health API. Tagged areas include Company, WebPlatform, LowCode, Analytics, and SEO.


  The actablesite-com catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: actablesite-com API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: actablesite-com-rules
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 48.2
    developer_ergonomics: 6.4
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Actablesite Com Domain Security
  slug: actablesite-com-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: actablesite-com-main
  slug: actablesite-com-main
slug: actablesite-com
tags:
- Company
- WebPlatform
- LowCode
- Analytics
- SEO
website: https://actablesite.com/
---
