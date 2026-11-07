---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.4
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: API for EBSCOhost services, providing access to search, retrieve, and AI insights for library resources.
  name: EBSCOhost API
  slug: ebscohost-api
- baseURL: https://apis.ebsco.com/medsapi-dynamed
  baseurl_source: declared
  description: The Content API from EBSCO — 1 operation(s) for content.
  name: EBSCO Content API
  slug: ebsco-content-api
- baseURL: https://apis.ebsco.com/medsapi-dynamed
  baseurl_source: declared
  description: The Publishers API from EBSCO — 1 operation(s) for publishers.
  name: EBSCO Publishers API
  slug: ebsco-publishers-api
artifact_total: 10
common:
- group: operate
  href: https://artifacts.apis.io/ebsco/rate-limits/ebsco-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ebsco-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/ebsco/rules/ebsco-rules.yml
  title: ''
  type: Spectral
  url: rules/ebsco-rules.yml
- group: design
  href: https://artifacts.apis.io/ebsco/json-ld/ebsco-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ebsco-context.jsonld
- group: design
  href: https://artifacts.apis.io/ebsco/vocabulary/ebsco-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ebsco-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ebsco/data-model/ebsco-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ebsco-data-model.yml
- group: operate
  href: https://artifacts.apis.io/ebsco/changelog/ebsco-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ebsco-changelog.yml
- group: auth
  href: https://artifacts.apis.io/ebsco/authentication/ebsco-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ebsco-authentication.yml
- group: design
  href: https://artifacts.apis.io/ebsco/conformance/ebsco-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ebsco-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ebsco/llms/ebsco-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ebsco-llms.txt
- group: auth
  href: https://artifacts.apis.io/ebsco/well-known/ebsco-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ebsco-status-security.txt
- group: agent
  href: https://artifacts.apis.io/ebsco/well-known/ebsco-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ebsco-well-known.yml
- group: other
  href: https://artifacts.apis.io/ebsco/hosts/ebsco-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ebsco-hosts.yml
- group: other
  href: https://artifacts.apis.io/ebsco/vendors/ebsco-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ebsco-vendors.yml
- group: build
  href: https://artifacts.apis.io/ebsco/packages/ebsco-packages.yml
  title: ''
  type: SDKs
  url: packages/ebsco-packages.yml
- group: build
  href: https://artifacts.apis.io/ebsco/packages/ebsco-packages.yml
  title: ''
  type: Packages
  url: packages/ebsco-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.ebsco.com/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ebsco.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.ebsco.com/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://about.ebsco.com/about/leadership
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ebsco.com/ebscohost-ai-exchange/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ebsco.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ebsco
- group: auth
  href: https://artifacts.apis.io/ebsco/security/ebsco-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ebsco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ebsco.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ebsco.com
coverage:
  checked: '2026-10-14'
  detail: Developer portal provides API docs but no OpenAPI or other machine-readable contract was found.
  evidence:
  - status: 404
    url: https://developer.ebsco.com/ebscohost-api/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: EBSCO is the leading provider of research databases, e‑journals, magazine subscriptions, e‑books and a discovery service for academic libraries, public libraries, corporations, schools, government and medical institutions. It offers a comprehensive suite of information resources and tools that enable users to search, discover, and access scholarly content across a wide range of subjects and formats, supporting research, education, and professional development worldwide.
image: https://www.ebsco.com/ebsco-default-og-image.png
json_schemas:
- name: GetContentChangeAlertsResponse
  property_count: 18
  slug: ebsco-get-content-change-alerts-response
- name: GetPublishersPublisheridDocumentsDocumentidResponse
  property_count: 3
  slug: ebsco-get-publishers-publisherid-documents-documentid-response
jsonld:
- class_count: 2
  name: Ebsco Context
  property_count: 7
  slug: ebsco-context
layout: provider
modified: '2026-10-14'
name: EBSCO
nav: Providers
network: true
overview: 'EBSCO is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Content API, Publishers API, and 1 more. Tagged areas include Company, Research, Library, Education, and Information.


  The EBSCO catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  EBSCO''s developer surface includes changelog, authentication, getting-started guide, documentation, and 21 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 6
  name: Ebsco Rate Limits
  slug: ebsco-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: EBSCO API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: ebsco-rules
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 22.4
    developer_ergonomics: 34.5
    discoverability: 70.5
    operational_transparency: 68.4
  previous_composite: 40.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/ebsco/ebsco-2026-11-03T131250.png
security:
- kind: authentication
  name: Ebsco Authentication
  slug: ebsco-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ebsco Domain Security
  slug: ebsco-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ebsco
tags:
- Company
- Research
- Library
- Education
- Information
website: https://www.ebsco.com
---
