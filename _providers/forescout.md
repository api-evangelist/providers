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
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: 'The Web API plugin of the Forescout eyeExtend Connect Open Integration Module lets external systems query and act on the Forescout platform over HTTP. Clients authenticate at POST /api/login and pass '
  name: Forescout Web API (Open Integration Module)
  slug: forescout-web-api-open-integration-module
- description: REST API for the eyeInspect (SilentDefense) OT/ICS Command Center, providing access to asset inventory (hosts), alerts, vulnerabilities, sensors, and blacklists. Uses HTTP basic authentication against
  name: Forescout eyeInspect Command Center REST API
  slug: forescout-eyeinspect-command-center-rest-api
- description: Administrative REST API plugin for the Forescout eyeSight platform, used to manage appliance configuration and switch/device administration surfaced in the Forescout examples repository (admin-switch-
  name: Forescout eyeSight Admin API
  slug: forescout-eyesight-admin-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.forescout.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.forescout.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.forescout.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.forescout.com/bundle/web-api-1-5-3-h/page/web-api-1-5-3-h.RESTful-Web-Service-Interaction.html
- group: company
  title: ''
  type: Blog
  url: https://www.forescout.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Forescout
- group: build
  title: ''
  type: Postman
  url: https://github.com/Forescout/examples/tree/master/web-api/postman
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.forescout.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.forescout.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.forescout.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/forescout-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/forescout-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/forescout-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forescout-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/forescout-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/forescout-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/forescout-lifecycle.yml
created: '2026-07-17'
description: Forescout Technologies is a cybersecurity company specializing in automated cybersecurity for device visibility, control, and compliance across IT, OT/ICS, IoT, and IoMT environments. The Forescout Platform (eyeSight, eyeControl, eyeInspect, eyeExtend, and Risk & Exposure Management) discovers, classifies, assesses, and secures every connected asset on the network without requiring agents. Forescout exposes REST APIs for external integration through the Open Integration Module (OIM) of eyeExtend Connect — the Web API and Data Exchange (DEX) plugins — plus the eyeSight Admin API and the eyeInspect Command Center REST API, giving programmatic access to host inventory, network policies, alerts, and vulnerability data. First-party integration example code (Python, Node, and Postman collections) is published in the Forescout GitHub org.
image: https://www.forescout.com/wp-content/uploads/2021/09/forescout-logo.png
layout: provider
mcp_servers:
- description: ''
  name: forescout-mcp.yml
  slug: forescout-mcpyml
modified: '2026-07-19'
name: Forescout
nav: Providers
network: true
overview: 'Forescout publishes 1 API on the [APIs.io](https://apis.io/) network: Web API (Open Integration Module). Tagged areas include Company, Cybersecurity, Network Security, Device Visibility, and Asset Inventory.


  Forescout''s developer surface includes documentation, API reference, engineering blog, authentication, and 13 more developer resources.'
random_paper: 62
score:
  band: emerging
  composite: 24.4
  delta: -0.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 24.9
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/forescout/refs/heads/main/screenshots/forescout-2026-07-25T214933.png
security:
- kind: authentication
  name: Forescout Authentication
  slug: forescout-authentication
  summary_line: http · 4 schemes
- kind: domain-security
  name: Forescout Domain Security
  slug: forescout-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: forescout
tags:
- Company
- Cybersecurity
- Network Security
- Device Visibility
- Asset Inventory
- OT Security
- IoT Security
- Vulnerability Management
- Zero Trust
- REST API
website: https://www.forescout.com
---
