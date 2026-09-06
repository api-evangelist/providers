---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: The Vidyard Dashboard API provides full CRUD access to your Vidyard account assets including players, videos, chapters, organizations, teams, users, roles, events, campaigns, tags, webhooks, embeds, a
  name: Vidyard Dashboard API
  slug: vidyard-dashboard-api
- description: The Video Agent API enables integration of Vidyard's AI-powered video generation into any application or custom workflow. It allows triggering personalized video creation of Vidyard campaigns programm
  name: Vidyard Video Agent API
  slug: vidyard-video-agent-api
- description: The Analytics Webhook API allows subscribing to and streaming video view data from Vidyard to an external application. View events are delivered as HTTP POST requests in JSON format to a configured en
  name: Vidyard Analytics Webhook API
  slug: vidyard-analytics-webhook-api
artifact_total: 12
asyncapis:
- description: ''
  name: Vidyard Webhooks
  slug: vidyard-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/vidyard-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vidyard-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vidyard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vidyard.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.vidyard.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Vidyard
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vidyard
- group: company
  title: ''
  type: Blog
  url: https://www.vidyard.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vidyard.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vidyard.com/
- group: other
  title: ''
  type: X
  url: https://x.com/vidyard
- group: commercial
  title: ''
  type: Plans
  url: plans/vidyard-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vidyard-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vidyard-finops.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/vidyard-a2a.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vidyard-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vidyard-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vidyard-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vidyard-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vidyard-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vidyard-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vidyard-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vidyard-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vidyard-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vidyard-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/vidyard-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vidyard-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/vidyard-cli.yml
- group: design
  title: ''
  type: Components
  url: components/vidyard-components.yml
- group: build
  title: ''
  type: Postman
  url: https://vy-docs.s3.amazonaws.com/postman/VidyardAnalyticsWebhooks.postman_collection.json
- group: auth
  title: ''
  type: Security
  url: https://www.vidyard.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.vidyard.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.vidyard.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.vidyard.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://knowledge.vidyard.com/hc/en-us/articles/360010000133-How-to-use-the-Vidyard-Dashboard-API
- group: operate
  title: ''
  type: Support
  url: https://knowledge.vidyard.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://knowledge.vidyard.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vidyard
- group: start
  title: ''
  type: SignUp
  url: https://www.vidyard.com/sign-up-for-free/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vidyard.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vidyard.com/privacy/
created: '2026-06-12'
description: Vidyard is a video platform for business that provides REST APIs for managing video libraries, generating sharing links, tracking viewer analytics, and integrating with CRM and marketing tools. The Dashboard API enables programmatic control over players, videos, chapters, organizations, teams, users, events, campaigns, webhooks, and more. The Video Agent API supports AI-powered personalized video creation workflows, and the Analytics Webhook API streams real-time viewer data to external systems.
finops:
- name: Vidyard Finops
  service_category: ''
  slug: vidyard-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vidyard.png
jsonld:
- class_count: 6
  name: Vidyard Context
  property_count: 20
  slug: vidyard-context
layout: provider
modified: '2026-08-13'
name: Vidyard
nav: Providers
network: true
overview: 'Vidyard publishes 1 API on the [APIs.io](https://apis.io/) network: Analytics Webhook API. Tagged areas include Video, Video Platform, Video Analytics, Video Sharing, and Sales Video.


  The Vidyard catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Vidyard''s developer surface includes documentation, GitHub presence, engineering blog, pricing, authentication, changelog, CLI, and 34 more developer resources.'
plans:
- name: Vidyard Plans Pricing
  plan_count: 4
  slug: vidyard-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Vidyard Rate Limits
  slug: vidyard-rate-limits
score:
  band: exemplar
  composite: 69.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 78.0
    catalog_earned_first_party: 24.0
    catalog_gap: 37.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 55.8
    developer_ergonomics: 76.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 68.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vidyard/refs/heads/main/screenshots/vidyard-2026-06-20T201023.png
security:
- kind: authentication
  name: Vidyard Authentication
  slug: vidyard-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Vidyard Domain Security
  slug: vidyard-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Vidyard Vulnerability Disclosure
  slug: vidyard-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Vidyard Trust Center
  slug: vidyard-trust-center
  summary_line: SOC 2 Type 2, GDPR, Microsoft SSPA
slug: vidyard
tags:
- Video
- Video Platform
- Video Analytics
- Video Sharing
- Sales Video
- CRM Integration
- Marketing
- AI Video
- Webhook
website: https://www.vidyard.com/
---
