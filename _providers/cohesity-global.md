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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: RESTful interface for data management, backup and recovery, cyber resilience, reporting, and site continuity operations across Cohesity Helios (multi-cluster SaaS control plane) and on-premises Cohesi
  name: Cohesity Helios and Cluster REST API
  slug: cohesity-helios-and-cluster-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cohesity-global-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cohesity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cohesity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cohesity.com/apidocs/versions
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cohesity.com/versions.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cohesity.com/docs/get-started-apps.html
- group: operate
  title: ''
  type: Support
  url: https://support.cohesity.com/
- group: company
  title: ''
  type: Blog
  url: https://www.cohesity.com/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cohesity
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cohesity.com/buy/cohesity-data-cloud-packaging/
- group: start
  title: ''
  type: SignUp
  url: https://my.cohesity.com/s/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cohesity.com/agreements-docs/cohesity-website-terms-of-use.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cohesity.com/agreements/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/cohesity/
- group: build
  title: ''
  type: Packages
  url: packages/cohesity-global-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cohesity-global-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cohesity-global-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cohesity-global-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cohesity-global-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cohesity-global-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.cohesity.com/trust/
- group: auth
  title: ''
  type: TrustCenter
  url: security/cohesity-global-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cohesity-global-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cohesity.com/trust/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cohesity-global-llms.txt
created: '2026-07-17'
description: Cohesity is an AI-powered data security and management company whose platform consolidates backup and recovery, cyber resilience, threat defense, and data insights across cloud, on-premises, and SaaS environments. Cohesity exposes RESTful Helios and Cluster APIs alongside first-party Python, Go, PowerShell, Ansible, and Terraform tooling so developers can automate data protection, orchestrate recovery, run reporting, and build custom workflows against 1,000+ supported workloads. Originally surfaced as a portfolio company of Battery Ventures and enriched from Cohesity's public developer surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cohesity-global.png
layout: provider
modified: '2026-07-18'
name: Cohesity Global
nav: Providers
network: true
overview: 'Cohesity Global publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Security, Data Management, Backup and Recovery, and Cyber Resilience.


  Cohesity Global''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 18 more developer resources.'
random_paper: 102
scopes:
- name: Cohesity Global Scopes
  scope_count: 6
  slug: cohesity-global-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: thin
  composite: 35.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 63.0
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 35.8
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cohesity-global/refs/heads/main/screenshots/cohesity-global-2026-07-25T210017.png
security:
- kind: authentication
  name: Cohesity Global Authentication
  slug: cohesity-global-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Cohesity Global Domain Security
  slug: cohesity-global-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cohesity Global Vulnerability Disclosure
  slug: cohesity-global-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Cohesity Global Trust Center
  slug: cohesity-global-trust-center
  summary_line: SOC 2 Type II, ISO 27001:2022, HIPAA, FedRAMP Moderate, GovRAMP, Common Criteria EAL2+, NIST FIPS 140-2, USGv6
slug: cohesity-global
tags:
- Company
- Data Security
- Data Management
- Backup and Recovery
- Cyber Resilience
- Data Protection
- Disaster Recovery
- Cloud
website: https://www.cohesity.com/
---
