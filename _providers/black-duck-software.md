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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.blackduck.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.blackduck.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blackduck.com/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.blackduck.com/category/api
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.blackduck.com/bundle/bd-hub/page/SDK/Using_the_Hub_SDK.html
- group: company
  title: ''
  type: Blog
  url: https://www.blackduck.com/blog.html
- group: operate
  title: ''
  type: Support
  url: https://community.blackduck.com/s/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blackducksoftware
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blackduck.com/company/legal/privacy-policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blackduck.com/company/legal/terms-of-use.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blackduck.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.blackduck.com/company/legal/security-commitments.html
- group: auth
  title: ''
  type: TrustCenter
  url: security/black-duck-software-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.blackduck.com/company/legal/vulnerability-disclosure-policy.html
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/black-duck-software-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/black-duck-software-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/black-duck-software-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/black-duck-software-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/black-duck-software-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/black-duck-software-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/black-duck-software-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/black-duck-software-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/black-duck-software-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/black-duck-software-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/black-duck-software-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/black-duck-software-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/black-duck-software-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/black-duck-software-well-known.yml
created: '2026-07-17'
description: Black Duck Software is an independent application security company (formerly the Synopsys Software Integrity Group, spun out in October 2024 and backed by Clearlake Capital and Francisco Partners). Its portfolio spans Software Composition Analysis (Black Duck SCA), static analysis (Coverity), dynamic and interactive testing, fuzzing, and the Polaris SaaS platform, helping organizations find and fix open-source, license, and security risk across the SDLC. Black Duck exposes a versioned REST API (custom media types, bearer-token / API-token auth, HAL-style hypermedia), native CI/CD plug-ins, the Detect command-line scanner, webhooks, and an official MCP server (Black Duck Signal) for AI coding assistants.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/black-duck-software.png
layout: provider
mcp_servers:
- description: Black Duck Signal connects with popular AI coding assistants (Claude Code, Google Gemini, GitHub Copilot) via the Model Context Protocol so developers can run Black Duck security scans and query SCA/K
  name: Black Duck Signal
  slug: black-duck-signal
modified: '2026-07-18'
name: Black Duck Software
nav: Providers
network: true
overview: 'Black Duck Software is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Application Security, Software Composition Analysis, and Open Source Security.


  Black Duck Software''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, authentication, and 21 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 36.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/black-duck-software/refs/heads/main/screenshots/black-duck-software-2026-07-25T203232.png
security:
- kind: authentication
  name: Black Duck Software Authentication
  slug: black-duck-software-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Black Duck Software Domain Security
  slug: black-duck-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Black Duck Software Vulnerability Disclosure
  slug: black-duck-software-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Black Duck Software Trust Center
  slug: black-duck-software-trust-center
  summary_line: SOC 2 Type 2, SOC 3 Type 2, ISO 27001, ISO 27017, ISO 26262, CSA STAR (Self-Assessment / CAIQ), TISAX Level 2, TX-RAMP Level 2
slug: black-duck-software
tags:
- Company
- Security
- Application Security
- Software Composition Analysis
- Open Source Security
- Static Analysis
- DevSecOps
- Vulnerability Management
- SAST
- SCA
website: https://www.blackduck.com/
---
