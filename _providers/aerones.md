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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.4
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: The GraphQL surface of the Aerones Operations Hub, served at /graphql with anonymous introspection enabled and the full SDL published as text/plain at /api/graphql-schema. 1,524 types, 339 Query field
  name: Aerones Operations Hub GraphQL API
  slug: aerones-operations-hub-graphql
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The accounting API from Aerones — 11 operation(s) for accounting.
  name: Aerones Accounting API
  slug: aerones-accounting-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The accounting.billing-statements API from Aerones — 2 operation(s) for accounting.billing-statements.
  name: Aerones Accounting.billing Statements API
  slug: aerones-accounting-billing-statements-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The accounting.netsuite-departments API from Aerones — 1 operation(s) for accounting.netsuite-departments.
  name: Aerones Accounting.netsuite Departments API
  slug: aerones-accounting-netsuite-departments-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The accounting.notes API from Aerones — 2 operation(s) for accounting.notes.
  name: Aerones Accounting.notes API
  slug: aerones-accounting-notes-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The accounting.sales-invoices API from Aerones — 2 operation(s) for accounting.sales-invoices.
  name: Aerones Accounting.sales Invoices API
  slug: aerones-accounting-sales-invoices-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The accounting.sales-order-lines API from Aerones — 2 operation(s) for accounting.sales-order-lines.
  name: Aerones Accounting.sales Order Lines API
  slug: aerones-accounting-sales-order-lines-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The accounting.sales-orders API from Aerones — 2 operation(s) for accounting.sales-orders.
  name: Aerones Accounting.sales Orders API
  slug: aerones-accounting-sales-orders-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The accounting.service-charges API from Aerones — 2 operation(s) for accounting.service-charges.
  name: Aerones Accounting.service Charges API
  slug: aerones-accounting-service-charges-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The active-workload API from Aerones — 5 operation(s) for active-workload.
  name: Aerones Active Workload API
  slug: aerones-active-workload-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The auth API from Aerones — 4 operation(s) for auth.
  name: Aerones Auth API
  slug: aerones-auth-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The bamboohr.employees API from Aerones — 1 operation(s) for bamboohr.employees.
  name: Aerones Bamboohr.employees API
  slug: aerones-bamboohr-employees-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The bto.crew API from Aerones — 4 operation(s) for bto.crew.
  name: Aerones Bto.crew API
  slug: aerones-bto-crew-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The bto.travel-orders API from Aerones — 9 operation(s) for bto.travel-orders.
  name: Aerones Bto.travel Orders API
  slug: aerones-bto-travel-orders-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The commercial-offers API from Aerones — 2 operation(s) for commercial-offers.
  name: Aerones Commercial Offers API
  slug: aerones-commercial-offers-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The confluence API from Aerones — 1 operation(s) for confluence.
  name: Aerones Confluence API
  slug: aerones-confluence-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.anomalies API from Aerones — 14 operation(s) for core.anomalies.
  name: Aerones Core.anomalies API
  slug: aerones-core-anomalies-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.blade-diagrams API from Aerones — 2 operation(s) for core.blade-diagrams.
  name: Aerones Core.blade Diagrams API
  slug: aerones-core-blade-diagrams-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.business-regions API from Aerones — 1 operation(s) for core.business-regions.
  name: Aerones Core.business Regions API
  slug: aerones-core-business-regions-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.certificate-categories API from Aerones — 2 operation(s) for core.certificate-categories.
  name: Aerones Core.certificate Categories API
  slug: aerones-core-certificate-categories-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.certificate-expenses API from Aerones — 2 operation(s) for core.certificate-expenses.
  name: Aerones Core.certificate Expenses API
  slug: aerones-core-certificate-expenses-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.certificate-issuers API from Aerones — 2 operation(s) for core.certificate-issuers.
  name: Aerones Core.certificate Issuers API
  slug: aerones-core-certificate-issuers-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.certificate-offerings API from Aerones — 2 operation(s) for core.certificate-offerings.
  name: Aerones Core.certificate Offerings API
  slug: aerones-core-certificate-offerings-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.certificate-requirements API from Aerones — 4 operation(s) for core.certificate-requirements.
  name: Aerones Core.certificate Requirements API
  slug: aerones-core-certificate-requirements-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.certificates API from Aerones — 2 operation(s) for core.certificates.
  name: Aerones Core.certificates API
  slug: aerones-core-certificates-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.commercial-offers API from Aerones — 2 operation(s) for core.commercial-offers.
  name: Aerones Core.commercial Offers API
  slug: aerones-core-commercial-offers-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.component-models API from Aerones — 2 operation(s) for core.component-models.
  name: Aerones Core.component Models API
  slug: aerones-core-component-models-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.component-types API from Aerones — 1 operation(s) for core.component-types.
  name: Aerones Core.component Types API
  slug: aerones-core-component-types-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.countries API from Aerones — 1 operation(s) for core.countries.
  name: Aerones Core.countries API
  slug: aerones-core-countries-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.cross-sections API from Aerones — 2 operation(s) for core.cross-sections.
  name: Aerones Core.cross Sections API
  slug: aerones-core-cross-sections-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.currencies API from Aerones — 1 operation(s) for core.currencies.
  name: Aerones Core.currencies API
  slug: aerones-core-currencies-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.customer-locations API from Aerones — 1 operation(s) for core.customer-locations.
  name: Aerones Core.customer Locations API
  slug: aerones-core-customer-locations-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.customers.addresses API from Aerones — 2 operation(s) for core.customers.addresses.
  name: Aerones Core.customers.addresses API
  slug: aerones-core-customers-addresses-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.customers.anomaly-client-fields API from Aerones — 3 operation(s) for core.customers.anomaly-client-fields.
  name: Aerones Core.customers.anomaly Client Fields API
  slug: aerones-core-customers-anomaly-client-fields-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.customers API from Aerones — 3 operation(s) for core.customers.
  name: Aerones Core.customers API
  slug: aerones-core-customers-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.customers.bank-accounts API from Aerones — 2 operation(s) for core.customers.bank-accounts.
  name: Aerones Core.customers.bank Accounts API
  slug: aerones-core-customers-bank-accounts-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.customers.contacts API from Aerones — 2 operation(s) for core.customers.contacts.
  name: Aerones Core.customers.contacts API
  slug: aerones-core-customers-contacts-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.customers.locations API from Aerones — 2 operation(s) for core.customers.locations.
  name: Aerones Core.customers.locations API
  slug: aerones-core-customers-locations-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.customers.roles API from Aerones — 1 operation(s) for core.customers.roles.
  name: Aerones Core.customers.roles API
  slug: aerones-core-customers-roles-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.customers.turbines API from Aerones — 2 operation(s) for core.customers.turbines.
  name: Aerones Core.customers.turbines API
  slug: aerones-core-customers-turbines-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.customers.users API from Aerones — 2 operation(s) for core.customers.users.
  name: Aerones Core.customers.users API
  slug: aerones-core-customers-users-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.delay-categories API from Aerones — 2 operation(s) for core.delay-categories.
  name: Aerones Core.delay Categories API
  slug: aerones-core-delay-categories-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.delay-types API from Aerones — 2 operation(s) for core.delay-types.
  name: Aerones Core.delay Types API
  slug: aerones-core-delay-types-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.delays API from Aerones — 2 operation(s) for core.delays.
  name: Aerones Core.delays API
  slug: aerones-core-delays-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.erp-part-codes API from Aerones — 1 operation(s) for core.erp-part-codes.
  name: Aerones Core.erp Part Codes API
  slug: aerones-core-erp-part-codes-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.erp-parts API from Aerones — 2 operation(s) for core.erp-parts.
  name: Aerones Core.erp Parts API
  slug: aerones-core-erp-parts-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.file-entity-links API from Aerones — 2 operation(s) for core.file-entity-links.
  name: Aerones Core.file Entity Links API
  slug: aerones-core-file-entity-links-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.files API from Aerones — 6 operation(s) for core.files.
  name: Aerones Core.files API
  slug: aerones-core-files-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.item-categories API from Aerones — 1 operation(s) for core.item-categories.
  name: Aerones Core.item Categories API
  slug: aerones-core-item-categories-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.locations API from Aerones — 3 operation(s) for core.locations.
  name: Aerones Core.locations API
  slug: aerones-core-locations-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.manufacturers API from Aerones — 2 operation(s) for core.manufacturers.
  name: Aerones Core.manufacturers API
  slug: aerones-core-manufacturers-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.notifications API from Aerones — 6 operation(s) for core.notifications.
  name: Aerones Core.notifications API
  slug: aerones-core-notifications-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.pipedrive-deals API from Aerones — 1 operation(s) for core.pipedrive-deals.
  name: Aerones Core.pipedrive Deals API
  slug: aerones-core-pipedrive-deals-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.planned-resource-set-items.commitments API from Aerones — 2 operation(s) for core.planned-resource-set-items.commitments.
  name: Aerones Core.planned Resource Set Items.commitments API
  slug: aerones-core-planned-resource-set-items-commitments-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.planned-resource-sets.items API from Aerones — 2 operation(s) for core.planned-resource-sets.items.
  name: Aerones Core.planned Resource Sets.items API
  slug: aerones-core-planned-resource-sets-items-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.positions API from Aerones — 2 operation(s) for core.positions.
  name: Aerones Core.positions API
  slug: aerones-core-positions-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.pricing-units API from Aerones — 1 operation(s) for core.pricing-units.
  name: Aerones Core.pricing Units API
  slug: aerones-core-pricing-units-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.project-question-configs API from Aerones — 1 operation(s) for core.project-question-configs.
  name: Aerones Core.project Question Configs API
  slug: aerones-core-project-question-configs-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.project-scope-change-requests API from Aerones — 5 operation(s) for core.project-scope-change-requests.
  name: Aerones Core.project Scope Change Requests API
  slug: aerones-core-project-scope-change-requests-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.project-status API from Aerones — 1 operation(s) for core.project-status.
  name: Aerones Core.project Status API
  slug: aerones-core-project-status-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.projects API from Aerones — 11 operation(s) for core.projects.
  name: Aerones Core.projects API
  slug: aerones-core-projects-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.projects.billings API from Aerones — 2 operation(s) for core.projects.billings.
  name: Aerones Core.projects.billings API
  slug: aerones-core-projects-billings-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.projects.bto API from Aerones — 5 operation(s) for core.projects.bto.
  name: Aerones Core.projects.bto API
  slug: aerones-core-projects-bto-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.projects.communication API from Aerones — 5 operation(s) for core.projects.communication.
  name: Aerones Core.projects.communication API
  slug: aerones-core-projects-communication-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.projects.contacts API from Aerones — 2 operation(s) for core.projects.contacts.
  name: Aerones Core.projects.contacts API
  slug: aerones-core-projects-contacts-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.projects.locations API from Aerones — 6 operation(s) for core.projects.locations.
  name: Aerones Core.projects.locations API
  slug: aerones-core-projects-locations-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.projects.offers API from Aerones — 10 operation(s) for core.projects.offers.
  name: Aerones Core.projects.offers API
  slug: aerones-core-projects-offers-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.projects.offers.items API from Aerones — 3 operation(s) for core.projects.offers.items.
  name: Aerones Core.projects.offers.items API
  slug: aerones-core-projects-offers-items-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.projects.planned-resource-sets API from Aerones — 2 operation(s) for core.projects.planned-resource-sets.
  name: Aerones Core.projects.planned Resource Sets API
  slug: aerones-core-projects-planned-resource-sets-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.projects.pre-job-answers API from Aerones — 3 operation(s) for core.projects.pre-job-answers.
  name: Aerones Core.projects.pre Job Answers API
  slug: aerones-core-projects-pre-job-answers-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.projects.pre-job-sites API from Aerones — 1 operation(s) for core.projects.pre-job-sites.
  name: Aerones Core.projects.pre Job Sites API
  slug: aerones-core-projects-pre-job-sites-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.projects.readiness API from Aerones — 1 operation(s) for core.projects.readiness.
  name: Aerones Core.projects.readiness API
  slug: aerones-core-projects-readiness-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.projects.report-types API from Aerones — 2 operation(s) for core.projects.report-types.
  name: Aerones Core.projects.report Types API
  slug: aerones-core-projects-report-types-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.projects.resource-sets API from Aerones — 4 operation(s) for core.projects.resource-sets.
  name: Aerones Core.projects.resource Sets API
  slug: aerones-core-projects-resource-sets-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.projects.rfi-billing API from Aerones — 1 operation(s) for core.projects.rfi-billing.
  name: Aerones Core.projects.rfi Billing API
  slug: aerones-core-projects-rfi-billing-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.projects.scope-items API from Aerones — 3 operation(s) for core.projects.scope-items.
  name: Aerones Core.projects.scope Items API
  slug: aerones-core-projects-scope-items-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.purchase-orders API from Aerones — 2 operation(s) for core.purchase-orders.
  name: Aerones Core.purchase Orders API
  slug: aerones-core-purchase-orders-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.purchase-orders.projects API from Aerones — 2 operation(s) for core.purchase-orders.projects.
  name: Aerones Core.purchase Orders.projects API
  slug: aerones-core-purchase-orders-projects-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.purchase-orders.versions API from Aerones — 3 operation(s) for core.purchase-orders.versions.
  name: Aerones Core.purchase Orders.versions API
  slug: aerones-core-purchase-orders-versions-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.regions API from Aerones — 1 operation(s) for core.regions.
  name: Aerones Core.regions API
  slug: aerones-core-regions-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.relationship-types API from Aerones — 1 operation(s) for core.relationship-types.
  name: Aerones Core.relationship Types API
  slug: aerones-core-relationship-types-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.report-types API from Aerones — 1 operation(s) for core.report-types.
  name: Aerones Core.report Types API
  slug: aerones-core-report-types-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.resource-sets API from Aerones — 2 operation(s) for core.resource-sets.
  name: Aerones Core.resource Sets API
  slug: aerones-core-resource-sets-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.resources API from Aerones — 3 operation(s) for core.resources.
  name: Aerones Core.resources API
  slug: aerones-core-resources-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.resources.certificates API from Aerones — 2 operation(s) for core.resources.certificates.
  name: Aerones Core.resources.certificates API
  slug: aerones-core-resources-certificates-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.resources.service-positions API from Aerones — 2 operation(s) for core.resources.service-positions.
  name: Aerones Core.resources.service Positions API
  slug: aerones-core-resources-service-positions-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.robot-sets API from Aerones — 3 operation(s) for core.robot-sets.
  name: Aerones Core.robot Sets API
  slug: aerones-core-robot-sets-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.robot-sets.services API from Aerones — 1 operation(s) for core.robot-sets.services.
  name: Aerones Core.robot Sets.services API
  slug: aerones-core-robot-sets-services-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.service-categories API from Aerones — 1 operation(s) for core.service-categories.
  name: Aerones Core.service Categories API
  slug: aerones-core-service-categories-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.service-families API from Aerones — 1 operation(s) for core.service-families.
  name: Aerones Core.service Families API
  slug: aerones-core-service-families-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.service-groups API from Aerones — 1 operation(s) for core.service-groups.
  name: Aerones Core.service Groups API
  slug: aerones-core-service-groups-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.service-order-lines.lps-results API from Aerones — 1 operation(s) for core.service-order-lines.lps-results.
  name: Aerones Core.service Order Lines.lps Results API
  slug: aerones-core-service-order-lines-lps-results-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.service-standard-items API from Aerones — 2 operation(s) for core.service-standard-items.
  name: Aerones Core.service Standard Items API
  slug: aerones-core-service-standard-items-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.services API from Aerones — 2 operation(s) for core.services.
  name: Aerones Core.services API
  slug: aerones-core-services-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.services.pricing-units API from Aerones — 1 operation(s) for core.services.pricing-units.
  name: Aerones Core.services.pricing Units API
  slug: aerones-core-services-pricing-units-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.services.related-services API from Aerones — 1 operation(s) for core.services.related-services.
  name: Aerones Core.services.related Services API
  slug: aerones-core-services-related-services-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.standards API from Aerones — 1 operation(s) for core.standards.
  name: Aerones Core.standards API
  slug: aerones-core-standards-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.timezones API from Aerones — 1 operation(s) for core.timezones.
  name: Aerones Core.timezones API
  slug: aerones-core-timezones-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.turbine-components API from Aerones — 5 operation(s) for core.turbine-components.
  name: Aerones Core.turbine Components API
  slug: aerones-core-turbine-components-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.turbine-components.receptors API from Aerones — 1 operation(s) for core.turbine-components.receptors.
  name: Aerones Core.turbine Components.receptors API
  slug: aerones-core-turbine-components-receptors-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.turbine-models API from Aerones — 2 operation(s) for core.turbine-models.
  name: Aerones Core.turbine Models API
  slug: aerones-core-turbine-models-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.turbine-models.receptor-presets API from Aerones — 3 operation(s) for core.turbine-models.receptor-presets.
  name: Aerones Core.turbine Models.receptor Presets API
  slug: aerones-core-turbine-models-receptor-presets-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.turbines API from Aerones — 4 operation(s) for core.turbines.
  name: Aerones Core.turbines API
  slug: aerones-core-turbines-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.turbines.receptors API from Aerones — 2 operation(s) for core.turbines.receptors.
  name: Aerones Core.turbines.receptors API
  slug: aerones-core-turbines-receptors-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.users API from Aerones — 4 operation(s) for core.users.
  name: Aerones Core.users API
  slug: aerones-core-users-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The core.vendors API from Aerones — 2 operation(s) for core.vendors.
  name: Aerones Core.vendors API
  slug: aerones-core-vendors-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The customer-portal API from Aerones — 2 operation(s) for customer-portal.
  name: Aerones Customer Portal API
  slug: aerones-customer-portal-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The data-tracking API from Aerones — 3 operation(s) for data-tracking.
  name: Aerones Data Tracking API
  slug: aerones-data-tracking-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The deviations API from Aerones — 6 operation(s) for deviations.
  name: Aerones Deviations API
  slug: aerones-deviations-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The dispatch.board-annotations API from Aerones — 8 operation(s) for dispatch.board-annotations.
  name: Aerones Dispatch.board Annotations API
  slug: aerones-dispatch-board-annotations-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The dispatch.board API from Aerones — 14 operation(s) for dispatch.board.
  name: Aerones Dispatch.board API
  slug: aerones-dispatch-board-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The dispatch.board-workorders API from Aerones — 18 operation(s) for dispatch.board-workorders.
  name: Aerones Dispatch.board Workorders API
  slug: aerones-dispatch-board-workorders-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The dispatch.scope-commitments API from Aerones — 10 operation(s) for dispatch.scope-commitments.
  name: Aerones Dispatch.scope Commitments API
  slug: aerones-dispatch-scope-commitments-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The dispatch.services API from Aerones — 15 operation(s) for dispatch.services.
  name: Aerones Dispatch.services API
  slug: aerones-dispatch-services-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The dispatch.workorder-activity-metadata API from Aerones — 2 operation(s) for dispatch.workorder-activity-metadata.
  name: Aerones Dispatch.workorder Activity Metadata API
  slug: aerones-dispatch-workorder-activity-metadata-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The dispatch.workorders API from Aerones — 16 operation(s) for dispatch.workorders.
  name: Aerones Dispatch.workorders API
  slug: aerones-dispatch-workorders-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The docs API from Aerones — 1 operation(s) for docs.
  name: Aerones Docs API
  slug: aerones-docs-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The email API from Aerones — 4 operation(s) for email.
  name: Aerones Email API
  slug: aerones-email-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The files API from Aerones — 4 operation(s) for files.
  name: Aerones Files API
  slug: aerones-files-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The maintainx.assets API from Aerones — 1 operation(s) for maintainx.assets.
  name: Aerones Maintainx.assets API
  slug: aerones-maintainx-assets-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The misc API from Aerones — 10 operation(s) for misc.
  name: Aerones Misc API
  slug: aerones-misc-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The netsuite API from Aerones — 6 operation(s) for netsuite.
  name: Aerones Netsuite API
  slug: aerones-netsuite-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The notifications.events API from Aerones — 1 operation(s) for notifications.events.
  name: Aerones Notifications.events API
  slug: aerones-notifications-events-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The payroll API from Aerones — 3 operation(s) for payroll.
  name: Aerones Payroll API
  slug: aerones-payroll-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The planning API from Aerones — 2 operation(s) for planning.
  name: Aerones Planning API
  slug: aerones-planning-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The planning.campaigns API from Aerones — 2 operation(s) for planning.campaigns.
  name: Aerones Planning.campaigns API
  slug: aerones-planning-campaigns-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The planning.customer-vendors API from Aerones — 2 operation(s) for planning.customer-vendors.
  name: Aerones Planning.customer Vendors API
  slug: aerones-planning-customer-vendors-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The planning.projects API from Aerones — 2 operation(s) for planning.projects.
  name: Aerones Planning.projects API
  slug: aerones-planning-projects-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The planning.service-orders API from Aerones — 2 operation(s) for planning.service-orders.
  name: Aerones Planning.service Orders API
  slug: aerones-planning-service-orders-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The planning.services API from Aerones — 2 operation(s) for planning.services.
  name: Aerones Planning.services API
  slug: aerones-planning-services-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The planning.statuses API from Aerones — 1 operation(s) for planning.statuses.
  name: Aerones Planning.statuses API
  slug: aerones-planning-statuses-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The planning.work-order-types API from Aerones — 2 operation(s) for planning.work-order-types.
  name: Aerones Planning.work Order Types API
  slug: aerones-planning-work-order-types-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The planning.work-orders API from Aerones — 2 operation(s) for planning.work-orders.
  name: Aerones Planning.work Orders API
  slug: aerones-planning-work-orders-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The platform API from Aerones — 2 operation(s) for platform.
  name: Aerones Platform API
  slug: aerones-platform-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.accounting API from Aerones — 37 operation(s) for projects.accounting.
  name: Aerones Projects.accounting API
  slug: aerones-projects-accounting-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.bto API from Aerones — 1 operation(s) for projects.bto.
  name: Aerones Projects.bto API
  slug: aerones-projects-bto-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.core API from Aerones — 8 operation(s) for projects.core.
  name: Aerones Projects.core API
  slug: aerones-projects-core-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.offer API from Aerones — 5 operation(s) for projects.offer.
  name: Aerones Projects.offer API
  slug: aerones-projects-offer-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.offer.changelog API from Aerones — 6 operation(s) for projects.offer.changelog.
  name: Aerones Projects.offer.changelog API
  slug: aerones-projects-offer-changelog-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.overview API from Aerones — 2 operation(s) for projects.overview.
  name: Aerones Projects.overview API
  slug: aerones-projects-overview-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.platform API from Aerones — 1 operation(s) for projects.platform.
  name: Aerones Projects.platform API
  slug: aerones-projects-platform-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.pre-job API from Aerones — 1 operation(s) for projects.pre-job.
  name: Aerones Projects.pre Job API
  slug: aerones-projects-pre-job-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.pre-job.assets-services API from Aerones — 1 operation(s) for projects.pre-job.assets-services.
  name: Aerones Projects.pre Job.assets Services API
  slug: aerones-projects-pre-job-assets-services-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.pre-job.assets-services.table API from Aerones — 4 operation(s) for projects.pre-job.assets-services.table.
  name: Aerones Projects.pre Job.assets Services.table API
  slug: aerones-projects-pre-job-assets-services-table-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.rams API from Aerones — 20 operation(s) for projects.rams.
  name: Aerones Projects.rams API
  slug: aerones-projects-rams-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.rams-templates API from Aerones — 6 operation(s) for projects.rams-templates.
  name: Aerones Projects.rams Templates API
  slug: aerones-projects-rams-templates-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.reporting-requirements API from Aerones — 4 operation(s) for projects.reporting-requirements.
  name: Aerones Projects.reporting Requirements API
  slug: aerones-projects-reporting-requirements-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.rfi API from Aerones — 7 operation(s) for projects.rfi.
  name: Aerones Projects.rfi API
  slug: aerones-projects-rfi-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.robot-sets-and-teams API from Aerones — 4 operation(s) for projects.robot-sets-and-teams.
  name: Aerones Projects.robot Sets And Teams API
  slug: aerones-projects-robot-sets-and-teams-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.service-orders API from Aerones — 20 operation(s) for projects.service-orders.
  name: Aerones Projects.service Orders API
  slug: aerones-projects-service-orders-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.set-demobs API from Aerones — 8 operation(s) for projects.set-demobs.
  name: Aerones Projects.set Demobs API
  slug: aerones-projects-set-demobs-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.set-requests API from Aerones — 21 operation(s) for projects.set-requests.
  name: Aerones Projects.set Requests API
  slug: aerones-projects-set-requests-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.team-requests API from Aerones — 21 operation(s) for projects.team-requests.
  name: Aerones Projects.team Requests API
  slug: aerones-projects-team-requests-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.upcoming-rotations API from Aerones — 1 operation(s) for projects.upcoming-rotations.
  name: Aerones Projects.upcoming Rotations API
  slug: aerones-projects-upcoming-rotations-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.weather API from Aerones — 4 operation(s) for projects.weather.
  name: Aerones Projects.weather API
  slug: aerones-projects-weather-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The projects.workorders API from Aerones — 2 operation(s) for projects.workorders.
  name: Aerones Projects.workorders API
  slug: aerones-projects-workorders-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The readiness API from Aerones — 1 operation(s) for readiness.
  name: Aerones Readiness API
  slug: aerones-readiness-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The reporting-requirements.cru API from Aerones — 9 operation(s) for reporting-requirements.cru.
  name: Aerones Reporting Requirements.cru API
  slug: aerones-reporting-requirements-cru-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The reports API from Aerones — 7 operation(s) for reports.
  name: Aerones Reports API
  slug: aerones-reports-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The resource-mobilization.obd-gps-devices API from Aerones — 6 operation(s) for resource-mobilization.obd-gps-devices.
  name: Aerones Resource Mobilization.obd Gps Devices API
  slug: aerones-resource-mobilization-obd-gps-devices-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The resource-mobilization.vehicle-fleet-assignments API from Aerones — 11 operation(s) for resource-mobilization.vehicle-fleet-assignments.
  name: Aerones Resource Mobilization.vehicle Fleet Assignments API
  slug: aerones-resource-mobilization-vehicle-fleet-assignments-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The resource-mobilization.vehicle-fleet-invoices API from Aerones — 6 operation(s) for resource-mobilization.vehicle-fleet-invoices.
  name: Aerones Resource Mobilization.vehicle Fleet Invoices API
  slug: aerones-resource-mobilization-vehicle-fleet-invoices-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The resource-mobilization.vehicle-fleet-locations API from Aerones — 2 operation(s) for resource-mobilization.vehicle-fleet-locations.
  name: Aerones Resource Mobilization.vehicle Fleet Locations API
  slug: aerones-resource-mobilization-vehicle-fleet-locations-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The resource-mobilization.vehicles API from Aerones — 7 operation(s) for resource-mobilization.vehicles.
  name: Aerones Resource Mobilization.vehicles API
  slug: aerones-resource-mobilization-vehicles-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The services API from Aerones — 3 operation(s) for services.
  name: Aerones Services API
  slug: aerones-services-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The talentlms.users API from Aerones — 1 operation(s) for talentlms.users.
  name: Aerones Talentlms.users API
  slug: aerones-talentlms-users-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The technician.projects API from Aerones — 3 operation(s) for technician.projects.
  name: Aerones Technician.projects API
  slug: aerones-technician-projects-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The technician.reports API from Aerones — 11 operation(s) for technician.reports.
  name: Aerones Technician.reports API
  slug: aerones-technician-reports-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The technician.service_results API from Aerones — 8 operation(s) for technician.service_results.
  name: Aerones Technician.service Results API
  slug: aerones-technician-service-results-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The technician.workorders API from Aerones — 6 operation(s) for technician.workorders.
  name: Aerones Technician.workorders API
  slug: aerones-technician-workorders-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The turbines API from Aerones — 7 operation(s) for turbines.
  name: Aerones Turbines API
  slug: aerones-turbines-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The users API from Aerones — 2 operation(s) for users.
  name: Aerones Users API
  slug: aerones-users-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The utilities API from Aerones — 1 operation(s) for utilities.
  name: Aerones Utilities API
  slug: aerones-utilities-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The vis.ai-anomalies API from Aerones — 5 operation(s) for vis.ai-anomalies.
  name: Aerones Vis.ai Anomalies API
  slug: aerones-vis-ai-anomalies-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The vis.external-photos API from Aerones — 1 operation(s) for vis.external-photos.
  name: Aerones Vis.external Photos API
  slug: aerones-vis-external-photos-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The vis.inspections API from Aerones — 4 operation(s) for vis.inspections.
  name: Aerones Vis.inspections API
  slug: aerones-vis-inspections-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The vis.pointclouds API from Aerones — 1 operation(s) for vis.pointclouds.
  name: Aerones Vis.pointclouds API
  slug: aerones-vis-pointclouds-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The vis.root-photos API from Aerones — 1 operation(s) for vis.root-photos.
  name: Aerones Vis.root Photos API
  slug: aerones-vis-root-photos-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The vis.rosbags API from Aerones — 2 operation(s) for vis.rosbags.
  name: Aerones Vis.rosbags API
  slug: aerones-vis-rosbags-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The vis.video-files API from Aerones — 3 operation(s) for vis.video-files.
  name: Aerones Vis.video Files API
  slug: aerones-vis-video-files-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The webhooks API from Aerones — 5 operation(s) for webhooks.
  name: Aerones Webhooks API
  slug: aerones-webhooks-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The webhooks.travel API from Aerones — 1 operation(s) for webhooks.travel.
  name: Aerones Webhooks.travel API
  slug: aerones-webhooks-travel-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The webhooks.wms API from Aerones — 1 operation(s) for webhooks.wms.
  name: Aerones Webhooks.wms API
  slug: aerones-webhooks-wms-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The wms API from Aerones — 6 operation(s) for wms.
  name: Aerones Wms API
  slug: aerones-wms-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The work-management.activities API from Aerones — 7 operation(s) for work-management.activities.
  name: Aerones Work Management.activities API
  slug: aerones-work-management-activities-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The work-management.activity-templates API from Aerones — 2 operation(s) for work-management.activity-templates.
  name: Aerones Work Management.activity Templates API
  slug: aerones-work-management-activity-templates-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The work-management.anomaly-work-orders API from Aerones — 2 operation(s) for work-management.anomaly-work-orders.
  name: Aerones Work Management.anomaly Work Orders API
  slug: aerones-work-management-anomaly-work-orders-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The work-management.campaigns API from Aerones — 7 operation(s) for work-management.campaigns.
  name: Aerones Work Management.campaigns API
  slug: aerones-work-management-campaigns-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The work-management.client-work-orders API from Aerones — 8 operation(s) for work-management.client-work-orders.
  name: Aerones Work Management.client Work Orders API
  slug: aerones-work-management-client-work-orders-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The work-management.statuses API from Aerones — 1 operation(s) for work-management.statuses.
  name: Aerones Work Management.statuses API
  slug: aerones-work-management-statuses-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The work-management.task-types API from Aerones — 2 operation(s) for work-management.task-types.
  name: Aerones Work Management.task Types API
  slug: aerones-work-management-task-types-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The work-management.vendors API from Aerones — 2 operation(s) for work-management.vendors.
  name: Aerones Work Management.vendors API
  slug: aerones-work-management-vendors-api
- baseURL: https://operations.aerones.com/api
  baseurl_source: declared
  description: The work-management.work-packages API from Aerones — 8 operation(s) for work-management.work-packages.
  name: Aerones Work Management.work Packages API
  slug: aerones-work-management-work-packages-api
artifact_total: 200
asyncapis:
- description: ''
  name: Aerones Event Surface
  slug: aerones-event-surface
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aerones/refs/heads/main/overlays/aerones-operations-hub-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aerones-operations-hub-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://aerones.com/
- group: docs
  title: ''
  type: APIReference
  url: https://operations.aerones.com/api/docs
- group: start
  title: ''
  type: Login
  url: https://portal.aerones.com/
- group: operate
  title: ''
  type: Support
  url: https://aerones.com/our-contacts/
- group: company
  title: ''
  type: Blog
  url: https://aerones.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://aerones.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aerones.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aerones.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://aerones.com/certification/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aerones/refs/heads/main/llms/aerones-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aerones-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aerones/refs/heads/main/well-known/aerones-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aerones-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aerones/refs/heads/main/authentication/aerones-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aerones-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aerones/refs/heads/main/scopes/aerones-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aerones-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aerones/refs/heads/main/conformance/aerones-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aerones-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aerones/refs/heads/main/lifecycle/aerones-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aerones-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aerones/refs/heads/main/security/aerones-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aerones-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aerones/refs/heads/main/mcp/aerones-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aerones-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aerones/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aerones/refs/heads/main/plans/aerones-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aerones-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aerones/refs/heads/main/rate-limits/aerones-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aerones-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aerones/refs/heads/main/packages/aerones-packages.yml
  title: ''
  type: Packages
  url: packages/aerones-packages.yml
created: '2026-09-10'
description: Aerones is a Latvian robotics company that performs wind turbine blade inspection, cleaning, coating, leading-edge repair and lightning-protection testing with cable-suspended robots and autonomous drones, operating onshore and offshore for owners and OEMs including NextEra, GE, Vestas, Enel and Siemens Gamesa. Its software side is the Operations Hub — a Django Ninja backend behind portal.aerones.com that publishes an unauthenticated OpenAPI 3.1.0 description (760 paths, 1,114 operations, 1,377 schemas) alongside a companion GraphQL schema (339 queries, 325 mutations, 4 subscriptions), covering turbines, blades, anomalies, robot sets, work orders, dispatch, projects, inspections and accounting. Authentication is Keycloak OIDC on sso.aerones.com (realm "aerones", client "operations-hub"). The contract is public; the data behind it is customer- and staff-gated, and Aerones publishes no developer program, SDKs, pricing or partner API documentation.
image: https://aerones.com/wp-content/uploads/2022/07/LPS_DJI_194_dng_43324928_0_2022516142538_photo_original.DNG-1-copy-e1658346007934.jpg
layout: provider
mcp_servers:
- description: ''
  name: Aerones MCP Server
  slug: aerones-mcp-server
modified: '2026-09-10'
name: Aerones
nav: Providers
network: true
overview: 'Aerones publishes 192 APIs on the [APIs.io](https://apis.io/) network, including Accounting API, Accounting.billing Statements API, Accounting.netsuite Departments API, and 189 more. Tagged areas include Company, Wind Energy, Renewable Energy, Robotics, and Drones.


  The Aerones catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aerones'' developer surface includes API reference, support, engineering blog, authentication, and 18 more developer resources.'
plans:
- name: Aerones Plans Pricing
  plan_count: 0
  slug: aerones-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Aerones Rate Limits
  slug: aerones-rate-limits
scopes:
- name: Aerones Scopes
  scope_count: 12
  slug: aerones-scopes
  summary_line: 12 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 34.0
    catalog_earned_first_party: 0.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 62.3
    developer_ergonomics: 20.8
    discoverability: 70.4
    operational_transparency: 0.0
  previous_composite: 50.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 192
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 63.5
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 100.0
security:
- kind: authentication
  name: Aerones Authentication
  slug: aerones-authentication
  summary_line: apiKey/http/openIdConnect · 4 schemes
- kind: domain-security
  name: Aerones Domain Security
  slug: aerones-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aerones
tags:
- Company
- Wind Energy
- Renewable Energy
- Robotics
- Drones
- Inspection
- Field Service Management
- Asset Management
- Industrial
- Energy
- Maintenance
- Latvia
website: https://aerones.com/
---
