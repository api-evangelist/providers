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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Quilt API as documented publicly: 27 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Quilt API
  slug: quilt-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/quilt/plans/quilt-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/quilt-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/quilt/rules/quilt-rules.yml
  title: ''
  type: Spectral
  url: rules/quilt-rules.yml
- group: design
  href: https://artifacts.apis.io/quilt/json-ld/quilt-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/quilt-context.jsonld
- group: design
  href: https://artifacts.apis.io/quilt/vocabulary/quilt-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/quilt-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/quilt/data-model/quilt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/quilt-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.quilt.bio/security
- group: auth
  href: https://artifacts.apis.io/quilt/authentication/quilt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/quilt-authentication.yml
- group: design
  href: https://artifacts.apis.io/quilt/conformance/quilt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/quilt-conformance.yml
- group: agent
  href: https://artifacts.apis.io/quilt/llms/quilt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/quilt-llms.txt
- group: agent
  href: https://artifacts.apis.io/quilt/well-known/quilt-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/quilt-well-known.yml
- group: other
  href: https://artifacts.apis.io/quilt/hosts/quilt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quilt-hosts.yml
- group: other
  href: https://artifacts.apis.io/quilt/vendors/quilt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/quilt-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quilt.bio/terms
- group: operate
  title: ''
  type: Support
  url: https://support.quilt.bio/_hcms/mem/login?redirect_url=https%3A%2F%2Fsupport.quilt.bio%2Fportal
- group: auth
  title: ''
  type: Security
  url: https://www.quilt.bio/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quilt.bio/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.quilt.bio/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.quilt.bio/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.quilt.bio/quilt-python-sdk/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.quilt.bio/quilt-python-sdk/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.quilt.bio/
- group: auth
  href: https://artifacts.apis.io/quilt/security/quilt-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/quilt-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/quilt/security/quilt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quilt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.quilt.bio/
coverage:
  checked: '2026-10-23'
  detail: Documentation is provided as markdown pages without a machine‑readable OpenAPI or GraphQL spec.
  evidence:
  - status: 200
    url: https://docs.quilt.bio/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: Quilt is an AWS‑native life‑science data management platform that transforms data chaos into scientific clarity. It provides AI‑powered tools to accelerate research, ensure compliance, and enable secure, scalable data handling for life‑science teams.
image: https://www.quilt.bio/hubfs/quilt_with_wwwurl.png
json_schemas:
- name: GetQuiltPythonSdkEditingAPackageMdResponse
  property_count: 1
  slug: quilt-get-quilt-python-sdk-editing-apackage-md-response
jsonld:
- class_count: 1
  name: Quilt Context
  property_count: 1
  slug: quilt-context
layout: provider
modified: '2026-10-23'
name: Quilt
nav: Providers
network: true
overview: 'Quilt is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Platform, Life Sciences, and AI.


  The Quilt catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Quilt''s developer surface includes authentication, support, pricing, engineering blog, API reference, getting-started guide, documentation, and 17 more developer resources.'
plans:
- name: Quilt Plans Pricing
  plan_count: 4
  slug: quilt-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Quilt API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: quilt-rules
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 55.2
    catalog_earned_first_party: 12.0
    catalog_gap: 59.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 17.6
    developer_ergonomics: 47.6
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 22.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Quilt Authentication
  slug: quilt-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Quilt Domain Security
  slug: quilt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Quilt Trust Center
  slug: quilt-trust-center
  summary_line: SOC 2, HIPAA
slug: quilt
tags:
- Company
- Data Platform
- Life Sciences
- AI
website: https://www.quilt.bio/
---
