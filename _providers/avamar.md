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
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: The Avamar REST API provides a framework to develop applications and tools that interact with a stand-alone Avamar server. It exposes backup, restore, client, domain, dataset, retention, policy, plugi
  name: Avamar REST API
  slug: avamar-rest-api
artifact_total: 6
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dell.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dell.com/support/home/en-us/product-support/product/avamar-rest-api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.dell.com/support/product-details/en-us/product/avamar-rest-api/resources/manuals
- group: start
  title: ''
  type: GettingStarted
  url: https://www.delltechnologies.com/asset/en-us/products/data-protection/technical-support/docu89854.pdf
- group: operate
  title: ''
  type: Support
  url: https://www.dell.com/support/home/en-us/product-support/product/avamar-server/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dell
- group: auth
  title: ''
  type: Authentication
  url: authentication/avamar-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/avamar-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/avamar-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/avamar-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/avamar-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.dell.com/support/kbdoc/en-us/000185734/all-dell-emc-end-of-life-documents
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/avamar-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/avamar-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/avamar-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/avamar-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.dell.com/en-us/dt/about-us/security-and-trust-center/compliance-service-organization-control-overlay.htm
- group: auth
  title: ''
  type: TrustCenter
  url: security/avamar-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/avamar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.dell.com/support/contents/en-us/article/product-support/self-support-knowledgebase/security-antivirus/alerts-vulnerabilities/dell-vulnerability-response-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avamar-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/avamar-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/avamar-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/avamar-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/avamar-llms.txt
created: '2026-07-17'
description: Avamar is enterprise backup and recovery software built on client-side global data deduplication, founded in Irvine, California and backed by Lightspeed Venture Partners before EMC acquired the company in November 2006 for approximately $165 million. Avamar now ships as Dell Avamar, part of the Dell Technologies data protection portfolio, and is deployed as a customer-hosted appliance or virtual edition rather than as a public SaaS. It exposes a REST API on the Avamar server for programmatic backup, restore, client, domain, dataset, policy and activity management, secured with OAuth 2.0 access tokens and optional OIDC single sign-on, and documented through a Swagger UI served from the appliance itself. A first-party Management Console Command Line Interface (mccli) and the avtar/avmaint command set provide the scripted administrative surface alongside the API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/avamar.png
layout: provider
modified: '2026-07-19'
name: Avamar
nav: Providers
network: true
overview: 'Avamar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Backup, Data Protection, Deduplication, and Disaster Recovery.


  Avamar''s developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, CLI, and 18 more developer resources.'
random_paper: 62
scopes:
- name: Avamar Scopes
  scope_count: 5
  slug: avamar-scopes
  summary_line: 5 scopes · password/authorizationCode/clientCredentials/implicit
score:
  band: thin
  composite: 29.8
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 39.5
  previous_composite: 29.8
  provenance:
    conformance: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/avamar/refs/heads/main/screenshots/avamar-2026-07-25T201915.png
security:
- kind: authentication
  name: Avamar Authentication
  slug: avamar-authentication
  summary_line: oauth2/http/openIdConnect · 5 schemes
- kind: domain-security
  name: Avamar Domain Security
  slug: avamar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Avamar Vulnerability Disclosure
  slug: avamar-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Avamar Trust Center
  slug: avamar-trust-center
  summary_line: ISO/IEC 27001:2022, SOC 2 Type II
slug: avamar
tags:
- Company
- Backup
- Data Protection
- Deduplication
- Disaster Recovery
- Storage
- Enterprise Software
- Infrastructure
- Dell Technologies
- On-Premise
website: https://developer.dell.com/
---
