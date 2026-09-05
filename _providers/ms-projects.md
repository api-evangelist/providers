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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-09-04'
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
overview: 'Microsoft Project APIs publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Microsoft-365, Project Management, Resources, and Scheduling.


  Microsoft Project APIs'' developer surface includes developer portal, engineering blog, and 6 more developer resources.'
plans:
- name: Ms Projects Plans Pricing
  plan_count: 3
  slug: ms-projects-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Ms Projects Rate Limits
  slug: ms-projects-rate-limits
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 40.5
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 25.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Microsoft-365
- Project Management
- Resources
- Scheduling
- Task
website: https://developer.microsoft.com/
---
