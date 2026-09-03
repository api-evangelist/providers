---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 10
  name: Armory Agentic Access
  operation_count: 56
  slug: armory-agentic-access
  summary_line: 56 operations · 10 acting · 10 human-in-the-loop
api_count: 6
apis:
- description: 'Armory Continuous Deployment ships the Spinnaker Gate API as its programmatic interface. Armory documents how to expose it for automation clients on a second Gate port (8085) secured with x509 client '
  name: Armory Continuous Deployment API (Spinnaker Gate)
  slug: armory-cd-gate-api
- baseURL: /
  baseurl_source: spec
  description: The agent-accounts-controller API from Armory — 2 operation(s) for agent-accounts-controller.
  name: Armory Agent Accounts Controller API
  slug: armory-agent-accounts-controller-api
- baseURL: /
  baseurl_source: spec
  description: The applications-controller API from Armory — 2 operation(s) for applications-controller.
  name: Armory Applications Controller API
  slug: armory-applications-controller-api
- baseURL: /
  baseurl_source: spec
  description: The artifact-controller API from Armory — 1 operation(s) for artifact-controller.
  name: Armory Artifact Controller API
  slug: armory-artifact-controller-api
- baseURL: /
  baseurl_source: spec
  description: The cache-controller API from Armory — 2 operation(s) for cache-controller.
  name: Armory Cache Controller API
  slug: armory-cache-controller-api
- baseURL: /
  baseurl_source: spec
  description: The cluster-controller API from Armory — 8 operation(s) for cluster-controller.
  name: Armory Cluster Controller API
  slug: armory-cluster-controller-api
- baseURL: /
  baseurl_source: spec
  description: The credentials-controller API from Armory — 4 operation(s) for credentials-controller.
  name: Armory Credentials Controller API
  slug: armory-credentials-controller-api
- baseURL: /
  baseurl_source: spec
  description: The elastic-ip-controller API from Armory — 1 operation(s) for elastic-ip-controller.
  name: Armory Elastic Ip Controller API
  slug: armory-elastic-ip-controller-api
- baseURL: /
  baseurl_source: spec
  description: The function-controller API from Armory — 1 operation(s) for function-controller.
  name: Armory Function Controller API
  slug: armory-function-controller-api
- baseURL: /
  baseurl_source: spec
  description: The instance-controller API from Armory — 2 operation(s) for instance-controller.
  name: Armory Instance Controller API
  slug: armory-instance-controller-api
- baseURL: /
  baseurl_source: spec
  description: The instance-type-controller API from Armory — 1 operation(s) for instance-type-controller.
  name: Armory Instance Type Controller API
  slug: armory-instance-type-controller-api
- baseURL: /
  baseurl_source: spec
  description: The job-controller API from Armory — 2 operation(s) for job-controller.
  name: Armory Job Controller API
  slug: armory-job-controller-api
- baseURL: /
  baseurl_source: spec
  description: The load-balancer-controller API from Armory — 1 operation(s) for load-balancer-controller.
  name: Armory Load Balancer Controller API
  slug: armory-load-balancer-controller-api
- baseURL: /
  baseurl_source: spec
  description: The network-controller API from Armory — 2 operation(s) for network-controller.
  name: Armory Network Controller API
  slug: armory-network-controller-api
- baseURL: /
  baseurl_source: spec
  description: The operations-controller API from Armory — 7 operation(s) for operations-controller.
  name: Armory Operations Controller API
  slug: armory-operations-controller-api
- baseURL: /
  baseurl_source: spec
  description: The raw-resource-controller API from Armory — 1 operation(s) for raw-resource-controller.
  name: Armory Raw Resource Controller API
  slug: armory-raw-resource-controller-api
- baseURL: /
  baseurl_source: spec
  description: The reservation-report-controller API from Armory — 2 operation(s) for reservation-report-controller.
  name: Armory Reservation Report Controller API
  slug: armory-reservation-report-controller-api
- baseURL: /
  baseurl_source: spec
  description: The search-controller API from Armory — 1 operation(s) for search-controller.
  name: Armory Search Controller API
  slug: armory-search-controller-api
- baseURL: /
  baseurl_source: spec
  description: The security-group-controller API from Armory — 5 operation(s) for security-group-controller.
  name: Armory Security Group Controller API
  slug: armory-security-group-controller-api
- baseURL: /
  baseurl_source: spec
  description: The server-group-controller API from Armory — 2 operation(s) for server-group-controller.
  name: Armory Server Group Controller API
  slug: armory-server-group-controller-api
- baseURL: /
  baseurl_source: spec
  description: The server-group-manager-controller API from Armory — 1 operation(s) for server-group-manager-controller.
  name: Armory Server Group Manager Controller API
  slug: armory-server-group-manager-controller-api
- baseURL: /
  baseurl_source: spec
  description: The subnet-controller API from Armory — 2 operation(s) for subnet-controller.
  name: Armory Subnet Controller API
  slug: armory-subnet-controller-api
- baseURL: /
  baseurl_source: spec
  description: The vpc-controller API from Armory — 1 operation(s) for vpc-controller.
  name: Armory Vpc Controller API
  slug: armory-vpc-controller-api
artifact_total: 50
asyncapis:
- description: ''
  name: Armory Webhooks
  slug: armory-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Armory Scale Agent Dynamic Accounts Agent Accounts Controller API
  slug: open-armory-agent-accounts-controller-api
- collection_type: open
  name: Armory Scale Agent Applications & Clusters Applications Controller API
  slug: open-armory-applications-controller-api
- collection_type: open
  name: Armory Scale Agent Credentials Artifact Controller API
  slug: open-armory-artifact-controller-api
- collection_type: open
  name: Armory Scale Agent Operations & Tasks Cache Controller API
  slug: open-armory-cache-controller-api
- collection_type: open
  name: Armory Scale Agent Applications & Clusters Cluster Controller API
  slug: open-armory-cluster-controller-api
- collection_type: open
  name: Armory Scale Agent Credentials Credentials Controller API
  slug: open-armory-credentials-controller-api
- collection_type: open
  name: Armory Scale Agent Infrastructure Elastic Ip Controller API
  slug: open-armory-elastic-ip-controller-api
- collection_type: open
  name: Armory Scale Agent Applications & Clusters Function Controller API
  slug: open-armory-function-controller-api
- collection_type: open
  name: Armory Scale Agent Applications & Clusters Instance Controller API
  slug: open-armory-instance-controller-api
- collection_type: open
  name: Armory Scale Agent Infrastructure Instance Type Controller API
  slug: open-armory-instance-type-controller-api
- collection_type: open
  name: Armory Scale Agent Applications & Clusters Job Controller API
  slug: open-armory-job-controller-api
- collection_type: open
  name: Armory Scale Agent Applications & Clusters Load Balancer Controller API
  slug: open-armory-load-balancer-controller-api
- collection_type: open
  name: Armory Scale Agent Infrastructure Network Controller API
  slug: open-armory-network-controller-api
- collection_type: open
  name: Armory Scale Agent Operations & Tasks Operations Controller API
  slug: open-armory-operations-controller-api
- collection_type: open
  name: Armory Scale Agent Applications & Clusters Raw Resource Controller API
  slug: open-armory-raw-resource-controller-api
- collection_type: open
  name: Armory Scale Agent Infrastructure Reservation Report Controller API
  slug: open-armory-reservation-report-controller-api
- collection_type: open
  name: Armory Scale Agent Infrastructure Search Controller API
  slug: open-armory-search-controller-api
- collection_type: open
  name: Armory Scale Agent Infrastructure Security Group Controller API
  slug: open-armory-security-group-controller-api
- collection_type: open
  name: Armory Scale Agent Applications & Clusters Server Group Controller API
  slug: open-armory-server-group-controller-api
- collection_type: open
  name: Armory Scale Agent Applications & Clusters Server Group Manager Controller API
  slug: open-armory-server-group-manager-controller-api
- collection_type: open
  name: Armory Scale Agent Infrastructure Subnet Controller API
  slug: open-armory-subnet-controller-api
- collection_type: open
  name: Armory Scale Agent Infrastructure Vpc Controller API
  slug: open-armory-vpc-controller-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/armory/docs/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/armory/docs/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/armory/docs/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://docs.armory.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.armory.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.armory.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.armory.io/plugins/scale-agent/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.armory.io/plugins/scale-agent/install/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://support.armory.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/armory
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/armory-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.armory.io/continuous-deployment/release-notes/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/armory-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/armory-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/armory-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/armory-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/armory-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/armory-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/armory-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.armory.io/continuous-deployment/feature-status/deprecations/
- group: other
  title: ''
  type: Overlay
  url: overlays/armory-scale-agent-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/armory-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/armory-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/armory-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/armory-cli.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/armory-webhooks.yml
- group: agent
  title: ''
  type: MCPCandidate
  url: mcp/armory-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/armory-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/armory-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/armory-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/armory-domain-security.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/armory
- group: other
  title: ''
  type: DockerHub
  url: https://hub.docker.com/u/armory
- group: operate
  title: ''
  type: Community
  url: https://join.slack.com/t/spinnakerteam/shared_invite/zt-7juwxmx0-nQ4Ud4pJcbuPykX3SXwQrg
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cloudarmory
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC9ESNuSCMXLsdRdBDhjSzcA/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/armory_stock/
created: '2026-08-06'
description: Armory, Inc. is a San Mateo, California software company founded in 2016 that built and sold an enterprise distribution of the open source Spinnaker continuous delivery platform. Its product line covered Armory Continuous Deployment (self-hosted and Armory-managed Spinnaker), Armory Continuous Deployment-as-a-Service, and a set of proprietary Spinnaker plugins - the Armory Scale Agent for Spinnaker and Kubernetes, Pipelines-as-Code (Dinghy), an OPA-backed Policy Engine, Terraform Integration, GitHub Integration and AWS Event Cache. Armory raised more than $82M including a $40M Series C, and its assets were acquired by Harness in January 2024. www.armory.io now redirects to harness.io, but docs.armory.io remains live and still publishes the full product documentation plus a real Swagger 2.0 API reference for the Armory Scale Agent Clouddriver surface.
image: https://docs.armory.io/favicons/android-192x192.png
layout: provider
modified: '2026-08-06'
name: Armory
nav: Providers
network: true
overview: 'Armory publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Agent Accounts Controller API, Applications Controller API, Artifact Controller API, and 19 more. Tagged areas include Continuous Delivery, Spinnaker, Kubernetes, DevOps, and Deployment Automation.


  The Armory catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Armory''s developer surface includes documentation, API reference, getting-started guide, support, changelog, release notes, authentication, and 31 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 20
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 53.0
    developer_ergonomics: 68.5
    discoverability: 64.8
    governance: 4.5
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 25.0
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/armory/refs/heads/main/screenshots/armory-2026-08-07T161731.png
security:
- kind: authentication
  name: Armory Authentication
  slug: armory-authentication
  summary_line: mutualTLS/x509/oauth2/saml/ldap/basic · 4 schemes
- kind: domain-security
  name: Armory Domain Security
  slug: armory-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: armory
tags:
- Continuous Delivery
- Spinnaker
- Kubernetes
- DevOps
- Deployment Automation
- Multi-Cloud
- Pipelines
- Developer Tools
- Plugins
- Continuous Deployment
website: https://docs.armory.io/
---
