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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'REST API for the Kenna / Cisco Vulnerability Management platform: manage assets, asset groups, applications, findings, fixes, vulnerabilities, vulnerability intelligence, connectors, data exports, das'
  name: Cisco Vulnerability Management API (Kenna)
  slug: cisco-vulnerability-management-api-kenna
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.kennasecurity.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.kennasecurity.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.kennasecurity.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.kennasecurity.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.kennasecurity.com/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://apidocs.kennasecurity.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://learn-cloudsecurity.cisco.com/vulnerability-management-resources
- group: operate
  title: ''
  type: Support
  url: https://help.kennasecurity.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kennasecurity.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KennaSecurity
- group: auth
  title: ''
  type: Authentication
  url: authentication/kenna-security-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kenna-security-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kenna-security-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://apidocs.kennasecurity.com/docs/getting-started-with-vulnerability-inference-v2
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kenna-security-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/kenna-security-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/kenna-security-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kenna-security-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kenna-security-domain-security.yml
created: '2026-07-17'
description: 'Kenna Security is the risk-based vulnerability management platform now part of Cisco as Cisco Vulnerability Management. Founded in Chicago and acquired by Cisco in 2021, the platform ingests scanner, asset, and threat-intelligence data to prioritize vulnerabilities by real-world exploitability and business risk. It exposes a REST API (the Kenna / Cisco Vulnerability Management API) at api.kennasecurity.com covering assets, asset groups, applications, findings, fixes, vulnerabilities, vulnerability intelligence, connectors, data exports, dashboards, metrics, roles, and users. The API uses an X-Risk-Token API-key header over HTTPS, page-number pagination, and JSON payloads. Kenna also publishes a first-party open-source Scripting Toolkit on GitHub for building connectors and integrations. Sector: cybersecurity / vulnerability management.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kenna-security.png
layout: provider
modified: '2026-07-19'
name: Kenna Security
nav: Providers
network: true
overview: 'Kenna Security publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Vulnerability Management, Risk-Based Prioritization, and Threat Intelligence.


  Kenna Security''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, support, authentication, and 12 more developer resources.'
random_paper: 72
score:
  band: emerging
  composite: 26.3
  delta: -0.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 26.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/screenshots/kenna-security-2026-07-25T223615.png
security:
- kind: authentication
  name: Kenna Security Authentication
  slug: kenna-security-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kenna Security Domain Security
  slug: kenna-security-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kenna-security
tags:
- Company
- Cybersecurity
- Vulnerability Management
- Risk-Based Prioritization
- Threat Intelligence
- Security
- Cisco
- REST API
website: https://www.kennasecurity.com
---
