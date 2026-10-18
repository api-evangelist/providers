---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 495
  human_in_the_loop: 42
  name: Zadara Agentic Access
  operation_count: 794
  slug: zadara-agentic-access
  summary_line: 794 operations · 495 acting · 42 human-in-the-loop
api_count: 8
apis:
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving Command Center access logs.
  name: Zadara Access Logs API
  slug: zadara-access-logs-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations for Accounts.
  name: Zadara Accounts API
  slug: zadara-accounts-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Methods for authenticating with the Provisioning Portal.
  name: Zadara Authentication API
  slug: zadara-authentication-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving billing.
  name: Zadara Billing API
  slug: zadara-billing-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Retrieve Cloud's Configurations
  name: Zadara Cloud API
  slug: zadara-cloud-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving Cloud Settings.
  name: Zadara Cloud Settings API
  slug: zadara-cloud-settings-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving Cloud's users.
  name: Zadara Cloud Users API
  slug: zadara-cloud-users-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving Clouds.
  name: Zadara Clouds API
  slug: zadara-clouds-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving Comments.
  name: Zadara Comments API
  slug: zadara-comments-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Compute accounts operations
  name: Zadara Compute API
  slug: zadara-compute-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving Computes.
  name: Zadara Computes API
  slug: zadara-computes-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving Consistency Groups.
  name: Zadara Consistency Groups API
  slug: zadara-consistency-groups-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations for Container Replications
  name: Zadara Container Replications API
  slug: zadara-container-replications-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations for Containers
  name: Zadara Containers API
  slug: zadara-containers-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations for Controllers.
  name: Zadara Controllers API
  slug: zadara-controllers-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving Custom Networks.
  name: Zadara Custom Networks API
  slug: zadara-custom-networks-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving drives.
  name: Zadara Drive API
  slug: zadara-drive-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving Drive Types.
  name: Zadara Drive Types API
  slug: zadara-drive-types-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving Drives.
  name: Zadara Drives API
  slug: zadara-drives-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving APP/IO engine types.
  name: Zadara Engine types API
  slug: zadara-engine-types-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving fault domains.
  name: Zadara Fault Domains API
  slug: zadara-fault-domains-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving File Lifecycle.
  name: Zadara File Lifecycle API
  slug: zadara-file-lifecycle-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving File Lifecycle Policies.
  name: Zadara File Lifecycle Policies API
  slug: zadara-file-lifecycle-policies-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving images.
  name: Zadara Images API
  slug: zadara-images-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations for Load Balancer.
  name: Zadara Load Balancer API
  slug: zadara-load-balancer-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving central logs.
  name: Zadara Logs API
  slug: zadara-logs-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations for Remote Mirroring and Cloning.
  name: Zadara Mirroring and Cloning API
  slug: zadara-mirroring-and-cloning-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations for NAS (Network Attached Storage) Users and Groups.
  name: Zadara NAS API
  slug: zadara-nas-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations for Object Storage Destinations.
  name: Zadara Object Storage Destinations API
  slug: zadara-object-storage-destinations-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Organizations
  name: Zadara Organizations API
  slug: zadara-organizations-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving Pools.
  name: Zadara Pools API
  slug: zadara-pools-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Get the list of prices for all providers.
  name: Zadara Prices API
  slug: zadara-prices-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Retrieve Providers Configurations
  name: Zadara Providers API
  slug: zadara-providers-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving RAID Groups.
  name: Zadara RAID Groups API
  slug: zadara-raid-groups-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving Command Center remote authentication directories.
  name: Zadara Remote authentications API
  slug: zadara-remote-authentications-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations for Remote Object Storages.
  name: Zadara Remote object storage API
  slug: zadara-remote-object-storage-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving Command Center roles.
  name: Zadara Roles API
  slug: zadara-roles-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving Servers.
  name: Zadara Servers API
  slug: zadara-servers-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Get / Modify Settings.
  name: Zadara Settings API
  slug: zadara-settings-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations for Snapshot Policies.
  name: Zadara Snapshot Policies API
  slug: zadara-snapshot-policies-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations for Snapshots.
  name: Zadara Snapshots API
  slug: zadara-snapshots-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving logs.
  name: Zadara Software install API
  slug: zadara-software-install-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving Storage Nodes.
  name: Zadara Storage Nodes API
  slug: zadara-storage-nodes-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations for Storage Policies.
  name: Zadara Storage Policies API
  slug: zadara-storage-policies-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Retrieve Tenants information
  name: Zadara Tenant API
  slug: zadara-tenant-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations for Unified Identity.
  name: Zadara Unified Identity API
  slug: zadara-unified-identity-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations for usage reports.
  name: Zadara Usage Reports API
  slug: zadara-usage-reports-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving Command Center users.
  name: Zadara Users API
  slug: zadara-users-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations for Virtual Controllers.
  name: Zadara Virtual Controllers API
  slug: zadara-virtual-controllers-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Retrieve Vlan's Configurations
  name: Zadara Virtual Network API
  slug: zadara-virtual-network-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving VLAN.
  name: Zadara VLAN API
  slug: zadara-vlan-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving volumes.
  name: Zadara Volume API
  slug: zadara-volume-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving Volumes.
  name: Zadara Volumes API
  slug: zadara-volumes-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: The VPSA API from Zadara — 65 operation(s) for vpsa.
  name: Zadara VPSA API
  slug: zadara-vpsa-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving VPSA Object Storage.
  name: Zadara VPSA Object Storage API
  slug: zadara-vpsa-object-storage-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Vpsa Requests Actions
  name: Zadara Vpsa Requests API
  slug: zadara-vpsa-requests-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Operations involving VPSA Storage Arrays.
  name: Zadara VPSA Storage Array API
  slug: zadara-vpsa-storage-array-api
- baseURL: https://{vpsa-host}/api
  baseurl_source: declared
  description: Vpsas Description
  name: Zadara Vpsas API
  slug: zadara-vpsas-api
artifact_total: 63
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zadara/refs/heads/main/capabilities/zadara-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/zadara-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zadara/refs/heads/main/agentic-access/zadara-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zadara-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zadara/refs/heads/main/rules/zadara-rules.yml
  title: ''
  type: Spectral
  url: rules/zadara-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zadara/refs/heads/main/vocabulary/zadara-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zadara-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zadara/refs/heads/main/data-model/zadara-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zadara-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.zadara.com/edge-cloud/compliance/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zadara/refs/heads/main/errors/zadara-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zadara-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zadara/refs/heads/main/conformance/zadara-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zadara-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zadara/refs/heads/main/llms/zadara-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zadara-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zadara/refs/heads/main/well-known/zadara-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zadara-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zadara/refs/heads/main/hosts/zadara-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zadara-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zadara/refs/heads/main/vendors/zadara-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zadara-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zadara/refs/heads/main/authentication/zadara-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zadara-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zadara/refs/heads/main/security/zadara-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/zadara-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zadara/refs/heads/main/security/zadara-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zadara-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zadara.com
- group: docs
  title: ''
  type: APIReference
  url: https://api-doc.zadara.com/
- group: docs
  title: ''
  type: Documentation
  url: https://guides.zadara.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zadarastorage
- group: company
  title: ''
  type: Blog
  url: https://www.zadara.com/blog/
- group: start
  title: ''
  type: Login
  url: https://partners.zadara.com/user/login
- group: company
  title: ''
  type: Newsroom
  url: https://www.zadara.com/news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zadara.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zadara.com/privacypolicy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zadara.com/resources/terms/
created: '2026-10-13'
description: Zadara is an edge cloud and storage-as-a-service provider offering zStorage (VPSA Storage Array and Flash Array block/file storage, VPSA Object Storage) and zCompute, delivered fully managed in its own and partner data centers. Its public API documentation at api-doc.zadara.com publishes Swagger 2.0 contracts for the VPSA Storage Array, Object Storage, Command Center and Provisioning Portal REST APIs, each authenticated with an X-Access-Key header.
image: https://www.zadara.com/wp-content/uploads/poster2.jpg
layout: provider
modified: '2026-10-13'
name: Zadara
nav: Providers
network: true
overview: 'Zadara publishes 58 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Logs API, Accounts API, Authentication API, and 55 more. Tagged areas include Company, Storage, Object Storage, Block Storage, and Edge Cloud.


  The Zadara catalog on APIs.io includes 1 Spectral governance ruleset.


  Zadara''s developer surface includes authentication, API reference, documentation, engineering blog, pricing, and 20 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Zadara API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: zadara-rules
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.8
    catalog_earned_first_party: 0.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 44.2
    developer_ergonomics: 31.0
    discoverability: 80.4
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 58
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 11.1
security:
- kind: authentication
  name: Zadara Authentication
  slug: zadara-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Zadara Domain Security
  slug: zadara-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Zadara Trust Center
  slug: zadara-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: zadara
tags:
- Company
- Storage
- Object Storage
- Block Storage
- Edge Cloud
- Cloud Infrastructure
- Storage As A Service
website: https://www.zadara.com
---
