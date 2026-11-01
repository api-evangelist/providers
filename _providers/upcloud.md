---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 260
  human_in_the_loop: 8
  name: Upcloud Agentic Access
  operation_count: 487
  slug: upcloud-agentic-access
  summary_line: 487 operations · 260 acting · 8 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: Account management and authentication
  name: UpCloud Account API
  slug: upcloud-account-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: 'UpCloud API calls can be authenticated with HTTP Bearer (token) authentication. The token API requests below allow creation, management and deletion of bearer tokens. The bearer token can be used for '
  name: UpCloud Account Tokens API
  slug: upcloud-account-tokens-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: The Audit Log Service API allows customers to query and export their audit logs. Audit logs track all actions performed on customer accounts, including resource creation, modification, and deletion. T
  name: UpCloud Audit Logs API
  slug: upcloud-audit-logs-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: Currency management
  name: UpCloud Currency API
  slug: upcloud-currency-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: A Managed Database is a database-as-a-service that lets customers use a database without setting up servers or database software. The service configuration defines high availability, resources, the da
  name: UpCloud Database API
  slug: upcloud-database-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: Device management
  name: UpCloud Device API
  slug: upcloud-device-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: Event management
  name: UpCloud Events API
  slug: upcloud-events-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: File Storage is a scalable file storage service that provides shared access to files over a network using the NFS protocol. The File Storage API allows the creation, configuration, and deletion of fil
  name: UpCloud File Storage API
  slug: upcloud-file-storage-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: UpCloud SDN Firewall API. Allows creation, management and deletion of Firewall rulesets and Firewall rules.
  name: UpCloud Firewall Ruleset API
  slug: upcloud-firewall-ruleset-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: UpCloud Gateway API. Allows creation, management and deletion of gateways.
  name: UpCloud Gateway API
  slug: upcloud-gateway-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: The UpCloud network has public and private IP addresses. Public IP addresses are used to connect to the server from the Internet. Private Utility network addresses are available for all servers within
  name: UpCloud Ip Address API
  slug: upcloud-ip-address-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: 'Kubernetes is a container orchestration system for automating, managing and scaling software deployment. Managed Kubernetes allows you to easily create Kubernetes clusters without having to take care '
  name: UpCloud Kubernetes API
  slug: upcloud-kubernetes-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: A Managed load balancer works as the network level frontend of customer application by directing connections to the backend servers. The Managed load balancer API allows customer to manage their servi
  name: UpCloud Load Balancer API
  slug: upcloud-load-balancer-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: 'The network API calls present the different networks attached to cloud servers and allow the configuration of SDN private networks. Networks define a secure connections between attached cloud servers '
  name: UpCloud Network API
  slug: upcloud-network-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: Network peering management
  name: UpCloud Network Peering API
  slug: upcloud-network-peering-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: Object Storage is a computer data storage architecture that manages data as objects as opposed to block storage which manages data as blocks within sectors and tracks. Managed Object storage is common
  name: UpCloud Object Storage 2 API
  slug: upcloud-object-storage-2-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: Partner API gives UpCloud partners the ability manage accounts for their customers. Note that use of this API is available only to accounts provisioned as partner accounts. Please contact your account
  name: UpCloud Partner API
  slug: upcloud-partner-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: Manage permissions for sub-accounts to access resources owned by the main account.
  name: UpCloud Permission API
  slug: upcloud-permission-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: Plans are preconfigured server configurations with fixed price. Each plan includes certain number of CPU cores, memory amount, storage and transfer quota. Most plans also include one public IPv4 addre
  name: UpCloud Plan API
  slug: upcloud-plan-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: Retrieve pricing information for UpCloud resources and services.
  name: UpCloud Price API
  slug: upcloud-price-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: Router management
  name: UpCloud Router API
  slug: upcloud-router-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: Manages Cloud Servers
  name: UpCloud Server API
  slug: upcloud-server-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: Server group management
  name: UpCloud Server Group API
  slug: upcloud-server-group-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: Server size management
  name: UpCloud Server Size API
  slug: upcloud-server-size-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: Block Storage is similar to a physical hard disk. It can be used to install an operating system or hold another filesystem for a Cloud Server. Writable Block Storage and CD-ROM resources can be freely
  name: UpCloud Storage API
  slug: upcloud-storage-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: User can define a set of free-form tags to group and identify a subset of their servers. Tags can be for example _webserver_, _database_, _PROD_, _QA_, _DEV_ etc. A server can have several tags. API c
  name: UpCloud Tag API
  slug: upcloud-tag-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: Timezone management
  name: UpCloud Timezone API
  slug: upcloud-timezone-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: VNC keymap management
  name: UpCloud Vnc Keymap API
  slug: upcloud-vnc-keymap-api
- baseURL: https://api.upcloud.com
  baseurl_source: declared
  description: Operations for managing zones.
  name: UpCloud Zone API
  slug: upcloud-zone-api
artifact_total: 37
common:
- group: commercial
  href: https://artifacts.apis.io/upcloud/plans/upcloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/upcloud-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/upcloud/capabilities/upcloud-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/upcloud-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/upcloud/agentic-access/upcloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/upcloud-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/upcloud/rules/upcloud-rules.yml
  title: ''
  type: Spectral
  url: rules/upcloud-rules.yml
- group: design
  href: https://artifacts.apis.io/upcloud/json-ld/upcloud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/upcloud-context.jsonld
- group: design
  href: https://artifacts.apis.io/upcloud/vocabulary/upcloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/upcloud-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/upcloud/data-model/upcloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/upcloud-data-model.yml
- group: build
  href: https://artifacts.apis.io/upcloud/cli/upcloud-cli.yml
  title: ''
  type: CLI
  url: cli/upcloud-cli.yml
- group: design
  href: https://artifacts.apis.io/upcloud/errors/upcloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/upcloud-problem-types.yml
- group: design
  href: https://artifacts.apis.io/upcloud/conformance/upcloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/upcloud-conformance.yml
- group: agent
  href: https://artifacts.apis.io/upcloud/llms/upcloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/upcloud-llms.txt
- group: auth
  href: https://artifacts.apis.io/upcloud/well-known/upcloud-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/upcloud-status-security.txt
- group: agent
  href: https://artifacts.apis.io/upcloud/well-known/upcloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/upcloud-well-known.yml
- group: other
  href: https://artifacts.apis.io/upcloud/hosts/upcloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/upcloud-hosts.yml
- group: other
  href: https://artifacts.apis.io/upcloud/vendors/upcloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/upcloud-vendors.yml
- group: build
  href: https://artifacts.apis.io/upcloud/packages/upcloud-packages.yml
  title: ''
  type: SDKs
  url: packages/upcloud-packages.yml
- group: build
  href: https://artifacts.apis.io/upcloud/packages/upcloud-packages.yml
  title: ''
  type: Packages
  url: packages/upcloud-packages.yml
- group: auth
  href: https://artifacts.apis.io/upcloud/authentication/upcloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/upcloud-authentication.yml
- group: auth
  href: https://artifacts.apis.io/upcloud/security/upcloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/upcloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://upcloud.com
- group: company
  title: ''
  type: Blog
  url: https://upcloud.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://upcloud.com/docs/changelog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.upcloud.com/api/1.3
- group: docs
  title: ''
  type: Documentation
  url: https://upcloud.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.upcloud.com/api/1.3/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UpCloudLtd
- group: start
  title: ''
  type: Login
  url: https://hub.upcloud.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://upcloud.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upcloud.com/privacy-notice/
- group: start
  title: ''
  type: SignUp
  url: https://signup.upcloud.com/?promo=goupcloud
- group: operate
  title: ''
  type: StatusPage
  url: https://status.upcloud.com/
- group: operate
  title: ''
  type: Support
  url: https://upcloud.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://upcloud.com/terms-of-service/
created: '2026-10-13'
description: UpCloud is a Finnish cloud infrastructure provider offering cloud servers, block and object storage, managed databases, managed Kubernetes (UKS), load balancers and private networking from data centres in Europe, North America, Asia and Australia. Its public REST API (version 1.3, api.upcloud.com) is documented at developers.upcloud.com with a published OpenAPI 3.1 contract, and is backed by official Go, Python and PHP clients, the upctl CLI and a Terraform provider.
finops:
- has_sources: true
  method: derived
  name: Upcloud Finops
  primary_unit: hour
  service_category: ''
  slug: upcloud-finops
  template: false
jsonld:
- class_count: 120
  name: Upcloud Context
  property_count: 168
  slug: upcloud-context
layout: provider
modified: '2026-10-13'
name: UpCloud
nav: Providers
network: true
overview: 'UpCloud publishes 29 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Account Tokens API, Audit Logs API, and 26 more. Tagged areas include Company, Cloud, Infrastructure, Object Storage, and Kubernetes.


  The UpCloud catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  UpCloud''s developer surface includes CLI, authentication, engineering blog, changelog, documentation, getting-started guide, pricing, and 26 more developer resources.'
plans:
- name: Upcloud Plans Pricing
  plan_count: 22
  slug: upcloud-plans-pricing
- name: Upcloud Price Estimates
  plan_count: 0
  slug: upcloud-price-estimates
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: UpCloud API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: upcloud-rules
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 58.7
    developer_ergonomics: 64.3
    discoverability: 62.5
    operational_transparency: 47.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - finland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 52.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Upcloud Authentication
  slug: upcloud-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Upcloud Domain Security
  slug: upcloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: upcloud
tags:
- Company
- Cloud
- Infrastructure
- Object Storage
- Kubernetes
- Database
- Servers
- Networking
website: https://upcloud.com
---
