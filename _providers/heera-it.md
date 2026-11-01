---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Heera It Agentic Access
  operation_count: 4
  slug: heera-it-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://heera.it/wp-json
  baseurl_source: declared
  description: Read-only access to this site’s published content via the WordPress REST API.
  name: Sheikh Heera Content API
  slug: content-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/heera-it/llms/heera-it-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/heera-it-llms.txt
- group: agent
  href: https://artifacts.apis.io/heera-it/agentic-access/heera-it-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/heera-it-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/heera-it/rules/heera-it-rules.yml
  title: ''
  type: Spectral
  url: rules/heera-it-rules.yml
- group: design
  href: https://artifacts.apis.io/heera-it/json-ld/heera-it-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/heera-it-context.jsonld
- group: design
  href: https://artifacts.apis.io/heera-it/vocabulary/heera-it-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/heera-it-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/heera-it/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/heera-it/data-model/heera-it-data-model.yml
  title: ''
  type: DataModel
  url: data-model/heera-it-data-model.yml
- group: auth
  href: https://artifacts.apis.io/heera-it/security/heera-it-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/heera-it-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/heera-it/errors/heera-it-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/heera-it-problem-types.yml
- group: design
  href: https://artifacts.apis.io/heera-it/conformance/heera-it-conformance.yml
  title: ''
  type: Conformance
  url: conformance/heera-it-conformance.yml
- group: auth
  href: https://artifacts.apis.io/heera-it/well-known/heera-it-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/heera-it-security.txt
- group: agent
  href: https://artifacts.apis.io/heera-it/well-known/heera-it-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/heera-it-well-known.yml
- group: other
  href: https://artifacts.apis.io/heera-it/hosts/heera-it-hosts.yml
  title: ''
  type: Hosts
  url: hosts/heera-it-hosts.yml
- group: other
  href: https://artifacts.apis.io/heera-it/vendors/heera-it-vendors.yml
  title: ''
  type: Vendors
  url: vendors/heera-it-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://heera.it/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://heera.it/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/heera
- group: company
  title: ''
  type: Website
  url: https://heera.it/
- group: auth
  href: https://artifacts.apis.io/heera-it/security/heera-it-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/heera-it-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/heera-it/security/heera-it-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/heera-it-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://heera.it/blog
created: '2026-10-30'
description: Heera IT is the personal brand of Sheikh Heera, a software architect and CTO of Authlab, showcasing his expertise in software development, system architecture, and fragrance collecting. The site heera.it serves as a personal blog and portfolio, featuring articles on technology, programming, and personal interests, and provides contact information. While no formal company API is offered, the site highlights Heera's professional background and projects such as the Agentimus WordPress plugin.
image: https://heera.it/wp-content/uploads/2026/07/og-default.jpg
json_schemas:
- name: ContentItem
  property_count: 9
  slug: heera-it-content-item
jsonld:
- class_count: 2
  name: Heera It Context
  property_count: 12
  slug: heera-it-context
layout: provider
modified: '2026-10-30'
name: heera-it
nav: Providers
network: true
overview: 'heera-it is listed with 1 API on the [APIs.io](https://apis.io/) network: Sheikh Heera Content API. Tagged areas include Software Development, Personal Brand, Technology, Consulting, and Architecture.


  The heera-it catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  heera-it''s developer surface includes engineering blog and 20 more developer resources.'
plans:
- name: Heera It Plans Pricing
  plan_count: 0
  slug: heera-it-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: heera-it API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: heera-it-rules
scopes:
- name: Heera It Scopes
  scope_count: 0
  slug: heera-it-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 71.1
    catalog_earned_first_party: 0.0
    catalog_gap: 43.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 79.1
    contract_quality: 50.7
    developer_ergonomics: 8.8
    discoverability: 66.1
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Heera It Authentication
  slug: heera-it-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Heera It Domain Security
  slug: heera-it-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Heera It Vulnerability Disclosure
  slug: heera-it-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: content-api
  slug: heera-it-content-api
slug: heera-it
tags:
- Software Development
- Personal Brand
- Technology
- Consulting
- Architecture
website: https://heera.it/
---
