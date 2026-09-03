---
access_model:
  confidence: high
  label: Self-serve signup, 14-day free trial
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - https://encharge.io/pricing
  - authentication
  trial: true
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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Encharge Agentic Access
  operation_count: 69
  slug: encharge-agentic-access
  summary_line: 69 operations · 43 acting
api_count: 1
apis:
- description: REST API for sending transactional emails through Encharge. Accepts JSON at POST /v1/emails/send with exactly one of template, html or text, returns 202 Accepted, and authenticates via the same accoun
  name: Encharge Transactional Email API
  slug: transactional-email-api
- description: Single-endpoint Ingest API for creating/updating people and submitting product events into Encharge from an application backend. POSTs JSON to https://ingest.encharge.io/v1/ with the account write key
  name: Encharge Ingest API
  slug: ingest-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Account API from Encharge — 2 operation(s) for account information.
  name: Encharge Account API
  slug: encharge-account-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Broadcasts API from Encharge — 1 operation(s) for sending broadcasts.
  name: Encharge Broadcasts API
  slug: encharge-broadcasts-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Custom Objects API from Encharge — 18 operation(s) for creating, reading, searching and associating custom objects and companies.
  name: Encharge Custom Objects API
  slug: encharge-customobjects-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Custom Objects Schema API from Encharge — 10 operation(s) for defining object types, their fields, and the associations between them.
  name: Encharge Custom Objects Schema API
  slug: encharge-customobjectsschema-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Email Templates API from Encharge — 9 operation(s) for creating and versioning email templates.
  name: Encharge Email Templates API
  slug: encharge-emailtemplates-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Folders API from Encharge — 2 operation(s) for organizing assets into folders.
  name: Encharge Folders API
  slug: encharge-folders-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The People API from Encharge — 5 operation(s) for creating, updating, reading, unsubscribing and archiving people.
  name: Encharge People API
  slug: encharge-people-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Person Fields API from Encharge — 4 operation(s) for managing person fields.
  name: Encharge Person Fields API
  slug: encharge-personfields-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Segments API from Encharge — 4 operation(s) for dynamic segments.
  name: Encharge Segments API
  slug: encharge-segments-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The email settings API from Encharge — 5 operation(s) for adding and verifying sending domains.
  name: Encharge Email Domain Settings API
  slug: encharge-settings-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Tags API from Encharge — 2 operation(s) for tagging and untagging people.
  name: Encharge Tags API
  slug: encharge-tags-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Tags Management API from Encharge — 5 operation(s) for the account tag registry and tag counts.
  name: Encharge Tags Management API
  slug: encharge-tags-management-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Webhooks API from Encharge — 2 operation(s) for creating and deleting event subscriptions against Encharge's event catalog.
  name: Encharge Webhooks API
  slug: encharge-webhooks-api
artifact_total: 34
asyncapis:
- description: ''
  name: Encharge Webhooks
  slug: encharge-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Encharge REST Account API
  slug: open-encharge-account-api
- collection_type: open
  name: Encharge REST Account Events API
  slug: open-encharge-events-api
- collection_type: open
  name: Encharge REST Account Fields API
  slug: open-encharge-fields-api
- collection_type: open
  name: Encharge REST Account Ingest API
  slug: open-encharge-ingest-api
- collection_type: open
  name: Encharge REST Account People API
  slug: open-encharge-people-api
- collection_type: open
  name: Encharge REST Account Segments API
  slug: open-encharge-segments-api
- collection_type: open
  name: Encharge REST Account Tags API
  slug: open-encharge-tags-api
- collection_type: open
  name: Encharge REST Account Transactional Email API
  slug: open-encharge-transactional-email-api
- collection_type: open
  name: Encharge REST API
  slug: open-encharge
common:
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/encharge-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/encharge-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/encharge-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://encharge.io/responsible-disclosure/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/encharge-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/encharge-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://gdpr.encharge.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/encharge-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/encharge-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/encharge-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/encharge-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/encharge-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/encharge-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/encharge-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/encharge-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/encharge-well-known.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/encharge-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/encharge-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/encharge-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://encharge.noorahq.com/changelog
- group: operate
  title: ''
  type: Roadmap
  url: https://encharge.noorahq.com/roadmap
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/encharge-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/encharge-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/encharge-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.encharge.io/llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/encharge
- group: company
  title: ''
  type: Website
  url: https://encharge.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.encharge.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.encharge.io
- group: docs
  title: ''
  type: API Documentation
  url: https://docs.encharge.io/api-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://app-encharge-resources.s3.amazonaws.com/redoc.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.encharge.io/getting-started/connecting-your-app-to-encharge
- group: operate
  title: ''
  type: Support
  url: https://help.encharge.io
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/460427/TVRj5o3E
- group: commercial
  title: ''
  type: Pricing
  url: https://encharge.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.encharge.io/signup
- group: start
  title: ''
  type: Signup
  url: https://app.encharge.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://encharge.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://encharge.io/privacy-policy/
- group: build
  title: ''
  type: API Integration
  url: https://encharge.io/integrations/api/
- group: company
  title: ''
  type: Blog
  url: https://encharge.io/feed/
created: '2026-05-11'
description: 'Encharge is a behavior-based marketing automation platform built for SaaS companies, with a visual flow builder, broadcasts, segments, lead scoring, A/B testing, native forms, custom objects, and 50+ native integrations (HubSpot, Stripe, Salesforce, Segment, Facebook Ads, and more). The platform combines email marketing automation, user profiles, and product-event tracking to send targeted emails based on what users do (or do not do) in a SaaS product. Encharge exposes three developer surfaces: a REST API of 69 operations covering people, person fields, segments, tags, broadcasts, email templates, sending domains, custom objects and event subscriptions, described by a published OpenAPI 3.0 definition; a prose-documented Transactional Email API; and an Ingest API for streaming people and product events from a backend. All three authenticate with the same account token, passed in the X-Encharge-Token header or a token query parameter, with OAuth 2 available for partner apps.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/encharge.png
layout: provider
modified: '2026-08-13'
name: Encharge
nav: Providers
network: true
overview: 'Encharge publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Transactional Email API, Ingest API, Account API, and 12 more. Tagged areas include Email Marketing, Marketing Automation, Transactional Email, Software-as-a-Service, and Behavioral Email.


  The Encharge catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Encharge''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, pricing, and 35 more developer resources.'
plans:
- name: Encharge Plans Pricing
  plan_count: 3
  slug: encharge-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Encharge Rate Limits
  slug: encharge-rate-limits
scopes:
- name: Encharge Scopes
  scope_count: 8
  slug: encharge-scopes
  summary_line: 8 scopes · authorizationCode
score:
  band: developing
  composite: 53.9
  coverage:
    artifact_dirs: 24
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 4.5
    contract_quality: 53.3
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/encharge/refs/heads/main/screenshots/encharge-2026-06-20T180652.png
security:
- kind: authentication
  name: Encharge Authentication
  slug: encharge-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Encharge Domain Security
  slug: encharge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Encharge Vulnerability Disclosure
  slug: encharge-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Encharge Trust Center
  slug: encharge-trust-center
  summary_line: GDPR
slug: encharge
tags:
- Email Marketing
- Marketing Automation
- Transactional Email
- Software-as-a-Service
- Behavioral Email
- Customer Engagement
- Customer Data
- Webhook
website: https://encharge.io
---
