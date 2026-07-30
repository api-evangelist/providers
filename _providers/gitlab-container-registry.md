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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Gitlab Container Registry Agentic Access
  operation_count: 8
  slug: gitlab-container-registry-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 2
apis:
- description: Container registry repositories
  name: GitLab Container Registry Repositories API
  slug: gitlab-container-registry-repositories-api
- description: Container image tags
  name: GitLab Container Registry Tags API
  slug: gitlab-container-registry-tags-api
artifact_total: 13
collections:
- collection_type: open
  name: GitLab Container Registry API
  slug: open-gitlab-container-registry
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gitlab-container-registry-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gitlab-container-registry-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gitlab-container-registry-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gitlab-container-registry-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gitlab-container-registry-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gitlab-container-registry-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://docs.gitlab.com/user/packages/container_registry/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gitlab.com/user/packages/container_registry/
- group: docs
  title: ''
  type: API Documentation
  url: https://docs.gitlab.com/api/container_registry/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://gitlab.com/gitlab-org
- group: commercial
  title: ''
  type: Pricing
  url: https://about.gitlab.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gitlab.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.gitlab.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://about.gitlab.com/atom.xml
created: '2026-03-26'
description: GitLab Container Registry is a built-in container registry that allows users to store Docker images alongside their code in GitLab repositories. It exposes a REST API for managing image repositories, tags, and cleanup policies.
finops:
- name: Gitlab Container Registry Finops
  service_category: API
  slug: gitlab-container-registry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gitlab-container-registry.png
layout: provider
modified: '2026-05-19'
name: GitLab Container Registry
nav: Providers
network: true
overview: 'GitLab Container Registry publishes 2 APIs on the [APIs.io](https://apis.io/) network: Repositories API and Tags API. Tagged areas include Container Images, Containers, GitLab, and Registry.


  The GitLab Container Registry catalog on APIs.io includes 1 Spectral governance ruleset.


  GitLab Container Registry''s developer surface includes authentication, documentation, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Gitlab Container Registry Plans Pricing
  plan_count: 3
  slug: gitlab-container-registry-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Gitlab Container Registry Rate Limits
  slug: gitlab-container-registry-rate-limits
rules:
- name: GitLab Container Registry API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: gitlab-container-registry-rules
scopes:
- name: Gitlab Container Registry Scopes
  scope_count: 1
  slug: gitlab-container-registry-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 44.2
  delta: -1.9
  facets:
    commercial_clarity: 57.9
    contract_quality: 51.7
    developer_ergonomics: 28.3
    discoverability: 59.3
    governance: 10.4
    operational_transparency: 52.6
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gitlab-container-registry/refs/heads/main/screenshots/gitlab-container-registry-2026-06-20T181850.png
security:
- kind: authentication
  name: Gitlab Container Registry Authentication
  slug: gitlab-container-registry-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Gitlab Container Registry Domain Security
  slug: gitlab-container-registry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gitlab Container Registry Vulnerability Disclosure
  slug: gitlab-container-registry-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Gitlab Container Registry Trust Center
  slug: gitlab-container-registry-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, GDPR, CSA STAR
slug: gitlab-container-registry
tags:
- Container Images
- Containers
- GitLab
- Registry
website: https://docs.gitlab.com/user/packages/container_registry/
---
