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
  schema_version: 0.2
  score: 27.4
  scored_at: '2026-09-05'
api_count: 4
apis:
- description: The HTTP/JSON surface of OpenMLDB's optional APIServer module — insert rows into a table, invoke a deployed real-time feature-computation service, run online/offline SQL, read deployment and table met
  name: OpenMLDB APIServer REST API
  slug: 4paradigm-openmldb-apiserver
- description: The Protobuf/brpc service contracts behind an OpenMLDB cluster — TabletServer, NameServer, TaskManager, the data-sync services and the APIServer HTTP bridge — published verbatim in the OpenMLDB source
  name: OpenMLDB Cluster RPC Services
  slug: 4paradigm-openmldb-cluster-rpc
- baseURL: http://127.0.0.1:1234/api
  baseurl_source: declared
  description: The REST API of OpenAIOS-Platform, 4Paradigm's Kubernetes-based AI development platform — environments, applications, Helm releases, the app store, container images, object storage, competitions, cont
  name: OpenAIOS Platform API (Pineapple)
  slug: 4paradigm-openaios-platform
- baseURL: http://127.0.0.1:4321/api
  baseurl_source: declared
  description: The metering and billing service of OpenAIOS-Platform — user accounts, account balances, compute-unit assignment by user and group, and compute-unit pricing. Published as OpenAPI 3.0.3 in the openaios
  name: OpenAIOS Platform Billing API
  slug: 4paradigm-openaios-billing
- description: 'The read-only JSON API behind 4Paradigm''s Sage App Store — the model catalogue (62 AI models with version, category and short description), the self-referencing category tree, the solutions list, the '
  name: Sage App Store Catalogue API
  slug: 4paradigm-sage-app-store
- description: PhanthyMotus is 4Paradigm's open-source embodied-AI agent framework. Every hardware driver bundle is a Model Context Protocol server exposing typed cards — sensor, actuator, processor and resource — w
  name: PhanthyMotus Agent Core and Driver MCP Bus
  slug: 4paradigm-phanthymotus
artifact_total: 11
common:
- group: auth
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
  title: ''
  type: Packages
  url: packages/4paradigm-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/4paradigm-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/4paradigm-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/4paradigm-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/4paradigm-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/4paradigm-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/4paradigm-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/4paradigm-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/4paradigm-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/4paradigm-authentication.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/4paradigm-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/4paradigm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/4paradigm-rate-limits.yml
- group: agent
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
overview: '4Paradigm publishes 2 APIs on the [APIs.io](https://apis.io/) network: OpenAIOS Platform API (Pineapple) and OpenAIOS Platform Billing API. Tagged areas include Company, Artificial Intelligence, Machine Learning, Feature Store, and Databases.


  4Paradigm''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, changelog, and 17 more developer resources.'
plans:
- name: 4Paradigm Plans Pricing
  plan_count: 0
  slug: 4paradigm-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: 4Paradigm Rate Limits
  slug: 4paradigm-rate-limits
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 4.5
    contract_quality: 46.5
    developer_ergonomics: 60.1
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 18.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Machine Learning
- Feature Store
- Databases
- Open Source
- MLOps
- Agents
- Robotics
- Kubernetes
website: https://www.4paradigm.com/
---
