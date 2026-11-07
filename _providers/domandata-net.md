---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Domandata survey platform
  name: Domandata API
  slug: domandata-api
- description: 'Domandata API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Domandata API
  slug: domandata-net-api
artifact_total: 10
common:
- group: docs
  title: ''
  type: Documentation
  url: https://www.domandata.net/guides
- group: commercial
  href: https://artifacts.apis.io/domandata-net/plans/domandata-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/domandata-net-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/domandata-net/rules/domandata-net-rules.yml
  title: ''
  type: Spectral
  url: rules/domandata-net-rules.yml
- group: design
  href: https://artifacts.apis.io/domandata-net/json-ld/domandata-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/domandata-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/domandata-net/vocabulary/domandata-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/domandata-net-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/domandata-net/data-model/domandata-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/domandata-net-data-model.yml
- group: operate
  href: https://artifacts.apis.io/domandata-net/changelog/domandata-net-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/domandata-net-changelog.yml
- group: design
  href: https://artifacts.apis.io/domandata-net/conventions/domandata-net-conventions.yml
  title: ''
  type: Conventions
  url: conventions/domandata-net-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.domandata.net/trust
- group: auth
  href: https://artifacts.apis.io/domandata-net/authentication/domandata-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/domandata-net-authentication.yml
- group: design
  href: https://artifacts.apis.io/domandata-net/conformance/domandata-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/domandata-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/domandata-net/llms/domandata-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/domandata-net-llms.txt
- group: other
  href: https://artifacts.apis.io/domandata-net/hosts/domandata-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/domandata-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/domandata-net/vendors/domandata-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/domandata-net-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.domandata.net/status
- group: auth
  title: ''
  type: Security
  url: https://www.domandata.net/security
- group: start
  title: ''
  type: Login
  url: https://www.domandata.net/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.domandata.net/changelog
- group: auth
  href: https://artifacts.apis.io/domandata-net/security/domandata-net-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/domandata-net-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/domandata-net/security/domandata-net-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/domandata-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/domandata-net/security/domandata-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domandata-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.domandata.net/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.domandata.net/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.domandata.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.domandata.net/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.domandata.net/help
coverage:
  checked: '2026-11-06'
  detail: Documentation pages are rendered via JavaScript and provide no machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.domandata.net/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: Domandata provides academic survey software for social science research and experiments. It offers visual branching, random assignment, quotas, and analysis‑ready exports, enabling researchers to design complex surveys, manage participant allocation, and obtain clean data for rigorous analysis. The platform supports customizable logic, secure data handling, and integrates with statistical tools, making it suitable for universities, labs, and research institutes seeking robust experimental survey capabilities.
image: https://www.domandata.net/opengraph-image?3aa6850c66b27afc
json_schemas:
- name: GetApiV1ResponsesResponse
  property_count: 2
  slug: domandata-net-get-api-v1-responses-response
jsonld:
- class_count: 1
  name: Domandata Net Context
  property_count: 2
  slug: domandata-net-context
layout: provider
modified: '2026-11-05'
name: Domandata
nav: Providers
network: true
overview: 'Domandata is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Surveys, Academic, Research, and Software.


  The Domandata catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Domandata''s developer surface includes documentation, changelog, authentication, pricing, support, and 21 more developer resources.'
plans:
- name: Domandata Net Plans Pricing
  plan_count: 6
  slug: domandata-net-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Domandata API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: domandata-net-rules
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 17.8
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 42.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Domandata Net Authentication
  slug: domandata-net-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Domandata Net Domain Security
  slug: domandata-net-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Domandata Net Vulnerability Disclosure
  slug: domandata-net-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Domandata Net Trust Center
  slug: domandata-net-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA
slug: domandata-net
tags:
- Company
- Surveys
- Academic
- Research
- Software
website: https://www.domandata.net/
---
