---
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
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 131
  human_in_the_loop: 9
  name: Leaseweb Agentic Access
  operation_count: 254
  slug: leaseweb-agentic-access
  summary_line: 254 operations · 131 acting · 9 human-in-the-loop
api_count: 20
apis:
- baseURL: https://api.leaseweb.com/publicCloud/v1
  baseurl_source: declared
  description: The abuse API from Leaseweb — 7 operation(s) for abuse.
  name: Leaseweb Abuse API
  slug: leaseweb-abuse-api
- baseURL: https://api.leaseweb.com/publicCloud/v1
  baseurl_source: declared
  description: The aggregationpack API from Leaseweb — 2 operation(s) for aggregationpack.
  name: Leaseweb Aggregationpack API
  slug: leaseweb-aggregationpack-api
- baseURL: https://api.leaseweb.com/publicCloud/v1
  baseurl_source: declared
  description: The dedicatedserver API from Leaseweb — 46 operation(s) for dedicatedserver.
  name: Leaseweb Dedicatedserver API
  slug: leaseweb-dedicatedserver-api
- baseURL: https://api.leaseweb.com/publicCloud/v1
  baseurl_source: declared
  description: The dns API from Leaseweb — 8 operation(s) for dns.
  name: Leaseweb Dns API
  slug: leaseweb-dns-api
- baseURL: https://api.leaseweb.com/publicCloud/v1
  baseurl_source: declared
  description: The invoice API from Leaseweb — 5 operation(s) for invoice.
  name: Leaseweb Invoice API
  slug: leaseweb-invoice-api
- baseURL: https://api.leaseweb.com/publicCloud/v1
  baseurl_source: declared
  description: The ipmgmt API from Leaseweb — 7 operation(s) for ipmgmt.
  name: Leaseweb Ipmgmt API
  slug: leaseweb-ipmgmt-api
- baseURL: https://api.leaseweb.com/publicCloud/v1
  baseurl_source: declared
  description: The networkequipment API from Leaseweb — 14 operation(s) for networkequipment.
  name: Leaseweb Networkequipment API
  slug: leaseweb-networkequipment-api
- baseURL: https://api.leaseweb.com/publicCloud/v1
  baseurl_source: declared
  description: The objectstorage API from Leaseweb — 9 operation(s) for objectstorage.
  name: Leaseweb Objectstorage API
  slug: leaseweb-objectstorage-api
- baseURL: https://api.leaseweb.com/publicCloud/v1
  baseurl_source: declared
  description: The ordering API from Leaseweb — 6 operation(s) for ordering.
  name: Leaseweb Ordering API
  slug: leaseweb-ordering-api
artifact_total: 68
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/leaseweb/refs/heads/main/agentic-access/leaseweb-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/leaseweb-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leaseweb/refs/heads/main/rules/leaseweb-rules.yml
  title: ''
  type: Spectral
  url: rules/leaseweb-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leaseweb/refs/heads/main/json-ld/leaseweb-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/leaseweb-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leaseweb/refs/heads/main/vocabulary/leaseweb-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/leaseweb-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leaseweb/refs/heads/main/data-model/leaseweb-data-model.yml
  title: ''
  type: DataModel
  url: data-model/leaseweb-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leaseweb/refs/heads/main/authentication/leaseweb-authentication.yml
  title: ''
  type: Authentication
  url: authentication/leaseweb-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leaseweb/refs/heads/main/errors/leaseweb-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/leaseweb-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leaseweb/refs/heads/main/conformance/leaseweb-conformance.yml
  title: ''
  type: Conformance
  url: conformance/leaseweb-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/leaseweb/refs/heads/main/hosts/leaseweb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/leaseweb-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/leaseweb/refs/heads/main/vendors/leaseweb-vendors.yml
  title: ''
  type: Vendors
  url: vendors/leaseweb-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/leaseweb/refs/heads/main/packages/leaseweb-packages.yml
  title: ''
  type: SDKs
  url: packages/leaseweb-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/leaseweb/refs/heads/main/packages/leaseweb-packages.yml
  title: ''
  type: Packages
  url: packages/leaseweb-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leaseweb/refs/heads/main/security/leaseweb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leaseweb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.leaseweb.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.leaseweb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.leaseweb.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.leaseweb.com/get-started/
- group: company
  title: ''
  type: Blog
  url: https://blog.leaseweb.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leaseweb
- group: start
  title: ''
  type: Login
  url: https://secure.leaseweb.com/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/leaseweb/leaseweb-go-sdk
created: '2026-10-13'
description: Leaseweb is a Netherlands-founded global Infrastructure-as-a-Service provider offering dedicated (bare metal) servers, public and private cloud, object storage, CDN, colocation and networking. Its Developer API at api.leaseweb.com lets customers automate and integrate their infrastructure, authenticated with an API key sent in the X-LSW-Auth header; Leaseweb publishes the OpenAPI definitions in its leaseweb-go-sdk GitHub repository.
json_schemas:
- name: aggregationPack
  property_count: 11
  slug: leaseweb-aggregation-pack
- name: autoScalingGroupDetails
  property_count: 16
  slug: leaseweb-auto-scaling-group-details
- name: bucket
  property_count: 8
  slug: leaseweb-bucket
- name: createObjectStorageAccessKeyResult
  property_count: 6
  slug: leaseweb-create-object-storage-access-key-result
- name: createObjectStorageBucketOpts
  property_count: 3
  slug: leaseweb-create-object-storage-bucket-opts
- name: createReportMessageOpts
  property_count: 2
  slug: leaseweb-create-report-message-opts
- name: credentialList
  property_count: 2
  slug: leaseweb-credential-list
- name: dedicatedServerList
  property_count: 2
  slug: leaseweb-dedicated-server-list
- name: dedicatedServer
  property_count: 0
  slug: leaseweb-dedicated-server
- name: getAggregationPackListResult
  property_count: 2
  slug: leaseweb-get-aggregation-pack-list-result
- name: getHardwareResult
  property_count: 5
  slug: leaseweb-get-hardware-result
- name: getInvoicePdfResult
  property_count: 0
  slug: leaseweb-get-invoice-pdf-result
- name: getInvoiceResult
  property_count: 12
  slug: leaseweb-get-invoice-result
- name: getInvoicesExportCsvResult
  property_count: 0
  slug: leaseweb-get-invoices-export-csv-result
- name: getInvoicesResult
  property_count: 2
  slug: leaseweb-get-invoices-result
- name: getIPListResult
  property_count: 2
  slug: leaseweb-get-iplist-result
- name: getNetworkEquipmentListResult
  property_count: 2
  slug: leaseweb-get-network-equipment-list-result
- name: getNullRouteHistoryListResult
  property_count: 2
  slug: leaseweb-get-null-route-history-list-result
- name: objectStorageBucketList
  property_count: 1
  slug: leaseweb-get-object-storage-bucket-list-result
- name: objectStorageList
  property_count: 2
  slug: leaseweb-get-object-storage-list-result
- name: getProformaResult
  property_count: 7
  slug: leaseweb-get-proforma-result
- name: getQueryMetricsResult
  property_count: 2
  slug: leaseweb-get-query-metrics-result
- name: getReportListResult
  property_count: 2
  slug: leaseweb-get-report-list-result
- name: getReportMessageListResult
  property_count: 2
  slug: leaseweb-get-report-message-list-result
- name: getReportResolutionListResult
  property_count: 2
  slug: leaseweb-get-report-resolution-list-result
- name: getReportResult
  property_count: 17
  slug: leaseweb-get-report-result
- name: getResourceRecordSetListResult
  property_count: 0
  slug: leaseweb-get-resource-record-set-list-result
- name: getServerListResult
  property_count: 2
  slug: leaseweb-get-server-list-result
- name: group
  property_count: 4
  slug: leaseweb-group
- name: importResourceRecordSetsResult
  property_count: 3
  slug: leaseweb-import-resource-record-sets-result
- name: infoMessageResult
  property_count: 1
  slug: leaseweb-info-message-result
- name: instanceDetails
  property_count: 21
  slug: leaseweb-instance-details
- name: instanceList
  property_count: 2
  slug: leaseweb-instance-list
- name: ipList
  property_count: 2
  slug: leaseweb-ip-list
- name: ip
  property_count: 9
  slug: leaseweb-ip
- name: jobList
  property_count: 2
  slug: leaseweb-job-list
- name: job
  property_count: 15
  slug: leaseweb-job
- name: loadBalancerDetails
  property_count: 11
  slug: leaseweb-load-balancer-details
- name: loadBalancerListenerDetails
  property_count: 0
  slug: leaseweb-load-balancer-listener-details
- name: loadBalancers
  property_count: 2
  slug: leaseweb-load-balancers
- name: networkEquipment
  property_count: 11
  slug: leaseweb-network-equipment
- name: nullRouteIPOpts
  property_count: 3
  slug: leaseweb-null-route-ipopts
- name: nullRouteList
  property_count: 2
  slug: leaseweb-null-route-list
- name: nullRoutedIP
  property_count: 12
  slug: leaseweb-null-routed-ip
- name: orderDedicatedServerOpts
  property_count: 4
  slug: leaseweb-order-dedicated-server-opts
- name: orderVpsOpts
  property_count: 7
  slug: leaseweb-order-vps-opts
- name: resolveReportResult
  property_count: 2
  slug: leaseweb-resolve-report-result
- name: resourceRecordSetDetails
  property_count: 0
  slug: leaseweb-resource-record-set-details
- name: resourceRecordSet
  property_count: 4
  slug: leaseweb-resource-record-set
- name: serverJob
  property_count: 15
  slug: leaseweb-server-job
- name: server
  property_count: 14
  slug: leaseweb-server
- name: updateNullRouteOpts
  property_count: 3
  slug: leaseweb-update-null-route-opts
- name: vpsList
  property_count: 2
  slug: leaseweb-vps-list
- name: vps
  property_count: 0
  slug: leaseweb-vps
jsonld:
- class_count: 120
  name: Leaseweb Context
  property_count: 250
  slug: leaseweb-context
layout: provider
modified: '2026-10-13'
name: Leaseweb
nav: Providers
network: true
overview: 'Leaseweb publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Abuse API, Aggregationpack API, Dedicatedserver API, and 6 more. Tagged areas include Company, Cloud, Infrastructure-as-a-Service, Bare Metal, and Dedicated Servers.


  The Leaseweb catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Leaseweb''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 17 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Leaseweb API Rules
  rule_count: 15
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 0
  slug: leaseweb-rules
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 63.0
    catalog_earned_first_party: 0.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 19.7
    contract_quality: 64.4
    developer_ergonomics: 52.4
    discoverability: 67.9
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Leaseweb Authentication
  slug: leaseweb-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Leaseweb Domain Security
  slug: leaseweb-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: leaseweb
tags:
- Company
- Cloud
- Infrastructure-as-a-Service
- Bare Metal
- Dedicated Servers
- Object Storage
- DNS
- Hosting
website: https://www.leaseweb.com
---
