---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/blockcypher/plans/blockcypher-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blockcypher-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/blockcypher/authentication/blockcypher-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blockcypher-authentication.yml
- group: design
  href: https://artifacts.apis.io/blockcypher/conformance/blockcypher-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blockcypher-conformance.yml
- group: other
  href: https://artifacts.apis.io/blockcypher/hosts/blockcypher-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blockcypher-hosts.yml
- group: other
  href: https://artifacts.apis.io/blockcypher/vendors/blockcypher-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blockcypher-vendors.yml
- group: build
  href: https://artifacts.apis.io/blockcypher/packages/blockcypher-packages.yml
  title: ''
  type: SDKs
  url: packages/blockcypher-packages.yml
- group: build
  href: https://artifacts.apis.io/blockcypher/packages/blockcypher-packages.yml
  title: ''
  type: Packages
  url: packages/blockcypher-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blockcypher.com/terms-of-service.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blockcypher.com/privacy-policy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blockcypher.com/pricing.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blockcypher
- group: company
  title: ''
  type: Blog
  url: https://blog.blockcypher.com
- group: start
  title: ''
  type: GettingStarted
  url: https://www.blockcypher.com/getting-started.html
- group: auth
  href: https://artifacts.apis.io/blockcypher/security/blockcypher-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blockcypher-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blockcypher.com
coverage:
  checked: '2026-10-22'
  detail: Documentation provides code examples but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://www.blockcypher.com/dev/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: 'BlockCypher is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by nea) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-22'
name: BlockCypher
nav: Providers
network: true
overview: 'BlockCypher is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include APIs, Blockchain, Infrastructure, and Enterprise.


  BlockCypher''s developer surface includes authentication, pricing, engineering blog, getting-started guide, and 11 more developer resources.'
plans:
- name: Blockcypher Plans Pricing
  plan_count: 3
  slug: blockcypher-plans-pricing
random_paper: 22
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 12.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 26.8
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blockcypher Authentication
  slug: blockcypher-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Blockcypher Domain Security
  slug: blockcypher-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blockcypher
tags:
- APIs
- Blockchain
- Infrastructure
- Enterprise
website: https://www.blockcypher.com
---
