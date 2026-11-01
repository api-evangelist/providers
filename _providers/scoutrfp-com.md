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
- description: 'ScoutRFP * API as documented publicly: 18 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: ScoutRFP * API
  slug: scoutrfp-com-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/scoutrfp-com/rules/scoutrfp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/scoutrfp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/scoutrfp-com/json-ld/scoutrfp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/scoutrfp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/scoutrfp-com/vocabulary/scoutrfp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/scoutrfp-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/scoutrfp-com/data-model/scoutrfp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scoutrfp-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/scoutrfp-com/changelog/scoutrfp-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/scoutrfp-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/scoutrfp-com/conventions/scoutrfp-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/scoutrfp-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/scoutrfp-com/lifecycle/scoutrfp-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/scoutrfp-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/scoutrfp-com/conformance/scoutrfp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scoutrfp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/scoutrfp-com/llms/scoutrfp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scoutrfp-com-llms.txt
- group: other
  href: https://artifacts.apis.io/scoutrfp-com/hosts/scoutrfp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scoutrfp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/scoutrfp-com/vendors/scoutrfp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scoutrfp-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- group: company
  title: ''
  type: Blog
  url: https://blog.workday.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.workday.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ScoutRFP
- group: auth
  href: https://artifacts.apis.io/scoutrfp-com/security/scoutrfp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scoutrfp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://scoutrfp.com
coverage:
  checked: '2026-10-26'
  detail: The company redirects its main domain to a Workday product page and provides no API documentation or developer portal.
  evidence:
  - status: 301
    url: https://scoutrfp.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: ScoutRFP provides a cloud‑based platform that helps organizations automate and manage the strategic sourcing process, from request for proposal (RFP) creation to vendor selection and contract award. The service offers tools for collaboration, document management, scoring, and analytics, enabling procurement teams to streamline sourcing workflows, improve compliance, and achieve better supplier outcomes. ScoutRFP is backed by GV and targets enterprises seeking modern, data‑driven sourcing solutions.
image: https://www.workday.com/content/dam/web/en-us/images/social/workday-og-theme.png
json_schemas:
- name: GetReportingV11AppsAppidOrchestrationsOrchnameRunsResponse
  property_count: 8
  slug: scoutrfp-com-get-reporting-v11-apps-appid-orchestrations-orchname-runs-response
- name: GetReportingV11AppsAppidOrchestrationsOrchnameRunsRunidRespo
  property_count: 4
  slug: scoutrfp-com-get-reporting-v11-apps-appid-orchestrations-orchname-runs-runid-respo
- name: GetReportingV11AppsAppidOrchestrationsResponse
  property_count: 3
  slug: scoutrfp-com-get-reporting-v11-apps-appid-orchestrations-response
- name: GetReportingV11OrganizationsOrgidAppsResponse
  property_count: 3
  slug: scoutrfp-com-get-reporting-v11-organizations-orgid-apps-response
- name: GetReportingV11TenantedAppsResponse
  property_count: 3
  slug: scoutrfp-com-get-reporting-v11-tenanted-apps-response
- name: PostDataRequest
  property_count: 2
  slug: scoutrfp-com-post-data-request
jsonld:
- class_count: 12
  name: Scoutrfp Com Context
  property_count: 23
  slug: scoutrfp-com-context
layout: provider
modified: '2026-10-25'
name: ScoutRFP *
nav: Providers
network: true
overview: 'ScoutRFP * is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Procurement, SaaS, RFP, and Collaboration.


  The ScoutRFP * catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ScoutRFP *''s developer surface includes changelog, engineering blog, documentation, and 14 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: ScoutRFP * API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: scoutrfp-com-rules
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 35.6
    contract_quality: 24.7
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Scoutrfp Com Domain Security
  slug: scoutrfp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scoutrfp-com
tags:
- Company
- Procurement
- SaaS
- RFP
- Collaboration
website: http://scoutrfp.com
---
