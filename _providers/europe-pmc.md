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
    agentic_access: derived
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
  score: 19.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Europe Pmc Agentic Access
  operation_count: 2
  slug: europe-pmc-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- baseURL: https://dev.europepmc.org
  baseurl_source: declared
  description: Provides RESTful access to articles and grants.
  name: Europe PMC API
  slug: europe-pmc-api
- baseURL: https://dev.europepmc.org
  baseurl_source: declared
  description: The Europepmc API from Europe PMC — 2 operation(s) for europepmc.
  name: Europe PMC Europepmc API
  slug: europe-pmc-europepmc-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/europe-pmc/agentic-access/europe-pmc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/europe-pmc-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/europe-pmc/vocabulary/europe-pmc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/europe-pmc-vocabulary.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://europepmc.org/Roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://europepmc.org/PrivacyNotice
- group: start
  title: ''
  type: Login
  url: https://europepmc.org/accounts/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://europepmc.org/developers
- group: design
  href: https://artifacts.apis.io/europe-pmc/rules/europe-pmc-rules.yml
  title: ''
  type: Spectral
  url: rules/europe-pmc-rules.yml
- group: design
  href: https://artifacts.apis.io/europe-pmc/conformance/europe-pmc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/europe-pmc-conformance.yml
- group: agent
  href: https://artifacts.apis.io/europe-pmc/well-known/europe-pmc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/europe-pmc-well-known.yml
- group: other
  href: https://artifacts.apis.io/europe-pmc/hosts/europe-pmc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/europe-pmc-hosts.yml
- group: other
  href: https://artifacts.apis.io/europe-pmc/vendors/europe-pmc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/europe-pmc-vendors.yml
- group: build
  href: https://artifacts.apis.io/europe-pmc/packages/europe-pmc-packages.yml
  title: ''
  type: SDKs
  url: packages/europe-pmc-packages.yml
- group: build
  href: https://artifacts.apis.io/europe-pmc/packages/europe-pmc-packages.yml
  title: ''
  type: Packages
  url: packages/europe-pmc-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.europepmc.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EuropePMC
- group: auth
  href: https://artifacts.apis.io/europe-pmc/security/europe-pmc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/europe-pmc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://europepmc.org
created: '2026-10-13'
description: 'Europe PMC is a company surfaced via the API Evangelist harvest backlog (source: tag-qc) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-13'
name: Europe PMC
nav: Providers
network: true
overview: 'Europe PMC is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Europepmc API, and 1 more. Tagged areas include Company.


  The Europe PMC catalog on APIs.io includes 1 Spectral governance ruleset.


  Europe PMC''s developer surface includes documentation and 16 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 66
  extends:
  - spectral:oas
  name: Europe PMC API Rules
  rule_count: 25
  severity_counts:
    error: 23
    hint: 0
    info: 1
    warn: 1
  slug: europe-pmc-rules
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 30.8
    catalog_earned_first_party: 0.0
    catalog_gap: 69.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.1
  facets:
    access_clarity: 28.6
    contract_governance: 22.0
    contract_quality: 11.7
    developer_ergonomics: 21.4
    discoverability: 44.6
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 14.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/europe-pmc/europe-pmc-2026-11-03T131637.png
security:
- kind: domain-security
  name: Europe Pmc Domain Security
  slug: europe-pmc-domain-security
  summary_line: TLSv1.3
slug: europe-pmc
tags:
- Company
website: https://europepmc.org
---
