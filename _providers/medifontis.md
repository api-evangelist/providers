---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Medifontis Agentic Access
  operation_count: 1
  slug: medifontis-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Country-scoped search over official medicine sources via the Medifontis API.
  name: Medifontis API
  slug: medifontis-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/medifontis/agentic-access/medifontis-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/medifontis-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/medifontis/rate-limits/medifontis-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/medifontis-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/medifontis/rules/medifontis-rules.yml
  title: ''
  type: Spectral
  url: rules/medifontis-rules.yml
- group: design
  href: https://artifacts.apis.io/medifontis/conventions/medifontis-conventions.yml
  title: ''
  type: Conventions
  url: conventions/medifontis-conventions.yml
- group: auth
  href: https://artifacts.apis.io/medifontis/authentication/medifontis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/medifontis-authentication.yml
- group: design
  href: https://artifacts.apis.io/medifontis/conformance/medifontis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/medifontis-conformance.yml
- group: agent
  href: https://artifacts.apis.io/medifontis/llms/medifontis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/medifontis-llms.txt
- group: other
  href: https://artifacts.apis.io/medifontis/hosts/medifontis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/medifontis-hosts.yml
- group: other
  href: https://artifacts.apis.io/medifontis/vendors/medifontis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/medifontis-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.medifontis.com/us/en/docs/quickstart/
- group: docs
  title: ''
  type: APIReference
  url: https://www.medifontis.com/us/en/docs/api/
- group: auth
  href: https://artifacts.apis.io/medifontis/security/medifontis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/medifontis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.medifontis.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.medifontis.com/it/it/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.medifontis.com/it/it/developers/
- group: start
  title: ''
  type: SignUp
  url: https://www.medifontis.com/it/it/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.medifontis.com/it/it/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.medifontis.com/it/it/privacy/
created: '2026-10-27'
description: Medifontis provides a US drug database API that aggregates FDA NDC directory, Drugs@FDA, DailyMed, RxNorm, UNII substances, and FDA animal drugs into a single RESTful service. The API offers searchable endpoints by name, NDC, RxCUI, application number, SPL ID, and more, with daily updates and licensed source data, enabling developers to integrate comprehensive drug information into their applications.
image: https://www.medifontis.com/og-image.png
layout: provider
modified: '2026-10-27'
name: Medifontis
nav: Providers
network: true
overview: 'Medifontis is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, API, FDA, and Drugs.


  The Medifontis catalog on APIs.io includes 1 Spectral governance ruleset.


  Medifontis'' developer surface includes authentication, getting-started guide, API reference, documentation, signup flow, and 13 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 2
  name: Medifontis Rate Limits
  slug: medifontis-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Medifontis API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: medifontis-rules
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Medifontis Authentication
  slug: medifontis-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Medifontis Domain Security
  slug: medifontis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: medifontis
tags:
- Company
- Healthcare
- API
- FDA
- Drugs
website: https://www.medifontis.com
---
