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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tagetik Agentic Access
  operation_count: 2
  slug: tagetik-agentic-access
  summary_line: 2 operations
api_count: 3
apis:
- description: 'SCIM v2 (System for Cross-domain Identity Management) API for automated user provisioning and deprovisioning in CCH Tagetik. Supports synchronizing users and groups from Microsoft Entra ID (Azure AD) '
  name: CCH Tagetik SCIM API
  slug: cch-tagetik-scim-api
- description: The Financial Data API from CCH Tagetik — 1 operation(s) for financial data.
  name: CCH Tagetik Financial Data API
  slug: tagetik-financial-data-api
- description: The Metadata API from CCH Tagetik — 1 operation(s) for metadata.
  name: CCH Tagetik Metadata API
  slug: tagetik-metadata-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CCH Tagetik OData API
  slug: open-cch-tagetik-odata
- collection_type: open
  name: CCH Tagetik OData Financial Data API
  slug: open-tagetik-financial-data-api
- collection_type: open
  name: CCH Tagetik OData Financial Data Metadata API
  slug: open-tagetik-metadata-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tagetik-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tagetik-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tagetik-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tagetik-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tagetik
- group: company
  title: ''
  type: Website
  url: https://www.wolterskluwer.com/en/solutions/cch-tagetik
- group: docs
  title: ''
  type: Documentation
  url: https://help.tagetik.com
- group: build
  title: ''
  type: Technology Integrations
  url: https://www.wolterskluwer.com/en/solutions/cch-tagetik/technology-integrations
- group: operate
  title: ''
  type: Support
  url: https://www.wolterskluwer.com/en/solutions/cch-tagetik/services/support
- group: build
  title: ''
  type: Power BI Integration
  url: https://learn.microsoft.com/en-us/power-query/connectors/wolters-kluwer-cch-tagetik
- group: learn
  title: ''
  type: Azure AD SSO Tutorial
  url: https://learn.microsoft.com/azure/active-directory/saas-apps/cch-tagetik-tutorial
- group: learn
  title: ''
  type: Training
  url: https://www.academy.registration.tagetik.com
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/tagetik/refs/heads/main/json-schema/cch-tagetik-financial-record-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/tagetik/refs/heads/main/vocabulary/tagetik-vocabulary.yml
created: '2025-01-15'
description: CCH Tagetik (a Wolters Kluwer solution) is a comprehensive Corporate Performance Management platform covering financial close and consolidation, extended planning and analysis, ESG and regulatory reporting, and corporate tax management. The platform exposes data via OData v4 REST APIs and SCIM, enabling integration with Power BI, Qlik, SAP HANA, and other BI tools. OAuth 2.0 and Basic Authentication are supported for secure access.
examples:
- key_count: 2
  name: Cch Tagetik Query Financial Data Example
  slug: cch-tagetik-query-financial-data-example
finops:
- name: Tagetik Finops
  service_category: API
  slug: tagetik-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tagetik.png
json_schemas:
- name: Financial Record
  property_count: 18
  slug: cch-tagetik-financial-record
json_structures:
- name: Cch Tagetik Financial Record Structure
  property_count: 0
  slug: cch-tagetik-financial-record-structure
jsonld:
- class_count: 3
  name: Tagetik Context
  property_count: 20
  slug: tagetik-context
layout: provider
modified: '2026-05-19'
name: CCH Tagetik
nav: Providers
network: true
overview: 'CCH Tagetik publishes 2 APIs on the [APIs.io](https://apis.io/) network: Financial Data API and Metadata API. Tagged areas include Analytics, Budgeting, Corporate Performance Management, ESG, and Financial Close.


  The CCH Tagetik catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  CCH Tagetik''s developer surface includes authentication, documentation, support, training material, and 10 more developer resources.'
plans:
- name: Tagetik Plans Pricing
  plan_count: 3
  slug: tagetik-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Tagetik Rate Limits
  slug: tagetik-rate-limits
rules:
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: CCH Tagetik API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 4
  slug: cch-tagetik-odata-rules
- effective_rule_count: 5
  extends: []
  name: CCH Tagetik API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tagetik-jsonschema-spectral-rules
scopes:
- name: Tagetik Scopes
  scope_count: 1
  slug: tagetik-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 40.3
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 69.7
    contract_quality: 60.5
    developer_ergonomics: 26.2
    discoverability: 74.1
    governance: 69.7
    operational_transparency: 7.9
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tagetik/refs/heads/main/screenshots/tagetik-2026-06-20T194856.png
security:
- kind: authentication
  name: Tagetik Authentication
  slug: tagetik-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Tagetik Domain Security
  slug: tagetik-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tagetik
tags:
- Analytics
- Budgeting
- Corporate Performance Management
- ESG
- Financial Close
- Financial Consolidation
- Financial Planning
- OData
- Reporting
website: https://www.wolterskluwer.com/en/solutions/cch-tagetik
---
