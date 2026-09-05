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
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 122
  human_in_the_loop: 11
  name: Tttech Agentic Access
  operation_count: 228
  slug: tttech-agentic-access
  summary_line: 228 operations · 122 acting · 11 human-in-the-loop
api_count: 2
apis:
- baseURL: https://trynerve1.nerve.cloud
  baseurl_source: declared
  description: REST API of the Nerve Management System, the cloud-hosted control plane for Nerve edge nodes. Covers authentication and MFA, node registration and lifecycle, workload and workload-version management (
  name: Nerve Management System API
  slug: nerve-management-system-api
- baseURL: http://172.20.2.1:3333
  baseurl_source: declared
  description: 'REST API served by the Nerve Local UI on each Nerve edge node. Covers node initialization and license activation, system and network configuration, proxy settings, local users and permissions, Docker '
  name: Nerve Node API
  slug: nerve-node-api
artifact_total: 8
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tttech-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tttech-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tttech-domain-security.yml
- group: auth
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
  title: ''
  type: Packages
  url: packages/tttech-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tttech-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tttech-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tttech-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tttech-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tttech-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tttech-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tttech-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tttech-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tttech-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tttech-plans-pricing.yml
- group: design
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
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
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
overview: 'TTTech publishes 2 APIs on the [APIs.io](https://apis.io/) network: Nerve Management System API and Nerve Node API. Tagged areas include Company, Industrial IoT, Edge Computing, Device Management, and Deterministic Networking.


  TTTech''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, changelog, and 24 more developer resources.'
plans:
- name: Tttech Plans Pricing
  plan_count: 0
  slug: tttech-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Tttech Rate Limits
  slug: tttech-rate-limits
score:
  band: developing
  composite: 53.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 56.6
    developer_ergonomics: 80.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 63.2
  previous_composite: 53.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
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
