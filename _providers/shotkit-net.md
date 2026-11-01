---
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'shotkit-net API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: shotkit-net API
  slug: shotkit-net-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/shotkit-net/plans/shotkit-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shotkit-net-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/shotkit-net/rules/shotkit-net-rules.yml
  title: ''
  type: Spectral
  url: rules/shotkit-net-rules.yml
- group: design
  href: https://artifacts.apis.io/shotkit-net/json-ld/shotkit-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/shotkit-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/shotkit-net/vocabulary/shotkit-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shotkit-net-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/shotkit-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/shotkit-net/data-model/shotkit-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shotkit-net-data-model.yml
- group: auth
  href: https://artifacts.apis.io/shotkit-net/authentication/shotkit-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shotkit-net-authentication.yml
- group: design
  href: https://artifacts.apis.io/shotkit-net/conformance/shotkit-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shotkit-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/shotkit-net/llms/shotkit-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shotkit-net-llms.txt
- group: other
  href: https://artifacts.apis.io/shotkit-net/hosts/shotkit-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shotkit-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/shotkit-net/vendors/shotkit-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shotkit-net-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://shotkit.net/playground
- group: start
  title: ''
  type: Login
  url: https://shotkit.net/login
- group: auth
  href: https://artifacts.apis.io/shotkit-net/security/shotkit-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shotkit-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shotkit.net/
- group: docs
  title: ''
  type: Documentation
  url: https://shotkit.net/docs
- group: docs
  title: ''
  type: APIReference
  url: https://shotkit.net/api/take
- group: start
  title: ''
  type: GettingStarted
  url: https://shotkit.net/docs/quickstart
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shotkit.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shotkit.net/privacy
- group: operate
  title: ''
  type: Contact
  url: https://shotkit.net/contact
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are served as a JavaScript single-page app, preventing machine-readable extraction.
  evidence:
  - status: 200
    url: https://shotkit.net/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: Shotkit provides a Web Screenshot API that allows developers and agents to capture pixel-perfect screenshots of any webpage, HTML, or Markdown with a single HTTP request. Features include full-page, retina, and mobile rendering, automatic removal of cookie banners and ads, and output formats such as PNG, PDF, video, or Markdown. The service offers a free tier with no credit card required, and supports multiple programming languages. It is designed for use cases like website thumbnails, visual regression testing, and website change monitoring.
image: https://shotkit.net/opengraph-image?ad1df63c33987af4
json_schemas:
- name: PostApiTakeRequest
  property_count: 2
  slug: shotkit-net-post-api-take-request
jsonld:
- class_count: 1
  name: Shotkit Net Context
  property_count: 2
  slug: shotkit-net-context
layout: provider
modified: '2026-10-31'
name: shotkit-net
nav: Providers
network: true
overview: 'shotkit-net is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Screenshot, API, Web, and Automation.


  The shotkit-net catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  shotkit-net''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, and 16 more developer resources.'
plans:
- name: Shotkit Net Plans Pricing
  plan_count: 4
  slug: shotkit-net-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: shotkit-net API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: shotkit-net-rules
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 73.9
    catalog_earned_first_party: 0.0
    catalog_gap: 41.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 62.6
    contract_governance: 79.1
    contract_quality: 45.0
    developer_ergonomics: 54.0
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Shotkit Net Authentication
  slug: shotkit-net-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Shotkit Net Domain Security
  slug: shotkit-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shotkit-net
tags:
- Company
- Screenshot
- API
- Web
- Automation
website: https://shotkit.net/
---
