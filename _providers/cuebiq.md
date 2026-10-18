---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Cuebiq Agentic Access
  operation_count: 83
  slug: cuebiq-agentic-access
  summary_line: 83 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.cuebiq.com
  baseurl_source: declared
  description: The Conversion Feed V1 API from Cuebiq — 1 operation(s) for conversion feed v1.
  name: Cuebiq Conversion Feed V1 API
  slug: cuebiq-conversion-feed-v1-api
- baseURL: https://api.cuebiq.com
  baseurl_source: declared
  description: The endpoints managing geosets
  name: Cuebiq Geoset API
  slug: cuebiq-geoset-api
- baseURL: https://api.cuebiq.com
  baseurl_source: declared
  description: The KPIs V2 - Campaign Reports API from Cuebiq — 12 operation(s) for kpis v2 - campaign reports.
  name: Cuebiq KPIs V2 - Campaign Reports API
  slug: cuebiq-kpis-v2-campaign-reports-api
- baseURL: https://api.cuebiq.com
  baseurl_source: declared
  description: The KPIs V2 - Campaigns API from Cuebiq — 10 operation(s) for kpis v2 - campaigns.
  name: Cuebiq KPIs V2 - Campaigns API
  slug: cuebiq-kpis-v2-campaigns-api
- baseURL: https://api.cuebiq.com
  baseurl_source: declared
  description: The KPIs V2 - Customer API from Cuebiq — 1 operation(s) for kpis v2 - customer.
  name: Cuebiq KPIs V2 - Customer API
  slug: cuebiq-kpis-v2-customer-api
- baseURL: https://api.cuebiq.com
  baseurl_source: declared
  description: The KPIs V2 - Shared Campaign Reports API from Cuebiq — 11 operation(s) for kpis v2 - shared campaign reports.
  name: Cuebiq KPIs V2 - Shared Campaign Reports API
  slug: cuebiq-kpis-v2-shared-campaign-reports-api
- baseURL: https://api.cuebiq.com
  baseurl_source: declared
  description: The KPIs V2 - Shared Campaigns API from Cuebiq — 9 operation(s) for kpis v2 - shared campaigns.
  name: Cuebiq KPIs V2 - Shared Campaigns API
  slug: cuebiq-kpis-v2-shared-campaigns-api
- baseURL: https://api.cuebiq.com
  baseurl_source: declared
  description: The KPIs V2 - Shared Reports API from Cuebiq — 11 operation(s) for kpis v2 - shared reports.
  name: Cuebiq KPIs V2 - Shared Reports API
  slug: cuebiq-kpis-v2-shared-reports-api
- baseURL: https://api.cuebiq.com
  baseurl_source: declared
  description: The Measurement V2 API from Cuebiq — 16 operation(s) for measurement v2.
  name: Cuebiq Measurement V2 API
  slug: cuebiq-measurement-v2-api
artifact_total: 21
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cuebiq/refs/heads/main/agentic-access/cuebiq-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cuebiq-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cuebiq/refs/heads/main/rules/cuebiq-rules.yml
  title: ''
  type: Spectral
  url: rules/cuebiq-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cuebiq/refs/heads/main/json-ld/cuebiq-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cuebiq-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cuebiq/refs/heads/main/vocabulary/cuebiq-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cuebiq-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cuebiq/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cuebiq/refs/heads/main/data-model/cuebiq-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cuebiq-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cuebiq/refs/heads/main/errors/cuebiq-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cuebiq-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cuebiq/refs/heads/main/conformance/cuebiq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cuebiq-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cuebiq/refs/heads/main/llms/cuebiq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cuebiq-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cuebiq/refs/heads/main/hosts/cuebiq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cuebiq-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cuebiq/refs/heads/main/vendors/cuebiq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cuebiq-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cuebiq
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuebiq/refs/heads/main/scopes/cuebiq-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cuebiq-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuebiq/refs/heads/main/authentication/cuebiq-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cuebiq-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuebiq/refs/heads/main/security/cuebiq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cuebiq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cuebiq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://openapi.cuebiq.com/
- group: company
  title: ''
  type: Blog
  url: https://cuebiq.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://cuebiq.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cuebiq.com/termsofservice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cuebiq.com/privacy-policy/
created: '2026-10-11'
description: Cuebiq provides location intelligence solutions for brands, agencies, and researchers, turning real‑world movement data into actionable marketing insights. Their platform offers footfall measurement, audience targeting, data platform services, and a suite of resources such as privacy center, blog, case studies, and benchmarks. Cuebiq helps clients understand how people move, shop, and engage, enabling smarter decisions through detailed location analytics and exposure measurement.
json_schemas:
- name: Campaign
  property_count: 9
  slug: cuebiq-campaign
- name: CreateCampaignReportRequest
  property_count: 9
  slug: cuebiq-create-campaign-report-request
- name: CreateCampaignRequest
  property_count: 6
  slug: cuebiq-create-campaign-request
- name: KpiAnalysisByCut
  property_count: 11
  slug: cuebiq-kpi-analysis-by-cut
- name: PerformanceKpis
  property_count: 11
  slug: cuebiq-performance-kpis
- name: PostGeosetRequestBodyRaw
  property_count: 6
  slug: cuebiq-post-geoset-request-body-raw
jsonld:
- class_count: 52
  name: Cuebiq Context
  property_count: 114
  slug: cuebiq-context
layout: provider
modified: '2026-10-11'
name: Cuebiq
nav: Providers
network: true
overview: 'Cuebiq publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Conversion Feed V1 API, Geoset API, KPIs V2 - Campaign Reports API, and 6 more. Tagged areas include Company, Location-Intelligence, Marketing, Data Analytics, and Footfall-Measurement.


  The Cuebiq catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cuebiq''s developer surface includes authentication, API reference, engineering blog, pricing, and 17 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Cuebiq API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 2
  slug: cuebiq-rules
scopes:
- name: Cuebiq Scopes
  scope_count: 0
  slug: cuebiq-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 57.7
    developer_ergonomics: 23.2
    discoverability: 69.6
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Cuebiq Authentication
  slug: cuebiq-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cuebiq Domain Security
  slug: cuebiq-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cuebiq
tags:
- Company
- Location-Intelligence
- Marketing
- Data Analytics
- Footfall-Measurement
website: https://cuebiq.com/
---
