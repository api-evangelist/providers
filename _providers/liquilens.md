---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Liquilens Agentic Access
  operation_count: 14
  slug: liquilens-agentic-access
  summary_line: 14 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.seiche.info/openbb
  baseurl_source: declared
  description: The Agent Query API from LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs — 1 operation(s) for agent query.
  name: LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs Agent Query API
  slug: liquilens-agent-query-api
- baseURL: https://api.seiche.info/openbb
  baseurl_source: declared
  description: The Agent Review API from LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs — 1 operation(s) for agent review.
  name: LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs Agent Review API
  slug: liquilens-agent-review-api
- baseURL: https://api.seiche.info/openbb
  baseurl_source: declared
  description: The Applications API from LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs — 2 operation(s) for applications.
  name: LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs Applications API
  slug: liquilens-applications-api
- baseURL: https://api.seiche.info/openbb
  baseurl_source: declared
  description: The Datasets API from LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs — 1 operation(s) for datasets.
  name: LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs Datasets API
  slug: liquilens-datasets-api
- baseURL: https://api.seiche.info/openbb
  baseurl_source: declared
  description: The Financial Evidence For OpenBB API from LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs — 1 operation(s) for financial evidence for openbb.
  name: LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs Financial Evidence For OpenBB API
  slug: liquilens-financial-evidence-for-openbb-api
- baseURL: https://api.seiche.info/openbb
  baseurl_source: declared
  description: The Funding Review API from LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs — 1 operation(s) for funding review.
  name: LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs Funding Review API
  slug: liquilens-funding-review-api
- baseURL: https://api.seiche.info/openbb
  baseurl_source: declared
  description: The Funding Review.csv API from LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs — 1 operation(s) for funding review.csv.
  name: LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs Funding Review.csv API
  slug: liquilens-funding-review-csv-api
- baseURL: https://api.seiche.info/openbb
  baseurl_source: declared
  description: The Guide API from LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs — 1 operation(s) for guide.
  name: LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs Guide API
  slug: liquilens-guide-api
- baseURL: https://api.seiche.info/openbb
  baseurl_source: declared
  description: The Healthz API from LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs — 1 operation(s) for healthz.
  name: LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs Healthz API
  slug: liquilens-healthz-api
- baseURL: https://api.seiche.info/openbb
  baseurl_source: declared
  description: The Packet API from LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs — 1 operation(s) for packet.
  name: LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs Packet API
  slug: liquilens-packet-api
- baseURL: https://api.seiche.info/openbb
  baseurl_source: declared
  description: The Query API from LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs — 1 operation(s) for query.
  name: LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs Query API
  slug: liquilens-query-api
- baseURL: https://api.seiche.info/openbb
  baseurl_source: declared
  description: The Release API from LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs — 1 operation(s) for release.
  name: LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs Release API
  slug: liquilens-release-api
- baseURL: https://api.seiche.info/openbb
  baseurl_source: declared
  description: The Sources API from LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs — 1 operation(s) for sources.
  name: LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs Sources API
  slug: liquilens-sources-api
artifact_total: 19
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/liquilens/refs/heads/main/llms/liquilens-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/liquilens-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/liquilens/refs/heads/main/well-known/liquilens-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/liquilens-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/liquilens/refs/heads/main/agentic-access/liquilens-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/liquilens-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/liquilens/refs/heads/main/rules/liquilens-rules.yml
  title: ''
  type: Spectral
  url: rules/liquilens-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/liquilens/refs/heads/main/json-ld/liquilens-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/liquilens-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/liquilens/refs/heads/main/vocabulary/liquilens-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/liquilens-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/liquilens/refs/heads/main/data-model/liquilens-data-model.yml
  title: ''
  type: DataModel
  url: data-model/liquilens-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/liquilens/refs/heads/main/errors/liquilens-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/liquilens-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/liquilens/refs/heads/main/conformance/liquilens-conformance.yml
  title: ''
  type: Conformance
  url: conformance/liquilens-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/liquilens/refs/heads/main/well-known/liquilens-liquilens-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/liquilens-liquilens-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/liquilens/refs/heads/main/well-known/liquilens-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/liquilens-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/liquilens/refs/heads/main/hosts/liquilens-hosts.yml
  title: ''
  type: Hosts
  url: hosts/liquilens-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/liquilens/refs/heads/main/vendors/liquilens-vendors.yml
  title: ''
  type: Vendors
  url: vendors/liquilens-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/liquilens/refs/heads/main/packages/liquilens-packages.yml
  title: ''
  type: SDKs
  url: packages/liquilens-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/liquilens/refs/heads/main/packages/liquilens-packages.yml
  title: ''
  type: Packages
  url: packages/liquilens-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://liquilens.in/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.liquilens.in/
- group: auth
  title: ''
  type: Security
  url: https://liquilens.in/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://liquilens.in/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://api.liquilens.in/api/public-signals/news
- group: docs
  title: ''
  type: APIReference
  url: https://liquilens.in/developers/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/liquilens/refs/heads/main/security/liquilens-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/liquilens-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/liquilens/refs/heads/main/security/liquilens-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/liquilens-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://liquilens.in/
- group: docs
  title: ''
  type: Documentation
  url: https://beepboop2025.github.io/financial-evidence-skills/api/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://api.liquilens.in/mcp
  - status: 401
    url: https://demo.liquilens.in/mcp
  - status: 200
    url: https://liquilens.in/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: LiquiLens Private Limited provides a financial research API platform that aggregates bank evidence, funding data, market liquidity, and source availability across multiple datasets. The service offers public read access without API keys, delivering up to five rows per example query for quick inspection. It integrates with tools like Postman, Bruno, and Insomnia, and supports data export via OpenAPI 3.1. Updated October 2026, LiquiLens aims to facilitate transparent financial data research and analysis.
image: https://liquilens.in/share.png?v=b4962f8b5a592bb2
json_schemas:
- name: QueryResult
  property_count: 16
  slug: liquilens-query-result
jsonld:
- class_count: 4
  name: Liquilens Context
  property_count: 40
  slug: liquilens-context
layout: provider
modified: '2026-10-08'
name: LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs
nav: Providers
network: true
overview: 'LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Query API, Agent Review API, Applications API, and 10 more. Tagged areas include Company, Finance, Research, and Data.


  The LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs'' developer surface includes API reference, documentation, and 23 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: LIQUILENS PRIVATE LIMITED -- LiquiLens financial research APIs API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: liquilens-rules
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 51.2
    catalog_earned_first_party: 0.0
    catalog_gap: 63.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 47.9
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Liquilens Domain Security
  slug: liquilens-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Liquilens Vulnerability Disclosure
  slug: liquilens-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: liquilens
tags:
- Company
- Finance
- Research
- Data
website: https://liquilens.in/
---
