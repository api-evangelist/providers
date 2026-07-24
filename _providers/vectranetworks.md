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
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
api_count: 17
apis:
- description: Dedicated endpoint to Accounts.
  name: Vectra AI Accounts API
  slug: vectranetworks-accounts-api
- description: Dedicated endpoint to Assignment Outcomes.
  name: Vectra AI Assignment Outcomes API
  slug: vectranetworks-assignment-outcomes-api
- description: Dedicated endpoint to Assignments.
  name: Vectra AI Assignments API
  slug: vectranetworks-assignments-api
- description: Dedicated endpoint to Detections.
  name: Vectra AI Detections API
  slug: vectranetworks-detections-api
- description: The Entities API from Vectra AI — 4 operation(s) for entities.
  name: Vectra AI Entities API
  slug: vectranetworks-entities-api
- description: The Events API from Vectra AI — 3 operation(s) for events.
  name: Vectra AI Events API
  slug: vectranetworks-events-api
- description: The Groups API from Vectra AI — 1 operation(s) for groups.
  name: Vectra AI Groups API
  slug: vectranetworks-groups-api
- description: The Health API from Vectra AI — 1 operation(s) for health.
  name: Vectra AI Health API
  slug: vectranetworks-health-api
- description: Dedicated endpoint to Hosts.
  name: Vectra AI Hosts API
  slug: vectranetworks-hosts-api
- description: The Lockdown API from Vectra AI — 1 operation(s) for lockdown.
  name: Vectra AI Lockdown API
  slug: vectranetworks-lockdown-api
- description: The Match API from Vectra AI — 7 operation(s) for match.
  name: Vectra AI Match API
  slug: vectranetworks-match-api
- description: Manage entities notes
  name: Vectra AI Notes API
  slug: vectranetworks-notes-api
- description: Dedicated endpoint to Proxies
  name: Vectra AI Proxies API
  slug: vectranetworks-proxies-api
- description: Dedicated endpoint to run searches among entities
  name: Vectra AI Search API
  slug: vectranetworks-search-api
- description: Dedicated endpoint to manage entities's tags
  name: Vectra AI Tagging API
  slug: vectranetworks-tagging-api
- description: The threatFeeds endpoint can be used to automate the upload of STIX files for threat intelligence matching. This endpoint can also be used to retrieve the current list of threatFeed objects already co
  name: Vectra AI Threat Feeds API
  slug: vectranetworks-threat-feeds-api
- description: Dedicated endpoint to Users.
  name: Vectra AI Users API
  slug: vectranetworks-users-api
artifact_total: 22
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vectranetworks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vectranetworks-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vectranetworks-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.vectra.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.vectra.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://support.vectra.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vectra.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vectranetworks
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vectra.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vectra.ai/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vectra.ai/legal/terms-of-service
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vectranetworks-llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://support.vectra.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.vectra.ai/s/topic/0TO6S000000J745WAC/product-announcements
- group: build
  title: ''
  type: Packages
  url: packages/vectranetworks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vectranetworks-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vectranetworks-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vectranetworks-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vectranetworks-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vectranetworks-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vectranetworks-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vectranetworks-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vectranetworks-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vectranetworks-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Vectra AI (founded as Vectra Networks, a Khosla Ventures portfolio company) is an AI-native network detection and response (NDR) platform that correlates attacker behavior across network, identity, cloud, and SaaS domains. Its Attack Signal Intelligence prioritizes real threats for SOC teams, and the platform exposes REST APIs — the OAuth2-secured Vectra Platform API (RUX) and the token-based Vectra Detect API — for pulling detections, entities, and health data into SIEM, SOAR, EDR, and ITSM workflows.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vectranetworks.png
layout: provider
mcp_servers:
- description: ''
  name: vectranetworks-mcp.yml
  slug: vectranetworks-mcpyml
modified: '2026-07-21'
name: Vectra AI
nav: Providers
network: true
overview: 'Vectra AI publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Assignment Outcomes API, Assignments API, and 14 more. Tagged areas include Company, Cybersecurity, Network Detection and Response, Threat Detection, and Security Operations.


  Vectra AI''s developer surface includes authentication, engineering blog, support, pricing, documentation, changelog, and 19 more developer resources.'
random_paper: 8
scopes:
- name: Vectranetworks Scopes
  scope_count: 0
  slug: vectranetworks-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 44.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 49.3
    developer_ergonomics: 47.8
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 44.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Vectranetworks Authentication
  slug: vectranetworks-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Vectranetworks Domain Security
  slug: vectranetworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vectranetworks Trust Center
  slug: vectranetworks-trust-center
  summary_line: trust center published
slug: vectranetworks
tags:
- Company
- Cybersecurity
- Network Detection and Response
- Threat Detection
- Security Operations
- Artificial Intelligence
- SIEM
website: https://www.vectra.ai/
---
