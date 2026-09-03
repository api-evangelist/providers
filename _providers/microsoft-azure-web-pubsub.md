---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Microsoft Azure Web Pubsub Agentic Access
  operation_count: 19
  slug: microsoft-azure-web-pubsub-agentic-access
  summary_line: 19 operations · 15 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: AsyncAPI 2.6 description of the Azure Web PubSub client WebSocket subprotocols (json.webpubsub.azure.v1 and json.reliable.webpubsub.azure.v1) and the CloudEvents 1.0 HTTP upstream contract used by the
  name: Azure Web PubSub Client and Upstream Events
  slug: azure-web-pubsub-client-and-upstream-events
- description: REST API for managing hub configurations within a Web PubSub instance. Hubs provide logical isolation for messaging and allow per-hub configuration of event handlers, anonymous connect policies, and a
  name: Azure Web PubSub Hubs REST API
  slug: azure-web-pubsub-hubs-rest-api
- description: REST API for managing Azure Web PubSub for Socket.IO instances. Provides a fully managed Socket.IO server replacement that allows existing Socket.IO applications to scale to millions of connections wi
  name: Azure Web PubSub for Socket.IO REST API
  slug: azure-web-pubsub-for-socketio-rest-api
- description: REST API for managing private endpoint connections to a Web PubSub service instance. Enables secure, private connectivity from virtual networks to Web PubSub through Azure Private Link without exposin
  name: Azure Web PubSub Private Endpoint Connections REST API
  slug: azure-web-pubsub-private-endpoint-connections-rest-api
- description: REST API for managing shared private link resources for a Web PubSub service. Enables outbound private connectivity from Web PubSub to other Azure resources such as Key Vault and Storage when configur
  name: Azure Web PubSub Shared Private Link Resources REST API
  slug: azure-web-pubsub-shared-private-link-resources-rest-api
- baseURL: https://{instance}.webpubsub.azure.com
  baseurl_source: declared
  description: Generate JWT tokens for client connections
  name: Azure Web PubSub ClientToken API
  slug: microsoft-azure-web-pubsub-clienttoken-api
- baseURL: https://{instance}.webpubsub.azure.com
  baseurl_source: declared
  description: Send messages and manage connections, groups, and users in a hub
  name: Azure Web PubSub Hub API
  slug: microsoft-azure-web-pubsub-hub-api
- baseURL: https://{instance}.webpubsub.azure.com
  baseurl_source: declared
  description: Permission management for client connections
  name: Azure Web PubSub Permission API
  slug: microsoft-azure-web-pubsub-permission-api
arazzos:
- description: Verify a connection exists before closing it, branching on whether it is present.
  name: Azure Web PubSub Check then Close Connection
  slug: microsoft-azure-web-pubsub-check-then-close-connection-workflow
- description: Confirm a connection exists, then send a targeted message to just that connection.
  name: Azure Web PubSub Direct Connection Message
  slug: microsoft-azure-web-pubsub-direct-connection-message-workflow
- description: Grant a connection a group permission, then deliver a message to that user.
  name: Azure Web PubSub Grant Permission then Send to User
  slug: microsoft-azure-web-pubsub-grant-permission-and-send-to-user-workflow
- description: Check whether a connection already holds a permission, granting it only when absent.
  name: Azure Web PubSub Grant Permission if Missing
  slug: microsoft-azure-web-pubsub-grant-permission-if-missing-workflow
- description: Only broadcast to a group when it currently has connected members.
  name: Azure Web PubSub Broadcast to Group if Active
  slug: microsoft-azure-web-pubsub-group-broadcast-if-active-workflow
- description: Broadcast a final warning to a group, then close every connection in that group.
  name: Azure Web PubSub Warn Group and Tear Down
  slug: microsoft-azure-web-pubsub-group-warn-and-teardown-workflow
- description: Add a connection to a group, broadcast a message to that group, then remove the connection.
  name: Azure Web PubSub Join Group, Send, then Leave
  slug: microsoft-azure-web-pubsub-join-group-and-send-workflow
- description: Send a user a message only when they currently have at least one live connection.
  name: Azure Web PubSub Notify User if Online
  slug: microsoft-azure-web-pubsub-notify-user-if-online-workflow
- description: Mint a client token, add the connection to a group, and announce the join to that group.
  name: Azure Web PubSub Provision Client and Join Group
  slug: microsoft-azure-web-pubsub-provision-client-and-join-group-workflow
- description: Revoke a connection's group permission, then forcibly close that connection.
  name: Azure Web PubSub Revoke Permission and Evict Connection
  slug: microsoft-azure-web-pubsub-revoke-permission-and-evict-workflow
- description: Mint a client access token for a hub and immediately broadcast a message to every connection.
  name: Azure Web PubSub Generate Token then Broadcast
  slug: microsoft-azure-web-pubsub-token-then-broadcast-workflow
- description: Add a user to a group and welcome them with a targeted message in one flow.
  name: Azure Web PubSub Onboard User to Group
  slug: microsoft-azure-web-pubsub-user-onboard-to-group-workflow
artifact_total: 36
asyncapis:
- description: Azure Web PubSub is a fully managed real-time messaging service from Microsoft Azure that lets clients exchange publish/subscribe messages over WebSockets without operating WebSocket infrastructure. C
  name: Azure Web PubSub
  slug: microsoft-azure-web-pubsub-asyncapi
collections:
- collection_type: postman
  name: Azure Web PubSub Service Data Plane REST ClientToken API
  slug: postman-microsoft-azure-web-pubsub-clienttoken-api
- collection_type: postman
  name: Azure Web PubSub Service Data Plane REST ClientToken Hub API
  slug: postman-microsoft-azure-web-pubsub-hub-api
- collection_type: postman
  name: Azure Web PubSub Service Data Plane REST ClientToken Permission API
  slug: postman-microsoft-azure-web-pubsub-permission-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Web PubSub Service Data Plane REST ClientToken API
  slug: open-microsoft-azure-web-pubsub-clienttoken-api
- collection_type: open
  name: Azure Web PubSub Service Data Plane REST ClientToken Hub API
  slug: open-microsoft-azure-web-pubsub-hub-api
- collection_type: open
  name: Azure Web PubSub Service Data Plane REST ClientToken Permission API
  slug: open-microsoft-azure-web-pubsub-permission-api
- collection_type: open
  name: Azure Web PubSub Service Data Plane REST API
  slug: open-microsoft-azure-web-pubsub
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-web-pubsub/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-web-pubsub-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-web-pubsub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-web-pubsub-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-web-pubsub-check-then-close-connection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-web-pubsub-direct-connection-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-web-pubsub-grant-permission-and-send-to-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-web-pubsub-grant-permission-if-missing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-web-pubsub-group-broadcast-if-active-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-web-pubsub-group-warn-and-teardown-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-web-pubsub-join-group-and-send-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-web-pubsub-notify-user-if-online-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-web-pubsub-provision-client-and-join-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-web-pubsub-revoke-permission-and-evict-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-web-pubsub-token-then-broadcast-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-web-pubsub-user-onboard-to-group-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/web-pubsub
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-generate-client-tokens
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/web-pubsub/
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://azure.microsoft.com/en-us/support/legal/sla/web-pubsub/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/azure-sdk/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/options/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free
- group: start
  title: ''
  type: Login
  url: https://portal.azure.com
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-server-sdk-js
- group: build
  title: ''
  type: SDK - JavaScript
  url: https://www.npmjs.com/package/@azure/web-pubsub
- group: build
  title: ''
  type: SDK - Python
  url: https://pypi.org/project/azure-messaging-webpubsubservice/
- group: build
  title: ''
  type: SDK - .NET
  url: https://www.nuget.org/packages/Azure.Messaging.WebPubSub
- group: build
  title: ''
  type: SDK - Java
  url: https://learn.microsoft.com/en-us/java/api/overview/azure/messaging-webpubsub-readme
- group: build
  title: ''
  type: SDK - Go
  url: https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/messaging/azwebpubsub
- group: build
  title: ''
  type: CLI Tools
  url: https://learn.microsoft.com/en-us/cli/azure/webpubsub
- group: operate
  title: ''
  type: ChangeLog
  url: https://azure.microsoft.com/en-us/updates/?product=web-pubsub
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: build
  title: ''
  type: GitHub Samples
  url: https://github.com/Azure/azure-webpubsub
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-webpubsub
- group: operate
  title: ''
  type: Community
  url: https://learn.microsoft.com/en-us/answers/tags/371/azure-web-pubsub
- group: operate
  title: ''
  type: FAQ
  url: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/resource-faq
- group: operate
  title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/concept-billing-model
created: '2026-03-13'
description: Azure Web PubSub is a fully-managed service that enables building real-time, two-way messaging applications using publish-subscribe patterns over WebSockets. It supports broadcasting messages to clients in groups, sending messages to specific connections or users, and integrating with serverless event handlers for scalable real-time experiences.
finops:
- name: Microsoft Azure Web Pubsub Finops
  service_category: API
  slug: microsoft-azure-web-pubsub-finops
image: https://azure.microsoft.com/svghandler/web-pubsub/
layout: provider
modified: '2026-05-30'
name: Azure Web PubSub
nav: Providers
network: true
overview: 'Azure Web PubSub publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Client and Upstream Events, ClientToken API, Hub API, and 1 more. Tagged areas include Messaging, Pub-Sub, Real-Time, Serverless, and WebSockets.


  The Azure Web PubSub catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Azure Web PubSub''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, support, and 37 more developer resources.'
plans:
- name: Microsoft Azure Web Pubsub Plans Pricing
  plan_count: 3
  slug: microsoft-azure-web-pubsub-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Microsoft Azure Web Pubsub Rate Limits
  slug: microsoft-azure-web-pubsub-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Azure Web PubSub API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: microsoft-azure-web-pubsub-asyncapi-spectral-rules
score:
  band: developing
  composite: 52.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 64.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 13.6
    contract_quality: 58.3
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 42.1
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-web-pubsub/refs/heads/main/screenshots/microsoft-azure-web-pubsub-2026-06-20T185444.png
security:
- kind: authentication
  name: Microsoft Azure Web Pubsub Authentication
  slug: microsoft-azure-web-pubsub-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Azure Web Pubsub Domain Security
  slug: microsoft-azure-web-pubsub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-web-pubsub
tags:
- Messaging
- Pub-Sub
- Real-Time
- Serverless
- WebSockets
website: https://azure.microsoft.com/en-us/products/web-pubsub
---
