---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 62
  human_in_the_loop: 4
  name: Docker Agentic Access
  operation_count: 107
  slug: docker-agentic-access
  summary_line: 107 operations · 62 acting · 4 human-in-the-loop
api_count: 15
apis:
- description: Configs are application configurations that can be used by services. Swarm mode must be enabled for these endpoints to work.
  name: Docker Config API
  slug: docker-config-api
- description: Create and manage containers.
  name: Docker Container API
  slug: docker-container-api
- description: The Distribution API from Docker — 1 operation(s) for distribution.
  name: Docker Distribution API
  slug: docker-distribution-api
- description: Run new commands inside running containers. Refer to the [command-line reference](https://docs.docker.com/engine/reference/commandline/exec/) for more information. To exec a command in a container, yo
  name: Docker Exec API
  slug: docker-exec-api
- description: The Image API from Docker — 15 operation(s) for image.
  name: Docker Image API
  slug: docker-image-api
- description: Networks are user-defined networks that containers can be attached to. See the [networking documentation](https://docs.docker.com/network/) for more information.
  name: Docker Network API
  slug: docker-network-api
- description: Nodes are instances of the Engine participating in a swarm. Swarm mode must be enabled for these endpoints to work.
  name: Docker Node API
  slug: docker-node-api
- description: The Plugin API from Docker — 11 operation(s) for plugin.
  name: Docker Plugin API
  slug: docker-plugin-api
- description: Secrets are sensitive data that can be used by services. Swarm mode must be enabled for these endpoints to work.
  name: Docker Secret API
  slug: docker-secret-api
- description: Services are the definitions of tasks to run on a swarm. Swarm mode must be enabled for these endpoints to work.
  name: Docker Service API
  slug: docker-service-api
- description: The Session API from Docker — 1 operation(s) for session.
  name: Docker Session API
  slug: docker-session-api
- description: Engines can be clustered together in a swarm. Refer to the [swarm mode documentation](https://docs.docker.com/engine/swarm/) for more information.
  name: Docker Swarm API
  slug: docker-swarm-api
- description: The System API from Docker — 6 operation(s) for system.
  name: Docker System API
  slug: docker-system-api
- description: A task is a container running on a swarm. It is the atomic scheduling unit of swarm. Swarm mode must be enabled for these endpoints to work.
  name: Docker Task API
  slug: docker-task-api
- description: Create and manage persistent storage that can be attached to containers.
  name: Docker Volume API
  slug: docker-volume-api
arazzos:
- description: Check registry credentials, build an image from a build context, tag it for a registry, and push it.
  name: Docker Build, Tag, and Push an Image
  slug: docker-build-and-push-image-workflow
- description: Pause a running container, commit its filesystem to a new image, unpause it, and tag the snapshot for a registry.
  name: Docker Snapshot a Running Container as an Image
  slug: docker-commit-container-to-image-workflow
- description: Confirm the node is in a swarm, create a secret, deploy a replicated service that mounts it, and watch the tasks converge.
  name: Docker Deploy a Replicated Swarm Service with a Secret
  slug: docker-deploy-swarm-service-workflow
- description: Confirm a container is running, create an exec instance, start it, and read back the command exit code.
  name: Docker Run a Command Inside a Running Container
  slug: docker-exec-command-in-container-workflow
- description: Read the privileges a plugin demands, install it with those privileges acknowledged, enable it, and confirm it is running.
  name: Docker Review Privileges and Install a Plugin
  slug: docker-install-plugin-workflow
- description: Create a user-defined bridge network, create a container, connect it with an alias, start it, and verify the attachment.
  name: Docker Create a Network and Attach a Container
  slug: docker-provision-network-workflow
- description: Create a named volume, create a container that binds it to a mount path, start the container, and confirm the volume is in use.
  name: Docker Create a Volume and Mount It Into a Container
  slug: docker-provision-volume-workflow
- description: Measure disk usage, prune stopped containers, dangling images, unused volumes and networks, and the build cache, then measure again.
  name: Docker Reclaim Disk Space on a Host
  slug: docker-reclaim-disk-space-workflow
- description: Read a service's current version, update it to a new image, watch the tasks reconverge, and tail the service logs.
  name: Docker Roll a Swarm Service Onto a New Image
  slug: docker-rolling-update-service-workflow
- description: Pull an image from a registry, create a container from it, start it, and read back its running state.
  name: Docker Pull an Image and Run a Container
  slug: docker-run-container-workflow
- description: Search the registry for an official image, pull it, then inspect its metadata and layer history before use.
  name: Docker Search, Pull, and Vet an Image
  slug: docker-search-and-pull-image-workflow
- description: Find a container by name, stop it gracefully, wait for it to exit, and remove it with its anonymous volumes.
  name: Docker Stop and Remove a Container
  slug: docker-stop-and-remove-container-workflow
- description: Gather the full diagnostic picture for a container — state, logs, processes, resource stats, and filesystem drift.
  name: Docker Troubleshoot a Failing Container
  slug: docker-troubleshoot-container-workflow
artifact_total: 53
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Docker Engine Config API
  slug: open-docker-config-api
- collection_type: open
  name: Docker Engine Config Container API
  slug: open-docker-container-api
- collection_type: open
  name: Docker Engine Config Distribution API
  slug: open-docker-distribution-api
- collection_type: open
  name: Docker Engine Config Exec API
  slug: open-docker-exec-api
- collection_type: open
  name: Docker Engine Config Image API
  slug: open-docker-image-api
- collection_type: open
  name: Docker Engine Config Network API
  slug: open-docker-network-api
- collection_type: open
  name: Docker Engine Config Node API
  slug: open-docker-node-api
- collection_type: open
  name: Docker Engine Config Plugin API
  slug: open-docker-plugin-api
- collection_type: open
  name: Docker Engine Config Secret API
  slug: open-docker-secret-api
- collection_type: open
  name: Docker Engine Config Service API
  slug: open-docker-service-api
- collection_type: open
  name: Docker Engine Config Session API
  slug: open-docker-session-api
- collection_type: open
  name: Docker Engine Config Swarm API
  slug: open-docker-swarm-api
- collection_type: open
  name: Docker Engine Config System API
  slug: open-docker-system-api
- collection_type: open
  name: Docker Engine Config Task API
  slug: open-docker-task-api
- collection_type: open
  name: Docker Engine Config Volume API
  slug: open-docker-volume-api
- collection_type: open
  name: Docker Engine API
  slug: open-docker
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/docker-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/docker-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/docker-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/docker
- group: company
  title: ''
  type: Website
  url: https://www.docker.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.docker.com/
- group: company
  title: ''
  type: Blog
  url: https://www.docker.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/docker
- group: commercial
  title: ''
  type: Pricing
  url: https://www.docker.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://hub.docker.com/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://www.dockerstatus.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.docker.com/legal/docker-terms-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.docker.com/legal/privacy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/docker
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/docker/mcp-gateway
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.docker.com/llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/docker-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/docker-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/docker-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/docker-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/docker-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/docker-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/docker-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/docker-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/docker-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/docker-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/docker-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/docker-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/docker-data-model.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docker-run-container-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docker-stop-and-remove-container-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docker-build-and-push-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docker-exec-command-in-container-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docker-troubleshoot-container-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docker-search-and-pull-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docker-provision-network-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docker-provision-volume-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docker-deploy-swarm-service-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docker-rolling-update-service-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docker-reclaim-disk-space-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docker-commit-container-to-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docker-install-plugin-workflow.yml
created: '2025-06-05'
description: Docker is a platform for developers and sysadmins to build, share, and run applications in containers, packaging code and dependencies together for consistent deployment across environments.
finops:
- name: Docker Finops
  service_category: API
  slug: docker-finops
image: https://www.docker.com/sites/default/files/d8/2019-07/docker-logo-blue.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: 'Docker publishes first-party MCP infrastructure: the Docker MCP Gateway (a `docker mcp` CLI plugin that runs, secures, and orchestrates MCP servers as containers), the Docker MCP Catalog (200+ verifie'
  name: Docker MCP (artifact)
  slug: docker-mcp-artifact
modified: '2026-06-20'
name: Docker
nav: Providers
network: true
overview: 'Docker publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Config API, Container API, Distribution API, and 12 more. Tagged areas include Cloud, Containers, DevOps, Infrastructure, and Microservices.


  Docker''s developer surface includes documentation, engineering blog, pricing, signup flow, changelog, CLI, and 36 more developer resources.'
plans:
- name: Docker Plans Pricing
  plan_count: 3
  slug: docker-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Docker Rate Limits
  slug: docker-rate-limits
score:
  band: developing
  composite: 43.2
  delta: 2.4
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 16.7
    contract_quality: 40.0
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 16.7
    operational_transparency: 42.1
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/docker/refs/heads/main/screenshots/docker-2026-06-20T180111.png
security:
- kind: domain-security
  name: Docker Domain Security
  slug: docker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Docker Vulnerability Disclosure
  slug: docker-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: docker
tags:
- Cloud
- Containers
- DevOps
- Infrastructure
- Microservices
website: https://www.docker.com/
---
