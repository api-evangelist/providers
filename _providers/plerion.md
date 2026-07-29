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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-07-28'
api_count: 13
apis:
- description: The Plerion Risk Score (PRS) Engine has calculated Alerts that are the highest priority items based on the available information across Identity, Configuration, and Vulnerability Management. Alerts of
  name: Plerion Alerts API
  slug: plerion-alerts-api
- description: Asset Group is classifying assets into specific group based on the different criteria such as integration, asset tag, resource type and resource name. This helps users to manage, organize, and analyze
  name: Plerion Asset groups API
  slug: plerion-asset-groups-api
- description: Plerion Assets form the basis upon which all Plerion contextual security is reported. Every unique cloud resource on which Plerion collects information is classified as a single asset on the Plerion p
  name: Plerion Assets API
  slug: plerion-assets-api
- description: 'Audit logs provide a comprehensive trail of user activities and system operations within a tenant. These logs capture important events such as user logins, API calls, configuration changes, and other '
  name: Plerion Audit logs API
  slug: plerion-audit-logs-api
- description: In order to connect your AWS account to Plerion or update existing account, you will need, <ol> <li> <b>CloudFormation Template URL</b>. Retrieve the template from <a href="#tag/AWS-Integration/operat
  name: Plerion AWS integration API
  slug: plerion-aws-integration-api
- description: The Code security API from Plerion — 4 operation(s) for code security.
  name: Plerion Code security API
  slug: plerion-code-security-api
- description: Compliance Frameworks help our customers meet their regulatory and compliance obligations, and reduce compliance risk, enabling them to achieve their strategic objectives. Plerion offers customers hun
  name: Plerion Compliance frameworks API
  slug: plerion-compliance-frameworks-api
- description: Findings are the results of the Plerion Detection Engine (PDE) Detection reporting a finding and rating the severity of the finding as it relates to best practices or a relevant compliance standard. P
  name: Plerion Findings API
  slug: plerion-findings-api
- description: Integrations enable customers to connect their own cloud environments to the Plerion platform. Integrations allow for the collection of data from the integrated environment, e.g. Connecting Plerion to
  name: Plerion Integrations API
  slug: plerion-integrations-api
- description: In a cloud environment there are usually many hundreds or thousands of misconfigurations, but which of those pose a clear and present danger of a breach? That’s what the Plerion risk is about.
  name: Plerion Risks API
  slug: plerion-risks-api
- description: The Plerion platform caters for multi-tenancy. Multi-tenancy within the Plerion platform delivers isolation for the integrations supported by Plerion. Each Tenancy (Tenant) allows for multiple inbound
  name: Plerion Tenant API
  slug: plerion-tenant-api
- description: The Vulnerabilities API from Plerion — 3 operation(s) for vulnerabilities.
  name: Plerion Vulnerabilities API
  slug: plerion-vulnerabilities-api
- description: The AWS Well-Architected Framework helps customers design secure, high-performing, resilient, and efficient cloud infrastructure. Plerion continuously assesses your environment against the AWS Well-Ar
  name: Plerion Well-Architected frameworks API
  slug: plerion-well-architected-frameworks-api
artifact_total: 18
common:
- group: company
  title: ''
  type: Website
  url: https://plerion.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.plerion.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.plerion.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.plerion.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.plerion.com/api-reference/index
- group: auth
  title: ''
  type: Authentication
  url: authentication/plerion-authentication.yml
- group: build
  title: ''
  type: CLI
  url: cli/plerion-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/plerion-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/plerion-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plerion-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/plerion-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/plerion-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plerion-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/plerion-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/plerion-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/plerion-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plerion-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/plerion-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.plerion.com/company/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.plerion.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/plerion-changelog.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plerionhq
- group: company
  title: ''
  type: Blog
  url: https://www.plerion.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.plerion.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.plerion.com/sign-in
- group: operate
  title: ''
  type: Support
  url: https://www.plerion.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.plerion.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.plerion.com/company/privacy-policy
created: '2026-07-17'
description: Plerion is an AI-powered cloud security platform that gives teams unified visibility and automated remediation across cloud, code, and AI. It covers Cloud Security Posture Management (CSPM) for AWS, Azure, GCP, and Kubernetes; Cloud Workload Protection (CWPP) with vulnerability and SBOM scanning; Code Security (IaC and SCA scanning for GitHub, GitLab, and Bitbucket); AI Security Posture Management (AI-SPM) for Bedrock, OpenAI, and Anthropic deployments; attack-path analysis, entitlements analysis, resource access grants, and compliance tracking against frameworks like ISO 27001, SOC 2, CIS, and ISMS-P. Plerion exposes a tenant-scoped REST API (Bearer API key, regional hosts) plus a cross-platform CLI so teams can query findings, assets, risks, vulnerabilities, and compliance posture programmatically.
image: https://www.plerion.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: plerion-mcp.yml
  slug: plerion-mcpyml
modified: '2026-07-20'
name: Plerion
nav: Providers
network: true
overview: 'Plerion publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Asset groups API, Assets API, and 10 more. Tagged areas include Company, Security, Cloud Security, CSPM, and Cloud Workload Protection.


  Plerion''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, changelog, engineering blog, and 22 more developer resources.'
random_paper: 50
score:
  band: developing
  composite: 53.9
  delta: -1.4
  facets:
    commercial_clarity: 52.6
    contract_quality: 64.4
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 55.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Plerion Authentication
  slug: plerion-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Plerion Domain Security
  slug: plerion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Plerion Vulnerability Disclosure
  slug: plerion-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Plerion Trust Center
  slug: plerion-trust-center
  summary_line: trust center published
slug: plerion
tags:
- Company
- Security
- Cloud Security
- CSPM
- Cloud Workload Protection
- Vulnerability Management
- Compliance
- AI Security
- DevSecOps
- API
website: https://plerion.com
---
