---
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Alyawmgold Agentic Access
  operation_count: 3
  slug: alyawmgold-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Open gold and silver spot references, supported markets, and USD history.
  name: AlyawmGold Public API
  slug: alyawmgold-public-api
artifact_total: 5
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alyawmgold/refs/heads/main/agentic-access/alyawmgold-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/alyawmgold-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alyawmgold/refs/heads/main/rules/alyawmgold-rules.yml
  title: ''
  type: Spectral
  url: rules/alyawmgold-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alyawmgold/refs/heads/main/json-ld/alyawmgold-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/alyawmgold-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alyawmgold/refs/heads/main/vocabulary/alyawmgold-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/alyawmgold-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alyawmgold/refs/heads/main/data-model/alyawmgold-data-model.yml
  title: ''
  type: DataModel
  url: data-model/alyawmgold-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alyawmgold/refs/heads/main/errors/alyawmgold-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alyawmgold-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alyawmgold/refs/heads/main/conformance/alyawmgold-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alyawmgold-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alyawmgold/refs/heads/main/hosts/alyawmgold-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alyawmgold-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alyawmgold/refs/heads/main/vendors/alyawmgold-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alyawmgold-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alyawmgold.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alyawmgold.com/legal/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://alyawmgold.com/developers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alyawmgold
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alyawmgold/refs/heads/main/security/alyawmgold-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alyawmgold-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alyawmgold.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://alyawmgold.com/
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: AlyawmGold Public API provides real‑time gold and silver price data for the United Arab Emirates and surrounding markets. The service offers up‑to‑date pricing in multiple currencies, historical price charts, and conversion tools. It targets developers building financial, e‑commerce, and market‑analysis applications who need reliable precious‑metal pricing information. The platform supports multilingual interfaces and offers APIs for price retrieval, historical data queries, and custom calculations, ensuring seamless integration into diverse software ecosystems.
image: https://alyawmgold.com/social/alyawmgold-gold-prices-og.png
jsonld:
- class_count: 1
  name: Alyawmgold Context
  property_count: 5
  slug: alyawmgold-context
layout: provider
modified: '2026-09-27'
name: AlyawmGold Public API
nav: Providers
network: true
overview: 'AlyawmGold Public API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gold, Prices, and Finance.


  The AlyawmGold Public API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AlyawmGold Public API''s developer surface includes API reference and 14 more developer resources.'
random_paper: 17
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: AlyawmGold Public API API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: alyawmgold-rules
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 6.7
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alyawmgold Domain Security
  slug: alyawmgold-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alyawmgold
tags:
- Company
- Gold
- Prices
- Finance
website: https://alyawmgold.com/
---
