---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 37
  human_in_the_loop: 0
  name: Filen Agentic Access
  operation_count: 58
  slug: filen-agentic-access
  summary_line: 58 operations · 37 acting
api_count: 2
apis:
- baseURL: https://gateway.filen.io/v3
  baseurl_source: declared
  description: The Health API from Filen — 1 operation(s) for health.
  name: Filen Health API
  slug: filen-health-api
- baseURL: https://gateway.filen.io/v3
  baseurl_source: declared
  description: The Items API from Filen — 3 operation(s) for items.
  name: Filen Items API
  slug: filen-items-api
- baseURL: https://gateway.filen.io/v3
  baseurl_source: declared
  description: 'The Items: Directories API from Filen — 15 operation(s) for items: directories.'
  name: 'Filen Items: Directories API'
  slug: filen-items-directories-api
- baseURL: https://gateway.filen.io/v3
  baseurl_source: declared
  description: 'The Items: Files API from Filen — 9 operation(s) for items: files.'
  name: 'Filen Items: Files API'
  slug: filen-items-files-api
- baseURL: https://gateway.filen.io/v3
  baseurl_source: declared
  description: The Public Links API from Filen — 15 operation(s) for public links.
  name: Filen Public Links API
  slug: filen-public-links-api
- baseURL: https://gateway.filen.io/v3
  baseurl_source: declared
  description: The Shared API from Filen — 8 operation(s) for shared.
  name: Filen Shared API
  slug: filen-shared-api
- baseURL: https://gateway.filen.io/v3
  baseurl_source: declared
  description: The User API from Filen — 7 operation(s) for user.
  name: Filen User API
  slug: filen-user-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/filen/agentic-access/filen-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/filen-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/filen/plans/filen-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/filen-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/filen/rules/filen-rules.yml
  title: ''
  type: Spectral
  url: rules/filen-rules.yml
- group: design
  href: https://artifacts.apis.io/filen/json-ld/filen-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/filen-context.jsonld
- group: design
  href: https://artifacts.apis.io/filen/vocabulary/filen-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/filen-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/filen/data-model/filen-data-model.yml
  title: ''
  type: DataModel
  url: data-model/filen-data-model.yml
- group: build
  href: https://artifacts.apis.io/filen/cli/filen-cli.yml
  title: ''
  type: CLI
  url: cli/filen-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://filen.io/security
- group: auth
  href: https://artifacts.apis.io/filen/authentication/filen-authentication.yml
  title: ''
  type: Authentication
  url: authentication/filen-authentication.yml
- group: design
  href: https://artifacts.apis.io/filen/conformance/filen-conformance.yml
  title: ''
  type: Conformance
  url: conformance/filen-conformance.yml
- group: other
  href: https://artifacts.apis.io/filen/hosts/filen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/filen-hosts.yml
- group: other
  href: https://artifacts.apis.io/filen/vendors/filen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/filen-vendors.yml
- group: build
  href: https://artifacts.apis.io/filen/packages/filen-packages.yml
  title: ''
  type: SDKs
  url: packages/filen-packages.yml
- group: build
  href: https://artifacts.apis.io/filen/packages/filen-packages.yml
  title: ''
  type: Packages
  url: packages/filen-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://filen.io/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FilenCloudDienste
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.filen.io/docs/desktop/setup
- group: auth
  href: https://artifacts.apis.io/filen/security/filen-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/filen-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/filen/security/filen-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/filen-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/filen/security/filen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/filen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://filen.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.filen.io
- group: commercial
  title: ''
  type: Pricing
  url: https://filen.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://filen.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://filen.io/privacy
- group: operate
  title: ''
  type: Support
  url: https://filen.io/hub
created: '2026-10-28'
description: Filen provides next‑generation end‑to‑end encrypted cloud storage, offering zero‑knowledge security for individuals and teams. Its platform includes web, desktop, mobile, and CLI clients, a network drive feature, and a focus on privacy, transparency, and open‑source tools. Users can store, sync, and share files securely without the provider ever accessing the data.
image: https://filen.io/og.png
json_schemas:
- name: response
  property_count: 3
  slug: filen-response
jsonld:
- class_count: 1
  name: Filen Context
  property_count: 3
  slug: filen-context
layout: provider
modified: '2026-10-28'
name: Filen
nav: Providers
network: true
overview: 'Filen publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Health API, Items API, Items: Directories API, and 4 more. Tagged areas include Company, Cloud Storage, Encryption, Zero Knowledge, and File Sync.


  The Filen catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Filen''s developer surface includes CLI, authentication, getting-started guide, documentation, pricing, support, and 20 more developer resources.'
plans:
- name: Filen Plans Pricing
  plan_count: 4
  slug: filen-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Filen Rate Limits
  slug: filen-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Filen API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 3
  slug: filen-rules
scopes:
- name: Filen Scopes
  scope_count: 0
  slug: filen-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 65.2
    catalog_earned_first_party: 12.0
    catalog_gap: 49.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 52.0
    developer_ergonomics: 52.4
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Filen Authentication
  slug: filen-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Filen Domain Security
  slug: filen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Filen Vulnerability Disclosure
  slug: filen-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Filen Trust Center
  slug: filen-trust-center
  summary_line: ISO 27001, GDPR
slug: filen
tags:
- Company
- Cloud Storage
- Encryption
- Zero Knowledge
- File Sync
website: https://filen.io/
---
