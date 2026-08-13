---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: 'The Blueshift REST API: 81 operations across 21 resource groups covering customer profiles and privacy operations (create/update, bulk, merge, forget/unforget, delete), event ingestion (single, bulk, '
  name: Blueshift REST API
  slug: blueshift-rest-api
- description: Official hosted remote MCP server, in public beta, exposing a catalogue of 131 tools (97 read, 34 write) across campaigns, segments, customer profiles, catalogs, templates, shared assets, tags, report
  name: Blueshift MCP Server
  slug: blueshift-mcp-server
artifact_total: 10
asyncapis:
- description: ''
  name: Blueshift Webhooks
  slug: blueshift-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/blueshift-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blueshift-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blueshift.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.blueshift.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.blueshift.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.blueshift.com/reference/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.blueshift.com/docs/generate-api-keys
- group: operate
  title: ''
  type: Support
  url: https://help.blueshift.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.blueshift.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://blueshift.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blueshift-labs
- group: commercial
  title: ''
  type: Pricing
  url: https://blueshift.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://blueshift.com/request-demo/
- group: start
  title: ''
  type: Login
  url: https://app.getblueshift.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blueshift.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blueshift.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: postman/blueshift-postman-collection.json
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blueshift.com/
- group: auth
  title: ''
  type: Compliance
  url: conformance/blueshift-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blueshift-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blueshift-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/blueshift-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/blueshift-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blueshift-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/blueshift-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/blueshift-plans-pricing.yml
- group: design
  title: ''
  type: Components
  url: components/blueshift-components.yml
created: '2026-08-12'
description: Blueshift is an AI-powered customer engagement and customer data platform (CDP) that unifies customer profiles, product and content catalogs, and behavioural event streams, then activates them across email, SMS, push, in-app messaging, mobile inbox, iOS Live Activities and on-site live content. Its public surface is a REST API on api.getblueshift.com (US) and api.eu.getblueshift.com (EU) covering customers, events, catalogs, segments, custom user lists, campaigns, templates, shared assets, promotions, external fetches, interest alerts, subscription groups and email validation, documented operation-by-operation with a machine-readable OpenAPI 3.0 document behind every reference page. Blueshift also runs an official OAuth 2.0 remote MCP server in public beta, and ships first-party SDKs for iOS, Android, React Native, Flutter and Cordova.
image: https://blueshift.com/wp-content/uploads/2025/10/web-featured-image.webp
layout: provider
mcp_servers:
- description: ''
  name: blueshift-mcp.yml
  slug: blueshift-mcpyml
modified: '2026-08-12'
name: Blueshift
nav: Providers
network: true
overview: 'Blueshift publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include customer-data-platform, customer-engagement, marketing-automation, cross-channel-messaging, and email.


  The Blueshift catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Blueshift''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
plans:
- name: Blueshift Plans Pricing
  plan_count: 3
  slug: blueshift-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 6
  name: Blueshift Rate Limits
  slug: blueshift-rate-limits
scopes:
- name: Blueshift Scopes
  scope_count: 0
  slug: blueshift-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 66.4
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 8.3
    operational_transparency: 68.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 56.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: authentication
  name: Blueshift Authentication
  slug: blueshift-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Blueshift Domain Security
  slug: blueshift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Blueshift Trust Center
  slug: blueshift-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: blueshift
tags:
- customer-data-platform
- customer-engagement
- marketing-automation
- cross-channel-messaging
- email
- sms
- push-notifications
- segmentation
- personalization
- product-recommendations
- event-tracking
- product-catalog
- martech
- mcp
- agent-native
website: https://blueshift.com/
---
