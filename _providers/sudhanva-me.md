---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Sudhanva Me Agentic Access
  operation_count: 4
  slug: sudhanva-me-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: Public API providing access to Sudhanva Narayana's profile, writings, and batch insight jobs.
  name: Sudhanva Public API
  slug: sudhanva-public-api
- baseURL: https://sudhanva.me/api/v1
  baseurl_source: declared
  description: Find the API contract and the available resources.
  name: sudhanva-me Discovery API
  slug: sudhanva-me-discovery-api
- baseURL: https://sudhanva.me/api/v1
  baseurl_source: declared
  description: Read metadata for published writing.
  name: sudhanva-me Posts API
  slug: sudhanva-me-posts-api
- baseURL: https://sudhanva.me/api/v1
  baseurl_source: declared
  description: Read Sudhanva Narayana's published professional profile.
  name: sudhanva-me Profile API
  slug: sudhanva-me-profile-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/sudhanva-me/data-model/sudhanva-me-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sudhanva-me-data-model.yml
- group: agent
  href: https://artifacts.apis.io/sudhanva-me/agentic-access/sudhanva-me-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sudhanva-me-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/sudhanva-me/rules/sudhanva-me-rules.yml
  title: ''
  type: Spectral
  url: rules/sudhanva-me-rules.yml
- group: design
  href: https://artifacts.apis.io/sudhanva-me/vocabulary/sudhanva-me-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sudhanva-me-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/sudhanva-me/cli/sudhanva-me-cli.yml
  title: ''
  type: CLI
  url: cli/sudhanva-me-cli.yml
- group: design
  href: https://artifacts.apis.io/sudhanva-me/lifecycle/sudhanva-me-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sudhanva-me-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sudhanva-me/errors/sudhanva-me-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sudhanva-me-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sudhanva-me/conformance/sudhanva-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sudhanva-me-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sudhanva-me/llms/sudhanva-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sudhanva-me-llms.txt
- group: other
  href: https://artifacts.apis.io/sudhanva-me/a2a/sudhanva-me-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/sudhanva-me-a2a.yml
- group: auth
  href: https://artifacts.apis.io/sudhanva-me/well-known/sudhanva-me-crates-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sudhanva-me-crates-security.txt
- group: agent
  href: https://artifacts.apis.io/sudhanva-me/well-known/sudhanva-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sudhanva-me-well-known.yml
- group: other
  href: https://artifacts.apis.io/sudhanva-me/hosts/sudhanva-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sudhanva-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/sudhanva-me/vendors/sudhanva-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sudhanva-me-vendors.yml
- group: build
  href: https://artifacts.apis.io/sudhanva-me/packages/sudhanva-me-packages.yml
  title: ''
  type: SDKs
  url: packages/sudhanva-me-packages.yml
- group: build
  href: https://artifacts.apis.io/sudhanva-me/packages/sudhanva-me-packages.yml
  title: ''
  type: Packages
  url: packages/sudhanva-me-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nsudhanva
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sudhanva.me/developers/
- group: auth
  href: https://artifacts.apis.io/sudhanva-me/security/sudhanva-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sudhanva-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sudhanva.me/
- group: docs
  title: ''
  type: Documentation
  url: https://sudhanva.me/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://sudhanva.me/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://sudhanva.me/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sudhanva.me/privacy/
- group: operate
  title: ''
  type: Support
  url: https://sudhanva.me/contact/
created: '2026-10-30'
description: Sudhanva Narayana is a senior machine learning engineer based in the San Francisco Bay Area. His personal site sudhanva.me showcases his professional profile, engineering blog, and a public API that provides read‑only access to his published writings, project case studies, and profile‑insight batch jobs. The site offers documentation, a blog, and privacy information, reflecting his expertise in production ML systems, model serving, and cloud‑native AI platforms.
image: https://sudhanva.me/og-default.png
layout: provider
modified: '2026-10-30'
name: sudhanva-me
nav: Providers
network: true
overview: 'sudhanva-me publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Discovery API, Posts API, Profile API, and 1 more. Tagged areas include Machine Learning, Engineering, Personal Site, San Francisco, and AI.


  The sudhanva-me catalog on APIs.io includes 1 Spectral governance ruleset.


  sudhanva-me''s developer surface includes CLI, documentation, API reference, engineering blog, support, and 20 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: sudhanva-me API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: sudhanva-me-rules
scopes:
- name: Sudhanva Me Scopes
  scope_count: 0
  slug: sudhanva-me-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 47.1
    developer_ergonomics: 47.6
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sudhanva Me Authentication
  slug: sudhanva-me-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sudhanva Me Domain Security
  slug: sudhanva-me-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sudhanva-me
tags:
- Machine Learning
- Engineering
- Personal Site
- San Francisco
- AI
website: https://sudhanva.me/
---
