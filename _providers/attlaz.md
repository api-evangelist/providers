---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.attlaz.com
  baseurl_source: declared
  description: 'Attlaz API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: Attlaz API
  slug: attlaz-api
artifact_total: 5
common:
- group: operate
  href: https://artifacts.apis.io/attlaz/rate-limits/attlaz-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/attlaz-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/attlaz/rules/attlaz-rules.yml
  title: ''
  type: Spectral
  url: rules/attlaz-rules.yml
- group: design
  href: https://artifacts.apis.io/attlaz/vocabulary/attlaz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/attlaz-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/attlaz/cli/attlaz-cli.yml
  title: ''
  type: CLI
  url: cli/attlaz-cli.yml
- group: design
  href: https://artifacts.apis.io/attlaz/conventions/attlaz-conventions.yml
  title: ''
  type: Conventions
  url: conventions/attlaz-conventions.yml
- group: auth
  href: https://artifacts.apis.io/attlaz/authentication/attlaz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/attlaz-authentication.yml
- group: design
  href: https://artifacts.apis.io/attlaz/conformance/attlaz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/attlaz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/attlaz/well-known/attlaz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/attlaz-well-known.yml
- group: other
  href: https://artifacts.apis.io/attlaz/hosts/attlaz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/attlaz-hosts.yml
- group: other
  href: https://artifacts.apis.io/attlaz/vendors/attlaz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/attlaz-vendors.yml
- group: build
  href: https://artifacts.apis.io/attlaz/packages/attlaz-packages.yml
  title: ''
  type: SDKs
  url: packages/attlaz-packages.yml
- group: build
  href: https://artifacts.apis.io/attlaz/packages/attlaz-packages.yml
  title: ''
  type: Packages
  url: packages/attlaz-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://attlaz.com/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://attlaz.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.attlaz.com/
- group: auth
  href: https://artifacts.apis.io/attlaz/security/attlaz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/attlaz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://attlaz.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.attlaz.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.attlaz.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.attlaz.com/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.attlaz.com/reference/api/overview
- group: operate
  title: ''
  type: Changelog
  url: https://docs.attlaz.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://attlaz.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.attlaz.com/signin
created: '2026-10-19'
description: Attlaz provides a unified platform that streamlines data integration, automation, and visualization across various business workflows. Their solution connects ecommerce, finance, IT, marketing, and sales applications, offering real-time monitoring, error management, advanced workflow automation, and data quality tools. Attlaz aims to simplify complex integrations, enabling organizations to centralize and manage their data and processes efficiently.
layout: provider
modified: '2026-10-19'
name: Attlaz
nav: Providers
network: true
overview: 'Attlaz is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, Automation, Data Visualization, and Workflows.


  The Attlaz catalog on APIs.io includes 1 Spectral governance ruleset.


  Attlaz''s developer surface includes CLI, authentication, support, documentation, getting-started guide, API reference, changelog, and 17 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 1
  name: Attlaz Rate Limits
  slug: attlaz-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Attlaz API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: attlaz-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 48.8
    catalog_earned_first_party: 8.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 11.9
    developer_ergonomics: 71.4
    discoverability: 62.5
    operational_transparency: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Attlaz Authentication
  slug: attlaz-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Attlaz Domain Security
  slug: attlaz-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: attlaz
tags:
- Company
- Integration
- Automation
- Data Visualization
- Workflows
website: https://attlaz.com/
---
