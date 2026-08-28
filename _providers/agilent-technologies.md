---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    auth_clarity: bearer
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
  score: 30.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Agilent Technologies Agentic Access
  operation_count: 11
  slug: agilent-technologies-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 10
apis:
- description: The SLIMS (Smart Laboratory Information Management System) REST API provides programmatic access to Agilent SLIMS laboratory data management platform. SLIMS features three APIs — REST, Java, and Pytho
  name: Agilent SLIMS REST API
  slug: agilent-slims-rest-api
- description: The CrossLab Asset Manager API provides programmatic access to Agilent's CrossLab instrument services platform, enabling management of laboratory assets, instrument service records, maintenance schedu
  name: Agilent CrossLab Asset Manager API
  slug: agilent-crosslab-asset-manager-api
- description: The VWorks API provides a Component Object Model (COM) application programming interface for VWorks laboratory automation software (version 14.0 and later). It enables programmatic control of laborato
  name: Agilent VWorks Automation API
  slug: agilent-vworks-automation-api
- description: Core facility resources — the root resource of the API
  name: agilent-technologies Cores API
  slug: agilent-technologies-cores-api
- description: Billing invoices and financial records
  name: agilent-technologies Invoices API
  slug: agilent-technologies-invoices-api
- description: Core facility membership and user management
  name: agilent-technologies Members API
  slug: agilent-technologies-members-api
- description: Research projects and cost accounts
  name: agilent-technologies Projects API
  slug: agilent-technologies-projects-api
- description: Equipment reservations and scheduling
  name: agilent-technologies Reservations API
  slug: agilent-technologies-reservations-api
- description: Service request submissions and management
  name: agilent-technologies Service Requests API
  slug: agilent-technologies-service-requests-api
- description: Services and price lists offered by a core facility
  name: agilent-technologies Services API
  slug: agilent-technologies-services-api
artifact_total: 103
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Agilent iLab Operations Cores API
  slug: open-agilent-technologies-cores-api
- collection_type: open
  name: Agilent iLab Operations Cores Invoices API
  slug: open-agilent-technologies-invoices-api
- collection_type: open
  name: Agilent iLab Operations Cores Members API
  slug: open-agilent-technologies-members-api
- collection_type: open
  name: Agilent iLab Operations Cores Projects API
  slug: open-agilent-technologies-projects-api
- collection_type: open
  name: Agilent iLab Operations Cores Reservations API
  slug: open-agilent-technologies-reservations-api
- collection_type: open
  name: Agilent iLab Operations Cores Service Requests API
  slug: open-agilent-technologies-service-requests-api
- collection_type: open
  name: Agilent iLab Operations Cores Services API
  slug: open-agilent-technologies-services-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agilent-technologies-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agilent-technologies-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agilent-technologies-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agilent-technologies
- group: company
  title: ''
  type: Website
  url: https://www.agilent.com/en
- group: operate
  title: ''
  type: Support
  url: https://www.agilent.com/en/support
- group: operate
  title: ''
  type: Community
  url: https://community.agilent.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Agilent
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agilent.com/en/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agilent.com/en/privacy-statement
- group: design
  title: ''
  type: SpectralRules
  url: rules/agilent-technologies-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/agilent-technologies-vocabulary.yaml
description: Agilent Technologies is a global leader in life sciences, diagnostics, and applied chemical markets, providing instruments, software, services, and consumables for laboratory workflows. Agilent offers APIs for laboratory operations management including iLab for core facility billing and scheduling, SLIMS for laboratory information management, CrossLab Asset Manager for instrument management, and VWorks for laboratory automation.
examples:
- key_count: 7
  name: Ilab Operations Api Core Example
  slug: ilab-operations-api-core-example
- key_count: 4
  name: Ilab Operations Api Cores List Response Example
  slug: ilab-operations-api-cores-list-response-example
- key_count: 3
  name: Ilab Operations Api Error Response Example
  slug: ilab-operations-api-error-response-example
- key_count: 6
  name: Ilab Operations Api Invoice Example
  slug: ilab-operations-api-invoice-example
- key_count: 1
  name: Ilab Operations Api Invoices List Response Example
  slug: ilab-operations-api-invoices-list-response-example
- key_count: 5
  name: Ilab Operations Api Member Example
  slug: ilab-operations-api-member-example
- key_count: 1
  name: Ilab Operations Api Members List Response Example
  slug: ilab-operations-api-members-list-response-example
- key_count: 5
  name: Ilab Operations Api Price Example
  slug: ilab-operations-api-price-example
- key_count: 2
  name: Ilab Operations Api Price Update Request Example
  slug: ilab-operations-api-price-update-request-example
- key_count: 1
  name: Ilab Operations Api Prices List Response Example
  slug: ilab-operations-api-prices-list-response-example
- key_count: 5
  name: Ilab Operations Api Project Example
  slug: ilab-operations-api-project-example
- key_count: 1
  name: Ilab Operations Api Projects List Response Example
  slug: ilab-operations-api-projects-list-response-example
- key_count: 5
  name: Ilab Operations Api Reservation Example
  slug: ilab-operations-api-reservation-example
- key_count: 1
  name: Ilab Operations Api Reservations List Response Example
  slug: ilab-operations-api-reservations-list-response-example
- key_count: 5
  name: Ilab Operations Api Service Example
  slug: ilab-operations-api-service-example
- key_count: 4
  name: Ilab Operations Api Service Request Create Request Example
  slug: ilab-operations-api-service-request-create-request-example
- key_count: 8
  name: Ilab Operations Api Service Request Example
  slug: ilab-operations-api-service-request-example
- key_count: 1
  name: Ilab Operations Api Service Requests List Response Example
  slug: ilab-operations-api-service-requests-list-response-example
- key_count: 1
  name: Ilab Operations Api Services List Response Example
  slug: ilab-operations-api-services-list-response-example
features:
- description: iLab and CrossLab APIs leverage RESTful architecture with HATEOAS for discoverable resource navigation.
  name: RESTful Architecture
- description: Secure access to APIs via OAuth2 with client ID and API token-based authentication.
  name: OAuth2 Authentication
- description: Pre-built integration support for SAP, Oracle/PeopleSoft, Lawson, and Banner financial systems.
  name: Financial System Integration
- description: Integration with laboratory information management systems for sample tracking and results management.
  name: LIMS Integration
- description: Ability to import usage logs and data directly from connected laboratory instruments.
  name: Instrument Data Import
- description: SLIMS supports custom plugin development via Java and Python APIs for workflow extension.
  name: Plugin Architecture
- description: SLIMS REST API documentation is automatically generated from each deployed instance.
  name: Auto-Generated API Documentation
finops:
- name: Agilent Technologies Finops
  service_category: Life Sciences / Lab Software
  slug: agilent-technologies-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agilent-technologies.png
integrations:
- description: Financial system integration for billing and cost accounting via iLab API.
  name: SAP
- description: ERP integration for institutional billing and financial reporting.
  name: Oracle PeopleSoft
- description: Financial management system integration for laboratory billing workflows.
  name: Lawson
- description: Higher education ERP integration for core facility cost center management.
  name: Banner
- description: Integration between Agilent instruments and LabWare LIMS for data transfer and workflow coordination.
  name: LabWare LIMS
- description: Integration with institutional identity providers for single sign-on and user provisioning.
  name: Identity Management Systems
json_schemas:
- name: Core
  property_count: 7
  slug: ilab-operations-api-core
- name: Cores List Response
  property_count: 4
  slug: ilab-operations-api-cores-list-response
- name: Error Response
  property_count: 3
  slug: ilab-operations-api-error-response
- name: Invoice
  property_count: 6
  slug: ilab-operations-api-invoice
- name: Invoices List Response
  property_count: 1
  slug: ilab-operations-api-invoices-list-response
- name: Member
  property_count: 5
  slug: ilab-operations-api-member
- name: Members List Response
  property_count: 1
  slug: ilab-operations-api-members-list-response
- name: Price
  property_count: 5
  slug: ilab-operations-api-price
- name: Price Update Request
  property_count: 2
  slug: ilab-operations-api-price-update-request
- name: Prices List Response
  property_count: 1
  slug: ilab-operations-api-prices-list-response
- name: Project
  property_count: 5
  slug: ilab-operations-api-project
- name: Projects List Response
  property_count: 1
  slug: ilab-operations-api-projects-list-response
- name: Reservation
  property_count: 5
  slug: ilab-operations-api-reservation
- name: Reservations List Response
  property_count: 1
  slug: ilab-operations-api-reservations-list-response
- name: Service Request Create Request
  property_count: 4
  slug: ilab-operations-api-service-request-create-request
- name: Service Request
  property_count: 8
  slug: ilab-operations-api-service-request
- name: Service Requests List Response
  property_count: 1
  slug: ilab-operations-api-service-requests-list-response
- name: Service
  property_count: 5
  slug: ilab-operations-api-service
- name: Services List Response
  property_count: 1
  slug: ilab-operations-api-services-list-response
json_structures:
- name: Ilab Operations Api Core Structure
  property_count: 7
  slug: ilab-operations-api-core-structure
- name: Ilab Operations Api Cores List Response Structure
  property_count: 4
  slug: ilab-operations-api-cores-list-response-structure
- name: Ilab Operations Api Error Response Structure
  property_count: 3
  slug: ilab-operations-api-error-response-structure
- name: Ilab Operations Api Invoice Structure
  property_count: 6
  slug: ilab-operations-api-invoice-structure
- name: Ilab Operations Api Invoices List Response Structure
  property_count: 1
  slug: ilab-operations-api-invoices-list-response-structure
- name: Ilab Operations Api Member Structure
  property_count: 5
  slug: ilab-operations-api-member-structure
- name: Ilab Operations Api Members List Response Structure
  property_count: 1
  slug: ilab-operations-api-members-list-response-structure
- name: Ilab Operations Api Price Structure
  property_count: 5
  slug: ilab-operations-api-price-structure
- name: Ilab Operations Api Price Update Request Structure
  property_count: 2
  slug: ilab-operations-api-price-update-request-structure
- name: Ilab Operations Api Prices List Response Structure
  property_count: 1
  slug: ilab-operations-api-prices-list-response-structure
- name: Ilab Operations Api Project Structure
  property_count: 5
  slug: ilab-operations-api-project-structure
- name: Ilab Operations Api Projects List Response Structure
  property_count: 1
  slug: ilab-operations-api-projects-list-response-structure
- name: Ilab Operations Api Reservation Structure
  property_count: 5
  slug: ilab-operations-api-reservation-structure
- name: Ilab Operations Api Reservations List Response Structure
  property_count: 1
  slug: ilab-operations-api-reservations-list-response-structure
- name: Ilab Operations Api Service Request Create Request Structure
  property_count: 4
  slug: ilab-operations-api-service-request-create-request-structure
- name: Ilab Operations Api Service Request Structure
  property_count: 8
  slug: ilab-operations-api-service-request-structure
- name: Ilab Operations Api Service Requests List Response Structure
  property_count: 1
  slug: ilab-operations-api-service-requests-list-response-structure
- name: Ilab Operations Api Service Structure
  property_count: 5
  slug: ilab-operations-api-service-structure
- name: Ilab Operations Api Services List Response Structure
  property_count: 1
  slug: ilab-operations-api-services-list-response-structure
jsonld:
- class_count: 23
  name: Agilent Ilab Operations Api Context
  property_count: 37
  slug: agilent-ilab-operations-api-context
layout: provider
modified: '2026-05-19'
name: agilent-technologies
nav: Providers
network: true
overview: 'agilent-technologies publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Cores API, Invoices API, Members API, and 4 more. Tagged areas include Fortune 500, Life Sciences, Diagnostics, Laboratory, and Scientific Instruments.


  The agilent-technologies catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  agilent-technologies'' developer surface includes authentication, support, and 10 more developer resources.'
plans:
- name: Agilent Technologies Plans Pricing
  plan_count: 1
  slug: agilent-technologies-plans-pricing
press:
- date: '2026-05-25'
  title: Latest A News - Agilent Acquires Artificial Intelligence Techn...
  url: https://www.stocktitan.net/news/A/page-30.html
- date: '2026-05-25'
  title: Agilent Acquires Artificial Intelligence Technology to ...
  url: https://www.agilent.com/about/newsroom/presrel/2022/17feb-gp22004.html?srsltid=AfmBOoopyXeP_F_3H7w_Drtjkn4uL5JTMPDo3ofoYLBhOKNGyCDZrSmP
- date: '2026-05-25'
  title: Press Releases
  url: https://www.agilent.com/about/newsroom/presrel.html?cat=corporate&start=1&page=1&srsltid=AfmBOorb-8haBtodoHEkxyD5ndka2TYQoOjrCQVclI0F0lmO7BfAXJY2
- date: '2026-05-25'
  title: Unlock the lab of the future with Agilent's Digital ...
  url: https://www.facebook.com/Agilent.Tech/posts/unlock-the-lab-of-the-future-with-agilents-digital-lab-solutions-our-open-and-co/923676106457953/
- date: '2026-05-25'
  title: Lunit and Agilent Technologies Announce Collaboration to ...
  url: https://www.prnewswire.com/news-releases/lunit-and-agilent-technologies-announce-collaboration-to-enhance-development-of-companion-diagnostic-solutions-powered-with-ai-for-precision-medicine-302562617.html
random_paper: 11
rate_limits:
- limit_count: 1
  name: Agilent Technologies Rate Limits
  slug: agilent-technologies-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: agilent-technologies API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: agilent-technologies-jsonschema-spectral-rules
- effective_rule_count: 82
  extends:
  - spectral:oas
  name: agilent-technologies API Rules
  rule_count: 41
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 27
  slug: agilent-technologies-spectral-rules
score:
  band: thin
  composite: 33.8
  delta: 3.3
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 28.8
    contract_quality: 28.5
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agilent-technologies/refs/heads/main/screenshots/agilent-technologies-2026-07-25T195311.png
security:
- kind: authentication
  name: Agilent Technologies Authentication
  slug: agilent-technologies-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agilent Technologies Domain Security
  slug: agilent-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: agilent-technologies
tags:
- Fortune 500
- Life Sciences
- Diagnostics
- Laboratory
- Scientific Instruments
- LIMS
- Laboratory Automation
use_cases:
- description: Automate billing workflows between iLab core facilities and institutional financial systems such as SAP or Oracle.
  name: Core Facility Billing Automation
- description: Integrate external scheduling applications with iLab's equipment reservation and usage tracking.
  name: Laboratory Scheduling Integration
- description: Use the SLIMS API to track samples from receipt through analysis and reporting across NGS, biobank, and R&D workflows.
  name: Sample Lifecycle Management
- description: Manage laboratory instrument service records, calibration schedules, and compliance documentation via CrossLab Asset Manager API.
  name: Instrument Asset Tracking
- description: Programmatically control VWorks-driven liquid handling robots and integrated workstations for high-throughput workflows.
  name: Automation Workflow Control
- description: Extract and aggregate laboratory data from SLIMS for custom reporting and business intelligence integrations.
  name: LIMS Data Reporting
website: https://www.agilent.com/en
---
