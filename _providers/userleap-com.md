---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Sprig API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Sprig API
  slug: userleap-com-api
artifact_total: 11
asyncapis:
- description: ''
  name: Userleap Com Webhooks
  slug: userleap-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/userleap-com/rules/userleap-com-rules.yml
  title: ''
  type: Spectral
  url: rules/userleap-com-rules.yml
- group: design
  href: https://artifacts.apis.io/userleap-com/json-ld/userleap-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/userleap-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/userleap-com/vocabulary/userleap-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/userleap-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/userleap-com/asyncapi/userleap-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/userleap-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/userleap-com/data-model/userleap-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/userleap-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/userleap-com/changelog/userleap-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/userleap-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/userleap-com/conformance/userleap-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/userleap-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/userleap-com/llms/userleap-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/userleap-com-llms.txt
- group: other
  href: https://artifacts.apis.io/userleap-com/a2a/userleap-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/userleap-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/userleap-com/well-known/userleap-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/userleap-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/userleap-com/hosts/userleap-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/userleap-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/userleap-com/vendors/userleap-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/userleap-com-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://sprig.com/integrations/webhooks
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sprig.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://sprig.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sprig.com/docs/welcome-to-sprig/quick-start-guide/index
- group: docs
  title: ''
  type: Documentation
  url: https://docs.userleap.com/
- group: auth
  href: https://artifacts.apis.io/userleap-com/security/userleap-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/userleap-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://userleap.com/
coverage:
  checked: '2026-10-21'
  detail: Sprig provides HTML documentation but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec was found.
  evidence:
  - status: 200
    url: https://sprig.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Sprig offers an enterprise survey platform that uses AI‑driven research agents to design, field, analyze, and synthesize studies. The service enables enterprise research teams to run adaptive surveys across email, panels, web apps, and mobile apps, delivering statistical analysis and report generation without manual configuration. Sprig’s agents support experience measurement, market and consumer insights, journey and behavioral research, and concept testing for product and market discovery.
image: https://cdn.prod.website-files.com/651206cc884d0caef0f4c520/69c2fd5f6882434c7781fd39_meta-img-new.png
json_schemas:
- name: GetV1ResponsesResponse
  property_count: 2
  slug: userleap-com-get-v1-responses-response
- name: GetV1ThemesResponse
  property_count: 14
  slug: userleap-com-get-v1-themes-response
- name: GetV2UsersUseridResponse
  property_count: 3
  slug: userleap-com-get-v2-users-userid-response
- name: PostV2PurgeVisitorsRequest
  property_count: 4
  slug: userleap-com-post-v2-purge-visitors-request
- name: PostV2UsersRequest
  property_count: 7
  slug: userleap-com-post-v2-users-request
- name: PostV2UsersResponse
  property_count: 4
  slug: userleap-com-post-v2-users-response
jsonld:
- class_count: 8
  name: Userleap Com Context
  property_count: 12
  slug: userleap-com-context
layout: provider
modified: '2026-10-21'
name: Sprig
nav: Providers
network: true
overview: 'Sprig is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Survey, Enterprise Research, AI Agents, Market Insights, and Customer Experience.


  The Sprig catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Sprig''s developer surface includes changelog, engineering blog, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Sprig API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: userleap-com-rules
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 19.7
    contract_quality: 32.4
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Userleap Com Domain Security
  slug: userleap-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: userleap-com
tags:
- Survey
- Enterprise Research
- AI Agents
- Market Insights
- Customer Experience
- Prototype Testing
- Omnichannel Distribution
website: http://userleap.com/
---
