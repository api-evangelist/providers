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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 28.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Solarwinds Agentic Access
  operation_count: 47
  slug: solarwinds-agentic-access
  summary_line: 47 operations · 17 acting
api_count: 5
apis:
- description: API for database monitoring and performance analysis.
  name: SolarWinds Database Performance Analyzer API
  slug: solarwinds-dpa-api
- description: Network Performance Monitor REST API for network device monitoring.
  name: SolarWinds NPM REST API
  slug: solarwinds-npm-rest-api
- description: REST API for creating, reading, updating, and deleting data in Web Help Desk including tickets, clients, assets, and locations.
  name: SolarWinds Web Help Desk API
  slug: solarwinds-whd-api
- description: API for IP address management providing CRUD operations for subnets, IP addresses, and DNS entries through the SolarWinds Information Service.
  name: SolarWinds IPAM API
  slug: solarwinds-ipam-api
- description: API for network configuration management providing automation of configuration backups, change management, and compliance through the SolarWinds Information Service.
  name: SolarWinds NCM API
  slug: solarwinds-ncm-api
- description: Server and Application Monitor API for monitoring application health and performance using the API Poller feature and SolarWinds Information Service.
  name: SolarWinds SAM API
  slug: solarwinds-sam-api
- description: REST API for application performance monitoring providing CRUD access to metrics, dashboards, alerts, and traces. Supports custom metrics submission and distributed tracing for cloud-native applicatio
  name: SolarWinds AppOptics API
  slug: solarwinds-appoptics-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Account information and management
  name: SolarWinds Account API
  slug: solarwinds-account-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Manage hardware and software assets
  name: SolarWinds Assets API
  slug: solarwinds-assets-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Perform bulk create, update, and delete operations
  name: SolarWinds BulkOperations API
  slug: solarwinds-bulkoperations-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Manage categories for incidents and requests
  name: SolarWinds Categories API
  slug: solarwinds-categories-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Manage change requests
  name: SolarWinds Changes API
  slug: solarwinds-changes-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Manage uptime and transaction checks
  name: SolarWinds Checks API
  slug: solarwinds-checks-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Manage alert contacts
  name: SolarWinds Contacts API
  slug: solarwinds-contacts-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Create, read, update, and delete operations on SWIS entities
  name: SolarWinds CRUD API
  slug: solarwinds-crud-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Search and retrieve log events
  name: SolarWinds Events API
  slug: solarwinds-events-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Manage system groups
  name: SolarWinds Groups API
  slug: solarwinds-groups-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Manage IT incidents
  name: SolarWinds Incidents API
  slug: solarwinds-incidents-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Invoke verbs (methods) on SWIS entities
  name: SolarWinds Invoke API
  slug: solarwinds-invoke-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Manage maintenance windows
  name: SolarWinds Maintenance API
  slug: solarwinds-maintenance-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: List available probe servers
  name: SolarWinds ProbeServers API
  slug: solarwinds-probeservers-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Manage problem records
  name: SolarWinds Problems API
  slug: solarwinds-problems-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Execute SWQL queries against the SolarWinds Information Service
  name: SolarWinds Query API
  slug: solarwinds-query-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Retrieve check results and performance data
  name: SolarWinds Results API
  slug: solarwinds-results-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Manage saved searches
  name: SolarWinds SavedSearches API
  slug: solarwinds-savedsearches-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Search and retrieve log events
  name: SolarWinds Search API
  slug: solarwinds-search-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Manage service requests
  name: SolarWinds ServiceRequests API
  slug: solarwinds-servicerequests-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Retrieve performance and outage summaries
  name: SolarWinds Summary API
  slug: solarwinds-summary-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Manage log-sending systems
  name: SolarWinds Systems API
  slug: solarwinds-systems-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Manage alert teams
  name: SolarWinds Teams API
  slug: solarwinds-teams-api
- baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
  baseurl_source: declared
  description: Manage user accounts
  name: SolarWinds Users API
  slug: solarwinds-users-api
artifact_total: 332
collections:
- collection_type: postman
  name: SolarWinds Loggly Account API
  slug: postman-solarwinds-account-api
- collection_type: postman
  name: SolarWinds Loggly Account Assets API
  slug: postman-solarwinds-assets-api
- collection_type: postman
  name: SolarWinds Loggly Account BulkOperations API
  slug: postman-solarwinds-bulkoperations-api
- collection_type: postman
  name: SolarWinds Loggly Account Categories API
  slug: postman-solarwinds-categories-api
- collection_type: postman
  name: SolarWinds Loggly Account Changes API
  slug: postman-solarwinds-changes-api
- collection_type: postman
  name: SolarWinds Loggly Account Checks API
  slug: postman-solarwinds-checks-api
- collection_type: postman
  name: SolarWinds Loggly Account Contacts API
  slug: postman-solarwinds-contacts-api
- collection_type: postman
  name: SolarWinds Loggly Account CRUD API
  slug: postman-solarwinds-crud-api
- collection_type: postman
  name: SolarWinds Loggly Account Events API
  slug: postman-solarwinds-events-api
- collection_type: postman
  name: SolarWinds Loggly Account Groups API
  slug: postman-solarwinds-groups-api
- collection_type: postman
  name: SolarWinds Loggly Account Incidents API
  slug: postman-solarwinds-incidents-api
- collection_type: postman
  name: SolarWinds Loggly Account Invoke API
  slug: postman-solarwinds-invoke-api
- collection_type: postman
  name: SolarWinds Loggly Account Maintenance API
  slug: postman-solarwinds-maintenance-api
- collection_type: postman
  name: SolarWinds Loggly Account ProbeServers API
  slug: postman-solarwinds-probeservers-api
- collection_type: postman
  name: SolarWinds Loggly Account Problems API
  slug: postman-solarwinds-problems-api
- collection_type: postman
  name: SolarWinds Loggly Account Query API
  slug: postman-solarwinds-query-api
- collection_type: postman
  name: SolarWinds Loggly Account Results API
  slug: postman-solarwinds-results-api
- collection_type: postman
  name: SolarWinds Loggly Account SavedSearches API
  slug: postman-solarwinds-savedsearches-api
- collection_type: postman
  name: SolarWinds Loggly Account Search API
  slug: postman-solarwinds-search-api
- collection_type: postman
  name: SolarWinds Loggly Account ServiceRequests API
  slug: postman-solarwinds-servicerequests-api
- collection_type: postman
  name: SolarWinds Loggly Account Summary API
  slug: postman-solarwinds-summary-api
- collection_type: postman
  name: SolarWinds Loggly Account Systems API
  slug: postman-solarwinds-systems-api
- collection_type: postman
  name: SolarWinds Loggly Account Teams API
  slug: postman-solarwinds-teams-api
- collection_type: postman
  name: SolarWinds Loggly Account Users API
  slug: postman-solarwinds-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SolarWinds Loggly Account API
  slug: open-solarwinds-account-api
- collection_type: open
  name: SolarWinds Loggly Account Assets API
  slug: open-solarwinds-assets-api
- collection_type: open
  name: SolarWinds Loggly Account BulkOperations API
  slug: open-solarwinds-bulkoperations-api
- collection_type: open
  name: SolarWinds Loggly Account Categories API
  slug: open-solarwinds-categories-api
- collection_type: open
  name: SolarWinds Loggly Account Changes API
  slug: open-solarwinds-changes-api
- collection_type: open
  name: SolarWinds Loggly Account Checks API
  slug: open-solarwinds-checks-api
- collection_type: open
  name: SolarWinds Loggly Account Contacts API
  slug: open-solarwinds-contacts-api
- collection_type: open
  name: SolarWinds Loggly Account CRUD API
  slug: open-solarwinds-crud-api
- collection_type: open
  name: SolarWinds Loggly Account Events API
  slug: open-solarwinds-events-api
- collection_type: open
  name: SolarWinds Loggly Account Groups API
  slug: open-solarwinds-groups-api
- collection_type: open
  name: SolarWinds Loggly Account Incidents API
  slug: open-solarwinds-incidents-api
- collection_type: open
  name: SolarWinds Loggly Account Invoke API
  slug: open-solarwinds-invoke-api
- collection_type: open
  name: SolarWinds Loggly API
  slug: open-solarwinds-loggly
- collection_type: open
  name: SolarWinds Loggly Account Maintenance API
  slug: open-solarwinds-maintenance-api
- collection_type: open
  name: SolarWinds Orion Platform API
  slug: open-solarwinds-orion
- collection_type: open
  name: SolarWinds Papertrail API
  slug: open-solarwinds-papertrail
- collection_type: open
  name: SolarWinds Pingdom API
  slug: open-solarwinds-pingdom
- collection_type: open
  name: SolarWinds Loggly Account ProbeServers API
  slug: open-solarwinds-probeservers-api
- collection_type: open
  name: SolarWinds Loggly Account Problems API
  slug: open-solarwinds-problems-api
- collection_type: open
  name: SolarWinds Loggly Account Query API
  slug: open-solarwinds-query-api
- collection_type: open
  name: SolarWinds Loggly Account Results API
  slug: open-solarwinds-results-api
- collection_type: open
  name: SolarWinds Loggly Account SavedSearches API
  slug: open-solarwinds-savedsearches-api
- collection_type: open
  name: SolarWinds Loggly Account Search API
  slug: open-solarwinds-search-api
- collection_type: open
  name: SolarWinds Service Desk API
  slug: open-solarwinds-service-desk
- collection_type: open
  name: SolarWinds Loggly Account ServiceRequests API
  slug: open-solarwinds-servicerequests-api
- collection_type: open
  name: SolarWinds Loggly Account Summary API
  slug: open-solarwinds-summary-api
- collection_type: open
  name: SolarWinds Loggly Account Systems API
  slug: open-solarwinds-systems-api
- collection_type: open
  name: SolarWinds Loggly Account Teams API
  slug: open-solarwinds-teams-api
- collection_type: open
  name: SolarWinds Loggly Account Users API
  slug: open-solarwinds-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/solarwinds-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/solarwinds/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/solarwinds-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solarwinds-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/solarwinds-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.solarwinds.com
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.solarwinds.com
- group: operate
  title: ''
  type: Support
  url: https://support.solarwinds.com
- group: company
  title: ''
  type: Blog
  url: https://www.solarwinds.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/solarwinds
- group: operate
  title: ''
  type: StatusPage
  url: https://status.solarwinds.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.solarwinds.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.solarwinds.com/legal/terms
- group: start
  title: ''
  type: Login
  url: https://customerportal.solarwinds.com
- group: auth
  title: ''
  type: Security
  url: https://www.solarwinds.com/information-security
- group: other
  title: ''
  type: X
  url: https://twitter.com/solarwinds
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/solarwinds
- group: build
  title: ''
  type: SDKs
  url: https://github.com/solarwinds/OrionSDK
- group: build
  title: ''
  type: CLI
  url: https://github.com/solarwinds/OrionSDK/tree/master/Samples/PowerShell
- group: design
  title: ''
  type: JSONLD
  url: json-ld/solarwinds-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/solarwinds-node-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/solarwinds-alert-schema.json
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/solarwinds/gns3-skills
created: '2024-01-15'
description: A collection of APIs provided by SolarWinds for IT infrastructure management, monitoring, and observability.
examples:
- key_count: 6
  name: Solarwinds Bulkdelete Example
  slug: solarwinds-bulkdelete-example
- key_count: 6
  name: Solarwinds Bulkupdate Example
  slug: solarwinds-bulkupdate-example
- key_count: 6
  name: Solarwinds Createcheck Example
  slug: solarwinds-createcheck-example
- key_count: 6
  name: Solarwinds Createentity Example
  slug: solarwinds-createentity-example
- key_count: 6
  name: Solarwinds Createincident Example
  slug: solarwinds-createincident-example
- key_count: 6
  name: Solarwinds Createservicerequest Example
  slug: solarwinds-createservicerequest-example
- key_count: 6
  name: Solarwinds Getaccountinfo Example
  slug: solarwinds-getaccountinfo-example
- key_count: 6
  name: Solarwinds Getcheck Example
  slug: solarwinds-getcheck-example
- key_count: 6
  name: Solarwinds Getevents Example
  slug: solarwinds-getevents-example
- key_count: 6
  name: Solarwinds Getgroup Example
  slug: solarwinds-getgroup-example
- key_count: 6
  name: Solarwinds Getincident Example
  slug: solarwinds-getincident-example
- key_count: 6
  name: Solarwinds Getresults Example
  slug: solarwinds-getresults-example
- key_count: 6
  name: Solarwinds Getsummaryaverage Example
  slug: solarwinds-getsummaryaverage-example
- key_count: 6
  name: Solarwinds Getsummaryoutage Example
  slug: solarwinds-getsummaryoutage-example
- key_count: 6
  name: Solarwinds Getsystem Example
  slug: solarwinds-getsystem-example
- key_count: 6
  name: Solarwinds Invokeverb Example
  slug: solarwinds-invokeverb-example
- key_count: 6
  name: Solarwinds Iterateevents Example
  slug: solarwinds-iterateevents-example
- key_count: 6
  name: Solarwinds Listassets Example
  slug: solarwinds-listassets-example
- key_count: 6
  name: Solarwinds Listcategories Example
  slug: solarwinds-listcategories-example
- key_count: 6
  name: Solarwinds Listchanges Example
  slug: solarwinds-listchanges-example
- key_count: 6
  name: Solarwinds Listchecks Example
  slug: solarwinds-listchecks-example
- key_count: 6
  name: Solarwinds Listcontacts Example
  slug: solarwinds-listcontacts-example
- key_count: 6
  name: Solarwinds Listgroups Example
  slug: solarwinds-listgroups-example
- key_count: 6
  name: Solarwinds Listincidents Example
  slug: solarwinds-listincidents-example
- key_count: 6
  name: Solarwinds Listmaintenancewindows Example
  slug: solarwinds-listmaintenancewindows-example
- key_count: 6
  name: Solarwinds Listprobes Example
  slug: solarwinds-listprobes-example
- key_count: 6
  name: Solarwinds Listproblems Example
  slug: solarwinds-listproblems-example
- key_count: 6
  name: Solarwinds Listsavedsearches Example
  slug: solarwinds-listsavedsearches-example
- key_count: 6
  name: Solarwinds Listservicerequests Example
  slug: solarwinds-listservicerequests-example
- key_count: 6
  name: Solarwinds Listsystems Example
  slug: solarwinds-listsystems-example
- key_count: 6
  name: Solarwinds Listteams Example
  slug: solarwinds-listteams-example
- key_count: 6
  name: Solarwinds Listusers Example
  slug: solarwinds-listusers-example
- key_count: 5
  name: Solarwinds Loggly Account Info Example
  slug: solarwinds-loggly-account-info-example
- key_count: 3
  name: Solarwinds Loggly Events Response Example
  slug: solarwinds-loggly-events-response-example
- key_count: 2
  name: Solarwinds Loggly Iterate Response Example
  slug: solarwinds-loggly-iterate-response-example
- key_count: 6
  name: Solarwinds Loggly Log Event Example
  slug: solarwinds-loggly-log-event-example
- key_count: 1
  name: Solarwinds Loggly Search Response Example
  slug: solarwinds-loggly-search-response-example
- key_count: 1
  name: Solarwinds Orion Bulk Delete Request Example
  slug: solarwinds-orion-bulk-delete-request-example
- key_count: 2
  name: Solarwinds Orion Bulk Update Request Example
  slug: solarwinds-orion-bulk-update-request-example
- key_count: 2
  name: Solarwinds Orion Query Request Example
  slug: solarwinds-orion-query-request-example
- key_count: 1
  name: Solarwinds Orion Query Result Example
  slug: solarwinds-orion-query-result-example
- key_count: 12
  name: Solarwinds Papertrail Event Example
  slug: solarwinds-papertrail-event-example
- key_count: 5
  name: Solarwinds Papertrail Event Search Result Example
  slug: solarwinds-papertrail-event-search-result-example
- key_count: 4
  name: Solarwinds Papertrail Group Example
  slug: solarwinds-papertrail-group-example
- key_count: 3
  name: Solarwinds Papertrail Saved Search Example
  slug: solarwinds-papertrail-saved-search-example
- key_count: 1
  name: Solarwinds Papertrail System Create Example
  slug: solarwinds-papertrail-system-create-example
- key_count: 7
  name: Solarwinds Papertrail System Example
  slug: solarwinds-papertrail-system-example
- key_count: 1
  name: Solarwinds Papertrail System Update Example
  slug: solarwinds-papertrail-system-update-example
- key_count: 3
  name: Solarwinds Papertrail User Example
  slug: solarwinds-papertrail-user-example
- key_count: 6
  name: Solarwinds Pingdom Check Create Example
  slug: solarwinds-pingdom-check-create-example
- key_count: 1
  name: Solarwinds Pingdom Check Detail Example
  slug: solarwinds-pingdom-check-detail-example
- key_count: 10
  name: Solarwinds Pingdom Check Example
  slug: solarwinds-pingdom-check-example
- key_count: 2
  name: Solarwinds Pingdom Check List Example
  slug: solarwinds-pingdom-check-list-example
- key_count: 4
  name: Solarwinds Pingdom Check Update Example
  slug: solarwinds-pingdom-check-update-example
- key_count: 1
  name: Solarwinds Pingdom Contact List Example
  slug: solarwinds-pingdom-contact-list-example
- key_count: 1
  name: Solarwinds Pingdom Maintenance List Example
  slug: solarwinds-pingdom-maintenance-list-example
- key_count: 1
  name: Solarwinds Pingdom Probe List Example
  slug: solarwinds-pingdom-probe-list-example
- key_count: 6
  name: Solarwinds Pingdom Result Example
  slug: solarwinds-pingdom-result-example
- key_count: 1
  name: Solarwinds Pingdom Result List Example
  slug: solarwinds-pingdom-result-list-example
- key_count: 1
  name: Solarwinds Pingdom Summary Average Example
  slug: solarwinds-pingdom-summary-average-example
- key_count: 1
  name: Solarwinds Pingdom Summary Outage Example
  slug: solarwinds-pingdom-summary-outage-example
- key_count: 1
  name: Solarwinds Pingdom Team List Example
  slug: solarwinds-pingdom-team-list-example
- key_count: 6
  name: Solarwinds Queryswis Example
  slug: solarwinds-queryswis-example
- key_count: 6
  name: Solarwinds Queryswispost Example
  slug: solarwinds-queryswispost-example
- key_count: 6
  name: Solarwinds Readentity Example
  slug: solarwinds-readentity-example
- key_count: 6
  name: Solarwinds Registersystem Example
  slug: solarwinds-registersystem-example
- key_count: 6
  name: Solarwinds Searchevents Example
  slug: solarwinds-searchevents-example
- key_count: 6
  name: Solarwinds Service Desk Asset Example
  slug: solarwinds-service-desk-asset-example
- key_count: 3
  name: Solarwinds Service Desk Category Example
  slug: solarwinds-service-desk-category-example
- key_count: 2
  name: Solarwinds Service Desk Category Ref Example
  slug: solarwinds-service-desk-category-ref-example
- key_count: 8
  name: Solarwinds Service Desk Change Example
  slug: solarwinds-service-desk-change-example
- key_count: 1
  name: Solarwinds Service Desk Incident Create Example
  slug: solarwinds-service-desk-incident-create-example
- key_count: 8
  name: Solarwinds Service Desk Incident Example
  slug: solarwinds-service-desk-incident-example
- key_count: 1
  name: Solarwinds Service Desk Incident Update Example
  slug: solarwinds-service-desk-incident-update-example
- key_count: 7
  name: Solarwinds Service Desk Problem Example
  slug: solarwinds-service-desk-problem-example
- key_count: 1
  name: Solarwinds Service Desk Service Request Create Example
  slug: solarwinds-service-desk-service-request-create-example
- key_count: 7
  name: Solarwinds Service Desk Service Request Example
  slug: solarwinds-service-desk-service-request-example
- key_count: 5
  name: Solarwinds Service Desk User Example
  slug: solarwinds-service-desk-user-example
- key_count: 3
  name: Solarwinds Service Desk User Ref Example
  slug: solarwinds-service-desk-user-ref-example
- key_count: 6
  name: Solarwinds Updatecheck Example
  slug: solarwinds-updatecheck-example
- key_count: 6
  name: Solarwinds Updateentity Example
  slug: solarwinds-updateentity-example
- key_count: 6
  name: Solarwinds Updateincident Example
  slug: solarwinds-updateincident-example
- key_count: 6
  name: Solarwinds Updatesystem Example
  slug: solarwinds-updatesystem-example
features:
- Network Device Monitoring via SWIS/SWQL
- IT Service Management and Ticketing
- Cloud-Native Observability (Logs, Metrics, Traces)
- Website Uptime and Synthetic Monitoring
- Cloud-Based Log Aggregation and Search
- Database Performance Analysis
- IP Address Management
- Network Configuration Compliance
finops:
- name: Solarwinds Finops
  service_category: IT Management and Observability
  slug: solarwinds-finops
image: https://www.solarwinds.com/sites/all/themes/solarwinds_theme/logo.png
integrations:
- Slack
- PagerDuty
- Microsoft Teams
- ServiceNow
- Jira
- AWS CloudWatch
- Azure Monitor
- Splunk
json_schemas:
- name: AccountInfo
  property_count: 5
  slug: solarwinds-accountinfo
- name: SolarWinds Alert
  property_count: 13
  slug: solarwinds-alert
- name: Asset
  property_count: 7
  slug: solarwinds-asset
- name: BulkDeleteRequest
  property_count: 1
  slug: solarwinds-bulkdeleterequest
- name: BulkUpdateRequest
  property_count: 2
  slug: solarwinds-bulkupdaterequest
- name: Category
  property_count: 3
  slug: solarwinds-category
- name: CategoryRef
  property_count: 2
  slug: solarwinds-categoryref
- name: Change
  property_count: 8
  slug: solarwinds-change
- name: Check
  property_count: 10
  slug: solarwinds-check
- name: CheckCreate
  property_count: 6
  slug: solarwinds-checkcreate
- name: CheckDetail
  property_count: 1
  slug: solarwinds-checkdetail
- name: CheckList
  property_count: 2
  slug: solarwinds-checklist
- name: CheckUpdate
  property_count: 4
  slug: solarwinds-checkupdate
- name: ContactList
  property_count: 1
  slug: solarwinds-contactlist
- name: Event
  property_count: 12
  slug: solarwinds-event
- name: EventSearchResult
  property_count: 5
  slug: solarwinds-eventsearchresult
- name: EventsResponse
  property_count: 3
  slug: solarwinds-eventsresponse
- name: Group
  property_count: 4
  slug: solarwinds-group
- name: Incident
  property_count: 11
  slug: solarwinds-incident
- name: IncidentCreate
  property_count: 1
  slug: solarwinds-incidentcreate
- name: IncidentUpdate
  property_count: 1
  slug: solarwinds-incidentupdate
- name: IterateResponse
  property_count: 2
  slug: solarwinds-iterateresponse
- name: LogEvent
  property_count: 6
  slug: solarwinds-logevent
- name: AccountInfo
  property_count: 5
  slug: solarwinds-loggly-account-info
- name: EventsResponse
  property_count: 3
  slug: solarwinds-loggly-events-response
- name: IterateResponse
  property_count: 2
  slug: solarwinds-loggly-iterate-response
- name: LogEvent
  property_count: 6
  slug: solarwinds-loggly-log-event
- name: SearchResponse
  property_count: 1
  slug: solarwinds-loggly-search-response
- name: MaintenanceList
  property_count: 1
  slug: solarwinds-maintenancelist
- name: SolarWinds Monitored Node
  property_count: 24
  slug: solarwinds-node
- name: BulkDeleteRequest
  property_count: 1
  slug: solarwinds-orion-bulk-delete-request
- name: BulkUpdateRequest
  property_count: 2
  slug: solarwinds-orion-bulk-update-request
- name: QueryRequest
  property_count: 2
  slug: solarwinds-orion-query-request
- name: QueryResult
  property_count: 1
  slug: solarwinds-orion-query-result
- name: Event
  property_count: 12
  slug: solarwinds-papertrail-event
- name: EventSearchResult
  property_count: 5
  slug: solarwinds-papertrail-event-search-result
- name: Group
  property_count: 4
  slug: solarwinds-papertrail-group
- name: SavedSearch
  property_count: 3
  slug: solarwinds-papertrail-saved-search
- name: SystemCreate
  property_count: 1
  slug: solarwinds-papertrail-system-create
- name: System
  property_count: 7
  slug: solarwinds-papertrail-system
- name: SystemUpdate
  property_count: 1
  slug: solarwinds-papertrail-system-update
- name: User
  property_count: 3
  slug: solarwinds-papertrail-user
- name: CheckCreate
  property_count: 6
  slug: solarwinds-pingdom-check-create
- name: CheckDetail
  property_count: 1
  slug: solarwinds-pingdom-check-detail
- name: CheckList
  property_count: 2
  slug: solarwinds-pingdom-check-list
- name: Check
  property_count: 10
  slug: solarwinds-pingdom-check
- name: CheckUpdate
  property_count: 4
  slug: solarwinds-pingdom-check-update
- name: ContactList
  property_count: 1
  slug: solarwinds-pingdom-contact-list
- name: MaintenanceList
  property_count: 1
  slug: solarwinds-pingdom-maintenance-list
- name: ProbeList
  property_count: 1
  slug: solarwinds-pingdom-probe-list
- name: ResultList
  property_count: 1
  slug: solarwinds-pingdom-result-list
- name: Result
  property_count: 6
  slug: solarwinds-pingdom-result
- name: SummaryAverage
  property_count: 1
  slug: solarwinds-pingdom-summary-average
- name: SummaryOutage
  property_count: 1
  slug: solarwinds-pingdom-summary-outage
- name: TeamList
  property_count: 1
  slug: solarwinds-pingdom-team-list
- name: ProbeList
  property_count: 1
  slug: solarwinds-probelist
- name: Problem
  property_count: 7
  slug: solarwinds-problem
- name: QueryRequest
  property_count: 2
  slug: solarwinds-queryrequest
- name: QueryResult
  property_count: 1
  slug: solarwinds-queryresult
- name: Result
  property_count: 6
  slug: solarwinds-result
- name: ResultList
  property_count: 1
  slug: solarwinds-resultlist
- name: SavedSearch
  property_count: 4
  slug: solarwinds-savedsearch
- name: SearchResponse
  property_count: 1
  slug: solarwinds-searchresponse
- name: Asset
  property_count: 6
  slug: solarwinds-service-desk-asset
- name: CategoryRef
  property_count: 2
  slug: solarwinds-service-desk-category-ref
- name: Category
  property_count: 3
  slug: solarwinds-service-desk-category
- name: Change
  property_count: 8
  slug: solarwinds-service-desk-change
- name: IncidentCreate
  property_count: 1
  slug: solarwinds-service-desk-incident-create
- name: Incident
  property_count: 8
  slug: solarwinds-service-desk-incident
- name: IncidentUpdate
  property_count: 1
  slug: solarwinds-service-desk-incident-update
- name: Problem
  property_count: 7
  slug: solarwinds-service-desk-problem
- name: ServiceRequestCreate
  property_count: 1
  slug: solarwinds-service-desk-service-request-create
- name: ServiceRequest
  property_count: 7
  slug: solarwinds-service-desk-service-request
- name: UserRef
  property_count: 3
  slug: solarwinds-service-desk-user-ref
- name: User
  property_count: 5
  slug: solarwinds-service-desk-user
- name: ServiceRequest
  property_count: 8
  slug: solarwinds-servicerequest
- name: ServiceRequestCreate
  property_count: 1
  slug: solarwinds-servicerequestcreate
- name: SummaryAverage
  property_count: 1
  slug: solarwinds-summaryaverage
- name: SummaryOutage
  property_count: 1
  slug: solarwinds-summaryoutage
- name: System
  property_count: 7
  slug: solarwinds-system
- name: SystemCreate
  property_count: 1
  slug: solarwinds-systemcreate
- name: SystemUpdate
  property_count: 1
  slug: solarwinds-systemupdate
- name: TeamList
  property_count: 1
  slug: solarwinds-teamlist
- name: User
  property_count: 3
  slug: solarwinds-user
- name: UserRef
  property_count: 3
  slug: solarwinds-userref
json_structures:
- name: Solarwinds Loggly Account Info Structure
  property_count: 5
  slug: solarwinds-loggly-account-info-structure
- name: Solarwinds Loggly Events Response Structure
  property_count: 3
  slug: solarwinds-loggly-events-response-structure
- name: Solarwinds Loggly Iterate Response Structure
  property_count: 2
  slug: solarwinds-loggly-iterate-response-structure
- name: Solarwinds Loggly Log Event Structure
  property_count: 6
  slug: solarwinds-loggly-log-event-structure
- name: Solarwinds Loggly Search Response Structure
  property_count: 1
  slug: solarwinds-loggly-search-response-structure
- name: Solarwinds Orion Bulk Delete Request Structure
  property_count: 1
  slug: solarwinds-orion-bulk-delete-request-structure
- name: Solarwinds Orion Bulk Update Request Structure
  property_count: 2
  slug: solarwinds-orion-bulk-update-request-structure
- name: Solarwinds Orion Query Request Structure
  property_count: 2
  slug: solarwinds-orion-query-request-structure
- name: Solarwinds Orion Query Result Structure
  property_count: 1
  slug: solarwinds-orion-query-result-structure
- name: Solarwinds Papertrail Event Search Result Structure
  property_count: 5
  slug: solarwinds-papertrail-event-search-result-structure
- name: Solarwinds Papertrail Event Structure
  property_count: 12
  slug: solarwinds-papertrail-event-structure
- name: Solarwinds Papertrail Group Structure
  property_count: 4
  slug: solarwinds-papertrail-group-structure
- name: Solarwinds Papertrail Saved Search Structure
  property_count: 3
  slug: solarwinds-papertrail-saved-search-structure
- name: Solarwinds Papertrail System Create Structure
  property_count: 1
  slug: solarwinds-papertrail-system-create-structure
- name: Solarwinds Papertrail System Structure
  property_count: 7
  slug: solarwinds-papertrail-system-structure
- name: Solarwinds Papertrail System Update Structure
  property_count: 1
  slug: solarwinds-papertrail-system-update-structure
- name: Solarwinds Papertrail User Structure
  property_count: 3
  slug: solarwinds-papertrail-user-structure
- name: Solarwinds Pingdom Check Create Structure
  property_count: 6
  slug: solarwinds-pingdom-check-create-structure
- name: Solarwinds Pingdom Check Detail Structure
  property_count: 1
  slug: solarwinds-pingdom-check-detail-structure
- name: Solarwinds Pingdom Check List Structure
  property_count: 2
  slug: solarwinds-pingdom-check-list-structure
- name: Solarwinds Pingdom Check Structure
  property_count: 10
  slug: solarwinds-pingdom-check-structure
- name: Solarwinds Pingdom Check Update Structure
  property_count: 4
  slug: solarwinds-pingdom-check-update-structure
- name: Solarwinds Pingdom Contact List Structure
  property_count: 1
  slug: solarwinds-pingdom-contact-list-structure
- name: Solarwinds Pingdom Maintenance List Structure
  property_count: 1
  slug: solarwinds-pingdom-maintenance-list-structure
- name: Solarwinds Pingdom Probe List Structure
  property_count: 1
  slug: solarwinds-pingdom-probe-list-structure
- name: Solarwinds Pingdom Result List Structure
  property_count: 1
  slug: solarwinds-pingdom-result-list-structure
- name: Solarwinds Pingdom Result Structure
  property_count: 6
  slug: solarwinds-pingdom-result-structure
- name: Solarwinds Pingdom Summary Average Structure
  property_count: 1
  slug: solarwinds-pingdom-summary-average-structure
- name: Solarwinds Pingdom Summary Outage Structure
  property_count: 1
  slug: solarwinds-pingdom-summary-outage-structure
- name: Solarwinds Pingdom Team List Structure
  property_count: 1
  slug: solarwinds-pingdom-team-list-structure
- name: Solarwinds Service Desk Asset Structure
  property_count: 6
  slug: solarwinds-service-desk-asset-structure
- name: Solarwinds Service Desk Category Ref Structure
  property_count: 2
  slug: solarwinds-service-desk-category-ref-structure
- name: Solarwinds Service Desk Category Structure
  property_count: 3
  slug: solarwinds-service-desk-category-structure
- name: Solarwinds Service Desk Change Structure
  property_count: 8
  slug: solarwinds-service-desk-change-structure
- name: Solarwinds Service Desk Incident Create Structure
  property_count: 1
  slug: solarwinds-service-desk-incident-create-structure
- name: Solarwinds Service Desk Incident Structure
  property_count: 8
  slug: solarwinds-service-desk-incident-structure
- name: Solarwinds Service Desk Incident Update Structure
  property_count: 1
  slug: solarwinds-service-desk-incident-update-structure
- name: Solarwinds Service Desk Problem Structure
  property_count: 7
  slug: solarwinds-service-desk-problem-structure
- name: Solarwinds Service Desk Service Request Create Structure
  property_count: 1
  slug: solarwinds-service-desk-service-request-create-structure
- name: Solarwinds Service Desk Service Request Structure
  property_count: 7
  slug: solarwinds-service-desk-service-request-structure
- name: Solarwinds Service Desk User Ref Structure
  property_count: 3
  slug: solarwinds-service-desk-user-ref-structure
- name: Solarwinds Service Desk User Structure
  property_count: 5
  slug: solarwinds-service-desk-user-structure
- name: Solarwinds Structure
  property_count: 0
  slug: solarwinds-structure
jsonld:
- class_count: 0
  name: Solarwinds Context
  property_count: 5
  slug: solarwinds-context
- class_count: 0
  name: Solarwinds Loggly Context
  property_count: 0
  slug: solarwinds-loggly-context
- class_count: 0
  name: Solarwinds Orion Context
  property_count: 0
  slug: solarwinds-orion-context
- class_count: 0
  name: Solarwinds Papertrail Context
  property_count: 0
  slug: solarwinds-papertrail-context
- class_count: 0
  name: Solarwinds Pingdom Context
  property_count: 0
  slug: solarwinds-pingdom-context
- class_count: 0
  name: Solarwinds Service Desk Context
  property_count: 0
  slug: solarwinds-service-desk-context
layout: provider
modified: '2026-05-19'
name: SolarWinds
nav: Providers
network: true
overview: 'SolarWinds publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Account API, Assets API, BulkOperations API, and 21 more. Tagged areas include Application Monitoring, Database Monitoring, Infrastructure, IP Address Management, and IT Management.


  The SolarWinds catalog on APIs.io includes 6 JSON-LD contexts and 2 Spectral governance rulesets.


  SolarWinds'' developer surface includes authentication, developer portal, documentation, support, engineering blog, CLI, and 17 more developer resources.'
plans:
- name: Solarwinds Plans Pricing
  plan_count: 1
  slug: solarwinds-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Solarwinds Rate Limits
  slug: solarwinds-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SolarWinds API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: solarwinds-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: SolarWinds API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 7
  slug: solarwinds-spectral-rules
score:
  band: developing
  composite: 52.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 48.5
    catalog_earned_first_party: 0.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 13.6
    contract_quality: 66.8
    developer_ergonomics: 79.8
    discoverability: 66.7
    governance: 13.6
    operational_transparency: 28.9
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/solarwinds/refs/heads/main/screenshots/solarwinds-2026-06-20T194153.png
security:
- kind: authentication
  name: Solarwinds Authentication
  slug: solarwinds-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Solarwinds Domain Security
  slug: solarwinds-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: solarwinds
tags:
- Application Monitoring
- Database Monitoring
- Infrastructure
- IP Address Management
- IT Management
- ITSM
- Log Management
- Network Monitoring
- Observability
use_cases:
- Network Infrastructure Monitoring and Alerting
- IT Incident Management and Ticketing Workflows
- Cloud Application Performance Monitoring
- Centralized Log Management and Search
- Website and API Uptime Monitoring
- Database Query Performance Tuning
website: https://www.solarwinds.com
---
