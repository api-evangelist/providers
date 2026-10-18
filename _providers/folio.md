---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 690
  human_in_the_loop: 37
  name: Folio Agentic Access
  operation_count: 1341
  slug: folio-agentic-access
  summary_line: 1341 operations · 690 acting · 37 human-in-the-loop
api_count: 204
apis:
- description: 'FOLIO edge-oai-pmh module API, described in RAML (no OpenAPI published for this module). FOLIO is self-hosted: each library deployment exposes these endpoints through its own Okapi/Kong gateway URL.'
  name: FOLIO edge-oai-pmh
  slug: edge-oai-pmh
- description: 'FOLIO edge-orders module API, described in RAML (no OpenAPI published for this module). FOLIO is self-hosted: each library deployment exposes these endpoints through its own Okapi/Kong gateway URL.'
  name: FOLIO edge-orders
  slug: edge-orders
- description: 'FOLIO edge-patron module API, described in RAML (no OpenAPI published for this module). FOLIO is self-hosted: each library deployment exposes these endpoints through its own Okapi/Kong gateway URL.'
  name: FOLIO edge-patron
  slug: edge-patron
- description: 'FOLIO folio-custom-fields module API, described in RAML (no OpenAPI published for this module). Interfaces: custom-fields 3.2. FOLIO is self-hosted: each library deployment exposes these endpoints thr'
  name: FOLIO folio-custom-fields
  slug: folio-custom-fields
- description: 'FOLIO mod-audit module API, described in RAML (no OpenAPI published for this module). Interfaces: _timer 1.0, acquisition-invoice-events 1.0, acquisition-invoice-line-events 1.0, acquisition-order-eve'
  name: FOLIO mod-audit
  slug: mod-audit
- description: 'FOLIO mod-circulation-storage module API, described in RAML (no OpenAPI published for this module). Interfaces: _timer 1.0, actual-cost-record-storage 0.9, anonymize-storage-loans 0.1, cancellation-re'
  name: FOLIO mod-circulation-storage
  slug: mod-circulation-storage
- description: 'FOLIO mod-circulation module API, described in RAML (no OpenAPI published for this module). Interfaces: _timer 1.0, add-info 0.1, allowed-service-points 1.2, change-due-date 0.1, circulation 14.7, cir'
  name: FOLIO mod-circulation
  slug: mod-circulation
- description: 'FOLIO mod-configuration module API, described in RAML (no OpenAPI published for this module). Interfaces: configuration 2.0. FOLIO is self-hosted: each library deployment exposes these endpoints throu'
  name: FOLIO mod-configuration
  slug: mod-configuration
- description: 'FOLIO mod-copycat module API, described in RAML (no OpenAPI published for this module). Interfaces: copycat-imports 1.1, copycat-profiles 1.2. FOLIO is self-hosted: each library deployment exposes the'
  name: FOLIO mod-copycat
  slug: mod-copycat
- description: 'FOLIO mod-courses module API, described in RAML (no OpenAPI published for this module). Interfaces: copyright-status-storage 0.1, course-reserves-storage 0.3, course-storage 0.1, course-type-storage 0'
  name: FOLIO mod-courses
  slug: mod-courses
- description: 'FOLIO mod-data-import module API, described in RAML (no OpenAPI published for this module). Interfaces: data-import 3.2. FOLIO is self-hosted: each library deployment exposes these endpoints through i'
  name: FOLIO mod-data-import
  slug: mod-data-import
- description: 'FOLIO mod-di-converter-storage module API, described in RAML (no OpenAPI published for this module). Interfaces: converter-storage-forms-configs 1.2, data-import-converter-storage 1.5, field-protectio'
  name: FOLIO mod-di-converter-storage
  slug: mod-di-converter-storage
- description: 'FOLIO mod-email module API, described in RAML (no OpenAPI published for this module). Interfaces: _timer 1.0, email 1.2, email.settings 1.0, smtpConfiguration 0.1. FOLIO is self-hosted: each library d'
  name: FOLIO mod-email
  slug: mod-email
- description: 'FOLIO mod-erm-usage-harvester module API, described in RAML (no OpenAPI published for this module). Interfaces: _timer 1.0, erm-usage-harvester 2.1. FOLIO is self-hosted: each library deployment expos'
  name: FOLIO mod-erm-usage-harvester
  slug: mod-erm-usage-harvester
- description: 'FOLIO mod-erm-usage module API, described in RAML (no OpenAPI published for this module). Interfaces: aggregator-settings 2.0, counter-reports 5.0, custom-reports 2.0, erm-usage-files 1.0, usage-data-'
  name: FOLIO mod-erm-usage
  slug: mod-erm-usage
- description: 'FOLIO mod-event-config module API, described in RAML (no OpenAPI published for this module). Interfaces: mod-event 2.0. FOLIO is self-hosted: each library deployment exposes these endpoints through it'
  name: FOLIO mod-event-config
  slug: mod-event-config
- description: 'FOLIO mod-feesfines module API, described in RAML (no OpenAPI published for this module). Interfaces: actual-cost-fee-fine 0.3, feefine-reports 2.3, feesfines 19.1. FOLIO is self-hosted: each library '
  name: FOLIO mod-feesfines
  slug: mod-feesfines
- description: 'FOLIO mod-finance-storage module API, described in RAML (no OpenAPI published for this module). Interfaces: _timer 1.0, finance-storage.budget-expense-classes 2.0, finance-storage.budgets 3.0, finance'
  name: FOLIO mod-finance-storage
  slug: mod-finance-storage
- description: 'FOLIO mod-finance module API, described in RAML (no OpenAPI published for this module). Interfaces: finance.budgets 2.0, finance.exchange-rate 1.0, finance.expense-classes 3.0, finance.finance-data 1.'
  name: FOLIO mod-finance
  slug: mod-finance
- description: 'FOLIO mod-finc-config module API, described in RAML (no OpenAPI published for this module). Interfaces: _timer 1.0, finc-config-contacts 1.0, finc-config-ezb-credentials 1.0, finc-config-files 1.1, fi'
  name: FOLIO mod-finc-config
  slug: mod-finc-config
- description: 'FOLIO mod-gobi module API, described in RAML (no OpenAPI published for this module). Interfaces: custom-mapping 1.0, gobi 1.12. FOLIO is self-hosted: each library deployment exposes these endpoints th'
  name: FOLIO mod-gobi
  slug: mod-gobi
- description: 'FOLIO mod-idm-connect module API, described in RAML (no OpenAPI published for this module). Interfaces: idm-connect 1.0. FOLIO is self-hosted: each library deployment exposes these endpoints through i'
  name: FOLIO mod-idm-connect
  slug: mod-idm-connect
- description: 'FOLIO mod-inventory-storage module API, described in RAML (no OpenAPI published for this module). Interfaces: alternative-title-types 1.0, async-migration 1.0, bound-with-parts-storage 2.0, call-numbe'
  name: FOLIO mod-inventory-storage
  slug: mod-inventory-storage
- description: 'FOLIO mod-inventory module API, described in RAML (no OpenAPI published for this module). Interfaces: inventory 14.4, inventory-batch 3.0, inventory-config 0.2, inventory-move 0.3, inventory-update-ow'
  name: FOLIO mod-inventory
  slug: mod-inventory
- description: 'FOLIO mod-invoice-storage module API, described in RAML (no OpenAPI published for this module). Interfaces: _timer 1.0, batch-group-storage.batch-groups 1.0, batch-voucher-storage.batch-voucher-export'
  name: FOLIO mod-invoice-storage
  slug: mod-invoice-storage
- description: 'FOLIO mod-invoice module API, described in RAML (no OpenAPI published for this module). Interfaces: batch-group 1.1, batch-voucher.batch-voucher-exports 1.2, batch-voucher.batch-vouchers 2.0, batch-vo'
  name: FOLIO mod-invoice
  slug: mod-invoice
- description: 'FOLIO mod-kb-ebsco-java module API, described in RAML (no OpenAPI published for this module). Interfaces: _timer 1.0, eholdings 5.0. FOLIO is self-hosted: each library deployment exposes these endpoin'
  name: FOLIO mod-kb-ebsco-java
  slug: mod-kb-ebsco-java
- description: 'FOLIO mod-login-saml module API, described in RAML (no OpenAPI published for this module). Interfaces: login-saml 2.1. FOLIO is self-hosted: each library deployment exposes these endpoints through its'
  name: FOLIO mod-login-saml
  slug: mod-login-saml
- description: 'FOLIO mod-login module API, described in RAML (no OpenAPI published for this module). Interfaces: login 7.3. FOLIO is self-hosted: each library deployment exposes these endpoints through its own Okapi'
  name: FOLIO mod-login
  slug: mod-login
- description: 'FOLIO mod-notify module API, described in RAML (no OpenAPI published for this module). Interfaces: notify 2.2, patron-notice 1.2. FOLIO is self-hosted: each library deployment exposes these endpoints '
  name: FOLIO mod-notify
  slug: mod-notify
- description: 'FOLIO mod-oai-pmh module API, described in RAML (no OpenAPI published for this module). Interfaces: _timer 1.0, oai-pmh 3.4. FOLIO is self-hosted: each library deployment exposes these endpoints throu'
  name: FOLIO mod-oai-pmh
  slug: mod-oai-pmh
- description: 'FOLIO mod-orders-storage module API, described in RAML (no OpenAPI published for this module). Interfaces: _timer 1.0, acquisitions-units-storage.memberships 1.0, acquisitions-units-storage.units 1.1,'
  name: FOLIO mod-orders-storage
  slug: mod-orders-storage
- description: 'FOLIO mod-orders module API, described in RAML (no OpenAPI published for this module). Interfaces: acquisition-methods 1.0, acquisitions-units 1.1, configuration.prefixes 1.2, configuration.reasons-fo'
  name: FOLIO mod-orders
  slug: mod-orders
- description: 'FOLIO mod-organizations-storage module API, described in RAML (no OpenAPI published for this module). Interfaces: _timer 1.0, organizations-storage.banking-account-types 1.0, organizations-storage.ban'
  name: FOLIO mod-organizations-storage
  slug: mod-organizations-storage
- description: 'FOLIO mod-organizations module API, described in RAML (no OpenAPI published for this module). Interfaces: banking-information 1.0, organizations.organizations 1.2. FOLIO is self-hosted: each library d'
  name: FOLIO mod-organizations
  slug: mod-organizations
- description: 'FOLIO mod-patron-blocks module API, described in RAML (no OpenAPI published for this module). Interfaces: _timer 1.0, automated-patron-blocks 0.1, patron-block-conditions 0.1, patron-block-limits 0.1,'
  name: FOLIO mod-patron-blocks
  slug: mod-patron-blocks
- description: 'FOLIO mod-patron module API, described in RAML (no OpenAPI published for this module). Interfaces: patron 6.6, patron.settings 1.0. FOLIO is self-hosted: each library deployment exposes these endpoint'
  name: FOLIO mod-patron
  slug: mod-patron
- description: 'FOLIO mod-permissions module API, described in RAML (no OpenAPI published for this module). Interfaces: _tenantPermissions 2.1, permissions 5.8. FOLIO is self-hosted: each library deployment exposes t'
  name: FOLIO mod-permissions
  slug: mod-permissions
- description: 'FOLIO mod-pubsub module API, described in RAML (no OpenAPI published for this module). Interfaces: pubsub-audit 0.1, pubsub-event-types 0.1, pubsub-messaging-modules 0.1, pubsub-publish 0.1, pubsub-pu'
  name: FOLIO mod-pubsub
  slug: mod-pubsub
- description: 'FOLIO mod-reporting module API, described in RAML (no OpenAPI published for this module). Interfaces: ldp-query 1.4. FOLIO is self-hosted: each library deployment exposes these endpoints through its o'
  name: FOLIO mod-reporting
  slug: mod-reporting
- description: 'FOLIO mod-rtac module API, described in RAML (no OpenAPI published for this module). Interfaces: rtac 1.5, rtac-batch 1.2. FOLIO is self-hosted: each library deployment exposes these endpoints through'
  name: FOLIO mod-rtac
  slug: mod-rtac
- description: 'FOLIO mod-sender module API, described in RAML (no OpenAPI published for this module). Interfaces: message-delivery 1.1. FOLIO is self-hosted: each library deployment exposes these endpoints through i'
  name: FOLIO mod-sender
  slug: mod-sender
- description: 'FOLIO mod-source-record-manager module API, described in RAML (no OpenAPI published for this module). Interfaces: mapping-metadata-provider 1.1, mapping-rules-provider 2.0, metadata-provider-job-execu'
  name: FOLIO mod-source-record-manager
  slug: mod-source-record-manager
- description: 'FOLIO mod-source-record-storage module API, described in RAML (no OpenAPI published for this module). Interfaces: source-storage-async-migrations 1.1, source-storage-batch 1.3, source-storage-records '
  name: FOLIO mod-source-record-storage
  slug: mod-source-record-storage
- description: 'FOLIO mod-template-engine module API, described in RAML (no OpenAPI published for this module). Interfaces: template-engine 2.3. FOLIO is self-hosted: each library deployment exposes these endpoints t'
  name: FOLIO mod-template-engine
  slug: mod-template-engine
- description: 'FOLIO mod-user-import module API, described in RAML (no OpenAPI published for this module). Interfaces: user-import 2.2. FOLIO is self-hosted: each library deployment exposes these endpoints through i'
  name: FOLIO mod-user-import
  slug: mod-user-import
- description: 'FOLIO mod-users-bl module API, described in RAML (no OpenAPI published for this module). Interfaces: users-bl 6.1. FOLIO is self-hosted: each library deployment exposes these endpoints through its own'
  name: FOLIO mod-users-bl
  slug: mod-users-bl
- description: 'FOLIO mod-users module API, described in RAML (no OpenAPI published for this module). Interfaces: _timer 1.0, patron-pin 1.0, staging-users 1.2, user-tenants 1.0, users 16.5, users.settings 2.0. FOLIO'
  name: FOLIO mod-users
  slug: mod-users
- description: 'FOLIO okapi module API, described in RAML (no OpenAPI published for this module). FOLIO is self-hosted: each library deployment exposes these endpoints through its own Okapi/Kong gateway URL.'
  name: FOLIO okapi
  slug: okapi
- description: 'FOLIO raml-module-builder module API, described in RAML (no OpenAPI published for this module). FOLIO is self-hosted: each library deployment exposes these endpoints through its own Okapi/Kong gateway'
  name: FOLIO raml-module-builder
  slug: raml-module-builder
- description: 'FOLIO raml module API, described in RAML (no OpenAPI published for this module). FOLIO is self-hosted: each library deployment exposes these endpoints through its own Okapi/Kong gateway URL.'
  name: FOLIO raml
  slug: raml
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Access Control API from FOLIO — 23 operation(s) for access control.
  name: FOLIO Access Control API
  slug: folio-access-control-api
- baseURL: /remote-storage/
  baseurl_source: spec
  description: The Accessions API from FOLIO — 3 operation(s) for accessions.
  name: FOLIO Accessions API
  slug: folio-accessions-api
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: The action-controller API from FOLIO — 1 operation(s) for action-controller.
  name: FOLIO Action Controller API
  slug: folio-action-controller-api
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: Monitor and interact
  name: FOLIO Actuator API
  slug: folio-actuator-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Admin API from FOLIO — 12 operation(s) for admin.
  name: FOLIO Admin API
  slug: folio-admin-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The agency-mappings API from FOLIO — 1 operation(s) for agency-mappings.
  name: FOLIO Agency Mappings API
  slug: folio-agency-mappings-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Agreements API from FOLIO — 20 operation(s) for agreements.
  name: FOLIO Agreements API
  slug: folio-agreements-api
- description: The allowedServicePoints API from FOLIO — 1 operation(s) for allowedservicepoints.
  name: FOLIO Allowed Service Points API
  slug: folio-allowedservicepoints-api
- baseURL: /inventory
  baseurl_source: spec
  description: The alternativeTitleTypes API from FOLIO — 1 operation(s) for alternativetitletypes.
  name: FOLIO Alternative Title Types API
  slug: folio-alternativetitletypes-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Amendments API from FOLIO — 3 operation(s) for amendments.
  name: FOLIO Amendments API
  slug: folio-amendments-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The application-discovery API from FOLIO — 2 operation(s) for application-discovery.
  name: FOLIO Application Discovery API
  slug: folio-application-discovery-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The applications API from FOLIO — 6 operation(s) for applications.
  name: FOLIO Applications API
  slug: folio-applications-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The auth-user API from FOLIO — 1 operation(s) for auth-user.
  name: FOLIO Auth User API
  slug: folio-auth-user-api
- baseURL: /innreach/
  baseurl_source: spec
  description: The authentication API from FOLIO — 2 operation(s) for authentication.
  name: FOLIO Authentication API
  slug: folio-authentication-api
- baseURL: /inventory
  baseurl_source: spec
  description: The authorities API from FOLIO — 1 operation(s) for authorities.
  name: FOLIO Authorities API
  slug: folio-authorities-api
- description: The authority API from FOLIO — 1 operation(s) for authority.
  name: FOLIO Authority API
  slug: folio-authority-api
- baseURL: https://localhost:8081
  baseurl_source: spec
  description: The authority-heading-type API from FOLIO — 1 operation(s) for authority-heading-type.
  name: FOLIO Authority Heading Type API
  slug: folio-authority-heading-type-api
- baseURL: https://localhost:8081
  baseurl_source: spec
  description: The authority-identifier-type API from FOLIO — 1 operation(s) for authority-identifier-type.
  name: FOLIO Authority Identifier Type API
  slug: folio-authority-identifier-type-api
- baseURL: https://localhost:8081
  baseurl_source: spec
  description: The authority-note-type API from FOLIO — 2 operation(s) for authority-note-type.
  name: FOLIO Authority Note Type API
  slug: folio-authority-note-type-api
- baseURL: https://localhost:8081
  baseurl_source: spec
  description: The authority-source-file API from FOLIO — 3 operation(s) for authority-source-file.
  name: FOLIO Authority Source File API
  slug: folio-authority-source-file-api
- baseURL: https://localhost:8081
  baseurl_source: spec
  description: The authority-storage API from FOLIO — 3 operation(s) for authority-storage.
  name: FOLIO Authority Storage API
  slug: folio-authority-storage-api
- baseURL: https://localhost:8081
  baseurl_source: spec
  description: The authority-storage-reindex API from FOLIO — 2 operation(s) for authority-storage-reindex.
  name: FOLIO Authority Storage Reindex API
  slug: folio-authority-storage-reindex-api
- baseURL: /inventory
  baseurl_source: spec
  description: The authoritySourceRecords API from FOLIO — 1 operation(s) for authoritysourcerecords.
  name: FOLIO Authority Source Records API
  slug: folio-authoritysourcerecords-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: Stub implementation for `authtoken` and `authtoken2` interfaces.
  name: FOLIO Authtoken API
  slug: folio-authtoken-api
- description: The Base Url API from FOLIO — 1 operation(s) for base url.
  name: FOLIO Base Url API
  slug: folio-base-url-api
- description: The batchJob API from FOLIO — 4 operation(s) for batchjob.
  name: FOLIO Batch Job API
  slug: folio-batchjob-api
- baseURL: /erm/
  baseurl_source: spec
  description: The batchLicenseTerms API from FOLIO — 1 operation(s) for batchlicenseterms.
  name: FOLIO Batch License Terms API
  slug: folio-batchlicenseterms-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The bib-info-d2ir API from FOLIO — 1 operation(s) for bib-info-d2ir.
  name: FOLIO Bib Info D2ir API
  slug: folio-bib-info-d2ir-api
- baseURL_template: https://{environment}-okapi.ci.folio.org
  baseurl_source: spec_template
  description: Provides endpoints to browse records (e.g., instances, authorities) in alphabetical order by a specific field, such as call number, classification number, subject, or contributor.
  name: FOLIO Browse API
  slug: folio-browse-api
- description: The Bulk Operations API from FOLIO — 17 operation(s) for bulk operations.
  name: FOLIO Bulk Operations API
  slug: folio-bulk-operations-api
- baseURL: /
  baseurl_source: spec
  description: The Calendar API from FOLIO — 4 operation(s) for calendar.
  name: FOLIO Calendar API
  slug: folio-calendar-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The capability API from FOLIO — 3 operation(s) for capability.
  name: FOLIO Capability API
  slug: folio-capability-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The capability-set API from FOLIO — 2 operation(s) for capability-set.
  name: FOLIO Capability Set API
  slug: folio-capability-set-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The central-patron-type-mappings API from FOLIO — 1 operation(s) for central-patron-type-mappings.
  name: FOLIO Central Patron Type Mappings API
  slug: folio-central-patron-type-mappings-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The central-server-configuration API from FOLIO — 3 operation(s) for central-server-configuration.
  name: FOLIO Central Server Configuration API
  slug: folio-central-server-configuration-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The central-servers API from FOLIO — 2 operation(s) for central-servers.
  name: FOLIO Central Servers API
  slug: folio-central-servers-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Charges API from FOLIO — 2 operation(s) for charges.
  name: FOLIO Charges API
  slug: folio-charges-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Checklist Items API from FOLIO — 2 operation(s) for checklist items.
  name: FOLIO Checklist Items API
  slug: folio-checklist-items-api
- description: The Circulation Bff API from FOLIO — 3 operation(s) for circulation bff.
  name: FOLIO Circulation Bff API
  slug: folio-circulation-bff-api
- description: The Circulation Item API from FOLIO — 2 operation(s) for circulation item.
  name: FOLIO Circulation Item API
  slug: folio-circulation-item-api
- description: The claimItemReturned API from FOLIO — 1 operation(s) for claimitemreturned.
  name: FOLIO Claim Item Returned API
  slug: folio-claimitemreturned-api
- baseURL: /inventory
  baseurl_source: spec
  description: The classificationTypes API from FOLIO — 1 operation(s) for classificationtypes.
  name: FOLIO Classification Types API
  slug: folio-classificationtypes-api
- baseURL: /data-export/
  baseurl_source: spec
  description: The Clean Up Files API from FOLIO — 1 operation(s) for clean up files.
  name: FOLIO Clean Up Files API
  slug: folio-clean-up-files-api
- baseURL_template: https://{environment}-okapi.ci.folio.org
  baseurl_source: spec_template
  description: Provides endpoints to configure search and browse features, such as enabling/disabling specific features or managing language settings.
  name: FOLIO Config API
  slug: folio-config-api
- baseURL: /data-export-spring/
  baseurl_source: spec
  description: The Configs API from FOLIO — 2 operation(s) for configs.
  name: FOLIO Configs API
  slug: folio-configs-api
- baseURL: /data-export/
  baseurl_source: spec
  description: The Configuration API from FOLIO — 1 operation(s) for configuration.
  name: FOLIO Configuration API
  slug: folio-configuration-api
- baseURL: /remote-storage/
  baseurl_source: spec
  description: The Configurations API from FOLIO — 2 operation(s) for configurations.
  name: FOLIO Configurations API
  slug: folio-configurations-api
- description: The confirmMediatedRequests API from FOLIO — 1 operation(s) for confirmmediatedrequests.
  name: FOLIO Confirm Mediated Requests API
  slug: folio-confirmmediatedrequests-api
- description: The Consortia API from FOLIO — 2 operation(s) for consortia.
  name: FOLIO Consortia API
  slug: folio-consortia-api
- description: The Consortia Configuration API from FOLIO — 1 operation(s) for consortia configuration.
  name: FOLIO Consortia Configuration API
  slug: folio-consortia-configuration-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Contacts API from FOLIO — 2 operation(s) for contacts.
  name: FOLIO Contacts API
  slug: folio-contacts-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The contribution-criteria API from FOLIO — 1 operation(s) for contribution-criteria.
  name: FOLIO Contribution Criteria API
  slug: folio-contribution-criteria-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The contributions API from FOLIO — 3 operation(s) for contributions.
  name: FOLIO Contributions API
  slug: folio-contributions-api
- baseURL: /inventory
  baseurl_source: spec
  description: The contributorNameTypes API from FOLIO — 1 operation(s) for contributornametypes.
  name: FOLIO Contributor Name Types API
  slug: folio-contributornametypes-api
- baseURL: /inventory
  baseurl_source: spec
  description: The contributorTypes API from FOLIO — 1 operation(s) for contributortypes.
  name: FOLIO Contributor Types API
  slug: folio-contributortypes-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Correspondence API from FOLIO — 2 operation(s) for correspondence.
  name: FOLIO Correspondence API
  slug: folio-correspondence-api
- baseURL: /courses/
  baseurl_source: spec
  description: The Courses API from FOLIO — 5 operation(s) for courses.
  name: FOLIO Courses API
  slug: folio-courses-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The credentials API from FOLIO — 3 operation(s) for credentials.
  name: FOLIO Credentials API
  slug: folio-credentials-api
- baseURL: https://folio-etesting-snapshot-kong.ci.folio.org/
  baseurl_source: spec
  description: The custom API from FOLIO — 3 operation(s) for custom.
  name: FOLIO Custom API
  slug: folio-custom-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Custom Properties API from FOLIO — 3 operation(s) for custom properties.
  name: FOLIO Custom Properties API
  slug: folio-custom-properties-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Custom Property Definitions API from FOLIO — 3 operation(s) for custom property definitions.
  name: FOLIO Custom Property Definitions API
  slug: folio-custom-property-definitions-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Dashboard API from FOLIO — 1 operation(s) for dashboard.
  name: FOLIO Dashboard API
  slug: folio-dashboard-api
- description: The declareClaimedReturnedItemAsMissing API from FOLIO — 1 operation(s) for declareclaimedreturneditemasmissing.
  name: FOLIO Declare Claimed Returned Item As Missing API
  slug: folio-declareclaimedreturneditemasmissing-api
- description: The declareItemLost API from FOLIO — 1 operation(s) for declareitemlost.
  name: FOLIO Declare Item Lost API
  slug: folio-declareitemlost-api
- description: The Default API from FOLIO — 2 operation(s) for default.
  name: FOLIO Default API
  slug: folio-default-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The deployment API from FOLIO — 2 operation(s) for deployment.
  name: FOLIO Deployment API
  slug: folio-deployment-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The discovery API from FOLIO — 8 operation(s) for discovery.
  name: FOLIO Discovery API
  slug: folio-discovery-api
- baseURL: /data-export/
  baseurl_source: spec
  description: The Download Record API from FOLIO — 1 operation(s) for download record.
  name: FOLIO Download Record API
  slug: folio-download-record-api
- description: The ecs-request-transactions API from FOLIO — 1 operation(s) for ecs-request-transactions.
  name: FOLIO Ecs Request Transactions API
  slug: folio-ecs-request-transactions-api
- description: The ecsLoans API from FOLIO — 4 operation(s) for ecsloans.
  name: FOLIO Ecs Loans API
  slug: folio-ecsloans-api
- description: The ecsRequestExternal API from FOLIO — 2 operation(s) for ecsrequestexternal.
  name: FOLIO Ecs Request External API
  slug: folio-ecsrequestexternal-api
- description: The ecsTlr API from FOLIO — 2 operation(s) for ecstlr.
  name: FOLIO Ecs Tlr API
  slug: folio-ecstlr-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The entitlement API from FOLIO — 2 operation(s) for entitlement.
  name: FOLIO Entitlement API
  slug: folio-entitlement-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The entitlement-application API from FOLIO — 1 operation(s) for entitlement-application.
  name: FOLIO Entitlement Application API
  slug: folio-entitlement-application-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Entitlement Log API from FOLIO — 2 operation(s) for entitlement log.
  name: FOLIO Entitlement Log API
  slug: folio-entitlement-log-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The entitlement-module API from FOLIO — 1 operation(s) for entitlement-module.
  name: FOLIO Entitlement Module API
  slug: folio-entitlement-module-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The entitlement-validation API from FOLIO — 1 operation(s) for entitlement-validation.
  name: FOLIO Entitlement Validation API
  slug: folio-entitlement-validation-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Entitlements API from FOLIO — 2 operation(s) for entitlements.
  name: FOLIO Entitlements API
  slug: folio-entitlements-api
- baseURL: https://folio-etesting-snapshot-kong.ci.folio.org/
  baseurl_source: spec
  description: The entity-types API from FOLIO — 7 operation(s) for entity-types.
  name: FOLIO Entity Types API
  slug: folio-entity-types-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The environment API from FOLIO — 2 operation(s) for environment.
  name: FOLIO Environment API
  slug: folio-environment-api
- description: The Eusage Reports API from FOLIO — 11 operation(s) for eusage reports.
  name: FOLIO Eusage Reports API
  slug: folio-eusage-reports-api
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: The event-controller API from FOLIO — 1 operation(s) for event-controller.
  name: FOLIO Event Controller API
  slug: folio-event-controller-api
- baseURL: /data-export/
  baseurl_source: spec
  description: The Expire Jobs API from FOLIO — 1 operation(s) for expire jobs.
  name: FOLIO Expire Jobs API
  slug: folio-expire-jobs-api
- baseURL: /data-export/
  baseurl_source: spec
  description: The Export All API from FOLIO — 1 operation(s) for export all.
  name: FOLIO Export All API
  slug: folio-export-all-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Export API from FOLIO — 4 operation(s) for export.
  name: FOLIO Export API
  slug: folio-export-api
- baseURL: /data-export/
  baseurl_source: spec
  description: The Export Authority Deleted API from FOLIO — 1 operation(s) for export authority deleted.
  name: FOLIO Export Authority Deleted API
  slug: folio-export-authority-deleted-api
- baseURL: /data-export/
  baseurl_source: spec
  description: The Export Deleted API from FOLIO — 1 operation(s) for export deleted.
  name: FOLIO Export Deleted API
  slug: folio-export-deleted-api
- baseURL: /remote-storage/
  baseurl_source: spec
  description: The Extended Mappings API from FOLIO — 4 operation(s) for extended mappings.
  name: FOLIO Extended Mappings API
  slug: folio-extended-mappings-api
- baseURL: /
  baseurl_source: spec
  description: The External API from FOLIO — 4 operation(s) for external.
  name: FOLIO External API
  slug: folio-external-api
- baseURL_template: https://{environment}-okapi.ci.folio.org
  baseurl_source: spec_template
  description: Provides endpoints to retrieve aggregated information (facets) about records, such as counts of records by specific fields or ranges of values. This can be used for faceted search or browsing.
  name: FOLIO Facets API
  slug: folio-facets-api
- baseURL: /data-export/
  baseurl_source: spec
  description: The File Definitions API from FOLIO — 3 operation(s) for file definitions.
  name: FOLIO File Definitions API
  slug: folio-file-definitions-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Files API from FOLIO — 6 operation(s) for files.
  name: FOLIO Files API
  slug: folio-files-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The flow API from FOLIO — 6 operation(s) for flow.
  name: FOLIO Flow API
  slug: folio-flow-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The forgotten-username-password API from FOLIO — 2 operation(s) for forgotten-username-password.
  name: FOLIO Forgotten Username Password API
  slug: folio-forgotten-username-password-api
- baseURL: https://folio-etesting-snapshot-kong.ci.folio.org/
  baseurl_source: spec
  description: The fqlQuery API from FOLIO — 6 operation(s) for fqlquery.
  name: FOLIO Fql Query API
  slug: folio-fqlquery-api
- baseURL: https://folio-etesting-snapshot-kong.ci.folio.org/
  baseurl_source: spec
  description: The fqmVersion API from FOLIO — 2 operation(s) for fqmversion.
  name: FOLIO Fqm Version API
  slug: folio-fqmversion-api
- description: The getAllowedServicePoints API from FOLIO — 1 operation(s) for getallowedservicepoints.
  name: FOLIO Get Allowed Service Points API
  slug: folio-getallowedservicepoints-api
- description: The getCirculationLoanById API from FOLIO — 1 operation(s) for getcirculationloanbyid.
  name: FOLIO Get Circulation Loan By ID API
  slug: folio-getcirculationloanbyid-api
- description: The getCirculationLoans API from FOLIO — 1 operation(s) for getcirculationloans.
  name: FOLIO Get Circulation Loans API
  slug: folio-getcirculationloans-api
- description: The getCirculationRequests API from FOLIO — 1 operation(s) for getcirculationrequests.
  name: FOLIO Get Circulation Requests API
  slug: folio-getcirculationrequests-api
- description: The getExternalUsers API from FOLIO — 1 operation(s) for getexternalusers.
  name: FOLIO Get External Users API
  slug: folio-getexternalusers-api
- description: The getInstancesByQuery API from FOLIO — 1 operation(s) for getinstancesbyquery.
  name: FOLIO Get Instances By Query API
  slug: folio-getinstancesbyquery-api
- description: The getInventoryItemsByQuery API from FOLIO — 1 operation(s) for getinventoryitemsbyquery.
  name: FOLIO Get Inventory Items By Query API
  slug: folio-getinventoryitemsbyquery-api
- description: The getPickSlips API from FOLIO — 1 operation(s) for getpickslips.
  name: FOLIO Get Pick Slips API
  slug: folio-getpickslips-api
- description: The getSearchSlips API from FOLIO — 1 operation(s) for getsearchslips.
  name: FOLIO Get Search Slips API
  slug: folio-getsearchslips-api
- description: The graph API from FOLIO — 1 operation(s) for graph.
  name: FOLIO Graph API
  slug: folio-graph-api
- baseURL: /inventory
  baseurl_source: spec
  description: The holdings API from FOLIO — 1 operation(s) for holdings.
  name: FOLIO Holdings API
  slug: folio-holdings-api
- baseURL: /inventory
  baseurl_source: spec
  description: The holdingsNoteTypes API from FOLIO — 1 operation(s) for holdingsnotetypes.
  name: FOLIO Holdings Note Types API
  slug: folio-holdingsnotetypes-api
- description: The hub API from FOLIO — 1 operation(s) for hub.
  name: FOLIO Hub API
  slug: folio-hub-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Identifiers API from FOLIO — 3 operation(s) for identifiers.
  name: FOLIO Identifiers API
  slug: folio-identifiers-api
- baseURL: /inventory
  baseurl_source: spec
  description: The identifierTypes API from FOLIO — 1 operation(s) for identifiertypes.
  name: FOLIO Identifier Types API
  slug: folio-identifiertypes-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The idp-migration API from FOLIO — 1 operation(s) for idp-migration.
  name: FOLIO Idp Migration API
  slug: folio-idp-migration-api
- description: The import API from FOLIO — 2 operation(s) for import.
  name: FOLIO Import API
  slug: folio-import-api
- description: The import, job API from FOLIO — 3 operation(s) for import, job.
  name: FOLIO import, job API
  slug: folio-import-job-api
- description: The import, start API from FOLIO — 1 operation(s) for import, start.
  name: FOLIO import, start API
  slug: folio-import-start-api
- baseURL_template: https://{environment}-okapi.ci.folio.org
  baseurl_source: spec_template
  description: Provides endpoints to manage the search index, including creating or updating mappings, settings, and manually populating the index with records from external sources (e.g., inventory).
  name: FOLIO Index Management API
  slug: folio-index-management-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The inn-reach-circulation API from FOLIO — 16 operation(s) for inn-reach-circulation.
  name: FOLIO Inn Reach Circulation API
  slug: folio-inn-reach-circulation-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The inn-reach-recall-user API from FOLIO — 1 operation(s) for inn-reach-recall-user.
  name: FOLIO Inn Reach Recall User API
  slug: folio-inn-reach-recall-user-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The inn-reach-transaction API from FOLIO — 16 operation(s) for inn-reach-transaction.
  name: FOLIO Inn Reach Transaction API
  slug: folio-inn-reach-transaction-api
- baseURL: https://localhost:8081
  baseurl_source: spec
  description: The instance-authority-links-statistics API from FOLIO — 2 operation(s) for instance-authority-links-statistics.
  name: FOLIO Instance Authority Links Statistics API
  slug: folio-instance-authority-links-statistics-api
- baseURL: https://localhost:8081
  baseurl_source: spec
  description: The instance-links API from FOLIO — 1 operation(s) for instance-links.
  name: FOLIO Instance Links API
  slug: folio-instance-links-api
- baseURL: /inventory
  baseurl_source: spec
  description: The instanceFormats API from FOLIO — 1 operation(s) for instanceformats.
  name: FOLIO Instance Formats API
  slug: folio-instanceformats-api
- baseURL: /inventory
  baseurl_source: spec
  description: The instanceNoteTypes API from FOLIO — 1 operation(s) for instancenotetypes.
  name: FOLIO Instance Note Types API
  slug: folio-instancenotetypes-api
- baseURL: /inventory
  baseurl_source: spec
  description: The instances API from FOLIO — 4 operation(s) for instances.
  name: FOLIO Instances API
  slug: folio-instances-api
- baseURL: /inventory
  baseurl_source: spec
  description: The instanceTypes API from FOLIO — 1 operation(s) for instancetypes.
  name: FOLIO Instance Types API
  slug: folio-instancetypes-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Internal Contacts API from FOLIO — 2 operation(s) for internal contacts.
  name: FOLIO Internal Contacts API
  slug: folio-internal-contacts-api
- baseURL: /inventory
  baseurl_source: spec
  description: The Inventory API from FOLIO — 4 operation(s) for inventory.
  name: FOLIO Inventory API
  slug: folio-inventory-api
- description: The Inventory Batch Upsert Hrid API from FOLIO — 1 operation(s) for inventory batch upsert hrid.
  name: FOLIO Inventory Batch Upsert Hrid API
  slug: folio-inventory-batch-upsert-hrid-api
- description: The Inventory Import API from FOLIO — 26 operation(s) for inventory import.
  name: FOLIO Inventory Import API
  slug: folio-inventory-import-api
- description: The Inventory Upsert Hrid API from FOLIO — 2 operation(s) for inventory upsert hrid.
  name: FOLIO Inventory Upsert Hrid API
  slug: folio-inventory-upsert-hrid-api
- baseURL: /inventory
  baseurl_source: spec
  description: The inventoryViewInstances API from FOLIO — 1 operation(s) for inventoryviewinstances.
  name: FOLIO Inventory View Instances API
  slug: folio-inventoryviewinstances-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The invoke-service API from FOLIO — 1 operation(s) for invoke-service.
  name: FOLIO Invoke Service API
  slug: folio-invoke-service-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The item-contribution-options-configuration API from FOLIO — 1 operation(s) for item-contribution-options-configuration.
  name: FOLIO Item Contribution Options Configuration API
  slug: folio-item-contribution-options-configuration-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The item-type-mappings API from FOLIO — 1 operation(s) for item-type-mappings.
  name: FOLIO Item Type Mappings API
  slug: folio-item-type-mappings-api
- baseURL: /caiasoftService/
  baseurl_source: spec
  description: The ItemBarcodes API from FOLIO — 1 operation(s) for itembarcodes.
  name: FOLIO Item Barcodes API
  slug: folio-itembarcodes-api
- baseURL: /inventory
  baseurl_source: spec
  description: The items API from FOLIO — 2 operation(s) for items.
  name: FOLIO Items API
  slug: folio-items-api
- baseURL: /data-export-spring/
  baseurl_source: spec
  description: The Job Deletion Intervals API from FOLIO — 2 operation(s) for job deletion intervals.
  name: FOLIO Job Deletion Intervals API
  slug: folio-job-deletion-intervals-api
- baseURL: /data-export/
  baseurl_source: spec
  description: The Job Executions API from FOLIO — 3 operation(s) for job executions.
  name: FOLIO Job Executions API
  slug: folio-job-executions-api
- baseURL: /data-export/
  baseurl_source: spec
  description: The Job Profiles API from FOLIO — 2 operation(s) for job profiles.
  name: FOLIO Job Profiles API
  slug: folio-job-profiles-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Jobs API from FOLIO — 21 operation(s) for jobs.
  name: FOLIO Jobs API
  slug: folio-jobs-api
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: The json-schemas-controller API from FOLIO — 1 operation(s) for json-schemas-controller.
  name: FOLIO JSON Schemas Controller API
  slug: folio-json-schemas-controller-api
- baseURL: https://order-stub.com/
  baseurl_source: spec
  description: The Kafka Stub Endpoint API from FOLIO — 1 operation(s) for kafka stub endpoint.
  name: FOLIO Kafka Stub Endpoint API
  slug: folio-kafka-stub-endpoint-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The library-mappings API from FOLIO — 1 operation(s) for library-mappings.
  name: FOLIO Library Mappings API
  slug: folio-library-mappings-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Licenses API from FOLIO — 5 operation(s) for licenses.
  name: FOLIO Licenses API
  slug: folio-licenses-api
- baseURL: /erm/
  baseurl_source: spec
  description: The licenseTerms API from FOLIO — 1 operation(s) for licenseterms.
  name: FOLIO License Terms API
  slug: folio-licenseterms-api
- baseURL: https://localhost:8081
  baseurl_source: spec
  description: The linking-rules API from FOLIO — 2 operation(s) for linking-rules.
  name: FOLIO Linking Rules API
  slug: folio-linking-rules-api
- baseURL: https://localhost:8081
  baseurl_source: spec
  description: The links-suggestions API from FOLIO — 1 operation(s) for links-suggestions.
  name: FOLIO Links Suggestions API
  slug: folio-links-suggestions-api
- baseURL: https://folio-etesting-snapshot-kong.ci.folio.org/
  baseurl_source: spec
  description: The list API from FOLIO — 6 operation(s) for list.
  name: FOLIO List API
  slug: folio-list-api
- baseURL: https://folio-etesting-snapshot-kong.ci.folio.org/
  baseurl_source: spec
  description: The listConfiguration API from FOLIO — 1 operation(s) for listconfiguration.
  name: FOLIO List Configuration API
  slug: folio-listconfiguration-api
- baseURL: https://folio-etesting-snapshot-kong.ci.folio.org/
  baseurl_source: spec
  description: The listExport API from FOLIO — 4 operation(s) for listexport.
  name: FOLIO List Export API
  slug: folio-listexport-api
- baseURL: https://folio-etesting-snapshot-kong.ci.folio.org/
  baseurl_source: spec
  description: The listRelatedUsers API from FOLIO — 1 operation(s) for listrelatedusers.
  name: FOLIO List Related Users API
  slug: folio-listrelatedusers-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The loadable-roles API from FOLIO — 1 operation(s) for loadable-roles.
  name: FOLIO Loadable Roles API
  slug: folio-loadable-roles-api
- description: The Locale API from FOLIO — 1 operation(s) for locale.
  name: FOLIO Locale API
  slug: folio-locale-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The location-mappings API from FOLIO — 2 operation(s) for location-mappings.
  name: FOLIO Location Mappings API
  slug: folio-location-mappings-api
- baseURL: /inventory
  baseurl_source: spec
  description: The locations API from FOLIO — 15 operation(s) for locations.
  name: FOLIO Locations API
  slug: folio-locations-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The logEvents API from FOLIO — 2 operation(s) for logevents.
  name: FOLIO Log Events API
  slug: folio-logevents-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The login API from FOLIO — 6 operation(s) for login.
  name: FOLIO Login API
  slug: folio-login-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The loginAttempts API from FOLIO — 1 operation(s) for loginattempts.
  name: FOLIO Login Attempts API
  slug: folio-loginattempts-api
- baseURL: /data-export/
  baseurl_source: spec
  description: The Logs API from FOLIO — 1 operation(s) for logs.
  name: FOLIO Logs API
  slug: folio-logs-api
- baseURL: /asrService/asr/
  baseurl_source: spec
  description: The LookupAsrRequests API from FOLIO — 1 operation(s) for lookupasrrequests.
  name: FOLIO Lookup Asr Requests API
  slug: folio-lookupasrrequests-api
- baseURL: /asrService/asr/
  baseurl_source: spec
  description: The LookupNewAsrItems API from FOLIO — 1 operation(s) for lookupnewasritems.
  name: FOLIO Lookup New Asr Items API
  slug: folio-lookupnewasritems-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The M-A-R-C-transformation-options-settings API from FOLIO — 2 operation(s) for m-a-r-c-transformation-options-settings.
  name: FOLIO M A R C Transformation Options Settings API
  slug: folio-m-a-r-c-transformation-options-settings-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The M-A-R-C-transformation-records API from FOLIO — 1 operation(s) for m-a-r-c-transformation-records.
  name: FOLIO M A R C Transformation Records API
  slug: folio-m-a-r-c-transformation-records-api
- description: The Mail API from FOLIO — 1 operation(s) for mail.
  name: FOLIO Mail API
  slug: folio-mail-api
- baseURL: /data-export/
  baseurl_source: spec
  description: The Mapping Profiles API from FOLIO — 2 operation(s) for mapping profiles.
  name: FOLIO Mapping Profiles API
  slug: folio-mapping-profiles-api
- baseURL: /remote-storage/
  baseurl_source: spec
  description: The Mappings API from FOLIO — 2 operation(s) for mappings.
  name: FOLIO Mappings API
  slug: folio-mappings-api
- description: MARC migration operations
  name: FOLIO Marc Migrations API
  slug: folio-marc-migrations-api
- baseURL: https://folio-edev-spitfire-diku.ci.folio.org
  baseurl_source: spec
  description: Operations for retrieving MARC field specifications
  name: FOLIO Marc Specifications API
  slug: folio-marc-specifications-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The material-type-mappings API from FOLIO — 2 operation(s) for material-type-mappings.
  name: FOLIO Material Type Mappings API
  slug: folio-material-type-mappings-api
- baseURL: https://folio-etesting-snapshot-kong.ci.folio.org/
  baseurl_source: spec
  description: The materializedViews API from FOLIO — 1 operation(s) for materializedviews.
  name: FOLIO Materialized Views API
  slug: folio-materializedviews-api
- baseURL: /inventory
  baseurl_source: spec
  description: The materialTypes API from FOLIO — 2 operation(s) for materialtypes.
  name: FOLIO Material Types API
  slug: folio-materialtypes-api
- description: The mediatedBatchRequests API from FOLIO — 4 operation(s) for mediatedbatchrequests.
  name: FOLIO Mediated Batch Requests API
  slug: folio-mediatedbatchrequests-api
- description: The mediatedRequestsActions API from FOLIO — 4 operation(s) for mediatedrequestsactions.
  name: FOLIO Mediated Requests Actions API
  slug: folio-mediatedrequestsactions-api
- description: The mediatedRequestsCrud API from FOLIO — 2 operation(s) for mediatedrequestscrud.
  name: FOLIO Mediated Requests Crud API
  slug: folio-mediatedrequestscrud-api
- description: The mediatedRequestsLoans API from FOLIO — 5 operation(s) for mediatedrequestsloans.
  name: FOLIO Mediated Requests Loans API
  slug: folio-mediatedrequestsloans-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The migration API from FOLIO — 5 operation(s) for migration.
  name: FOLIO Migration API
  slug: folio-migration-api
- baseURL: /inventory
  baseurl_source: spec
  description: The modesOfIssuance API from FOLIO — 1 operation(s) for modesofissuance.
  name: FOLIO Modes Of Issuance API
  slug: folio-modesofissuance-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The module-bootstrap API from FOLIO — 2 operation(s) for module-bootstrap.
  name: FOLIO Module Bootstrap API
  slug: folio-module-bootstrap-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The module-discovery API from FOLIO — 2 operation(s) for module-discovery.
  name: FOLIO Module Discovery API
  slug: folio-module-discovery-api
- description: The multiItemBatchRequests API from FOLIO — 4 operation(s) for multiitembatchrequests.
  name: FOLIO Multi Item Batch Requests API
  slug: folio-multiitembatchrequests-api
- baseURL: /inventory
  baseurl_source: spec
  description: The natureOfContentTerms API from FOLIO — 1 operation(s) for natureofcontentterms.
  name: FOLIO Nature Of Content Terms API
  slug: folio-natureofcontentterms-api
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: The node-entity-controller API from FOLIO — 2 operation(s) for node-entity-controller.
  name: FOLIO Node Entity Controller API
  slug: folio-node-entity-controller-api
- description: The note-types API from FOLIO — 2 operation(s) for note-types.
  name: FOLIO Note Types API
  slug: folio-note-types-api
- description: The notes API from FOLIO — 4 operation(s) for notes.
  name: FOLIO Notes API
  slug: folio-notes-api
- baseURL: https://order-stub.com/
  baseurl_source: spec
  description: The Order Stub API from FOLIO — 1 operation(s) for order stub.
  name: FOLIO Order Stub API
  slug: folio-order-stub-api
- baseURL: /ebsconet/
  baseurl_source: spec
  description: The Orders API from FOLIO — 2 operation(s) for orders.
  name: FOLIO Orders API
  slug: folio-orders-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Organisations API from FOLIO — 4 operation(s) for organisations.
  name: FOLIO Organisations API
  slug: folio-organisations-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Packages API from FOLIO — 10 operation(s) for packages.
  name: FOLIO Packages API
  slug: folio-packages-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The paging-slip API from FOLIO — 1 operation(s) for paging-slip.
  name: FOLIO Paging Slip API
  slug: folio-paging-slip-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The paging-slip-template API from FOLIO — 2 operation(s) for paging-slip-template.
  name: FOLIO Paging Slip Template API
  slug: folio-paging-slip-template-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Parties API from FOLIO — 2 operation(s) for parties.
  name: FOLIO Parties API
  slug: folio-parties-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The password API from FOLIO — 6 operation(s) for password.
  name: FOLIO Password API
  slug: folio-password-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The password-reset API from FOLIO — 3 operation(s) for password-reset.
  name: FOLIO Password Reset API
  slug: folio-password-reset-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The patron-type-mapping API from FOLIO — 1 operation(s) for patron-type-mapping.
  name: FOLIO Patron Type Mapping API
  slug: folio-patron-type-mapping-api
- baseURL: /
  baseurl_source: spec
  description: The PatronRequests API from FOLIO — 4 operation(s) for patronrequests.
  name: FOLIO Patron Requests API
  slug: folio-patronrequests-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The PCIs API from FOLIO — 2 operation(s) for pcis.
  name: FOLIO PCIs API
  slug: folio-pcis-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The permissions-users API from FOLIO — 1 operation(s) for permissions-users.
  name: FOLIO Permissions Users API
  slug: folio-permissions-users-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Platforms API from FOLIO — 2 operation(s) for platforms.
  name: FOLIO Platforms API
  slug: folio-platforms-api
- baseURL_template: /consortia/{consortiumId}/sharing
  baseurl_source: spec_template
  description: The Policies API from FOLIO — 4 operation(s) for policies.
  name: FOLIO Policies API
  slug: folio-policies-api
- description: The Print API from FOLIO — 3 operation(s) for print.
  name: FOLIO Print API
  slug: folio-print-api
- description: The profile API from FOLIO — 6 operation(s) for profile.
  name: FOLIO Profile API
  slug: folio-profile-api
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: The profile-controller API from FOLIO — 4 operation(s) for profile-controller.
  name: FOLIO Profile Controller API
  slug: folio-profile-controller-api
- baseURL: /remote-storage/
  baseurl_source: spec
  description: The Providers API from FOLIO — 1 operation(s) for providers.
  name: FOLIO Providers API
  slug: folio-providers-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The proxy-descriptor API from FOLIO — 1 operation(s) for proxy-descriptor.
  name: FOLIO Proxy Descriptor API
  slug: folio-proxy-descriptor-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The proxy-health API from FOLIO — 1 operation(s) for proxy-health.
  name: FOLIO Proxy Health API
  slug: folio-proxy-health-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The proxy-module API from FOLIO — 4 operation(s) for proxy-module.
  name: FOLIO Proxy Module API
  slug: folio-proxy-module-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The proxy-tenant API from FOLIO — 2 operation(s) for proxy-tenant.
  name: FOLIO Proxy Tenant API
  slug: folio-proxy-tenant-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The proxy-tenant-installation API from FOLIO — 3 operation(s) for proxy-tenant-installation.
  name: FOLIO Proxy Tenant Installation API
  slug: folio-proxy-tenant-installation-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The proxy-tenant-interface API from FOLIO — 2 operation(s) for proxy-tenant-interface.
  name: FOLIO Proxy Tenant Interface API
  slug: folio-proxy-tenant-interface-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The proxy-tenant-module API from FOLIO — 2 operation(s) for proxy-tenant-module.
  name: FOLIO Proxy Tenant Module API
  slug: folio-proxy-tenant-module-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The proxy-tenant-timer API from FOLIO — 2 operation(s) for proxy-tenant-timer.
  name: FOLIO Proxy Tenant Timer API
  slug: folio-proxy-tenant-timer-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The PTIs API from FOLIO — 2 operation(s) for ptis.
  name: FOLIO PTIs API
  slug: folio-ptis-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Publication requests API from FOLIO — 2 operation(s) for publication requests.
  name: FOLIO Publication requests API
  slug: folio-publication-requests-api
- baseURL_template: /consortia/{consortiumId}/
  baseurl_source: spec_template
  description: The Publications API from FOLIO — 3 operation(s) for publications.
  name: FOLIO Publications API
  slug: folio-publications-api
- baseURL: https://folio-etesting-snapshot-kong.ci.folio.org/
  baseurl_source: spec
  description: The purgeQuery API from FOLIO — 1 operation(s) for purgequery.
  name: FOLIO Purge Query API
  slug: folio-purgequery-api
- baseURL: /data-export/
  baseurl_source: spec
  description: The Quick Export API from FOLIO — 1 operation(s) for quick export.
  name: FOLIO Quick Export API
  slug: folio-quick-export-api
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: The ramls-controller API from FOLIO — 1 operation(s) for ramls-controller.
  name: FOLIO Ramls Controller API
  slug: folio-ramls-controller-api
- description: The Reading Room API from FOLIO — 4 operation(s) for reading room.
  name: FOLIO Reading Room API
  slug: folio-reading-room-api
- description: The Reading Room Patron Permission API from FOLIO — 1 operation(s) for reading room patron permission.
  name: FOLIO Reading Room Patron Permission API
  slug: folio-reading-room-patron-permission-api
- baseURL: https://folio-edev-spitfire-diku.ci.folio.org
  baseurl_source: spec
  description: Operations for managing MARC records
  name: FOLIO Records Editor API
  slug: folio-records-editor-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Reference data API from FOLIO — 9 operation(s) for reference data.
  name: FOLIO Reference data API
  slug: folio-reference-data-api
- description: The Refresh Presigned Url API from FOLIO — 1 operation(s) for refresh presigned url.
  name: FOLIO Refresh Presigned Url API
  slug: folio-refresh-presigned-url-api
- description: The RefreshShadowLocations API from FOLIO — 1 operation(s) for refreshshadowlocations.
  name: FOLIO Refresh Shadow Locations API
  slug: folio-refreshshadowlocations-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The reinstall API from FOLIO — 2 operation(s) for reinstall.
  name: FOLIO Reinstall API
  slug: folio-reinstall-api
- baseURL: /data-export/
  baseurl_source: spec
  description: The Related Users API from FOLIO — 1 operation(s) for related users.
  name: FOLIO Related Users API
  slug: folio-related-users-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Remote Knowledge Bases API from FOLIO — 2 operation(s) for remote knowledge bases.
  name: FOLIO Remote Knowledge Bases API
  slug: folio-remote-knowledge-bases-api
- baseURL: /
  baseurl_source: spec
  description: The RemoteAction API from FOLIO — 1 operation(s) for remoteaction.
  name: FOLIO Remote Action API
  slug: folio-remoteaction-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Reports API from FOLIO — 3 operation(s) for reports.
  name: FOLIO Reports API
  slug: folio-reports-api
- baseURL: /caiasoftService/
  baseurl_source: spec
  description: The RequestBarcodes API from FOLIO — 1 operation(s) for requestbarcodes.
  name: FOLIO Request Barcodes API
  slug: folio-requestbarcodes-api
- baseURL: /caiasoftService/
  baseurl_source: spec
  description: The Requests API from FOLIO — 1 operation(s) for requests.
  name: FOLIO Requests API
  slug: folio-requests-api
- description: The resource API from FOLIO — 8 operation(s) for resource.
  name: FOLIO Resource API
  slug: folio-resource-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Resources API from FOLIO — 15 operation(s) for resources.
  name: FOLIO Resources API
  slug: folio-resources-api
- baseURL: /remote-storage/
  baseurl_source: spec
  description: The Retrievals API from FOLIO — 3 operation(s) for retrievals.
  name: FOLIO Retrievals API
  slug: folio-retrievals-api
- baseURL: /remote-storage/
  baseurl_source: spec
  description: The Retrieve API from FOLIO — 2 operation(s) for retrieve.
  name: FOLIO Retrieve API
  slug: folio-retrieve-api
- baseURL: /remote-storage/
  baseurl_source: spec
  description: The Return API from FOLIO — 1 operation(s) for return.
  name: FOLIO Return API
  slug: folio-return-api
- baseURL_template: /consortia/{consortiumId}/sharing
  baseurl_source: spec_template
  description: The role-capabilities API from FOLIO — 2 operation(s) for role-capabilities.
  name: FOLIO Role Capabilities API
  slug: folio-role-capabilities-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The role-capability API from FOLIO — 2 operation(s) for role-capability.
  name: FOLIO Role Capability API
  slug: folio-role-capability-api
- baseURL_template: /consortia/{consortiumId}/sharing
  baseurl_source: spec_template
  description: The role-capability-set API from FOLIO — 3 operation(s) for role-capability-set.
  name: FOLIO Role Capability Set API
  slug: folio-role-capability-set-api
- baseURL_template: /consortia/{consortiumId}/sharing
  baseurl_source: spec_template
  description: The roles API from FOLIO — 4 operation(s) for roles.
  name: FOLIO Roles API
  slug: folio-roles-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The roles-users API from FOLIO — 2 operation(s) for roles-users.
  name: FOLIO Roles Users API
  slug: folio-roles-users-api
- description: The RTAC API from FOLIO — 10 operation(s) for rtac.
  name: FOLIO RTAC API
  slug: folio-rtac-api
- baseURL: /tenant/
  baseurl_source: spec
  description: The Rules API from FOLIO — 2 operation(s) for rules.
  name: FOLIO Rules API
  slug: folio-rules-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The Scheduler API from FOLIO — 2 operation(s) for scheduler.
  name: FOLIO Scheduler API
  slug: folio-scheduler-api
- baseURL_template: https://{environment}-okapi.ci.folio.org
  baseurl_source: spec_template
  description: Provides endpoints to search for records (e.g., instances, authorities) using CQL (Contextual Query Language) queries. Supports various search options and retrieval of search results.
  name: FOLIO Search API
  slug: folio-search-api
- baseURL_template: https://{environment}-okapi.ci.folio.org
  baseurl_source: spec_template
  description: Provides endpoints to search for consolidated records (e.g., holdings, items) across multiple institutions or libraries within a consortium.
  name: FOLIO Search Consortium API
  slug: folio-search-consortium-api
- baseURL_template: https://{environment}-okapi.ci.folio.org
  baseurl_source: spec_template
  description: Provides endpoints to retrieve record IDs by CQL queries, without returning the full record data.
  name: FOLIO Search Resources IDs API
  slug: folio-search-resources-ids-api
- baseURL_template: /consortia/{consortiumId}/
  baseurl_source: spec_template
  description: The Self API from FOLIO — 1 operation(s) for self.
  name: FOLIO Self API
  slug: folio-self-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Serials Management API from FOLIO — 20 operation(s) for serials management.
  name: FOLIO Serials Management API
  slug: folio-serials-management-api
- baseURL_template: https://folio-{environment}.ci.folio.org
  baseurl_source: spec_template
  description: Manage service points.
  name: FOLIO Service Points API
  slug: folio-service-points-api
- baseURL_template: https://folio-{environment}.ci.folio.org
  baseurl_source: spec_template
  description: Manage service points users.
  name: FOLIO Service Points Users API
  slug: folio-service-points-users-api
- baseURL: /inventory
  baseurl_source: spec
  description: The servicePoints API from FOLIO — 1 operation(s) for servicepoints.
  name: FOLIO Service Points API
  slug: folio-servicepoints-api
- description: The setting API from FOLIO — 2 operation(s) for setting.
  name: FOLIO Setting API
  slug: folio-setting-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Settings API from FOLIO — 11 operation(s) for settings.
  name: FOLIO Settings API
  slug: folio-settings-api
- description: The Shared Inventory Batch Upsert Matchkey API from FOLIO — 1 operation(s) for shared inventory batch upsert matchkey.
  name: FOLIO Shared Inventory Batch Upsert Matchkey API
  slug: folio-shared-inventory-batch-upsert-matchkey-api
- description: The Shared Inventory Upsert Matchkey API from FOLIO — 2 operation(s) for shared inventory upsert matchkey.
  name: FOLIO Shared Inventory Upsert Matchkey API
  slug: folio-shared-inventory-upsert-matchkey-api
- baseURL: /inventory
  baseurl_source: spec
  description: The sourceRecords API from FOLIO — 1 operation(s) for sourcerecords.
  name: FOLIO Source Records API
  slug: folio-sourcerecords-api
- baseURL_template: https://{environment}-okapi.ci.folio.org
  baseurl_source: spec_template
  description: Provides API for managing specifications.
  name: FOLIO Specification Storage API
  slug: folio-specification-storage-api
- baseURL_template: https://{environment}-okapi.ci.folio.org
  baseurl_source: spec_template
  description: Provides API for managing specification fields.
  name: FOLIO Specification Storage Fields API
  slug: folio-specification-storage-fields-api
- baseURL_template: https://{environment}-okapi.ci.folio.org
  baseurl_source: spec_template
  description: Provides API for managing specification field indicators.
  name: FOLIO Specification Storage Indicators API
  slug: folio-specification-storage-indicators-api
- baseURL_template: https://{environment}-okapi.ci.folio.org
  baseurl_source: spec_template
  description: Provides API for managing specification field subfields.
  name: FOLIO Specification Storage Subfields API
  slug: folio-specification-storage-subfields-api
- baseURL: /tlr/staff-slips
  baseurl_source: spec
  description: The staffSlips API from FOLIO — 2 operation(s) for staffslips.
  name: FOLIO Staff Slips API
  slug: folio-staffslips-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Statistics API from FOLIO — 2 operation(s) for statistics.
  name: FOLIO Statistics API
  slug: folio-statistics-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The String Templates API from FOLIO — 4 operation(s) for string templates.
  name: FOLIO String Templates API
  slug: folio-string-templates-api
- baseURL: https://stub.com/
  baseurl_source: spec
  description: The Stub API from FOLIO — 1 operation(s) for stub.
  name: FOLIO Stub API
  slug: folio-stub-api
- baseURL: /inventory
  baseurl_source: spec
  description: The subjectSources API from FOLIO — 1 operation(s) for subjectsources.
  name: FOLIO Subject Sources API
  slug: folio-subjectsources-api
- baseURL: /inventory
  baseurl_source: spec
  description: The subjectTypes API from FOLIO — 1 operation(s) for subjecttypes.
  name: FOLIO Subject Types API
  slug: folio-subjecttypes-api
- description: The Tags API from FOLIO — 2 operation(s) for tags.
  name: FOLIO Tags API
  slug: folio-tags-api
- baseURL: /mosaic
  baseurl_source: spec
  description: The Template API from FOLIO — 1 operation(s) for template.
  name: FOLIO Template API
  slug: folio-template-api
- description: The Tenant Addresses API from FOLIO — 2 operation(s) for tenant addresses.
  name: FOLIO Tenant Addresses API
  slug: folio-tenant-addresses-api
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: the tenant API
  name: FOLIO Tenant API
  slug: folio-tenant-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The tenant-attributes API from FOLIO — 2 operation(s) for tenant-attributes.
  name: FOLIO Tenant Attributes API
  slug: folio-tenant-attributes-api
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: The tenant-controller API from FOLIO — 1 operation(s) for tenant-controller.
  name: FOLIO Tenant Controller API
  slug: folio-tenant-controller-api
- description: The tenant-settings API from FOLIO — 3 operation(s) for tenant-settings.
  name: FOLIO Tenant Settings API
  slug: folio-tenant-settings-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The tenants API from FOLIO — 7 operation(s) for tenants.
  name: FOLIO Tenants API
  slug: folio-tenants-api
- baseURL: /
  baseurl_source: spec
  description: The TestDocumentDelivery API from FOLIO — 2 operation(s) for testdocumentdelivery.
  name: FOLIO Test Document Delivery API
  slug: folio-testdocumentdelivery-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Title instances API from FOLIO — 2 operation(s) for title instances.
  name: FOLIO Title instances API
  slug: folio-title-instances-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Titles API from FOLIO — 4 operation(s) for titles.
  name: FOLIO Titles API
  slug: folio-titles-api
- description: The tlrSettings API from FOLIO — 1 operation(s) for tlrsettings.
  name: FOLIO Tlr Settings API
  slug: folio-tlrsettings-api
- description: The transactions API from FOLIO — 6 operation(s) for transactions.
  name: FOLIO Transactions API
  slug: folio-transactions-api
- baseURL: /data-export/
  baseurl_source: spec
  description: The Transformation Fields API from FOLIO — 1 operation(s) for transformation fields.
  name: FOLIO Transformation Fields API
  slug: folio-transformation-fields-api
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: The trigger-entity-controller API from FOLIO — 2 operation(s) for trigger-entity-controller.
  name: FOLIO Trigger Entity Controller API
  slug: folio-trigger-entity-controller-api
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: The trigger-search-controller API from FOLIO — 1 operation(s) for trigger-search-controller.
  name: FOLIO Trigger Search Controller API
  slug: folio-trigger-search-controller-api
- baseURL: /asrService/asr/
  baseurl_source: spec
  description: The UpdateASRItemStatusAvailable API from FOLIO — 1 operation(s) for updateasritemstatusavailable.
  name: FOLIO Update ASR Item Status Available API
  slug: folio-updateasritemstatusavailable-api
- baseURL: /asrService/asr/
  baseurl_source: spec
  description: The UpdateASRItemStatusBeingRetrieved API from FOLIO — 1 operation(s) for updateasritemstatusbeingretrieved.
  name: FOLIO Update ASR Item Status Being Retrieved API
  slug: folio-updateasritemstatusbeingretrieved-api
- description: The upload API from FOLIO — 1 operation(s) for upload.
  name: FOLIO Upload API
  slug: folio-upload-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The user-capability API from FOLIO — 2 operation(s) for user-capability.
  name: FOLIO User Capability API
  slug: folio-user-capability-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The user-capability-set API from FOLIO — 3 operation(s) for user-capability-set.
  name: FOLIO User Capability Set API
  slug: folio-user-capability-set-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The user-custom-field-mappings API from FOLIO — 1 operation(s) for user-custom-field-mappings.
  name: FOLIO User Custom Field Mappings API
  slug: folio-user-custom-field-mappings-api
- baseURL_template: /consortia/{consortiumId}/
  baseurl_source: spec_template
  description: The User Tenants API from FOLIO — 2 operation(s) for user tenants.
  name: FOLIO User Tenants API
  slug: folio-user-tenants-api
- baseURL: /users/
  baseurl_source: spec
  description: The Users API from FOLIO — 8 operation(s) for users.
  name: FOLIO Users API
  slug: folio-users-api
- baseURL: /ebsconet/
  baseurl_source: spec
  description: The Validate API from FOLIO — 1 operation(s) for validate.
  name: FOLIO Validate API
  slug: folio-validate-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Validation API from FOLIO — 4 operation(s) for validation.
  name: FOLIO Validation API
  slug: folio-validation-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The verify-patron-d2ir API from FOLIO — 1 operation(s) for verify-patron-d2ir.
  name: FOLIO Verify Patron D2ir API
  slug: folio-verify-patron-d2ir-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: The version API from FOLIO — 1 operation(s) for version.
  name: FOLIO Version API
  slug: folio-version-api
- baseURL: /inn-reach/
  baseurl_source: spec
  description: The visible-patron-field-configuration API from FOLIO — 1 operation(s) for visible-patron-field-configuration.
  name: FOLIO Visible Patron Field Configuration API
  slug: folio-visible-patron-field-configuration-api
- description: The vocabulary API from FOLIO — 1 operation(s) for vocabulary.
  name: FOLIO Vocabulary API
  slug: folio-vocabulary-api
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: The workflow-entity-controller API from FOLIO — 2 operation(s) for workflow-entity-controller.
  name: FOLIO Workflow Entity Controller API
  slug: folio-workflow-entity-controller-api
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: The workflow-property-reference-controller API from FOLIO — 2 operation(s) for workflow-property-reference-controller.
  name: FOLIO Workflow Property Reference Controller API
  slug: folio-workflow-property-reference-controller-api
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: The workflow-search-controller API from FOLIO — 2 operation(s) for workflow-search-controller.
  name: FOLIO Workflow Search Controller API
  slug: folio-workflow-search-controller-api
- baseURL: https://folio-snapshot-okapi.dev.folio.org
  baseurl_source: spec
  description: The Works API from FOLIO — 3 operation(s) for works.
  name: FOLIO Works API
  slug: folio-works-api
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: The work flow controller API from FOLIO — 9 operation(s) for work flow controller.
  name: FOLIO work flow controller API
  slug: folio-work-flow-controller-api
artifact_total: 477
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/capabilities/folio-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/folio-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/agentic-access/folio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/folio-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/rules/folio-rules.yml
  title: ''
  type: Spectral
  url: rules/folio-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/rules/folio-mod-record-specifications-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/folio-mod-record-specifications-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/rules/folio-mod-quick-marc-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/folio-mod-quick-marc-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/json-ld/folio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/folio-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/vocabulary/folio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/folio-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/data-model/folio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/folio-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/components/folio-components.yml
  title: ''
  type: Components
  url: components/folio-components.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/cli/folio-cli.yml
  title: ''
  type: CLI
  url: cli/folio-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/changelog/folio-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/folio-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/conventions/folio-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/folio-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/conventions/folio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/folio-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/sandbox/folio-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/folio-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/lifecycle/folio-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/folio-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/lifecycle/folio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/folio-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/errors/folio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/folio-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/conformance/folio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/folio-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/overlays/folio-edge-caiasoft-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/folio-edge-caiasoft-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/well-known/folio-issues-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/folio-issues-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/well-known/folio-folio-org-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/folio-folio-org-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/well-known/folio-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/folio-api-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/well-known/folio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/folio-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/hosts/folio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/folio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/vendors/folio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/folio-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/packages/folio-packages.yml
  title: ''
  type: SDKs
  url: packages/folio-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/packages/folio-packages.yml
  title: ''
  type: Packages
  url: packages/folio-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/authentication/folio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/folio-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/security/folio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/folio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.folio.org
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/folio-org/mod-record-specifications/blob/0d5ec1fe5628eb7355fa3feefa30d89e929d543e/.spectral.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.folio.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.folio.org/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.folio.org/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.folio.org/start/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/folio-org
- group: company
  title: ''
  type: Newsroom
  url: https://folio.org/about/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://folio.org/privacy-policy
- group: operate
  title: ''
  type: Roadmap
  url: https://folio.org/platform/roadmap/
- group: operate
  title: ''
  type: Community
  url: https://folio.org/community/
- group: other
  title: ''
  type: Wiki
  url: https://folio-org.atlassian.net/wiki/spaces/COMMUNITY/overview
- group: operate
  title: ''
  type: Slack
  url: https://slack-invitation.folio.org/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/folio_lsp
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC4Vs5mb1qgOXPZgso1LESUw
created: '2026-10-09'
description: FOLIO (Future of Libraries is Open) is an open source library services platform (LSP) built by a community of libraries, developers and vendors. Developer documentation and an API reference are published on the FOLIO developer portal (dev.folio.org), user documentation at docs.folio.org, and source code in the folio-org GitHub organization.
image: https://folio.org/wp-content/uploads/2023/08/folio-site-general-Illustration-social-image-1200.jpg
json_schemas:
- name: accessTokenResponse
  property_count: 3
  slug: folio-access-token-response
- name: accessionItem
  property_count: 23
  slug: folio-accession-item
- name: Agreement
  property_count: 28
  slug: folio-agreement
- name: applicationCleanupResult
  property_count: 7
  slug: folio-application-cleanup-result
- name: Application Descriptor Schema
  property_count: 8
  slug: folio-application-descriptor
- name: applicationDescriptors
  property_count: 2
  slug: folio-application-descriptors
- name: applicationDescriptorsValidation
  property_count: 2
  slug: folio-application-descriptors-validation
- name: applicationDiscoveries
  property_count: 2
  slug: folio-application-discoveries
- name: Application Entitlement Flow Schema
  property_count: 9
  slug: folio-application-flow
- name: asrItems
  property_count: 1
  slug: folio-asr-items
- name: asrRequests
  property_count: 1
  slug: folio-asr-requests
- name: authorityDto
  property_count: 81
  slug: folio-authority-dto
- name: authorityNoteTypeDto
  property_count: 4
  slug: folio-authority-note-type-dto
- name: authoritySourceFileDtoCollection
  property_count: 2
  slug: folio-authority-source-file-dto-collection
- name: authoritySourceFileDto
  property_count: 10
  slug: folio-authority-source-file-dto
- name: authorityStatsDtoCollection
  property_count: 2
  slug: folio-authority-stats-dto-collection
- name: baseCircRequestDTO
  property_count: 5
  slug: folio-base-circ-request-dto
- name: BatchHoldingsResponse
  property_count: 2
  slug: folio-batch-holdings-response
- name: bffRequest
  property_count: 22
  slug: folio-bff-request
- name: BulkOperationDto
  property_count: 40
  slug: folio-bulk-operation-dto
- name: calendarCollection
  property_count: 2
  slug: folio-calendar-collection
- name: calendar
  property_count: 8
  slug: folio-calendar
- name: channel
  property_count: 13
  slug: folio-channel
- name: checkInResponse
  property_count: 3
  slug: folio-check-in-response
- name: checkOutResponse
  property_count: 19
  slug: folio-check-out-response
- name: circulationItem
  property_count: 10
  slug: folio-circulation-item
- name: circulationItems
  property_count: 0
  slug: folio-circulation-items
- name: Loan
  property_count: 33
  slug: folio-circulation-loan
- name: ContentsRequest
  property_count: 5
  slug: folio-contents-request
- name: Custom Entity Type Schema
  property_count: 0
  slug: folio-custom-entity-type
- name: CustomPropertyDefinition
  property_count: 10
  slug: folio-custom-property-definition
- name: DashboardWidgetDefinition
  property_count: 4
  slug: folio-dashboard-widget-definition
- name: dataRefreshResponse
  property_count: 2
  slug: folio-data-refresh-response
- name: Tenant Desired State Request Schema
  property_count: 2
  slug: folio-desired-state-request-body
- name: ebsconet_order_line
  property_count: 17
  slug: folio-ebsconet-order-line
- name: EntityType
  property_count: 15
  slug: folio-entity-type
- name: EntityTypeSummaries
  property_count: 2
  slug: folio-entity-type-summaries
- name: entries
  property_count: 2
  slug: folio-entries
- name: entry
  property_count: 5
  slug: folio-entry
- name: ErmResource
  property_count: 17
  slug: folio-erm-resource
- name: exportAllRequest
  property_count: 5
  slug: folio-export-all-request
- name: ExportConfigCollection
  property_count: 2
  slug: folio-export-config-collection
- name: ExportConfig
  property_count: 8
  slug: folio-export-config
- name: ExportEntry
  property_count: 14
  slug: folio-export-entry
- name: exportRequest
  property_count: 11
  slug: folio-export-request
- name: Tenant Entitlement Result Schema
  property_count: 3
  slug: folio-extended-entitlements
- name: failedRecord
  property_count: 11
  slug: folio-failed-record
- name: fileDefinition
  property_count: 8
  slug: folio-file-definition
- name: Control Flow Schema
  property_count: 8
  slug: folio-flow
- name: Flow Stage Schema
  property_count: 10
  slug: folio-flow-stage
- name: importJob
  property_count: 11
  slug: folio-import-job
- name: innReachTransactionDTO
  property_count: 7
  slug: folio-inn-reach-transaction-dto
- name: InstanceHoldings
  property_count: 2
  slug: folio-instance-holdings
- name: instructors
  property_count: 2
  slug: folio-instructors
- name: itemShippedDTO
  property_count: 8
  slug: folio-item-shipped-dto
- name: jobProfile
  property_count: 12
  slug: folio-job-profile
- name: Kb
  property_count: 18
  slug: folio-kb
- name: License
  property_count: 0
  slug: folio-license
- name: license-terms-batch
  property_count: 1
  slug: folio-license-terms-batch
- name: license-terms
  property_count: 1
  slug: folio-license-terms
- name: Link
  property_count: 8
  slug: folio-link
- name: localHoldDTO
  property_count: 10
  slug: folio-local-hold-dto
- name: mappingProfile
  property_count: 14
  slug: folio-mapping-profile
- name: mediatedRequest
  property_count: 31
  slug: folio-mediated-request
- name: Mail Entity Schema
  property_count: 5
  slug: folio-message-request
- name: messageResponse
  property_count: 1
  slug: folio-message-response
- name: moduleDiscoveries
  property_count: 2
  slug: folio-module-discoveries
- name: Module Reinstall Request Schema
  property_count: 3
  slug: folio-module-reinstall-request-body
- name: pagingSlipsDTO
  property_count: 2
  slug: folio-paging-slips-dto
- name: parsedRecordContentCollection
  property_count: 1
  slug: folio-parsed-record-content-collection
- name: Patron Pin Schema
  property_count: 2
  slug: folio-patron-pin-with-id
- name: PersistentJob
  property_count: 14
  slug: folio-persistent-job
- name: PoliciesResponse
  property_count: 6
  slug: folio-policies-response
- name: profile_dto
  property_count: 11
  slug: folio-profile-dto
- name: IDs of deleted queries
  property_count: 1
  slug: folio-purged-queries
- name: QueryDetails
  property_count: 11
  slug: folio-query-details
- name: queryStatusSummaries
  property_count: 0
  slug: folio-query-status-summaries
- name: quickExportRequest
  property_count: 7
  slug: folio-quick-export-request
- name: refreshToken
  property_count: 1
  slug: folio-refresh-token
- name: reportCost
  property_count: 11
  slug: folio-report-cost
- name: reportDataEntries
  property_count: 2
  slug: folio-report-data-entries
- name: report
  property_count: 12
  slug: folio-report
- name: reportStatus
  property_count: 3
  slug: folio-report-status
- name: reportTitles
  property_count: 2
  slug: folio-report-titles
- name: request-ids
  property_count: 1
  slug: folio-request-ids
- name: request
  property_count: 33
  slug: folio-request
- name: ResponseErrors
  property_count: 2
  slug: folio-response-errors
- name: returnItemResponse
  property_count: 1
  slug: folio-return-item-response
- name: rtacRequest
  property_count: 1
  slug: folio-rtac-request
- name: Setting
  property_count: 6
  slug: folio-setting
- name: SettingsCollection
  property_count: 2
  slug: folio-settings-collection
- name: signRefreshToken
  property_count: 2
  slug: folio-sign-refresh-token
- name: signTokenPayload
  property_count: 1
  slug: folio-sign-token-payload
- name: singleDayOpeningCollection
  property_count: 2
  slug: folio-single-day-opening-collection
- name: step
  property_count: 6
  slug: folio-step
- name: SubmitQuery
  property_count: 5
  slug: folio-submit-query
- name: surroundingOpenings
  property_count: 1
  slug: folio-surrounding-openings
- name: Tenant Attribute Schema
  property_count: 4
  slug: folio-tenant-attribute
- name: Tenant job attributes
  property_count: 4
  slug: folio-tenant-attributes
- name: Tenant job
  property_count: 6
  slug: folio-tenant-job
- name: Tenant Schema
  property_count: 7
  slug: folio-tenant
- name: Tenants Schema
  property_count: 2
  slug: folio-tenants
- name: TestDocumentDeliveryOffer
  property_count: 13
  slug: folio-test-document-delivery-offer
- name: TestDocumentDeliveryRegister
  property_count: 4
  slug: folio-test-document-delivery-register
- name: titleDataEntries
  property_count: 2
  slug: folio-title-data-entries
- name: tokenResponseLegacy
  property_count: 1
  slug: folio-token-response-legacy
- name: tokenResponse
  property_count: 3
  slug: folio-token-response
- name: token
  property_count: 1
  slug: folio-token
- name: transactionHoldDTO
  property_count: 27
  slug: folio-transaction-hold-dto
- name: transformation
  property_count: 5
  slug: folio-transformation
- name: transformationStepAssociation
  property_count: 6
  slug: folio-transformation-step-association
- name: updateAsrItem
  property_count: 3
  slug: folio-update-asr-item
- name: UpdateUsedByRequest
  property_count: 2
  slug: folio-update-used-by-request
- name: user-results
  property_count: 3
  slug: folio-user-results
- name: User Schema
  property_count: 20
  slug: folio-userdata
- name: validation_response
  property_count: 1
  slug: folio-validation-response
- name: Workflow
  property_count: 10
  slug: folio-workflow
jsonld:
- class_count: 120
  name: Folio Context
  property_count: 291
  slug: folio-context
layout: provider
modified: '2026-10-09'
name: FOLIO
nav: Providers
network: true
overview: 'FOLIO publishes 352 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Control API, Accessions API, Action Controller API, and 349 more. Tagged areas include Company, Library, Library Services Platform, Open Source, and Microservices.


  The FOLIO catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  FOLIO''s developer surface includes CLI, changelog, sandbox, authentication, documentation, API reference, getting-started guide, and 38 more developer resources.'
plans:
- name: Folio Plans Pricing
  plan_count: 0
  slug: folio-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Folio Rate Limits
  slug: folio-rate-limits
rules:
- authorship: provider
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: FOLIO — mod record specifications rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: folio-mod-record-specifications-spectral-rules
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: FOLIO API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 4
  slug: folio-rules
score:
  band: strong
  composite: 56.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 65.3
    catalog_earned_first_party: 18.0
    catalog_gap: 49.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.1
  facets:
    access_clarity: 10.5
    contract_governance: 76.5
    contract_quality: 55.3
    developer_ergonomics: 78.0
    discoverability: 64.3
    operational_transparency: 34.2
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 29.5
      derived: 0
      marker_coverage: 0.0
      total: 301
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 50.0
screenshot: https://raw.githubusercontent.com/api-evangelist/folio/refs/heads/main/screenshots/folio-2026-10-11T104602.png
security:
- kind: authentication
  name: Folio Authentication
  slug: folio-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Folio Domain Security
  slug: folio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: folio
tags:
- Company
- Library
- Library Services Platform
- Open Source
- Microservices
- Education
website: https://www.folio.org
---
