---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 129
  human_in_the_loop: 7
  name: Portainer Agentic Access
  operation_count: 237
  slug: portainer-agentic-access
  summary_line: 237 operations · 129 acting · 7 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Authenticate against Portainer HTTP API
  name: Portainer auth API
  slug: portainer-auth-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage backups
  name: Portainer backup API
  slug: portainer-backup-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Custom Templates
  name: Portainer custom_templates API
  slug: portainer-custom-templates-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Docker resources
  name: Portainer docker API
  slug: portainer-docker-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Edge related environment(endpoint) settings
  name: Portainer edge API
  slug: portainer-edge-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Edge Groups
  name: Portainer edge_groups API
  slug: portainer-edge-groups-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Edge Jobs
  name: Portainer edge_jobs API
  slug: portainer-edge-jobs-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Edge Stacks
  name: Portainer edge_stacks API
  slug: portainer-edge-stacks-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage environment(endpoint) groups
  name: Portainer endpoint_groups API
  slug: portainer-endpoint-groups-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Docker environments(endpoints)
  name: Portainer endpoints API
  slug: portainer-endpoints-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Operate git repository
  name: Portainer gitops API
  slug: portainer-gitops-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Helm charts
  name: Portainer helm API
  slug: portainer-helm-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Intel AMT settings
  name: Portainer intel API
  slug: portainer-intel-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Kubernetes cluster
  name: Portainer kubernetes API
  slug: portainer-kubernetes-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage LDAP settings
  name: Portainer ldap API
  slug: portainer-ldap-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Fetch the message of the day
  name: Portainer motd API
  slug: portainer-motd-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Docker registries
  name: Portainer registries API
  slug: portainer-registries-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage access control on Docker resources
  name: Portainer resource_controls API
  slug: portainer-resource-controls-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage roles
  name: Portainer roles API
  slug: portainer-roles-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Portainer settings
  name: Portainer settings API
  slug: portainer-settings-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage ssl settings
  name: Portainer ssl API
  slug: portainer-ssl-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage stacks
  name: Portainer stacks API
  slug: portainer-stacks-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Information about the Portainer instance
  name: Portainer status API
  slug: portainer-status-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Portainer system
  name: Portainer system API
  slug: portainer-system-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage tags
  name: Portainer tags API
  slug: portainer-tags-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage team memberships
  name: Portainer team_memberships API
  slug: portainer-team-memberships-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage teams
  name: Portainer teams API
  slug: portainer-teams-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage App Templates
  name: Portainer templates API
  slug: portainer-templates-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Upload files
  name: Portainer upload API
  slug: portainer-upload-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage users
  name: Portainer users API
  slug: portainer-users-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage webhooks
  name: Portainer webhooks API
  slug: portainer-webhooks-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Create exec sessions using websockets
  name: Portainer websocket API
  slug: portainer-websocket-api
artifact_total: 72
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PortainerCE auth API
  slug: open-portainer-auth-api
- collection_type: open
  name: PortainerCE auth backup API
  slug: open-portainer-backup-api
- collection_type: open
  name: PortainerCE auth custom_templates API
  slug: open-portainer-custom-templates-api
- collection_type: open
  name: PortainerCE auth docker API
  slug: open-portainer-docker-api
- collection_type: open
  name: PortainerCE auth edge API
  slug: open-portainer-edge-api
- collection_type: open
  name: PortainerCE auth edge_groups API
  slug: open-portainer-edge-groups-api
- collection_type: open
  name: PortainerCE auth edge_jobs API
  slug: open-portainer-edge-jobs-api
- collection_type: open
  name: PortainerCE auth edge_stacks API
  slug: open-portainer-edge-stacks-api
- collection_type: open
  name: PortainerCE auth endpoint_groups API
  slug: open-portainer-endpoint-groups-api
- collection_type: open
  name: PortainerCE auth endpoints API
  slug: open-portainer-endpoints-api
- collection_type: open
  name: PortainerCE auth gitops API
  slug: open-portainer-gitops-api
- collection_type: open
  name: PortainerCE auth helm API
  slug: open-portainer-helm-api
- collection_type: open
  name: PortainerCE auth intel API
  slug: open-portainer-intel-api
- collection_type: open
  name: PortainerCE auth kubernetes API
  slug: open-portainer-kubernetes-api
- collection_type: open
  name: PortainerCE auth ldap API
  slug: open-portainer-ldap-api
- collection_type: open
  name: PortainerCE auth motd API
  slug: open-portainer-motd-api
- collection_type: open
  name: PortainerCE auth registries API
  slug: open-portainer-registries-api
- collection_type: open
  name: PortainerCE auth resource_controls API
  slug: open-portainer-resource-controls-api
- collection_type: open
  name: PortainerCE auth roles API
  slug: open-portainer-roles-api
- collection_type: open
  name: PortainerCE auth settings API
  slug: open-portainer-settings-api
- collection_type: open
  name: PortainerCE auth ssl API
  slug: open-portainer-ssl-api
- collection_type: open
  name: PortainerCE auth stacks API
  slug: open-portainer-stacks-api
- collection_type: open
  name: PortainerCE auth status API
  slug: open-portainer-status-api
- collection_type: open
  name: PortainerCE auth system API
  slug: open-portainer-system-api
- collection_type: open
  name: PortainerCE auth tags API
  slug: open-portainer-tags-api
- collection_type: open
  name: PortainerCE auth team_memberships API
  slug: open-portainer-team-memberships-api
- collection_type: open
  name: PortainerCE auth teams API
  slug: open-portainer-teams-api
- collection_type: open
  name: PortainerCE auth templates API
  slug: open-portainer-templates-api
- collection_type: open
  name: PortainerCE auth upload API
  slug: open-portainer-upload-api
- collection_type: open
  name: PortainerCE auth users API
  slug: open-portainer-users-api
- collection_type: open
  name: PortainerCE auth webhooks API
  slug: open-portainer-webhooks-api
- collection_type: open
  name: PortainerCE auth websocket API
  slug: open-portainer-websocket-api
- collection_type: open
  name: PortainerCE API
  slug: open-portainer
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/portainer/portainer/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/portainer/portainer/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/portainer/portainer/blob/develop/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/portainer/portainer/blob/develop/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/portainer/portainer/blob/develop/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/portainer/portainer/blob/develop/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/portainer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/portainer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/portainer-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/portainer
- group: company
  title: ''
  type: Website
  url: https://www.portainer.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.portainer.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.portainer.io/
- group: company
  title: ''
  type: Blog
  url: https://www.portainer.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.portainer.io/pricing
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/portainer
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/portainer/portainer
- group: operate
  title: ''
  type: Community
  url: https://www.portainer.io/community
- group: operate
  title: ''
  type: Slack
  url: https://www.portainer.io/slack
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.portainer.io/llms.txt
created: '2026-03-26'
description: Portainer is an open source container management platform that simplifies deploying, managing, and monitoring Docker, Swarm, Podman, and Kubernetes environments through a unified web UI and REST API.
finops:
- name: Portainer Finops
  service_category: API
  slug: portainer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/portainer.png
layout: provider
modified: '2026-05-19'
name: Portainer
nav: Providers
network: true
overview: 'Portainer publishes 32 APIs on the [APIs.io](https://apis.io/) network, including auth API, backup API, custom_templates API, and 29 more. Tagged areas include Container Management, Containers, Docker, and Kubernetes.


  Portainer''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Portainer Plans Pricing
  plan_count: 3
  slug: portainer-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Portainer Rate Limits
  slug: portainer-rate-limits
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 56.4
    developer_ergonomics: 38.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 32
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/portainer/refs/heads/main/screenshots/portainer-2026-06-20T191931.png
security:
- kind: authentication
  name: Portainer Authentication
  slug: portainer-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Portainer Domain Security
  slug: portainer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: portainer
tags:
- Container Management
- Containers
- Docker
- Kubernetes
website: https://www.portainer.io/
---
