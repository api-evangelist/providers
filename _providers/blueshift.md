---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.0
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Official hosted remote MCP server, in public beta, exposing a catalogue of 131 tools (97 read, 34 write) across campaigns, segments, customer profiles, catalogs, templates, shared assets, tags, report
  name: Blueshift MCP Server
  slug: blueshift-mcp-server
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: Adapters are entities that provide integration to various services with Blueshift. For example, we provide adapters for various services such as Mailgun, Sendgrid, and Sparkpost for sending emails, an
  name: Blueshift Adapters API
  slug: blueshift-adapters-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: Manage your campaigns in Blueshift.
  name: Blueshift Campaigns API
  slug: blueshift-campaigns-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: A catalog is a list of items which may include content or products.
  name: Blueshift Catalog API
  slug: blueshift-catalog-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: A custom user list contains information about the users of your site such as name, email, phone number, and location. You can use this list as a segment and run campaigns for them.
  name: Blueshift Custom user lists API
  slug: blueshift-custom-user-lists-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: Blueshift hosts 360 degree customer profile for each of your users to represent all of their demographic, behavioral and engagement activity.
  name: Blueshift Customer API
  slug: blueshift-customer-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: Customer groups link multiple customer profiles to a common parent entity with shared attributes. Use these endpoints to delete a group or remove a user from a group.
  name: Blueshift Customer groups API
  slug: blueshift-customer-groups-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: Email template lifecycle management
  name: Blueshift Email template API
  slug: blueshift-email-template-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: Validate single or bulk email addresses to assess deliverability and risk.
  name: Blueshift Email validation API
  slug: blueshift-email-validation-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: Use the event APIs to send events from your servers.
  name: Blueshift Event API
  slug: blueshift-event-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: External fetch is a Blueshift capability that lets you include dynamic content from external servers that is fetched “just in time” before sending a message.
  name: Blueshift External fetch API
  slug: blueshift-external-fetch-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: Interest alerts store information about users' interests. When an event occurs in an area or topic in which multiple users are interested, you can trigger a single API call to send a notification to a
  name: Blueshift Interest alerts API
  slug: blueshift-interest-alerts-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: The Live Activities API from Blueshift — 2 operation(s) for live activities.
  name: Blueshift Live Activities API
  slug: blueshift-live-activities-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: Use the Live content API endpoint to insert content recommendations in your website and mobile apps.
  name: Blueshift Live content API
  slug: blueshift-live-content-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: Promotions allows you to manage promo codes that you may wish to send to your customers through Blueshift Campaigns
  name: Blueshift Promotions API
  slug: blueshift-promotions-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: Push template lifecycle management
  name: Blueshift Push template API
  slug: blueshift-push-template-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: You can use the `customer_search` API to search for events associated with a customer.
  name: Blueshift Search API
  slug: blueshift-search-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: A segment is a list of users that satisfy a criteria. For example, you can create a segment for users who are located in the San Francisco area and run campaigns for them.
  name: Blueshift Segments API
  slug: blueshift-segments-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: Manage reusable assets such as HTML, rich text, subject lines, and visual editor content.
  name: Blueshift Shared assets API
  slug: blueshift-shared-assets-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: SMS template lifecycle management
  name: Blueshift SMS template API
  slug: blueshift-sms-template-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: Retrieve subscription groups and view detailed information for each subscription group.
  name: Blueshift Subscription groups API
  slug: blueshift-subscription-groups-api
- baseURL: https://api.getblueshift.com
  baseurl_source: declared
  description: Tags are folder-based entities that you can use to organize your resources. Each tag folder contains its own isolated set of tags.
  name: Blueshift Tags API
  slug: blueshift-tags-api
artifact_total: 31
asyncapis:
- description: ''
  name: Blueshift Webhooks
  slug: blueshift-webhooks
collections:
- collection_type: open
  name: Blueshift APIs
  slug: open-blueshift
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/blueshift-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/blueshift-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
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
- description: Blueshift operates an official hosted remote MCP server, in public beta, at https://app.getblueshift.com/mcp (US and rest of world) and https://app.eu.getblueshift.com/mcp (EU). Transport is streamabl
  name: Blueshift MCP Server
  slug: blueshift-mcp-server
modified: '2026-08-12'
name: Blueshift
nav: Providers
network: true
overview: 'Blueshift publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Adapters API, Campaigns API, Catalog API, and 18 more. Tagged areas include Customer Data Platform, Customer Engagement, Marketing Automation, Cross-Channel Messaging, and Email.


  The Blueshift catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Blueshift''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Blueshift Plans Pricing
  plan_count: 3
  slug: blueshift-plans-pricing
random_paper: 0
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
  band: exemplar
  composite: 67.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 0.0
    contract_quality: 63.1
    developer_ergonomics: 55.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 73.7
  previous_composite: 67.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 65.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blueshift/refs/heads/main/screenshots/blueshift-2026-08-17T080647.png
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
- Customer Data Platform
- Customer Engagement
- Marketing Automation
- Cross-Channel Messaging
- Email
- SMS
- Push Notifications
- Segmentation
- Personalization
- Product Recommendations
- Event Tracking
- Product Catalog
- MarTech
- MCP
- agent-native
website: https://blueshift.com/
---
