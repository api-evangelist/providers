---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mlsgrid Agentic Access
  operation_count: 8
  slug: mlsgrid-agentic-access
  summary_line: 8 operations
api_count: 7
apis:
- description: Enumerated lookup values per originating MLS.
  name: mlsgrid Lookup API
  slug: mlsgrid-lookup-api
- description: Listing media (photos, virtual tours) expanded from Property.
  name: mlsgrid Media API
  slug: mlsgrid-media-api
- description: Real estate agents (RESO Data Dictionary Member resource).
  name: mlsgrid Member API
  slug: mlsgrid-member-api
- description: OData service and EDMX metadata.
  name: mlsgrid Metadata API
  slug: mlsgrid-metadata-api
- description: Brokerage offices (RESO Data Dictionary Office resource).
  name: mlsgrid Office API
  slug: mlsgrid-office-api
- description: Open house events (RESO Data Dictionary OpenHouse resource).
  name: mlsgrid OpenHouse API
  slug: mlsgrid-openhouse-api
- description: Property listings (RESO Data Dictionary Property resource).
  name: mlsgrid Property API
  slug: mlsgrid-property-api
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MLS Grid RESO Web Lookup API
  slug: open-mlsgrid-lookup-api
- collection_type: open
  name: MLS Grid RESO Web Lookup Media API
  slug: open-mlsgrid-media-api
- collection_type: open
  name: MLS Grid RESO Web Lookup Member API
  slug: open-mlsgrid-member-api
- collection_type: open
  name: MLS Grid RESO Web Lookup Metadata API
  slug: open-mlsgrid-metadata-api
- collection_type: open
  name: MLS Grid RESO Web Lookup Office API
  slug: open-mlsgrid-office-api
- collection_type: open
  name: MLS Grid RESO Web Lookup OpenHouse API
  slug: open-mlsgrid-openhouse-api
- collection_type: open
  name: MLS Grid RESO Web Lookup Property API
  slug: open-mlsgrid-property-api
- collection_type: open
  name: MLS Grid RESO Web API
  slug: open-mlsgrid-reso-web-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mlsgrid-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mlsgrid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mlsgrid-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.mlsgrid.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mlsgrid.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mlsgrid.com/master.md
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mlsgrid.com/api-documentation/api-version-2.0.md
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mlsgrid.com/sitemap.md
- group: other
  title: ''
  type: Resources
  url: https://www.mlsgrid.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mlsgrid.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mlsgrid.com
- group: operate
  title: ''
  type: Support
  url: mailto:support@mlsgrid.com
- group: operate
  title: ''
  type: Contact
  url: mailto:info@mlsgrid.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mlsgrid
- group: docs
  title: ''
  type: Documentation
  url: https://www.reso.org/data-dictionary/
- group: docs
  title: ''
  type: Documentation
  url: https://www.reso.org/reso-web-api/
- group: commercial
  title: ''
  type: Plans
  url: plans/mlsgrid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mlsgrid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mlsgrid-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mlsgrid-vocabulary.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/mlsgrid-rules.yml
created: '2026-05-25T00:00:00.000Z'
description: The MLS Grid is a normalized, RESO-compliant data distribution platform that gives brokers, MLSs, and application vendors a single OData v4 Web API and one master data license agreement covering 50+ participating MLSs across the United States. Built on the RESO Data Dictionary, the MLS Grid Web API standardizes Property, Member, Office, OpenHouse, Media, and Lookup resources for IDX, VOW, broker-only, and product-development use cases, replacing the per-MLS RETS feed sprawl that historically burdened real-estate technology vendors.
examples:
- key_count: 2
  name: Mlsgrid List Properties Example
  slug: mlsgrid-list-properties-example
features:
- RESO Data Dictionary compliant entity model (Property, Member, Office, OpenHouse, Media, Lookup)
- RESO Web API compliant OData v4 surface with $select, $filter, $expand, $top, $count, @odata.nextLink
- Single Master Data License Agreement spanning all participating MLSs
- OAuth 2.0 bearer-token authentication with long-lived tokens
- Incremental replication via OriginatingSystemName + ModificationTimestamp pattern
- $expand=Media,Rooms,UnitTypes for nested resource replication on Property
- Standalone Media resource where the originating MLS permits (e.g. Northstar MLS)
- All date fields normalized to UTC
- Prefixed key fields (e.g. actris-1234567) to namespace records across MLSs
- MlgCanView flag for license-driven retention and deletion handling
- MlgCanUse array indicating allowed use cases (IDX, VOW, BO, PT)
- 50+ participating MLSs including ACTRIS, MRED, Northstar, NWMLS, REcolorado, MARIS, Heartland, Realtracs, OneKey
- Quarterly compliance audits and centralized vendor management
- Per-minute import cadence where the originating MLS permits
- Documented rate limits (2 RPS, 7,200/hour, 40,000/24h, 4 GB/hour) with HTTP 429 on violation
finops:
- name: Mlsgrid Finops
  service_category: ''
  slug: mlsgrid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mlsgrid.png
json_schemas:
- name: MLS Grid Media
  property_count: 15
  slug: mlsgrid-media
- name: MLS Grid Property
  property_count: 37
  slug: mlsgrid-property
jsonld:
- class_count: 24
  name: Mlsgrid Context
  property_count: 2
  slug: mlsgrid-context
layout: provider
modified: '2026-05-25'
name: mlsgrid
nav: Providers
network: true
overview: 'mlsgrid publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Lookup API, Media API, Member API, and 4 more.


  The mlsgrid catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  mlsgrid''s developer surface includes authentication, developer portal, documentation, support, and 17 more developer resources.'
plans:
- name: Mlsgrid Plans Pricing
  plan_count: 2
  slug: mlsgrid-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Mlsgrid Rate Limits
  slug: mlsgrid-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: mlsgrid API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: mlsgrid-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: mlsgrid API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 2
  slug: mlsgrid-rules
score:
  band: developing
  composite: 49.7
  delta: -5.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 73.0
    developer_ergonomics: 35.7
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 36.8
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/mlsgrid/refs/heads/main/screenshots/mlsgrid-2026-06-20T185627.png
security:
- kind: authentication
  name: Mlsgrid Authentication
  slug: mlsgrid-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mlsgrid Domain Security
  slug: mlsgrid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mlsgrid
website: https://www.mlsgrid.com
---
