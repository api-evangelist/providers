---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Sap Fieldglass Agentic Access
  operation_count: 14
  slug: sap-fieldglass-agentic-access
  summary_line: 14 operations · 3 acting
api_count: 5
apis:
- description: Core REST API for SAP Fieldglass that allows clients to send and receive integrated data directly against the application. Supports upload (POST/PUT) and download (GET) of data in JSON and CSV formats
  name: SAP Fieldglass REST API
  slug: sap-fieldglass-rest-api
- description: SCIM-based identity management API for SAP Fieldglass enabling user provisioning, deprovisioning, and lifecycle management for workers, buyers, and suppliers across the contingent workforce platform.
  name: SAP Fieldglass Identity Management API
  slug: sap-fieldglass-identity-management-api
- description: Retrieves configurable pick list values from SAP Fieldglass for use in integration and data validation, including worker types, cost centers, regions, and other reference data.
  name: SAP Fieldglass Pick List Value Download API
  slug: sap-fieldglass-pick-list-value-download-api
- baseURL: https://www.fieldglass.net/api
  baseurl_source: declared
  description: The Approval API from SAP Fieldglass — 5 operation(s) for approval.
  name: SAP Fieldglass Approval API
  slug: sap-fieldglass-approval-api
- baseURL: https://www.fieldglass.net/api
  baseurl_source: declared
  description: The Audit Trail API from SAP Fieldglass — 1 operation(s) for audit trail.
  name: SAP Fieldglass Audit Trail API
  slug: sap-fieldglass-audit-trail-api
- baseURL: https://www.fieldglass.net/api
  baseurl_source: declared
  description: The Get Data API from SAP Fieldglass — 1 operation(s) for get data.
  name: SAP Fieldglass Get Data API
  slug: sap-fieldglass-get-data-api
- baseURL: https://www.fieldglass.net/api
  baseurl_source: declared
  description: The Get Entities API from SAP Fieldglass — 1 operation(s) for get entities.
  name: SAP Fieldglass Get Entities API
  slug: sap-fieldglass-get-entities-api
- baseURL: https://www.fieldglass.net/api
  baseurl_source: declared
  description: The Get Metadata API from SAP Fieldglass — 1 operation(s) for get metadata.
  name: SAP Fieldglass Get Metadata API
  slug: sap-fieldglass-get-metadata-api
- baseURL: https://www.fieldglass.net/api
  baseurl_source: declared
  description: The Get Providers API from SAP Fieldglass — 1 operation(s) for get providers.
  name: SAP Fieldglass Get Providers API
  slug: sap-fieldglass-get-providers-api
- baseURL: https://www.fieldglass.net/api
  baseurl_source: declared
  description: The Order Confirmation API from SAP Fieldglass — 1 operation(s) for order confirmation.
  name: SAP Fieldglass Order Confirmation API
  slug: sap-fieldglass-order-confirmation-api
- baseURL: https://www.fieldglass.net/api
  baseurl_source: declared
  description: The Reports API from SAP Fieldglass — 2 operation(s) for reports.
  name: SAP Fieldglass Reports API
  slug: sap-fieldglass-reports-api
- baseURL: https://www.fieldglass.net/api
  baseurl_source: declared
  description: The Results API from SAP Fieldglass — 1 operation(s) for results.
  name: SAP Fieldglass Results API
  slug: sap-fieldglass-results-api
artifact_total: 63
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Approval API
  slug: open-sap-fieldglass-approval-api
- collection_type: open
  name: Approval Audit Trail API
  slug: open-sap-fieldglass-audit-trail-api
- collection_type: open
  name: Approval Get Data API
  slug: open-sap-fieldglass-get-data-api
- collection_type: open
  name: Approval Get Entities API
  slug: open-sap-fieldglass-get-entities-api
- collection_type: open
  name: Approval Get Metadata API
  slug: open-sap-fieldglass-get-metadata-api
- collection_type: open
  name: Approval Get Providers API
  slug: open-sap-fieldglass-get-providers-api
- collection_type: open
  name: Approval Order Confirmation API
  slug: open-sap-fieldglass-order-confirmation-api
- collection_type: open
  name: Approval Reports API
  slug: open-sap-fieldglass-reports-api
- collection_type: open
  name: Approval Results API
  slug: open-sap-fieldglass-results-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/sap/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sap-fieldglass-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sap-fieldglass-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sap-fieldglass-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sap-fieldglass-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sap-fieldglass-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.sap.com/products/hcm/contingent-workforce-management.html
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/SAP_FIELDGLASS_INTEGRATION
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/SAP
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sapfieldglass/
- group: company
  title: ''
  type: Blog
  url: https://community.sap.com/t5/spend-management-blog-posts-by-sap/bg-p/spend-management-blog-posts-by-sap
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sap.com/products/hcm/contingent-workforce-management/pricing.html
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sap.com/about/trust-center/cloud-service-status.html
- group: other
  title: ''
  type: X
  url: https://x.com/sapfieldglass
- group: commercial
  title: ''
  type: Plans
  url: plans/sap-fieldglass-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sap-fieldglass-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sap-fieldglass-finops.yml
- group: auth
  title: ''
  type: Authentication
  url: https://help.sap.com/docs/SAP_FIELDGLASS_INTEGRATION
- group: other
  title: ''
  type: Hub
  url: https://api.sap.com/package/FieldglassAPI/overview
- group: other
  title: REST APIs
  type: Hub
  url: https://api.sap.com/package/FieldglassAPI/rest
- group: operate
  title: ''
  type: Community
  url: https://pages.community.sap.com/topics/spend-management/fieldglass
- group: operate
  title: ''
  type: Support
  url: https://help.sap.com/docs/SAP_Fieldglass
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fieldglass.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fieldglass.com/privacy-policy
created: '2026-06-13'
description: SAP Fieldglass is a cloud-based vendor management system (VMS) that enables organizations to manage their contingent workforce, services procurement, and external talent. It provides REST APIs for managing work orders, job postings, statements of work, worker profiles, time sheets, invoices, and external talent across more than 165 countries.
examples:
- key_count: 4
  name: Sap Fieldglass Analytics Examples
  slug: sap-fieldglass-analytics-examples
- key_count: 4
  name: Sap Fieldglass Approval Examples
  slug: sap-fieldglass-approval-examples
- key_count: 4
  name: Sap Fieldglass Audit Examples
  slug: sap-fieldglass-audit-examples
- key_count: 4
  name: Sap Fieldglass Bgcheck Examples
  slug: sap-fieldglass-bgcheck-examples
- key_count: 4
  name: Sap Fieldglass Odata Examples
  slug: sap-fieldglass-odata-examples
features:
- description: End-to-end management of contingent workers including job postings, work orders, time sheets, and invoicing.
  name: Contingent Workforce Management
- description: Manage service engagements and statements of work with suppliers and service providers.
  name: Services Procurement
- description: Source, engage, and manage external talent across gig workers and contractors in 165+ countries.
  name: External Talent Management
- description: Track and manage supplier relationships, rates, and performance for the external workforce.
  name: Vendor Management System
- description: Secure API access using OAuth 2.0 protocol supporting web server, installed, and client-side application scenarios.
  name: OAuth 2.0 Authentication
finops:
- name: Sap Fieldglass Finops
  service_category: Vendor Management / Human Capital Management
  slug: sap-fieldglass-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sap-fieldglass.png
integrations:
- description: Native integration with SAP ERP for purchase orders, invoices, cost centers, and financial data.
  name: SAP S/4HANA
- description: Total workforce management integration connecting internal and external talent management.
  name: SAP SuccessFactors
- description: Combined services procurement workflow connecting Ariba sourcing with Fieldglass worker management.
  name: SAP Ariba
json_schemas:
- name: SAP Fieldglass Business Analytics API - Error
  property_count: 3
  slug: sap-fieldglass-analytics-error
- name: SAP Fieldglass Business Analytics API - report
  property_count: 10
  slug: sap-fieldglass-analytics-report
- name: SAP Fieldglass Approval API - approvals
  property_count: 2
  slug: sap-fieldglass-approval-approvals
- name: SAP Fieldglass Approval API - Error
  property_count: 0
  slug: sap-fieldglass-approval-error
- name: SAP Fieldglass Approval API - Status
  property_count: 3
  slug: sap-fieldglass-approval-status
- name: SAP Fieldglass Audit Trail API - auditTrail
  property_count: 2
  slug: sap-fieldglass-audit-audittrail
- name: SAP Fieldglass Audit Trail API - Error
  property_count: 3
  slug: sap-fieldglass-audit-error
- name: SAP Fieldglass Background Check API - OrderConfirmation
  property_count: 4
  slug: sap-fieldglass-bgcheck-orderconfirmation
- name: SAP Fieldglass Background Check API - ResultConfirmation
  property_count: 2
  slug: sap-fieldglass-bgcheck-resultconfirmation
- name: SAP Fieldglass OData-Based Analytic API - Data
  property_count: 1
  slug: sap-fieldglass-odata-data
- name: SAP Fieldglass OData-Based Analytic API - Error
  property_count: 0
  slug: sap-fieldglass-odata-error
- name: SAP Fieldglass OData-Based Analytic API - metaData
  property_count: 1
  slug: sap-fieldglass-odata-metadata
- name: SAP Fieldglass OData-Based Analytic API - Providers
  property_count: 0
  slug: sap-fieldglass-odata-providers
- name: SAP Fieldglass OData-Based Analytic API - ServiceURL
  property_count: 1
  slug: sap-fieldglass-odata-serviceurl
- name: SAP Fieldglass OData-Based Analytic API - Status
  property_count: 3
  slug: sap-fieldglass-odata-status
layout: provider
modified: '2026-08-21'
name: SAP Fieldglass
nav: Providers
network: true
overview: 'SAP Fieldglass publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Approval API, Audit Trail API, Get Data API, and 6 more. Tagged areas include Contingent Workforce, External Talent, HCM, Services Procurement, and Statements of Work.


  The SAP Fieldglass catalog on APIs.io includes 1 Spectral governance ruleset.


  SAP Fieldglass'' developer surface includes authentication, documentation, engineering blog, pricing, support, and 19 more developer resources.'
plans:
- name: Sap Fieldglass Plans Pricing
  plan_count: 1
  slug: sap-fieldglass-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Sap Fieldglass Rate Limits
  slug: sap-fieldglass-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: SAP Fieldglass API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: sap-fieldglass-jsonschema-spectral-rules
scopes:
- name: Sap Fieldglass Scopes
  scope_count: 1
  slug: sap-fieldglass-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 62.3
    catalog_earned_first_party: 0.0
    catalog_gap: 52.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 9.8
    contract_quality: 54.9
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 42.1
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sap-fieldglass/refs/heads/main/screenshots/sap-fieldglass-2026-06-20T193426.png
security:
- kind: authentication
  name: Sap Fieldglass Authentication
  slug: sap-fieldglass-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Sap Fieldglass Domain Security
  slug: sap-fieldglass-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sap Fieldglass Vulnerability Disclosure
  slug: sap-fieldglass-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sap-fieldglass
tags:
- Contingent Workforce
- External Talent
- HCM
- Services Procurement
- Statements of Work
- Vendor Management
- Workforce Management
use_cases:
- description: Create, manage, and track work orders for contingent workers through the full engagement lifecycle.
  name: Work Order Management
- description: Integrate services procurement statements of work with ERP and financial systems.
  name: Statement of Work Integration
- description: Access analytics and reporting data on external workforce spend, headcount, and performance.
  name: Workforce Analytics
- description: Automate worker onboarding and offboarding with SCIM-based identity management.
  name: Identity Provisioning
website: https://www.sap.com/products/hcm/contingent-workforce-management.html
---
