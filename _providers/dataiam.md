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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Data I Am provides a Salesforce data loading API documented at the Fix & Load release notes page.
  name: Data I Am Fix & Load API
  slug: data-i-am-fix-load-api
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/dataiam/changelog/dataiam-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dataiam-changelog.yml
- group: design
  href: https://artifacts.apis.io/dataiam/errors/dataiam-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dataiam-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dataiam/conformance/dataiam-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dataiam-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dataiam/llms/dataiam-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dataiam-llms.txt
- group: other
  href: https://artifacts.apis.io/dataiam/hosts/dataiam-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dataiam-hosts.yml
- group: other
  href: https://artifacts.apis.io/dataiam/vendors/dataiam-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dataiam-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dataiam.com/fix-and-load/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dataiam.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://dataiam.com/fix-and-load/release-notes
- group: company
  title: ''
  type: Blog
  url: https://dataiam.com/blog
- group: auth
  href: https://artifacts.apis.io/dataiam/security/dataiam-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataiam-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dataiam.com/
coverage:
  checked: '2026-10-20'
  detail: The provider's documentation pages are HTML without a published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 404
    url: https://api.dataiam.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: DataIAm builds Salesforce-native products that integrate and manage data for financial services customers. Its offerings include DataIAm for FSC, a core banking integration with over 200 field mappings across more than 10 objects, and DataIAm Fix & Load, an AI‑powered loader that cleans addresses, dates, phone numbers, and currencies while validating picklist values. The solutions target Salesforce users needing industry‑specific data integration and spreadsheet uploads.
image: https://dataiam.com/assets/images/og-home.png
layout: provider
modified: '2026-10-20'
name: Data I Am
nav: Providers
network: true
overview: 'Data I Am is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Salesforce, Data Integration, and Financial Services.


  Data I Am''s developer surface includes changelog, engineering blog, and 10 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dataiam Domain Security
  slug: dataiam-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dataiam
tags:
- Company
- Salesforce
- Data Integration
- Financial Services
website: https://dataiam.com/
---
