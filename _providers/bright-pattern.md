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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 127
  human_in_the_loop: 2
  name: Bright Pattern Agentic Access
  operation_count: 178
  slug: bright-pattern-agentic-access
  summary_line: 178 operations · 127 acting · 2 human-in-the-loop
api_count: 14
apis:
- description: The OAuth 2.0 Client Credentials Grant is used to authenticate clients of this API. The authenticated user is checked for having appropriate privileges to perform the requested operation. The complete
  name: Bright Pattern Authentication API
  slug: bright-pattern-authentication-api
- description: The Calling List API from Bright Pattern — 8 operation(s) for calling list.
  name: Bright Pattern Calling List API
  slug: bright-pattern-calling-list-api
- description: The Campaigns API from Bright Pattern — 27 operation(s) for campaigns.
  name: Bright Pattern Campaigns API
  slug: bright-pattern-campaigns-api
- description: Bright Pattern's List Management API makes it easy to manage the contents of Do Not Call (DNC) lists with bulk delete, add, and replace actions. The API methods described in this section fully support
  name: Bright Pattern DNC Lists API
  slug: bright-pattern-dnc-lists-api
- description: The Do Not Call List API from Bright Pattern — 4 operation(s) for do not call list.
  name: Bright Pattern Do Not Call List API
  slug: bright-pattern-do-not-call-list-api
- description: 'Bright Pattern''s List Management API provides the ability to manage Link Groups so several campaigns can be linked together. When processing all records of one campaign is finished, the next campaign '
  name: Bright Pattern Link Groups API
  slug: bright-pattern-link-groups-api
- description: 'Bright Pattern''s List Management API streamlines the creation and deletion of lists and formats and provides a convenient way to manage list records. Note: Performing operations on lists requires the '
  name: Bright Pattern Lists API
  slug: bright-pattern-lists-api
- description: The Methods API from Bright Pattern — 32 operation(s) for methods.
  name: Bright Pattern Methods API
  slug: bright-pattern-methods-api
- description: These methods are used to extract individual segments of multichannel call recordings (i.e., recordings where voice of each paricipating party is recorded into a separate audio file). The Get Multicha
  name: Bright Pattern Multichannel Call Recordings API
  slug: bright-pattern-multichannel-call-recordings-api
- description: 'With the https://:tenant/configapi/v2/phone endpoint you can: Get a list of all contact center users with their extensions and DID numbers Get a list of all access numbers with thier current assignmen'
  name: Bright Pattern Phones API
  slug: bright-pattern-phones-api
- description: These methods enable retrieval of regular voice recordings (i.e., recordings where voices of all participating parties are recorded in the same audio file) and the related call metadata. Both audio fi
  name: Bright Pattern Regular Call Recordings API
  slug: bright-pattern-regular-call-recordings-api
- description: These methods enable sending of SMS and MMS messages and checking the delivery status. The response parameters are explained below. Response parameters Parameter Description tenant_id Unique identifie
  name: Bright Pattern SMS/MMS Messaging API
  slug: bright-pattern-sms-mms-messaging-api
- description: The following methods allow tasks within Bright Pattern Contact Center to be queued, canceled, updated, and queried.
  name: Bright Pattern Task Routing API
  slug: bright-pattern-task-routing-api
- description: 'With the https://:tenant_url/configapi/v2/user endpoint you can: Create new users and define most of their attributes Update existing users Check and clear user lockout state Manage agents'' skills Del'
  name: Bright Pattern Users API
  slug: bright-pattern-users-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bright Pattern Authentication API
  slug: open-bright-pattern-authentication-api
- collection_type: open
  name: BPCC List Management API v2.0 Calling List API
  slug: open-bright-pattern-calling-list-api
- collection_type: open
  name: Bright Pattern Campaigns API
  slug: open-bright-pattern-campaigns-api
- collection_type: open
  name: Bright Pattern DNC Lists API
  slug: open-bright-pattern-dnc-lists-api
- collection_type: open
  name: BPCC List Management API v2.0 Do Not Call List API
  slug: open-bright-pattern-do-not-call-list-api
- collection_type: open
  name: BPCC List Management API v3.2 Link Groups API
  slug: open-bright-pattern-link-groups-api
- collection_type: open
  name: Bright Pattern Lists API
  slug: open-bright-pattern-lists-api
- collection_type: open
  name: Bright Pattern Methods API
  slug: open-bright-pattern-methods-api
- collection_type: open
  name: BPCC Interaction Content Multichannel Call Recordings API
  slug: open-bright-pattern-multichannel-call-recordings-api
- collection_type: open
  name: BPCC Configuration Phones API
  slug: open-bright-pattern-phones-api
- collection_type: open
  name: BPCC Interaction Content Regular Call Recordings API
  slug: open-bright-pattern-regular-call-recordings-api
- collection_type: open
  name: BPCC SMS/MMS SMS/MMS Messaging API
  slug: open-bright-pattern-sms-mms-messaging-api
- collection_type: open
  name: BPCC Task Routing API
  slug: open-bright-pattern-task-routing-api
- collection_type: open
  name: Bright Pattern Users API
  slug: open-bright-pattern-users-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bright-pattern-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bright-pattern-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bright-pattern-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bright-pattern-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bright-pattern-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.brightpattern.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.brightpattern.com/latest:Api
- group: docs
  title: ''
  type: Documentation
  url: https://help.brightpattern.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.brightpattern.com/latest:Api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.brightpattern.com/latest:Tutorials-for-admins/API/Access
- group: build
  title: ''
  type: Postman
  url: postman/bright-pattern-postman.yml
- group: operate
  title: ''
  type: Support
  url: https://www.brightpattern.com/contact-center-support/
- group: company
  title: ''
  type: Blog
  url: https://www.brightpattern.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.brightpattern.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ServicePattern
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brightpattern.com/call-center-software-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.brightpattern.com/contact-bright-pattern/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brightpattern.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brightpattern.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.brightpattern.com/compliance/
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.brightpattern.com/WhatsNew
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/bright-pattern-list-management-v3-2-openapi.yml
- group: build
  title: ''
  type: Packages
  url: packages/bright-pattern-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bright-pattern-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bright-pattern-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bright-pattern-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/bright-pattern-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bright-pattern-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bright-pattern-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bright-pattern-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/bright-pattern-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/bright-pattern-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bright-pattern-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bright-pattern-list-management-v3-2-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-08'
description: 'Bright Pattern is a cloud contact center (CCaaS) software company whose omnichannel platform routes voice, IVR, email, chat, SMS/MMS, video and social messenger conversations to agents, with built-in quality management, workforce management, outbound dialing and AI/bot assistance. The platform is multi-tenant: every customer contact center runs on its own tenant hostname, and Bright Pattern exposes nine public REST API families against that tenant — Configuration, SCIM-compliant user provisioning, List Management (v2, v3.0, v3.2), Task Routing, SMS/MMS, Interaction Content (call recordings and metadata), Real-Time Statistics, and the Mobile/Web Messaging APIs (v1 and v2) that back the iOS and Android Mobile SDKs. The public API reference is published as Postman documenter collections linked from the Bright Pattern documentation wiki.'
image: https://www.brightpattern.com/wp-content/uploads/2025/02/Brightpattern-Homepage-Logo.png
layout: provider
mcp_servers:
- description: ''
  name: bright-pattern-mcp.yml
  slug: bright-pattern-mcpyml
modified: '2026-08-08'
name: Bright Pattern
nav: Providers
network: true
overview: 'Bright Pattern publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Calling List API, Campaigns API, and 11 more. Tagged areas include Company, Contact Center, CCaaS, Customer Experience, and Omnichannel.


  Bright Pattern''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 28 more developer resources.'
random_paper: 2
score:
  band: strong
  composite: 56.1
  delta: 5.3
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 30.3
    contract_quality: 55.4
    developer_ergonomics: 70.8
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 18.4
  previous_composite: 50.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/bright-pattern/refs/heads/main/screenshots/bright-pattern-2026-08-17T080703.png
security:
- kind: authentication
  name: Bright Pattern Authentication
  slug: bright-pattern-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Bright Pattern Domain Security
  slug: bright-pattern-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Bright Pattern Trust Center
  slug: bright-pattern-trust-center
  summary_line: PCI DSS 3.2, SOC 2, HIPAA, GDPR, TCPA
slug: bright-pattern
tags:
- Company
- Contact Center
- CCaaS
- Customer Experience
- Omnichannel
- Call Center
- Telephony
- Messaging
- SMS
- Voice
- Customer Service
- Workforce Management
website: https://www.brightpattern.com/
---
