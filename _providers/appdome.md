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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Appdome Build2Secure (DEV-API) REST API automates Appdome's no-code mobile app defense pipeline — upload, build/fuse, add context, sign (standard, private, and Auto-DEV signing), download, publish
  name: Appdome Build2Secure API
  slug: appdome-build2secure-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appdome-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appdome.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apis.appdome.com/docs/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://apis.appdome.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://apis.appdome.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://apis.appdome.com/docs/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://fusion.appdome.com/#/signup
- group: start
  title: ''
  type: Login
  url: https://fusion.appdome.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.appdome.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.appdome.com/dev-sec-blog/
- group: operate
  title: ''
  type: Support
  url: https://www.appdome.com/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.appdome.com/how-to/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.appdome.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appdome.com/legal/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Appdome
- group: build
  title: ''
  type: Packages
  url: packages/appdome-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/appdome-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/appdome-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/appdome-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appdome-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/appdome-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/appdome-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/appdome-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/appdome-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/appdome-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/appdome-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Appdome is a mobile app defense and DevSecOps platform that lets development and security teams add cyber-defense, anti-fraud, anti-malware, anti-cheat, and runtime protections to Android and iOS apps with no code and no SDK. Its Build2Secure ("DEV-API") REST API connects the no-code build, fuse, context, sign, and publish steps to CI/CD systems such as GitHub, GitLab, Jenkins, Azure DevOps, Bitrise, CircleCI, and TeamCity, enabling teams to protect, sign, certify, and release mobile apps automatically at scale. The platform also covers app validation, Certified Secure certificates, team and user management, DEV-Logs audit events, and device-matching services. Appdome is backed by Menlo Ventures.
image: https://www.appdome.com/wp-content/uploads/2025/10/cropped-AppdomeShield-270x270.png
layout: provider
mcp_servers:
- description: ''
  name: appdome-mcp.yml
  slug: appdome-mcpyml
modified: '2026-07-17'
name: Appdome
nav: Providers
network: true
overview: 'Appdome publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobile App Security, Mobile App Defense, DevSecOps, and Application Security.


  Appdome''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, support, and 20 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 26.9
  delta: -4.5
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 31.4
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/screenshots/appdome-2026-07-25T200727.png
security:
- kind: authentication
  name: Appdome Authentication
  slug: appdome-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Appdome Domain Security
  slug: appdome-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appdome
tags:
- Company
- Mobile App Security
- Mobile App Defense
- DevSecOps
- Application Security
- Mobile
- CI/CD
- App Signing
- Anti-Fraud
- Code Signing
website: https://appdome.com
---
