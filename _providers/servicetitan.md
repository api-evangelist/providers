---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - finops
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Servicetitan Agentic Access
  operation_count: 90
  slug: servicetitan-agentic-access
  summary_line: 90 operations · 38 acting
api_count: 8
apis:
- description: Manage marketing campaigns, campaign categories, suppression lists, and attribution data that powers cost-per-lead and cost-per-booked-job reporting. Underpins Marketing Pro email and SMS campaigns.
  name: ServiceTitan Marketing API
  slug: servicetitan-marketing-api
- description: Retrieve aggregated customer reviews and reputation metrics across Google, Facebook, Yelp, BBB, and other connected review providers. Read-only API surfacing review text, ratings, sentiment, and respo
  name: ServiceTitan Marketing Reputation API
  slug: servicetitan-marketing-reputation-api
- description: 'Manage membership types, customer memberships, membership invoice templates, recurring service types, and recurring service events. Drives the recurring revenue surface — maintenance agreements, club '
  name: ServiceTitan Memberships API
  slug: servicetitan-memberships-api
- description: Manage commercial service agreements — contract terms, billed locations, line items, renewal cadence, and invoice generation rules. Used by commercial trades for multi-site recurring service contracts
  name: ServiceTitan Service Agreements API
  slug: servicetitan-service-agreements-api
- description: Retrieve form definitions and field-completed form submissions including photos, signatures, checkbox values, and free-text responses. Used for safety checklists, equipment commissioning, compliance a
  name: ServiceTitan Forms API
  slug: servicetitan-forms-api
- description: Manage payroll adjustments, gross-pay items, job splits, timesheet codes, activity codes, non-job timesheets, and payroll settings. Exports to ADP, Paychex, Gusto, Paylocity, and other downstream payr
  name: ServiceTitan Payroll API
  slug: servicetitan-payroll-api
- description: Read and write timesheet entries, activity codes, and shift segments tying technician time to jobs, non-job activities, paid time off, and travel. Feeds the Payroll API and FieldRoutes reconciliation.
  name: ServiceTitan Timesheets API
  slug: servicetitan-timesheets-api
- description: 'Run published custom reports with parameters and retrieve dynamic value sets used by report inputs. Lower rate limit than other surfaces — 1 of the same report per minute per tenant. Replaces fragile '
  name: ServiceTitan Reporting API
  slug: servicetitan-reporting-api
- description: Create and retrieve estimates, estimate items, and proposal templates. Backs the Proposal Builder feature used to convert leads into approved scopes of work — including good / better / best presentati
  name: ServiceTitan Sales & Estimates API
  slug: servicetitan-sales-estimates-api
- description: Submit and retrieve post-service technician ratings and customer feedback. Powers the "How did we do?" SMS / email flow that aggregates into Marketing Reputation.
  name: ServiceTitan Customer Interactions API
  slug: servicetitan-customer-interactions-api
- description: Create, update, and resolve internal tasks, task types, sub-tasks, and task statuses. Used for office-to-field handoffs, escalations, and back-office workflows that aren't customer jobs.
  name: ServiceTitan Task Management API
  slug: servicetitan-task-management-api
- description: Retrieve inbound and outbound call records, call recordings, call analytics, and call reasons. Powers Contact Center Pro reporting and Voice Agent transcript analysis.
  name: ServiceTitan Telecom API
  slug: servicetitan-telecom-api
- description: 'Power online booking widgets — list configured schedulers, retrieve scheduler availability, create and update booking sessions. Backed by the Schedule Engine acquisition; required for customer-facing '
  name: ServiceTitan Scheduling Pro API
  slug: servicetitan-scheduling-pro-api
- description: Retrieve call reasons, job booking call reason metadata, capacity-aware booking windows, and recommended slot suggestions. Bridges Telecom call intake with JPM job creation.
  name: ServiceTitan Job Booking & Capacity API
  slug: servicetitan-jbce-api
- description: Manage webhook subscriptions for customer, job, appointment, invoice, payment, and membership lifecycle events. V1 is closed to new subscriptions; V2 webhooks are in development. Polling-based change-
  name: ServiceTitan Webhooks API
  slug: servicetitan-webhooks-api
- description: The Adjustments API from ServiceTitan — 1 operation(s) for adjustments.
  name: ServiceTitan Adjustments API
  slug: servicetitan-adjustments-api
- description: The Appointment Assignments API from ServiceTitan — 3 operation(s) for appointment assignments.
  name: ServiceTitan Appointment Assignments API
  slug: servicetitan-appointment-assignments-api
- description: Job appointments and visits
  name: ServiceTitan Appointments API
  slug: servicetitan-appointments-api
- description: The Attachments API from ServiceTitan — 1 operation(s) for attachments.
  name: ServiceTitan Attachments API
  slug: servicetitan-attachments-api
- description: Customer-initiated booking requests
  name: ServiceTitan Bookings API
  slug: servicetitan-bookings-api
- description: The Business Hours API from ServiceTitan — 1 operation(s) for business hours.
  name: ServiceTitan Business Hours API
  slug: servicetitan-business-hours-api
- description: The Business Units API from ServiceTitan — 2 operation(s) for business units.
  name: ServiceTitan Business Units API
  slug: servicetitan-business-units-api
- description: The Capacity API from ServiceTitan — 1 operation(s) for capacity.
  name: ServiceTitan Capacity API
  slug: servicetitan-capacity-api
- description: The Categories API from ServiceTitan — 1 operation(s) for categories.
  name: ServiceTitan Categories API
  slug: servicetitan-categories-api
- description: Customer contact methods (phone, email)
  name: ServiceTitan Contacts API
  slug: servicetitan-contacts-api
- description: Customer-of-record records
  name: ServiceTitan Customers API
  slug: servicetitan-customers-api
- description: The Discounts And Fees API from ServiceTitan — 1 operation(s) for discounts and fees.
  name: ServiceTitan Discounts And Fees API
  slug: servicetitan-discounts-and-fees-api
- description: The Employees API from ServiceTitan — 1 operation(s) for employees.
  name: ServiceTitan Employees API
  slug: servicetitan-employees-api
- description: The Equipment API from ServiceTitan — 2 operation(s) for equipment.
  name: ServiceTitan Equipment API
  slug: servicetitan-equipment-api
- description: The GL Accounts API from ServiceTitan — 1 operation(s) for gl accounts.
  name: ServiceTitan GL Accounts API
  slug: servicetitan-gl-accounts-api
- description: The GPS API from ServiceTitan — 1 operation(s) for gps.
  name: ServiceTitan GPS API
  slug: servicetitan-gps-api
- description: The Installed Equipment API from ServiceTitan — 2 operation(s) for installed equipment.
  name: ServiceTitan Installed Equipment API
  slug: servicetitan-installed-equipment-api
- description: The Invoices API from ServiceTitan — 3 operation(s) for invoices.
  name: ServiceTitan Invoices API
  slug: servicetitan-invoices-api
- description: Job type definitions
  name: ServiceTitan Job Types API
  slug: servicetitan-job-types-api
- description: Service jobs (work orders)
  name: ServiceTitan Jobs API
  slug: servicetitan-jobs-api
- description: The Journal Entries API from ServiceTitan — 1 operation(s) for journal entries.
  name: ServiceTitan Journal Entries API
  slug: servicetitan-journal-entries-api
- description: Pre-customer lead records
  name: ServiceTitan Leads API
  slug: servicetitan-leads-api
- description: Customer service locations and addresses
  name: ServiceTitan Locations API
  slug: servicetitan-locations-api
- description: The Materials API from ServiceTitan — 2 operation(s) for materials.
  name: ServiceTitan Materials API
  slug: servicetitan-materials-api
- description: The Payments API from ServiceTitan — 3 operation(s) for payments.
  name: ServiceTitan Payments API
  slug: servicetitan-payments-api
- description: Multi-job projects
  name: ServiceTitan Projects API
  slug: servicetitan-projects-api
- description: The Purchase Orders API from ServiceTitan — 2 operation(s) for purchase orders.
  name: ServiceTitan Purchase Orders API
  slug: servicetitan-purchase-orders-api
- description: The Receipts API from ServiceTitan — 1 operation(s) for receipts.
  name: ServiceTitan Receipts API
  slug: servicetitan-receipts-api
- description: The Services API from ServiceTitan — 2 operation(s) for services.
  name: ServiceTitan Services API
  slug: servicetitan-services-api
- description: The Tag Types API from ServiceTitan — 1 operation(s) for tag types.
  name: ServiceTitan Tag Types API
  slug: servicetitan-tag-types-api
- description: Tag types and customer tagging
  name: ServiceTitan Tags API
  slug: servicetitan-tags-api
- description: The Tax Zones API from ServiceTitan — 1 operation(s) for tax zones.
  name: ServiceTitan Tax Zones API
  slug: servicetitan-tax-zones-api
- description: The Technician Shifts API from ServiceTitan — 1 operation(s) for technician shifts.
  name: ServiceTitan Technician Shifts API
  slug: servicetitan-technician-shifts-api
- description: The Technicians API from ServiceTitan — 2 operation(s) for technicians.
  name: ServiceTitan Technicians API
  slug: servicetitan-technicians-api
- description: The Transfers API from ServiceTitan — 1 operation(s) for transfers.
  name: ServiceTitan Transfers API
  slug: servicetitan-transfers-api
- description: The Trucks API from ServiceTitan — 1 operation(s) for trucks.
  name: ServiceTitan Trucks API
  slug: servicetitan-trucks-api
- description: The User Roles API from ServiceTitan — 1 operation(s) for user roles.
  name: ServiceTitan User Roles API
  slug: servicetitan-user-roles-api
- description: The Vendors API from ServiceTitan — 1 operation(s) for vendors.
  name: ServiceTitan Vendors API
  slug: servicetitan-vendors-api
- description: The Warehouses API from ServiceTitan — 1 operation(s) for warehouses.
  name: ServiceTitan Warehouses API
  slug: servicetitan-warehouses-api
- description: The Zones API from ServiceTitan — 1 operation(s) for zones.
  name: ServiceTitan Zones API
  slug: servicetitan-zones-api
artifact_total: 176
collections:
- collection_type: postman
  name: ServiceTitan Accounting Adjustments API
  slug: postman-servicetitan-adjustments-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Appointment Assignments API
  slug: postman-servicetitan-appointment-assignments-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Appointments API
  slug: postman-servicetitan-appointments-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Attachments API
  slug: postman-servicetitan-attachments-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Bookings API
  slug: postman-servicetitan-bookings-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Business Hours API
  slug: postman-servicetitan-business-hours-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Business Units API
  slug: postman-servicetitan-business-units-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Capacity API
  slug: postman-servicetitan-capacity-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Categories API
  slug: postman-servicetitan-categories-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Contacts API
  slug: postman-servicetitan-contacts-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Customers API
  slug: postman-servicetitan-customers-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Discounts And Fees API
  slug: postman-servicetitan-discounts-and-fees-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Employees API
  slug: postman-servicetitan-employees-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Equipment API
  slug: postman-servicetitan-equipment-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments GL Accounts API
  slug: postman-servicetitan-gl-accounts-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments GPS API
  slug: postman-servicetitan-gps-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Installed Equipment API
  slug: postman-servicetitan-installed-equipment-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Invoices API
  slug: postman-servicetitan-invoices-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Job Types API
  slug: postman-servicetitan-job-types-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Jobs API
  slug: postman-servicetitan-jobs-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Journal Entries API
  slug: postman-servicetitan-journal-entries-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Leads API
  slug: postman-servicetitan-leads-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Locations API
  slug: postman-servicetitan-locations-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Materials API
  slug: postman-servicetitan-materials-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Payments API
  slug: postman-servicetitan-payments-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Projects API
  slug: postman-servicetitan-projects-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Purchase Orders API
  slug: postman-servicetitan-purchase-orders-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Receipts API
  slug: postman-servicetitan-receipts-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Services API
  slug: postman-servicetitan-services-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Tag Types API
  slug: postman-servicetitan-tag-types-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Tags API
  slug: postman-servicetitan-tags-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Tax Zones API
  slug: postman-servicetitan-tax-zones-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Technician Shifts API
  slug: postman-servicetitan-technician-shifts-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Technicians API
  slug: postman-servicetitan-technicians-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Transfers API
  slug: postman-servicetitan-transfers-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Trucks API
  slug: postman-servicetitan-trucks-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments User Roles API
  slug: postman-servicetitan-user-roles-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Vendors API
  slug: postman-servicetitan-vendors-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Warehouses API
  slug: postman-servicetitan-warehouses-api
- collection_type: postman
  name: ServiceTitan Accounting Adjustments Zones API
  slug: postman-servicetitan-zones-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ServiceTitan Accounting API
  slug: open-servicetitan-accounting-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments API
  slug: open-servicetitan-adjustments-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Appointment Assignments API
  slug: open-servicetitan-appointment-assignments-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Appointments API
  slug: open-servicetitan-appointments-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Attachments API
  slug: open-servicetitan-attachments-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Bookings API
  slug: open-servicetitan-bookings-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Business Hours API
  slug: open-servicetitan-business-hours-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Business Units API
  slug: open-servicetitan-business-units-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Capacity API
  slug: open-servicetitan-capacity-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Categories API
  slug: open-servicetitan-categories-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Contacts API
  slug: open-servicetitan-contacts-api
- collection_type: open
  name: ServiceTitan CRM API
  slug: open-servicetitan-crm-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Customers API
  slug: open-servicetitan-customers-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Discounts And Fees API
  slug: open-servicetitan-discounts-and-fees-api
- collection_type: open
  name: ServiceTitan Dispatch API
  slug: open-servicetitan-dispatch-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Employees API
  slug: open-servicetitan-employees-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Equipment API
  slug: open-servicetitan-equipment-api
- collection_type: open
  name: ServiceTitan Equipment Systems API
  slug: open-servicetitan-equipment-systems-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments GL Accounts API
  slug: open-servicetitan-gl-accounts-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments GPS API
  slug: open-servicetitan-gps-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Installed Equipment API
  slug: open-servicetitan-installed-equipment-api
- collection_type: open
  name: ServiceTitan Inventory API
  slug: open-servicetitan-inventory-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Invoices API
  slug: open-servicetitan-invoices-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Job Types API
  slug: open-servicetitan-job-types-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Jobs API
  slug: open-servicetitan-jobs-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Journal Entries API
  slug: open-servicetitan-journal-entries-api
- collection_type: open
  name: ServiceTitan Job Planning & Management API
  slug: open-servicetitan-jpm-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Leads API
  slug: open-servicetitan-leads-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Locations API
  slug: open-servicetitan-locations-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Materials API
  slug: open-servicetitan-materials-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Payments API
  slug: open-servicetitan-payments-api
- collection_type: open
  name: ServiceTitan Pricebook API
  slug: open-servicetitan-pricebook-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Projects API
  slug: open-servicetitan-projects-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Purchase Orders API
  slug: open-servicetitan-purchase-orders-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Receipts API
  slug: open-servicetitan-receipts-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Services API
  slug: open-servicetitan-services-api
- collection_type: open
  name: ServiceTitan Settings API
  slug: open-servicetitan-settings-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Tag Types API
  slug: open-servicetitan-tag-types-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Tags API
  slug: open-servicetitan-tags-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Tax Zones API
  slug: open-servicetitan-tax-zones-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Technician Shifts API
  slug: open-servicetitan-technician-shifts-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Technicians API
  slug: open-servicetitan-technicians-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Transfers API
  slug: open-servicetitan-transfers-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Trucks API
  slug: open-servicetitan-trucks-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments User Roles API
  slug: open-servicetitan-user-roles-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Vendors API
  slug: open-servicetitan-vendors-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Warehouses API
  slug: open-servicetitan-warehouses-api
- collection_type: open
  name: ServiceTitan Accounting Adjustments Zones API
  slug: open-servicetitan-zones-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/servicetitan-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/servicetitan/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/servicetitan-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/servicetitan-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/servicetitan-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/servicetitan-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/servicetitan
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/servicetitan
- group: start
  title: ''
  type: Portal
  url: https://developer.servicetitan.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.servicetitan.io/docs/welcome/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.servicetitan.io/docs/apis
- group: docs
  title: ''
  type: Documentation
  url: https://developer.servicetitan.io/api-details/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.servicetitan.io/docs/get-going-environments/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.servicetitan.io/docs/faqs-apis-app-keys-client-keys/
- group: start
  title: ''
  type: Portal
  url: https://partnerapis.servicetitan.io/apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.servicetitan.com/how-to/get-started-with-apidev-portal-v2
- group: operate
  title: ''
  type: RateLimits
  url: https://help.servicetitan.com/problem-solution/what-are-the-default-api-rate-limits-in-servicetitan-for-regular-apis-and
- group: operate
  title: ''
  type: StatusPage
  url: https://status.servicetitan.com/
- group: start
  title: ''
  type: Portal
  url: https://www.servicetitan.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.servicetitan.com/products
- group: company
  title: ''
  type: Blog
  url: https://www.servicetitan.com/blog
- group: company
  title: ''
  type: Blog
  url: https://www.servicetitan.com/news
- group: company
  title: ''
  type: AboutUs
  url: https://www.servicetitan.com/about-us
- group: other
  title: ''
  type: CaseStudies
  url: https://www.servicetitan.com/customer-stories
- group: company
  title: ''
  type: Careers
  url: https://www.servicetitan.com/careers
- group: operate
  title: ''
  type: Forums
  url: https://community.servicetitan.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.servicetitan.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.servicetitan.com/legal/terms-of-service
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.servicetitan.com/trust
- group: commercial
  title: ''
  type: Pricing
  url: https://www.servicetitan.com/pricing
- group: operate
  title: ''
  type: Contact
  url: https://www.servicetitan.com/contact
- group: company
  title: ''
  type: Partners
  url: https://www.servicetitan.com/partners
- group: start
  title: ''
  type: Login
  url: https://app.servicetitan.com/
- group: build
  title: ''
  type: Tools
  url: https://github.com/servicetitan/request-middleware-templates
- group: build
  title: ''
  type: Tools
  url: https://github.com/servicetitan/Stl.Fusion
- group: docs
  title: ''
  type: Documentation
  url: https://www.postman.com/api-evangelist/servicetitan
- group: other
  title: ''
  type: Marketplace
  url: https://www.servicetitan.com/products/integrations
- group: docs
  title: ''
  type: Documentation
  url: https://www.servicetitan.com/products/conduit
- group: docs
  title: ''
  type: Documentation
  url: https://www.servicetitan.com/products/fieldroutes
- group: docs
  title: ''
  type: Documentation
  url: https://www.servicetitan.com/products/aspire
- group: docs
  title: ''
  type: Documentation
  url: https://www.servicetitan.com/products/convex
- group: docs
  title: ''
  type: Documentation
  url: https://www.servicetitan.com/products/atlas
- group: commercial
  title: ''
  type: Plans
  url: plans/servicetitan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/servicetitan-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/servicetitan-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/servicetitan-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/servicetitan-rules.yml
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: other
  title: ''
  type: Environments
  url: ''
created: '2026-05-25T00:00:00.000Z'
description: ServiceTitan is the operating system for the trades — all-in-one field service management software for residential and commercial contractors in HVAC, plumbing, electrical, roofing, garage door, pest control, refrigeration, fire & life safety, septic, landscape, and other service-based industries. The platform unifies CRM, dispatch, scheduling, job management, pricebook, mobile field execution, invoicing, payments, payroll, marketing attribution, memberships, service agreements, reporting, and Contact Center / Voice Agent capabilities behind a tenant-scoped V2 REST API surface accessed via OAuth 2.0 client credentials and a per-application App Key. ServiceTitan is the parent of FieldRoutes (pest), Aspire (landscape), and Convex (commercial sales), and ships Conduit as its integration platform.
examples:
- key_count: 2
  name: Servicetitan Customer Create Example
  slug: servicetitan-customer-create-example
- key_count: 2
  name: Servicetitan Invoice List Example
  slug: servicetitan-invoice-list-example
- key_count: 2
  name: Servicetitan Job Create Example
  slug: servicetitan-job-create-example
features:
- All-in-one field service management for residential and commercial trades
- 24 published REST API surfaces covering CRM, JPM, Dispatch, Accounting, Pricebook, Inventory, and more
- OAuth 2.0 client-credentials authentication with per-tenant App Keys and Client IDs
- Default rate limit of 60 calls per second per application per tenant; Reporting API limited to 1 of the same report per minute per tenant
- Production and Integration (sandbox) environments with separate auth endpoints
- Webhooks V1 (closed to new subscriptions) plus polling via `modifiedOnOrAfter` for change tracking; Webhooks V2 in development
- Developer Portal V2 with API & Webhook Reference, app key management, and request access flow
- Tenant-scoped data — every API path includes the tenant ID and every request includes ST-App-Key
- Marketplace of certified partner integrations (Conduit, Zapier, Celigo, Prismatic, Workato, Rollout)
- 'Pro add-ons exposed via the same API surface: Marketing Pro, Dispatch Pro, Pricebook Pro, Scheduling Pro, Fleet Pro, Contact Center Pro, Field Pro, Voice Agent'
- Supply chain partner integrations through the open-source request-middleware-templates Liquid framework
- Sister platforms — FieldRoutes (pest), Aspire (landscape), Convex (commercial sales) — share the ServiceTitan account but have separate API surfaces not yet documented in the public developer portal
finops:
- name: Servicetitan Finops
  service_category: SaaS — Field Service Management
  slug: servicetitan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/servicetitan.png
json_schemas:
- name: ServiceTitan Appointment
  property_count: 13
  slug: servicetitan-appointment
- name: ServiceTitan Customer
  property_count: 16
  slug: servicetitan-customer
- name: ServiceTitan Invoice
  property_count: 20
  slug: servicetitan-invoice
- name: ServiceTitan Job
  property_count: 22
  slug: servicetitan-job
- name: ServiceTitan Location
  property_count: 11
  slug: servicetitan-location
- name: ServiceTitan Pricebook Material
  property_count: 16
  slug: servicetitan-material
- name: ServiceTitan Payment
  property_count: 14
  slug: servicetitan-payment
- name: ServiceTitan Project
  property_count: 15
  slug: servicetitan-project
- name: ServiceTitan Pricebook Service
  property_count: 20
  slug: servicetitan-service
jsonld:
- class_count: 0
  name: Servicetitan Context
  property_count: 12
  slug: servicetitan-context
layout: provider
modified: '2026-05-25'
name: ServiceTitan
nav: Providers
network: true
overview: 'ServiceTitan publishes 40 APIs on the [APIs.io](https://apis.io/) network, including Adjustments API, Appointment Assignments API, Appointments API, and 37 more. Tagged areas include Field Service Management, Trades, HVAC, Plumbing, and Electrical.


  The ServiceTitan catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ServiceTitan''s developer surface includes authentication, developer portal, getting-started guide, documentation, engineering blog, pricing, tooling, and 40 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 2
  name: Servicetitan Rate Limits
  slug: servicetitan-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: ServiceTitan API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: servicetitan-jsonschema-spectral-rules
scopes:
- name: Servicetitan Scopes
  scope_count: 0
  slug: servicetitan-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 40.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 25.0
    contract_quality: 60.5
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 42.1
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 40
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/servicetitan/refs/heads/main/screenshots/servicetitan-2026-06-20T193732.png
security:
- kind: authentication
  name: Servicetitan Authentication
  slug: servicetitan-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Servicetitan Domain Security
  slug: servicetitan-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: servicetitan
tags:
- Field Service Management
- Trades
- HVAC
- Plumbing
- Electrical
- Construction
- CRM
- Dispatch
- Accounting
- Pricebook
- Marketing
- Memberships
- Webhook
website: https://developer.servicetitan.io/
---
