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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Docker Hub Agentic Access
  operation_count: 54
  slug: docker-hub-agentic-access
  summary_line: 54 operations · 27 acting
api_count: 10
apis:
- description: The Personal Access Token endpoints lets you manage personal access tokens. For more information, see [Access Tokens](https://docs.docker.com/security/access-tokens/). You can use a personal access to
  name: Docker Hub access-tokens API
  slug: docker-hub-access-tokens-api
- description: The Audit Logs API endpoints allow you to query audit log events across a namespace. For more information, see [Audit Logs](https://docs.docker.com/admin/activity-logs/).
  name: Docker Hub audit-logs API
  slug: docker-hub-audit-logs-api
- description: The authentication endpoints allow you to authenticate with Docker Hub APIs. For more information, see [Authentication](#tag/authentication).
  name: Docker Hub authentication-api API
  slug: docker-hub-authentication-api-api
- description: The groups endpoints allow you to manage your organization's teams and their members. For more information, see [Create and manage a team](https://docs.docker.com/admin/organization/manage/manage-a-te
  name: Docker Hub groups API
  slug: docker-hub-groups-api
- description: The invites endpoints allow you to manage invites for users to join your Docker organization. For more information, see [Invite members](https://docs.docker.com/admin/organization/manage/members/#invi
  name: Docker Hub invites API
  slug: docker-hub-invites-api
- description: The organization access token endpoints allow you to manage organization access tokens (OATs). See [Organization access tokens](https://docs.docker.com/security/for-admins/access-tokens/) for more inf
  name: Docker Hub org-access-tokens API
  slug: docker-hub-org-access-tokens-api
- description: The Org Settings API endpoints allow you to manage your organization's settings.
  name: Docker Hub org-settings API
  slug: docker-hub-org-settings-api
- description: The organization endpoints allow you to interact with and manage your organizations. For more information, see [Organization administration overview](https://docs.docker.com/admin/organization/).
  name: Docker Hub orgs API
  slug: docker-hub-orgs-api
- description: The repository endpoints allow you to access your repository's tags.
  name: Docker Hub repositories API
  slug: docker-hub-repositories-api
- description: SCIM is a provisioning system that lets you manage users within your identity provider (IdP). For more information, see [System for Cross-domain Identity management](https://docs.docker.com/security/f
  name: Docker Hub scim API
  slug: docker-hub-scim-api
artifact_total: 18
collections:
- collection_type: open
  name: Docker HUB API
  slug: open-docker-hub
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/docker-hub-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/docker-hub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/docker-hub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/docker-hub-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://hub.docker.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.docker.com/docker-hub/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.docker.com/docker-hub/api/latest/
- group: start
  title: ''
  type: Signup
  url: https://hub.docker.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://hub.docker.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.docker.com/docker-hub/release-notes/
- group: company
  title: ''
  type: Blog
  url: https://www.docker.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.docker.com/support/
- group: operate
  title: ''
  type: Forums
  url: https://forums.docker.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.docker.com/legal/docker-terms-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.docker.com/legal/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.docker.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/docker
- group: other
  title: ''
  type: X
  url: https://x.com/Docker
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/docker
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/dockerrun
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.docker.com/llms.txt
created: '2024-01-01'
description: Docker Hub is the world's largest container image registry, providing a cloud-based service for finding, storing, sharing, and managing container images. It offers public and private repositories, automated builds, webhooks, and integrations with Docker tooling and CI/CD pipelines.
finops:
- name: Docker Hub Finops
  service_category: API
  slug: docker-hub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/docker-hub.png
layout: provider
modified: '2026-05-19'
name: Docker Hub
nav: Providers
network: true
overview: 'Docker Hub publishes 10 APIs on the [APIs.io](https://apis.io/) network, including access-tokens API, audit-logs API, authentication-api API, and 7 more. Tagged areas include Containers, DevOps, Docker, and Registry.


  Docker Hub''s developer surface includes authentication, documentation, signup flow, pricing, changelog, engineering blog, support, and 14 more developer resources.'
plans:
- name: Docker Hub Plans Pricing
  plan_count: 3
  slug: docker-hub-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Docker Hub Rate Limits
  slug: docker-hub-rate-limits
score:
  band: developing
  composite: 47.7
  delta: -2.2
  facets:
    commercial_clarity: 71.1
    contract_quality: 53.9
    developer_ergonomics: 26.1
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 49.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/docker-hub/refs/heads/main/screenshots/docker-hub-2026-06-20T180106.png
security:
- kind: authentication
  name: Docker Hub Authentication
  slug: docker-hub-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Docker Hub Domain Security
  slug: docker-hub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Docker Hub Vulnerability Disclosure
  slug: docker-hub-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: docker-hub
tags:
- Containers
- DevOps
- Docker
- Registry
website: https://hub.docker.com/
---
