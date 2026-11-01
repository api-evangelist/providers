---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://services.wolfram.com
  baseurl_source: declared
  description: 'Wolfram Research API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: Wolfram Research API
  slug: wolfram-api
artifact_total: 10
common:
- group: other
  href: https://artifacts.apis.io/wolfram/vendors/wolfram-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wolfram-vendors.yml
- group: build
  href: https://artifacts.apis.io/wolfram/packages/wolfram-packages.yml
  title: ''
  type: SDKs
  url: packages/wolfram-packages.yml
- group: build
  href: https://artifacts.apis.io/wolfram/packages/wolfram-packages.yml
  title: ''
  type: Packages
  url: packages/wolfram-packages.yml
- group: commercial
  href: https://artifacts.apis.io/wolfram/plans/wolfram-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wolfram-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/wolfram/rules/wolfram-rules.yml
  title: ''
  type: Spectral
  url: rules/wolfram-rules.yml
- group: design
  href: https://artifacts.apis.io/wolfram/json-ld/wolfram-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/wolfram-context.jsonld
- group: design
  href: https://artifacts.apis.io/wolfram/vocabulary/wolfram-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wolfram-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/wolfram/data-model/wolfram-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wolfram-data-model.yml
- group: design
  href: https://artifacts.apis.io/wolfram/conformance/wolfram-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wolfram-conformance.yml
- group: agent
  href: https://artifacts.apis.io/wolfram/llms/wolfram-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wolfram-llms.txt
- group: other
  href: https://artifacts.apis.io/wolfram/hosts/wolfram-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wolfram-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.wolfram.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.wolfram.com/faculty/register.cgi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WolframResearch
- group: company
  title: ''
  type: Blog
  url: https://blog.wolfram.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://reference.wolfram.com/language/guide/WolframSystemSetup.html
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wolfram.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.wolframalpha.com/
- group: auth
  href: https://artifacts.apis.io/wolfram/security/wolfram-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wolfram-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wolfram.com/
coverage:
  checked: '2026-10-21'
  detail: Wolfram developer docs are served as JavaScript-rendered pages with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.wolfram.com/developer/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Wolfram Research develops computational technologies including the Wolfram Language, Mathematica, and Wolfram|Alpha. It provides cloud services, APIs, and developer tools that enable complex calculations, data analysis, and knowledge-based applications across scientific, engineering, and business domains. The company also offers consulting and education resources to empower users in leveraging computational intelligence.
image: https://files.wolframcdn.com/pub/www.wolfram.com/home/img/hero/hero-background.webp
json_schemas:
- name: PostApiAgentOneV1ChatCompletionsRequest
  property_count: 1
  slug: wolfram-post-api-agent-one-v1-chat-completions-request
- name: PostApiCagV1WolframalphacontextRequest
  property_count: 1
  slug: wolfram-post-api-cag-v1-wolframalphacontext-request
- name: PostApiCagV1WolframlanguagecomputeRequest
  property_count: 1
  slug: wolfram-post-api-cag-v1-wolframlanguagecompute-request
- name: PostApiCagV1WolframlanguagecomputeResponse
  property_count: 4
  slug: wolfram-post-api-cag-v1-wolframlanguagecompute-response
- name: PostApiCagV1WolframlanguagehintsRequest
  property_count: 1
  slug: wolfram-post-api-cag-v1-wolframlanguagehints-request
jsonld:
- class_count: 5
  name: Wolfram Context
  property_count: 6
  slug: wolfram-context
layout: provider
modified: '2026-10-21'
name: Wolfram Research
nav: Providers
network: true
overview: 'Wolfram Research is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Computational, Mathematics, and Cloud.


  The Wolfram Research catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Wolfram Research''s developer surface includes support, signup flow, engineering blog, getting-started guide, documentation, and 15 more developer resources.'
plans:
- name: Wolfram Plans Pricing
  plan_count: 8
  slug: wolfram-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Wolfram Research API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: wolfram-rules
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 35.6
    contract_quality: 24.1
    developer_ergonomics: 45.2
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Wolfram Domain Security
  slug: wolfram-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wolfram
tags:
- Company
- Computational
- Mathematics
- Cloud
website: https://wolfram.com/
---
