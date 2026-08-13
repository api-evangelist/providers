---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Jit REST API for programmatic access to security findings, artifacts (SBOM, scan results), teams, plans, policies, workflows, integrations, billing metrics, and on-demand scan execution. Authenticates
  name: Jit API
  slug: jit-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.jit.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.jit.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jit.io/docs/about-jit
- group: docs
  title: ''
  type: APIReference
  url: https://docs.jit.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.jit.io/docs/welcome-to-onboarding
- group: company
  title: ''
  type: Blog
  url: https://www.jit.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jitsecurity
- group: start
  title: ''
  type: SignUp
  url: https://platform.jit.io/
- group: start
  title: ''
  type: Login
  url: https://platform.jit.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jit.io/legal/terms/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jit.io/legal/terms/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jit.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.jit.io/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.jit.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/jit-fka-cbrix-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jit-fka-cbrix-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jit-fka-cbrix-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jit-fka-cbrix-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jit-fka-cbrix-mcp.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jit-fka-cbrix-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jit-fka-cbrix-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jit-fka-cbrix-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jit-fka-cbrix-domain-security.yml
created: '2026-07-17'
description: Jit is an AI-powered Application Security Posture Management (ASPM) and DevSecOps orchestration platform for modern engineering teams. It unifies open-source and proprietary security scanners (Semgrep, Prowler, KICS, OWASP ZAP, Trivy, npm-audit, Wiz and more) behind one control plane, correlates their signals, prioritizes findings by policy, and drives fix-focused remediation directly in the developer workflow. Jit exposes a REST API at api.jit.io with OAuth2 client-credentials (JWT bearer) authentication and a fine-grained jit.* permission model covering findings, artifacts, teams, plans, policies, workflows, integrations, and scan execution. Formerly Cbrix, Jit is backed by Insight Partners and integrates across GitHub, GitLab, Bitbucket, Azure DevOps, AWS, GCP, and Azure.
image: https://cdn.prod.website-files.com/61e3cab9aff0501e51b0bd77/67fe6ccbc18c587b9d9b93bf_og.webp
layout: provider
mcp_servers:
- description: ''
  name: jit-fka-cbrix-mcp.yml
  slug: jit-fka-cbrix-mcpyml
modified: '2026-07-19'
name: Jit (fka Cbrix)
nav: Providers
network: true
overview: 'Jit (fka Cbrix) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Application Security, DevSecOps, and ASPM.


  Jit (fka Cbrix)''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, and 17 more developer resources.'
random_paper: 59
scopes:
- name: Jit Fka Cbrix Scopes
  scope_count: 0
  slug: jit-fka-cbrix-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 32.9
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jit-fka-cbrix/refs/heads/main/screenshots/jit-fka-cbrix-2026-07-25T223206.png
security:
- kind: authentication
  name: Jit Fka Cbrix Authentication
  slug: jit-fka-cbrix-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Jit Fka Cbrix Domain Security
  slug: jit-fka-cbrix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Jit Fka Cbrix Trust Center
  slug: jit-fka-cbrix-trust-center
  summary_line: SOC 2 Type 2
slug: jit-fka-cbrix
tags:
- Company
- Cybersecurity
- Application Security
- DevSecOps
- ASPM
- Security
- Vulnerability Management
- API
website: https://www.jit.io/
---
