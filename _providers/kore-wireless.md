---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.2
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 46
  human_in_the_loop: 1
  name: Kore Wireless Agentic Access
  operation_count: 117
  slug: kore-wireless-agentic-access
  summary_line: 117 operations · 46 acting · 1 human-in-the-loop
api_count: 8
apis:
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: Account details of customer
  name: KORE Wireless Account API
  slug: kore-wireless-account-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The Accounts API from KORE Wireless — 2 operation(s) for accounts.
  name: KORE Wireless Accounts API
  slug: kore-wireless-accounts-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: API to manage activation profile related activities for a given account . <br> For more details please go to our help desk article [here](https://helpdesk.korewireless.com/hc/en-us/articles/3600501444
  name: KORE Wireless Activation Profiles API
  slug: kore-wireless-activation-profiles-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: APIs that provides alerts on subscribed events
  name: KORE Wireless Alerting API
  slug: kore-wireless-alerting-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The Auth API from KORE Wireless — 1 operation(s) for auth.
  name: KORE Wireless Auth API
  slug: kore-wireless-auth-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: These APIs enable users to perform various operations, including creating, retrieving, updating, and deleting client information. Through these APIs, users can interact with a wide range of client dat
  name: KORE Wireless Clients API
  slug: kore-wireless-clients-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The Commands Resource API from KORE Wireless — 2 operation(s) for commands resource.
  name: KORE Wireless Commands Resource API
  slug: kore-wireless-commands-resource-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The DataSessions Resource API from KORE Wireless — 1 operation(s) for datasessions resource.
  name: KORE Wireless DataSessions Resource API
  slug: kore-wireless-datasessions-resource-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The Diagnostics API from KORE Wireless — 2 operation(s) for diagnostics.
  name: KORE Wireless Diagnostics API
  slug: kore-wireless-diagnostics-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: Retrieve details about the eligibility of a given account
  name: KORE Wireless Eligibility API
  slug: kore-wireless-eligibility-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: API to manage eSIM Switch related activities for a given account <br> Refer to the <a href="https://korewireless.service-now.com/csm?sys_kb_id=ec87a82f976ee110d038301e6253afa3&id=kb_article_view&syspa
  name: KORE Wireless eSIM Profile Management API
  slug: kore-wireless-esim-profile-management-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: ping health service
  name: KORE Wireless Health API
  slug: kore-wireless-health-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: API to send message to the SIMs about any software upgrade/similar things.
  name: KORE Wireless Messages API
  slug: kore-wireless-messages-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: Status of requests made by the customer
  name: KORE Wireless Provisioning API
  slug: kore-wireless-provisioning-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The RatePlans Resource API from KORE Wireless — 2 operation(s) for rateplans resource.
  name: KORE Wireless RatePlans Resource API
  slug: kore-wireless-rateplans-resource-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: Customers of KORE who pre-configure report schedules have reports automatically generated and securely stored at the scheduled times — when accessed via API, they receive data in the agreed format, wi
  name: KORE Wireless Reports API
  slug: kore-wireless-reports-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The Secrets API from KORE Wireless — 2 operation(s) for secrets.
  name: KORE Wireless Secrets API
  slug: kore-wireless-secrets-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: 'Customers of KORE having Radius Accounting integrated at carrier level will have session events collected at KORE. Session START and STOP events are correlated, and data is exposed as Session API for '
  name: KORE Wireless Session API
  slug: kore-wireless-session-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The Sims Resource API from KORE Wireless — 2 operation(s) for sims resource.
  name: KORE Wireless Sims Resource API
  slug: kore-wireless-sims-resource-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: API provides subscription enquiries made by the customer.
  name: KORE Wireless Subscription API
  slug: kore-wireless-subscription-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The SupersimV1BillingPeriod API from KORE Wireless — 1 operation(s) for supersimv1billingperiod.
  name: KORE Wireless Supersim V1 Billing Period API
  slug: kore-wireless-supersimv1billingperiod-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The SupersimV1EsimProfile API from KORE Wireless — 2 operation(s) for supersimv1esimprofile.
  name: KORE Wireless Supersim V1 Esim Profile API
  slug: kore-wireless-supersimv1esimprofile-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The SupersimV1Fleet API from KORE Wireless — 2 operation(s) for supersimv1fleet.
  name: KORE Wireless Supersim V1 Fleet API
  slug: kore-wireless-supersimv1fleet-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The SupersimV1IpCommand API from KORE Wireless — 2 operation(s) for supersimv1ipcommand.
  name: KORE Wireless Supersim V1 Ip Command API
  slug: kore-wireless-supersimv1ipcommand-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The SupersimV1Network API from KORE Wireless — 2 operation(s) for supersimv1network.
  name: KORE Wireless Supersim V1 Network API
  slug: kore-wireless-supersimv1network-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The SupersimV1NetworkAccessProfile API from KORE Wireless — 2 operation(s) for supersimv1networkaccessprofile.
  name: KORE Wireless Supersim V1 Network Access Profile API
  slug: kore-wireless-supersimv1networkaccessprofile-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The SupersimV1NetworkAccessProfileNetwork API from KORE Wireless — 2 operation(s) for supersimv1networkaccessprofilenetwork.
  name: KORE Wireless Supersim V1 Network Access Profile Network API
  slug: kore-wireless-supersimv1networkaccessprofilenetwork-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The SupersimV1SettingsUpdate API from KORE Wireless — 1 operation(s) for supersimv1settingsupdate.
  name: KORE Wireless Supersim V1 Settings Update API
  slug: kore-wireless-supersimv1settingsupdate-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The SupersimV1Sim API from KORE Wireless — 2 operation(s) for supersimv1sim.
  name: KORE Wireless Supersim V1 Sim API
  slug: kore-wireless-supersimv1sim-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The SupersimV1SimIpAddress API from KORE Wireless — 1 operation(s) for supersimv1simipaddress.
  name: KORE Wireless Supersim V1 Sim Ip Address API
  slug: kore-wireless-supersimv1simipaddress-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The SupersimV1SmsCommand API from KORE Wireless — 2 operation(s) for supersimv1smscommand.
  name: KORE Wireless Supersim V1 Sms Command API
  slug: kore-wireless-supersimv1smscommand-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The SupersimV1UsageRecord API from KORE Wireless — 1 operation(s) for supersimv1usagerecord.
  name: KORE Wireless Supersim V1 Usage Record API
  slug: kore-wireless-supersimv1usagerecord-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: APIs that are currently under testing
  name: KORE Wireless Testing API
  slug: kore-wireless-testing-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: A user can retrieve usage records for a given subscription or plan
  name: KORE Wireless Usage API
  slug: kore-wireless-usage-api
- baseURL: https://api.korewireless.com/connectivity
  baseurl_source: declared
  description: The UsageRecords Resource API from KORE Wireless — 2 operation(s) for usagerecords resource.
  name: KORE Wireless UsageRecords Resource API
  slug: kore-wireless-usagerecords-resource-api
artifact_total: 50
asyncapis:
- description: ''
  name: Kore Wireless Event Streams Webhooks
  slug: kore-wireless-event-streams-webhooks
collections:
- collection_type: open
  name: Client APIs
  slug: open-kore-wireless-api-clients
- collection_type: open
  name: Connectivity APIs
  slug: open-kore-wireless-connectivity-pro
- collection_type: open
  name: IaM APIs
  slug: open-kore-wireless-iam
- collection_type: open
  name: Programmable Wireless APIs
  slug: open-kore-wireless-programmable-wireless
- collection_type: open
  name: SMS API
  slug: open-kore-wireless-sms
- collection_type: open
  name: KORE - Supersim
  slug: open-kore-wireless-supersim
- collection_type: open
  name: v1-token
  slug: open-kore-wireless-token
- collection_type: open
  name: Webhook APIs
  slug: open-kore-wireless-webhook
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/kore-wireless-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/kore-wireless-connectivity-pro-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kore-wireless-supersim-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kore-wireless-programmable-wireless-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kore-wireless-sms-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kore-wireless-webhook-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kore-wireless-iam-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kore-wireless-api-clients-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kore-wireless-token-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kore-wireless-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kore-wireless-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kore-wireless-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kore-wireless-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kore-wireless-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.korewireless.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.korewireless.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.korewireless.com/api/api-reference
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.korewireless.com/
- group: start
  title: ''
  type: Console
  url: https://console.korewireless.com/
- group: start
  title: ''
  type: SignUp
  url: https://console.korewireless.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/korewireless
- group: docs
  title: ''
  type: OpenAPIRepository
  url: https://github.com/korewireless/kore-openapi
- group: auth
  title: ''
  type: Authentication
  url: https://docs.korewireless.com/developers/api-management/auth
- group: design
  title: ''
  type: Webhooks
  url: https://docs.korewireless.com/developers/webhooks
- group: other
  title: ''
  type: EventStreams
  url: https://docs.korewireless.com/developers/event-streams
- group: operate
  title: ''
  type: StatusPage
  url: https://korewireless.service-now.com/csm?id=services_status
- group: company
  title: ''
  type: Blog
  url: https://www.korewireless.com/blog/
- group: company
  title: ''
  type: News
  url: https://www.korewireless.com/news/
- group: docs
  title: ''
  type: TechnicalDocumentation
  url: https://www.korewireless.com/technical-documentation/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kore-wireless
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.korewireless.com/developers/get-started/apis
- group: operate
  title: ''
  type: Support
  url: https://docs.korewireless.com/troubleshooting/
- group: operate
  title: ''
  type: Contact
  url: https://www.korewireless.com/contact-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.korewireless.com/programmable-wireless/help-and-support/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.korewireless.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.korewireless.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.korewireless.com/responsible-disclosure-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kore-wireless-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/kore-wireless-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kore-wireless-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kore-wireless-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kore-wireless-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/kore-wireless-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kore-wireless-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kore-wireless-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kore-wireless-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kore-wireless-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kore-wireless-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kore-wireless-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kore-wireless-event-streams-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kore-wireless-data-model.yml
created: '2026-07-25'
description: 'KORE Wireless (KORE Group Holdings) is an Atlanta, Georgia headquartered global IoT connectivity provider operating as a mobile virtual network operator (MVNO) across more than 190 countries, with over 20 million IoT connections under management. KORE sits in the aggregator half of the telecom value chain: it does not own spectrum or radio access network, it resells and orchestrates multi-carrier cellular connectivity, eSIM/iSIM provisioning, device management, and IoT security as a service to enterprises in healthcare, fleet, logistics, utilities, and industrial automation. In 2024 KORE acquired the Twilio IoT business — Super SIM, Programmable Wireless, and Microvisor — inheriting a genuinely developer-first API surface, and it has kept that posture: KORE publishes eight OpenAPI 3.0 specifications in a public GitHub repository (github.com/korewireless/kore-openapi) with a make-based SDK generation workflow, an open GitBook documentation site at docs.korewireless.com requiring
  no login, self-serve account registration at console.korewireless.com, OAuth 2.0 client-credentials authorization, signed webhooks, and CloudEvents-formatted event streams. KORE publishes no CAMARA network APIs and is not a GSMA Open Gateway operator participant — as an MVNO it consumes carrier network capability rather than exposing it, and no CAMARA, Open Gateway, TM Forum, or NEF/SCEF reference appears anywhere in its documentation. In 2026 KORE was taken private by Searchlight Capital Partners and Abry Partners and delisted from the NYSE.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool surface derived from KORE OpenAPI
  slug: candidate-mcp-tool-surface-derived-from-kore-openapi
modified: '2026-07-25'
name: KORE Wireless
nav: Providers
network: true
overview: 'KORE Wireless publishes 35 APIs on the [APIs.io](https://apis.io/) network, including Account API, Accounts API, Activation Profiles API, and 32 more. Tagged areas include Telecommunications, United States, IoT, eSIM, and Connectivity.


  The KORE Wireless catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  KORE Wireless'' developer surface includes authentication, documentation, API reference, developer console, signup flow, engineering blog, product news, and 45 more developer resources.'
random_paper: 12
scopes:
- name: Kore Wireless Scopes
  scope_count: 0
  slug: kore-wireless-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 23
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 57.7
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 35
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 63.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kore-wireless/refs/heads/main/screenshots/kore-wireless-2026-08-07T171327.png
security:
- kind: authentication
  name: Kore Wireless Authentication
  slug: kore-wireless-authentication
  summary_line: oauth2/apiKey/http · 3 schemes
- kind: domain-security
  name: Kore Wireless Domain Security
  slug: kore-wireless-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kore Wireless Vulnerability Disclosure
  slug: kore-wireless-vulnerability-disclosure
  summary_line: disclosure policy published
slug: kore-wireless
tags:
- Telecommunications
- United States
- IoT
- eSIM
- Connectivity
- MVNO
- SIM Management
- Roaming
- Messaging
- SMS
- Device Management
- Network APIs
website: https://www.korewireless.com/
---
