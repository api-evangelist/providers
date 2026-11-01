---
agent_readiness:
  band: agent-aware
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 62
  human_in_the_loop: 0
  name: Promptzone Agentic Access
  operation_count: 142
  slug: promptzone-agentic-access
  summary_line: 142 operations · 62 acting
api_count: 1
apis:
- description: API for Promptzone services (details not publicly documented).
  name: Promptzone API
  slug: promptzone-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/promptzone/agentic-access/promptzone-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/promptzone-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/promptzone/rules/promptzone-rules.yml
  title: ''
  type: Spectral
  url: rules/promptzone-rules.yml
- group: design
  href: https://artifacts.apis.io/promptzone/json-ld/promptzone-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/promptzone-context.jsonld
- group: design
  href: https://artifacts.apis.io/promptzone/vocabulary/promptzone-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/promptzone-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/promptzone/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/promptzone/data-model/promptzone-data-model.yml
  title: ''
  type: DataModel
  url: data-model/promptzone-data-model.yml
- group: design
  href: https://artifacts.apis.io/promptzone/errors/promptzone-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/promptzone-problem-types.yml
- group: design
  href: https://artifacts.apis.io/promptzone/conformance/promptzone-conformance.yml
  title: ''
  type: Conformance
  url: conformance/promptzone-conformance.yml
- group: agent
  href: https://artifacts.apis.io/promptzone/llms/promptzone-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/promptzone-llms.txt
- group: agent
  href: https://artifacts.apis.io/promptzone/well-known/promptzone-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/promptzone-well-known.yml
- group: other
  href: https://artifacts.apis.io/promptzone/hosts/promptzone-hosts.yml
  title: ''
  type: Hosts
  url: hosts/promptzone-hosts.yml
- group: other
  href: https://artifacts.apis.io/promptzone/vendors/promptzone-vendors.yml
  title: ''
  type: Vendors
  url: vendors/promptzone-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.promptzone.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.promptzone.com/t/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.promptzone.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.promptzone.com/t/news
- group: auth
  href: https://artifacts.apis.io/promptzone/authentication/promptzone-authentication.yml
  title: ''
  type: Authentication
  url: authentication/promptzone-authentication.yml
- group: auth
  href: https://artifacts.apis.io/promptzone/security/promptzone-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/promptzone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://promptzone.com/
created: '2026-10-18'
description: PromptZone is a vibrant community dedicated to exploring the potential of AI and AI-generated prompts. Its mission is to foster discussions, share insights, and collaborate on projects that reveal how AI tools and technologies can shape our future. The platform offers AI prompts, guides, tools, a prompt library, research papers, and resources for builders, developers, and creators to innovate with artificial intelligence.
image: https://www.promptzone.com/logo.png
jsonld:
- class_count: 41
  name: Promptzone Context
  property_count: 155
  slug: promptzone-context
layout: provider
modified: '2026-10-18'
name: Promptzone
nav: Providers
network: true
overview: 'Promptzone publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Community, Prompts, Tools, and Resources.


  The Promptzone catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Promptzone''s developer surface includes support, authentication, and 17 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Promptzone API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: promptzone-rules
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 20.7
    developer_ergonomics: 18.5
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 33
    skills: derived
  regulatory:
    applies: true
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
  name: Promptzone Authentication
  slug: promptzone-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Promptzone Domain Security
  slug: promptzone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: promptzone-create-and-get-event
  slug: promptzone-create-and-get-event
- name: promptzone-create-segment-and-add-users
  slug: promptzone-create-segment-and-add-users
- name: promptzone-get-organization-details
  slug: promptzone-get-organization-details
- name: promptzone-invite-and-fetch-user
  slug: promptzone-invite-and-fetch-user
- name: promptzone-publish-article
  slug: promptzone-publish-article
slug: promptzone
tags:
- Artificial Intelligence
- Community
- Prompts
- Tools
- Resources
website: https://promptzone.com/
---
