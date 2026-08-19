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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: REST API for accessing and managing Project Online data, including projects, tasks, resources, and assignments.
  name: Microsoft Project Online API
  slug: microsoft-project-online-api
- description: Microsoft Graph API for Project for the web, enabling access to projects, tasks, and bucket management.
  name: Microsoft Graph Project API
  slug: microsoft-graph-project-api
- description: Client-Side Object Model (CSOM) API for Project Server, providing programmatic access to Project Server data.
  name: Microsoft Project Server CSOM API
  slug: microsoft-project-server-csom-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ms-projects-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ms-projects-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/project-blog/bg-p/ProjectBlog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.microsoft.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/servicesagreement
created: '2024-01-15'
description: APIs for Microsoft Project, including Project for the web, Project Online, and Project Server.
finops:
- name: Ms Projects Finops
  service_category: API
  slug: ms-projects-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ms-projects.png
layout: provider
modified: '2026-04-28'
name: Microsoft Project APIs
nav: Providers
network: true
overview: 'Microsoft Project APIs publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Microsoft 365, Project Management, Resources, and Scheduling.


  Microsoft Project APIs'' developer surface includes developer portal, engineering blog, and 6 more developer resources.'
plans:
- name: Ms Projects Plans Pricing
  plan_count: 3
  slug: ms-projects-plans-pricing
random_paper: 100
rate_limits:
- limit_count: 5
  name: Ms Projects Rate Limits
  slug: ms-projects-rate-limits
score:
  band: emerging
  composite: 18.4
  delta: -1.2
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 19.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ms-projects/refs/heads/main/screenshots/ms-projects-2026-06-20T185849.png
security:
- kind: domain-security
  name: Ms Projects Domain Security
  slug: ms-projects-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ms Projects Vulnerability Disclosure
  slug: ms-projects-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ms-projects
tags:
- Collaboration
- Microsoft 365
- Project Management
- Resources
- Scheduling
- Tasks
website: https://developer.microsoft.com/
---
