---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.5
  scored_at: '2026-11-06'
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
artifact_total: 14
common:
- group: company
  title: ''
  type: Blog
  url: https://semgrep.dev/blog/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/semgrep/semgrep/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/semgrep/semgrep/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/semgrep/semgrep/blob/develop/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/semgrep/semgrep/blob/develop/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/semgrep/semgrep/blob/develop/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/semgrep/semgrep/blob/develop/LICENSE
- group: auth
  href: https://artifacts.apis.io/semgrep/security/semgrep-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/semgrep-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/semgrep/security/semgrep-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/semgrep-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/semgrep/security/semgrep-domain-security.yml
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
  href: https://artifacts.apis.io/semgrep/plans/semgrep-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/semgrep-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/semgrep/rate-limits/semgrep-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/semgrep-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/semgrep/finops/semgrep-finops.yml
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
- has_sources: false
  method: generated
  name: Semgrep Finops
  primary_unit: ''
  service_category: API
  slug: semgrep-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/semgrep.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.semgrep.dev over HTTP; 3 tools listed.
  name: Semgrep MCP Server
  slug: semgrep
modified: '2026-10-06'
name: Semgrep
nav: Providers
network: true
overview: 'Semgrep is listed with 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Static Analysis, SAST, Application Security, Supply Chain, and Secrets Detection.


  Semgrep''s developer surface includes engineering blog, documentation, GitHub presence, and 15 more developer resources.'
plans:
- name: Semgrep Plans Pricing
  plan_count: 1
  slug: semgrep-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Semgrep Rate Limits
  slug: semgrep-rate-limits
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 80.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 26.3
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/semgrep/semgrep-2026-06-20T193645.png
security:
- kind: authentication
  name: Semgrep Authentication
  slug: semgrep-authentication
  summary_line: 2 schemes
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
