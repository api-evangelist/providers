---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.0
  scored_at: '2026-09-16'
api_count: 30
apis:
- description: 'CivicData.com is Accela''s free open-data platform for government agencies, described on its own site as "a free open data platform built by Accela" and "Built on open source using CKAN". It exposes a '
  name: CivicData Open Data API (CKAN) — END OF LIFE
  slug: civicdata-open-data-api-ckan-end-of-life
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: This is to return the version number of the AA server that is running, which allows the mobile app to make decisions as to what API's they have available.
  name: Accela AA Version API
  slug: accela-aa-version-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: An address provides details about the physical location of a parcel, building, contact, and so forth. An address is part of a property's APO (address, parcel, owner) information that is typically asso
  name: Accela Addresses API
  slug: accela-addresses-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Agencies API from Accela — 5 operation(s) for agencies.
  name: Accela Agencies API
  slug: accela-agencies-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The **announcements** API endpoints allow apps to get agency and public announcements, and mark them as read announcements.
  name: Accela Announcements API
  slug: accela-announcements-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: App settings are defined when a developer registers the app on [Accela Developer Portal](https://developer.accela.com). These settings include app name, ID, and so forth.
  name: Accela App Settings API
  slug: accela-app-settings-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: 'In Civic Platform, an assessment is synonymous to an asset condition assessment. An asset condition assessment is a scheduled maintenance review and/or a quality review of a group of assets. Agencies '
  name: Accela Assessments API
  slug: accela-assessments-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: An agency can define custom attributes for each type of assessment.
  name: Accela Assessments/Attributes API
  slug: accela-assessments-attributes-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: Inspectors can attach documents and photos as needed to the asset condition assessment record, and record the assignments and costs that occur on the assessment.
  name: Accela Assessments/Documents API
  slug: accela-assessments-documents-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: 'During an assessment, an inspector may make observations about the condition of the asset. For example, he may go to a certain area to look at the condition of the sidewalk and determine if there any '
  name: Accela Assessments/Observations API
  slug: accela-assessments-observations-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: Asset assessments often alert agencies to problems that need attention. A work order is the starting point in the repair process. Associating a work order with an assessment helps track the work order
  name: Accela Assessments/Work Orders API
  slug: accela-assessments-work-orders-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: 'Assets can be any object that an agency owns or maintains. Assets have standard properties such as date of service, start value, current value, depreciation value, salvage value, size, etc. To manage '
  name: Accela Assets API
  slug: accela-assets-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: Condition assessments apply to assets that change or deteriorate over time. These assets may require a visual condition assessment to effectively manage their life cycle. Transaction records and docum
  name: Accela Assets/Assessments API
  slug: accela-assets-assessments-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: In addition to these asset properties, assets can also have custom attributes which are customized characteristics of assets, structures, and establishments. Asset custom attributes can be grouped int
  name: Accela Assets/Attributes API
  slug: accela-assets-attributes-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: Document collaterals can be attached to assets.
  name: Accela Assets/Documents API
  slug: accela-assets-documents-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: Assets can be associated to transactional records when an asset assessment necessitates a service work order or if an application pertains to an agency asset.
  name: Accela Assets/Records API
  slug: accela-assets-records-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: API for batch API requests.
  name: Accela Batch API
  slug: accela-batch-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: A citizen user designates a delegate by first sending them an invitation. The invited citizen users can accept or reject invitations. When the invited citizen users accept the invitation, they officia
  name: Accela Citizen Access Delegate Invitations API
  slug: accela-citizen-access-delegate-invitations-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: description here
  name: Accela Citizen Access Delegate Management API
  slug: accela-citizen-access-delegate-management-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The **citizenaccess** API endpoints allow a logged-in Citizen Access user to register and manage his or her own account profile, status, and contacts.
  name: Accela Citizen Access Self-Registration API
  slug: accela-citizen-access-self-registration-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: description here
  name: Accela Citizen Access User Management API
  slug: accela-citizen-access-user-management-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The CivicId API from Accela — 3 operation(s) for civicid.
  name: Accela Civic ID API
  slug: accela-civicid-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: '**Conditions** The system provides standard conditions for different record types(permits, licenses, inspections, and so forth). Depending on the condition, condition violations result in one of the f'
  name: Accela Conditions API
  slug: accela-conditions-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Contacts/Addresses API from Accela — 2 operation(s) for contacts/addresses.
  name: Accela Contacts/Addresses API
  slug: accela-contacts-addresses-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: A reference contact captures information about people or organizations involved in a business process. Contacts include licensed professionals, such as contractors, architects, engineers, and develope
  name: Accela Contacts API
  slug: accela-contacts-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Contacts/Conditions API from Accela — 2 operation(s) for contacts/conditions.
  name: Accela Contacts/Conditions API
  slug: accela-contacts-conditions-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Contacts/Custom Forms API from Accela — 3 operation(s) for contacts/custom forms.
  name: Accela Contacts/Custom Forms API
  slug: accela-contacts-custom-forms-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Contacts/Custom Tables API from Accela — 3 operation(s) for contacts/custom tables.
  name: Accela Contacts/Custom Tables API
  slug: accela-contacts-custom-tables-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Contacts/Records API from Accela — 1 operation(s) for contacts/records.
  name: Accela Contacts/Records API
  slug: accela-contacts-records-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Documents API enables apps to upload and download documents, and attach a document to a record or inspection.
  name: Accela Documents API
  slug: accela-documents-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: 'Filters are user queries that are stored in Civic Platform and enable users to find information easily. Filters are configured in Civic Platform''s Data Filter Portlet to display only the data that is '
  name: Accela Filters API
  slug: accela-filters-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Geocoding API provides geo-coded address information based on map services configured on [Construct Admin Portal](https://admin.accela.com) > Agencies > {Agency} > Agency Settings > GIS Settings.
  name: Accela Geocoding API
  slug: accela-geocoding-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Gis API from Accela — 1 operation(s) for gis.
  name: Accela Gis API
  slug: accela-gis-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Inspections API from Accela — 15 operation(s) for inspections.
  name: Accela Inspections API
  slug: accela-inspections-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Inspections/Checklists API from Accela — 2 operation(s) for inspections/checklists.
  name: Accela Inspections/Checklists API
  slug: accela-inspections-checklists-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Inspections/Checklists/Checklist Items API from Accela — 6 operation(s) for inspections/checklists/checklist items.
  name: Accela Inspections/Checklists/Checklist Items API
  slug: accela-inspections-checklists-checklist-items-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Inspections/Checklists/Checklist Items/Custom Forms API from Accela — 3 operation(s) for inspections/checklists/checklist items/custom forms.
  name: Accela Inspections/Checklists/Checklist Items/Custom Forms API
  slug: accela-inspections-checklists-checklist-items-custom-forms-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Inspections/Checklists/Checklist Items/Custom Tables API from Accela — 4 operation(s) for inspections/checklists/checklist items/custom tables.
  name: Accela Inspections/Checklists/Checklist Items/Custom Tables API
  slug: accela-inspections-checklists-checklist-items-custom-tables-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Inspections/Condition Approvals API from Accela — 3 operation(s) for inspections/condition approvals.
  name: Accela Inspections/Condition Approvals API
  slug: accela-inspections-condition-approvals-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Inspections/Conditions API from Accela — 4 operation(s) for inspections/conditions.
  name: Accela Inspections/Conditions API
  slug: accela-inspections-conditions-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Inspections/Documents API from Accela — 2 operation(s) for inspections/documents.
  name: Accela Inspections/Documents API
  slug: accela-inspections-documents-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Inspections/Time Accounting API from Accela — 3 operation(s) for inspections/time accounting.
  name: Accela Inspections/Time Accounting API
  slug: accela-inspections-time-accounting-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Inspectors API from Accela — 2 operation(s) for inspectors.
  name: Accela Inspectors API
  slug: accela-inspectors-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: 'An invoice fee can either be generated manually in the Civic Platform''s Payment Processing portlet or automatically if configured in Civic Platform Administration. The Invoice API enables apps to get '
  name: Accela Invoices API
  slug: accela-invoices-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: API for tracking vehicle mileage associated with inspections.
  name: Accela Mileage API
  slug: accela-mileage-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: An owner defines an individual or entity related to a parcel so that the owner becomes the responsible party and point of contact for the parcel. The parcel owner must initiate or approve all work don
  name: Accela Owners API
  slug: accela-owners-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: A parcel defines a piece of land with a specific location and legally defined boundaries. The county assessor's office typically maintains information about all land parcels within its jurisdiction an
  name: Accela Parcels API
  slug: accela-parcels-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: Payments represent the acceptance of monetary funds submitted to the agency in relation to a transactional record. The system uses payments to invoice for services rendered and to create credit card t
  name: Accela Payments API
  slug: accela-payments-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: A professional is a contractor, architect, engineer, developer, or associated organization. The system requires that all professionals be licensed. Similar to reference contacts, licensed professional
  name: Accela Professionals API
  slug: accela-professionals-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Professionals/Conditions API from Accela — 1 operation(s) for professionals/conditions.
  name: Accela Professionals/Conditions API
  slug: accela-professionals-conditions-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Professionals/Records API from Accela — 1 operation(s) for professionals/records.
  name: Accela Professionals/Records API
  slug: accela-professionals-records-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: Activities related to a record can be assigned to a staff member when the activities require further action, such as a follow-up inspection or service maintenance.
  name: Accela Records/Activities API
  slug: accela-records-activities-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: A record can have at least one associated address, such as the address of the application contact or the location of a permit application, service request, or work order.
  name: Accela Records/Addresses API
  slug: accela-records-addresses-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Addresses/Custom Forms API from Accela — 2 operation(s) for records/addresses/custom forms.
  name: Accela Records/Addresses/Custom Forms API
  slug: accela-records-addresses-custom-forms-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: A record is a fundamental Civic Platform object that captures an agency's daily process tranactions, such as applications, permits, cases, licenses, service requests, and work orders.
  name: Accela Records API
  slug: accela-records-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: A work order record is linked to assets that require inspection, repair service, or any kind of task that needs to be performed and tracked in the system.
  name: Accela Records/Assets API
  slug: accela-records-assets-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: A staff user can add comments regarding the record, or can choose from standard comments that have been configured for the agency.
  name: Accela Records/Comments API
  slug: accela-records-comments-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Condition Approvals API from Accela — 3 operation(s) for records/condition approvals.
  name: Accela Records/Condition Approvals API
  slug: accela-records-condition-approvals-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: A condition is a requirement that you can apply to an application (or component of an application), that the application must fulfill to qualify for approval. Although conditions do not necessarily im
  name: Accela Records/Conditions API
  slug: accela-records-conditions-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: One or more reference contacts can be associated to an application or service request.
  name: Accela Records/Contacts API
  slug: accela-records-contacts-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Contacts/Custom Forms API from Accela — 3 operation(s) for records/contacts/custom forms.
  name: Accela Records/Contacts/Custom Forms API
  slug: accela-records-contacts-custom-forms-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Contacts/Custom Tables API from Accela — 3 operation(s) for records/contacts/custom tables.
  name: Accela Records/Contacts/Custom Tables API
  slug: accela-records-contacts-custom-tables-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Costs API from Accela — 2 operation(s) for records/costs.
  name: Accela Records/Costs API
  slug: accela-records-costs-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Custom Forms API from Accela — 3 operation(s) for records/custom forms.
  name: Accela Records/Custom Forms API
  slug: accela-records-custom-forms-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Custom Tables API from Accela — 4 operation(s) for records/custom tables.
  name: Accela Records/Custom Tables API
  slug: accela-records-custom-tables-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Documents API from Accela — 3 operation(s) for records/documents.
  name: Accela Records/Documents API
  slug: accela-records-documents-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Fees API from Accela — 2 operation(s) for records/fees.
  name: Accela Records/Fees API
  slug: accela-records-fees-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Inspections API from Accela — 2 operation(s) for records/inspections.
  name: Accela Records/Inspections API
  slug: accela-records-inspections-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Invoices API from Accela — 1 operation(s) for records/invoices.
  name: Accela Records/Invoices API
  slug: accela-records-invoices-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Owners API from Accela — 3 operation(s) for records/owners.
  name: Accela Records/Owners API
  slug: accela-records-owners-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Parcels API from Accela — 3 operation(s) for records/parcels.
  name: Accela Records/Parcels API
  slug: accela-records-parcels-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Part Transactions API from Accela — 2 operation(s) for records/part transactions.
  name: Accela Records/Part Transactions API
  slug: accela-records-part-transactions-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Payments API from Accela — 2 operation(s) for records/payments.
  name: Accela Records/Payments API
  slug: accela-records-payments-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Professionals API from Accela — 3 operation(s) for records/professionals.
  name: Accela Records/Professionals API
  slug: accela-records-professionals-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Trust Accounts API from Accela — 1 operation(s) for records/trust accounts.
  name: Accela Records/Trust Accounts API
  slug: accela-records-trust-accounts-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Votes API from Accela — 2 operation(s) for records/votes.
  name: Accela Records/Votes API
  slug: accela-records-votes-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Records/Workflows API from Accela — 7 operation(s) for records/workflows.
  name: Accela Records/Workflows API
  slug: accela-records-workflows-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: Civic Platform provides a set of standard reports, developed with reporting tools such as Crystal Reports, Microsoft Reporting Services. The Reports API sends requests to the report server to create r
  name: Accela Reports API
  slug: accela-reports-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Search API from Accela — 13 operation(s) for search.
  name: Accela Search API
  slug: accela-search-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Activities API from Accela — 3 operation(s) for settings/activities.
  name: Accela Settings/Activities API
  slug: accela-settings-activities-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Addresses API from Accela — 7 operation(s) for settings/addresses.
  name: Accela Settings/Addresses API
  slug: accela-settings-addresses-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Assessments API from Accela — 1 operation(s) for settings/assessments.
  name: Accela Settings/Assessments API
  slug: accela-settings-assessments-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Asset Types API from Accela — 5 operation(s) for settings/asset types.
  name: Accela Settings/Asset Types API
  slug: accela-settings-asset-types-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Assets API from Accela — 3 operation(s) for settings/assets.
  name: Accela Settings/Assets API
  slug: accela-settings-assets-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Comments API from Accela — 2 operation(s) for settings/comments.
  name: Accela Settings/Comments API
  slug: accela-settings-comments-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Conditions API from Accela — 4 operation(s) for settings/conditions.
  name: Accela Settings/Conditions API
  slug: accela-settings-conditions-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Contacts API from Accela — 7 operation(s) for settings/contacts.
  name: Accela Settings/Contacts API
  slug: accela-settings-contacts-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Costs API from Accela — 6 operation(s) for settings/costs.
  name: Accela Settings/Costs API
  slug: accela-settings-costs-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Departments API from Accela — 2 operation(s) for settings/departments.
  name: Accela Settings/Departments API
  slug: accela-settings-departments-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Documents API from Accela — 6 operation(s) for settings/documents.
  name: Accela Settings/Documents API
  slug: accela-settings-documents-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Drilldowns API from Accela — 1 operation(s) for settings/drilldowns.
  name: Accela Settings/Drilldowns API
  slug: accela-settings-drilldowns-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Inspections API from Accela — 12 operation(s) for settings/inspections.
  name: Accela Settings/Inspections API
  slug: accela-settings-inspections-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Modules API from Accela — 1 operation(s) for settings/modules.
  name: Accela Settings/Modules API
  slug: accela-settings-modules-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Owners API from Accela — 1 operation(s) for settings/owners.
  name: Accela Settings/Owners API
  slug: accela-settings-owners-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Parcels API from Accela — 1 operation(s) for settings/parcels.
  name: Accela Settings/Parcels API
  slug: accela-settings-parcels-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Parts API from Accela — 2 operation(s) for settings/parts.
  name: Accela Settings/Parts API
  slug: accela-settings-parts-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Pick Lists API from Accela — 2 operation(s) for settings/pick lists.
  name: Accela Settings/Pick Lists API
  slug: accela-settings-pick-lists-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Priorities API from Accela — 1 operation(s) for settings/priorities.
  name: Accela Settings/Priorities API
  slug: accela-settings-priorities-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Professsionals API from Accela — 3 operation(s) for settings/professsionals.
  name: Accela Settings/Professsionals API
  slug: accela-settings-professsionals-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Records API from Accela — 8 operation(s) for settings/records.
  name: Accela Settings/Records API
  slug: accela-settings-records-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Reports API from Accela — 3 operation(s) for settings/reports.
  name: Accela Settings/Reports API
  slug: accela-settings-reports-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The Settings/Time Accounting API from Accela — 2 operation(s) for settings/time accounting.
  name: Accela Settings/Time Accounting API
  slug: accela-settings-time-accounting-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: Shopping carts allow public users to add and manage multiple record payment transactions.A shopping cart contains attributes indicating the payment processing type and whether the shopping cart item i
  name: Accela Shopping Carts API
  slug: accela-shopping-carts-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: For general time accounting, Civic Platform provides the ability for employees to record the amount of time spent in performing their daily tasks, the descriptions and costs of materials used while pe
  name: Accela Time Accounting API
  slug: accela-time-accounting-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: Agency customers can deposit money into a trust account that the customer can drawn from when they need to pay fees for an application. This is helpful for customers that have a large amount of work t
  name: Accela Trust Accounts API
  slug: accela-trust-accounts-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: '**Agency Users** Although "users" is a broad and general term, the Accela API''s User object (user API resource) represents the agency user. An agency user is a staff member of the agency who logs in t'
  name: Accela Users API
  slug: accela-users-api
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: '**Workflow Tasks** A workflow is a sequence of tasks that agency users follow to process a record. When a user submits a new application, the system creates a record of a certain record type and launc'
  name: Accela Workflows API
  slug: accela-workflows-api
- baseURL: https://www.civicdata.com/api/3
  baseurl_source: declared
  description: The Oauth2 API from Accela — 3 operation(s) for oauth2.
  name: Accela Oauth2 API
  slug: accela-oauth2-api
- baseURL: https://www.civicdata.com/api/3
  baseurl_source: declared
  description: The Document Review API supports integration of the Civic Platform's Electronic Document Review ("EDR") feature with third-party document review tools.
  name: Accela Document Review API
  slug: accela-document-review-api
artifact_total: 114
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/overlays/accela-records-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/accela-records-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/security/accela-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accela-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.accela.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.accela.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.accela.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.accela.com/docs/api_reference/api-index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.accela.com/docs/construct-gettingStarted.html
- group: operate
  title: ''
  type: Support
  url: https://www.accela.com/services/technical-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://success.accela.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.accela.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.accela.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Accela-Inc
- group: start
  title: ''
  type: SignUp
  url: https://developer.accela.com/Register/Register
- group: start
  title: ''
  type: Login
  url: https://developer.accela.com/Login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.accela.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.accela.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.accela.com/docs/construct_api_v4_rel_notes.html
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/changelog/accela-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/accela-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.accela.com/civic-platform/security/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/llms/accela-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accela-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/well-known/accela-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/accela-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/authentication/accela-authentication.yml
  title: ''
  type: Authentication
  url: authentication/accela-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/scopes/accela-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/accela-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/conventions/accela-conventions.yml
  title: ''
  type: Conventions
  url: conventions/accela-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/errors/accela-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/accela-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/lifecycle/accela-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/accela-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/conformance/accela-conformance.yml
  title: ''
  type: Conformance
  url: conformance/accela-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/data-model/accela-data-model.yml
  title: ''
  type: DataModel
  url: data-model/accela-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/packages/accela-packages.yml
  title: ''
  type: Packages
  url: packages/accela-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/packages/accela-packages.yml
  title: ''
  type: SDKs
  url: packages/accela-packages.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/sandbox/accela-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/accela-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/plans/accela-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/accela-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/rate-limits/accela-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/accela-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accela/refs/heads/main/components/accela-components.yml
  title: ''
  type: Components
  url: components/accela-components.yml
created: '2026-09-06'
description: Accela is a San Ramon, California govtech company whose cloud Civic Platform runs permitting, planning, licensing, code enforcement, inspections, asset management and citizen service requests for state and local government agencies worldwide. Its public developer surface is the Accela Construct API (V4) — a 417-operation REST API served from apis.accela.com and documented as fifteen Swagger 2.0 documents on the Accela Developer Portal, covering records, inspections, contacts and professionals, addresses/parcels/owners, assets and assessments, documents, payments and shopping carts, reports, search, citizens, CivicID and platform settings. Access is OAuth 2.0 against auth.accela.com with agency- and environment-scoped tokens, and every request is bound to a specific government tenant through the x-accela-agency and x-accela-environment headers.
image: https://www.accela.com/wp-content/uploads/2026/07/AccelaLogo-website.webp
layout: provider
modified: '2026-09-06'
name: Accela
nav: Providers
network: true
overview: 'Accela publishes 108 APIs on the [APIs.io](https://apis.io/) network, including AA Version API, Addresses API, Agencies API, and 105 more. Tagged areas include GovTech, Government, Permitting, Licensing, and Code Enforcement.


  Accela''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 28 more developer resources.'
plans:
- name: Accela Plans Pricing
  plan_count: 0
  slug: accela-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Accela Rate Limits
  slug: accela-rate-limits
scopes:
- name: Accela Scopes
  scope_count: 0
  slug: accela-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 49.7
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 18.4
  previous_composite: 57.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 108
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 88.9
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Accela Authentication
  slug: accela-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Accela Domain Security
  slug: accela-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: accela
tags:
- GovTech
- Government
- Permitting
- Licensing
- Code Enforcement
- Inspection
- Asset Management
- Citizen Engagement
- Land Management
- Civic Platform
- Public Sector
- Software-as-a-Service
website: https://www.accela.com/
---
