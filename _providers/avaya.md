---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.8
  scored_at: '2026-09-14'
agentic_access:
- acting_count: 240
  human_in_the_loop: 10
  name: Avaya Agentic Access
  operation_count: 367
  slug: avaya-agentic-access
  summary_line: 367 operations · 240 acting · 10 human-in-the-loop
api_count: 40
apis:
- baseURL: https://core.{customerId}.ec.avayacloud.com
  baseurl_source: declared
  description: 'REST APIs for the Avaya Infinity cloud customer experience platform: user and group management, queue configuration and real-time queue metrics, customer profiles, transcripts and interaction transcri'
  name: Avaya Infinity Platform APIs
  slug: avaya-infinity-platform-apis
- baseURL: https://na.api.avayacloud.com
  baseurl_source: declared
  description: 'REST APIs for Avaya Experience Platform, Avaya''s CCaaS platform: account, user, group, profile, resource partition, match/queue/category and timetable administration; voice administration across Commu'
  name: Avaya Experience Platform (AXP) APIs
  slug: avaya-experience-platform-axp-apis
artifact_total: 11
asyncapis:
- description: ''
  name: Avaya Webhooks
  slug: avaya-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.avaya.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.avayacloud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.avayacloud.com/avaya-infinity/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.avayacloud.com/avaya-infinity/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.avayacloud.com/avaya-infinity/docs/quick-start
- group: operate
  title: ''
  type: Support
  url: https://support.avaya.com/support/en/public
- group: company
  title: ''
  type: Blog
  url: https://www.avaya.com/en/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/avaya
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/avaya/
- group: start
  title: ''
  type: SignUp
  url: https://developers.avayacloud.com/avaya-infinity/docs/obtaining-a-client-id-and-secret-from-avaya
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avaya.com/en/privacy/commitment/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avaya.com/en/legal/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/avaya-axp/avaya-experience-platform
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/plans/avaya-plans-pricing.yml
  title: ''
  type: Pricing
  url: plans/avaya-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/plans/avaya-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avaya-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/rate-limits/avaya-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/avaya-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/packages/avaya-packages.yml
  title: ''
  type: Packages
  url: packages/avaya-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/packages/avaya-packages.yml
  title: ''
  type: SDKs
  url: packages/avaya-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/cli/avaya-cli.yml
  title: ''
  type: CLI
  url: cli/avaya-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/components/avaya-components.yml
  title: ''
  type: Components
  url: components/avaya-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/well-known/avaya-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avaya-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/well-known/avaya-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/avaya-api-catalog.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/llms/avaya-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avaya-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/asyncapi/avaya-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/avaya-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/conventions/avaya-conventions.yml
  title: ''
  type: Conventions
  url: conventions/avaya-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/errors/avaya-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/avaya-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/data-model/avaya-data-model.yml
  title: ''
  type: DataModel
  url: data-model/avaya-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/lifecycle/avaya-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/avaya-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.avayacloud.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.avayacloud.com/avaya-experience-platform/docs/api-deprecation-notices
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/changelog/avaya-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/avaya-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/conformance/avaya-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avaya-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.avaya.com/en/trust-center/compliance/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/security/avaya-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/avaya-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/security/avaya-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/avaya-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://support.avaya.com/css/public/documents/100045520
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/security/avaya-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avaya-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/authentication/avaya-authentication.yml
  title: ''
  type: Authentication
  url: authentication/avaya-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/scopes/avaya-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/avaya-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/agentic-access/avaya-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/avaya-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/mcp/avaya-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/avaya-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-admin-account-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-admin-account-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-admin-element-inventory-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-admin-element-inventory-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-admin-group-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-admin-group-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-admin-match-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-admin-match-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-admin-timetable-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-admin-timetable-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-admin-user-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-admin-user-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-admin-voice-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-admin-voice-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-analytics-historical-data-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-analytics-historical-data-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-analytics-historical-data-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-analytics-historical-data-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-analytics-producer-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-analytics-producer-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-auth-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-auth-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-customer-journey-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-customer-journey-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-digital-custom-chat-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-digital-custom-chat-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-digital-custom-messaging-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-digital-custom-messaging-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-digital-notification-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-digital-notification-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-digital-sdk-auth-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-digital-sdk-auth-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-digital-signed-media-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-digital-signed-media-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-digital-signed-media-uri-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-digital-signed-media-uri-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-draft-retrieval-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-draft-retrieval-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-draft-save-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-draft-save-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-notification-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-notification-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-routing-queue-metrics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-routing-queue-metrics-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-transcript-retrieval-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-transcript-retrieval-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-transcript-save-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-transcript-save-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-access-token-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-access-token-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-analytics-historical-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-analytics-historical-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-groups-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-groups-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-messaging-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-messaging-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-notification-service-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-notification-service-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-notifications-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-notifications-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-outbound-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-outbound-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-profile-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-profile-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-queue-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-queue-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-queue-metrics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-queue-metrics-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-transcription-interactions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-transcription-interactions-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-transcripts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-transcripts-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-user-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-user-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-workflow-execution-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-workflow-execution-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-workflow-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-workflow-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-workflow-sessions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-workflow-sessions-overlay.yaml
created: '2026-01-01'
description: 'Avaya is a global enterprise communications company whose developer surface spans two cloud platforms: Avaya Infinity, the cloud-native customer experience platform launched in 2025, and Avaya Experience Platform (AXP), the CCaaS generation that preceded it. Between them they publish 40 OpenAPI 3.0 documents and 367 operations across administration (users, groups, profiles, queues, timetables, extensions, Communication Manager and hybrid cloud gateways), customer journey and engagement history, digital chat and custom messaging, transcripts, historical and real-time analytics, workflow sessions, outbound campaigns, and a webhook/WebSocket event surface. Authentication is a bearer JWT issued by a per-tenant Keycloak realm, carried alongside a tenant appkey header; every path is rooted at an account id and the Infinity host itself is per-tenant. Avaya publishes an llms.txt, an RFC 9727 API catalog, a public Postman workspace and first-party JavaScript SDKs, but no MCP server,
  no idempotency mechanism and no public pricing.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/avaya.png
layout: provider
modified: '2026-09-14'
name: Avaya
nav: Providers
network: true
overview: 'Avaya publishes 2 APIs on the [APIs.io](https://apis.io/) network: Infinity Platform APIs and Experience Platform (AXP) APIs. Tagged areas include Communications, Contact Center, Collaboration, Artificial Intelligence, and UCaaS.


  The Avaya catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Avaya''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 75 more developer resources.'
plans:
- name: Avaya Plans Pricing
  plan_count: 0
  slug: avaya-plans-pricing
press:
- date: '2026-05-25'
  title: Avaya Chooses Gemini Enterprise and Google Workspace ...
  url: https://www.businesswire.com/news/home/20251230219645/en/Avaya-Chooses-Gemini-Enterprise-and-Google-Workspace-for-AI-Driven-Collaboration-and-Next-Gen-Workplace-Productivity
- date: '2026-05-25'
  title: 'Avaya news: Avaya Infinity to support secure AI interaction'
  url: https://www.convergedsystems.com/blog/avaya-news-july-2025-avaya-infinity-platform-to-add-ai-model-context-protocol-mcp/
- date: '2026-05-25'
  title: 'Avaya Infinity Platform: AI-Powered CCaaS & CX Solutions'
  url: https://www.avaya.com/en/products/infinity-platform/
- date: '2026-05-25'
  title: Avaya to support Model Context Protocol, collaborate with ...
  url: https://www.linkedin.com/posts/avaya_avaya-is-thrilled-to-share-that-the-avaya-activity-7353409534989635584-MN14
- date: '2026-05-25'
  title: Artificial Intelligence | Avaya Trust Center
  url: https://www.avaya.com/en/trust-center/artificial-intelligence/
random_paper: 5
rate_limits:
- limit_count: 0
  name: Avaya Rate Limits
  slug: avaya-rate-limits
scopes:
- name: Avaya Scopes
  scope_count: 1
  slug: avaya-scopes
  summary_line: 1 scope · clientCredentials/password
score:
  band: strong
  composite: 62.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 56.1
  facets:
    access_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 71.0
    developer_ergonomics: 78.0
    discoverability: 81.5
    operational_transparency: 60.5
  previous_composite: 6.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 40
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: rising
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/screenshots/avaya-2026-06-20T172723.png
security:
- kind: authentication
  name: Avaya Authentication
  slug: avaya-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Avaya Domain Security
  slug: avaya-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Avaya Vulnerability Disclosure
  slug: avaya-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Avaya Trust Center
  slug: avaya-trust-center
  summary_line: FedRAMP
slug: avaya
tags:
- Communications
- Contact Center
- Collaboration
- Artificial Intelligence
- UCaaS
- CCaaS
- Customer Experience
- Telephony
- Webhook
- Enterprise Software
- Unified Communications
- Customer Service
website: https://www.avaya.com/en/
---
