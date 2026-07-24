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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Trabex Agentic Access
  operation_count: 11
  slug: trabex-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 5
apis:
- description: Submit and manage Electronic Export Information (EEI) filings to the Automated Export System (AES) for export reporting compliance.
  name: Trabex AES Filing API
  slug: trabex-aes-filing-api
- description: Manage company and party information used in trade compliance workflows including shippers, consignees, and freight forwarders.
  name: Trabex Companies API
  slug: trabex-companies-api
- description: Generate and retrieve export compliance documents including commercial invoices, packing lists, certificates of origin, and shipper's letter of instruction.
  name: Trabex Documents API
  slug: trabex-documents-api
- description: Perform restricted party screening (RPS) against denied party lists, sanctioned entities, and embargoed countries to identify compliance risks.
  name: Trabex Screening API
  slug: trabex-screening-api
- description: Submit and manage export shipment data for compliance processing, AES filing, and documentation generation.
  name: Trabex Shipments API
  slug: trabex-shipments-api
artifact_total: 19
collections:
- collection_type: open
  name: Trabex Trade Compliance API
  slug: open-trabex-trade-compliance
common:
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


  Trabex''s developer surface includes authentication, documentation, support, and 4 more developer resources.'
plans:
- name: Trabex Plans Pricing
  plan_count: 3
  slug: trabex-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 5
  name: Trabex Rate Limits
  slug: trabex-rate-limits
rules:
- name: Trabex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: trabex-jsonschema-spectral-rules
- name: Trabex API Rules
  rule_count: 11
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 6
  slug: trabex-rules
score:
  band: developing
  composite: 49.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.3
    developer_ergonomics: 23.9
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 31.6
  previous_composite: 49.2
  schema_version: 0.5
  scored_at: '2026-07-23'
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
