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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: The Findings API from Pixee — 2 operation(s) for findings.
  name: Pixee Findings API
  slug: pixee-ai-findings-api
- description: The Fixes API from Pixee — 2 operation(s) for fixes.
  name: Pixee Fixes API
  slug: pixee-ai-fixes-api
- description: The Repositories API from Pixee — 2 operation(s) for repositories.
  name: Pixee Repositories API
  slug: pixee-ai-repositories-api
- description: The Scans API from Pixee — 1 operation(s) for scans.
  name: Pixee Scans API
  slug: pixee-ai-scans-api
- description: The Webhooks API from Pixee — 2 operation(s) for webhooks.
  name: Pixee Webhooks API
  slug: pixee-ai-webhooks-api
artifact_total: 19
asyncapis:
- description: Pixee webhooks deliver real-time HTTP POST notifications when remediation events occur. This AsyncAPI document is a faithful reconstruction of the event types and payload schemas documented at https:/
  name: Pixee Webhooks
  slug: pixee-ai-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.pixee.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pixee.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pixee.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pixee.ai/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pixee.ai/getting-started/first-fix
- group: company
  title: ''
  type: Blog
  url: https://www.pixee.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pixee.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.pixee.ai/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pixee
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pixee.ai/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pixee.ai/policies/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pixee-ai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/pixee-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pixee-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/pixee-ai-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pixee-ai-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pixee-ai-well-known.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pixee-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pixee-ai-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: security/pixee-ai-trust-center.yml
created: '2026-07-17'
description: Pixee is an agentic security engineering (AppSec) platform — "your automated product security engineer." It ingests findings from SAST, SCA, and IaC scanners as SARIF, runs a three-tier triage engine that classifies each vulnerability with auditable, timestamped evidence, and delivers remediations as native pull requests across GitHub, GitLab, Azure DevOps, and Bitbucket using deterministic codemods plus quality-evaluated AI fixes. Pixee exposes a HAL-based REST API (organization-scoped bearer tokens), documented webhooks, a first-party CLI with bundled agent skills, and the open-source Codemodder framework (Java and Python). It is backed by Wing Venture Capital.
image: https://cdn.prod.website-files.com/696822cb241ff5e67581075b/69b1a742e6436bad27408920_pixee%20agentic%20appsec%20image.png
layout: provider
modified: '2026-07-20'
name: Pixee
nav: Providers
network: true
overview: 'Pixee publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Findings API, Fixes API, Repositories API, and 2 more. Tagged areas include Company, Security, Application Security, AppSec, and Vulnerability Remediation.


  The Pixee catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pixee''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, CLI, and 14 more developer resources.'
random_paper: 66
score:
  band: developing
  composite: 53.5
  delta: 0.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 66.9
    developer_ergonomics: 56.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 53.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Pixee Ai Authentication
  slug: pixee-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pixee Ai Domain Security
  slug: pixee-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pixee Ai Trust Center
  slug: pixee-ai-trust-center
  summary_line: SOC 2, ISO 27001, CSA STAR
skill_count: 10
skills:
- name: pixee-analysis
  slug: pixee-analysis
- name: pixee-api
  slug: pixee-api
- name: pixee-auth
  slug: pixee-auth
- name: pixee-finding
  slug: pixee-finding
- name: pixee-integration
  slug: pixee-integration
- name: pixee-preferences
  slug: pixee-preferences
- name: pixee-repo
  slug: pixee-repo
- name: pixee-scan
  slug: pixee-scan
- name: pixee-shared
  slug: pixee-shared
- name: pixee-workflow
  slug: pixee-workflow
slug: pixee-ai
tags:
- Company
- Security
- Application Security
- AppSec
- Vulnerability Remediation
- Static Analysis
- SARIF
- Code Security
- AI
- Developer Tools
website: https://www.pixee.ai/
---
