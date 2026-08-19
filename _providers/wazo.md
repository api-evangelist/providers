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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 540
  human_in_the_loop: 26
  name: Wazo Agentic Access
  operation_count: 932
  slug: wazo-agentic-access
  summary_line: 932 operations · 540 acting · 26 human-in-the-loop
api_count: 14
apis:
- description: 'Authentication and authorisation service for the Wazo Platform. Issues and validates X-Auth-Token tokens (username/password, LDAP, SAML and external identity providers including Google, Microsoft and '
  name: Wazo Authentication API (wazo-auth)
  slug: wazo-authentication-api-wazo-auth
- description: 'The configuration API for a Wazo stack and the largest of its microservice contracts. Manages users, lines, extensions, SIP/IAX/SCCP/custom endpoints, devices, contexts, groups, queues, agents, IVRs, '
  name: Wazo Configuration API (wazo-confd)
  slug: wazo-configuration-api-wazo-confd
- description: Runtime call control for the Wazo Platform. Originate, answer, hold, mute, transfer, relocate, record and hang up calls; drive adhoc conferences, conferences, meetings, faxes, voicemails, switchboards
  name: Wazo Call Control / Application API (wazo-calld)
  slug: wazo-call-control-application-api-wazo-calld
- description: Call Detail Record and contact-centre reporting API. Retrieves and exports CDRs (JSON, CSV) for a tenant or the authenticated user, recordings and voicemail transcription, retention configuration, and
  name: Wazo Call Detail Records API (wazo-call-logd)
  slug: wazo-call-detail-records-api-wazo-call-logd
- description: Directory lookup, reverse lookup and personal-contact service. Aggregates multiple directory backends (CSV, CSV web service, LDAP, Wazo confd, Google, Microsoft Office 365, conference and personal sou
  name: Wazo Directory & Contacts API (wazo-dird)
  slug: wazo-directory-contacts-api-wazo-dird
- description: Phone auto-provisioning service. Manages device plugins, configuration templates, device registrations, DHCP integration and the plugin repository used to provision desk phones and ATAs from vendors s
  name: Wazo Phone Provisioning API (wazo-provd)
  slug: wazo-phone-provisioning-api-wazo-provd
- description: Webhook subscription service. Connects to the Wazo event bus and relays platform events to external HTTP endpoints; manages tenant-wide and per-user subscriptions, the available relay services, mobile
  name: Wazo Webhooks API (wazo-webhookd)
  slug: wazo-webhooks-api-wazo-webhookd
- description: Plugin management microservice. Installs, upgrades and uninstalls Wazo plugins from a git or market source, exposes the plugin market and the list of installed plugins, and reports asynchronous instal
  name: Wazo Plugin Management API (wazo-plugind)
  slug: wazo-plugin-management-api-wazo-plugind
- description: Call-centre agent state API. Logs agents in and out of queues by agent id, agent number or extension, pauses and unpauses them, relogs all agents, and reports per-agent and tenant-wide agent status.
  name: Wazo Call Centre Agent API (wazo-agentd)
  slug: wazo-call-centre-agent-api-wazo-agentd
- description: Presence and chat microservice. Tracks user, line and refresh-token presence (including Microsoft Teams presence federation), and manages chat rooms and messages for the authenticated user.
  name: Wazo Presence & Chat API (wazo-chatd)
  slug: wazo-presence-chat-api-wazo-chatd
- description: Directory and service endpoints consumed directly by desk phones. Serves vendor-specific XML/HTML phone directory lookups and phone service actions (DND, call forward) for Aastra/Mitel, Cisco, Fanvil,
  name: Wazo Phone Directory & Service API (wazo-phoned)
  slug: wazo-phone-directory-service-api-wazo-phoned
- description: Initial system setup API. Performs the one-time bootstrap of a freshly installed Wazo stack — engine configuration, tenant creation and the first administrative credentials.
  name: Wazo Initial Setup API (wazo-setupd)
  slug: wazo-initial-setup-api-wazo-setupd
- description: A thin REST facade over the Asterisk Manager Interface. Executes AMI actions and Asterisk CLI commands, and republishes AMI events onto the Wazo bus. Internal-platform surface, not intended for direct
  name: Wazo Asterisk Manager Interface API (wazo-amid)
  slug: wazo-asterisk-manager-interface-api-wazo-amid
- description: WebSocket gateway onto the Wazo internal event bus. An authenticated client subscribes to named platform events (327 event types across confd, calld, agentd, dird, amid, sysconfd and webhookd) and rec
  name: Wazo Websocket Event Stream (wazo-websocketd)
  slug: wazo-websocket-event-stream-wazo-websocketd
artifact_total: 32
asyncapis:
- description: ''
  name: wazo-agentd events
  slug: wazo-agentd-asyncapi
- description: ''
  name: wazo-amid events
  slug: wazo-amid-asyncapi
- description: ''
  name: wazo-auth events
  slug: wazo-auth-asyncapi
- description: ''
  name: wazo-call_logd events
  slug: wazo-call-logd-asyncapi
- description: ''
  name: wazo-calld events
  slug: wazo-calld-asyncapi
- description: ''
  name: wazo-chatd events
  slug: wazo-chatd-asyncapi
- description: ''
  name: wazo-confd events
  slug: wazo-confd-asyncapi
- description: ''
  name: wazo-dird events
  slug: wazo-dird-asyncapi
- description: ''
  name: Wazo Events Webhooks
  slug: wazo-events-webhooks
- description: ''
  name: wazo-plugind events
  slug: wazo-plugind-asyncapi
- description: ''
  name: wazo-sysconfd events
  slug: wazo-sysconfd-asyncapi
- description: ''
  name: undefined events
  slug: wazo-unattributed-asyncapi
- description: ''
  name: wazo-webhookd events
  slug: wazo-webhookd-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wazo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wazo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wazo.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.wazo.io/
- group: start
  title: ''
  type: Portal
  url: https://developers.wazo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://wazo-platform.org/uc-doc/
- group: docs
  title: ''
  type: APIReference
  url: https://api.wazo.io/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://wazo-platform.org/uc-doc/api_sdk/rest_api/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://wazo-platform.org/uc-doc/api_sdk/rest_api/quickstart
- group: operate
  title: ''
  type: Support
  url: https://wazo-platform.discourse.group/
- group: operate
  title: ''
  type: Community
  url: https://mm.wazo.community/wazo-platform/
- group: company
  title: ''
  type: Blog
  url: https://wazo-platform.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wazo-platform
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wazo-communication
- group: operate
  title: ''
  type: IssueTracker
  url: https://wazo-dev.atlassian.net/
- group: start
  title: ''
  type: SignUp
  url: https://wazo.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wazo.io/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wazo.io/privacy
- group: other
  title: ''
  type: Download
  url: https://wazo.io/download
- group: other
  title: ''
  type: Ecosystem
  url: https://wazo-platform.org/ecosystem/
- group: learn
  title: ''
  type: Tutorials
  url: https://wazo-platform.org/tutorials/
- group: build
  title: ''
  type: Packages
  url: packages/wazo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wazo-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wazo-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/wazo-acl-permissions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wazo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wazo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wazo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wazo-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://wazo-platform.org/uc-doc/api_sdk/rest_api/changelog
- group: design
  title: ''
  type: Conformance
  url: conformance/wazo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wazo-data-model.yml
- group: build
  title: ''
  type: CLI
  url: cli/wazo-cli.yml
- group: design
  title: ''
  type: Components
  url: components/wazo-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wazo-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://api.wazo.io/documentation/console/authentication/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wazo-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wazo-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/wazo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wazo-rate-limits.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-unattributed-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-agentd-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-amid-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-auth-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-call-logd-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-calld-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-chatd-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-confd-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-dird-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-plugind-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-sysconfd-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-webhookd-asyncapi.yml
created: '2026-08-17'
description: 'Wazo Communication Inc. builds the Wazo Platform, an open-source (GPL-3.0) programmable unified-communications and contact-centre platform assembled from Asterisk, Kamailio, RabbitMQ, PostgreSQL and nginx, which MSPs, carriers, telecom integrators and enterprises self-host or resell white-label as UCaaS. The platform is API-first: thirteen HTTP microservices — authentication, stack configuration (confd), runtime call control (calld), call detail records, directories, call-centre agents, presence and chat, phone auto-provisioning, webhooks, plugin management, the Asterisk Manager facade and initial setup — each publish their own Swagger 2.0 contract totalling 932 operations, share a single X-Auth-Token bearer model governed by 788 fine-grained ACL permissions, and emit 327 named events onto a RabbitMQ bus that wazo-webhookd relays as HTTP webhooks and wazo-websocketd streams over WebSocket. There is no public multi-tenant API host: every base URL is the customer''s own stack.'
image: https://wazo-platform.org/images/logo-black.svg
layout: provider
modified: '2026-08-17'
name: Wazo
nav: Providers
network: true
overview: 'Wazo publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Authentication API (wazo-auth), Configuration API (wazo-confd), Call Control / Application API (wazo-calld), and 11 more. Tagged areas include telephony, voip, unified-communications, ucaas, and contact-center.


  The Wazo catalog on APIs.io includes 13 event-driven AsyncAPI specifications.


  Wazo''s developer surface includes developer portal, documentation, API reference, getting-started guide, quickstart, support, engineering blog, and 46 more developer resources.'
plans:
- name: Wazo Plans Pricing
  plan_count: 0
  slug: wazo-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Wazo Rate Limits
  slug: wazo-rate-limits
score:
  band: developing
  composite: 42.4
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 56.7
    developer_ergonomics: 80.4
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 21.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: authentication
  name: Wazo Authentication
  slug: wazo-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Wazo Domain Security
  slug: wazo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wazo
tags:
- telephony
- voip
- unified-communications
- ucaas
- contact-center
- sip
- asterisk
- webrtc
- open-source
- self-hosted
- white-label
- pbx
- msp
- call-center
- provisioning
- webhooks
- event-driven
- chat
- presence
- cdr
website: https://wazo.io/
---
