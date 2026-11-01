---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API for AppCheck security scanning platform
  name: AppCheck API
  slug: appcheck-api
- description: 'APPCHECK API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: APPCHECK API
  slug: appcheck-ng-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/appcheck-ng/rules/appcheck-ng-rules.yml
  title: ''
  type: Spectral
  url: rules/appcheck-ng-rules.yml
- group: design
  href: https://artifacts.apis.io/appcheck-ng/json-ld/appcheck-ng-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/appcheck-ng-context.jsonld
- group: design
  href: https://artifacts.apis.io/appcheck-ng/vocabulary/appcheck-ng-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/appcheck-ng-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/appcheck-ng/data-model/appcheck-ng-data-model.yml
  title: ''
  type: DataModel
  url: data-model/appcheck-ng-data-model.yml
- group: operate
  href: https://artifacts.apis.io/appcheck-ng/changelog/appcheck-ng-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/appcheck-ng-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://appcheck-ng.com/compliance/
- group: design
  href: https://artifacts.apis.io/appcheck-ng/conformance/appcheck-ng-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appcheck-ng-conformance.yml
- group: other
  href: https://artifacts.apis.io/appcheck-ng/hosts/appcheck-ng-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appcheck-ng-hosts.yml
- group: other
  href: https://artifacts.apis.io/appcheck-ng/vendors/appcheck-ng-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appcheck-ng-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appcheck-ng
- group: auth
  href: https://artifacts.apis.io/appcheck-ng/security/appcheck-ng-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/appcheck-ng-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/appcheck-ng/security/appcheck-ng-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appcheck-ng-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appcheck-ng.com/
- group: docs
  title: ''
  type: Documentation
  url: https://appcheck-ng.com/get-help/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://appcheck-ng.com/get-help/documentation/
- group: operate
  title: ''
  type: Support
  url: https://appcheck-ng.com/get-help/
- group: company
  title: ''
  type: Blog
  url: https://appcheck-ng.com/security-blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appcheck-ng.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appcheck-ng.com/terms-of-service/
coverage:
  checked: '2026-10-19'
  detail: API documentation pages are HTML without a machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contract.
  evidence:
  - status: 404
    url: https://api.appcheck-ng.com/openapi.json
  - status: 404
    url: https://api.appcheck-ng.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: AppCheck Ltd provides comprehensive security scanning solutions for web applications, infrastructure, APIs, CMS, single-page applications, and the entire software development lifecycle. Their platform offers automated penetration testing, vulnerability detection, compliance reporting, and continuous monitoring to help organizations protect digital assets and meet security standards.
image: https://appcheck-ng.com/wp-content/uploads/2023/06/logo.png
json_schemas:
- name: GetApiV13079080045Dfdc3B24966D972E890Bd2ScanprofilesResponse
  property_count: 6
  slug: appcheck-ng-get-api-v13079080045-dfdc3-b24966-d972-e890-bd2-scanprofiles-response
- name: GetApiV13079080045Dfdc3B24966D972E890Bd2ScansResponse
  property_count: 7
  slug: appcheck-ng-get-api-v13079080045-dfdc3-b24966-d972-e890-bd2-scans-response
- name: GetApiV144Df57D3F5A479E334E622F314787DccScanB4Ab4A50C3474B7D
  property_count: 4
  slug: appcheck-ng-get-api-v144-df57-d3-f5-a479-e334-e622-f314787-dcc-scan-b4-ab4-a50-c3474-b7-d
- name: GetApiV144Df57D3F5A479E334E622F314787DccScanB4Ab4A50C3474B7D2
  property_count: 4
  slug: appcheck-ng-get-api-v144-df57-d3-f5-a479-e334-e622-f314787-dcc-scan-b4-ab4-a50-c3474-b7-d2
- name: GetApiV144Df57D3F5A479E334E622F314787DccVulnerabilitiesRespo
  property_count: 14
  slug: appcheck-ng-get-api-v144-df57-d3-f5-a479-e334-e622-f314787-dcc-vulnerabilities-respo
- name: GetApiV18C283D9F0Fcce2034A88C6F6A4176B01Scan310B8E1B53Ed4060
  property_count: 7
  slug: appcheck-ng-get-api-v18-c283-d9-f0-fcce2034-a88-c6-f6-a4176-b01-scan310-b8-e1-b53-ed4060
jsonld:
- class_count: 10
  name: Appcheck Ng Context
  property_count: 8
  slug: appcheck-ng-context
layout: provider
modified: '2026-10-19'
name: APPCHECK
nav: Providers
network: true
overview: 'APPCHECK is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Web Application Scanning, API Security, Infrastructure Scanning, CMS Security, and Single Page Application Scanning.


  The APPCHECK catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APPCHECK''s developer surface includes changelog, documentation, getting-started guide, support, engineering blog, and 14 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: APPCHECK API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: appcheck-ng-rules
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 20.7
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 21.1
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Appcheck Ng Domain Security
  slug: appcheck-ng-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Appcheck Ng Trust Center
  slug: appcheck-ng-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: appcheck-ng
tags:
- Web Application Scanning
- API Security
- Infrastructure Scanning
- CMS Security
- Single Page Application Scanning
- Automated Penetration Testing
website: https://appcheck-ng.com/
---
