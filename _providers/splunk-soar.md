---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Splunk SOAR REST API creates, updates, queries and selectively removes the objects the platform automates against — containers, artifacts, playbooks, action runs, apps, assets, CEF fields, indicat
  name: Splunk SOAR REST API
  slug: splunk-soar-rest-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/splunk-soar-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://advisory.splunk.com/report
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/splunk-soar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/splunk-soar-domain-security.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/splunk/
- group: start
  title: ''
  type: Portal
  url: https://www.splunk.com/en_us/products/splunk-security-orchestration-and-automation.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.splunk.com/en/splunk-soar/soar-cloud
- group: docs
  title: ''
  type: Documentation
  url: https://help.splunk.com/en/splunk-soar/soar-cloud
- group: docs
  title: ''
  type: APIReference
  url: https://help.splunk.com/en/splunk-soar/soar-cloud/rest-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://help.splunk.com/en/splunk-soar/soar-cloud/rest-api-reference/using-the-splunk-soar-rest-api/using-the-rest-api-reference-for-splunk-soar-cloud
- group: operate
  title: ''
  type: Support
  url: https://www.splunk.com/en_us/support-and-services.html
- group: company
  title: ''
  type: Blog
  url: https://www.splunk.com/en_us/blog/security.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/phantomcyber
- group: commercial
  title: ''
  type: Pricing
  url: https://www.splunk.com/en_us/products/pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://www.splunk.com/en_us/download/soar-free-trial.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.splunk.com/en_us/legal/splunk-general-terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.splunk.com/en_us/legal/privacy.html
- group: build
  title: ''
  type: Packages
  url: packages/splunk-soar-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/splunk-soar-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/splunk-soar-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/splunk-soar-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/splunk-soar-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/splunk-soar-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/splunk-soar-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/splunk-soar-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/splunk-soar-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/splunk-soar-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.splunk.com
- group: operate
  title: ''
  type: Deprecation
  url: https://help.splunk.com/en/splunk-soar/soar-cloud/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/splunk-soar-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/splunk-soar-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.splunk.com/en_us/about-splunk/splunk-data-security-and-privacy/compliance-at-splunk.html
- group: agent
  title: ''
  type: WellKnown
  url: well-known/splunk-soar-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/splunk-soar-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/splunk-soar-llms.txt
created: '2026-08-19'
description: Splunk SOAR, built on the Phantom platform Splunk acquired in 2018 and now part of Cisco through the 2024 Splunk acquisition, is a security orchestration, automation and response platform. It runs playbooks across hundreds of connected security tools, and exposes a REST API for containers, artifacts, playbooks, actions, assets, indicators, evidence, vault files, workbooks and case management, served from each customer's own tenant at https://{soar-host}/rest/ rather than a shared API host. Authentication is HTTP Basic or a ph-auth-token automation token. Splunk publishes a documented app/connector SDK on PyPI with the soarapps CLI, a first-party VS Code extension, and 529 open connector repositories, but no anonymously fetchable OpenAPI document, no MCP server for SOAR, and no published rate limits or pricing.
image: https://www.splunk.com/content/dam/splunk2/images/icons/favicons/favicon.ico
layout: provider
modified: '2026-08-19'
name: Splunk SOAR
nav: Providers
network: true
overview: 'Splunk SOAR publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, SOAR, Automation, Orchestration, and Incident Response.


  Splunk SOAR''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 28 more developer resources.'
plans:
- name: Splunk Soar Plans Pricing
  plan_count: 0
  slug: splunk-soar-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Splunk Soar Rate Limits
  slug: splunk-soar-rate-limits
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 40.9
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Splunk Soar Authentication
  slug: splunk-soar-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Splunk Soar Domain Security
  slug: splunk-soar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Splunk Soar Vulnerability Disclosure
  slug: splunk-soar-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Splunk Soar Trust Center
  slug: splunk-soar-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: splunk-soar
tags:
- Security
- SOAR
- Automation
- Orchestration
- Incident Response
- SOC
- Security Operations
- Playbooks
- Case Management
- Threat Intelligence
website: https://help.splunk.com/en/splunk-soar/soar-cloud
---
