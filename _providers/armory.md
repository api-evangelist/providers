---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 10
  name: Armory Agentic Access
  operation_count: 56
  slug: armory-agentic-access
  summary_line: 56 operations · 10 acting · 10 human-in-the-loop
api_count: 2
apis:
- description: REST surface exposed by Clouddriver when the Armory Scale Agent plugin is installed. Covers the Armory-specific Dynamic Accounts endpoints (/agents/kubernetes/accounts) alongside the Clouddriver appli
  name: Armory Scale Agent API
  slug: armory-scale-agent-api
- description: 'Armory Continuous Deployment ships the Spinnaker Gate API as its programmatic interface. Armory documents how to expose it for automation clients on a second Gate port (8085) secured with x509 client '
  name: Armory Continuous Deployment API (Spinnaker Gate)
  slug: armory-cd-gate-api
artifact_total: 6
asyncapis:
- description: ''
  name: Armory Webhooks
  slug: armory-webhooks
common:
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
overview: 'Armory publishes 1 API on the [APIs.io](https://apis.io/) network: Scale Agent API. Tagged areas include Continuous Delivery, Spinnaker, Kubernetes, DevOps, and Deployment Automation.


  The Armory catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Armory''s developer surface includes documentation, API reference, getting-started guide, support, changelog, release notes, authentication, and 28 more developer resources.'
random_paper: 101
score:
  band: developing
  composite: 42.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 54.3
    developer_ergonomics: 69.6
    discoverability: 77.8
    governance: 20.8
    operational_transparency: 36.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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
