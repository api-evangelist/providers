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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 116
  human_in_the_loop: 6
  name: Ninjaone Agentic Access
  operation_count: 244
  slug: ninjaone-agentic-access
  summary_line: 244 operations · 116 acting · 6 human-in-the-loop
api_count: 22
apis:
- description: The Asset Tags API from NinjaOne — 6 operation(s) for asset tags.
  name: NinjaOne Asset Tags API
  slug: ninjaone-asset-tags-api
- description: Backup
  name: NinjaOne Backup API
  slug: ninjaone-backup-api
- description: Checklist Templates
  name: NinjaOne Checklist Templates API
  slug: ninjaone-checklist-templates-api
- description: Custom Fields
  name: NinjaOne Custom Fields API
  slug: ninjaone-custom-fields-api
- description: The Custom Tabs API from NinjaOne — 13 operation(s) for custom tabs.
  name: NinjaOne Custom Tabs API
  slug: ninjaone-custom-tabs-api
- description: Devices
  name: NinjaOne devices API
  slug: ninjaone-devices-api
- description: Document Templates
  name: NinjaOne Document Templates API
  slug: ninjaone-document-templates-api
- description: Groups/Search
  name: NinjaOne groups API
  slug: ninjaone-groups-api
- description: Knowledge Base Articles
  name: NinjaOne Knowledge Base Articles API
  slug: ninjaone-knowledge-base-articles-api
- description: Location
  name: NinjaOne Location API
  slug: ninjaone-location-api
- description: Management
  name: NinjaOne management API
  slug: ninjaone-management-api
- description: Organizations
  name: NinjaOne organization API
  slug: ninjaone-organization-api
- description: Organization Checklists
  name: NinjaOne Organization Checklists API
  slug: ninjaone-organization-checklists-api
- description: Organization Documents
  name: NinjaOne Organization Documents API
  slug: ninjaone-organization-documents-api
- description: Queries
  name: NinjaOne queries API
  slug: ninjaone-queries-api
- description: Related Items
  name: NinjaOne Related Items API
  slug: ninjaone-related-items-api
- description: Core system Entities and Resources
  name: NinjaOne system API
  slug: ninjaone-system-api
- description: ticketing
  name: NinjaOne ticketing API
  slug: ninjaone-ticketing-api
- description: The Unmanaged Devices API from NinjaOne — 2 operation(s) for unmanaged devices.
  name: NinjaOne Unmanaged Devices API
  slug: ninjaone-unmanaged-devices-api
- description: Users
  name: NinjaOne Users API
  slug: ninjaone-users-api
- description: Vulnerability Management
  name: NinjaOne Vulnerability Management API
  slug: ninjaone-vulnerability-management-api
- description: Webhook Endpoints
  name: NinjaOne webhooks API
  slug: ninjaone-webhooks-api
artifact_total: 30
asyncapis:
- description: ''
  name: Ninjaone Webhooks
  slug: ninjaone-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/ninjaone-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ninjaone-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ninjaone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ninjaone.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ninjaone.com/docs/application-programming-interface-api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ninjaone.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://app.ninjarmm.com/apidocs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ninjaone.com/docs/application-programming-interface-api/public-api-operations/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ninjaone-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ninjaone-scopes.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ninjaone.com/pricing/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.ninjaone.com/roadmap/
- group: company
  title: ''
  type: Blog
  url: https://www.ninjaone.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ninjaone.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ninjaone.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ninjaone.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ninjaone-lifecycle.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trustpage.ninjaone.com/
- group: auth
  title: ''
  type: Security
  url: https://www.ninjaone.com/.well-known/security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ninjaone-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/ninjaone-packages.yml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/ninjaone/ninjaone-api-workspace/collection/8gh1ujj/ninjaone-public-api-2-0
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ninjaone-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ninjaone-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ninjaone-security.txt
created: '2026-07-17'
description: NinjaOne is a unified IT operations and endpoint management platform for enterprise IT teams and managed service providers (MSPs), combining remote monitoring and management (RMM), endpoint management, patch management, remote access, backup, mobile device management, IT asset management, vulnerability management, endpoint security, IT documentation, and ticketing in a single cloud-native platform. Founded in 2013 as NinjaRMM, the company manages over five million endpoints across 30,000+ customers. The NinjaOne Public API 2.0 is an OAuth 2.0-secured REST API (client-credentials, authorization-code and refresh-token grants) that exposes organizations, devices, groups, queries, management actions, ticketing, users, locations, backup, custom fields, knowledge base, documents, checklists, vulnerability management, and webhooks for building integrations on top of the platform.
image: https://www.ninjaone.com/wp-content/uploads/2026/01/homepage-repositioning-social-share-1024x535.jpg
layout: provider
mcp_servers:
- description: ''
  name: ninjaone-mcp.yml
  slug: ninjaone-mcpyml
modified: '2026-07-20'
name: NinjaOne
nav: Providers
network: true
overview: 'NinjaOne publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Asset Tags API, Backup API, Checklist Templates API, and 19 more. Tagged areas include Company, Developer Tools, IT Management, RMM, and Endpoint Management.


  The NinjaOne catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  NinjaOne''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, engineering blog, and 20 more developer resources.'
random_paper: 30
scopes:
- name: Ninjaone Scopes
  scope_count: 4
  slug: ninjaone-scopes
  summary_line: 4 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 49.2
  delta: -2.4
  facets:
    commercial_clarity: 47.4
    contract_quality: 55.1
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Ninjaone Authentication
  slug: ninjaone-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Ninjaone Domain Security
  slug: ninjaone-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ninjaone Vulnerability Disclosure
  slug: ninjaone-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ninjaone Trust Center
  slug: ninjaone-trust-center
  summary_line: HIPAA, FedRAMP, GDPR
slug: ninjaone
tags:
- Company
- Developer Tools
- IT Management
- RMM
- Endpoint Management
- MSP
- IT Operations
- Monitoring
- Automation
- Ticketing
website: https://www.ninjaone.com/
---
