---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 6
apis:
- description: OpenAPI-described REST API for the Semgrep AppSec Platform. Lists deployments, projects, findings, scans, secrets, and supply chain data, and supports CI/CD and triage automation. Requires a Team or E
  name: Semgrep AppSec Platform REST API
  slug: appsec-platform-api
- description: Open-source command-line static analysis engine. Runs locally and in CI to scan code with community and custom rules, emit SARIF/JSON output, and enforce policies. Authored primarily in OCaml with Pyt
  name: Semgrep CLI
  slug: cli
- description: Community and Semgrep-maintained rule packs covering security, correctness, best-practice, and supply chain findings across many languages and frameworks. Consumed by the CLI and the AppSec Platform.
  name: Semgrep Community Rules
  slug: rules
- description: Visual Studio Code extension that surfaces Semgrep findings inline while developers edit code, with quick-fix and triage actions tied to the AppSec Platform.
  name: Semgrep VS Code Extension
  slug: vscode
- description: Shared interface definitions (ATD-generated types) used between the Semgrep CLI, AppSec Platform, and language-specific clients to keep output schemas in sync.
  name: Semgrep Interfaces
  slug: interfaces
- description: Source for the Semgrep product documentation site, including CLI reference, rule-writing guides, AppSec Platform docs, and API reference.
  name: Semgrep Documentation
  slug: docs
artifact_total: 12
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/semgrep/semgrep/blob/develop/LICENSE
- group: auth
  title: ''
  type: TrustCenter
  url: security/semgrep-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/semgrep-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/semgrep-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/semgrep
- group: company
  title: ''
  type: Website
  url: https://semgrep.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://semgrep.dev/docs/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/semgrep
- group: commercial
  title: ''
  type: Plans
  url: plans/semgrep-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/semgrep-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/semgrep-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://semgrep.dev/llms.txt
created: '2026-05-23'
description: Semgrep is a fast, open-source static analysis engine and an associated AppSec Platform (Semgrep Code, Semgrep Supply Chain, and Semgrep Secrets) that finds bugs, security issues, and policy violations across source code, dependencies, and credentials. The open-source CLI runs pattern-based rules locally or in CI; the AppSec Platform layers a managed control plane on top with organization-wide policy, triage workflows, findings management, and an OpenAPI-described REST API for deployments, projects, findings, scans, secrets, and supply chain data. Editor, CI, and SCM integrations (VS Code, JetBrains, GitHub, GitLab, Bitbucket, Azure DevOps) round out the developer surface.
finops:
- name: Semgrep Finops
  service_category: API
  slug: semgrep-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/semgrep.png
layout: provider
modified: '2026-05-23'
name: Semgrep
nav: Providers
network: true
overview: 'Semgrep publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Static Analysis, SAST, Application Security, Supply Chain, and Secrets Detection.


  Semgrep''s developer surface includes documentation, GitHub presence, and 10 more developer resources.'
plans:
- name: Semgrep Plans Pricing
  plan_count: 1
  slug: semgrep-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 2
  name: Semgrep Rate Limits
  slug: semgrep-rate-limits
score:
  band: emerging
  composite: 20.7
  delta: 0.8
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/semgrep/refs/heads/main/screenshots/semgrep-2026-06-20T193645.png
security:
- kind: domain-security
  name: Semgrep Domain Security
  slug: semgrep-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Semgrep Vulnerability Disclosure
  slug: semgrep-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Semgrep Trust Center
  slug: semgrep-trust-center
  summary_line: SOC 2, GDPR
slug: semgrep
tags:
- Static Analysis
- SAST
- Application Security
- Supply Chain
- Secrets Detection
- Developer Tools
- DevSecOps
website: https://semgrep.dev/
---
