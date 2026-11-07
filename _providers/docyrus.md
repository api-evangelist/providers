---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Docyrus low-code platform
  name: Docyrus API
  slug: docyrus-api-2
- description: 'Docyrus, Inc. API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Docyrus, Inc. API
  slug: docyrus-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/docyrus/plans/docyrus-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docyrus-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/docyrus/rules/docyrus-rules.yml
  title: ''
  type: Spectral
  url: rules/docyrus-rules.yml
- group: design
  href: https://artifacts.apis.io/docyrus/json-ld/docyrus-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/docyrus-context.jsonld
- group: design
  href: https://artifacts.apis.io/docyrus/vocabulary/docyrus-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/docyrus-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/docyrus/data-model/docyrus-data-model.yml
  title: ''
  type: DataModel
  url: data-model/docyrus-data-model.yml
- group: build
  href: https://artifacts.apis.io/docyrus/cli/docyrus-cli.yml
  title: ''
  type: CLI
  url: cli/docyrus-cli.yml
- group: design
  href: https://artifacts.apis.io/docyrus/conformance/docyrus-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docyrus-conformance.yml
- group: agent
  href: https://artifacts.apis.io/docyrus/llms/docyrus-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docyrus-llms.txt
- group: agent
  href: https://artifacts.apis.io/docyrus/well-known/docyrus-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docyrus-well-known.yml
- group: other
  href: https://artifacts.apis.io/docyrus/hosts/docyrus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docyrus-hosts.yml
- group: other
  href: https://artifacts.apis.io/docyrus/vendors/docyrus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docyrus-vendors.yml
- group: build
  href: https://artifacts.apis.io/docyrus/packages/docyrus-packages.yml
  title: ''
  type: SDKs
  url: packages/docyrus-packages.yml
- group: build
  href: https://artifacts.apis.io/docyrus/packages/docyrus-packages.yml
  title: ''
  type: Packages
  url: packages/docyrus-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docyrus.com/platform/developers/
- group: auth
  href: https://artifacts.apis.io/docyrus/security/docyrus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docyrus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docyrus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docyrus.com/platform/developers/api/
- group: docs
  title: ''
  type: APIReference
  url: https://docyrus.com/platform/developers/api/
- group: operate
  title: ''
  type: Support
  url: https://docyrus.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://docyrus.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Docyrus
- group: commercial
  title: ''
  type: Pricing
  url: https://docyrus.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://docyrus.app/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docyrus.com/terms-of-services/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docyrus.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/docyrus/workspace
coverage:
  checked: '2026-10-20'
  detail: Developer API page loads a JavaScript SPA and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docyrus.com/platform/developers/api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: Docyrus, Inc. provides an AI-native low-code platform enabling teams to build web, mobile, and agent applications without extensive coding. It offers AI-driven builders for web apps, agents, mobile apps, and portals, along with a desktop app, CLI, and Chrome extension. The platform includes workflow automation, data infrastructure, security governance, and integration connectors, targeting enterprises and developers seeking rapid, scalable solutions.
image: https://docyrus.com/images/og/v1/home.png
json_schemas:
- name: GetV1DsProjectsRec9381Response
  property_count: 6
  slug: docyrus-get-v1-ds-projects-rec9381-response
jsonld:
- class_count: 1
  name: Docyrus Context
  property_count: 6
  slug: docyrus-context
layout: provider
modified: '2026-10-20'
name: Docyrus, Inc.
nav: Providers
network: true
overview: 'Docyrus, Inc. is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Low-Code, Platform, Automation, and Enterprise.


  The Docyrus, Inc. catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Docyrus, Inc.''s developer surface includes CLI, documentation, API reference, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
plans:
- name: Docyrus Plans Pricing
  plan_count: 5
  slug: docyrus-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Docyrus, Inc. API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: docyrus-rules
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 16.4
    developer_ergonomics: 33.3
    discoverability: 64.3
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 41.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/docyrus/docyrus-2026-11-03T130910.png
security:
- kind: domain-security
  name: Docyrus Domain Security
  slug: docyrus-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: docyrus
tags:
- Artificial Intelligence
- Low-Code
- Platform
- Automation
- Enterprise
website: https://docyrus.com/
---
