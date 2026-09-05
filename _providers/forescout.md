---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
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
artifact_total: 5
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
  type: X-MCPServerCandidate
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
modified: '2026-07-19'
name: Forescout
nav: Providers
network: true
overview: 'Forescout publishes 1 API on the [APIs.io](https://apis.io/) network: Web API (Open Integration Module). Tagged areas include Company, Cybersecurity, Network Security, Device Visibility, and Asset Inventory.


  Forescout''s developer surface includes documentation, API reference, engineering blog, authentication, and 13 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 22.5
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
