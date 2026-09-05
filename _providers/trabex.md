---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: verified
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
  score: 25.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Trabex Agentic Access
  operation_count: 11
  slug: trabex-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.trabex.io
  baseurl_source: declared
  description: Submit and manage Electronic Export Information (EEI) filings to the Automated Export System (AES) for export reporting compliance.
  name: Trabex AES Filing API
  slug: trabex-aes-filing-api
- baseURL: https://api.trabex.io
  baseurl_source: declared
  description: Manage company and party information used in trade compliance workflows including shippers, consignees, and freight forwarders.
  name: Trabex Companies API
  slug: trabex-companies-api
- baseURL: https://api.trabex.io
  baseurl_source: declared
  description: Generate and retrieve export compliance documents including commercial invoices, packing lists, certificates of origin, and shipper's letter of instruction.
  name: Trabex Documents API
  slug: trabex-documents-api
- baseURL: https://api.trabex.io
  baseurl_source: declared
  description: Perform restricted party screening (RPS) against denied party lists, sanctioned entities, and embargoed countries to identify compliance risks.
  name: Trabex Screening API
  slug: trabex-screening-api
- baseURL: https://api.trabex.io
  baseurl_source: declared
  description: Submit and manage export shipment data for compliance processing, AES filing, and documentation generation.
  name: Trabex Shipments API
  slug: trabex-shipments-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trabex Trade Compliance AES Filing API
  slug: open-trabex-aes-filing-api
- collection_type: open
  name: Trabex Trade Compliance AES Filing Companies API
  slug: open-trabex-companies-api
- collection_type: open
  name: Trabex Trade Compliance AES Filing Documents API
  slug: open-trabex-documents-api
- collection_type: open
  name: Trabex Trade Compliance AES Filing Screening API
  slug: open-trabex-screening-api
- collection_type: open
  name: Trabex Trade Compliance AES Filing Shipments API
  slug: open-trabex-shipments-api
- collection_type: open
  name: Trabex Trade Compliance API
  slug: open-trabex-trade-compliance
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/trabex-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trabex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trabex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trabex-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trabex-export-compliance
- group: company
  title: ''
  type: Website
  url: https://trabex.io
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.trabex.io/
- group: operate
  title: ''
  type: Support
  url: https://support.trabex.io/support/home
created: '2026-03-16'
description: Trabex is a trade compliance platform that provides automated export compliance, shipment management, restricted party screening, and Automated Export System (AES) filing services. Trabex offers APIs for integrating trade compliance workflows including shipment data ingestion, export documentation generation, financial reporting, and ancillary compliance data to help organizations manage global trade risk.
examples:
- key_count: 2
  name: Trabex Create Shipment Example
  slug: trabex-create-shipment-example
- key_count: 2
  name: Trabex Screen Party Example
  slug: trabex-screen-party-example
finops:
- name: Trabex Finops
  service_category: API
  slug: trabex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trabex.png
json_schemas:
- name: Trabex Export Shipment
  property_count: 16
  slug: trabex-shipment
json_structures:
- name: Trabex Shipment Structure
  property_count: 0
  slug: trabex-shipment-structure
jsonld:
- class_count: 39
  name: Trabex Context
  property_count: 0
  slug: trabex-context
layout: provider
modified: '2026-05-19'
name: Trabex
nav: Providers
network: true
overview: 'Trabex publishes 5 APIs on the [APIs.io](https://apis.io/) network, including AES Filing API, Companies API, Documents API, and 2 more. Tagged areas include Compliance, Export Control, Logistics, Restricted Party Screening, and Shipment Management.


  The Trabex catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Trabex''s developer surface includes authentication, documentation, support, and 5 more developer resources.'
plans:
- name: Trabex Plans Pricing
  plan_count: 3
  slug: trabex-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Trabex Rate Limits
  slug: trabex-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Trabex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: trabex-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Trabex API Rules
  rule_count: 11
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 6
  slug: trabex-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 69.5
    catalog_earned_first_party: 0.0
    catalog_gap: 45.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 67.1
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trabex/refs/heads/main/screenshots/trabex-2026-06-20T195511.png
security:
- kind: authentication
  name: Trabex Authentication
  slug: trabex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Trabex Domain Security
  slug: trabex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trabex
tags:
- Compliance
- Export Control
- Logistics
- Restricted Party Screening
- Shipment Management
- Trade Compliance
website: https://trabex.io
---
