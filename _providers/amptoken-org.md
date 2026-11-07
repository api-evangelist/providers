---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.1
  scored_at: '2026-11-06'
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
- group: docs
  title: ''
  type: APIReference
  url: https://docs.amp.xyz/api-reference
- group: company
  title: ''
  type: Blog
  url: https://amptoken.substack.com
created: '2026-10-28'
description: AMP is a universal collateral token designed to facilitate fast and efficient transfers for any real-world application. It enables instant payments worldwide, guarantees value transfers, and offers a tokenized collateral solution for finance and blockchain use cases.
image: https://amp.xyz/images/amp-og.jpg
layout: provider
modified: '2026-10-28'
name: Amp
nav: Providers
network: true
overview: 'Amp is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Blockchain, Tokens, and Payments.


  The Amp catalog on APIs.io includes 1 Spectral governance ruleset.


  Amp''s developer surface includes documentation, API reference, engineering blog, and 10 more developer resources.'
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
  composite: 14.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 19.0
    discoverability: 64.3
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.6
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
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/amptoken-org/amptoken-org-2026-11-03T120826.png
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
- Tokens
- Payments
website: https://amp.xyz/
---
