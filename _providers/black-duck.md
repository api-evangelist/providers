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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for Black Duck SCA (Hub) — projects, versions, components, vulnerabilities, policies, scans, and reports. Each Black Duck server publishes its own OpenAPI 3 document at /api-doc/openapi3-publ
  name: Black Duck SCA REST API
  slug: black-duck-sca-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/black-duck-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.blackduck.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.blackduck.com/category/api
- group: docs
  title: ''
  type: APIReference
  url: https://community.blackduck.com/s/article/Blackduck-API-documentation-swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://community.blackduck.com/s/article/Black-Duck-HUB-How-to-view-the-API-documentation
- group: operate
  title: ''
  type: Support
  url: https://community.blackduck.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.blackduck.com/blog.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blackducksoftware
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blackduck.com/software-composition-analysis-tools/black-duck-sca/get-pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://www.blackduck.com/software-composition-analysis-tools/black-duck-sca/get-pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blackduck.com/company/legal/website-terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blackduck.com/company/legal/privacy.html
- group: build
  title: ''
  type: Packages
  url: packages/black-duck-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/black-duck-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/black-duck-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/black-duck-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/black-duck-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/black-duck-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://community.blackduck.com/s/black-duck-status
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/black-duck-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/black-duck-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.blackduck.com/company/legal/security-commitments.html
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/black-duck-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.blackduck.com/company/legal/security-commitments.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/black-duck-llms.txt
created: '2026-07-17'
description: Black Duck Software (formerly the Synopsys Software Integrity Group) is an application security company whose platform spans software composition analysis (SCA), static application security testing (SAST), dynamic application security testing (DAST), interactive application security testing (IAST), and open-source license and vulnerability management. Its API-first products — Black Duck SCA (Hub), Polaris, Coverity, and Seeker — expose REST APIs, webhooks, native CI/CD plug-ins, and the Detect command-line scanner so teams can automate open-source discovery, policy enforcement, and risk remediation across build pipelines such as Jenkins, GitHub Actions, GitLab CI, and Azure DevOps. Each Black Duck server publishes its own OpenAPI 3 document and Postman collection at /api-doc, and first-party Python and Go client libraries plus the Detect CLI wrap the API surface. This profile was seeded as a general-catalyst portfolio lead and enriched by the API Evangelist pipeline.
image: https://www.blackduck.com/content/dam/black-duck/style-guide/header/BlackDuckLogo.svg
layout: provider
mcp_servers:
- description: ''
  name: black-duck-mcp.yml
  slug: black-duck-mcpyml
modified: '2026-07-18'
name: Black Duck
nav: Providers
network: true
overview: 'Black Duck publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Application Security, Software Composition Analysis, and SAST.


  Black Duck''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 18 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 41.7
  delta: -0.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 73.9
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 42.3
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/screenshots/black-duck-2026-07-25T203232.png
security:
- kind: authentication
  name: Black Duck Authentication
  slug: black-duck-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Black Duck Domain Security
  slug: black-duck-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Black Duck Vulnerability Disclosure
  slug: black-duck-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Black Duck Trust Center
  slug: black-duck-trust-center
  summary_line: SOC 2 Type 2, SOC 3 Type 2, ISO 27001, ISO 27017, ISO 26262, CSA STAR Self-Assessment, TISAX (Assessment Level 2), TX-RAMP Level 2
slug: black-duck
tags:
- Company
- Enterprise
- Application Security
- Software Composition Analysis
- SAST
- DAST
- Open Source Security
- DevSecOps
- Vulnerability Management
website: https://documentation.blackduck.com/
---
