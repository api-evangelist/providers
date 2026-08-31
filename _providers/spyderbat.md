---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: Ad-hoc Search interface for complex queries
  name: Spyderbat Adhoc Search API
  slug: spyderbat-adhocsearch-api
- description: Agent Action defines actions that can be executed on remote agents in response to events.
  name: Spyderbat Agent Action API
  slug: spyderbat-agent-action-api
- description: Agents represent a sepecific agent which collects data for one or more sources.
  name: Spyderbat Agent API
  slug: spyderbat-agent-api
- description: Agents registrations are used to authorize and group agents by the registration.
  name: Spyderbat Agent Registration API
  slug: spyderbat-agent-registration-api
- description: AgentWork API is intended for use by the UI to convey work & configuration to agents, this data can be specific to an agent or gloal to an organization. An example use case is configuration data for a
  name: Spyderbat Agent Work API
  slug: spyderbat-agentwork-api
- description: An API to allow management of the organizations analytics policies. These will be used throughout the system to take various actions.
  name: Spyderbat Analytics Policy API
  slug: spyderbat-analyticspolicy-api
- description: An API to allow the management of analytics rulesets. Analytics rulesets are used within some types of analytics rulesets.
  name: Spyderbat Analytics Ruleset API
  slug: spyderbat-analyticsruleset-api
- description: Access to raw agent archive data.
  name: Spyderbat Archive API
  slug: spyderbat-archive-api
- description: Cases management API
  name: Spyderbat Cases API
  slug: spyderbat-cases-api
- description: Cluster represents known clusters, such as Kubernetes clusters running an appropriate agent.
  name: Spyderbat Cluster API
  slug: spyderbat-cluster-api
- description: An API to allow the management of custom flags. Custom flags allow users to define custom detections within Spyderbat.
  name: Spyderbat Custom Flag API
  slug: spyderbat-customflag-api
- description: Each source may send fingerprint data which is stored and processed by the system.
  name: Spyderbat Fingerprint Data API
  slug: spyderbat-fingerprintdata-api
- description: An API to allow retrieval of observations for a SIEM.
  name: Spyderbat Forwarded Events API
  slug: spyderbat-forwardedevents-api
- description: Investigations can be created by users as a way to have an investigation into a potential attack, allowing users to associate data from one or more sources into a single investigation. An investigatio
  name: Spyderbat Investigation API
  slug: spyderbat-investigation-api
- description: An API for retrieving, enabling, and disabling notification settings.
  name: Spyderbat Notifications API
  slug: spyderbat-notifications-api
- description: An API for creating, retrieving, updating, and deleting agent health notification settings.
  name: Spyderbat Notifications Agent Health API
  slug: spyderbat-notificationsagenthealth-api
- description: An API to allow the management of notification targets. Notification targets allow users to define where notifications are sent.
  name: Spyderbat Notification Target API
  slug: spyderbat-notificationtarget-api
- description: An API to allow the management of notification templates. Notification templates allow users to define custom notifications within Spyderbat.
  name: Spyderbat Notification Template API
  slug: spyderbat-notificationtemplate-api
- description: Organizations hold resources & data associated with an organization, users must be associated via roles with an organization to have permissions to interact with the organization. Each user my have mu
  name: Spyderbat Org API
  slug: spyderbat-org-api
- description: Organizational types specify both limits and defaults for organizations, they are used by the system to determine the resource utilization for an organization and associated settings.
  name: Spyderbat Org Type API
  slug: spyderbat-orgtype-api
- description: '# Introduction This RBAC model is based off of Amazon''s model with some simplifications and generic assumptions A user has some number of roles on some number of organizations, each role defines some '
  name: Spyderbat RBAC API
  slug: spyderbat-rbac-api
- description: An API to allow the management of saved queries. Saved queries are used to quickly run Athena searches.
  name: Spyderbat Saved Query API
  slug: spyderbat-savedquery-api
- description: An API to allow the management of search sets. Search sets can be used to augment queries in search.
  name: Spyderbat Search Set API
  slug: spyderbat-searchset-api
- description: Sources are used to represent a container for source of security data, such as a machine, or other potential source. The source itself has data associated with the source, see the 'Source Data' APIs f
  name: Spyderbat Source API
  slug: spyderbat-source-api
- description: 'Each source may send data which is stored and processed by the system. So for example a machine will send data in a raw form which is then analyzed, both the raw machine data and the analyzed data is '
  name: Spyderbat Source Data API
  slug: spyderbat-sourcedata-api
- description: A way to execute specific Spyctl logic via the API.
  name: Spyderbat Spyctl API
  slug: spyderbat-spyctl-api
- description: Security Token Service endpoints. Trusted services assume a role on a single org and receive a short-lived, org-locked JWT for downstream consumers. The caller's authority to assume is gated by the st
  name: Spyderbat STS API
  slug: spyderbat-sts-api
- description: An API that provides direct access to Spyderbat's tuning features.
  name: Spyderbat Suppress API
  slug: spyderbat-suppress-api
- description: An API to manage the watchlist for files within an organization.
  name: Spyderbat Watchlist API
  slug: spyderbat-watchlist-api
artifact_total: 35
asyncapis:
- description: ''
  name: Spyderbat Events Webhooks
  slug: spyderbat-events-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://spyderbat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spyderbat.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.spyderbat.com/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.spyderbat.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.spyderbat.com/getting-started/help-and-support
- group: company
  title: ''
  type: Blog
  url: https://spyderbat.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spyderbat
- group: start
  title: ''
  type: SignUp
  url: https://app.spyderbat.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spyderbat.com/privacy-en
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/spyderbat-openapi.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spyderbat-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spyderbat-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/spyderbat-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spyderbat-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spyderbat-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spyderbat-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spyderbat-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spyderbat-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/spyderbat-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spyderbat-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/spyderbat-events-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/spyderbat-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/spyderbat-cli.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/spyderbat-api-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/spyderbat-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spyderbat-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spyderbat-domain-security.yml
created: '2026-08-29'
description: Spyderbat is an Austin, Texas cloud-native runtime security company whose platform delivers cloud detection and response (CDR) for Linux servers, containers and Kubernetes. A lightweight eBPF-based Nano Agent captures kernel-level process, connection, container and Kubernetes activity and streams it into Spyderbat's causal-graph backend, where Spydertraces link related processes, network connections and red flags into scored, attack-path units that analysts can replay at any point in the past. The platform spans Scout (behavioral detection and custom flags), Flashback (time-travel investigations), Guardian (workload and ruleset policies that lock down critical workloads), suppression, notifications, dashboards and SIEM forwarding. Everything the console does is backed by a public REST API at api.prod.spyderbat.com, documented by a published OpenAPI 3.0.1 contract of 197 operations across 30 resource groups, authenticated with a bearer API key bound to an RBAC role. Spyderbat
  also ships a remote Model Context Protocol server, the open-source spyctl CLI, spydertop, and an event forwarder for SIEM integration.
image: https://spyderbat.com/favicon.ico
layout: provider
mcp_servers:
- description: A first-party, provider-hosted Model Context Protocol server that exposes Spyderbat's search, investigation and management surface to MCP-compatible AI clients. Documented and supported by Spyderbat w
  name: Spyderbat MCP Server
  slug: spyderbat-mcp-server
modified: '2026-08-29'
name: Spyderbat
nav: Providers
network: true
overview: 'Spyderbat publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Adhoc Search API, Agent Action API, Agent API, and 26 more. Tagged areas include Company, Security, Cloud Security, Runtime Security, and Cloud Detection and Response.


  The Spyderbat catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Spyderbat''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 21 more developer resources.'
plans:
- name: Spyderbat Plans Pricing
  plan_count: 0
  slug: spyderbat-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Spyderbat Rate Limits
  slug: spyderbat-rate-limits
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 1.2
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 61.9
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 41.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Spyderbat Authentication
  slug: spyderbat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Spyderbat Domain Security
  slug: spyderbat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spyderbat
tags:
- Company
- Security
- Cloud Security
- Runtime Security
- Cloud Detection and Response
- Kubernetes
- Containers
- eBPF
- Linux
- Observability
- Threat Detection
- Incident Response
- DevSecOps
- SIEM
- Monitoring
website: https://spyderbat.com/
---
