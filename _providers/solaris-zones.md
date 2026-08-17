---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 106
  human_in_the_loop: 12
  name: Solaris Zones Agentic Access
  operation_count: 141
  slug: solaris-zones-agentic-access
  summary_line: 141 operations · 106 acting · 12 human-in-the-loop
api_count: 26
apis:
- description: Create Unified Archives from zones
  name: Solaris Zones Archive Creation API
  slug: solaris-zones-archive-creation-api
- description: Deploy zones from Unified Archives
  name: Solaris Zones Archive Deployment API
  slug: solaris-zones-archive-deployment-api
- description: Query archive contents and metadata
  name: Solaris Zones Archive Information API
  slug: solaris-zones-archive-information-api
- description: Zone configuration editing and commit operations
  name: Solaris Zones Configuration API
  slug: solaris-zones-configuration-api
- description: CPU utilization and allocation statistics
  name: Solaris Zones CPU Statistics API
  slug: solaris-zones-cpu-statistics-api
- description: Zone install and uninstall operations
  name: Solaris Zones Installation API
  slug: solaris-zones-installation-api
- description: Kernel statistics via kstat module
  name: Solaris Zones Kernel Statistics API
  slug: solaris-zones-kernel-statistics-api
- description: Configure kernel zone resources and properties
  name: Solaris Zones Kernel Zone Configuration API
  slug: solaris-zones-kernel-zone-configuration-api
- description: Kernel zone boot, halt, suspend, and resume operations
  name: Solaris Zones Kernel Zone Lifecycle API
  slug: solaris-zones-kernel-zone-lifecycle-api
- description: Create and manage kernel zones
  name: Solaris Zones Kernel Zone Management API
  slug: solaris-zones-kernel-zone-management-api
- description: Live migration of kernel zones between hosts
  name: Solaris Zones Kernel Zone Migration API
  slug: solaris-zones-kernel-zone-migration-api
- description: Zone lifecycle state transitions
  name: Solaris Zones Lifecycle API
  slug: solaris-zones-lifecycle-api
- description: Memory and swap utilization statistics
  name: Solaris Zones Memory Statistics API
  slug: solaris-zones-memory-statistics-api
- description: Zone attach, detach, move, and migration operations
  name: Solaris Zones Migration API
  slug: solaris-zones-migration-api
- description: Zone resource management (net, device, fs, rctl, etc.)
  name: Solaris Zones Resources API
  slug: solaris-zones-resources-api
- description: Zone state and property queries
  name: Solaris Zones State Query API
  slug: solaris-zones-state-query-api
- description: Discover available statistics and namespaces
  name: Solaris Zones Statistics Discovery API
  slug: solaris-zones-statistics-discovery-api
- description: Retrieve current and historical statistics data
  name: Solaris Zones Statistics Retrieval API
  slug: solaris-zones-statistics-retrieval-api
- description: System-wide performance statistics
  name: Solaris Zones System Statistics API
  slug: solaris-zones-system-statistics-api
- description: Read-only zone information and status queries
  name: Solaris Zones Zone Info API
  slug: solaris-zones-zone-info-api
- description: System-wide zone management operations including creation, deletion, and evacuation
  name: Solaris Zones Zone Manager API
  slug: solaris-zones-zone-manager-api
- description: Live and cold zone migration operations between Solaris hosts
  name: Solaris Zones Zone Migration API
  slug: solaris-zones-zone-migration-api
- description: Recover zones from archives
  name: Solaris Zones Zone Recovery API
  slug: solaris-zones-zone-recovery-api
- description: Zone state monitoring via zonemgr module
  name: Solaris Zones Zone State API
  slug: solaris-zones-zone-state-api
- description: Per-zone resource utilization statistics
  name: Solaris Zones Zone Statistics API
  slug: solaris-zones-zone-statistics-api
- description: Individual zone operations including configuration, lifecycle, and resource management
  name: Solaris Zones Zones API
  slug: solaris-zones-zones-api
artifact_total: 414
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones API
  slug: open-solaris-kernel-zones
- collection_type: open
  name: Solaris Zones Oracle Solaris RAD Zone Management REST API
  slug: open-solaris-rad-zonemgr
- collection_type: open
  name: Solaris Zones Oracle Solaris StatsStore and Analytics API
  slug: open-solaris-statsstore
- collection_type: open
  name: Solaris Zones Oracle Solaris Unified Archives Zones API
  slug: open-solaris-unified-archives
- collection_type: open
  name: Solaris Zones Solaris Zone Administration API
  slug: open-solaris-zone-administration
- collection_type: open
  name: Solaris Zones Solaris Zone Configuration API
  slug: open-solaris-zone-configuration
- collection_type: open
  name: Solaris Zones Solaris Zone Monitoring API
  slug: open-solaris-zone-monitoring
- collection_type: open
  name: Solaris Zones Monitoring Statistics API
  slug: open-solaris-zone-stats
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation API
  slug: open-solaris-zones-archive-creation-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Archive Deployment API
  slug: open-solaris-zones-archive-deployment-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Archive Information API
  slug: open-solaris-zones-archive-information-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Configuration API
  slug: open-solaris-zones-configuration-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation CPU Statistics API
  slug: open-solaris-zones-cpu-statistics-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Installation API
  slug: open-solaris-zones-installation-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Kernel Statistics API
  slug: open-solaris-zones-kernel-statistics-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Kernel Zone Configuration API
  slug: open-solaris-zones-kernel-zone-configuration-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Kernel Zone Lifecycle API
  slug: open-solaris-zones-kernel-zone-lifecycle-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Kernel Zone Management API
  slug: open-solaris-zones-kernel-zone-management-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Kernel Zone Migration API
  slug: open-solaris-zones-kernel-zone-migration-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Lifecycle API
  slug: open-solaris-zones-lifecycle-api
- collection_type: open
  name: Solaris Zones Management API
  slug: open-solaris-zones-management
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Memory Statistics API
  slug: open-solaris-zones-memory-statistics-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Migration API
  slug: open-solaris-zones-migration-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Resources API
  slug: open-solaris-zones-resources-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation State Query API
  slug: open-solaris-zones-state-query-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Statistics Discovery API
  slug: open-solaris-zones-statistics-discovery-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Statistics Retrieval API
  slug: open-solaris-zones-statistics-retrieval-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation System Statistics API
  slug: open-solaris-zones-system-statistics-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Zone Info API
  slug: open-solaris-zones-zone-info-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Zone Manager API
  slug: open-solaris-zones-zone-manager-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Zone Migration API
  slug: open-solaris-zones-zone-migration-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Zone Recovery API
  slug: open-solaris-zones-zone-recovery-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Zone State API
  slug: open-solaris-zones-zone-state-api
- collection_type: open
  name: Solaris Zones Oracle Solaris Kernel Zones Archive Creation Zone Statistics API
  slug: open-solaris-zones-zone-statistics-api
- collection_type: open
  name: Solaris Oracle Solaris Kernel Archive Creation Zones API
  slug: open-solaris-zones-zones-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/solaris-zones-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solaris-zones-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/solaris-zones-authentication.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.oracle.com/en/cloud/paas/api-platform/authentication.html
- group: operate
  title: ''
  type: Support
  url: https://www.oracle.com/support/
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/solaris/
- group: start
  title: ''
  type: Portal
  url: https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/index.html
- group: other
  title: Developer Resources
  type: Resources
  url: https://www.oracle.com/solaris/technologies/solarisdeveloper.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle/oraclesolaris-contrib
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/cd/E37838_01/html/E61038/gitsf.html
- group: docs
  title: Virtual Environments Overview
  type: Documentation
  url: https://docs.oracle.com/cd/E37838_01/html/E61037/zonesoverview.html
- group: docs
  title: Zones Configuration Resources
  type: Documentation
  url: https://docs.oracle.com/cd/E37838_01/html/E61040/
- group: docs
  title: RAD Client Guide
  type: Documentation
  url: https://docs.oracle.com/cd/E37838_01/html/E68270/gpzpd.html
- group: design
  title: ''
  type: JSONLD
  url: json-ld/solaris-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/solaris-zone-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/solaris-zone-resource-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/solaris-zone-stats-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/solaris-zone-migration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/solaris-zone-evacuation-schema.json
created: '2024'
description: API for managing Solaris Zones (containers) and virtualization on Oracle Solaris systems.
examples:
- key_count: 6
  name: Solaris Kernel Zones Kernel Zone Example
  slug: solaris-kernel-zones-kernel-zone-example
- key_count: 3
  name: Solaris Kernel Zones Kernel Zone Resource Example
  slug: solaris-kernel-zones-kernel-zone-resource-example
- key_count: 5
  name: Solaris Kernel Zones Property Example
  slug: solaris-kernel-zones-property-example
- key_count: 2
  name: Solaris Kernel Zones Rad Error Example
  slug: solaris-kernel-zones-rad-error-example
- key_count: 2
  name: Solaris Kernel Zones Zone Result Example
  slug: solaris-kernel-zones-zone-result-example
- key_count: 5
  name: Solaris Rad Zonemgr Evacuation Migration Result Example
  slug: solaris-rad-zonemgr-evacuation-migration-result-example
- key_count: 3
  name: Solaris Rad Zonemgr Evacuation Result Example
  slug: solaris-rad-zonemgr-evacuation-result-example
- key_count: 5
  name: Solaris Rad Zonemgr Property Example
  slug: solaris-rad-zonemgr-property-example
- key_count: 2
  name: Solaris Rad Zonemgr Rad Interface Example
  slug: solaris-rad-zonemgr-rad-interface-example
- key_count: 3
  name: Solaris Rad Zonemgr Resource Example
  slug: solaris-rad-zonemgr-resource-example
- key_count: 4
  name: Solaris Rad Zonemgr Result Example
  slug: solaris-rad-zonemgr-result-example
- key_count: 1
  name: Solaris Rad Zonemgr Result Response Example
  slug: solaris-rad-zonemgr-result-response-example
- key_count: 6
  name: Solaris Rad Zonemgr Zone Detail Example
  slug: solaris-rad-zonemgr-zone-detail-example
- key_count: 5
  name: Solaris Rad Zonemgr Zone Info Example
  slug: solaris-rad-zonemgr-zone-info-example
- key_count: 1
  name: Solaris Rad Zonemgr Zone Manager Detail Example
  slug: solaris-rad-zonemgr-zone-manager-detail-example
- key_count: 3
  name: Solaris Statsstore Historical Statistic Example
  slug: solaris-statsstore-historical-statistic-example
- key_count: 2
  name: Solaris Statsstore Rad Error Example
  slug: solaris-statsstore-rad-error-example
- key_count: 3
  name: Solaris Statsstore Statistic Identifier Example
  slug: solaris-statsstore-statistic-identifier-example
- key_count: 6
  name: Solaris Statsstore Statistic Metadata Example
  slug: solaris-statsstore-statistic-metadata-example
- key_count: 4
  name: Solaris Statsstore Statistic Value Example
  slug: solaris-statsstore-statistic-value-example
- key_count: 4
  name: Solaris Statsstore System Statistic Example
  slug: solaris-statsstore-system-statistic-example
- key_count: 6
  name: Solaris Statsstore Zone Statistic Example
  slug: solaris-statsstore-zone-statistic-example
- key_count: 5
  name: Solaris Unified Archives Property Example
  slug: solaris-unified-archives-property-example
- key_count: 2
  name: Solaris Unified Archives Rad Error Example
  slug: solaris-unified-archives-rad-error-example
- key_count: 3
  name: Solaris Unified Archives Resource Example
  slug: solaris-unified-archives-resource-example
- key_count: 6
  name: Solaris Unified Archives Zone Example
  slug: solaris-unified-archives-zone-example
- key_count: 2
  name: Solaris Unified Archives Zone Result Example
  slug: solaris-unified-archives-zone-result-example
- key_count: 2
  name: Solaris Zone Administration Rad Error Example
  slug: solaris-zone-administration-rad-error-example
- key_count: 2
  name: Solaris Zone Administration Zone Result Example
  slug: solaris-zone-administration-zone-result-example
- key_count: 5
  name: Solaris Zone Configuration Property Example
  slug: solaris-zone-configuration-property-example
- key_count: 2
  name: Solaris Zone Configuration Rad Error Example
  slug: solaris-zone-configuration-rad-error-example
- key_count: 3
  name: Solaris Zone Configuration Resource Example
  slug: solaris-zone-configuration-resource-example
- key_count: 2
  name: Solaris Zone Configuration Zone Result Example
  slug: solaris-zone-configuration-zone-result-example
- key_count: 9
  name: Solaris Zone Monitoring Cpu Info Example
  slug: solaris-zone-monitoring-cpu-info-example
- key_count: 6
  name: Solaris Zone Monitoring Kstat Data Example
  slug: solaris-zone-monitoring-kstat-data-example
- key_count: 5
  name: Solaris Zone Monitoring Kstat Interface Example
  slug: solaris-zone-monitoring-kstat-interface-example
- key_count: 2
  name: Solaris Zone Monitoring Rad Error Example
  slug: solaris-zone-monitoring-rad-error-example
- key_count: 5
  name: Solaris Zone Monitoring Vm Cpu Stats Example
  slug: solaris-zone-monitoring-vm-cpu-stats-example
- key_count: 8
  name: Solaris Zone Monitoring Zone Cap Stats Example
  slug: solaris-zone-monitoring-zone-cap-stats-example
- key_count: 6
  name: Solaris Zone Monitoring Zone Interface Example
  slug: solaris-zone-monitoring-zone-interface-example
- key_count: 7
  name: Solaris Zone Stats Cpu Cap Stats Example
  slug: solaris-zone-stats-cpu-cap-stats-example
- key_count: 9
  name: Solaris Zone Stats Cpu Info Example
  slug: solaris-zone-stats-cpu-info-example
- key_count: 6
  name: Solaris Zone Stats Memory Cap Stats Example
  slug: solaris-zone-stats-memory-cap-stats-example
- key_count: 2
  name: Solaris Zone Stats Rad Error Example
  slug: solaris-zone-stats-rad-error-example
- key_count: 3
  name: Solaris Zone Stats Swap Cap Stats Example
  slug: solaris-zone-stats-swap-cap-stats-example
- key_count: 7
  name: Solaris Zone Stats System Memory Stats Example
  slug: solaris-zone-stats-system-memory-stats-example
- key_count: 9
  name: Solaris Zone Stats Zone Cap Stats Example
  slug: solaris-zone-stats-zone-cap-stats-example
- key_count: 6
  name: Solaris Zone Stats Zone Misc Stats Example
  slug: solaris-zone-stats-zone-misc-stats-example
- key_count: 6
  name: Solaris Zones Addkernelzoneresource Example
  slug: solaris-zones-addkernelzoneresource-example
- key_count: 6
  name: Solaris Zones Addzoneresource Example
  slug: solaris-zones-addzoneresource-example
- key_count: 6
  name: Solaris Zones Applyzoneconfig Example
  slug: solaris-zones-applyzoneconfig-example
- key_count: 6
  name: Solaris Zones Attachzone Example
  slug: solaris-zones-attachzone-example
- key_count: 6
  name: Solaris Zones Attachzonefromarchive Example
  slug: solaris-zones-attachzonefromarchive-example
- key_count: 6
  name: Solaris Zones Bootkernelzone Example
  slug: solaris-zones-bootkernelzone-example
- key_count: 6
  name: Solaris Zones Bootzone Example
  slug: solaris-zones-bootzone-example
- key_count: 6
  name: Solaris Zones Cancelevacuate Example
  slug: solaris-zones-cancelevacuate-example
- key_count: 6
  name: Solaris Zones Cancelevacuation Example
  slug: solaris-zones-cancelevacuation-example
- key_count: 6
  name: Solaris Zones Cancelzoneconfig Example
  slug: solaris-zones-cancelzoneconfig-example
- key_count: 6
  name: Solaris Zones Checkconfigislive Example
  slug: solaris-zones-checkconfigislive-example
- key_count: 6
  name: Solaris Zones Checkconfigisstale Example
  slug: solaris-zones-checkconfigisstale-example
- key_count: 6
  name: Solaris Zones Clearzoneresourceproperties Example
  slug: solaris-zones-clearzoneresourceproperties-example
- key_count: 6
  name: Solaris Zones Clonezone Example
  slug: solaris-zones-clonezone-example
- key_count: 6
  name: Solaris Zones Clonezonefromarchive Example
  slug: solaris-zones-clonezonefromarchive-example
- key_count: 6
  name: Solaris Zones Commitkernelzoneconfig Example
  slug: solaris-zones-commitkernelzoneconfig-example
- key_count: 6
  name: Solaris Zones Commitzoneconfig Example
  slug: solaris-zones-commitzoneconfig-example
- key_count: 6
  name: Solaris Zones Createephemeralconfig Example
  slug: solaris-zones-createephemeralconfig-example
- key_count: 6
  name: Solaris Zones Createkernelzone Example
  slug: solaris-zones-createkernelzone-example
- key_count: 6
  name: Solaris Zones Createzone Example
  slug: solaris-zones-createzone-example
- key_count: 6
  name: Solaris Zones Createzonefromarchive Example
  slug: solaris-zones-createzonefromarchive-example
- key_count: 6
  name: Solaris Zones Deletezone Example
  slug: solaris-zones-deletezone-example
- key_count: 6
  name: Solaris Zones Describestatistic Example
  slug: solaris-zones-describestatistic-example
- key_count: 6
  name: Solaris Zones Detachzone Example
  slug: solaris-zones-detachzone-example
- key_count: 6
  name: Solaris Zones Detachzoneforarchive Example
  slug: solaris-zones-detachzoneforarchive-example
- key_count: 6
  name: Solaris Zones Editkernelzoneconfig Example
  slug: solaris-zones-editkernelzoneconfig-example
- key_count: 6
  name: Solaris Zones Editzoneconfig Example
  slug: solaris-zones-editzoneconfig-example
- key_count: 6
  name: Solaris Zones Evacuate Example
  slug: solaris-zones-evacuate-example
- key_count: 6
  name: Solaris Zones Evacuatezones Example
  slug: solaris-zones-evacuatezones-example
- key_count: 6
  name: Solaris Zones Exportzoneconfig Example
  slug: solaris-zones-exportzoneconfig-example
- key_count: 6
  name: Solaris Zones Exportzoneconfigforarchive Example
  slug: solaris-zones-exportzoneconfigforarchive-example
- key_count: 6
  name: Solaris Zones Getarchivezoneresources Example
  slug: solaris-zones-getarchivezoneresources-example
- key_count: 6
  name: Solaris Zones Getcpuinfo Example
  slug: solaris-zones-getcpuinfo-example
- key_count: 6
  name: Solaris Zones Getkernelzone Example
  slug: solaris-zones-getkernelzone-example
- key_count: 6
  name: Solaris Zones Getkernelzoneresources Example
  slug: solaris-zones-getkernelzoneresources-example
- key_count: 6
  name: Solaris Zones Getkstat Example
  slug: solaris-zones-getkstat-example
- key_count: 6
  name: Solaris Zones Getsystemmemorypages Example
  slug: solaris-zones-getsystemmemorypages-example
- key_count: 6
  name: Solaris Zones Getvmcpustats Example
  slug: solaris-zones-getvmcpustats-example
- key_count: 6
  name: Solaris Zones Getzone Example
  slug: solaris-zones-getzone-example
- key_count: 6
  name: Solaris Zones Getzoneauxstate Example
  slug: solaris-zones-getzoneauxstate-example
- key_count: 6
  name: Solaris Zones Getzonebrand Example
  slug: solaris-zones-getzonebrand-example
- key_count: 6
  name: Solaris Zones Getzonecapstatistics Example
  slug: solaris-zones-getzonecapstatistics-example
- key_count: 6
  name: Solaris Zones Getzonecapstats Example
  slug: solaris-zones-getzonecapstats-example
- key_count: 6
  name: Solaris Zones Getzonecpucap Example
  slug: solaris-zones-getzonecpucap-example
- key_count: 6
  name: Solaris Zones Getzoneforarchive Example
  slug: solaris-zones-getzoneforarchive-example
- key_count: 6
  name: Solaris Zones Getzoneid Example
  slug: solaris-zones-getzoneid-example
- key_count: 6
  name: Solaris Zones Getzoneinfo Example
  slug: solaris-zones-getzoneinfo-example
- key_count: 6
  name: Solaris Zones Getzonemanager Example
  slug: solaris-zones-getzonemanager-example
- key_count: 6
  name: Solaris Zones Getzonemiscstatistics Example
  slug: solaris-zones-getzonemiscstatistics-example
- key_count: 6
  name: Solaris Zones Getzonename Example
  slug: solaris-zones-getzonename-example
- key_count: 6
  name: Solaris Zones Getzonephysicalmemorycap Example
  slug: solaris-zones-getzonephysicalmemorycap-example
- key_count: 6
  name: Solaris Zones Getzoneresourceproperties Example
  slug: solaris-zones-getzoneresourceproperties-example
- key_count: 6
  name: Solaris Zones Getzoneresources Example
  slug: solaris-zones-getzoneresources-example
- key_count: 6
  name: Solaris Zones Getzonestate Example
  slug: solaris-zones-getzonestate-example
- key_count: 6
  name: Solaris Zones Getzoneswapcap Example
  slug: solaris-zones-getzoneswapcap-example
- key_count: 6
  name: Solaris Zones Getzoneuuid Example
  slug: solaris-zones-getzoneuuid-example
- key_count: 6
  name: Solaris Zones Haltkernelzone Example
  slug: solaris-zones-haltkernelzone-example
- key_count: 6
  name: Solaris Zones Haltzone Example
  slug: solaris-zones-haltzone-example
- key_count: 6
  name: Solaris Zones Importzoneconfig Example
  slug: solaris-zones-importzoneconfig-example
- key_count: 6
  name: Solaris Zones Initevacuate Example
  slug: solaris-zones-initevacuate-example
- key_count: 6
  name: Solaris Zones Initializeevacuation Example
  slug: solaris-zones-initializeevacuation-example
- key_count: 6
  name: Solaris Zones Installkernelzone Example
  slug: solaris-zones-installkernelzone-example
- key_count: 6
  name: Solaris Zones Installzone Example
  slug: solaris-zones-installzone-example
- key_count: 6
  name: Solaris Zones Installzonefromarchive Example
  slug: solaris-zones-installzonefromarchive-example
- key_count: 6
  name: Solaris Zones Listallzones Example
  slug: solaris-zones-listallzones-example
- key_count: 6
  name: Solaris Zones Listkstatinterfaces Example
  slug: solaris-zones-listkstatinterfaces-example
- key_count: 6
  name: Solaris Zones Listsstoreinterfaces Example
  slug: solaris-zones-listsstoreinterfaces-example
- key_count: 6
  name: Solaris Zones Liststatistics Example
  slug: solaris-zones-liststatistics-example
- key_count: 6
  name: Solaris Zones Listzoneinfo Example
  slug: solaris-zones-listzoneinfo-example
- key_count: 6
  name: Solaris Zones Listzoneinterfaces Example
  slug: solaris-zones-listzoneinterfaces-example
- key_count: 6
  name: Solaris Zones Livelymigratekernelzone Example
  slug: solaris-zones-livelymigratekernelzone-example
- key_count: 3
  name: Solaris Zones Management Create Zone Request Example
  slug: solaris-zones-management-create-zone-request-example
- key_count: 4
  name: Solaris Zones Management Evacuation Migration Result Example
  slug: solaris-zones-management-evacuation-migration-result-example
- key_count: 3
  name: Solaris Zones Management Evacuation Result Example
  slug: solaris-zones-management-evacuation-result-example
- key_count: 3
  name: Solaris Zones Management Migrate Zone Request Example
  slug: solaris-zones-management-migrate-zone-request-example
- key_count: 3
  name: Solaris Zones Management Migration Error Example
  slug: solaris-zones-management-migration-error-example
- key_count: 2
  name: Solaris Zones Management Rad Error Example
  slug: solaris-zones-management-rad-error-example
- key_count: 2
  name: Solaris Zones Management Rad Interface Example
  slug: solaris-zones-management-rad-interface-example
- key_count: 2
  name: Solaris Zones Management Rad Result Example
  slug: solaris-zones-management-rad-result-example
- key_count: 6
  name: Solaris Zones Management Zone Example
  slug: solaris-zones-management-zone-example
- key_count: 5
  name: Solaris Zones Management Zone Info Example
  slug: solaris-zones-management-zone-info-example
- key_count: 0
  name: Solaris Zones Management Zone Manager Example
  slug: solaris-zones-management-zone-manager-example
- key_count: 2
  name: Solaris Zones Management Zone Result Example
  slug: solaris-zones-management-zone-result-example
- key_count: 6
  name: Solaris Zones Markzone Example
  slug: solaris-zones-markzone-example
- key_count: 6
  name: Solaris Zones Migratezone Example
  slug: solaris-zones-migratezone-example
- key_count: 6
  name: Solaris Zones Movezone Example
  slug: solaris-zones-movezone-example
- key_count: 6
  name: Solaris Zones Readhistoricalstatistics Example
  slug: solaris-zones-readhistoricalstatistics-example
- key_count: 6
  name: Solaris Zones Readstatistics Example
  slug: solaris-zones-readstatistics-example
- key_count: 6
  name: Solaris Zones Readsystemstatistics Example
  slug: solaris-zones-readsystemstatistics-example
- key_count: 6
  name: Solaris Zones Readyzone Example
  slug: solaris-zones-readyzone-example
- key_count: 6
  name: Solaris Zones Readzonestatistics Example
  slug: solaris-zones-readzonestatistics-example
- key_count: 6
  name: Solaris Zones Rebootkernelzone Example
  slug: solaris-zones-rebootkernelzone-example
- key_count: 6
  name: Solaris Zones Rebootzone Example
  slug: solaris-zones-rebootzone-example
- key_count: 6
  name: Solaris Zones Reloadzoneconfig Example
  slug: solaris-zones-reloadzoneconfig-example
- key_count: 6
  name: Solaris Zones Removezoneresources Example
  slug: solaris-zones-removezoneresources-example
- key_count: 6
  name: Solaris Zones Renamezone Example
  slug: solaris-zones-renamezone-example
- key_count: 6
  name: Solaris Zones Savecorezone Example
  slug: solaris-zones-savecorezone-example
- key_count: 6
  name: Solaris Zones Setzoneresourceproperties Example
  slug: solaris-zones-setzoneresourceproperties-example
- key_count: 6
  name: Solaris Zones Shutdownkernelzone Example
  slug: solaris-zones-shutdownkernelzone-example
- key_count: 6
  name: Solaris Zones Shutdownzone Example
  slug: solaris-zones-shutdownzone-example
- key_count: 6
  name: Solaris Zones Suspendkernelzone Example
  slug: solaris-zones-suspendkernelzone-example
- key_count: 6
  name: Solaris Zones Suspendzone Example
  slug: solaris-zones-suspendzone-example
- key_count: 6
  name: Solaris Zones Uninstallzone Example
  slug: solaris-zones-uninstallzone-example
- key_count: 6
  name: Solaris Zones Updatezoneconfig Example
  slug: solaris-zones-updatezoneconfig-example
- key_count: 6
  name: Solaris Zones Verifyzone Example
  slug: solaris-zones-verifyzone-example
features:
- description: Hardware-enforced isolation between zones providing secure multi-tenant environments on a single physical system.
  name: Zone Isolation
- description: Move running zones between physical systems without downtime using live migration capabilities.
  name: Live Migration
- description: Non-global zones with their own independent kernel for enhanced security isolation and OS independence.
  name: Kernel Zones
- description: Create portable system archives for zone cloning, recovery, and migration across Solaris systems.
  name: Unified Archives
- description: Consolidated resource statistics and historical analytics for monitoring zone performance and capacity planning.
  name: StatsStore Analytics
- description: RESTful remote administration daemon enabling programmatic zone management over HTTP/JSON.
  name: RAD Remote Administration
- description: Fine-grained CPU, memory, and swap resource controls with configurable caps per zone.
  name: Resource Capping
finops:
- name: Solaris Zones Finops
  service_category: Operating System Virtualization
  slug: solaris-zones-finops
image: https://www.oracle.com/a/ocom/img/cb71-solaris.jpg
integrations:
- description: Manage Solaris Zones through Oracle Enterprise Manager for centralized infrastructure monitoring and control.
  name: Oracle Enterprise Manager
- description: Automate zone provisioning and configuration management using Ansible playbooks with Oracle Solaris modules.
  name: Ansible
- description: Configure and manage Solaris Zones infrastructure as code using Puppet modules for Oracle Solaris.
  name: Puppet
json_schemas:
- name: KernelZoneResource
  property_count: 3
  slug: solaris-kernel-zones-kernel-zone-resource
- name: KernelZone
  property_count: 6
  slug: solaris-kernel-zones-kernel-zone
- name: Property
  property_count: 5
  slug: solaris-kernel-zones-property
- name: RadError
  property_count: 2
  slug: solaris-kernel-zones-rad-error
- name: ZoneResult
  property_count: 2
  slug: solaris-kernel-zones-zone-result
- name: EvacuationMigrationResult
  property_count: 5
  slug: solaris-rad-zonemgr-evacuation-migration-result
- name: EvacuationResult
  property_count: 3
  slug: solaris-rad-zonemgr-evacuation-result
- name: Property
  property_count: 5
  slug: solaris-rad-zonemgr-property
- name: RadInterface
  property_count: 2
  slug: solaris-rad-zonemgr-rad-interface
- name: Resource
  property_count: 3
  slug: solaris-rad-zonemgr-resource
- name: ResultResponse
  property_count: 1
  slug: solaris-rad-zonemgr-result-response
- name: Result
  property_count: 4
  slug: solaris-rad-zonemgr-result
- name: ZoneDetail
  property_count: 6
  slug: solaris-rad-zonemgr-zone-detail
- name: ZoneInfo
  property_count: 5
  slug: solaris-rad-zonemgr-zone-info
- name: ZoneManagerDetail
  property_count: 1
  slug: solaris-rad-zonemgr-zone-manager-detail
- name: HistoricalStatistic
  property_count: 3
  slug: solaris-statsstore-historical-statistic
- name: RadError
  property_count: 2
  slug: solaris-statsstore-rad-error
- name: StatisticIdentifier
  property_count: 3
  slug: solaris-statsstore-statistic-identifier
- name: StatisticMetadata
  property_count: 6
  slug: solaris-statsstore-statistic-metadata
- name: StatisticValue
  property_count: 4
  slug: solaris-statsstore-statistic-value
- name: SystemStatistic
  property_count: 4
  slug: solaris-statsstore-system-statistic
- name: ZoneStatistic
  property_count: 6
  slug: solaris-statsstore-zone-statistic
- name: Property
  property_count: 5
  slug: solaris-unified-archives-property
- name: RadError
  property_count: 2
  slug: solaris-unified-archives-rad-error
- name: Resource
  property_count: 3
  slug: solaris-unified-archives-resource
- name: ZoneResult
  property_count: 2
  slug: solaris-unified-archives-zone-result
- name: Zone
  property_count: 6
  slug: solaris-unified-archives-zone
- name: RadError
  property_count: 2
  slug: solaris-zone-administration-rad-error
- name: ZoneResult
  property_count: 2
  slug: solaris-zone-administration-zone-result
- name: Property
  property_count: 5
  slug: solaris-zone-configuration-property
- name: RadError
  property_count: 2
  slug: solaris-zone-configuration-rad-error
- name: Resource
  property_count: 3
  slug: solaris-zone-configuration-resource
- name: Oracle Solaris Zone Configuration
  property_count: 36
  slug: solaris-zone-configuration
- name: ZoneResult
  property_count: 2
  slug: solaris-zone-configuration-zone-result
- name: Oracle Solaris Zone Evacuation
  property_count: 4
  slug: solaris-zone-evacuation
- name: Oracle Solaris Zone Migration
  property_count: 8
  slug: solaris-zone-migration
- name: CpuInfo
  property_count: 9
  slug: solaris-zone-monitoring-cpu-info
- name: KstatData
  property_count: 6
  slug: solaris-zone-monitoring-kstat-data
- name: KstatInterface
  property_count: 5
  slug: solaris-zone-monitoring-kstat-interface
- name: RadError
  property_count: 2
  slug: solaris-zone-monitoring-rad-error
- name: VmCpuStats
  property_count: 5
  slug: solaris-zone-monitoring-vm-cpu-stats
- name: ZoneCapStats
  property_count: 8
  slug: solaris-zone-monitoring-zone-cap-stats
- name: ZoneInterface
  property_count: 6
  slug: solaris-zone-monitoring-zone-interface
- name: Oracle Solaris Zone Resource
  property_count: 3
  slug: solaris-zone-resource
- name: Oracle Solaris Zone
  property_count: 6
  slug: solaris-zone
- name: Oracle Solaris Zone State
  property_count: 11
  slug: solaris-zone-state
- name: CpuCapStats
  property_count: 7
  slug: solaris-zone-stats-cpu-cap-stats
- name: CpuInfo
  property_count: 9
  slug: solaris-zone-stats-cpu-info
- name: MemoryCapStats
  property_count: 6
  slug: solaris-zone-stats-memory-cap-stats
- name: RadError
  property_count: 2
  slug: solaris-zone-stats-rad-error
- name: Oracle Solaris Zone Statistics
  property_count: 13
  slug: solaris-zone-stats
- name: SwapCapStats
  property_count: 3
  slug: solaris-zone-stats-swap-cap-stats
- name: SystemMemoryStats
  property_count: 7
  slug: solaris-zone-stats-system-memory-stats
- name: ZoneCapStats
  property_count: 9
  slug: solaris-zone-stats-zone-cap-stats
- name: ZoneMiscStats
  property_count: 6
  slug: solaris-zone-stats-zone-misc-stats
- name: CpuCapStats
  property_count: 7
  slug: solaris-zones-cpucapstats
- name: CpuInfo
  property_count: 9
  slug: solaris-zones-cpuinfo
- name: CreateZoneRequest
  property_count: 3
  slug: solaris-zones-createzonerequest
- name: EvacuationMigrationResult
  property_count: 5
  slug: solaris-zones-evacuationmigrationresult
- name: EvacuationResult
  property_count: 3
  slug: solaris-zones-evacuationresult
- name: HistoricalStatistic
  property_count: 3
  slug: solaris-zones-historicalstatistic
- name: KernelZone
  property_count: 6
  slug: solaris-zones-kernelzone
- name: KernelZoneResource
  property_count: 3
  slug: solaris-zones-kernelzoneresource
- name: KstatData
  property_count: 6
  slug: solaris-zones-kstatdata
- name: KstatInterface
  property_count: 5
  slug: solaris-zones-kstatinterface
- name: CreateZoneRequest
  property_count: 3
  slug: solaris-zones-management-create-zone-request
- name: EvacuationMigrationResult
  property_count: 4
  slug: solaris-zones-management-evacuation-migration-result
- name: EvacuationResult
  property_count: 3
  slug: solaris-zones-management-evacuation-result
- name: MigrateZoneRequest
  property_count: 3
  slug: solaris-zones-management-migrate-zone-request
- name: MigrationError
  property_count: 3
  slug: solaris-zones-management-migration-error
- name: RadError
  property_count: 2
  slug: solaris-zones-management-rad-error
- name: RadInterface
  property_count: 2
  slug: solaris-zones-management-rad-interface
- name: RadResult
  property_count: 2
  slug: solaris-zones-management-rad-result
- name: ZoneInfo
  property_count: 5
  slug: solaris-zones-management-zone-info
- name: ZoneManager
  property_count: 0
  slug: solaris-zones-management-zone-manager
- name: ZoneResult
  property_count: 2
  slug: solaris-zones-management-zone-result
- name: Zone
  property_count: 6
  slug: solaris-zones-management-zone
- name: MemoryCapStats
  property_count: 6
  slug: solaris-zones-memorycapstats
- name: MigrateZoneRequest
  property_count: 3
  slug: solaris-zones-migratezonerequest
- name: MigrationError
  property_count: 3
  slug: solaris-zones-migrationerror
- name: Property
  property_count: 5
  slug: solaris-zones-property
- name: RadError
  property_count: 2
  slug: solaris-zones-raderror
- name: RadInterface
  property_count: 2
  slug: solaris-zones-radinterface
- name: RadResult
  property_count: 2
  slug: solaris-zones-radresult
- name: Resource
  property_count: 3
  slug: solaris-zones-resource
- name: Result
  property_count: 4
  slug: solaris-zones-result
- name: ResultResponse
  property_count: 2
  slug: solaris-zones-resultresponse
- name: StatisticIdentifier
  property_count: 3
  slug: solaris-zones-statisticidentifier
- name: StatisticMetadata
  property_count: 6
  slug: solaris-zones-statisticmetadata
- name: StatisticValue
  property_count: 4
  slug: solaris-zones-statisticvalue
- name: SwapCapStats
  property_count: 3
  slug: solaris-zones-swapcapstats
- name: SystemMemoryStats
  property_count: 7
  slug: solaris-zones-systemmemorystats
- name: SystemStatistic
  property_count: 4
  slug: solaris-zones-systemstatistic
- name: VmCpuStats
  property_count: 5
  slug: solaris-zones-vmcpustats
- name: Zone
  property_count: 6
  slug: solaris-zones-zone
- name: ZoneCapStats
  property_count: 8
  slug: solaris-zones-zonecapstats
- name: ZoneDetail
  property_count: 6
  slug: solaris-zones-zonedetail
- name: ZoneInfo
  property_count: 5
  slug: solaris-zones-zoneinfo
- name: ZoneInterface
  property_count: 6
  slug: solaris-zones-zoneinterface
- name: ZoneManager
  property_count: 1
  slug: solaris-zones-zonemanager
- name: ZoneManagerDetail
  property_count: 1
  slug: solaris-zones-zonemanagerdetail
- name: ZoneMiscStats
  property_count: 6
  slug: solaris-zones-zonemiscstats
- name: ZoneResult
  property_count: 2
  slug: solaris-zones-zoneresult
- name: ZoneStatistic
  property_count: 6
  slug: solaris-zones-zonestatistic
json_structures:
- name: Solaris Kernel Zones Kernel Zone Resource Structure
  property_count: 3
  slug: solaris-kernel-zones-kernel-zone-resource-structure
- name: Solaris Kernel Zones Kernel Zone Structure
  property_count: 6
  slug: solaris-kernel-zones-kernel-zone-structure
- name: Solaris Kernel Zones Property Structure
  property_count: 5
  slug: solaris-kernel-zones-property-structure
- name: Solaris Kernel Zones Rad Error Structure
  property_count: 2
  slug: solaris-kernel-zones-rad-error-structure
- name: Solaris Kernel Zones Zone Result Structure
  property_count: 2
  slug: solaris-kernel-zones-zone-result-structure
- name: Solaris Rad Zonemgr Evacuation Migration Result Structure
  property_count: 5
  slug: solaris-rad-zonemgr-evacuation-migration-result-structure
- name: Solaris Rad Zonemgr Evacuation Result Structure
  property_count: 3
  slug: solaris-rad-zonemgr-evacuation-result-structure
- name: Solaris Rad Zonemgr Property Structure
  property_count: 5
  slug: solaris-rad-zonemgr-property-structure
- name: Solaris Rad Zonemgr Rad Interface Structure
  property_count: 2
  slug: solaris-rad-zonemgr-rad-interface-structure
- name: Solaris Rad Zonemgr Resource Structure
  property_count: 3
  slug: solaris-rad-zonemgr-resource-structure
- name: Solaris Rad Zonemgr Result Response Structure
  property_count: 1
  slug: solaris-rad-zonemgr-result-response-structure
- name: Solaris Rad Zonemgr Result Structure
  property_count: 4
  slug: solaris-rad-zonemgr-result-structure
- name: Solaris Rad Zonemgr Zone Detail Structure
  property_count: 6
  slug: solaris-rad-zonemgr-zone-detail-structure
- name: Solaris Rad Zonemgr Zone Info Structure
  property_count: 5
  slug: solaris-rad-zonemgr-zone-info-structure
- name: Solaris Rad Zonemgr Zone Manager Detail Structure
  property_count: 1
  slug: solaris-rad-zonemgr-zone-manager-detail-structure
- name: Solaris Statsstore Historical Statistic Structure
  property_count: 3
  slug: solaris-statsstore-historical-statistic-structure
- name: Solaris Statsstore Rad Error Structure
  property_count: 2
  slug: solaris-statsstore-rad-error-structure
- name: Solaris Statsstore Statistic Identifier Structure
  property_count: 3
  slug: solaris-statsstore-statistic-identifier-structure
- name: Solaris Statsstore Statistic Metadata Structure
  property_count: 6
  slug: solaris-statsstore-statistic-metadata-structure
- name: Solaris Statsstore Statistic Value Structure
  property_count: 4
  slug: solaris-statsstore-statistic-value-structure
- name: Solaris Statsstore System Statistic Structure
  property_count: 4
  slug: solaris-statsstore-system-statistic-structure
- name: Solaris Statsstore Zone Statistic Structure
  property_count: 6
  slug: solaris-statsstore-zone-statistic-structure
- name: Solaris Unified Archives Property Structure
  property_count: 5
  slug: solaris-unified-archives-property-structure
- name: Solaris Unified Archives Rad Error Structure
  property_count: 2
  slug: solaris-unified-archives-rad-error-structure
- name: Solaris Unified Archives Resource Structure
  property_count: 3
  slug: solaris-unified-archives-resource-structure
- name: Solaris Unified Archives Zone Result Structure
  property_count: 2
  slug: solaris-unified-archives-zone-result-structure
- name: Solaris Unified Archives Zone Structure
  property_count: 6
  slug: solaris-unified-archives-zone-structure
- name: Solaris Zone Administration Rad Error Structure
  property_count: 2
  slug: solaris-zone-administration-rad-error-structure
- name: Solaris Zone Administration Zone Result Structure
  property_count: 2
  slug: solaris-zone-administration-zone-result-structure
- name: Solaris Zone Configuration Property Structure
  property_count: 5
  slug: solaris-zone-configuration-property-structure
- name: Solaris Zone Configuration Rad Error Structure
  property_count: 2
  slug: solaris-zone-configuration-rad-error-structure
- name: Solaris Zone Configuration Resource Structure
  property_count: 3
  slug: solaris-zone-configuration-resource-structure
- name: Solaris Zone Configuration Zone Result Structure
  property_count: 2
  slug: solaris-zone-configuration-zone-result-structure
- name: Solaris Zone Monitoring Cpu Info Structure
  property_count: 9
  slug: solaris-zone-monitoring-cpu-info-structure
- name: Solaris Zone Monitoring Kstat Data Structure
  property_count: 6
  slug: solaris-zone-monitoring-kstat-data-structure
- name: Solaris Zone Monitoring Kstat Interface Structure
  property_count: 5
  slug: solaris-zone-monitoring-kstat-interface-structure
- name: Solaris Zone Monitoring Rad Error Structure
  property_count: 2
  slug: solaris-zone-monitoring-rad-error-structure
- name: Solaris Zone Monitoring Vm Cpu Stats Structure
  property_count: 5
  slug: solaris-zone-monitoring-vm-cpu-stats-structure
- name: Solaris Zone Monitoring Zone Cap Stats Structure
  property_count: 8
  slug: solaris-zone-monitoring-zone-cap-stats-structure
- name: Solaris Zone Monitoring Zone Interface Structure
  property_count: 6
  slug: solaris-zone-monitoring-zone-interface-structure
- name: Solaris Zone Stats Cpu Cap Stats Structure
  property_count: 7
  slug: solaris-zone-stats-cpu-cap-stats-structure
- name: Solaris Zone Stats Cpu Info Structure
  property_count: 9
  slug: solaris-zone-stats-cpu-info-structure
- name: Solaris Zone Stats Memory Cap Stats Structure
  property_count: 6
  slug: solaris-zone-stats-memory-cap-stats-structure
- name: Solaris Zone Stats Rad Error Structure
  property_count: 2
  slug: solaris-zone-stats-rad-error-structure
- name: Solaris Zone Stats Swap Cap Stats Structure
  property_count: 3
  slug: solaris-zone-stats-swap-cap-stats-structure
- name: Solaris Zone Stats System Memory Stats Structure
  property_count: 7
  slug: solaris-zone-stats-system-memory-stats-structure
- name: Solaris Zone Stats Zone Cap Stats Structure
  property_count: 9
  slug: solaris-zone-stats-zone-cap-stats-structure
- name: Solaris Zone Stats Zone Misc Stats Structure
  property_count: 6
  slug: solaris-zone-stats-zone-misc-stats-structure
- name: Solaris Zones Management Create Zone Request Structure
  property_count: 3
  slug: solaris-zones-management-create-zone-request-structure
- name: Solaris Zones Management Evacuation Migration Result Structure
  property_count: 4
  slug: solaris-zones-management-evacuation-migration-result-structure
- name: Solaris Zones Management Evacuation Result Structure
  property_count: 3
  slug: solaris-zones-management-evacuation-result-structure
- name: Solaris Zones Management Migrate Zone Request Structure
  property_count: 3
  slug: solaris-zones-management-migrate-zone-request-structure
- name: Solaris Zones Management Migration Error Structure
  property_count: 3
  slug: solaris-zones-management-migration-error-structure
- name: Solaris Zones Management Rad Error Structure
  property_count: 2
  slug: solaris-zones-management-rad-error-structure
- name: Solaris Zones Management Rad Interface Structure
  property_count: 2
  slug: solaris-zones-management-rad-interface-structure
- name: Solaris Zones Management Rad Result Structure
  property_count: 2
  slug: solaris-zones-management-rad-result-structure
- name: Solaris Zones Management Zone Info Structure
  property_count: 5
  slug: solaris-zones-management-zone-info-structure
- name: Solaris Zones Management Zone Manager Structure
  property_count: 0
  slug: solaris-zones-management-zone-manager-structure
- name: Solaris Zones Management Zone Result Structure
  property_count: 2
  slug: solaris-zones-management-zone-result-structure
- name: Solaris Zones Management Zone Structure
  property_count: 6
  slug: solaris-zones-management-zone-structure
- name: Solaris Zones Structure
  property_count: 0
  slug: solaris-zones-structure
jsonld:
- class_count: 0
  name: Solaris Context
  property_count: 12
  slug: solaris-context
- class_count: 0
  name: Solaris Kernel Zones Context
  property_count: 0
  slug: solaris-kernel-zones-context
- class_count: 0
  name: Solaris Rad Zonemgr Context
  property_count: 0
  slug: solaris-rad-zonemgr-context
- class_count: 0
  name: Solaris Statsstore Context
  property_count: 0
  slug: solaris-statsstore-context
- class_count: 0
  name: Solaris Unified Archives Context
  property_count: 0
  slug: solaris-unified-archives-context
- class_count: 0
  name: Solaris Zone Administration Context
  property_count: 0
  slug: solaris-zone-administration-context
- class_count: 0
  name: Solaris Zone Configuration Context
  property_count: 0
  slug: solaris-zone-configuration-context
- class_count: 0
  name: Solaris Zone Monitoring Context
  property_count: 0
  slug: solaris-zone-monitoring-context
- class_count: 0
  name: Solaris Zone Stats Context
  property_count: 0
  slug: solaris-zone-stats-context
- class_count: 0
  name: Solaris Zones Context
  property_count: 15
  slug: solaris-zones-context
- class_count: 0
  name: Solaris Zones Management Context
  property_count: 0
  slug: solaris-zones-management-context
layout: provider
modified: '2026-05-19'
name: Solaris Zones
nav: Providers
network: true
overview: 'Solaris Zones publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Archive Creation API, Archive Deployment API, Archive Information API, and 23 more. Tagged areas include Containers, Kernel Zones, Operating Systems, Oracle, and RAD.


  The Solaris Zones catalog on APIs.io includes 11 JSON-LD contexts and 2 Spectral governance rulesets.


  Solaris Zones'' developer surface includes authentication, support, engineering blog, developer portal, getting-started guide, documentation, and 15 more developer resources.'
plans:
- name: Solaris Zones Plans Pricing
  plan_count: 1
  slug: solaris-zones-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 1
  name: Solaris Zones Rate Limits
  slug: solaris-zones-rate-limits
rules:
- name: Solaris Zones API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: solaris-zones-jsonschema-spectral-rules
- name: Solaris Zones API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 7
  slug: solaris-zones-spectral-rules
score:
  band: developing
  composite: 47.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 67.3
    developer_ergonomics: 45.7
    discoverability: 66.7
    governance: 58.3
    operational_transparency: 10.5
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 26
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/solaris-zones/refs/heads/main/screenshots/solaris-zones-2026-06-20T194146.png
security:
- kind: authentication
  name: Solaris Zones Authentication
  slug: solaris-zones-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Solaris Zones Domain Security
  slug: solaris-zones-domain-security
  summary_line: TLSv1.3 · DMARC
slug: solaris-zones
tags:
- Containers
- Kernel Zones
- Operating Systems
- Oracle
- RAD
- Resource Management
- Solaris
- StatsStore
- Virtualization
- Zones
use_cases:
- description: Consolidate multiple workloads onto a single physical system using zones for resource isolation and management.
  name: Server Consolidation
- description: Create isolated development and testing environments that mirror production without dedicated hardware.
  name: Development and Testing
- description: Use Unified Archives and zone migration to implement disaster recovery workflows across Solaris systems.
  name: Disaster Recovery
- description: Monitor zone resource utilization and system performance using StatsStore and zonestat APIs.
  name: Performance Monitoring
- description: Programmatically create, configure, and deploy zones using RAD REST APIs for automated infrastructure provisioning.
  name: Automated Provisioning
website: https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/index.html
---
