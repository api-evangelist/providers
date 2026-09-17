---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.4
  scored_at: '2026-09-16'
api_count: 8
apis:
- description: The HTTP/JSON surface of OpenMLDB's optional APIServer module — insert rows into a table, invoke a deployed real-time feature-computation service, run online/offline SQL, read deployment and table met
  name: OpenMLDB APIServer REST API
  slug: 4paradigm-openmldb-apiserver
- description: The Protobuf/brpc service contracts behind an OpenMLDB cluster — TabletServer, NameServer, TaskManager, the data-sync services and the APIServer HTTP bridge — published verbatim in the OpenMLDB source
  name: OpenMLDB Cluster RPC Services
  slug: 4paradigm-openmldb-cluster-rpc
- description: 'The read-only JSON API behind 4Paradigm''s Sage App Store — the model catalogue (62 AI models with version, category and short description), the self-referencing category tree, the solutions list, the '
  name: Sage App Store Catalogue API
  slug: 4paradigm-sage-app-store
- description: PhanthyMotus is 4Paradigm's open-source embodied-AI agent framework. Every hardware driver bundle is a Model Context Protocol server exposing typed cards — sensor, actuator, processor and resource — w
  name: PhanthyMotus Agent Core and Driver MCP Bus
  slug: 4paradigm-phanthymotus
- baseURL: http://127.0.0.1:8080
  baseurl_source: declared
  description: The account API from 4Paradigm — 3 operation(s) for account.
  name: 4Paradigm Account API
  slug: 4paradigm-account-api
- baseURL: http://127.0.0.1:8080
  baseurl_source: declared
  description: The applications API from 4Paradigm — 6 operation(s) for applications.
  name: 4Paradigm Applications API
  slug: 4paradigm-applications-api
- baseURL: http://127.0.0.1:8080
  baseurl_source: declared
  description: The competition API from 4Paradigm — 3 operation(s) for competition.
  name: 4Paradigm Competition API
  slug: 4paradigm-competition-api
- baseURL: http://127.0.0.1:8080
  baseurl_source: declared
  description: The computeunit API from 4Paradigm — 4 operation(s) for computeunit.
  name: 4Paradigm Computeunit API
  slug: 4paradigm-computeunit-api
- baseURL: http://127.0.0.1:8080
  baseurl_source: declared
  description: The computing_resource API from 4Paradigm — 1 operation(s) for computing_resource.
  name: 4Paradigm Computing Resource API
  slug: 4paradigm-computing-resource-api
- baseURL: http://127.0.0.1:8080
  baseurl_source: declared
  description: The environments API from 4Paradigm — 2 operation(s) for environments.
  name: 4Paradigm Environments API
  slug: 4paradigm-environments-api
- baseURL: http://127.0.0.1:8080
  baseurl_source: declared
  description: The finished API from 4Paradigm — 1 operation(s) for finished.
  name: 4Paradigm Finished API
  slug: 4paradigm-finished-api
- baseURL: http://127.0.0.1:8080
  baseurl_source: declared
  description: The images API from 4Paradigm — 6 operation(s) for images.
  name: 4Paradigm Images API
  slug: 4paradigm-images-api
- baseURL: http://127.0.0.1:8080
  baseurl_source: declared
  description: The logs API from 4Paradigm — 1 operation(s) for logs.
  name: 4Paradigm Logs API
  slug: 4paradigm-logs-api
- baseURL: http://127.0.0.1:8080
  baseurl_source: declared
  description: The releases API from 4Paradigm — 3 operation(s) for releases.
  name: 4Paradigm Releases API
  slug: 4paradigm-releases-api
- baseURL: http://127.0.0.1:8080
  baseurl_source: declared
  description: The storage API from 4Paradigm — 3 operation(s) for storage.
  name: 4Paradigm Storage API
  slug: 4paradigm-storage-api
- baseURL: http://127.0.0.1:8080
  baseurl_source: declared
  description: The users API from 4Paradigm — 3 operation(s) for users.
  name: 4Paradigm Users API
  slug: 4paradigm-users-api
- baseURL: http://127.0.0.1:8080
  baseurl_source: declared
  description: The App Store API from 4Paradigm — 3 operation(s) for app store.
  name: 4Paradigm App Store API
  slug: 4paradigm-app-store-api
artifact_total: 22
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/overlays/4paradigm-openaios-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/4paradigm-openaios-platform-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/overlays/4paradigm-openaios-platform-internal-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/4paradigm-openaios-platform-internal-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/overlays/4paradigm-openaios-webterminal-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/4paradigm-openaios-webterminal-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/overlays/4paradigm-openaios-billing-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/4paradigm-openaios-billing-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/security/4paradigm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/4paradigm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.4paradigm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://openmldb.ai/docs/en/main/
- group: docs
  title: ''
  type: APIReference
  url: https://openmldb.ai/docs/en/main/quickstart/sdk/rest_api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://openmldb.ai/docs/en/main/quickstart/openmldb_quickstart.html
- group: operate
  title: ''
  type: Support
  url: https://openmldb.ai/docs/en/main/about/community.html
- group: company
  title: ''
  type: Blog
  url: https://openmldb.ai/docs/en/main/blog_post/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/4paradigm
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.4paradigm.com/other/agreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.4paradigm.com/other/privacy.html
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/packages/4paradigm-packages.yml
  title: ''
  type: Packages
  url: packages/4paradigm-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/packages/4paradigm-packages.yml
  title: ''
  type: SDKs
  url: packages/4paradigm-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/cli/4paradigm-cli.yml
  title: ''
  type: CLI
  url: cli/4paradigm-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/llms/4paradigm-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/4paradigm-llms.txt
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/changelog/4paradigm-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/4paradigm-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/lifecycle/4paradigm-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/4paradigm-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/conventions/4paradigm-conventions.yml
  title: ''
  type: Conventions
  url: conventions/4paradigm-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/conformance/4paradigm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/4paradigm-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/errors/4paradigm-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/4paradigm-problem-types.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/authentication/4paradigm-authentication.yml
  title: ''
  type: Authentication
  url: authentication/4paradigm-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/data-model/4paradigm-data-model.yml
  title: ''
  type: DataModel
  url: data-model/4paradigm-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/plans/4paradigm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/4paradigm-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/rate-limits/4paradigm-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/4paradigm-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/4paradigm/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-05'
description: '4Paradigm (Beijing Fourth Paradigm Intelligent Technology, HKEX 6682) is a Chinese enterprise AI company building decision-making and generative AI platforms — the Sage AIOS AI operating system, Sage HyperCycle ML/CV/OCR, SageGPT and the SageOne AI computing appliances — for banking, insurance, securities, retail, energy, healthcare and manufacturing. Its public, machine-readable API surface is published almost entirely through its open-source community at github.com/4paradigm: OpenMLDB, an Apache-2.0 machine-learning feature database with a documented REST APIServer, Protobuf/brpc cluster services and Java/Python/Go/C++ SDKs; OpenAIOS-Platform (Pineapple), a Kubernetes-based AI development platform that ships OpenAPI 3.0.3 contracts; and PhanthyMotus, an MCP-native embodied-AI agent framework whose hardware drivers are Model Context Protocol servers.'
image: https://www.4paradigm.com/images/logo.png
layout: provider
mcp_servers:
- description: ''
  name: PhanthyMotus driver MCP bus
  slug: phanthymotus-driver-mcp-bus
modified: '2026-09-05'
name: 4Paradigm
nav: Providers
network: true
overview: '4Paradigm publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Account API, Applications API, Competition API, and 10 more. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Feature Store, and Database.


  4Paradigm''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, changelog, and 21 more developer resources.'
plans:
- name: 4Paradigm Plans Pricing
  plan_count: 0
  slug: 4paradigm-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: 4Paradigm Rate Limits
  slug: 4paradigm-rate-limits
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 15.8
    contract_governance: 4.5
    contract_quality: 48.3
    developer_ergonomics: 60.1
    discoverability: 72.2
    operational_transparency: 18.4
  previous_composite: 36.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: 4Paradigm Authentication
  slug: 4paradigm-authentication
  summary_line: apiKey/openIdConnect/none · 6 schemes
- kind: domain-security
  name: 4Paradigm Domain Security
  slug: 4paradigm-domain-security
  summary_line: TLSv1.2
slug: 4paradigm
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Feature Store
- Database
- Open-Source
- MLOps
- Agents
- Robotics
- Kubernetes
website: https://www.4paradigm.com/
---
