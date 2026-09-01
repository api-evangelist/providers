---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Us Patent And Trademark Office Agentic Access
  operation_count: 41
  slug: us-patent-and-trademark-office-agentic-access
  summary_line: 41 operations · 8 acting
api_count: 2
apis:
- description: Access bulk raw public data from the Chief Economist office
  name: US Patent and Trademark Office Bulk Datasets API
  slug: us-patent-and-trademark-office-bulk-datasets-api
- description: Retrieve trademark case documents and images
  name: US Patent and Trademark Office Case Documents API
  slug: us-patent-and-trademark-office-case-documents-api
- description: Retrieve trademark case status and metadata
  name: US Patent and Trademark Office Case Status API
  slug: us-patent-and-trademark-office-case-status-api
- description: Search and retrieve patent application data
  name: US Patent and Trademark Office Patent Search API
  slug: us-patent-and-trademark-office-patent-search-api
- description: Search and retrieve petition decision records
  name: US Patent and Trademark Office Petition Decisions API
  slug: us-patent-and-trademark-office-petition-decisions-api
- description: All public decisions filed in PTAB Appeals
  name: US Patent and Trademark Office PTAB Appeals API
  slug: us-patent-and-trademark-office-ptab-appeals-api
- description: All public decisions filed in PTAB Interferences
  name: US Patent and Trademark Office PTAB Interferences API
  slug: us-patent-and-trademark-office-ptab-interferences-api
- description: All public decisions filed in PTAB Trials
  name: US Patent and Trademark Office PTAB Trials Decisions API
  slug: us-patent-and-trademark-office-ptab-trials-decisions-api
- description: All public documents filed in PTAB Trials
  name: US Patent and Trademark Office PTAB Trials Documents API
  slug: us-patent-and-trademark-office-ptab-trials-documents-api
- description: All public PTAB Trial proceedings
  name: US Patent and Trademark Office PTAB Trials Proceedings API
  slug: us-patent-and-trademark-office-ptab-trials-proceedings-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USPTO Open Data Portal Bulk Datasets API
  slug: open-us-patent-and-trademark-office-bulk-datasets-api
- collection_type: open
  name: USPTO Open Data Portal Bulk Datasets Case Documents API
  slug: open-us-patent-and-trademark-office-case-documents-api
- collection_type: open
  name: USPTO Open Data Portal Bulk Datasets Case Status API
  slug: open-us-patent-and-trademark-office-case-status-api
- collection_type: open
  name: USPTO Open Data Portal Bulk Datasets Patent Search API
  slug: open-us-patent-and-trademark-office-patent-search-api
- collection_type: open
  name: USPTO Open Data Portal Bulk Datasets Petition Decisions API
  slug: open-us-patent-and-trademark-office-petition-decisions-api
- collection_type: open
  name: USPTO Open Data Portal Bulk Datasets PTAB Appeals API
  slug: open-us-patent-and-trademark-office-ptab-appeals-api
- collection_type: open
  name: USPTO Open Data Portal Bulk Datasets PTAB Interferences API
  slug: open-us-patent-and-trademark-office-ptab-interferences-api
- collection_type: open
  name: USPTO Open Data Portal Bulk Datasets PTAB Trials Decisions API
  slug: open-us-patent-and-trademark-office-ptab-trials-decisions-api
- collection_type: open
  name: USPTO Open Data Portal Bulk Datasets PTAB Trials Documents API
  slug: open-us-patent-and-trademark-office-ptab-trials-documents-api
- collection_type: open
  name: USPTO Open Data Portal Bulk Datasets PTAB Trials Proceedings API
  slug: open-us-patent-and-trademark-office-ptab-trials-proceedings-api
- collection_type: open
  name: USPTO Open Data Portal API
  slug: open-uspto-open-data-portal
- collection_type: open
  name: USPTO Trademark Status and Document Retrieval API
  slug: open-uspto-tsdr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/us-patent-and-trademark-office-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-patent-and-trademark-office-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/us-patent-and-trademark-office-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.uspto.gov/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USPTO
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uspto
created: '2024-12-03'
description: The US Patent and Trademark Office (USPTO) is responsible for granting patents and registering trademarks to protect intellectual property in the United States. The USPTO examines patent applications to determine if an invention is new, non-obvious, and useful, and grants patents to those that meet the criteria. They also register trademarks, which are words, phrases, symbols, or designs that distinguish goods or services of one entity from another. The USPTO Open Data Portal provides free programmatic access to patent applications, PTAB trial proceedings, petition decisions, trademark status, and bulk datasets.
examples:
- key_count: 2
  name: Uspto Get Ptab Proceeding Example
  slug: uspto-get-ptab-proceeding-example
- key_count: 2
  name: Uspto Get Trademark Case Status Example
  slug: uspto-get-trademark-case-status-example
- key_count: 2
  name: Uspto Search Patent Applications Example
  slug: uspto-search-patent-applications-example
finops:
- name: Us Patent And Trademark Office Finops
  service_category: API
  slug: us-patent-and-trademark-office-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-patent-and-trademark-office.png
json_schemas:
- name: USPTO Patent Application
  property_count: 12
  slug: uspto-patent-application
- name: USPTO Trademark Case
  property_count: 11
  slug: uspto-trademark-case
json_structures:
- name: Uspto Patent Application Structure
  property_count: 0
  slug: uspto-patent-application-structure
jsonld:
- class_count: 3
  name: Us Patent And Trademark Office Context
  property_count: 21
  slug: us-patent-and-trademark-office-context
layout: provider
modified: '2026-05-19'
name: US Patent and Trademark Office
nav: Providers
network: true
overview: 'US Patent and Trademark Office publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Bulk Datasets API, Case Documents API, Case Status API, and 7 more. Tagged areas include Federal-Government, Patents, Trademarks, Intellectual Property, and Open Data.


  The US Patent and Trademark Office catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  US Patent and Trademark Office''s developer surface includes authentication, engineering blog, and 4 more developer resources.'
plans:
- name: Us Patent And Trademark Office Plans Pricing
  plan_count: 3
  slug: us-patent-and-trademark-office-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Us Patent And Trademark Office Rate Limits
  slug: us-patent-and-trademark-office-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: US Patent and Trademark Office API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: us-patent-and-trademark-office-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: US Patent and Trademark Office API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 5
  slug: uspto-rules
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 16
    catalog_gap: 61.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 56.1
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-patent-and-trademark-office/refs/heads/main/screenshots/us-patent-and-trademark-office-2026-06-20T200649.png
security:
- kind: authentication
  name: Us Patent And Trademark Office Authentication
  slug: us-patent-and-trademark-office-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Us Patent And Trademark Office Domain Security
  slug: us-patent-and-trademark-office-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: us-patent-and-trademark-office
tags:
- Federal-Government
- Patents
- Trademarks
- Intellectual Property
- Open Data
---
