---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Unified API to access bank account data across European banks under PSD2. Docs at the developer portal provide usage details but no machine‑readable contract was found.
  name: Open Banking API
  slug: open-banking-api-2
- description: 'Tatic API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Tatic API
  slug: open-banking-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/open-banking/plans/open-banking-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/open-banking-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/open-banking/rules/open-banking-rules.yml
  title: ''
  type: Spectral
  url: rules/open-banking-rules.yml
- group: design
  href: https://artifacts.apis.io/open-banking/vocabulary/open-banking-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/open-banking-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/open-banking/cli/open-banking-cli.yml
  title: ''
  type: CLI
  url: cli/open-banking-cli.yml
- group: design
  href: https://artifacts.apis.io/open-banking/conformance/open-banking-conformance.yml
  title: ''
  type: Conformance
  url: conformance/open-banking-conformance.yml
- group: auth
  href: https://artifacts.apis.io/open-banking/well-known/open-banking-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/open-banking-security.txt
- group: agent
  href: https://artifacts.apis.io/open-banking/well-known/open-banking-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/open-banking-well-known.yml
- group: other
  href: https://artifacts.apis.io/open-banking/hosts/open-banking-hosts.yml
  title: ''
  type: Hosts
  url: hosts/open-banking-hosts.yml
- group: other
  href: https://artifacts.apis.io/open-banking/vendors/open-banking-vendors.yml
  title: ''
  type: Vendors
  url: vendors/open-banking-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://open-banking.io/en/security
- group: company
  title: ''
  type: Blog
  url: https://open-banking.io/en/blog
- group: auth
  href: https://artifacts.apis.io/open-banking/security/open-banking-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/open-banking-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/open-banking/security/open-banking-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/open-banking-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://open-banking.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open-banking.io/en/developers
- group: docs
  title: ''
  type: Documentation
  url: https://open-banking.io/en
- group: start
  title: ''
  type: GettingStarted
  url: https://open-banking.io/en
- group: commercial
  title: ''
  type: Pricing
  url: https://open-banking.io/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://open-banking.io/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://open-banking.io/en/privacy
coverage:
  checked: '2026-10-18'
  detail: The developer portal provides documentation but no OpenAPI or other machine‑readable contract was discovered.
  evidence:
  - status: 200
    url: https://open-banking.io/en/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Tatic ApS operates the open-banking.io platform, providing a unified API to access bank account data across European banks under PSD2 regulations. Users can sign up, connect their banks via secure OAuth flows, and retrieve account balances, transactions, and metadata without needing individual bank integrations. The service offers SDKs in multiple languages, a CLI, and transparent pricing, targeting developers, fintechs, and businesses seeking streamlined financial data access.
image: https://open-banking.io/og-image.png
layout: provider
modified: '2026-10-18'
name: Tatic
nav: Providers
network: true
overview: 'Tatic is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Tatic catalog on APIs.io includes 1 Spectral governance ruleset.


  Tatic''s developer surface includes CLI, engineering blog, documentation, getting-started guide, pricing, and 15 more developer resources.'
plans:
- name: Open Banking Plans Pricing
  plan_count: 2
  slug: open-banking-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Tatic API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: open-banking-rules
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 40.8
    catalog_earned_first_party: 8.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 35.6
    contract_quality: 10.5
    developer_ergonomics: 40.5
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Open Banking Domain Security
  slug: open-banking-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Open Banking Vulnerability Disclosure
  slug: open-banking-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: open-banking
tags:
- Company
website: https://open-banking.io/
---
