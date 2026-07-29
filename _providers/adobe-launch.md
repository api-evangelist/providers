---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 65
  human_in_the_loop: 0
  name: Adobe Launch Agentic Access
  operation_count: 135
  slug: adobe-launch-agentic-access
  summary_line: 135 operations · 65 acting
api_count: 16
apis:
- description: Manage compiled tag library builds for deployment.
  name: Adobe Launch Builds API
  slug: adobe-launch-builds-api
- description: Manage webhook callbacks triggered by audit events.
  name: Adobe Launch Callbacks API
  slug: adobe-launch-callbacks-api
- description: Manage organization companies.
  name: Adobe Launch Companies API
  slug: adobe-launch-companies-api
- description: Manage data elements for server-side event processing.
  name: Adobe Launch Data Elements API
  slug: adobe-launch-data-elements-api
- description: Send event data directly to the Adobe Experience Platform Edge Network. Supports both interactive (interact) and non-interactive (collect) data collection with authenticated and non-authenticated mode
  name: Adobe Launch Edge Network API API
  slug: adobe-launch-edge-network-api-api
- description: Manage environments for event forwarding builds.
  name: Adobe Launch Environments API
  slug: adobe-launch-environments-api
- description: Manage extension packages that define capabilities, library modules, and views available to Adobe Experience Platform Tags users.
  name: Adobe Launch Extension Packages API
  slug: adobe-launch-extension-packages-api
- description: Manage extensions installed in event forwarding properties.
  name: Adobe Launch Extensions API
  slug: adobe-launch-extensions-api
- description: Manage hosting destinations for tag library delivery.
  name: Adobe Launch Hosts API
  slug: adobe-launch-hosts-api
- description: Manage libraries for event forwarding deployment.
  name: Adobe Launch Libraries API
  slug: adobe-launch-libraries-api
- description: Track media playback events through the Adobe Experience Platform Edge Network. Requires the Streaming Media Collection Add-on. Supports session management, play/pause tracking, buffering, and error r
  name: Adobe Launch Media Edge API API
  slug: adobe-launch-media-edge-api-api
- description: Manage event forwarding properties (edge platform).
  name: Adobe Launch Properties API
  slug: adobe-launch-properties-api
- description: Manage the individual event, condition, and action components within rules.
  name: Adobe Launch Rule Components API
  slug: adobe-launch-rule-components-api
- description: Manage server-side event forwarding rules.
  name: Adobe Launch Rules API
  slug: adobe-launch-rules-api
- description: Search across multiple resource types.
  name: Adobe Launch Search API
  slug: adobe-launch-search-api
- description: Manage secrets for authenticating event forwarding rules with external systems. Supports token, simple-http, oauth2, and oauth2-google types.
  name: Adobe Launch Secrets API
  slug: adobe-launch-secrets-api
arazzos:
- description: Verify a rule exists, add a new rule component to it, and list the rule's components to confirm.
  name: Adobe Launch Add a Component to an Existing Rule
  slug: adobe-launch-add-rule-component-workflow
- description: Read a property and inventory its rules, data elements, and installed extensions.
  name: Adobe Launch Audit a Property's Contents
  slug: adobe-launch-audit-property-contents-workflow
- description: Create a server-side event forwarding property, then add a rule and a data element to it.
  name: Adobe Launch Bootstrap an Event Forwarding Property
  slug: adobe-launch-bootstrap-event-forwarding-workflow
- description: Stand up a new Tags property, add a rule to it, and attach a first rule component.
  name: Adobe Launch Bootstrap a Property with a Rule
  slug: adobe-launch-bootstrap-property-rule-workflow
- description: Create a data element under a property, then read it back to confirm it persisted.
  name: Adobe Launch Create and Verify a Data Element
  slug: adobe-launch-create-and-verify-data-element-workflow
- description: Create a secret scoped to an environment on an event forwarding property, then read it back.
  name: Adobe Launch Create an Event Forwarding Secret
  slug: adobe-launch-create-event-forwarding-secret-workflow
- description: Find an extension package by name, install it into a property, and read the installed extension back.
  name: Adobe Launch Install an Extension from a Package
  slug: adobe-launch-install-extension-workflow
- description: Create a library, add a rule to it, kick off a build, and poll the build until it finishes.
  name: Adobe Launch Build a Library and Poll for Completion
  slug: adobe-launch-library-build-and-poll-workflow
- description: Create a delivery host on a property, then create an environment that uses it.
  name: Adobe Launch Provision a Host and Environment
  slug: adobe-launch-provision-environment-workflow
- description: Transition an existing library through submit and approve, then compile a build and poll it.
  name: Adobe Launch Submit, Approve, and Build a Library
  slug: adobe-launch-publish-library-workflow
- description: Register a callback on a property to receive build notifications, then read it back.
  name: Adobe Launch Register a Build Callback Webhook
  slug: adobe-launch-register-callback-workflow
- description: Find a library's most recent build, republish it, and poll until the republish completes.
  name: Adobe Launch Republish a Library's Latest Build
  slug: adobe-launch-republish-latest-build-workflow
- description: Search across Tags resources by name for a property, then retrieve the matched property in full.
  name: Adobe Launch Search for a Property and Fetch It
  slug: adobe-launch-search-and-fetch-property-workflow
artifact_total: 486
collections:
- collection_type: postman
  name: Adobe Experience Platform Data Collection API
  slug: postman-data-collection-api
- collection_type: postman
  name: Adobe Experience Platform Event Forwarding API
  slug: postman-event-forwarding-api
- collection_type: postman
  name: Adobe Launch Extension API
  slug: postman-extension-api
- collection_type: postman
  name: Adobe Launch Reactor API
  slug: postman-reactor-api
- collection_type: open
  name: Adobe Experience Platform Data Collection API
  slug: open-data-collection-api
- collection_type: open
  name: Adobe Experience Platform Event Forwarding API
  slug: open-event-forwarding-api
- collection_type: open
  name: Adobe Launch Extension API
  slug: open-extension-api
- collection_type: open
  name: Adobe Launch Reactor API
  slug: open-reactor-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adobe-launch-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-launch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adobe-launch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adobe-launch-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/adobe-launch/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-add-rule-component-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-audit-property-contents-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-bootstrap-event-forwarding-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-bootstrap-property-rule-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-create-and-verify-data-element-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-create-event-forwarding-secret-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-install-extension-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-library-build-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-provision-environment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-publish-library-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-register-callback-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-republish-latest-build-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-search-and-fetch-property-workflow.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy.html
- group: start
  title: ''
  type: Console
  url: https://developer.adobe.com/developer-console/
- group: start
  title: ''
  type: Portal
  url: https://developer.adobe.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adobe.com/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/adobetech
- group: company
  title: ''
  type: BlogRSS
  url: https://medium.com/feed/adobetech
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adobe
- group: start
  title: ''
  type: Signup
  url: https://developer.adobe.com/developer-console/
- group: auth
  title: ''
  type: Authentication
  url: https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-apis/api-authentication
- group: operate
  title: ''
  type: ChangeLog
  url: https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/latest
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@adobe/reactor-sdk
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@adobe/reactor-scaffold
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@adobe/reactor-sandbox
created: '2024-01-15'
description: Adobe Launch, now known as Adobe Experience Platform Tags, is a next-generation tag management system that unifies the client-side marketing ecosystem by empowering developers to build integrations on a robust, extensible platform that partners, clients, and the broader industry can build on and contribute to.
examples:
- key_count: 1
  name: Data Collection Collect Request Example
  slug: data-collection-collect-request-example
- key_count: 1
  name: Data Collection Collect Response Example
  slug: data-collection-collect-response-example
- key_count: 5
  name: Data Collection Error Response Example
  slug: data-collection-error-response-example
- key_count: 1
  name: Data Collection Interact Request Example
  slug: data-collection-interact-request-example
- key_count: 2
  name: Data Collection Interact Response Example
  slug: data-collection-interact-response-example
- key_count: 1
  name: Data Collection Media Error Request Example
  slug: data-collection-media-error-request-example
- key_count: 1
  name: Data Collection Media Event Request Example
  slug: data-collection-media-event-request-example
- key_count: 1
  name: Data Collection Media Session Start Request Example
  slug: data-collection-media-session-start-request-example
- key_count: 2
  name: Data Collection Media Session Start Response Example
  slug: data-collection-media-session-start-response-example
- key_count: 5
  name: Data Collection Xdm Event Example
  slug: data-collection-xdm-event-example
- key_count: 1
  name: Event Forwarding Data Element Create Request Example
  slug: event-forwarding-data-element-create-request-example
- key_count: 1
  name: Event Forwarding Data Element List Response Example
  slug: event-forwarding-data-element-list-response-example
- key_count: 4
  name: Event Forwarding Data Element Resource Example
  slug: event-forwarding-data-element-resource-example
- key_count: 0
  name: Event Forwarding Data Element Single Response Example
  slug: event-forwarding-data-element-single-response-example
- key_count: 1
  name: Event Forwarding Environment List Response Example
  slug: event-forwarding-environment-list-response-example
- key_count: 1
  name: Event Forwarding Environment Single Response Example
  slug: event-forwarding-environment-single-response-example
- key_count: 1
  name: Event Forwarding Error Response Example
  slug: event-forwarding-error-response-example
- key_count: 1
  name: Event Forwarding Extension List Response Example
  slug: event-forwarding-extension-list-response-example
- key_count: 1
  name: Event Forwarding Library Create Request Example
  slug: event-forwarding-library-create-request-example
- key_count: 1
  name: Event Forwarding Library List Response Example
  slug: event-forwarding-library-list-response-example
- key_count: 1
  name: Event Forwarding Library Single Response Example
  slug: event-forwarding-library-single-response-example
- key_count: 1
  name: Event Forwarding Pagination Meta Example
  slug: event-forwarding-pagination-meta-example
- key_count: 5
  name: Event Forwarding Property Attributes Example
  slug: event-forwarding-property-attributes-example
- key_count: 1
  name: Event Forwarding Property Create Request Example
  slug: event-forwarding-property-create-request-example
- key_count: 1
  name: Event Forwarding Property List Response Example
  slug: event-forwarding-property-list-response-example
- key_count: 3
  name: Event Forwarding Property Resource Example
  slug: event-forwarding-property-resource-example
- key_count: 0
  name: Event Forwarding Property Single Response Example
  slug: event-forwarding-property-single-response-example
- key_count: 1
  name: Event Forwarding Property Update Request Example
  slug: event-forwarding-property-update-request-example
- key_count: 2
  name: Event Forwarding Relationship Example
  slug: event-forwarding-relationship-example
- key_count: 1
  name: Event Forwarding Rule Create Request Example
  slug: event-forwarding-rule-create-request-example
- key_count: 1
  name: Event Forwarding Rule List Response Example
  slug: event-forwarding-rule-list-response-example
- key_count: 4
  name: Event Forwarding Rule Resource Example
  slug: event-forwarding-rule-resource-example
- key_count: 0
  name: Event Forwarding Rule Single Response Example
  slug: event-forwarding-rule-single-response-example
- key_count: 1
  name: Event Forwarding Rule Update Request Example
  slug: event-forwarding-rule-update-request-example
- key_count: 6
  name: Event Forwarding Secret Attributes Example
  slug: event-forwarding-secret-attributes-example
- key_count: 1
  name: Event Forwarding Secret Create Request Example
  slug: event-forwarding-secret-create-request-example
- key_count: 1
  name: Event Forwarding Secret List Response Example
  slug: event-forwarding-secret-list-response-example
- key_count: 3
  name: Event Forwarding Secret Resource Example
  slug: event-forwarding-secret-resource-example
- key_count: 0
  name: Event Forwarding Secret Single Response Example
  slug: event-forwarding-secret-single-response-example
- key_count: 1
  name: Event Forwarding Secret Update Request Example
  slug: event-forwarding-secret-update-request-example
- key_count: 1
  name: Extension Error Response Example
  slug: extension-error-response-example
- key_count: 12
  name: Extension Extension Attributes Example
  slug: extension-extension-attributes-example
- key_count: 1
  name: Extension Extension Install Request Example
  slug: extension-extension-install-request-example
- key_count: 1
  name: Extension Extension List Response Example
  slug: extension-extension-list-response-example
- key_count: 13
  name: Extension Extension Package Attributes Example
  slug: extension-extension-package-attributes-example
- key_count: 1
  name: Extension Extension Package List Response Example
  slug: extension-extension-package-list-response-example
- key_count: 4
  name: Extension Extension Package Resource Example
  slug: extension-extension-package-resource-example
- key_count: 0
  name: Extension Extension Package Single Response Example
  slug: extension-extension-package-single-response-example
- key_count: 1
  name: Extension Extension Package Update Request Example
  slug: extension-extension-package-update-request-example
- key_count: 4
  name: Extension Extension Resource Example
  slug: extension-extension-resource-example
- key_count: 1
  name: Extension Extension Revise Request Example
  slug: extension-extension-revise-request-example
- key_count: 0
  name: Extension Extension Single Response Example
  slug: extension-extension-single-response-example
- key_count: 1
  name: Extension Library List Response Example
  slug: extension-library-list-response-example
- key_count: 1
  name: Extension Pagination Meta Example
  slug: extension-pagination-meta-example
- key_count: 1
  name: Extension Property Single Response Example
  slug: extension-property-single-response-example
- key_count: 2
  name: Extension Relationship Example
  slug: extension-relationship-example
- key_count: 4
  name: Reactor Build Attributes Example
  slug: reactor-build-attributes-example
- key_count: 1
  name: Reactor Build List Response Example
  slug: reactor-build-list-response-example
- key_count: 4
  name: Reactor Build Resource Example
  slug: reactor-build-resource-example
- key_count: 0
  name: Reactor Build Single Response Example
  slug: reactor-build-single-response-example
- key_count: 4
  name: Reactor Callback Attributes Example
  slug: reactor-callback-attributes-example
- key_count: 1
  name: Reactor Callback Create Request Example
  slug: reactor-callback-create-request-example
- key_count: 1
  name: Reactor Callback List Response Example
  slug: reactor-callback-list-response-example
- key_count: 4
  name: Reactor Callback Resource Example
  slug: reactor-callback-resource-example
- key_count: 0
  name: Reactor Callback Single Response Example
  slug: reactor-callback-single-response-example
- key_count: 1
  name: Reactor Callback Update Request Example
  slug: reactor-callback-update-request-example
- key_count: 7
  name: Reactor Company Attributes Example
  slug: reactor-company-attributes-example
- key_count: 1
  name: Reactor Company List Response Example
  slug: reactor-company-list-response-example
- key_count: 4
  name: Reactor Company Resource Example
  slug: reactor-company-resource-example
- key_count: 0
  name: Reactor Company Single Response Example
  slug: reactor-company-single-response-example
- key_count: 13
  name: Reactor Data Element Attributes Example
  slug: reactor-data-element-attributes-example
- key_count: 1
  name: Reactor Data Element Create Request Example
  slug: reactor-data-element-create-request-example
- key_count: 1
  name: Reactor Data Element List Response Example
  slug: reactor-data-element-list-response-example
- key_count: 4
  name: Reactor Data Element Resource Example
  slug: reactor-data-element-resource-example
- key_count: 0
  name: Reactor Data Element Single Response Example
  slug: reactor-data-element-single-response-example
- key_count: 1
  name: Reactor Data Element Update Request Example
  slug: reactor-data-element-update-request-example
- key_count: 9
  name: Reactor Environment Attributes Example
  slug: reactor-environment-attributes-example
- key_count: 1
  name: Reactor Environment Create Request Example
  slug: reactor-environment-create-request-example
- key_count: 1
  name: Reactor Environment List Response Example
  slug: reactor-environment-list-response-example
- key_count: 4
  name: Reactor Environment Resource Example
  slug: reactor-environment-resource-example
- key_count: 0
  name: Reactor Environment Single Response Example
  slug: reactor-environment-single-response-example
- key_count: 1
  name: Reactor Environment Update Request Example
  slug: reactor-environment-update-request-example
- key_count: 1
  name: Reactor Error Response Example
  slug: reactor-error-response-example
- key_count: 12
  name: Reactor Extension Attributes Example
  slug: reactor-extension-attributes-example
- key_count: 1
  name: Reactor Extension Create Request Example
  slug: reactor-extension-create-request-example
- key_count: 1
  name: Reactor Extension List Response Example
  slug: reactor-extension-list-response-example
- key_count: 11
  name: Reactor Extension Package Attributes Example
  slug: reactor-extension-package-attributes-example
- key_count: 1
  name: Reactor Extension Package List Response Example
  slug: reactor-extension-package-list-response-example
- key_count: 3
  name: Reactor Extension Package Resource Example
  slug: reactor-extension-package-resource-example
- key_count: 0
  name: Reactor Extension Package Single Response Example
  slug: reactor-extension-package-single-response-example
- key_count: 4
  name: Reactor Extension Resource Example
  slug: reactor-extension-resource-example
- key_count: 0
  name: Reactor Extension Single Response Example
  slug: reactor-extension-single-response-example
- key_count: 1
  name: Reactor Extension Update Request Example
  slug: reactor-extension-update-request-example
- key_count: 11
  name: Reactor Host Attributes Example
  slug: reactor-host-attributes-example
- key_count: 1
  name: Reactor Host Create Request Example
  slug: reactor-host-create-request-example
- key_count: 1
  name: Reactor Host List Response Example
  slug: reactor-host-list-response-example
- key_count: 4
  name: Reactor Host Resource Example
  slug: reactor-host-resource-example
- key_count: 0
  name: Reactor Host Single Response Example
  slug: reactor-host-single-response-example
- key_count: 1
  name: Reactor Host Update Request Example
  slug: reactor-host-update-request-example
- key_count: 5
  name: Reactor Library Attributes Example
  slug: reactor-library-attributes-example
- key_count: 1
  name: Reactor Library Create Request Example
  slug: reactor-library-create-request-example
- key_count: 1
  name: Reactor Library List Response Example
  slug: reactor-library-list-response-example
- key_count: 4
  name: Reactor Library Resource Example
  slug: reactor-library-resource-example
- key_count: 0
  name: Reactor Library Single Response Example
  slug: reactor-library-single-response-example
- key_count: 1
  name: Reactor Library Update Request Example
  slug: reactor-library-update-request-example
- key_count: 1
  name: Reactor Pagination Meta Example
  slug: reactor-pagination-meta-example
- key_count: 12
  name: Reactor Property Attributes Example
  slug: reactor-property-attributes-example
- key_count: 1
  name: Reactor Property Create Request Example
  slug: reactor-property-create-request-example
- key_count: 1
  name: Reactor Property List Response Example
  slug: reactor-property-list-response-example
- key_count: 4
  name: Reactor Property Resource Example
  slug: reactor-property-resource-example
- key_count: 0
  name: Reactor Property Single Response Example
  slug: reactor-property-single-response-example
- key_count: 1
  name: Reactor Property Update Request Example
  slug: reactor-property-update-request-example
- key_count: 2
  name: Reactor Relationship Example
  slug: reactor-relationship-example
- key_count: 1
  name: Reactor Relationship Request Example
  slug: reactor-relationship-request-example
- key_count: 1
  name: Reactor Relationship Single Request Example
  slug: reactor-relationship-single-request-example
- key_count: 7
  name: Reactor Rule Attributes Example
  slug: reactor-rule-attributes-example
- key_count: 13
  name: Reactor Rule Component Attributes Example
  slug: reactor-rule-component-attributes-example
- key_count: 1
  name: Reactor Rule Component Create Request Example
  slug: reactor-rule-component-create-request-example
- key_count: 1
  name: Reactor Rule Component List Response Example
  slug: reactor-rule-component-list-response-example
- key_count: 4
  name: Reactor Rule Component Resource Example
  slug: reactor-rule-component-resource-example
- key_count: 0
  name: Reactor Rule Component Single Response Example
  slug: reactor-rule-component-single-response-example
- key_count: 1
  name: Reactor Rule Component Update Request Example
  slug: reactor-rule-component-update-request-example
- key_count: 1
  name: Reactor Rule Create Request Example
  slug: reactor-rule-create-request-example
- key_count: 1
  name: Reactor Rule List Response Example
  slug: reactor-rule-list-response-example
- key_count: 4
  name: Reactor Rule Resource Example
  slug: reactor-rule-resource-example
- key_count: 0
  name: Reactor Rule Single Response Example
  slug: reactor-rule-single-response-example
- key_count: 1
  name: Reactor Rule Update Request Example
  slug: reactor-rule-update-request-example
- key_count: 1
  name: Reactor Search Request Example
  slug: reactor-search-request-example
- key_count: 2
  name: Reactor Search Response Example
  slug: reactor-search-response-example
- key_count: 6
  name: Reactor Secret Attributes Example
  slug: reactor-secret-attributes-example
- key_count: 1
  name: Reactor Secret Create Request Example
  slug: reactor-secret-create-request-example
- key_count: 1
  name: Reactor Secret List Response Example
  slug: reactor-secret-list-response-example
- key_count: 4
  name: Reactor Secret Resource Example
  slug: reactor-secret-resource-example
- key_count: 0
  name: Reactor Secret Single Response Example
  slug: reactor-secret-single-response-example
- key_count: 1
  name: Reactor Secret Update Request Example
  slug: reactor-secret-update-request-example
features:
- Next-generation tag management for web and mobile
- Extensible platform with public extension marketplace
- Server-side event forwarding via Edge Network
- Rule-based data collection and routing
- Library versioning with staging and production environments
- JSON API specification-based programmatic management
- Real-time data collection to Edge Network
- Media tracking and analytics integration
finops:
- name: Adobe Launch Finops
  service_category: Tag Management
  slug: adobe-launch-finops
image: /assets/icons/adobe-launch.png
integrations:
- Adobe Analytics
- Adobe Target
- Adobe Audience Manager
- Adobe Experience Platform
- Google Analytics
- Facebook Pixel
- LinkedIn Insight Tag
- Custom JavaScript libraries
- Third-party marketing platforms
json_schemas:
- name: Adobe Experience Platform Tags Build
  property_count: 5
  slug: build
- name: CollectRequest
  property_count: 1
  slug: data-collection-collect-request
- name: CollectResponse
  property_count: 1
  slug: data-collection-collect-response
- name: ErrorResponse
  property_count: 5
  slug: data-collection-error-response
- name: InteractRequest
  property_count: 1
  slug: data-collection-interact-request
- name: InteractResponse
  property_count: 2
  slug: data-collection-interact-response
- name: MediaErrorRequest
  property_count: 1
  slug: data-collection-media-error-request
- name: MediaEventRequest
  property_count: 1
  slug: data-collection-media-event-request
- name: MediaSessionStartRequest
  property_count: 1
  slug: data-collection-media-session-start-request
- name: MediaSessionStartResponse
  property_count: 2
  slug: data-collection-media-session-start-response
- name: XDMEvent
  property_count: 5
  slug: data-collection-xdm-event
- name: Adobe Experience Platform Tags Data Element
  property_count: 5
  slug: data-element
- name: DataElementCreateRequest
  property_count: 1
  slug: event-forwarding-data-element-create-request
- name: DataElementListResponse
  property_count: 1
  slug: event-forwarding-data-element-list-response
- name: DataElementResource
  property_count: 4
  slug: event-forwarding-data-element-resource
- name: DataElementSingleResponse
  property_count: 0
  slug: event-forwarding-data-element-single-response
- name: EnvironmentListResponse
  property_count: 1
  slug: event-forwarding-environment-list-response
- name: EnvironmentSingleResponse
  property_count: 1
  slug: event-forwarding-environment-single-response
- name: ErrorResponse
  property_count: 1
  slug: event-forwarding-error-response
- name: ExtensionListResponse
  property_count: 1
  slug: event-forwarding-extension-list-response
- name: LibraryCreateRequest
  property_count: 1
  slug: event-forwarding-library-create-request
- name: LibraryListResponse
  property_count: 1
  slug: event-forwarding-library-list-response
- name: LibrarySingleResponse
  property_count: 1
  slug: event-forwarding-library-single-response
- name: PaginationMeta
  property_count: 1
  slug: event-forwarding-pagination-meta
- name: PropertyAttributes
  property_count: 5
  slug: event-forwarding-property-attributes
- name: PropertyCreateRequest
  property_count: 1
  slug: event-forwarding-property-create-request
- name: PropertyListResponse
  property_count: 1
  slug: event-forwarding-property-list-response
- name: PropertyResource
  property_count: 3
  slug: event-forwarding-property-resource
- name: PropertySingleResponse
  property_count: 0
  slug: event-forwarding-property-single-response
- name: PropertyUpdateRequest
  property_count: 1
  slug: event-forwarding-property-update-request
- name: Relationship
  property_count: 2
  slug: event-forwarding-relationship
- name: RuleCreateRequest
  property_count: 1
  slug: event-forwarding-rule-create-request
- name: RuleListResponse
  property_count: 1
  slug: event-forwarding-rule-list-response
- name: RuleResource
  property_count: 4
  slug: event-forwarding-rule-resource
- name: RuleSingleResponse
  property_count: 0
  slug: event-forwarding-rule-single-response
- name: RuleUpdateRequest
  property_count: 1
  slug: event-forwarding-rule-update-request
- name: SecretAttributes
  property_count: 6
  slug: event-forwarding-secret-attributes
- name: SecretCreateRequest
  property_count: 1
  slug: event-forwarding-secret-create-request
- name: SecretListResponse
  property_count: 1
  slug: event-forwarding-secret-list-response
- name: SecretResource
  property_count: 3
  slug: event-forwarding-secret-resource
- name: SecretSingleResponse
  property_count: 0
  slug: event-forwarding-secret-single-response
- name: SecretUpdateRequest
  property_count: 1
  slug: event-forwarding-secret-update-request
- name: ErrorResponse
  property_count: 1
  slug: extension-error-response
- name: ExtensionAttributes
  property_count: 12
  slug: extension-extension-attributes
- name: ExtensionInstallRequest
  property_count: 1
  slug: extension-extension-install-request
- name: ExtensionListResponse
  property_count: 1
  slug: extension-extension-list-response
- name: ExtensionPackageAttributes
  property_count: 13
  slug: extension-extension-package-attributes
- name: ExtensionPackageListResponse
  property_count: 1
  slug: extension-extension-package-list-response
- name: ExtensionPackageResource
  property_count: 4
  slug: extension-extension-package-resource
- name: ExtensionPackageSingleResponse
  property_count: 0
  slug: extension-extension-package-single-response
- name: ExtensionPackageUpdateRequest
  property_count: 1
  slug: extension-extension-package-update-request
- name: ExtensionResource
  property_count: 4
  slug: extension-extension-resource
- name: ExtensionReviseRequest
  property_count: 1
  slug: extension-extension-revise-request
- name: ExtensionSingleResponse
  property_count: 0
  slug: extension-extension-single-response
- name: LibraryListResponse
  property_count: 1
  slug: extension-library-list-response
- name: PaginationMeta
  property_count: 1
  slug: extension-pagination-meta
- name: PropertySingleResponse
  property_count: 1
  slug: extension-property-single-response
- name: Relationship
  property_count: 2
  slug: extension-relationship
- name: Adobe Experience Platform Tags Extension
  property_count: 5
  slug: extension
- name: Adobe Experience Platform Tags Library
  property_count: 6
  slug: library
- name: Adobe Experience Platform Tags Property
  property_count: 5
  slug: property
- name: BuildAttributes
  property_count: 4
  slug: reactor-build-attributes
- name: BuildListResponse
  property_count: 1
  slug: reactor-build-list-response
- name: BuildResource
  property_count: 4
  slug: reactor-build-resource
- name: BuildSingleResponse
  property_count: 0
  slug: reactor-build-single-response
- name: CallbackAttributes
  property_count: 4
  slug: reactor-callback-attributes
- name: CallbackCreateRequest
  property_count: 1
  slug: reactor-callback-create-request
- name: CallbackListResponse
  property_count: 1
  slug: reactor-callback-list-response
- name: CallbackResource
  property_count: 4
  slug: reactor-callback-resource
- name: CallbackSingleResponse
  property_count: 0
  slug: reactor-callback-single-response
- name: CallbackUpdateRequest
  property_count: 1
  slug: reactor-callback-update-request
- name: CompanyAttributes
  property_count: 7
  slug: reactor-company-attributes
- name: CompanyListResponse
  property_count: 1
  slug: reactor-company-list-response
- name: CompanyResource
  property_count: 4
  slug: reactor-company-resource
- name: CompanySingleResponse
  property_count: 0
  slug: reactor-company-single-response
- name: DataElementAttributes
  property_count: 13
  slug: reactor-data-element-attributes
- name: DataElementCreateRequest
  property_count: 1
  slug: reactor-data-element-create-request
- name: DataElementListResponse
  property_count: 1
  slug: reactor-data-element-list-response
- name: DataElementResource
  property_count: 4
  slug: reactor-data-element-resource
- name: DataElementSingleResponse
  property_count: 0
  slug: reactor-data-element-single-response
- name: DataElementUpdateRequest
  property_count: 1
  slug: reactor-data-element-update-request
- name: EnvironmentAttributes
  property_count: 9
  slug: reactor-environment-attributes
- name: EnvironmentCreateRequest
  property_count: 1
  slug: reactor-environment-create-request
- name: EnvironmentListResponse
  property_count: 1
  slug: reactor-environment-list-response
- name: EnvironmentResource
  property_count: 4
  slug: reactor-environment-resource
- name: EnvironmentSingleResponse
  property_count: 0
  slug: reactor-environment-single-response
- name: EnvironmentUpdateRequest
  property_count: 1
  slug: reactor-environment-update-request
- name: ErrorResponse
  property_count: 1
  slug: reactor-error-response
- name: ExtensionAttributes
  property_count: 12
  slug: reactor-extension-attributes
- name: ExtensionCreateRequest
  property_count: 1
  slug: reactor-extension-create-request
- name: ExtensionListResponse
  property_count: 1
  slug: reactor-extension-list-response
- name: ExtensionPackageAttributes
  property_count: 11
  slug: reactor-extension-package-attributes
- name: ExtensionPackageListResponse
  property_count: 1
  slug: reactor-extension-package-list-response
- name: ExtensionPackageResource
  property_count: 3
  slug: reactor-extension-package-resource
- name: ExtensionPackageSingleResponse
  property_count: 0
  slug: reactor-extension-package-single-response
- name: ExtensionResource
  property_count: 4
  slug: reactor-extension-resource
- name: ExtensionSingleResponse
  property_count: 0
  slug: reactor-extension-single-response
- name: ExtensionUpdateRequest
  property_count: 1
  slug: reactor-extension-update-request
- name: HostAttributes
  property_count: 11
  slug: reactor-host-attributes
- name: HostCreateRequest
  property_count: 1
  slug: reactor-host-create-request
- name: HostListResponse
  property_count: 1
  slug: reactor-host-list-response
- name: HostResource
  property_count: 4
  slug: reactor-host-resource
- name: HostSingleResponse
  property_count: 0
  slug: reactor-host-single-response
- name: HostUpdateRequest
  property_count: 1
  slug: reactor-host-update-request
- name: LibraryAttributes
  property_count: 5
  slug: reactor-library-attributes
- name: LibraryCreateRequest
  property_count: 1
  slug: reactor-library-create-request
- name: LibraryListResponse
  property_count: 1
  slug: reactor-library-list-response
- name: LibraryResource
  property_count: 4
  slug: reactor-library-resource
- name: LibrarySingleResponse
  property_count: 0
  slug: reactor-library-single-response
- name: LibraryUpdateRequest
  property_count: 1
  slug: reactor-library-update-request
- name: PaginationMeta
  property_count: 1
  slug: reactor-pagination-meta
- name: PropertyAttributes
  property_count: 12
  slug: reactor-property-attributes
- name: PropertyCreateRequest
  property_count: 1
  slug: reactor-property-create-request
- name: PropertyListResponse
  property_count: 1
  slug: reactor-property-list-response
- name: PropertyResource
  property_count: 4
  slug: reactor-property-resource
- name: PropertySingleResponse
  property_count: 0
  slug: reactor-property-single-response
- name: PropertyUpdateRequest
  property_count: 1
  slug: reactor-property-update-request
- name: RelationshipRequest
  property_count: 1
  slug: reactor-relationship-request
- name: Relationship
  property_count: 2
  slug: reactor-relationship
- name: RelationshipSingleRequest
  property_count: 1
  slug: reactor-relationship-single-request
- name: RuleAttributes
  property_count: 7
  slug: reactor-rule-attributes
- name: RuleComponentAttributes
  property_count: 13
  slug: reactor-rule-component-attributes
- name: RuleComponentCreateRequest
  property_count: 1
  slug: reactor-rule-component-create-request
- name: RuleComponentListResponse
  property_count: 1
  slug: reactor-rule-component-list-response
- name: RuleComponentResource
  property_count: 4
  slug: reactor-rule-component-resource
- name: RuleComponentSingleResponse
  property_count: 0
  slug: reactor-rule-component-single-response
- name: RuleComponentUpdateRequest
  property_count: 1
  slug: reactor-rule-component-update-request
- name: RuleCreateRequest
  property_count: 1
  slug: reactor-rule-create-request
- name: RuleListResponse
  property_count: 1
  slug: reactor-rule-list-response
- name: RuleResource
  property_count: 4
  slug: reactor-rule-resource
- name: RuleSingleResponse
  property_count: 0
  slug: reactor-rule-single-response
- name: RuleUpdateRequest
  property_count: 1
  slug: reactor-rule-update-request
- name: SearchRequest
  property_count: 1
  slug: reactor-search-request
- name: SearchResponse
  property_count: 2
  slug: reactor-search-response
- name: SecretAttributes
  property_count: 6
  slug: reactor-secret-attributes
- name: SecretCreateRequest
  property_count: 1
  slug: reactor-secret-create-request
- name: SecretListResponse
  property_count: 1
  slug: reactor-secret-list-response
- name: SecretResource
  property_count: 4
  slug: reactor-secret-resource
- name: SecretSingleResponse
  property_count: 0
  slug: reactor-secret-single-response
- name: SecretUpdateRequest
  property_count: 1
  slug: reactor-secret-update-request
- name: Adobe Experience Platform Tags Rule
  property_count: 5
  slug: rule
json_structures:
- name: Data Collection Collect Request Structure
  property_count: 1
  slug: data-collection-collect-request-structure
- name: Data Collection Collect Response Structure
  property_count: 1
  slug: data-collection-collect-response-structure
- name: Data Collection Error Response Structure
  property_count: 5
  slug: data-collection-error-response-structure
- name: Data Collection Interact Request Structure
  property_count: 1
  slug: data-collection-interact-request-structure
- name: Data Collection Interact Response Structure
  property_count: 2
  slug: data-collection-interact-response-structure
- name: Data Collection Media Error Request Structure
  property_count: 1
  slug: data-collection-media-error-request-structure
- name: Data Collection Media Event Request Structure
  property_count: 1
  slug: data-collection-media-event-request-structure
- name: Data Collection Media Session Start Request Structure
  property_count: 1
  slug: data-collection-media-session-start-request-structure
- name: Data Collection Media Session Start Response Structure
  property_count: 2
  slug: data-collection-media-session-start-response-structure
- name: Data Collection Xdm Event Structure
  property_count: 5
  slug: data-collection-xdm-event-structure
- name: Event Forwarding Data Element Create Request Structure
  property_count: 1
  slug: event-forwarding-data-element-create-request-structure
- name: Event Forwarding Data Element List Response Structure
  property_count: 1
  slug: event-forwarding-data-element-list-response-structure
- name: Event Forwarding Data Element Resource Structure
  property_count: 4
  slug: event-forwarding-data-element-resource-structure
- name: Event Forwarding Data Element Single Response Structure
  property_count: 0
  slug: event-forwarding-data-element-single-response-structure
- name: Event Forwarding Environment List Response Structure
  property_count: 1
  slug: event-forwarding-environment-list-response-structure
- name: Event Forwarding Environment Single Response Structure
  property_count: 1
  slug: event-forwarding-environment-single-response-structure
- name: Event Forwarding Error Response Structure
  property_count: 1
  slug: event-forwarding-error-response-structure
- name: Event Forwarding Extension List Response Structure
  property_count: 1
  slug: event-forwarding-extension-list-response-structure
- name: Event Forwarding Library Create Request Structure
  property_count: 1
  slug: event-forwarding-library-create-request-structure
- name: Event Forwarding Library List Response Structure
  property_count: 1
  slug: event-forwarding-library-list-response-structure
- name: Event Forwarding Library Single Response Structure
  property_count: 1
  slug: event-forwarding-library-single-response-structure
- name: Event Forwarding Pagination Meta Structure
  property_count: 1
  slug: event-forwarding-pagination-meta-structure
- name: Event Forwarding Property Attributes Structure
  property_count: 5
  slug: event-forwarding-property-attributes-structure
- name: Event Forwarding Property Create Request Structure
  property_count: 1
  slug: event-forwarding-property-create-request-structure
- name: Event Forwarding Property List Response Structure
  property_count: 1
  slug: event-forwarding-property-list-response-structure
- name: Event Forwarding Property Resource Structure
  property_count: 3
  slug: event-forwarding-property-resource-structure
- name: Event Forwarding Property Single Response Structure
  property_count: 0
  slug: event-forwarding-property-single-response-structure
- name: Event Forwarding Property Update Request Structure
  property_count: 1
  slug: event-forwarding-property-update-request-structure
- name: Event Forwarding Relationship Structure
  property_count: 2
  slug: event-forwarding-relationship-structure
- name: Event Forwarding Rule Create Request Structure
  property_count: 1
  slug: event-forwarding-rule-create-request-structure
- name: Event Forwarding Rule List Response Structure
  property_count: 1
  slug: event-forwarding-rule-list-response-structure
- name: Event Forwarding Rule Resource Structure
  property_count: 4
  slug: event-forwarding-rule-resource-structure
- name: Event Forwarding Rule Single Response Structure
  property_count: 0
  slug: event-forwarding-rule-single-response-structure
- name: Event Forwarding Rule Update Request Structure
  property_count: 1
  slug: event-forwarding-rule-update-request-structure
- name: Event Forwarding Secret Attributes Structure
  property_count: 6
  slug: event-forwarding-secret-attributes-structure
- name: Event Forwarding Secret Create Request Structure
  property_count: 1
  slug: event-forwarding-secret-create-request-structure
- name: Event Forwarding Secret List Response Structure
  property_count: 1
  slug: event-forwarding-secret-list-response-structure
- name: Event Forwarding Secret Resource Structure
  property_count: 3
  slug: event-forwarding-secret-resource-structure
- name: Event Forwarding Secret Single Response Structure
  property_count: 0
  slug: event-forwarding-secret-single-response-structure
- name: Event Forwarding Secret Update Request Structure
  property_count: 1
  slug: event-forwarding-secret-update-request-structure
- name: Extension Error Response Structure
  property_count: 1
  slug: extension-error-response-structure
- name: Extension Extension Attributes Structure
  property_count: 12
  slug: extension-extension-attributes-structure
- name: Extension Extension Install Request Structure
  property_count: 1
  slug: extension-extension-install-request-structure
- name: Extension Extension List Response Structure
  property_count: 1
  slug: extension-extension-list-response-structure
- name: Extension Extension Package Attributes Structure
  property_count: 13
  slug: extension-extension-package-attributes-structure
- name: Extension Extension Package List Response Structure
  property_count: 1
  slug: extension-extension-package-list-response-structure
- name: Extension Extension Package Resource Structure
  property_count: 4
  slug: extension-extension-package-resource-structure
- name: Extension Extension Package Single Response Structure
  property_count: 0
  slug: extension-extension-package-single-response-structure
- name: Extension Extension Package Update Request Structure
  property_count: 1
  slug: extension-extension-package-update-request-structure
- name: Extension Extension Resource Structure
  property_count: 4
  slug: extension-extension-resource-structure
- name: Extension Extension Revise Request Structure
  property_count: 1
  slug: extension-extension-revise-request-structure
- name: Extension Extension Single Response Structure
  property_count: 0
  slug: extension-extension-single-response-structure
- name: Extension Library List Response Structure
  property_count: 1
  slug: extension-library-list-response-structure
- name: Extension Pagination Meta Structure
  property_count: 1
  slug: extension-pagination-meta-structure
- name: Extension Property Single Response Structure
  property_count: 1
  slug: extension-property-single-response-structure
- name: Extension Relationship Structure
  property_count: 2
  slug: extension-relationship-structure
- name: Reactor Build Attributes Structure
  property_count: 4
  slug: reactor-build-attributes-structure
- name: Reactor Build List Response Structure
  property_count: 1
  slug: reactor-build-list-response-structure
- name: Reactor Build Resource Structure
  property_count: 4
  slug: reactor-build-resource-structure
- name: Reactor Build Single Response Structure
  property_count: 0
  slug: reactor-build-single-response-structure
- name: Reactor Callback Attributes Structure
  property_count: 4
  slug: reactor-callback-attributes-structure
- name: Reactor Callback Create Request Structure
  property_count: 1
  slug: reactor-callback-create-request-structure
- name: Reactor Callback List Response Structure
  property_count: 1
  slug: reactor-callback-list-response-structure
- name: Reactor Callback Resource Structure
  property_count: 4
  slug: reactor-callback-resource-structure
- name: Reactor Callback Single Response Structure
  property_count: 0
  slug: reactor-callback-single-response-structure
- name: Reactor Callback Update Request Structure
  property_count: 1
  slug: reactor-callback-update-request-structure
- name: Reactor Company Attributes Structure
  property_count: 7
  slug: reactor-company-attributes-structure
- name: Reactor Company List Response Structure
  property_count: 1
  slug: reactor-company-list-response-structure
- name: Reactor Company Resource Structure
  property_count: 4
  slug: reactor-company-resource-structure
- name: Reactor Company Single Response Structure
  property_count: 0
  slug: reactor-company-single-response-structure
- name: Reactor Data Element Attributes Structure
  property_count: 13
  slug: reactor-data-element-attributes-structure
- name: Reactor Data Element Create Request Structure
  property_count: 1
  slug: reactor-data-element-create-request-structure
- name: Reactor Data Element List Response Structure
  property_count: 1
  slug: reactor-data-element-list-response-structure
- name: Reactor Data Element Resource Structure
  property_count: 4
  slug: reactor-data-element-resource-structure
- name: Reactor Data Element Single Response Structure
  property_count: 0
  slug: reactor-data-element-single-response-structure
- name: Reactor Data Element Update Request Structure
  property_count: 1
  slug: reactor-data-element-update-request-structure
- name: Reactor Environment Attributes Structure
  property_count: 9
  slug: reactor-environment-attributes-structure
- name: Reactor Environment Create Request Structure
  property_count: 1
  slug: reactor-environment-create-request-structure
- name: Reactor Environment List Response Structure
  property_count: 1
  slug: reactor-environment-list-response-structure
- name: Reactor Environment Resource Structure
  property_count: 4
  slug: reactor-environment-resource-structure
- name: Reactor Environment Single Response Structure
  property_count: 0
  slug: reactor-environment-single-response-structure
- name: Reactor Environment Update Request Structure
  property_count: 1
  slug: reactor-environment-update-request-structure
- name: Reactor Error Response Structure
  property_count: 1
  slug: reactor-error-response-structure
- name: Reactor Extension Attributes Structure
  property_count: 12
  slug: reactor-extension-attributes-structure
- name: Reactor Extension Create Request Structure
  property_count: 1
  slug: reactor-extension-create-request-structure
- name: Reactor Extension List Response Structure
  property_count: 1
  slug: reactor-extension-list-response-structure
- name: Reactor Extension Package Attributes Structure
  property_count: 11
  slug: reactor-extension-package-attributes-structure
- name: Reactor Extension Package List Response Structure
  property_count: 1
  slug: reactor-extension-package-list-response-structure
- name: Reactor Extension Package Resource Structure
  property_count: 3
  slug: reactor-extension-package-resource-structure
- name: Reactor Extension Package Single Response Structure
  property_count: 0
  slug: reactor-extension-package-single-response-structure
- name: Reactor Extension Resource Structure
  property_count: 4
  slug: reactor-extension-resource-structure
- name: Reactor Extension Single Response Structure
  property_count: 0
  slug: reactor-extension-single-response-structure
- name: Reactor Extension Update Request Structure
  property_count: 1
  slug: reactor-extension-update-request-structure
- name: Reactor Host Attributes Structure
  property_count: 11
  slug: reactor-host-attributes-structure
- name: Reactor Host Create Request Structure
  property_count: 1
  slug: reactor-host-create-request-structure
- name: Reactor Host List Response Structure
  property_count: 1
  slug: reactor-host-list-response-structure
- name: Reactor Host Resource Structure
  property_count: 4
  slug: reactor-host-resource-structure
- name: Reactor Host Single Response Structure
  property_count: 0
  slug: reactor-host-single-response-structure
- name: Reactor Host Update Request Structure
  property_count: 1
  slug: reactor-host-update-request-structure
- name: Reactor Library Attributes Structure
  property_count: 5
  slug: reactor-library-attributes-structure
- name: Reactor Library Create Request Structure
  property_count: 1
  slug: reactor-library-create-request-structure
- name: Reactor Library List Response Structure
  property_count: 1
  slug: reactor-library-list-response-structure
- name: Reactor Library Resource Structure
  property_count: 4
  slug: reactor-library-resource-structure
- name: Reactor Library Single Response Structure
  property_count: 0
  slug: reactor-library-single-response-structure
- name: Reactor Library Update Request Structure
  property_count: 1
  slug: reactor-library-update-request-structure
- name: Reactor Pagination Meta Structure
  property_count: 1
  slug: reactor-pagination-meta-structure
- name: Reactor Property Attributes Structure
  property_count: 12
  slug: reactor-property-attributes-structure
- name: Reactor Property Create Request Structure
  property_count: 1
  slug: reactor-property-create-request-structure
- name: Reactor Property List Response Structure
  property_count: 1
  slug: reactor-property-list-response-structure
- name: Reactor Property Resource Structure
  property_count: 4
  slug: reactor-property-resource-structure
- name: Reactor Property Single Response Structure
  property_count: 0
  slug: reactor-property-single-response-structure
- name: Reactor Property Update Request Structure
  property_count: 1
  slug: reactor-property-update-request-structure
- name: Reactor Relationship Request Structure
  property_count: 1
  slug: reactor-relationship-request-structure
- name: Reactor Relationship Single Request Structure
  property_count: 1
  slug: reactor-relationship-single-request-structure
- name: Reactor Relationship Structure
  property_count: 2
  slug: reactor-relationship-structure
- name: Reactor Rule Attributes Structure
  property_count: 7
  slug: reactor-rule-attributes-structure
- name: Reactor Rule Component Attributes Structure
  property_count: 13
  slug: reactor-rule-component-attributes-structure
- name: Reactor Rule Component Create Request Structure
  property_count: 1
  slug: reactor-rule-component-create-request-structure
- name: Reactor Rule Component List Response Structure
  property_count: 1
  slug: reactor-rule-component-list-response-structure
- name: Reactor Rule Component Resource Structure
  property_count: 4
  slug: reactor-rule-component-resource-structure
- name: Reactor Rule Component Single Response Structure
  property_count: 0
  slug: reactor-rule-component-single-response-structure
- name: Reactor Rule Component Update Request Structure
  property_count: 1
  slug: reactor-rule-component-update-request-structure
- name: Reactor Rule Create Request Structure
  property_count: 1
  slug: reactor-rule-create-request-structure
- name: Reactor Rule List Response Structure
  property_count: 1
  slug: reactor-rule-list-response-structure
- name: Reactor Rule Resource Structure
  property_count: 4
  slug: reactor-rule-resource-structure
- name: Reactor Rule Single Response Structure
  property_count: 0
  slug: reactor-rule-single-response-structure
- name: Reactor Rule Update Request Structure
  property_count: 1
  slug: reactor-rule-update-request-structure
- name: Reactor Search Request Structure
  property_count: 1
  slug: reactor-search-request-structure
- name: Reactor Search Response Structure
  property_count: 2
  slug: reactor-search-response-structure
- name: Reactor Secret Attributes Structure
  property_count: 6
  slug: reactor-secret-attributes-structure
- name: Reactor Secret Create Request Structure
  property_count: 1
  slug: reactor-secret-create-request-structure
- name: Reactor Secret List Response Structure
  property_count: 1
  slug: reactor-secret-list-response-structure
- name: Reactor Secret Resource Structure
  property_count: 4
  slug: reactor-secret-resource-structure
- name: Reactor Secret Single Response Structure
  property_count: 0
  slug: reactor-secret-single-response-structure
- name: Reactor Secret Update Request Structure
  property_count: 1
  slug: reactor-secret-update-request-structure
jsonld:
- class_count: 67
  name: context Context
  property_count: 30
  slug: context
- class_count: 0
  name: Data Collection Context
  property_count: 0
  slug: data-collection-context
- class_count: 0
  name: Event Forwarding Context
  property_count: 0
  slug: event-forwarding-context
- class_count: 0
  name: Extension Context
  property_count: 0
  slug: extension-context
- class_count: 0
  name: Reactor Context
  property_count: 0
  slug: reactor-context
layout: provider
modified: '2026-05-19'
name: Adobe Launch
nav: Providers
network: true
overview: 'Adobe Launch publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Builds API, Callbacks API, Companies API, and 13 more. Tagged areas include Data Collection, Edge Network, Event Forwarding, Marketing Technology, and Tag Management.


  The Adobe Launch catalog on APIs.io includes 5 JSON-LD contexts and 2 Spectral governance rulesets.


  Adobe Launch''s developer surface includes authentication, developer console, developer portal, engineering blog, signup flow, changelog, and 26 more developer resources.'
plans:
- name: Adobe Launch Plans Pricing
  plan_count: 1
  slug: adobe-launch-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 2
  name: Adobe Launch Rate Limits
  slug: adobe-launch-rate-limits
rules:
- name: Adobe Launch API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: adobe-launch-jsonschema-spectral-rules
- name: Adobe Launch API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 6
  slug: adobe-launch-spectral-rules
score:
  band: strong
  composite: 60.8
  delta: -4.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 79.6
    developer_ergonomics: 47.8
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 57.9
  previous_composite: 65.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/screenshots/adobe-launch-2026-06-20T164946.png
security:
- kind: authentication
  name: Adobe Launch Authentication
  slug: adobe-launch-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Adobe Launch Domain Security
  slug: adobe-launch-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adobe Launch Vulnerability Disclosure
  slug: adobe-launch-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: adobe-launch
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
use_cases:
- Unified tag management across marketing tools
- Server-side event forwarding for privacy compliance
- Custom extension development for third-party integrations
- Real-time data collection from web and mobile applications
- Media analytics tracking for video and audio content
- A/B testing and personalization data routing
- Cross-platform data collection orchestration
website: https://developer.adobe.com/
---
