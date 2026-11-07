---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Datavessel provides an e‑commerce MCP server connecting AI agents to shop platforms. Documentation is available at the docs site, but the reference is a JavaScript‑rendered SPA with no machine‑readabl
  name: Datavessel API
  slug: datavessel-api
- baseURL: https://api.datavessel.io
  baseurl_source: declared
  description: 'datavessel API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: datavessel API
  slug: datavessel-io-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/datavessel-io/plans/datavessel-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datavessel-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/datavessel-io/rules/datavessel-io-rules.yml
  title: ''
  type: Spectral
  url: rules/datavessel-io-rules.yml
- group: design
  href: https://artifacts.apis.io/datavessel-io/json-ld/datavessel-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datavessel-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/datavessel-io/vocabulary/datavessel-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datavessel-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/datavessel-io/data-model/datavessel-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datavessel-io-data-model.yml
- group: build
  href: https://artifacts.apis.io/datavessel-io/cli/datavessel-io-cli.yml
  title: ''
  type: CLI
  url: cli/datavessel-io-cli.yml
- group: design
  href: https://artifacts.apis.io/datavessel-io/conformance/datavessel-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datavessel-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datavessel-io/llms/datavessel-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datavessel-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/datavessel-io/well-known/datavessel-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datavessel-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/datavessel-io/hosts/datavessel-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datavessel-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/datavessel-io/vendors/datavessel-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datavessel-io-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.datavessel.io/signup
- group: auth
  title: ''
  type: Security
  url: https://datavessel.io/security
- group: auth
  href: https://artifacts.apis.io/datavessel-io/security/datavessel-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/datavessel-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/datavessel-io/security/datavessel-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datavessel-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datavessel.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.datavessel.io
- group: docs
  title: ''
  type: Documentation
  url: https://datavessel.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://datavessel.io/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://datavessel.io/about
- group: operate
  title: ''
  type: Support
  url: https://datavessel.io/contact
- group: company
  title: ''
  type: Blog
  url: https://blog.datavessel.io
- group: commercial
  title: ''
  type: Pricing
  url: https://datavessel.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datavessel.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datavessel.io/privacy-and-policy
coverage:
  checked: '2026-11-05'
  detail: Documentation is a JavaScript‑rendered SPA with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://datavessel.io/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: Datavessel provides an e‑commerce MCP server that connects AI agents such as Claude, ChatGPT, Codex, and n8n to shop platforms, merchant centers, and advertising services. It offers typed, validated tools for feeds, ads, and store data, with free reads and a limited number of free writes per month. The platform supports integrations with Shopify, WooCommerce, Shopware, Amazon, Google Ads, Analytics, and more, aiming to automate and augment e‑commerce operations through AI‑driven agents.
json_schemas:
- name: PostV1ProvidersExecuteRequest
  property_count: 2
  slug: datavessel-io-post-v1-providers-execute-request
jsonld:
- class_count: 1
  name: Datavessel Io Context
  property_count: 2
  slug: datavessel-io-context
layout: provider
modified: '2026-11-05'
name: datavessel
nav: Providers
network: true
overview: 'datavessel is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Artificial Intelligence, Automation, Integration, and MCP.


  The datavessel catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  datavessel''s developer surface includes CLI, signup flow, documentation, API reference, getting-started guide, support, engineering blog, and 18 more developer resources.'
plans:
- name: Datavessel Io Plans Pricing
  plan_count: 4
  slug: datavessel-io-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: datavessel API Rules
  rule_count: 39
  severity_counts:
    error: 36
    hint: 0
    info: 2
    warn: 1
  slug: datavessel-io-rules
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 58.2
    catalog_earned_first_party: 12.0
    catalog_gap: 56.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 19.0
    developer_ergonomics: 52.4
    discoverability: 53.6
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datavessel Io Domain Security
  slug: datavessel-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Datavessel Io Vulnerability Disclosure
  slug: datavessel-io-vulnerability-disclosure
  summary_line: no policy recorded
slug: datavessel-io
tags:
- E-Commerce
- Artificial Intelligence
- Automation
- Integration
- MCP
website: https://datavessel.io/
---
