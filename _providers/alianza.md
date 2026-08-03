---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 417
  human_in_the_loop: 14
  name: Alianza Agentic Access
  operation_count: 854
  slug: alianza-agentic-access
  summary_line: 854 operations · 417 acting · 14 human-in-the-loop
api_count: 1
apis:
- description: 'The Alianza Public API is the JSON REST web-service layer over the Alianza One cloud communications platform. Service providers use it to create and control every aspect of end-user accounts: partitio'
  name: Alianza Public API
  slug: alianza-public-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.alianza.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.alianza.com/home
- group: docs
  title: ''
  type: Documentation
  url: https://developer.alianza.com/api-guides
- group: docs
  title: ''
  type: APIReference
  url: https://developer.alianza.com/provisioning-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.alianza.com/web-services-datafeed-access
- group: company
  title: ''
  type: Blog
  url: https://www.alianza.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alianza-dev
- group: operate
  title: ''
  type: Support
  url: https://www.alianza.com/contact-us/
- group: start
  title: ''
  type: Login
  url: https://amp.alianza.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alianza.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alianza.com/privacy-policy/
- group: commercial
  title: ''
  type: Legal
  url: https://www.alianza.com/legal/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.alianza.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alianza-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alianza-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alianza-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alianza-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/alianza-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/alianza-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alianza-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/alianza-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/alianza-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alianza-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alianza-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alianza-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alianza-domain-security.yml
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/alianza_stock/
created: '2026-08-02'
description: Alianza is a cloud communications software company founded in 2009 and headquartered in Utah, providing a full-stack cloud voice and communications platform to more than 1,000 communications service providers across 81 countries. Its Intelligent Communications Fabric spans an experience layer, an orchestration layer, and an infrastructure layer, packaged as Alianza One (multi-tenant cloud voice), Alianza Core (physical, virtual and containerized network functions including MetaSphere, MaX UC, Perimeta SBC and Clearwater Core IMS), and Alianza Fusion (hosted core communications systems). Service providers use the platform for residential voice, business cloud communications, SIP trunking, business lines, managed specialty lines (POTS replacement), business text messaging, contact center, Microsoft Teams Direct Routing, robocall blocking and voice interconnect. The Alianza Public API is a JSON REST API over the Alianza One platform covering partition, account, end user, device,
  telephone number, porting, SIP trunk, calling plan, voicemail, CDR and reporting orchestration.
image: https://www.alianza.com/wp-content/uploads/2025/03/Alianza-Basic-Images-New.png
layout: provider
modified: '2026-08-02'
name: Alianza
nav: Providers
network: true
overview: 'Alianza publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Company, Communications, Cloud Communications, Voice, and VoIP.


  Alianza''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, legal docs, authentication, and 21 more developer resources.'
random_paper: 71
score:
  band: developing
  composite: 44.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 54.8
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Alianza Authentication
  slug: alianza-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Alianza Domain Security
  slug: alianza-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alianza
tags:
- Company
- Communications
- Cloud Communications
- Voice
- VoIP
- Telecommunications
- UCaaS
- SIP Trunking
- Telephone Numbers
- CPaaS
- Service Providers
website: https://www.alianza.com/
---
