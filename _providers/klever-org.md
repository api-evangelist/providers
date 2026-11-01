---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Klever provides a REST API for blockchain data and transaction operations on the mainnet.
  name: Klever API
  slug: klever-api
- baseURL: https://multisign.mainnet.klever.org
  baseurl_source: declared
  description: 'klever-org API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: klever-org API
  slug: klever-org-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/klever-org/rules/klever-org-rules.yml
  title: ''
  type: Spectral
  url: rules/klever-org-rules.yml
- group: design
  href: https://artifacts.apis.io/klever-org/json-ld/klever-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/klever-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/klever-org/vocabulary/klever-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/klever-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/klever-org/data-model/klever-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/klever-org-data-model.yml
- group: design
  href: https://artifacts.apis.io/klever-org/conformance/klever-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/klever-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/klever-org/llms/klever-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/klever-org-llms.txt
- group: other
  href: https://artifacts.apis.io/klever-org/hosts/klever-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/klever-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/klever-org/vendors/klever-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/klever-org-vendors.yml
- group: build
  href: https://artifacts.apis.io/klever-org/packages/klever-org-packages.yml
  title: ''
  type: SDKs
  url: packages/klever-org-packages.yml
- group: build
  href: https://artifacts.apis.io/klever-org/packages/klever-org-packages.yml
  title: ''
  type: Packages
  url: packages/klever-org-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/discourse/discourse-mcp#quick-start-release
- group: auth
  href: https://artifacts.apis.io/klever-org/security/klever-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/klever-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://klever.org/
- group: company
  title: ''
  type: Blog
  url: https://klever.org/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.klever.org/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://klever.org/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://klever.org/terms-of-use/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.klever.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.klever.org/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.klever.org/
coverage:
  checked: '2026-10-31'
  detail: Public documentation references a REST API at https://api.mainnet.klever.org/v1.0/ but no OpenAPI or other machine‑readable contract is available.
  evidence:
  - status: 200
    url: https://forum.klever.org/c/kleverchain/developers/9
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Klever is a blockchain platform offering a high-performance virtual machine (KVM) for building lightning-fast decentralized applications. It provides staking, validator services, and developer tools, aiming to simplify smart contract execution with efficiency, security, and intuitiveness. The ecosystem includes a comprehensive documentation portal, community blog, and support desk.
image: https://klever.org/wp-content/uploads/2024/09/Primary.png
json_schemas:
- name: PostTransactionRequest
  property_count: 5
  slug: klever-org-post-transaction-request
jsonld:
- class_count: 1
  name: Klever Org Context
  property_count: 5
  slug: klever-org-context
layout: provider
modified: '2026-10-30'
name: klever-org
nav: Providers
network: true
overview: 'klever-org is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Crypto, Smart-Contracts, and Developer-Platform.


  The klever-org catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  klever-org''s developer surface includes getting-started guide, engineering blog, support, documentation, API reference, and 15 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 0
  name: Klever Org Rate Limits
  slug: klever-org-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: klever-org API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: klever-org-rules
scopes:
- name: Klever Org Scopes
  scope_count: 0
  slug: klever-org-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 68.1
    catalog_earned_first_party: 0.0
    catalog_gap: 46.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 79.1
    contract_quality: 42.6
    developer_ergonomics: 52.4
    discoverability: 66.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Klever Org Authentication
  slug: klever-org-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Klever Org Domain Security
  slug: klever-org-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: klever-org
tags:
- Company
- Blockchain
- Crypto
- Smart-Contracts
- Developer-Platform
website: https://klever.org/
---
