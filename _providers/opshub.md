---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'OpsHub API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: OpsHub API
  slug: opshub-api
artifact_total: 8
common:
- group: other
  href: https://artifacts.apis.io/opshub/vendors/opshub-vendors.yml
  title: ''
  type: Vendors
  url: vendors/opshub-vendors.yml
- group: design
  href: https://artifacts.apis.io/opshub/rules/opshub-rules.yml
  title: ''
  type: Spectral
  url: rules/opshub-rules.yml
- group: design
  href: https://artifacts.apis.io/opshub/json-ld/opshub-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/opshub-context.jsonld
- group: design
  href: https://artifacts.apis.io/opshub/vocabulary/opshub-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/opshub-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/opshub/data-model/opshub-data-model.yml
  title: ''
  type: DataModel
  url: data-model/opshub-data-model.yml
- group: design
  href: https://artifacts.apis.io/opshub/conventions/opshub-conventions.yml
  title: ''
  type: Conventions
  url: conventions/opshub-conventions.yml
- group: auth
  href: https://artifacts.apis.io/opshub/authentication/opshub-authentication.yml
  title: ''
  type: Authentication
  url: authentication/opshub-authentication.yml
- group: design
  href: https://artifacts.apis.io/opshub/conformance/opshub-conformance.yml
  title: ''
  type: Conformance
  url: conformance/opshub-conformance.yml
- group: agent
  href: https://artifacts.apis.io/opshub/llms/opshub-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/opshub-llms.txt
- group: agent
  href: https://artifacts.apis.io/opshub/well-known/opshub-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/opshub-well-known.yml
- group: other
  href: https://artifacts.apis.io/opshub/hosts/opshub-hosts.yml
  title: ''
  type: Hosts
  url: hosts/opshub-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opshub.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opshub.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://community.opshub.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.opshub.com/release-notes
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.opshub.com/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opshub.com/
- group: auth
  href: https://artifacts.apis.io/opshub/security/opshub-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opshub-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opshub.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.opshub.com/plans/
- group: company
  title: ''
  type: Blog
  url: https://www.opshub.com/blogs/
- group: operate
  title: ''
  type: Contact
  url: https://www.opshub.com/contact-us/
coverage:
  checked: '2026-10-21'
  detail: Home page renders via JavaScript, preventing machine-readable spec extraction.
  evidence:
  - status: 200
    url: https://www.opshub.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: OpsHub provides enterprise-grade integration and migration solutions for Application Lifecycle Management (ALM), IT Service Management (ITSM), Customer Relationship Management (CRM), and DevOps systems. Their platform enables seamless data synchronization, process automation, and migration across disparate tools, helping organizations streamline workflows and reduce manual effort. OpsHub serves a wide range of industries, offering customizable connectors and robust security features to ensure reliable, compliant data transfers.
image: https://eadn-wc03-9136207.nxedge.io/cdn/wp-content/uploads/2024/04/oh-logo-icon.png
json_schemas:
- name: GetManageApiApiCapabilityMatrixMdResponse
  property_count: 1
  slug: opshub-get-manage-api-api-capability-matrix-md-response
- name: GetManageApiSampleUseCasesConfigureReconcileOnExisitingInteg
  property_count: 1
  slug: opshub-get-manage-api-sample-use-cases-configure-reconcile-on-exisiting-integ
- name: GetManageApiSampleUseCasesRetriveAndConfigureIntegrationPair
  property_count: 1
  slug: opshub-get-manage-api-sample-use-cases-retrive-and-configure-integration-pair
jsonld:
- class_count: 3
  name: Opshub Context
  property_count: 3
  slug: opshub-context
layout: provider
modified: '2026-10-21'
name: OpsHub
nav: Providers
network: true
overview: 'OpsHub is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, Migration, ALM, ITSM, and CRM.


  The OpsHub catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpsHub''s developer surface includes authentication, changelog, getting-started guide, documentation, pricing, engineering blog, and 16 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: OpsHub API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: opshub-rules
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 51.0
    catalog_earned_first_party: 0.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 22.4
    contract_governance: 19.7
    contract_quality: 20.1
    developer_ergonomics: 23.8
    discoverability: 64.3
    operational_transparency: 7.9
  previous_composite: 33.4
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/opshub/opshub-2026-11-03T140713.png
security:
- kind: authentication
  name: Opshub Authentication
  slug: opshub-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Opshub Domain Security
  slug: opshub-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: opshub
tags:
- Integration
- Migration
- ALM
- ITSM
- CRM
- DevOps
- Enterprise
website: https://www.opshub.com/
---
