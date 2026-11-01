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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.8
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API reference for Amp token platform.
  name: Amp API
  slug: amp-api
- description: 'Amp API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Amp API
  slug: amptoken-org-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/amptoken-org/rules/amptoken-org-rules.yml
  title: ''
  type: Spectral
  url: rules/amptoken-org-rules.yml
- group: design
  href: https://artifacts.apis.io/amptoken-org/vocabulary/amptoken-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/amptoken-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/amptoken-org/conformance/amptoken-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amptoken-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/amptoken-org/llms/amptoken-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amptoken-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/amptoken-org/well-known/amptoken-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amptoken-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/amptoken-org/hosts/amptoken-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amptoken-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/amptoken-org/vendors/amptoken-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amptoken-org-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amptoken
- group: auth
  href: https://artifacts.apis.io/amptoken-org/security/amptoken-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amptoken-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amp.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.amp.xyz/
created: '2026-10-28'
description: AMP is a universal collateral token designed to facilitate fast and efficient transfers for any real-world application. It enables instant payments worldwide, guarantees value transfers, and offers a tokenized collateral solution for finance and blockchain use cases.
image: https://amp.xyz/images/amp-og.jpg
layout: provider
modified: '2026-10-28'
name: Amp
nav: Providers
network: true
overview: 'Amp is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Blockchain, Token, and Payments.


  The Amp catalog on APIs.io includes 1 Spectral governance ruleset.


  Amp''s developer surface includes documentation and 10 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Amp API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: amptoken-org-rules
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amptoken Org Domain Security
  slug: amptoken-org-domain-security
  summary_line: TLSv1.3 · HSTS
slug: amptoken-org
tags:
- Company
- Finance
- Blockchain
- Token
- Payments
website: https://amp.xyz/
---
