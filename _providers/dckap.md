---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: DCKAP Integrator API provides integration capabilities for ERP and eCommerce platforms, as documented in the DCKAP Integrator documentation.
  name: Integrator API
  slug: integrator-api
- baseURL: https://integrator.dckap.com
  baseurl_source: declared
  description: 'DCKAP API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: DCKAP API
  slug: dckap-api
artifact_total: 14
common:
- group: auth
  href: https://artifacts.apis.io/dckap/well-known/dckap-dckapintegrator-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dckap-dckapintegrator-security.txt
- group: commercial
  href: https://artifacts.apis.io/dckap/plans/dckap-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dckap-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dckap/rules/dckap-rules.yml
  title: ''
  type: Spectral
  url: rules/dckap-rules.yml
- group: design
  href: https://artifacts.apis.io/dckap/json-ld/dckap-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dckap-context.jsonld
- group: design
  href: https://artifacts.apis.io/dckap/vocabulary/dckap-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dckap-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dckap/data-model/dckap-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dckap-data-model.yml
- group: operate
  href: https://artifacts.apis.io/dckap/changelog/dckap-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dckap-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.dckap.com/
- group: auth
  href: https://artifacts.apis.io/dckap/authentication/dckap-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dckap-authentication.yml
- group: design
  href: https://artifacts.apis.io/dckap/conformance/dckap-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dckap-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dckap/well-known/dckap-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dckap-well-known.yml
- group: other
  href: https://artifacts.apis.io/dckap/hosts/dckap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dckap-hosts.yml
- group: other
  href: https://artifacts.apis.io/dckap/vendors/dckap-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dckap-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dckap.com/terms-of-service/
- group: operate
  title: ''
  type: StatusPage
  url: https://dckapintegrator.statuspage.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dckap.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.dckap.com/others/release-notes/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dckap.com/getting-started/quick-start-guide/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dckap
- group: auth
  href: https://artifacts.apis.io/dckap/security/dckap-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dckap-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dckap/security/dckap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dckap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dckap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dckap.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.dckap.com/
- group: company
  title: ''
  type: Blog
  url: https://www.dckap.com/blog/
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.dckap.com/others/product-roadmap/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dckap.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.dckap.com/demo/
- group: operate
  title: ''
  type: Support
  url: https://docs.dckap.com/user-guide/contact-support/
created: '2026-10-20'
description: DCKAP provides ERP integration solutions for distributors and manufacturers, offering platform‑agnostic connectors to sync systems with major ERPs such as NetSuite, SAP, Microsoft Dynamics, and more. Their services include the DCKAP Integrator, DCKAP EDI, and custom data integration across ecommerce, CRM, and ERP platforms, helping businesses streamline operations and improve data flow.
image: https://www.dckap.com/wp-content/uploads/2024/03/DCKAP-Integrator.png
json_schemas:
- name: GetApiTemplatesGetAllResponse
  property_count: 7
  slug: dckap-get-api-templates-get-all-response
- name: GetWorkspaceProjectidApiCredentialsGetAllResponse
  property_count: 12
  slug: dckap-get-workspace-projectid-api-credentials-get-all-response
- name: PostApiProjectsCreateRequest
  property_count: 4
  slug: dckap-post-api-projects-create-request
- name: PostApiProjectsUpdateIdRequest
  property_count: 4
  slug: dckap-post-api-projects-update-id-request
- name: PostWorkspaceProjectidApiSettingsUpdateRequest
  property_count: 4
  slug: dckap-post-workspace-projectid-api-settings-update-request
- name: PostWorkspaceProjectidImportTemplateTemplateidRequest
  property_count: 4
  slug: dckap-post-workspace-projectid-import-template-templateid-request
jsonld:
- class_count: 17
  name: Dckap Context
  property_count: 28
  slug: dckap-context
layout: provider
modified: '2026-10-20'
name: DCKAP
nav: Providers
network: true
overview: 'DCKAP is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, ERP, E-Commerce, and Data Sync.


  The DCKAP catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DCKAP''s developer surface includes changelog, authentication, getting-started guide, documentation, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Dckap Plans Pricing
  plan_count: 1
  slug: dckap-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: DCKAP API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: dckap-rules
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 81.6
    contract_governance: 22.0
    contract_quality: 24.8
    developer_ergonomics: 50.0
    discoverability: 57.1
    operational_transparency: 52.6
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
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dckap Authentication
  slug: dckap-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dckap Domain Security
  slug: dckap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Dckap Trust Center
  slug: dckap-trust-center
  summary_line: SOC 2
slug: dckap
tags:
- Company
- Integration
- ERP
- E-Commerce
- Data Sync
website: https://dckap.com/
---
