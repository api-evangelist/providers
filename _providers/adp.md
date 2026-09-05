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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 27.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Adp Agentic Access
  operation_count: 11
  slug: adp-agentic-access
  summary_line: 11 operations · 3 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The ADP Embedded Payroll API enables ISVs and platforms to embed ADP payroll capabilities directly into their applications. REST APIs support payroll processing, tax compliance, and workforce manageme
  name: ADP Embedded Payroll API
  slug: adp-embedded-payroll-api
- description: The ADP Benefits Administration API provides access to employee benefits enrollment, eligibility, and plan data. APIs support benefits carrier connectivity, open enrollment workflows, and benefits dat
  name: ADP Benefits Administration API
  slug: adp-benefits-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Organizational unit management
  name: ADP Organizations API
  slug: adp-organizations-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Payroll instructions and overrides
  name: ADP PayrollInstructions API
  slug: adp-payrollinstructions-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Payroll output and run data
  name: ADP PayrollOutputs API
  slug: adp-payrolloutputs-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker (employee) data access
  name: ADP Workers API
  slug: adp-workers-api
artifact_total: 112
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ADP Payroll Organizations API
  slug: open-adp-organizations-api
- collection_type: open
  name: ADP Payroll API
  slug: open-adp-payroll
- collection_type: open
  name: ADP Payroll Organizations PayrollInstructions API
  slug: open-adp-payrollinstructions-api
- collection_type: open
  name: ADP Payroll Organizations PayrollOutputs API
  slug: open-adp-payrolloutputs-api
- collection_type: open
  name: ADP Payroll Organizations Workers API
  slug: open-adp-workers-api
- collection_type: open
  name: ADP Workers API
  slug: open-adp-workers
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/adp-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adp-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/adp-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://www.adp.com/~/spark_feed/insights-trends
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adpllc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adp
- group: start
  title: ''
  type: Portal
  url: https://developers.adp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.adp.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.adp.com/getting-started/client-integration-overview
- group: auth
  title: ''
  type: Authentication
  url: https://developers.adp.com/getting-started/client-integration-overview
- group: docs
  title: ADP Workers OpenAPI
  type: OpenAPI
  url: openapi/_original/adp-workers-openapi.yml
- group: docs
  title: ADP Payroll OpenAPI
  type: OpenAPI
  url: openapi/_original/adp-payroll-openapi.yml
- group: docs
  title: ADP Worker JSON Schema
  type: JSONSchema
  url: json-schema/adp-worker-schema.json
- group: design
  title: ADP JSON-LD Context
  type: JSONLD
  url: json-ld/adp-context.jsonld
created: '2026-03-18'
description: ADP (Automatic Data Processing) is a global provider of cloud-based human capital management solutions including payroll, benefits, talent, time, tax, and HR services for businesses of all sizes.
examples:
- key_count: 2
  name: Adp Payroll Amount Value Example
  slug: adp-payroll-amount-value-example
- key_count: 2
  name: Adp Payroll Deduction Item Example
  slug: adp-payroll-deduction-item-example
- key_count: 3
  name: Adp Payroll Earning Item Example
  slug: adp-payroll-earning-item-example
- key_count: 1
  name: Adp Payroll Error Message Example
  slug: adp-payroll-error-message-example
- key_count: 4
  name: Adp Payroll Payroll Instruction Example
  slug: adp-payroll-payroll-instruction-example
- key_count: 4
  name: Adp Payroll Payroll Instruction Request Example
  slug: adp-payroll-payroll-instruction-request-example
- key_count: 3
  name: Adp Payroll Payroll Output Example
  slug: adp-payroll-payroll-output-example
- key_count: 1
  name: Adp Payroll Payroll Output Response Example
  slug: adp-payroll-payroll-output-response-example
- key_count: 4
  name: Adp Payroll Payroll Output Summary Example
  slug: adp-payroll-payroll-output-summary-example
- key_count: 2
  name: Adp Payroll Payroll Outputs Response Example
  slug: adp-payroll-payroll-outputs-response-example
- key_count: 3
  name: Adp Payroll Tax Item Example
  slug: adp-payroll-tax-item-example
- key_count: 1
  name: Adp Payroll Worker Outputs Response Example
  slug: adp-payroll-worker-outputs-response-example
- key_count: 9
  name: Adp Payroll Worker Pay Output Example
  slug: adp-payroll-worker-pay-output-example
- key_count: 6
  name: Adp Workers Address Example
  slug: adp-workers-address-example
- key_count: 2
  name: Adp Workers Confirm Message Example
  slug: adp-workers-confirm-message-example
- key_count: 3
  name: Adp Workers Department Example
  slug: adp-workers-department-example
- key_count: 1
  name: Adp Workers Event Response Example
  slug: adp-workers-event-response-example
- key_count: 5
  name: Adp Workers Person Example
  slug: adp-workers-person-example
- key_count: 10
  name: Adp Workers Work Assignment Example
  slug: adp-workers-work-assignment-example
- key_count: 5
  name: Adp Workers Worker Example
  slug: adp-workers-worker-example
- key_count: 1
  name: Adp Workers Worker Hire Event Example
  slug: adp-workers-worker-hire-event-example
- key_count: 1
  name: Adp Workers Worker Response Example
  slug: adp-workers-worker-response-example
- key_count: 1
  name: Adp Workers Worker Terminate Event Example
  slug: adp-workers-worker-terminate-event-example
- key_count: 2
  name: Adp Workers Workers Response Example
  slug: adp-workers-workers-response-example
features:
- description: Manage the complete worker lifecycle including hiring, onboarding, job changes, and termination through REST APIs.
  name: Worker Lifecycle Management
- description: Programmatic access to payroll runs, payroll output data, and compensation analysis across ADP platforms.
  name: Payroll Processing
- description: Embed ADP payroll capabilities directly into ISV and partner applications with white-label support.
  name: Embedded Payroll
- description: Manage employee benefits enrollment, eligibility, and plan data with carrier connectivity support.
  name: Benefits Administration
- description: Access department structures, organizational hierarchies, and work assignment data.
  name: Organizational Data
- description: Retrieve payroll and workforce data in CSV-formatted bulk exports for analytics and reporting.
  name: Bulk Data Export
finops:
- name: Adp Finops
  service_category: Human Capital Management
  slug: adp-finops
graphqls:
- description: 'ADP (Automatic Data Processing) provides cloud-based human capital management (HCM) solutions covering payroll, benefits, talent, time, tax, and HR services. This conceptual GraphQL schema represents '
  name: ADP GraphQL Schema
  slug: adp-graphql
integrations:
- description: Full integration with ADP Workforce Now for mid-market HR, payroll, talent, and benefits management.
  name: ADP Workforce Now
- description: Enterprise-grade HCM integration for large organizations with complex payroll and HR requirements.
  name: ADP Vantage HCM
- description: Payroll and HR integration for small businesses using the ADP RUN platform.
  name: ADP RUN Powered by ADP
json_schemas:
- name: AmountValue
  property_count: 2
  slug: adp-payroll-amount-value
- name: DeductionItem
  property_count: 2
  slug: adp-payroll-deduction-item
- name: EarningItem
  property_count: 3
  slug: adp-payroll-earning-item
- name: ErrorMessage
  property_count: 1
  slug: adp-payroll-error-message
- name: PayrollInstructionRequest
  property_count: 4
  slug: adp-payroll-payroll-instruction-request
- name: PayrollInstruction
  property_count: 4
  slug: adp-payroll-payroll-instruction
- name: PayrollOutputResponse
  property_count: 1
  slug: adp-payroll-payroll-output-response
- name: PayrollOutput
  property_count: 3
  slug: adp-payroll-payroll-output
- name: PayrollOutputSummary
  property_count: 4
  slug: adp-payroll-payroll-output-summary
- name: PayrollOutputsResponse
  property_count: 2
  slug: adp-payroll-payroll-outputs-response
- name: TaxItem
  property_count: 3
  slug: adp-payroll-tax-item
- name: WorkerOutputsResponse
  property_count: 1
  slug: adp-payroll-worker-outputs-response
- name: WorkerPayOutput
  property_count: 9
  slug: adp-payroll-worker-pay-output
- name: ADP Worker
  property_count: 6
  slug: adp-worker
- name: Address
  property_count: 6
  slug: adp-workers-address
- name: ConfirmMessage
  property_count: 2
  slug: adp-workers-confirm-message
- name: Department
  property_count: 3
  slug: adp-workers-department
- name: EventResponse
  property_count: 1
  slug: adp-workers-event-response
- name: Person
  property_count: 5
  slug: adp-workers-person
- name: WorkAssignment
  property_count: 10
  slug: adp-workers-work-assignment
- name: WorkerHireEvent
  property_count: 1
  slug: adp-workers-worker-hire-event
- name: WorkerResponse
  property_count: 1
  slug: adp-workers-worker-response
- name: Worker
  property_count: 5
  slug: adp-workers-worker
- name: WorkerTerminateEvent
  property_count: 1
  slug: adp-workers-worker-terminate-event
- name: WorkersResponse
  property_count: 2
  slug: adp-workers-workers-response
json_structures:
- name: Adp Payroll Amount Value Structure
  property_count: 2
  slug: adp-payroll-amount-value-structure
- name: Adp Payroll Deduction Item Structure
  property_count: 2
  slug: adp-payroll-deduction-item-structure
- name: Adp Payroll Earning Item Structure
  property_count: 3
  slug: adp-payroll-earning-item-structure
- name: Adp Payroll Error Message Structure
  property_count: 1
  slug: adp-payroll-error-message-structure
- name: Adp Payroll Payroll Instruction Request Structure
  property_count: 4
  slug: adp-payroll-payroll-instruction-request-structure
- name: Adp Payroll Payroll Instruction Structure
  property_count: 4
  slug: adp-payroll-payroll-instruction-structure
- name: Adp Payroll Payroll Output Response Structure
  property_count: 1
  slug: adp-payroll-payroll-output-response-structure
- name: Adp Payroll Payroll Output Structure
  property_count: 3
  slug: adp-payroll-payroll-output-structure
- name: Adp Payroll Payroll Output Summary Structure
  property_count: 4
  slug: adp-payroll-payroll-output-summary-structure
- name: Adp Payroll Payroll Outputs Response Structure
  property_count: 2
  slug: adp-payroll-payroll-outputs-response-structure
- name: Adp Payroll Tax Item Structure
  property_count: 3
  slug: adp-payroll-tax-item-structure
- name: Adp Payroll Worker Outputs Response Structure
  property_count: 1
  slug: adp-payroll-worker-outputs-response-structure
- name: Adp Payroll Worker Pay Output Structure
  property_count: 9
  slug: adp-payroll-worker-pay-output-structure
- name: Adp Workers Address Structure
  property_count: 6
  slug: adp-workers-address-structure
- name: Adp Workers Confirm Message Structure
  property_count: 2
  slug: adp-workers-confirm-message-structure
- name: Adp Workers Department Structure
  property_count: 3
  slug: adp-workers-department-structure
- name: Adp Workers Event Response Structure
  property_count: 1
  slug: adp-workers-event-response-structure
- name: Adp Workers Person Structure
  property_count: 5
  slug: adp-workers-person-structure
- name: Adp Workers Work Assignment Structure
  property_count: 10
  slug: adp-workers-work-assignment-structure
- name: Adp Workers Worker Hire Event Structure
  property_count: 1
  slug: adp-workers-worker-hire-event-structure
- name: Adp Workers Worker Response Structure
  property_count: 1
  slug: adp-workers-worker-response-structure
- name: Adp Workers Worker Structure
  property_count: 5
  slug: adp-workers-worker-structure
- name: Adp Workers Worker Terminate Event Structure
  property_count: 1
  slug: adp-workers-worker-terminate-event-structure
- name: Adp Workers Workers Response Structure
  property_count: 2
  slug: adp-workers-workers-response-structure
jsonld:
- class_count: 0
  name: Adp Context
  property_count: 5
  slug: adp-context
- class_count: 0
  name: Adp Payroll Context
  property_count: 0
  slug: adp-payroll-context
- class_count: 0
  name: Adp Workers Context
  property_count: 0
  slug: adp-workers-context
layout: provider
modified: '2026-05-19'
name: ADP
nav: Providers
network: true
overview: 'ADP publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Organizations API, PayrollInstructions API, PayrollOutputs API, and 1 more. Tagged areas include Benefits, HCM, HR, Payroll, and Workforce.


  The ADP catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  ADP''s developer surface includes authentication, engineering blog, developer portal, documentation, getting-started guide, and 11 more developer resources.'
plans:
- name: Adp Plans Pricing
  plan_count: 2
  slug: adp-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Adp Rate Limits
  slug: adp-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: ADP API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: adp-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: ADP API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 5
  slug: adp-spectral-rules
scopes:
- name: Adp Scopes
  scope_count: 3
  slug: adp-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.5
    catalog_earned_first_party: 0.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 68.4
    developer_ergonomics: 11.9
    discoverability: 55.6
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 30.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/screenshots/adp-2026-06-20T165046.png
security:
- kind: authentication
  name: Adp Authentication
  slug: adp-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Adp Domain Security
  slug: adp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adp
tags:
- Benefits
- HCM
- HR
- Payroll
- Workforce
use_cases:
- description: Synchronize worker data between ADP and third-party HRIS, ERP, and workforce management systems.
  name: HCM Integration
- description: Automate payroll instruction submission and output retrieval for streamlined payroll processing workflows.
  name: Payroll Automation
- description: Extract headcount, compensation, and departmental data for workforce planning and business intelligence.
  name: Workforce Analytics
- description: Integrate ADP payroll processing directly into partner software applications for small business customers.
  name: ISV Embedded Payroll
website: https://developers.adp.com/
---
