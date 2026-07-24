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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 77.9
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 73
  human_in_the_loop: 0
  name: Dyspatch Agentic Access
  operation_count: 131
  slug: dyspatch-agentic-access
  summary_line: 131 operations · 73 acting
api_count: 20
apis:
- description: The Blocks API from Dyspatch — 6 operation(s) for blocks.
  name: Dyspatch Blocks API
  slug: dyspatch-blocks-api
- description: Customer Profiles contain JSON data that can be used for template personalization. Each profile can be associated with one or more workspaces, or none, and contains structured data content.
  name: Dyspatch Customer Profiles API
  slug: dyspatch-customer-profiles-api
- description: Drafts represent unpublished versions of templates that are still mutable. There could be many in progress drafts for a template.
  name: Dyspatch Drafts API
  slug: dyspatch-drafts-api
- description: Live Activity Drafts represent unpublished versions of templates that are still mutable. There could be many in progress drafts for a template.
  name: Dyspatch Live Activity Drafts API
  slug: dyspatch-live-activity-drafts-api
- description: Live Activity Localization objects are the same as Template objects except they contain localized content. If your account is using localizations then use this instead of the compiled Template object.
  name: Dyspatch Live Activity Localizations API
  slug: dyspatch-live-activity-localizations-api
- description: Live Activity Templates are the Live Activity templates found in your Dyspatch account. Only the published Template Draft is returned. A typical integration will start with using the Templates list en
  name: Dyspatch Live Activity Templates API
  slug: dyspatch-live-activity-templates-api
- description: Localization objects are the same as Template objects except they contain localized content. If your account is using localizations then use this instead of the compiled Template object.
  name: Dyspatch Localizations API
  slug: dyspatch-localizations-api
- description: Push Drafts represent unpublished versions of templates that are still mutable. There could be many in progress drafts for a template.
  name: Dyspatch Push Drafts API
  slug: dyspatch-push-drafts-api
- description: Push Localization objects are the same as Template objects except they contain localized content. If your account is using localizations then use this instead of the compiled Template object.
  name: Dyspatch Push Localizations API
  slug: dyspatch-push-localizations-api
- description: 'Push Templates are the Push templates found in your Dyspatch account. Only the published Template Draft is returned. A typical integration will start with using the Templates list endpoint to iterate '
  name: Dyspatch Push Templates API
  slug: dyspatch-push-templates-api
- description: SMS Drafts represent unpublished versions of templates that are still mutable. There could be many in progress drafts for a template.
  name: Dyspatch SMS Drafts API
  slug: dyspatch-sms-drafts-api
- description: SMS Localization objects are the same as Template objects except they contain localized content. If your account is using localizations then use this instead of the compiled Template object.
  name: Dyspatch SMS Localizations API
  slug: dyspatch-sms-localizations-api
- description: SMS Templates are the SMS templates found in your Dyspatch account. Only the published Template Draft is returned. A typical integration will start with using the Templates list endpoint to iterate th
  name: Dyspatch SMS Templates API
  slug: dyspatch-sms-templates-api
- description: Tags are a way of categorizing your resources (template and drafts) with helpful identifying information. You can decide what tags are useful for you, managing a master list of available tags and assi
  name: Dyspatch Tags API
  slug: dyspatch-tags-api
- description: Templates are the email templates found in your Dyspatch account. Only the published Template Draft is returned. A typical integration will start with using the Templates list endpoint to iterate thro
  name: Dyspatch Templates API
  slug: dyspatch-templates-api
- description: The Themes API from Dyspatch — 2 operation(s) for themes.
  name: Dyspatch Themes API
  slug: dyspatch-themes-api
- description: Voice Drafts represent unpublished versions of templates that are still mutable. There could be many in progress drafts for a template.
  name: Dyspatch Voice Drafts API
  slug: dyspatch-voice-drafts-api
- description: Voice Localization objects are the same as Template objects except they contain localized content. If your account is using localizations then use this instead of the compiled Template object.
  name: Dyspatch Voice Localizations API
  slug: dyspatch-voice-localizations-api
- description: Voice Templates are the Voice templates found in your Dyspatch account. Only the published Template Draft is returned. A typical integration will start with using the Templates list endpoint to iterat
  name: Dyspatch Voice Templates API
  slug: dyspatch-voice-templates-api
- description: The Workspaces API from Dyspatch — 2 operation(s) for workspaces.
  name: Dyspatch Workspaces API
  slug: dyspatch-workspaces-api
artifact_total: 26
asyncapis:
- description: ''
  name: Dyspatch Webhooks
  slug: dyspatch-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dyspatch.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dyspatch.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dyspatch.io/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dyspatch.io/administration/creating_api_keys/
- group: company
  title: ''
  type: Blog
  url: https://www.dyspatch.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dyspatch.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.dyspatch.io/
- group: start
  title: ''
  type: Login
  url: https://app.dyspatch.io/
- group: operate
  title: ''
  type: Support
  url: https://docs.dyspatch.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dyspatch.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dyspatch.io/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getdyspatch
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dyspatch.io
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dyspatch-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dyspatch-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dyspatch-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dyspatch-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dyspatch-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dyspatch-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dyspatch-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/dyspatch-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/dyspatch-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dyspatch-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dyspatch-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dyspatch-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dyspatch-webhooks.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/dyspatch-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dyspatch-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dyspatch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/dyspatch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dyspatch-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dyspatch-agentic-access.yml
created: '2026-07-17'
description: Dyspatch is an email template management and production platform that lets marketing, design, and engineering teams build, collaborate on, approve, localize, and publish transactional and marketing messages without hand-coding HTML. Content is authored in DML (Dyspatch Markup Language) using a modular, no-code drag-and-drop builder with reusable blocks and themes, then published to any ESP (Salesforce, HubSpot, Braze, Marketo, and others). Dyspatch also covers SMS, push, voice, and Live Activity messages, AMP for Email, and large-scale localization across hundreds of languages. The public REST API at api.dyspatch.io exposes published templates, drafts with an approval workflow, localizations and translations, customer profiles, themes, blocks, and tags, and is versioned by date through the Accept header. Dyspatch ships official OpenAPI-generated SDKs for six languages, a published MCP server, webhooks, and Agent Skills. Dyspatch is backed by Y Combinator.
image: https://www.dyspatch.io/wp-content/uploads/2025/04/fb-share-1.png
layout: provider
mcp_servers:
- description: ''
  name: dyspatch-mcp.yml
  slug: dyspatch-mcpyml
modified: '2026-07-18'
name: Dyspatch
nav: Providers
network: true
overview: 'Dyspatch publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Blocks API, Customer Profiles API, Drafts API, and 17 more. Tagged areas include Company, Email, Email Templates, Marketing, and Messaging.


  The Dyspatch catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dyspatch''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 26 more developer resources.'
random_paper: 48
score:
  band: developing
  composite: 59.1
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 72.6
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 59.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Dyspatch Authentication
  slug: dyspatch-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dyspatch Domain Security
  slug: dyspatch-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Dyspatch Vulnerability Disclosure
  slug: dyspatch-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: dyspatch
tags:
- Company
- Email
- Email Templates
- Marketing
- Messaging
- SMS
- Push Notifications
- Localization
- Content Management
- Developer Tools
website: https://docs.dyspatch.io
---
