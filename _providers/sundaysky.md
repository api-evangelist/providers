---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://help.sundaysky.com/hc/en-us/articles/6000894076957-Using-the-SundaySky-API-to-Connect-Data
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Storage-less HTTP API for real-time personalized video rendering. The caller POSTs a flat JSON object of viewer personalization fields (mapped in the SundaySky Studio data library) to the player-sessi
  name: SundaySky Video API
  slug: sundaysky-video-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://sundaysky.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.sundaysky.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://help.sundaysky.com/hc/en-us/articles/6000894076957-Using-the-SundaySky-API-to-Connect-Data
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sundaysky.com/hc/en-us/articles/18000152116509-Getting-Started-with-SundaySky
- group: operate
  title: ''
  type: Support
  url: https://help.sundaysky.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.sundaysky.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://sundaysky.com/resources/?_resource_type=blog
- group: operate
  title: ''
  type: StatusPage
  url: https://sundaysky.com/service-dashboard/
- group: operate
  title: ''
  type: Roadmap
  url: https://help.sundaysky.com/hc/en-us/articles/21123723976733-SundaySky-Product-Roadmap
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sundaysky-changelog.yml
- group: start
  title: ''
  type: Login
  url: https://app.sundaysky.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sundaysky
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sundaysky.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sundaysky.com/terms-of-service/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sundaysky-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sundaysky-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sundaysky-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sundaysky-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sundaysky-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sundaysky-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sundaysky-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sundaysky-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/sundaysky-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/sundaysky-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sundaysky-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sundaysky-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sundaysky-llms.txt
created: '2026-07-17'
description: SundaySky is an enterprise video personalization platform that uses AI to create, edit, and deliver dynamically personalized videos at scale. The platform lets organizations tailor video content to individual viewers using customer data and real-time rendering, serving customer experience, marketing, sales, and learning-and-development teams — with particular traction in regulated industries such as financial services, insurance, telecom, and healthcare. Its products include SundaySky Studio for content creation, the SundaySky Player, a Landing Page Builder, and analytics and reporting. SundaySky publishes one documented HTTP API — the SundaySky Video API, a storage-less POST endpoint at apis.sundaysky.com that accepts a flat JSON payload of viewer personalization fields and returns a base64 player session used to render a video in real time — alongside a data-connector marketplace (Salesforce, HubSpot, Snowflake, Databricks, Google Sheets, Marketo, file upload, URL parameters)
  and a client-side player web component with a documented browser event surface. There is no self-serve developer portal, no published OpenAPI, and no public pricing; platform access is sold and provisioned to enterprise customers. This profile was surfaced as a portfolio company of Norwest Venture Partners and enriched by the API Evangelist pipeline.
image: https://sundaysky.com/favicon.ico
layout: provider
modified: '2026-08-13'
name: SundaySky
nav: Providers
network: true
overview: 'SundaySky publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video, Personalization, Video Personalization, and Marketing.


  SundaySky''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 20 more developer resources.'
plans:
- name: Sundaysky Plans Pricing
  plan_count: 0
  slug: sundaysky-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Sundaysky Rate Limits
  slug: sundaysky-rate-limits
score:
  band: thin
  composite: 32.6
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 32.6
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Sundaysky Authentication
  slug: sundaysky-authentication
  summary_line: none/saml · 3 schemes
- kind: domain-security
  name: Sundaysky Domain Security
  slug: sundaysky-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sundaysky Trust Center
  slug: sundaysky-trust-center
  summary_line: trust center published
slug: sundaysky
tags:
- Company
- Video
- Personalization
- Video Personalization
- Marketing
- Customer Experience
- Artificial Intelligence
- Enterprise
- Video Generation
- Media
- Analytics
- MarTech
website: https://sundaysky.com
---
