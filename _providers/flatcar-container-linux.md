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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 28.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Flatcar Container Linux Agentic Access
  operation_count: 40
  slug: flatcar-container-linux-agentic-access
  summary_line: 40 operations · 17 acting
api_count: 8
apis:
- description: The Activity API from Flatcar Container Linux — 1 operation(s) for activity.
  name: Flatcar Container Linux Activity API
  slug: flatcar-container-linux-activity-api
- description: The Apps API from Flatcar Container Linux — 17 operation(s) for apps.
  name: Flatcar Container Linux Apps API
  slug: flatcar-container-linux-apps-api
- description: The Channels API from Flatcar Container Linux — 2 operation(s) for channels.
  name: Flatcar Container Linux Channels API
  slug: flatcar-container-linux-channels-api
- description: The Config API from Flatcar Container Linux — 1 operation(s) for config.
  name: Flatcar Container Linux Config API
  slug: flatcar-container-linux-config-api
- description: The Health API from Flatcar Container Linux — 1 operation(s) for health.
  name: Flatcar Container Linux Health API
  slug: flatcar-container-linux-health-api
- description: The Instances API from Flatcar Container Linux — 1 operation(s) for instances.
  name: Flatcar Container Linux Instances API
  slug: flatcar-container-linux-instances-api
- description: The Login API from Flatcar Container Linux — 3 operation(s) for login.
  name: Flatcar Container Linux Login API
  slug: flatcar-container-linux-login-api
- description: The Update API from Flatcar Container Linux — 1 operation(s) for update.
  name: Flatcar Container Linux Update API
  slug: flatcar-container-linux-update-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nebraska Activity API
  slug: open-flatcar-container-linux-activity-api
- collection_type: open
  name: Nebraska Activity Apps API
  slug: open-flatcar-container-linux-apps-api
- collection_type: open
  name: Nebraska Activity Channels API
  slug: open-flatcar-container-linux-channels-api
- collection_type: open
  name: Nebraska Activity Config API
  slug: open-flatcar-container-linux-config-api
- collection_type: open
  name: Nebraska Activity Health API
  slug: open-flatcar-container-linux-health-api
- collection_type: open
  name: Nebraska Activity Instances API
  slug: open-flatcar-container-linux-instances-api
- collection_type: open
  name: Nebraska Activity Login API
  slug: open-flatcar-container-linux-login-api
- collection_type: open
  name: Nebraska Activity Update API
  slug: open-flatcar-container-linux-update-api
- collection_type: open
  name: Nebraska
  slug: open-nebraska-update-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/flatcar/nebraska/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/flatcar/nebraska/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/flatcar/nebraska/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/flatcar/nebraska/blob/main/code-of-conduct.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/flatcar/nebraska/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/flatcar/nebraska/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flatcar-container-linux-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flatcar-container-linux-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flatcar-container-linux-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.flatcar.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.flatcar.org/docs/latest/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flatcar
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/flatcar/flatcar
- group: other
  title: ''
  type: NebraskaSource
  url: https://github.com/flatcar/nebraska
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.flatcar.org/releases/
- group: operate
  title: ''
  type: Community
  url: https://www.flatcar.org/community/
- group: company
  title: ''
  type: Blog
  url: https://www.flatcar.org/blog/index.xml
created: '2026-03-16'
description: Flatcar Container Linux is a CNCF incubating minimal, immutable Linux distribution designed for running containers. It provides automatic atomic updates through the Nebraska update server, ensuring nodes stay secure and consistent. Flatcar supports Kubernetes deployments on bare metal, cloud, and virtual environments with a focus on security and operational simplicity.
finops:
- name: Flatcar Container Linux Finops
  service_category: API
  slug: flatcar-container-linux-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flatcar-container-linux.png
layout: provider
modified: '2026-05-19'
name: Flatcar Container Linux
nav: Providers
network: true
overview: 'Flatcar Container Linux publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Activity API, Apps API, Channels API, and 5 more. Tagged areas include Cloud-Native, Containers, Immutable Infrastructure, Incubating, and Linux.


  Flatcar Container Linux''s developer surface includes authentication, documentation, release notes, engineering blog, and 13 more developer resources.'
plans:
- name: Flatcar Container Linux Plans Pricing
  plan_count: 3
  slug: flatcar-container-linux-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Flatcar Container Linux Rate Limits
  slug: flatcar-container-linux-rate-limits
score:
  band: thin
  composite: 32.4
  delta: 0.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 47.3
    developer_ergonomics: 26.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 31.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flatcar-container-linux/refs/heads/main/screenshots/flatcar-container-linux-2026-06-20T181304.png
security:
- kind: authentication
  name: Flatcar Container Linux Authentication
  slug: flatcar-container-linux-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Flatcar Container Linux Domain Security
  slug: flatcar-container-linux-domain-security
  summary_line: TLSv1.3 · HSTS
slug: flatcar-container-linux
tags:
- Cloud-Native
- Containers
- Immutable Infrastructure
- Incubating
- Linux
- Operating System
website: https://www.flatcar.org
---
