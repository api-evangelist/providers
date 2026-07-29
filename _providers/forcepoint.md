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
api_count: 4
apis:
- description: Config, Log export, and IP APIs plus SCIM 2.0 user/group provisioning for Forcepoint ONE / Data Security Cloud (SSE). OAuth 2.0 bearer authentication with configurable permission scopes.
  name: Forcepoint Data Security Cloud | SSE REST API
  slug: forcepoint-data-security-cloud-sse-rest-api
- description: REST API for Forcepoint Data Loss Prevention policy management; JSON over HTTP(S).
  name: Forcepoint DLP REST API
  slug: forcepoint-dlp-rest-api
- description: RESTful Security Management Center (SMC) API for Forcepoint Next-Generation Firewall — engines, network elements, and policy automation (JSON/XML). API-key authentication via an SMC API Client.
  name: Forcepoint NGFW SMC API
  slug: forcepoint-ngfw-smc-api
- description: REST API for managing Forcepoint appliances (basic auth over HTTP(S)).
  name: Forcepoint Appliance REST API
  slug: forcepoint-appliance-rest-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://forcepoint.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.forcepoint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.forcepoint.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.forcepoint.com/dlp/90/restapi/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Forcepoint
- group: operate
  title: ''
  type: Support
  url: https://support.forcepoint.com/
- group: company
  title: ''
  type: Blog
  url: https://www.forcepoint.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.forcepoint.com/legal/website-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.forcepoint.com/company/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.forcepoint.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/forcepoint-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.forcepoint.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/forcepoint-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/forcepoint-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/forcepoint-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/forcepoint-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/forcepoint-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forcepoint-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/forcepoint-llms.txt
created: '2026-07-17'
description: 'Forcepoint is a data-first cybersecurity vendor whose platform spans Data Loss Prevention (DLP), Security Service Edge / SASE (Forcepoint ONE and Data Security Cloud | SSE), Next-Generation Firewall (NGFW), and web, email, and data security. For developers and security engineers Forcepoint exposes several product REST APIs — DLP policy management, SSE Config/Log/IP and SCIM 2.0 provisioning, the NGFW Security Management Center (SMC) API, and an Appliance management API — documented on help.forcepoint.com. Auth varies by product: OAuth 2.0 bearer tokens for SSE, API-key clients for the NGFW SMC, and basic/session auth for DLP and appliances. Forcepoint publishes official automation tooling including the fp-NGFW-SMC-python SDK (PyPI), Ansible modules, and a Terraform provider, and runs a public status portal and trust center (SOC 2, ISO 27001/27017/27018, CSA STAR, FIPS 140, GDPR).'
image: https://logo.clearbit.com/forcepoint.com
layout: provider
modified: '2026-07-19'
name: Forcepoint
nav: Providers
network: true
overview: 'Forcepoint publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Security, Data Loss Prevention, and SASE.


  Forcepoint''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 14 more developer resources.'
random_paper: 54
score:
  band: thin
  composite: 29.3
  delta: -0.4
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 81.5
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 29.7
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/forcepoint/refs/heads/main/screenshots/forcepoint-2026-07-25T214926.png
security:
- kind: authentication
  name: Forcepoint Authentication
  slug: forcepoint-authentication
  summary_line: oauth2/apiKey/http · 4 schemes
- kind: domain-security
  name: Forcepoint Domain Security
  slug: forcepoint-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Forcepoint Trust Center
  slug: forcepoint-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, GDPR, CSA STAR, FIPS 140
slug: forcepoint
tags:
- Company
- Cybersecurity
- Security
- Data Loss Prevention
- SASE
- Security Service Edge
- Firewall
- Data Security
- Cloud Security
website: https://forcepoint.com
---
