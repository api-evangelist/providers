---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-11-06'
api_count: 8
apis:
- baseURL: https://{infinibox_host}/api/rest
  baseurl_source: declared
  description: The components API from Infinidat — 7 operation(s) for components.
  name: Infinidat Components API
  slug: infinidat-components-api
- baseURL: https://{infinibox_host}/api/rest
  baseurl_source: declared
  description: The config API from Infinidat — 11 operation(s) for config.
  name: Infinidat Config API
  slug: infinidat-config-api
- baseURL: https://{infinibox_host}/api/rest
  baseurl_source: declared
  description: The filesystems API from Infinidat — 2 operation(s) for filesystems.
  name: Infinidat Filesystems API
  slug: infinidat-filesystems-api
- baseURL: https://{infinibox_host}/api/rest
  baseurl_source: declared
  description: The hosts API from Infinidat — 1 operation(s) for hosts.
  name: Infinidat Hosts API
  slug: infinidat-hosts-api
- baseURL: https://{infinibox_host}/api/rest
  baseurl_source: declared
  description: The metadata API from Infinidat — 2 operation(s) for metadata.
  name: Infinidat Metadata API
  slug: infinidat-metadata-api
- baseURL: https://{infinibox_host}/api/rest
  baseurl_source: declared
  description: The pools API from Infinidat — 1 operation(s) for pools.
  name: Infinidat Pools API
  slug: infinidat-pools-api
- baseURL: https://{infinibox_host}/api/rest
  baseurl_source: declared
  description: The system API from Infinidat — 12 operation(s) for system.
  name: Infinidat System API
  slug: infinidat-system-api
- baseURL: https://{infinibox_host}/api/rest
  baseurl_source: declared
  description: The users API from Infinidat — 2 operation(s) for users.
  name: Infinidat Users API
  slug: infinidat-users-api
artifact_total: 17
asyncapis:
- description: ''
  name: Infinidat Events
  slug: infinidat-events
collections:
- collection_type: open
  name: Infinidat InfiniBox REST API (7.3)
  slug: open-infinidat-infinibox
common:
- group: other
  href: https://artifacts.apis.io/infinidat/overlays/infinidat-infinibox-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infinidat-infinibox-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.infinidat.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://support.infinidat.com/hc/en-us/categories/10106041231901-Documentation
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/Infinidat/api_7_3
- group: start
  title: ''
  type: GettingStarted
  url: https://infinisdk.readthedocs.io/en/latest/getting_started.html
- group: operate
  title: ''
  type: Support
  url: https://support.infinidat.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.infinidat.com/en/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.infinidat.com/en/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Infinidat
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.infinidat.com/en/sites/default/files/resource-pdfs/INFINIDAT-Customer-Product-Online-TCs.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.infinidat.com/sites/default/files/resource-pdfs/Infinidat-Privacy-Policy.pdf
- group: build
  href: https://artifacts.apis.io/infinidat/postman/infinidat-infinibox-7-3-postman.json
  title: ''
  type: Postman
  url: postman/infinidat-infinibox-7-3-postman.json
- group: build
  href: https://artifacts.apis.io/infinidat/packages/infinidat-packages.yml
  title: ''
  type: Packages
  url: packages/infinidat-packages.yml
- group: build
  href: https://artifacts.apis.io/infinidat/packages/infinidat-packages.yml
  title: ''
  type: SDKs
  url: packages/infinidat-packages.yml
- group: build
  href: https://artifacts.apis.io/infinidat/cli/infinidat-cli.yml
  title: ''
  type: CLI
  url: cli/infinidat-cli.yml
- group: agent
  href: https://artifacts.apis.io/infinidat/well-known/infinidat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/infinidat-well-known.yml
- group: auth
  href: https://artifacts.apis.io/infinidat/authentication/infinidat-authentication.yml
  title: ''
  type: Authentication
  url: authentication/infinidat-authentication.yml
- group: design
  href: https://artifacts.apis.io/infinidat/conventions/infinidat-conventions.yml
  title: ''
  type: Conventions
  url: conventions/infinidat-conventions.yml
- group: design
  href: https://artifacts.apis.io/infinidat/errors/infinidat-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/infinidat-problem-types.yml
- group: design
  href: https://artifacts.apis.io/infinidat/data-model/infinidat-data-model.yml
  title: ''
  type: DataModel
  url: data-model/infinidat-data-model.yml
- group: other
  href: https://artifacts.apis.io/infinidat/asyncapi/infinidat-events.yml
  title: ''
  type: Events
  url: asyncapi/infinidat-events.yml
- group: design
  href: https://artifacts.apis.io/infinidat/lifecycle/infinidat-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/infinidat-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/infinidat/changelog/infinidat-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/infinidat-changelog.yml
- group: design
  href: https://artifacts.apis.io/infinidat/conformance/infinidat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/infinidat-conformance.yml
- group: agent
  href: https://artifacts.apis.io/infinidat/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/infinidat/llms/infinidat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/infinidat-llms.txt
- group: auth
  href: https://artifacts.apis.io/infinidat/security/infinidat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/infinidat-domain-security.yml
created: '2026-08-01'
description: 'Infinidat is an enterprise storage vendor — a Lenovo company since April 2026 — building petabyte-scale primary storage, all-flash arrays and cyber-resilient backup appliances: InfiniBox and InfiniBox SSA for primary block and file workloads, InfiniGuard for backup and rapid recovery, and the InfiniSafe cyber-resilience layer with immutable snapshots, logical air-gapping, a fenced forensic environment and cyber detection. Every InfiniBox array serves its own management REST API (InfiniAPI) at https://<array>/api/rest, alongside the InfiniShell CLI and an HTML5 GUI. Infinidat publishes a first-party Postman collection for the InfiniBox 7.3 API, the InfiniSDK Python SDK, an Ansible collection, a Kubernetes CSI driver and an OpenStack Cinder driver on GitHub.'
image: https://www.infinidat.com/themes/sitetheme/images/opengraph.jpg
layout: provider
modified: '2026-08-01'
name: Infinidat
nav: Providers
network: true
overview: 'Infinidat is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including Components API, Config API, Filesystems API, and 5 more. Tagged areas include Company, Storage, Enterprise Storage, Data Infrastructure, and Data Protection.


  The Infinidat catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Infinidat''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, authentication, and 20 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Infinidat API Rules
  rule_count: 64
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 3
  slug: infinidat-rules
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 20.6
    developer_ergonomics: 68.0
    discoverability: 71.4
    operational_transparency: 18.4
  previous_composite: 35.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/infinidat/infinidat-2026-08-07T170658.png
security:
- kind: authentication
  name: Infinidat Authentication
  slug: infinidat-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Infinidat Domain Security
  slug: infinidat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: Check the health of an InfiniBox array
  slug: infinidat-array-health-check
- name: Inventory InfiniBox pools, filesystems and their metadata
  slug: infinidat-capacity-inventory
- name: Configure and verify an InfiniBox LDAP / Active Directory repository
  slug: infinidat-directory-integration
- name: Onboard a host onto an InfiniBox array
  slug: infinidat-host-onboarding
slug: infinidat
tags:
- Company
- Storage
- Enterprise Storage
- Data Infrastructure
- Data Protection
- Cyber Resilience
- Backup and Recovery
- Kubernetes
- Infrastructure
- On-Premises
website: https://www.infinidat.com/en
---
