---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.3
  scored_at: '2026-08-30'
api_count: 27
apis:
- description: Workday is a cloud HCM, payroll, and finance suite with a Web Services / REST API catalog spanning Human Capital Management, Payroll, Recruiting, Talent, and Time Tracking.
  name: Workday
  slug: workday
- description: BambooHR is a cloud HRIS for small and mid-size companies with a REST API for employee records, time off, reports, and webhooks.
  name: BambooHR
  slug: bamboohr
- description: Rippling is a workforce platform unifying HR, IT, and Finance with a public REST API covering employees, payroll, devices, and apps.
  name: Rippling
  slug: rippling
- description: Gusto is a payroll, benefits, and HR platform for small business with a partner REST API for embedded payroll and HR.
  name: Gusto
  slug: gusto
- description: Justworks is a PEO platform providing payroll, benefits, and compliance with an HRIS API for partners and integrations.
  name: Justworks
  slug: justworks
- description: Paylocity is a cloud payroll and HCM provider with a REST Web Services API for employees, payroll, benefits, time, and labor cost.
  name: Paylocity
  slug: paylocity
- description: ADP is the largest payroll and HCM provider with the ADP Marketplace and ADP Workforce Now / Run / Vantage APIs for HR, payroll, time, and benefits.
  name: ADP
  slug: adp
- description: UKG provides UKG Pro and UKG Ready HCM, workforce management, and payroll with a REST API and integration marketplace.
  name: UKG (Ultimate Kronos Group)
  slug: ukg
- description: Sage People is a global cloud HR system built on the Salesforce platform with a REST API for workers, employment, leave, and reviews.
  name: Sage People
  slug: sage-people
- description: Personio is a European all-in-one HR software for SMBs with a REST API for employees, attendance, absences, and applicants.
  name: Personio
  slug: personio
- description: HiBob is a modern HRIS with a REST API for people data, time off, lifecycle events, performance, and compensation.
  name: HiBob
  slug: hibob
- description: Namely is a mid-market HRIS with a REST API covering profiles, time off, benefits, and payroll.
  name: Namely
  slug: namely
- description: Merge is a unified API platform whose HRIS Unified API normalizes employee, employment, group, time-off, and payroll data across dozens of HRIS systems.
  name: Merge HRIS
  slug: merge
- description: Finch is a unified API for employment systems (HRIS and payroll) covering employee, company, payment, pay-statement, and directory endpoints across hundreds of providers.
  name: Finch
  slug: finch
- description: Kombo is a European unified HR API normalizing employees, employments, absences, candidates, jobs, and offers across HRIS and ATS providers.
  name: Kombo
  slug: kombo
- description: Greenhouse is an applicant tracking and recruiting platform with Harvest, Job Board, and Onboarding APIs for candidates, applications, jobs, and offers.
  name: Greenhouse
  slug: greenhouse
- description: Lever is a talent acquisition platform whose API covers candidates, opportunities, postings, requisitions, interviews, and offers.
  name: Lever
  slug: lever
- description: Workable is a recruiting platform with a REST API for jobs, candidates, activities, comments, and offers, plus a partner marketplace.
  name: Workable
  slug: workable
- description: SmartRecruiters is an enterprise talent acquisition suite with a REST API for candidates, postings, applications, offers, and onboarding.
  name: SmartRecruiters
  slug: smartrecruiters
- description: Ashby is an all-in-one talent platform with a REST API for candidates, applications, interviews, offers, jobs, and feedback.
  name: Ashby
  slug: ashby
- description: Lattice is a people-management platform covering performance, engagement, goals, growth, and compensation with a partner API.
  name: Lattice
  slug: lattice
- description: Culture Amp is an employee experience platform for engagement, performance, and development with a partner API and integrations marketplace.
  name: Culture Amp
  slug: culture-amp
- description: 15Five is a continuous performance management platform covering check-ins, OKRs, reviews, and engagement, with an API for HRIS-driven user sync.
  name: 15Five
  slug: 15five
- description: LinkedIn Talent Solutions provides Recruiter System Connect, Job Posting, Apply-with-LinkedIn, and Talent Hub APIs for talent acquisition and people data integration.
  name: LinkedIn Talent Solutions
  slug: linkedin-talent-solutions
- description: HiPeople is a talent assessment and reference-checking platform with an API for assessments, reference reports, and candidate insights.
  name: HiPeople
  slug: hipeople
- description: Compa is a real-time compensation intelligence platform for talent acquisition teams, providing offer-level pay benchmarks via API.
  name: Compa
  slug: compa
- description: OpenComp is a compensation planning platform offering pay benchmarks, pay equity, and compensation review tools, with HRIS-driven sync and an API.
  name: OpenComp
  slug: opencomp
artifact_total: 52
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/hr-and-people-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hr-and-people-domain-security.yml
- group: other
  title: ''
  type: APIEvangelistTopic
  url: https://github.com/api-evangelist/hr-and-people
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hr-and-people-employee-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hr-and-people-employment-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/hr-and-people-employee-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hr-and-people-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/hr-and-people-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/hr-and-people-employee-example.json
- group: build
  title: ''
  type: Examples
  url: examples/hr-and-people-employment-example.json
created: '2026-05-23'
description: API and integration profile for the HR and people-operations landscape. This topic repo catalogs the API surface of HRIS systems, unified HR APIs, payroll providers, talent acquisition platforms, performance and engagement tools, and people-data services. The focus is a portable Employee record schema (JSON Schema), schema.org/Person aligned semantics (JSON-LD), and a shared vocabulary for the people-operations domain.
examples:
- key_count: 35
  name: Hr And People Employee Example
  slug: hr-and-people-employee-example
- key_count: 21
  name: Hr And People Employment Example
  slug: hr-and-people-employment-example
features:
- description: Portable JSON Schema for an Employee record covering identity, employment, compensation, and lifecycle fields shared across HRIS systems
  name: Employee Record Schema
- description: JSON-LD context aligning the Employee vocabulary with schema.org/Person and schema.org/EmployeeRole for linked-data interoperability
  name: Schema.org Person Alignment
- description: Catalog of HRIS, unified HR, payroll, ATS, performance, and people-data API providers with links to their developer documentation
  name: HR Provider Catalog
- description: Includes the major unified-HRIS API platforms (Merge, Finch, Kombo) that normalize employee data across dozens of underlying HRIS and payroll systems
  name: Unified HRIS Coverage
- description: Shared vocabulary mapping employee, employment, compensation, time-off, performance, and recruiting concepts across the HR landscape
  name: People Operations Vocabulary
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hr-and-people.png
integrations:
- description: Workday, BambooHR, Rippling, Gusto, Justworks, Paylocity, ADP, UKG, Sage People, Personio, HiBob, Namely
  name: HRIS Providers
- description: Merge HRIS, Finch, Kombo
  name: Unified HRIS APIs
- description: Greenhouse, Lever, Workable, SmartRecruiters, Ashby
  name: Applicant Tracking
- description: Lattice, Culture Amp, 15Five
  name: Performance and Engagement
- description: LinkedIn Talent Solutions, HiPeople, Compa, OpenComp
  name: People Data and Compensation
json_schemas:
- name: Employee
  property_count: 40
  slug: hr-and-people-employee
- name: Employment
  property_count: 21
  slug: hr-and-people-employment
json_structures:
- name: Hr And People Employee Structure
  property_count: 0
  slug: hr-and-people-employee-structure
jsonld:
- class_count: 11
  name: Hr And People Context
  property_count: 46
  slug: hr-and-people-context
layout: provider
modified: '2026-05-23'
name: HR & People
nav: Providers
network: true
overview: 'HR & People publishes 27 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include HR, HRIS, People Operations, Payroll, and Talent Acquisition.


  The HR & People catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  HR & People''s developer surface includes code examples and 9 more developer resources.'
random_paper: 0
rules:
- effective_rule_count: 5
  extends: []
  name: HR & People API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: hr-and-people-jsonschema-spectral-rules
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 60.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 25.0
    contract_quality: 21.3
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 16.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hr-and-people/refs/heads/main/screenshots/hr-and-people-2026-06-20T182901.png
security:
- kind: domain-security
  name: Hr And People Domain Security
  slug: hr-and-people-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Hr And People Trust Center
  slug: hr-and-people-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: hr-and-people
tags:
- HR
- HRIS
- People Operations
- Payroll
- Talent Acquisition
- Performance Management
- Employee Engagement
- People Data
- Workforce Management
- Unified-API
use_cases:
- description: Map a customer's HRIS data into a normalized Employee record for downstream consumers (provisioning, analytics, compensation, security)
  name: HRIS Integration Mapping
- description: Catalog ATS and recruiting APIs feeding candidate, application, offer, and hire data into an HRIS or data warehouse
  name: Talent Acquisition Pipeline
- description: Build a people-data warehouse keyed on the Employee schema, joining HRIS, payroll, performance, and engagement records
  name: People Data Warehouse
- description: Combine HRIS employee/compensation records with compensation-intelligence APIs (Compa, OpenComp) for offer and review benchmarks
  name: Compensation Benchmarking
- description: Drive identity and access lifecycle off HRIS lifecycle events (hire, transfer, termination) via webhooks or unified-API event streams
  name: Joiner-Mover-Leaver Automation
- description: Provide governed AI capabilities (resume parsing, offer generation, compensation analysis, headcount planning) grounded in the Employee schema
  name: AI Capabilities for HR Workflows
---
