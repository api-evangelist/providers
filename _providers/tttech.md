---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 122
  human_in_the_loop: 11
  name: Tttech Agentic Access
  operation_count: 228
  slug: tttech-agentic-access
  summary_line: 228 operations · 122 acting · 11 human-in-the-loop
api_count: 4
apis:
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage authentication and authorization of MS users
  name: TTTech AUTH API
  slug: tttech-auth-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage node capabilities
  name: TTTech CAPABILITIES API
  slug: tttech-capabilities-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The CODESYS PROCESS API from TTTech — 1 operation(s) for codesys process.
  name: TTTech CODESYS PROCESS API
  slug: tttech-codesys-process-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: Node configuration operations (onboarding, retrieving the Management system version, retrieving the node's secure ID, etc.)
  name: TTTech CONFIGURATION API
  slug: tttech-configuration-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage node data exchange.
  name: TTTech DATA EXCHANGE API
  slug: tttech-data-exchange-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The DATAPATH API from TTTech — 1 operation(s) for datapath.
  name: TTTech DATAPATH API
  slug: tttech-datapath-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage workload DNA configuration
  name: TTTech DNA API
  slug: tttech-dna-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage docker compose file
  name: TTTech DOCKER COMPOSE FILE API
  slug: tttech-docker-compose-file-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The DOCKER_RESOURCES_IMAGES API from TTTech — 1 operation(s) for docker_resources_images.
  name: TTTech DOCKER RESOURCES IMAGES API
  slug: tttech-docker-resources-images-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The DOCKER_RESOURCES_VOLUMES API from TTTech — 4 operation(s) for docker_resources_volumes.
  name: TTTech DOCKER RESOURCES VOLUMES API
  slug: tttech-docker-resources-volumes-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage authentication and authorization of MQTT clients
  name: TTTech EMQX API
  slug: tttech-emqx-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The INITIALIZATION API from TTTech — 1 operation(s) for initialization.
  name: TTTech INITIALIZATION API
  slug: tttech-initialization-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: Operations intended solely for testing, used to validate system behavior under invalid or edge-case data scenarios. Not for production use.
  name: TTTech INTERNAL TEST API
  slug: tttech-internal-test-api-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage labels
  name: TTTech LABEL API
  slug: tttech-label-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage LDAP users
  name: TTTech LDAP API
  slug: tttech-ldap-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage Docker registry
  name: TTTech NERVE DOCKER REGISTRY API
  slug: tttech-nerve-docker-registry-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage Nerve updates
  name: TTTech NERVE UPDATE API
  slug: tttech-nerve-update-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage nodes v1.
  name: TTTech NODE API
  slug: tttech-node-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage nodes v2.
  name: TTTech NODE V2 API
  slug: tttech-node-v2-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage notifications.
  name: TTTech NOTIFICATION API
  slug: tttech-notification-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The PROXY SETTINGS API from TTTech — 1 operation(s) for proxy settings.
  name: TTTech PROXY SETTINGS API
  slug: tttech-proxy-settings-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage remote connections.
  name: TTTech REMOTE CONNECTIONS API
  slug: tttech-remote-connections-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The REPOSITORIES API from TTTech — 4 operation(s) for repositories.
  name: TTTech REPOSITORIES API
  slug: tttech-repositories-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage Service OS DNA configuration
  name: TTTech SERVICE OS DNA API
  slug: tttech-service-os-dna-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The SETUP NETWORK API from TTTech — 3 operation(s) for setup network.
  name: TTTech SETUP NETWORK API
  slug: tttech-setup-network-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The SYSTEM API from TTTech — 7 operation(s) for system.
  name: TTTech SYSTEM API
  slug: tttech-system-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage usage reports
  name: TTTech USAGE REPORTS API
  slug: tttech-usage-reports-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The USERS API from TTTech — 2 operation(s) for users.
  name: TTTech USERS API
  slug: tttech-users-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage workload files of specific versions v3
  name: TTTech WL VERSION FILE API
  slug: tttech-wl-version-file-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage specific versions of workloads v2
  name: TTTech WL VERSION V2 API
  slug: tttech-wl-version-v2-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage specific versions of workloads v3
  name: TTTech WL VERSION V3 API
  slug: tttech-wl-version-v3-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage workloads v1.
  name: TTTech WORKLOAD API
  slug: tttech-workload-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The WORKLOAD CODESYS API from TTTech — 2 operation(s) for workload codesys.
  name: TTTech WORKLOAD CODESYS API
  slug: tttech-workload-codesys-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage workload configurations
  name: TTTech WORKLOAD CONFIGURATION API
  slug: tttech-workload-configuration-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage workloads v2.
  name: TTTech WORKLOAD V2 API
  slug: tttech-workload-v2-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The operations to manage workloads v3.
  name: TTTech WORKLOAD V3 API
  slug: tttech-workload-v3-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The WORKLOADS API from TTTech — 6 operation(s) for workloads.
  name: TTTech WORKLOADS API
  slug: tttech-workloads-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The WORKLOADS BACKUPS API from TTTech — 3 operation(s) for workloads backups.
  name: TTTech WORKLOADS BACKUPS API
  slug: tttech-workloads-backups-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The WORKLOADS COMPOSE API from TTTech — 2 operation(s) for workloads compose.
  name: TTTech WORKLOADS COMPOSE API
  slug: tttech-workloads-compose-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The WORKLOADS LOGS API from TTTech — 2 operation(s) for workloads logs.
  name: TTTech WORKLOADS LOGS API
  slug: tttech-workloads-logs-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The WORKLOADS NETWORKS API from TTTech — 1 operation(s) for workloads networks.
  name: TTTech WORKLOADS NETWORKS API
  slug: tttech-workloads-networks-api
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: The WORKLOADS SNAPSHOTS API from TTTech — 2 operation(s) for workloads snapshots.
  name: TTTech WORKLOADS SNAPSHOTS API
  slug: tttech-workloads-snapshots-api
artifact_total: 48
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/overlays/tttech-nerve-management-system-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tttech-nerve-management-system-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/overlays/tttech-nerve-node-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tttech-nerve-node-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/agentic-access/tttech-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tttech-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/security/tttech-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tttech-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/security/tttech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tttech-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/authentication/tttech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tttech-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tttech.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://nerve.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nerve.cloud/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nerve.cloud/developer_guide/ms-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nerve.cloud/getting_started/
- group: operate
  title: ''
  type: Support
  url: https://tttech-industrial.xurrent.com/
- group: company
  title: ''
  type: Blog
  url: https://nerve.cloud/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tttech-nerve
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tttech.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tttech.com/privacy-notice
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.nerve.cloud/changelog/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/packages/tttech-packages.yml
  title: ''
  type: Packages
  url: packages/tttech-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/packages/tttech-packages.yml
  title: ''
  type: SDKs
  url: packages/tttech-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/cli/tttech-cli.yml
  title: ''
  type: CLI
  url: cli/tttech-cli.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/sandbox/tttech-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tttech-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/conventions/tttech-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tttech-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/errors/tttech-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tttech-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/data-model/tttech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tttech-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/lifecycle/tttech-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tttech-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/changelog/tttech-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tttech-changelog.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/rate-limits/tttech-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tttech-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/plans/tttech-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tttech-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/conformance/tttech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tttech-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.tttech.com/company/quality-and-standards
- group: auth
  title: ''
  type: Security
  url: https://www.tttech.com/responsible-disclosure
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/llms/tttech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tttech-llms.txt
created: '2026-09-01'
description: 'TTTech Computertechnik AG is a Vienna-based supplier of deterministic networking and safety-critical embedded platforms — TTP, TTEthernet and IEEE 802.1 Time-Sensitive Networking — for aerospace, space, automotive, energy and industrial automation. Its public developer surface is Nerve, the industrial edge computing and device-management platform built by TTTech Industrial Automation AG: a hosted Management System plus on-device node software that deploys and controls Docker, docker-compose, CODESYS and virtual machine workloads on certified edge hardware. Nerve publishes two OpenAPI 3 contracts — the Nerve Management System API (151 operations across nodes, workloads, labels, LDAP, DNA, remote connections, notifications and the Docker registry) and the Nerve Node API (77 operations for on-device configuration, networking, workloads and users) — together with a first-party Python library and CLI on GitHub. The platform is certified to IEC 62443-4-2 and ships a documented product-security
  reporting channel.'
image: https://nerve.cloud/sites/default/files/vision.jpg
layout: provider
modified: '2026-09-01'
name: TTTech
nav: Providers
network: true
overview: 'TTTech publishes 42 APIs on the [APIs.io](https://apis.io/) network, including AUTH API, CAPABILITIES API, CODESYS PROCESS API, and 39 more. Tagged areas include Company, Industrial IoT, Edge Computing, Device Management, and Deterministic Networking.


  TTTech''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, changelog, and 26 more developer resources.'
plans:
- name: Tttech Plans Pricing
  plan_count: 0
  slug: tttech-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Tttech Rate Limits
  slug: tttech-rate-limits
score:
  band: developing
  composite: 52.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 56.9
    developer_ergonomics: 80.4
    discoverability: 74.1
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 57.1
      derived: 0
      marker_coverage: 0.0
      total: 42
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/tttech/refs/heads/main/screenshots/tttech-2026-09-02T164452.png
security:
- kind: authentication
  name: Tttech Authentication
  slug: tttech-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Tttech Domain Security
  slug: tttech-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tttech Vulnerability Disclosure
  slug: tttech-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: tttech
tags:
- Company
- Industrial IoT
- Edge Computing
- Device Management
- Deterministic Networking
- Time-Sensitive Networking
- Industrial Automation
- Workload Orchestration
- Embedded Systems
- Safety Critical
- OPC UA
- MQTT
- CODESYS
- IEC 62443
website: https://www.tttech.com/
---
