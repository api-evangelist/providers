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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Chloris Geospatial Agentic Access
  operation_count: 15
  slug: chloris-geospatial-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 1
apis:
- baseURL: https://app.chloris.earth
  baseurl_source: declared
  description: The Aoi API from Chloris Geospatial — 2 operation(s) for aoi.
  name: Chloris Geospatial Aoi API
  slug: chloris-geospatial-aoi-api
- baseURL: https://app.chloris.earth
  baseurl_source: declared
  description: The Boundary API from Chloris Geospatial — 1 operation(s) for boundary.
  name: Chloris Geospatial Boundary API
  slug: chloris-geospatial-boundary-api
- baseURL: https://app.chloris.earth
  baseurl_source: declared
  description: The Collection API from Chloris Geospatial — 1 operation(s) for collection.
  name: Chloris Geospatial Collection API
  slug: chloris-geospatial-collection-api
- baseURL: https://app.chloris.earth
  baseurl_source: declared
  description: The Info API from Chloris Geospatial — 1 operation(s) for info.
  name: Chloris Geospatial Info API
  slug: chloris-geospatial-info-api
- baseURL: https://app.chloris.earth
  baseurl_source: declared
  description: The Invite API from Chloris Geospatial — 1 operation(s) for invite.
  name: Chloris Geospatial Invite API
  slug: chloris-geospatial-invite-api
- baseURL: https://app.chloris.earth
  baseurl_source: declared
  description: The MgrsTiles API from Chloris Geospatial — 2 operation(s) for mgrstiles.
  name: Chloris Geospatial Mgrs Tiles API
  slug: chloris-geospatial-mgrstiles-api
- baseURL: https://app.chloris.earth
  baseurl_source: declared
  description: The Organization API from Chloris Geospatial — 2 operation(s) for organization.
  name: Chloris Geospatial Organization API
  slug: chloris-geospatial-organization-api
- baseURL: https://app.chloris.earth
  baseurl_source: declared
  description: The ReportingUnit API from Chloris Geospatial — 1 operation(s) for reportingunit.
  name: Chloris Geospatial Reporting Unit API
  slug: chloris-geospatial-reportingunit-api
- baseURL: https://app.chloris.earth
  baseurl_source: declared
  description: The User API from Chloris Geospatial — 1 operation(s) for user.
  name: Chloris Geospatial User API
  slug: chloris-geospatial-user-api
artifact_total: 21
asyncapis:
- description: ''
  name: Chloris Geospatial Webhooks
  slug: chloris-geospatial-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chloris-geospatial/refs/heads/main/agentic-access/chloris-geospatial-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chloris-geospatial-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chloris-geospatial/refs/heads/main/rules/chloris-geospatial-rules.yml
  title: ''
  type: Spectral
  url: rules/chloris-geospatial-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chloris-geospatial/refs/heads/main/json-ld/chloris-geospatial-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chloris-geospatial-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chloris-geospatial/refs/heads/main/vocabulary/chloris-geospatial-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chloris-geospatial-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chloris-geospatial/refs/heads/main/asyncapi/chloris-geospatial-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/chloris-geospatial-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chloris-geospatial/refs/heads/main/data-model/chloris-geospatial-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chloris-geospatial-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chloris-geospatial/refs/heads/main/conventions/chloris-geospatial-conventions.yml
  title: ''
  type: Conventions
  url: conventions/chloris-geospatial-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chloris-geospatial/refs/heads/main/errors/chloris-geospatial-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chloris-geospatial-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chloris-geospatial/refs/heads/main/conformance/chloris-geospatial-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chloris-geospatial-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chloris-geospatial/refs/heads/main/hosts/chloris-geospatial-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chloris-geospatial-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chloris-geospatial/refs/heads/main/vendors/chloris-geospatial-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chloris-geospatial-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chloris.earth/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://app.chloris.earth/docs/1.12.0/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://app.chloris.earth/docs/1.12.0/quick_start_guide/01-account-organization-overview.html
- group: docs
  title: ''
  type: APIReference
  url: https://app.chloris.earth/docs/1.12.0/api-reference.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chloris-geospatial/refs/heads/main/authentication/chloris-geospatial-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chloris-geospatial-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chloris-geospatial/refs/heads/main/security/chloris-geospatial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chloris-geospatial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chloris.earth/
created: '2026-10-08'
description: Chloris Geospatial provides annual forest biomass and carbon data through a geospatial platform. Their service offers high‑resolution (30 m) forest carbon intelligence, covering over 120 million hectares worldwide, with data dating back to 2000. This enables corporations, investors, and carbon project developers to assess, monitor, and verify forest carbon projects with MRV‑ready outputs.
image: https://images.prismic.io/chloris/Qrser6mS2HOIqkgk_HeroOption2.png?auto=format,compress
json_schemas:
- name: collectionEntry
  property_count: 5
  slug: chloris-geospatial-collection-entry
- name: organizationEntry
  property_count: 8
  slug: chloris-geospatial-organization-entry
- name: organization
  property_count: 9
  slug: chloris-geospatial-organization
- name: organizationUsageReport
  property_count: 18
  slug: chloris-geospatial-organization-usage-report
- name: reportingUnitEntry
  property_count: 45
  slug: chloris-geospatial-reporting-unit-entry
- name: reportingUnit
  property_count: 14
  slug: chloris-geospatial-reporting-unit
jsonld:
- class_count: 6
  name: Chloris Geospatial Context
  property_count: 72
  slug: chloris-geospatial-context
layout: provider
modified: '2026-10-08'
name: Chloris Geospatial
nav: Providers
network: true
overview: 'Chloris Geospatial publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Aoi API, Boundary API, Collection API, and 6 more. Tagged areas include Company, Geospatial, Carbon, Data, and Environmental.


  The Chloris Geospatial catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Chloris Geospatial''s developer surface includes documentation, getting-started guide, API reference, authentication, and 14 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Chloris Geospatial API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: chloris-geospatial-rules
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 68.2
    developer_ergonomics: 40.5
    discoverability: 66.1
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Chloris Geospatial Authentication
  slug: chloris-geospatial-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Chloris Geospatial Domain Security
  slug: chloris-geospatial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chloris-geospatial
tags:
- Company
- Geospatial
- Carbon
- Data
- Environmental
website: https://www.chloris.earth/
---
