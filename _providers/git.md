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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-26'
api_count: 4
apis:
- description: Git command-line interface for version control operations.
  name: Git CLI
  slug: git-cli
- description: RESTful API for GitHub's Git hosting platform.
  name: GitHub API
  slug: github
- description: RESTful API for GitLab's Git repository management.
  name: GitLab API
  slug: gitlab
- description: RESTful API for Gitea's self-hosted Git service.
  name: Gitea API
  slug: gitea
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/git-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/git-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/git-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/git-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/git-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/git-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/git-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://git-scm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://git-scm.com/doc
created: '2024-01-01'
description: Git is a distributed version control system for tracking changes in source code during software development. It is designed for coordinating work among programmers, but it can be used to track changes in any set of files.
finops:
- name: Git Finops
  service_category: API
  slug: git-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/git.png
layout: provider
mcp_servers:
- description: ''
  name: Git MCP Server
  slug: git-mcp-server
modified: '2026-06-20'
name: Git
nav: Providers
network: true
overview: 'Git publishes 3 APIs on the [APIs.io](https://apis.io/) network: GitHub API, GitLab API, and Gitea API. Tagged areas include Distributed, Git, Open-Source, Source Code Management, and Version Control.


  Git''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Git Plans Pricing
  plan_count: 3
  slug: git-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Git Rate Limits
  slug: git-rate-limits
score:
  band: thin
  composite: 28.7
  delta: 3.8
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 28.6
    discoverability: 83.3
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 24.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/git/refs/heads/main/screenshots/git-2026-06-20T181828.png
security:
- kind: domain-security
  name: Git Domain Security
  slug: git-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Git Vulnerability Disclosure
  slug: git-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Git Trust Center
  slug: git-trust-center
  summary_line: trust center published
slug: git
tags:
- Distributed
- Git
- Open-Source
- Source Code Management
- Version Control
website: https://git-scm.com/
---
