---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: Contacts Management API for the Vodafone Business Messaging Hub, providing CRUD over contacts, lists and custom fields for SMS/MMS campaigns. Documented as an Apiary API Blueprint (project subdomain c
  name: TPG Telecom Messaging Hub Contacts API
  slug: tpg-telecom-messaging-hub-contacts-api
- description: The SMS/MMS REST API of the Vodafone Business Messaging Hub, listed on the product page as "Access to our REST API" on every plan tier. The API is live on the TPG-branded host https://api.messaging.tp
  name: TPG Telecom Messaging Hub REST API
  slug: tpg-telecom-messaging-hub-rest-api
artifact_total: 9
asyncapis:
- description: ''
  name: Tpg Telecom Messaging Webhooks
  slug: tpg-telecom-messaging-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tpg-telecom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tpg-telecom-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://www.tpgtelecom.com.au/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tpg-telecom-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tpg-telecom-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tpg-telecom-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tpg-telecom-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tpg-telecom-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/tpg-telecom-delivery-status-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tpg-telecom-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tpg-telecom-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.messaging.tpgtelecom.com.au
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tpg-telecom-messaging-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tpg-telecom-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/tpg-telecom-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tpg-telecom-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tpg-telecom-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tpg-telecom-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tpg-telecom-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://www.tpgtelecom.com.au/
- group: company
  title: ''
  type: About
  url: https://www.tpgtelecom.com.au/about-us
- group: docs
  title: ''
  type: Documentation
  url: https://support.messaging.tpgtelecom.com.au/hc/en-us
- group: start
  title: ''
  type: GettingStarted
  url: https://support.messaging.tpgtelecom.com.au/hc/en-us/sections/4656402628367-Quick-Start-Guides
- group: operate
  title: ''
  type: Support
  url: https://support.messaging.tpgtelecom.com.au/hc/en-us/articles/4783185128847-Contacting-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vodafone.com.au/business/messaging-hub
- group: start
  title: ''
  type: Login
  url: https://messaging.tpgtelecom.com.au/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tpgtelecom.com.au/website-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tpgtelecom.com.au/about-us/privacy
- group: commercial
  title: ''
  type: Legal
  url: https://www.tpgtelecom.com.au/legal
- group: company
  title: ''
  type: Press
  url: https://www.tpgtelecom.com.au/media_release
- group: company
  title: ''
  type: Careers
  url: https://www.tpgtelecom.com.au/careers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tpgtelecom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tpg-telecom/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.tpgtelecom.com.au/investor-relations
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-07-25'
description: 'TPG Telecom Limited is Australia''s second-largest telecommunications company and an ASX-listed mobile network operator and fixed broadband carrier, formed by the 2020 merger of Vodafone Hutchison Australia and TPG Corporation. It runs its own mobile network reaching 98.4% of the Australian population and sells under the Vodafone, TPG, iiNet, Internode, Lebara and felix brands, with business, enterprise, government and wholesale services consolidated under Vodafone Business. In the telecom API value chain TPG Telecom sits squarely on the network side and not the developer side: it publishes no first-party developer portal, no downloadable OpenAPI, and no network APIs. Its only public, callable developer surface is the Vodafone Business Messaging Hub — a white-labelled Sinch MessageMedia (Sinch Engage) CPaaS platform running on TPG-branded hosts at messaging.tpgtelecom.com.au and api.messaging.tpgtelecom.com.au, with documentation served from a Zendesk help centre and an Apiary
  API Blueprint owned by MessageMedia. On the sector''s defining signal, CAMARA and GSMA Open Gateway, TPG Telecom is a stated non-participant: while Telstra went live with Number Verification and SIM Swap through Aduna and Optus signalled it would follow, TPG''s public position is that it is "closely watching developments like GSMA Open Gateway" while prioritising local scam prevention — a watching brief, not an implementation. TPG Telecom is therefore partner-gated and aggregator-mediated: developers reach its network through a CPaaS supplier, not through TPG.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: 'TPG Telecom publishes no Model Context Protocol server, and none is listed in the official MCP registry or in the Messaging Hub help centre. One live finding is worth recording: the API gateway at api'
  name: TPG Telecom MCP Server
  slug: tpg-telecom-mcp-server
modified: '2026-07-25'
name: TPG Telecom
nav: Providers
network: true
overview: 'TPG Telecom publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Australia, Mobile Network Operator, Broadband, and Messaging.


  The TPG Telecom catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TPG Telecom''s developer surface includes authentication, documentation, getting-started guide, support, pricing, legal docs, and 30 more developer resources.'
plans:
- name: Tpg Telecom Plans
  plan_count: 5
  slug: tpg-telecom-plans
random_paper: 8
rate_limits:
- limit_count: 4
  name: Tpg Telecom Rate Limits
  slug: tpg-telecom-rate-limits
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 42.7
    developer_ergonomics: 47.0
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 63.2
  previous_composite: 51.6
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 51.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tpg-telecom/refs/heads/main/screenshots/tpg-telecom-2026-08-17T082417.png
security:
- kind: authentication
  name: Tpg Telecom Authentication
  slug: tpg-telecom-authentication
  summary_line: http/hmac · 3 schemes
- kind: domain-security
  name: Tpg Telecom Domain Security
  slug: tpg-telecom-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Tpg Telecom Vulnerability Disclosure
  slug: tpg-telecom-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tpg-telecom
tags:
- Telecommunications
- Australia
- Mobile Network Operator
- Broadband
- Messaging
- SMS
- IoT
- 5G
- Partner Gated
website: https://www.tpgtelecom.com.au/
---
