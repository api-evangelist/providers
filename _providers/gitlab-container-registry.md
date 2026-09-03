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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Gitlab Container Registry Agentic Access
  operation_count: 8
  slug: gitlab-container-registry-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Container registry repositories
  name: GitLab Container Registry Repositories API
  slug: gitlab-container-registry-repositories-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Container image tags
  name: GitLab Container Registry Tags API
  slug: gitlab-container-registry-tags-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GitLab Container Registry Repositories API
  slug: open-gitlab-container-registry-repositories-api
- collection_type: open
  name: GitLab Container Registry Repositories Tags API
  slug: open-gitlab-container-registry-tags-api
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
random_paper: 7
rate_limits:
- limit_count: 5
  name: Gitlab Container Registry Rate Limits
  slug: gitlab-container-registry-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: GitLab Container Registry API Rules
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
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 31.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
