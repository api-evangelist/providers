---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Flyreel Agentic Access
  operation_count: 7
  slug: flyreel-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 2
apis:
- baseURL: https://connect.flyreel.co/v2
  baseurl_source: declared
  description: The Conversation API from Flyreel — 1 operation(s) for conversation.
  name: Flyreel Conversation API
  slug: flyreel-conversation-api
- baseURL: https://connect.flyreel.co/v2
  baseurl_source: declared
  description: The Inspection API from Flyreel — 2 operation(s) for inspection.
  name: Flyreel Inspection API
  slug: flyreel-inspection-api
- baseURL: https://connect.flyreel.co/v2
  baseurl_source: declared
  description: '{''$ref'': ''./descriptions/callback-url.md''}'
  name: Flyreel Webhook API
  slug: flyreel-webhook-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/flyreel/agentic-access/flyreel-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flyreel-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/flyreel/rules/flyreel-rules.yml
  title: ''
  type: Spectral
  url: rules/flyreel-rules.yml
- group: design
  href: https://artifacts.apis.io/flyreel/json-ld/flyreel-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/flyreel-context.jsonld
- group: design
  href: https://artifacts.apis.io/flyreel/vocabulary/flyreel-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/flyreel-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/flyreel/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/flyreel/data-model/flyreel-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flyreel-data-model.yml
- group: design
  href: https://artifacts.apis.io/flyreel/conformance/flyreel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flyreel-conformance.yml
- group: other
  href: https://artifacts.apis.io/flyreel/hosts/flyreel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flyreel-hosts.yml
- group: other
  href: https://artifacts.apis.io/flyreel/vendors/flyreel-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flyreel-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://risk.lexisnexis.com/-/media/files/insurance/tpu%20-%20total%20property%20understanding/nxr16067-00-0623_total_property_understanding_dal_08232023%20pdf.pdf
- group: other
  title: ''
  type: Leadership
  url: https://risk.lexisnexis.com/about-us/leadership
- group: auth
  href: https://artifacts.apis.io/flyreel/security/flyreel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flyreel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.flyreel.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flyreel.co/
- group: operate
  title: ''
  type: Support
  url: https://support.flyreel.co/
- group: company
  title: ''
  type: Blog
  url: https://risk.lexisnexis.com/insights-resources/blog-post
- group: commercial
  title: ''
  type: TermsOfService
  url: https://risk.lexisnexis.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://risk.lexisnexis.com/corporate/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.flyreel.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Flyreel
created: '2026-10-29'
description: Flyreel provides a cloud‑based risk assessment platform for insurance and property inspections. Its API enables developers to retrieve inspection data, submit inspection updates, and receive webhook notifications for events such as inspection creation or status changes. Integrated with LexisNexis Risk Solutions, Flyreel leverages extensive data sources to deliver accurate property risk insights for insurers, underwriters, and third‑party service providers.
image: https://risk.lexisnexis.com/-/media/files/insurance/tpu%20-%20total%20property%20understanding/picture4%20jpg.jpg
json_schemas:
- name: V2BaseInspection
  property_count: 38
  slug: flyreel-v2-base-inspection
- name: V2Conversation
  property_count: 12
  slug: flyreel-v2-conversation
- name: V2GetInspectionByIdResponseDto
  property_count: 52
  slug: flyreel-v2-get-inspection-by-id-response-dto
jsonld:
- class_count: 76
  name: Flyreel Context
  property_count: 390
  slug: flyreel-context
layout: provider
modified: '2026-10-29'
name: Flyreel
nav: Providers
network: true
overview: 'Flyreel publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Conversation API, Inspection API, and Webhook API. Tagged areas include Company, Insurance, Risk, API, and Data.


  The Flyreel catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Flyreel''s developer surface includes documentation, support, engineering blog, and 17 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Flyreel API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: flyreel-rules
scopes:
- name: Flyreel Scopes
  scope_count: 0
  slug: flyreel-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 63.6
    developer_ergonomics: 32.6
    discoverability: 69.6
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
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 31.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Flyreel Authentication
  slug: flyreel-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Flyreel Domain Security
  slug: flyreel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: inspection
  slug: flyreel-inspection-skill
slug: flyreel
tags:
- Company
- Insurance
- Risk
- API
- Data
- Analytics
website: https://www.flyreel.co/
---
