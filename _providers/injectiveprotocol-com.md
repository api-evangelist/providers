---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Injective provides blockchain and DeFi functionality via its platform. Documentation is available at https://docs.injective.network/. No machine‑readable API contract was found.
  name: Injective API
  slug: injective-api
- baseURL: https://sentry.lcd.injective.network
  baseurl_source: declared
  description: 'Injective API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Injective API
  slug: injectiveprotocol-com-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/injectiveprotocol-com/rules/injectiveprotocol-com-rules.yml
  title: ''
  type: Spectral
  url: rules/injectiveprotocol-com-rules.yml
- group: design
  href: https://artifacts.apis.io/injectiveprotocol-com/json-ld/injectiveprotocol-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/injectiveprotocol-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/injectiveprotocol-com/vocabulary/injectiveprotocol-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/injectiveprotocol-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/injectiveprotocol-com/data-model/injectiveprotocol-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/injectiveprotocol-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/injectiveprotocol-com/cli/injectiveprotocol-com-cli.yml
  title: ''
  type: CLI
  url: cli/injectiveprotocol-com-cli.yml
- group: design
  href: https://artifacts.apis.io/injectiveprotocol-com/conformance/injectiveprotocol-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/injectiveprotocol-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/injectiveprotocol-com/llms/injectiveprotocol-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/injectiveprotocol-com-llms.txt
- group: other
  href: https://artifacts.apis.io/injectiveprotocol-com/a2a/injectiveprotocol-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/injectiveprotocol-com-a2a.yml
- group: other
  href: https://artifacts.apis.io/injectiveprotocol-com/hosts/injectiveprotocol-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/injectiveprotocol-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/injectiveprotocol-com/vendors/injectiveprotocol-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/injectiveprotocol-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/injectiveprotocol-com/packages/injectiveprotocol-com-packages.yml
  title: ''
  type: SDKs
  url: packages/injectiveprotocol-com-packages.yml
- group: build
  href: https://artifacts.apis.io/injectiveprotocol-com/packages/injectiveprotocol-com-packages.yml
  title: ''
  type: Packages
  url: packages/injectiveprotocol-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://injective.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://injective.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://injective.com/press
- group: auth
  href: https://artifacts.apis.io/injectiveprotocol-com/security/injectiveprotocol-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/injectiveprotocol-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://injective.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.injective.network/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://injective.com/dev
- group: docs
  title: ''
  type: APIReference
  url: https://docs.injective.network/
- group: start
  title: ''
  type: GettingStarted
  url: https://injective.com/dev
- group: company
  title: ''
  type: Blog
  url: https://injective.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InjectiveLabs
coverage:
  checked: '2026-10-30'
  detail: Docs site renders via Mintlify SPA, no machine‑readable OpenAPI spec found.
  evidence:
  - status: 200
    url: https://docs.injective.network/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Injective is a high-performance, interoperable layer‑one blockchain infrastructure built for finance. It enables developers, institutions, and AI agents to trade, tokenize, and transact at scale with embedded financial primitives such as stablecoins, derivatives, and real‑world assets. The platform offers extensive developer tools, SDKs, and APIs for building DeFi applications, market making, and automated trading strategies.
image: https://willing-flame-a009dd7c0a.media.strapiapp.com/homepage_247c60c04e.webp
json_schemas:
- name: GetPerpsResponse
  property_count: 1
  slug: injectiveprotocol-com-get-perps-response
- name: GetStatusSyncResponse
  property_count: 1
  slug: injectiveprotocol-com-get-status-sync-response
jsonld:
- class_count: 2
  name: Injectiveprotocol Com Context
  property_count: 1
  slug: injectiveprotocol-com-context
layout: provider
modified: '2026-10-28'
name: Injective
nav: Providers
network: true
overview: 'Injective is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Finance, DeFi, Infrastructure, and Web3.


  The Injective catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Injective''s developer surface includes CLI, documentation, API reference, getting-started guide, engineering blog, and 18 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Injective API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: injectiveprotocol-com-rules
score:
  band: thin
  composite: 30.0
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
    contract_quality: 20.2
    developer_ergonomics: 54.8
    discoverability: 58.9
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
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
  name: Injectiveprotocol Com Domain Security
  slug: injectiveprotocol-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: injectiveprotocol-com
tags:
- Blockchain
- Finance
- DeFi
- Infrastructure
- Web3
website: https://injective.com/
---
