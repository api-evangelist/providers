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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Backend API for the Tolmo cloud security platform, consumed through the Tolmo CLI (SQL/Cypher queries over the infrastructure graph, security findings management, and a secure server-side proxy for co
  name: Tolmo Platform API
  slug: tolmo-platform-api
artifact_total: 5
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tolmo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tolmo.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tolmo.com/installation
- group: auth
  title: ''
  type: Authentication
  url: authentication/tolmo-authentication.yml
- group: build
  title: ''
  type: CLI
  url: cli/tolmo-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/tolmo-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tolmo-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tolmo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tolmo.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tolmo-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tolmo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tolmo-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tolmo-security.txt
- group: auth
  title: ''
  type: Security
  url: https://tolmo.com/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tolmo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tolmo-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tolmo-trust-center.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tolmohq
- group: company
  title: ''
  type: Blog
  url: https://tolmo.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://tolmo.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://app.tolmo.com/
- group: company
  title: ''
  type: Website
  url: https://tolmo.com/
created: '2026-07-17'
description: 'Tolmo builds AI-native cybersecurity for engineering teams. Its platform pairs automated cloud and SaaS discovery (AWS, GitHub, Datadog, Linear, Cloudflare, and more) with event-driven agents that run continuous pentesting, threat modeling, finding generation, and verified remediation against the customer''s real infrastructure graph. The primary developer surface is the Tolmo CLI: SQL and Cypher queries over the infrastructure graph, full-lifecycle security findings management, and a secure server-side proxy for GitHub/AWS/Linear/ Sentry/Datadog requests, plus a first-party agent skill for Claude Code and other AI agents. Backed by Accel and Y Combinator.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tolmo.png
layout: provider
modified: '2026-07-21'
name: Tolmo
nav: Providers
network: true
overview: 'Tolmo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Cloud Security, and Vulnerability Management.


  Tolmo''s developer surface includes documentation, getting-started guide, authentication, CLI, changelog, engineering blog, support, and 16 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 24.7
  provenance:
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Tolmo Authentication
  slug: tolmo-authentication
  summary_line: oauth2/http-bearer · 2 schemes
- kind: domain-security
  name: Tolmo Domain Security
  slug: tolmo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tolmo Vulnerability Disclosure
  slug: tolmo-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Tolmo Trust Center
  slug: tolmo-trust-center
  summary_line: trust center published
slug: tolmo
tags:
- Company
- Security
- Cybersecurity
- Cloud Security
- Vulnerability Management
- CLI
- DevSecOps
- AI Agents
- Infrastructure Graph
website: https://tolmo.com/
---
