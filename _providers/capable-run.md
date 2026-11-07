---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documented at the Capable developer portal, providing access to CRM functionality.
  name: Capable CRM API
  slug: capable-crm-api
- description: 'Capable API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Capable API
  slug: capable-run-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/capable-run/plans/capable-run-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/capable-run-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/capable-run/rules/capable-run-rules.yml
  title: ''
  type: Spectral
  url: rules/capable-run-rules.yml
- group: design
  href: https://artifacts.apis.io/capable-run/json-ld/capable-run-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/capable-run-context.jsonld
- group: design
  href: https://artifacts.apis.io/capable-run/vocabulary/capable-run-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/capable-run-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/capable-run/data-model/capable-run-data-model.yml
  title: ''
  type: DataModel
  url: data-model/capable-run-data-model.yml
- group: design
  href: https://artifacts.apis.io/capable-run/conformance/capable-run-conformance.yml
  title: ''
  type: Conformance
  url: conformance/capable-run-conformance.yml
- group: agent
  href: https://artifacts.apis.io/capable-run/llms/capable-run-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/capable-run-llms.txt
- group: agent
  href: https://artifacts.apis.io/capable-run/well-known/capable-run-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/capable-run-well-known.yml
- group: other
  href: https://artifacts.apis.io/capable-run/hosts/capable-run-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capable-run-hosts.yml
- group: other
  href: https://artifacts.apis.io/capable-run/vendors/capable-run-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capable-run-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capable.run/legal/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://capable.run/legal/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capable.run/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://capable.run/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://crm.capable.run/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://crm.capable.run/guides/imap
- group: start
  title: ''
  type: DeveloperPortal
  url: https://crm.capable.run/developers
- group: auth
  href: https://artifacts.apis.io/capable-run/security/capable-run-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capable-run-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capable.run/
coverage:
  checked: '2026-11-04'
  detail: Developer portal pages render via JavaScript, providing no machine‑readable spec.
  evidence:
  - status: 200
    url: https://crm.capable.run/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Capable is an MCP‑native CRM that turns your calls, emails and meetings into CRM updates you approve, from inside Claude or ChatGPT, for founders and small B2B teams. It offers a pay‑per‑active‑account pricing model with no seats required, a 14‑day free trial, and integrates AI assistants to streamline sales pipelines. Founded in 2024 in Stockholm, Sweden, Capable aims to simplify customer relationship management for startups and growing businesses.
image: https://capable.run/og.png?v=9
json_schemas:
- name: PostApiCaptureV1Request
  property_count: 1
  slug: capable-run-post-api-capture-v1-request
- name: PostApiCaptureV1Response
  property_count: 1
  slug: capable-run-post-api-capture-v1-response
- name: PostApiMcpResponse
  property_count: 3
  slug: capable-run-post-api-mcp-response
jsonld:
- class_count: 3
  name: Capable Run Context
  property_count: 5
  slug: capable-run-context
layout: provider
modified: '2026-11-04'
name: Capable
nav: Providers
network: true
overview: 'Capable is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include CRM, Artificial Intelligence, MCP, Software-as-a-Service, and Sales.


  The Capable catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Capable''s developer surface includes pricing, getting-started guide, documentation, and 16 more developer resources.'
plans:
- name: Capable Run Plans Pricing
  plan_count: 2
  slug: capable-run-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: Capable API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: capable-run-rules
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 59.8
    catalog_earned_first_party: 8.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 20.4
    developer_ergonomics: 15.5
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Capable Run Domain Security
  slug: capable-run-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: capable-run
tags:
- CRM
- Artificial Intelligence
- MCP
- Software-as-a-Service
- Sales
website: https://capable.run/
---
