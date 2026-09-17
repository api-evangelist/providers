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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.5
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 171
  human_in_the_loop: 3
  name: Adp Agentic Access
  operation_count: 373
  slug: adp-agentic-access
  summary_line: 373 operations · 171 acting · 3 human-in-the-loop
api_count: 61
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
  description: Worker (employee) data access
  name: ADP Workers API
  slug: adp-workers-api
- description: ADP's change-data-capture surface. When data changes in an ADP product ADP generates an event notification and delivers it either into the subscriber's FIFO message queue, drained with GET/DELETE /cor
  name: ADP Event Notifications API
  slug: event-notifications-api
- description: ADP Embedded Payroll lets a software platform embed complete RUN Powered by ADP payroll screens — "Journeys" for People, Payroll, Reports, Taxes, Onboarding and Settings — inside its own product via a
  name: ADP Embedded Payroll (RUN)
  slug: embedded-payroll
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: A worker additional remuneration add management
  name: ADP Add Additional Remuneration API
  slug: adp-add-additional-remuneration-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal contact add management events.
  name: ADP Add Personal Contact API
  slug: adp-add-personal-contact-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Work schedule add day management events
  name: ADP Add Schedule Day API
  slug: adp-add-schedule-day-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Add a new work assignment
  name: ADP Add Work Assignment API
  slug: adp-add-work-assignment-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Work schedule add management events
  name: ADP Add Work Schedule API
  slug: adp-add-work-schedule-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker business communication email add management events.
  name: ADP Add Worker Business Email API
  slug: adp-add-worker-business-email-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker business communication fax add management events.
  name: ADP Add Worker Business Fax API
  slug: adp-add-worker-business-fax-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker business communication landline add management events.
  name: ADP Add Worker Business Landline API
  slug: adp-add-worker-business-landline-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker business communication mobile add management events.
  name: ADP Add Worker Business Mobile API
  slug: adp-add-worker-business-mobile-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker business communication pager add management events.
  name: ADP Add Worker Business Pager API
  slug: adp-add-worker-business-pager-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker government id add management events
  name: ADP Add Worker Government ID API
  slug: adp-add-worker-government-id-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker legal address add management events
  name: ADP Add Worker Legal Address API
  slug: adp-add-worker-legal-address-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal address add management events
  name: ADP Add Worker Personal Address API
  slug: adp-add-worker-personal-address-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal communication email add management events.
  name: ADP Add Worker Personal Email API
  slug: adp-add-worker-personal-email-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal communication fax add management events.
  name: ADP Add Worker Personal Fax API
  slug: adp-add-worker-personal-fax-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal communication landline add management events.
  name: ADP Add Worker Personal Landline API
  slug: adp-add-worker-personal-landline-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal communication mobile add management events.
  name: ADP Add Worker Personal Mobile API
  slug: adp-add-worker-personal-mobile-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal communication pager add management events.
  name: ADP Add Worker Personal Pager API
  slug: adp-add-worker-personal-pager-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: API to manage the applicant's assessment by the external agency
  name: ADP Applicant's External Assessment API
  slug: adp-applicant-s-external-assessment-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: API to manage the applicant's background screening by the external agency
  name: ADP Applicant's External Screening API
  slug: adp-applicant-s-external-screening-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: APIs to manage associate preferred gender pronoun
  name: ADP Associate Preferred Gender Pronoun API
  slug: adp-associate-preferred-gender-pronoun-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Validation Table - Associate Work Locations
  name: ADP Associate Work Locations API
  slug: adp-associate-work-locations-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List all beneficiaries
  name: ADP Beneficiaries API
  slug: adp-beneficiaries-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Validation Table - Business Units
  name: ADP Business Units API
  slug: adp-business-units-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker cancel worker leave management events.
  name: ADP Cancel Worker Leave API
  slug: adp-cancel-worker-leave-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Organization certification add management events.
  name: ADP Certification Add API
  slug: adp-certification-add-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Organization certification change management events.
  name: ADP Certification Change API
  slug: adp-certification-change-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Organization certification remove management events.
  name: ADP Certification Remove API
  slug: adp-certification-remove-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List all certifications
  name: ADP Certifications API
  slug: adp-certifications-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: A worker additional remuneration change management
  name: ADP Change Additional Remuneration API
  slug: adp-change-additional-remuneration-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: A worker base remuneration change management
  name: ADP Change Base Remuneration API
  slug: adp-change-base-remuneration-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker's birth date change management events.
  name: ADP Change Birth Date API
  slug: adp-change-birth-date-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker birth name change management events.
  name: ADP Change Birth Name API
  slug: adp-change-birth-name-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker's gender change management events.
  name: ADP Change Gender API
  slug: adp-change-gender-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker legal name change management events.
  name: ADP Change Legal Name API
  slug: adp-change-legal-name-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Pay distribution change management events
  name: ADP Change Pay Distribution API
  slug: adp-change-pay-distribution-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker person amount custom field management
  name: ADP Change Person Custom Amount API
  slug: adp-change-person-custom-amount-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker person code custom field management
  name: ADP Change Person Custom Code API
  slug: adp-change-person-custom-code-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker person date custom field management
  name: ADP Change Person Custom Date API
  slug: adp-change-person-custom-date-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker person indicator custom field management
  name: ADP Change Person Custom Indicator API
  slug: adp-change-person-custom-indicator-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker person number custom field management
  name: ADP Change Person Custom Number API
  slug: adp-change-person-custom-number-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker person percentage custom field management
  name: ADP Change Person Custom Percentage API
  slug: adp-change-person-custom-percentage-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker person string custom field management
  name: ADP Change Person Custom String API
  slug: adp-change-person-custom-string-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker person telephone custom field management
  name: ADP Change Person Custom Telephone API
  slug: adp-change-person-custom-telephone-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal contact change management events.
  name: ADP Change Personal Contact API
  slug: adp-change-personal-contact-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker preferred name change management events.
  name: ADP Change Preferred Name API
  slug: adp-change-preferred-name-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker's race change management events.
  name: ADP Change Race API
  slug: adp-change-race-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Work schedule change day management events
  name: ADP Change Schedule Day API
  slug: adp-change-schedule-day-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Work schedule change entry management events
  name: ADP Change Schedule Entry API
  slug: adp-change-schedule-entry-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: A worker standard hours change management
  name: ADP Change Standard Hours API
  slug: adp-change-standard-hours-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Work schedule change management events
  name: ADP Change Work Schedule API
  slug: adp-change-work-schedule-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker business communication email change management events.
  name: ADP Change Worker Business Email API
  slug: adp-change-worker-business-email-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker business communication fax change management events.
  name: ADP Change Worker Business Fax API
  slug: adp-change-worker-business-fax-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker business communication landline change management events.
  name: ADP Change Worker Business Landline API
  slug: adp-change-worker-business-landline-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker business communication mobile change management events.
  name: ADP Change Worker Business Mobile API
  slug: adp-change-worker-business-mobile-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker business communication pager change management events.
  name: ADP Change Worker Business Pager API
  slug: adp-change-worker-business-pager-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker percentage custom field management
  name: ADP Change Worker Custom Percentage API
  slug: adp-change-worker-custom-percentage-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker telephone custom field management
  name: ADP Change Worker Custom Telephone API
  slug: adp-change-worker-custom-telephone-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker change worker gender identity management events.
  name: ADP Change Worker Gender Identity API
  slug: adp-change-worker-gender-identity-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker government id change management events
  name: ADP Change Worker Government ID API
  slug: adp-change-worker-government-id-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker person highest level educational change management events.
  name: ADP Change Worker Highest Education Level API
  slug: adp-change-worker-highest-education-level-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker change worker leave management events.
  name: ADP Change Worker Leave API
  slug: adp-change-worker-leave-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker legal address change management events
  name: ADP Change Worker Legal Address API
  slug: adp-change-worker-legal-address-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker person marital status change management events.
  name: ADP Change Worker Marital Status API
  slug: adp-change-worker-marital-status-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker person military classification change management events.
  name: ADP Change Worker Military Classification API
  slug: adp-change-worker-military-classification-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker person military status change management events.
  name: ADP Change Worker Military Status API
  slug: adp-change-worker-military-status-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal address management events
  name: ADP Change Worker Personal Address API
  slug: adp-change-worker-personal-address-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal communication email change management events.
  name: ADP Change Worker Personal Email API
  slug: adp-change-worker-personal-email-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal communication fax change management events.
  name: ADP Change Worker Personal Fax API
  slug: adp-change-worker-personal-fax-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal communication landline change management events.
  name: ADP Change Worker Personal Landline API
  slug: adp-change-worker-personal-landline-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal communication mobile change management events.
  name: ADP Change Worker Personal Mobile API
  slug: adp-change-worker-personal-mobile-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal communication pager change management events.
  name: ADP Change Worker Personal Pager API
  slug: adp-change-worker-personal-pager-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: An instance to capture the work assignment worker type change event.
  name: ADP Change Worker Type API
  slug: adp-change-worker-type-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker compensation data APIs, e.g. pay history, regular and vairiable compensation details
  name: ADP Compensation Management API
  slug: adp-compensation-management-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List all competencies
  name: ADP Competencies API
  slug: adp-competencies-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Organization competency add management events.
  name: ADP Competency Add API
  slug: adp-competency-add-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Organization competency change management events.
  name: ADP Competency Change API
  slug: adp-competency-change-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Organization competency remove management events.
  name: ADP Competency Remove API
  slug: adp-competency-remove-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Work schedule copy day management events
  name: ADP Copy Schedule Day API
  slug: adp-copy-schedule-day-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Work schedule copy management events
  name: ADP Copy Work Schedule API
  slug: adp-copy-work-schedule-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List all corporate contacts
  name: ADP Corporate Directory API
  slug: adp-corporate-directory-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Corporate Groups data APIs
  name: ADP Corporate Groups Management API
  slug: adp-corporate-groups-management-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Validation Table - Cost Centers
  name: ADP Cost Centers API
  slug: adp-cost-centers-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Manage deduction configurations (extended version)
  name: ADP Deduction Configuration Details API
  slug: adp-deduction-configuration-details-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Validation Table - Departments
  name: ADP Departments API
  slug: adp-departments-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: APIs to manage dependents in the benefits domain
  name: ADP Dependents API
  slug: adp-dependents-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Educational degree add management events.
  name: ADP Educational Degree Add API
  slug: adp-educational-degree-add-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Educational degree change management events.
  name: ADP Educational Degree Change API
  slug: adp-educational-degree-change-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Educational degree remove management events.
  name: ADP Educational Degree Remove API
  slug: adp-educational-degree-remove-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List all educational degrees
  name: ADP Educational Degrees API
  slug: adp-educational-degrees-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Provide one or more employee benefits plans as per LIMRA WBEDX specification
  name: ADP External Benefit Plans API
  slug: adp-external-benefit-plans-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Change worker general deduction instruction event management
  name: ADP General Deduction Instruction Change API
  slug: adp-general-deduction-instruction-change-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Start worker general deduction instruction event management
  name: ADP General Deduction Instruction Start API
  slug: adp-general-deduction-instruction-start-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Stop worker general deduction instruction event management
  name: ADP General Deduction Instruction Stop API
  slug: adp-general-deduction-instruction-stop-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: General ledger document mamangement
  name: ADP General Ledger Documents API
  slug: adp-general-ledger-documents-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List all job applications
  name: ADP Job Applications API
  slug: adp-job-applications-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List job requisitions
  name: ADP Job Requisitions API
  slug: adp-job-requisitions-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Validation Table - Jobs
  name: ADP Jobs API
  slug: adp-jobs-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Labor Charge Code Mass Uploads
  name: ADP Labor Charge Code Uploads API
  slug: adp-labor-charge-code-uploads-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Organization language add management events.
  name: ADP Language Add API
  slug: adp-language-add-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Organization language change management events.
  name: ADP Language Change API
  slug: adp-language-change-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Organization language remove management events.
  name: ADP Language Remove API
  slug: adp-language-remove-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List all languages
  name: ADP Languages API
  slug: adp-languages-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Organization license add management events.
  name: ADP License Add API
  slug: adp-license-add-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Organization license change management events.
  name: ADP License Change API
  slug: adp-license-change-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Organization license remove management events.
  name: ADP License Remove API
  slug: adp-license-remove-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List all licenses
  name: ADP Licenses API
  slug: adp-licenses-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker amount custom field management
  name: ADP Manage Worker Custom Amount API
  slug: adp-manage-worker-custom-amount-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker code custom field management
  name: ADP Manage Worker Custom Code API
  slug: adp-manage-worker-custom-code-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker date custom field management
  name: ADP Manage Worker Custom Date API
  slug: adp-manage-worker-custom-date-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker indicator custom field management
  name: ADP Manage Worker Custom Indicator API
  slug: adp-manage-worker-custom-indicator-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker number custom field management
  name: ADP Manage Worker Custom Number API
  slug: adp-manage-worker-custom-number-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker string custom field management
  name: ADP Manage Worker Custom String API
  slug: adp-manage-worker-custom-string-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Organization membership add management events.
  name: ADP Membership Add API
  slug: adp-membership-add-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Organization membership change management events.
  name: ADP Membership Change API
  slug: adp-membership-change-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Organization membership remove management events.
  name: ADP Membership Remove API
  slug: adp-membership-remove-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List all memberships
  name: ADP Memberships API
  slug: adp-memberships-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: APIs to request the metadata to manage the corresponding valdiation table
  name: ADP Meta APIs API
  slug: adp-meta-apis-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Modify worker's assigned units, e.g. department, division, etc.
  name: ADP Modify Assigned Organizational Units API
  slug: adp-modify-assigned-organizational-units-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Modify a set of time entries
  name: ADP Modify Time Entries API
  slug: adp-modify-time-entries-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Modify a set of time off balances
  name: ADP Modify Time Off Balances API
  slug: adp-modify-time-off-balances-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Modify work assignment details
  name: ADP Modify Work Assignment API
  slug: adp-modify-work-assignment-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Modify the details of the worker's supervisors
  name: ADP Modify Worker Reports To API
  slug: adp-modify-worker-reports-to-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: APIs to obtain the applicant onboarding APIs metadata
  name: ADP Onboarding API Metadata API
  slug: adp-onboarding-api-metadata-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: APIs to manage the applicant onboarding process
  name: ADP Onboarding Process Management API
  slug: adp-onboarding-process-management-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List Time Off Requests
  name: ADP Paid Time Off - Requests API
  slug: adp-paid-time-off-requests-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Modify pay data input event management
  name: ADP Pay Data Input Modify API
  slug: adp-pay-data-input-modify-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List all pay distributions
  name: ADP Pay Distributions API
  slug: adp-pay-distributions-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List worker pay statements
  name: ADP Pay Statements API
  slug: adp-pay-statements-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Custom codelists applicable to the WFN APIs across payroll management features
  name: ADP Payroll Codelists API
  slug: adp-payroll-codelists-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Retrieve the list of pay periods for pay groups
  name: ADP Payroll Group Pay Periods API
  slug: adp-payroll-group-pay-periods-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Output payment allocations of individual payroll items
  name: ADP Payroll Output - Associate Payment Allocations API
  slug: adp-payroll-output-associate-payment-allocations-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Output summaries of individual payroll items, e.g. earnings, deductions, etc.
  name: ADP Payroll Output - Associate Payment Summaries API
  slug: adp-payroll-output-associate-payment-summaries-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker payroll outputs - complete details
  name: ADP Payroll Outputs API
  slug: adp-payroll-outputs-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Validation Table -Person Custom Fields
  name: ADP Person Custom Fields API
  slug: adp-person-custom-fields-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List all personal contacts
  name: ADP Personal Contacts API
  slug: adp-personal-contacts-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Work assignment data APIs, e.g. business communication, employment custom fields, etc.
  name: ADP Position Data Management API
  slug: adp-position-data-management-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: This API supports the processing of a collection data collection entries from 1 to Many data collection terminals (i.e. Time Clock).
  name: ADP Process Data Collection Entries API
  slug: adp-process-data-collection-entries-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: APIs to manage the questionnaire defintions
  name: ADP Questionnaire Management API
  slug: adp-questionnaire-management-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker read management events.
  name: ADP Read Worker API
  slug: adp-read-worker-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Recognition add management events.
  name: ADP Recognition Add API
  slug: adp-recognition-add-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Recognition change management events.
  name: ADP Recognition Change API
  slug: adp-recognition-change-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Recognition remove management events.
  name: ADP Recognition Remove API
  slug: adp-recognition-remove-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List all recognitions
  name: ADP Recognitions API
  slug: adp-recognitions-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker rehire management events.
  name: ADP Rehire Worker API
  slug: adp-rehire-worker-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: A worker additional remuneration remove management
  name: ADP Remove Additional Remuneration API
  slug: adp-remove-additional-remuneration-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal contact remove management events.
  name: ADP Remove Personal Contact API
  slug: adp-remove-personal-contact-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Work schedule day removal management events
  name: ADP Remove Schedule Day API
  slug: adp-remove-schedule-day-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Work schedule remove management events
  name: ADP Remove Work Schedule API
  slug: adp-remove-work-schedule-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker business communication email remove management events.
  name: ADP Remove Worker Business Email API
  slug: adp-remove-worker-business-email-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker business communication fax remove management events.
  name: ADP Remove Worker Business Fax API
  slug: adp-remove-worker-business-fax-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker business communication landline remove management events.
  name: ADP Remove Worker Business Landline API
  slug: adp-remove-worker-business-landline-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker business communication mobile remove management events.
  name: ADP Remove Worker Business Mobile API
  slug: adp-remove-worker-business-mobile-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker business communication pager remove management events.
  name: ADP Remove Worker Business Pager API
  slug: adp-remove-worker-business-pager-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker legal address remove management events
  name: ADP Remove Worker Legal Address API
  slug: adp-remove-worker-legal-address-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal address remove management events
  name: ADP Remove Worker Personal Address API
  slug: adp-remove-worker-personal-address-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal communication email remove management events.
  name: ADP Remove Worker Personal Email API
  slug: adp-remove-worker-personal-email-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal communication fax remove management events.
  name: ADP Remove Worker Personal Fax API
  slug: adp-remove-worker-personal-fax-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal communication landline remove management events.
  name: ADP Remove Worker Personal Landline API
  slug: adp-remove-worker-personal-landline-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal communication mobile remove management events.
  name: ADP Remove Worker Personal Mobile API
  slug: adp-remove-worker-personal-mobile-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker personal communication pager remove management events.
  name: ADP Remove Worker Personal Pager API
  slug: adp-remove-worker-personal-pager-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker leave of absence management events.
  name: ADP Request Leave Of Absence API
  slug: adp-request-leave-of-absence-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Worker return from leave of absence management events.
  name: ADP Request Return From Leave Of Absence API
  slug: adp-request-return-from-leave-of-absence-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: An instance to capture a review event when an associate adds a new membership
  name: ADP Review Add Membership API
  slug: adp-review-add-membership-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: An instance to capture a review event when an associate changes a new membership
  name: ADP Review Change Membership API
  slug: adp-review-change-membership-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: An instance to capture a review event when an associate removes a new membership
  name: ADP Review Remove Membership API
  slug: adp-review-remove-membership-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: APIs to retrieve statutory policies with applicable ADP codes and statutory data
  name: ADP Tax Policy Eligibility Solutions API
  slug: adp-tax-policy-eligibility-solutions-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Get a worker's team's timecards. That is all the time cards for the worker's team members. The worker is identified by workers/{associateOID}
  name: ADP Team Time Cards API
  slug: adp-team-time-cards-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Terminate work assignment details
  name: ADP Terminate Work Assignment API
  slug: adp-terminate-work-assignment-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: APIs to manage the change of a US tax profile federal income tax instruction
  name: ADP US Federal Tax Profile - Change Federal Income Tax Instruction API
  slug: adp-us-federal-tax-profile-change-federal-income-tax-instruction-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: APIs to manage the addition of a US tax profile local income tax instruction
  name: ADP US Local Tax Profile - Add Local Income Tax Instruction API
  slug: adp-us-local-tax-profile-add-local-income-tax-instruction-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Details of the US local tax profile
  name: ADP US Local Tax Profile API
  slug: adp-us-local-tax-profile-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: APIs to manage the change of a US tax profile local income tax instruction
  name: ADP US Local Tax Profile - Change Local Income Tax Instruction API
  slug: adp-us-local-tax-profile-change-local-income-tax-instruction-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: APIs to manage the change of a US tax profile local income tax instruction
  name: ADP US Local Tax Profile - Remove Local Income Tax Instruction API
  slug: adp-us-local-tax-profile-remove-local-income-tax-instruction-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: APIs to manage the addition of a US tax profile state income tax instruction
  name: ADP US State Tax Profile - Add State Income Tax Instruction API
  slug: adp-us-state-tax-profile-add-state-income-tax-instruction-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Details of the US State tax profile
  name: ADP US State Tax Profile API
  slug: adp-us-state-tax-profile-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: APIs to manage the change of a US tax profile state income tax instruction
  name: ADP US State Tax Profile - Change State Income Tax Instruction API
  slug: adp-us-state-tax-profile-change-state-income-tax-instruction-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List all US tax profiles (Federal, State and Local)
  name: ADP US Tax Profiles API
  slug: adp-us-tax-profiles-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Import Schedules for multiple employees
  name: ADP Work Schedule Entry Uploads API
  slug: adp-work-schedule-entry-uploads-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List all work schedules
  name: ADP Work Schedules API
  slug: adp-work-schedules-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Validation Table Worker Custom Fields
  name: ADP Worker Custom Fields API
  slug: adp-worker-custom-fields-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List all worker demographics
  name: ADP Worker Demographics API
  slug: adp-worker-demographics-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: APIs to retrieve worker images, e.g profile photo or background
  name: ADP Worker Images API
  slug: adp-worker-images-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Retrieve worker leaves details
  name: ADP Worker Leaves API
  slug: adp-worker-leaves-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: Custom codelists applicable to the WFN APIs across worker management features
  name: ADP Worker Management Codelists API
  slug: adp-worker-management-codelists-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List all payroll instructions
  name: ADP Worker Payroll Instructions API
  slug: adp-worker-payroll-instructions-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: APIs to manage the worker profile picture
  name: ADP Worker Profile Photo Management API
  slug: adp-worker-profile-photo-management-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: APIs to manage worker time card input requests
  name: ADP Worker Time Card Inputs API
  slug: adp-worker-time-card-inputs-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: List a worker's time off requests
  name: ADP Worker Time Off Requests API
  slug: adp-worker-time-off-requests-api
- baseURL: https://api.adp.com
  baseurl_source: declared
  description: APIs to retrieve the worker data, either for a collection or a single worker
  name: ADP Workers Data Retrieval API
  slug: adp-workers-data-retrieval-api
artifact_total: 307
asyncapis:
- description: ''
  name: Adp Event Notifications Webhooks
  slug: adp-event-notifications-webhooks
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
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-payroll-deduction-configurations-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-payroll-deduction-configurations-v3-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-payroll-general-ledger-documents-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-payroll-general-ledger-documents-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-payroll-pay-data-input-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-payroll-pay-data-input-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-payroll-pay-distributions-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-payroll-pay-distributions-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-payroll-pay-statements-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-payroll-pay-statements-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-payroll-payroll-group-pay-periods-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-payroll-payroll-group-pay-periods-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-payroll-payroll-outputs-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-payroll-payroll-outputs-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-payroll-tax-policy-eligibility-solutions-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-payroll-tax-policy-eligibility-solutions-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-payroll-us-tax-profiles-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-payroll-us-tax-profiles-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-payroll-us-tax-profiles-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-payroll-us-tax-profiles-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-payroll-worker-payroll-instructions-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-payroll-worker-payroll-instructions-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-corporate-directory-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-corporate-directory-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-hr-work-assignment-management-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-hr-work-assignment-management-v3-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-hr-worker-profiles-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-hr-worker-profiles-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-personal-contacts-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-personal-contacts-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-worker-associate-profiles-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-worker-associate-profiles-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-worker-demographics-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-worker-demographics-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-worker-leaves-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-worker-leaves-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-workers-biological-data-management-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-workers-biological-data-management-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-workers-business-communication-management-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-workers-business-communication-management-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-workers-compensation-management-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-workers-compensation-management-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-workers-custom-data-management-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-workers-custom-data-management-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-workers-data-integration-management-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-workers-data-integration-management-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-workers-demographic-data-management-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-workers-demographic-data-management-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-workers-identification-management-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-workers-identification-management-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-workers-ksaoc-management-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-workers-ksaoc-management-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-workers-lifecycle-management-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-workers-lifecycle-management-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-workers-person-custom-data-management-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-workers-person-custom-data-management-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-workers-personal-communication-management-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-workers-personal-communication-management-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-workers-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-workers-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-workers-work-assignment-management-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-workers-work-assignment-management-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hr-workers-work-deployment-management-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hr-workers-work-deployment-management-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-time-data-collection-entries-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-time-data-collection-entries-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-time-labor-allocation-code-uploads-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-time-labor-allocation-code-uploads-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-time-team-time-cards-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-time-team-time-cards-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-time-time-card-inputs-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-time-time-card-inputs-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-time-time-cards-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-time-time-cards-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-time-time-off-balances-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-time-time-off-balances-v3-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-time-time-off-requests-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-time-time-off-requests-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-time-time-off-requests-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-time-time-off-requests-v3-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-time-work-schedule-entry-uploads-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-time-work-schedule-entry-uploads-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-time-work-schedules-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-time-work-schedules-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-benefits-beneficiaries-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-benefits-beneficiaries-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-benefits-dependents-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-benefits-dependents-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-benefits-external-plans-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-benefits-external-plans-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-talent-associate-certifications-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-talent-associate-certifications-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-talent-associate-competencies-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-talent-associate-competencies-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-talent-associate-educational-degrees-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-talent-associate-educational-degrees-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-talent-associate-languages-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-talent-associate-languages-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-talent-associate-licenses-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-talent-associate-licenses-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-talent-associate-memberships-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-talent-associate-memberships-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-talent-associate-recognitions-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-talent-associate-recognitions-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-staffing-job-applicants-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-staffing-job-applicants-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-staffing-job-applications-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-staffing-job-applications-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-staffing-job-requisitions-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-staffing-job-requisitions-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-staffing-recruiting-questionnaires-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-staffing-recruiting-questionnaires-v3-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hcm-applicant-onboarding-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hcm-applicant-onboarding-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hcm-validation-tables-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hcm-validation-tables-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/overlays/adp-hcm-wfn-codelists-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adp-hcm-wfn-codelists-v3-overlay.yaml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/plans/adp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adp-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/rate-limits/adp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/adp-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/finops/adp-finops.yml
  title: ''
  type: FinOps
  url: finops/adp-finops.yml
- group: start
  title: ''
  type: SignUp
  url: https://developers.adp.com/getting-started/partner-integration-overview
- group: docs
  title: ''
  type: APIReference
  url: https://developers.adp.com/apis/api-explorer
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.adp.com
- group: start
  title: ''
  type: Quickstart
  url: https://developers.adp.com/getting-started/client-integration-overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adp.com/what-we-offer/integrations/api-central.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adp.com/legal.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adp.com/privacy.aspx
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/postman/adp-wfn-postman-collection.json
  title: ''
  type: Postman
  url: postman/adp-wfn-postman-collection.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/conventions/adp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adp-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/errors/adp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adp-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/conformance/adp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adp-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.adp.com/about-adp/data-security.aspx
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/security/adp-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/adp-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/security/adp-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/adp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.adp.com/about-adp/data-security/vulnerability-disclosure.aspx
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/lifecycle/adp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/adp-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/changelog/adp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/adp-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/data-model/adp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adp-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/packages/adp-packages.yml
  title: ''
  type: Packages
  url: packages/adp-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/packages/adp-packages.yml
  title: ''
  type: SDKs
  url: packages/adp-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/components/adp-components.yml
  title: ''
  type: Components
  url: components/adp-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/sandbox/adp-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/adp-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/asyncapi/adp-event-notifications-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/adp-event-notifications-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/mcp/adp-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adp-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/well-known/adp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adp-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/llms/adp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adp-llms.txt
- group: start
  title: ''
  type: Signup
  url: https://developers.adp.com/articles/guide/registration
- group: other
  title: ''
  type: Marketplace
  url: https://apps.adp.com
- group: operate
  title: ''
  type: Support
  url: https://developers.adp.com/articles/guide/support
- group: company
  title: ''
  type: Website
  url: https://www.adp.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/capabilities/adp-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/adp-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/agentic-access/adp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adp-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/security/adp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adp-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/authentication/adp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adp-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/scopes/adp-scopes.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/openapi/_original/adp-workers-openapi.yml
  title: ADP Workers OpenAPI
  type: OpenAPI
  url: openapi/_original/adp-workers-openapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/openapi/_original/adp-payroll-openapi.yml
  title: ADP Payroll OpenAPI
  type: OpenAPI
  url: openapi/_original/adp-payroll-openapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/json-schema/adp-worker-schema.json
  title: ADP Worker JSON Schema
  type: JSONSchema
  url: json-schema/adp-worker-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/json-ld/adp-context.jsonld
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
mcp_servers:
- description: ''
  name: ADP MCP Server
  slug: adp-mcp-server
modified: '2026-05-19'
name: ADP
nav: Providers
network: true
overview: 'ADP publishes 193 APIs on the [APIs.io](https://apis.io/) network, including Organizations API, PayrollInstructions API, Workers API, and 190 more. Tagged areas include Benefits, HCM, Human Resources, Payroll, and Workforce.


  The ADP catalog on APIs.io includes 1 event-driven AsyncAPI specification, 3 JSON-LD contexts, and 2 Spectral governance rulesets.


  ADP''s developer surface includes signup flow, API reference, quickstart, pricing, changelog, sandbox, support, and 102 more developer resources.'
plans:
- name: Adp Plans Pricing
  plan_count: 2
  slug: adp-plans-pricing
random_paper: 1
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
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 35
    catalog_earned: 52.5
    catalog_earned_first_party: 0.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 73.7
    contract_governance: 31.8
    contract_quality: 34.5
    developer_ergonomics: 41.1
    discoverability: 63.0
    operational_transparency: 42.1
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 190
      marker_coverage: 98.4
      total: 193
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- kind: vulnerability-disclosure
  name: Adp Vulnerability Disclosure
  slug: adp-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Adp Trust Center
  slug: adp-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 27701, PCI DSS, Sarbanes-Oxley (SOX)
slug: adp
tags:
- Benefits
- HCM
- Human Resources
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
website: https://www.adp.com/
---
