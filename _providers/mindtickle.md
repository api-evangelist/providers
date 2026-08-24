---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: Core REST API for managing users, groups, modules, learner details, and reporting within the Mindtickle revenue productivity platform. Supports SCIM-based user provisioning and returns JSON responses.
  name: Mindtickle REST API
  slug: mindtickle-rest-api
- description: GraphQL public API providing programmatic access to call recordings, transcriptions, coaching scores, and conversation intelligence data from the Mindtickle Call AI platform. Authenticated via OAuth 2
  name: Mindtickle Call AI Public API
  slug: mindtickle-call-ai-graphql-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/mindtickle-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mindtickle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mindtickle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mindtickle.com/platform/integrations/
- group: company
  title: ''
  type: Blog
  url: https://www.mindtickle.com/blog/
- group: company
  title: ''
  type: News
  url: https://www.mindtickle.com/news/
- group: operate
  title: ''
  type: Status
  url: https://status.mindtickle.com
- group: start
  title: ''
  type: Login
  url: https://app.mindtickle.com/
- group: operate
  title: ''
  type: Support
  url: https://help.mindtickle.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.mindtickle.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mindtickle.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mindtickle.com/terms-of-service/
- group: auth
  title: ''
  type: Security
  url: https://www.mindtickle.com/security/policy/
- group: build
  title: ''
  type: IntegrationPlatform
  url: https://www.mindtickle.com/platform/integrations/
- group: other
  title: ''
  type: Salesforce
  url: https://www.mindtickle.com/platform-integrations-salesforce/
- group: commercial
  title: ''
  type: Plans
  url: plans/mindtickle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mindtickle-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mindtickle-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mindtickle-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mindtickle-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mindtickle-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mindtickle-scopes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mindtickle-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mindtickle-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mindtickle.com/
- group: operate
  title: ''
  type: SLA
  url: https://www.mindtickle.com/service-level-agreement/
- group: design
  title: ''
  type: Conformance
  url: conformance/mindtickle-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.mindtickle.com/compliance/
- group: design
  title: ''
  type: Conventions
  url: conventions/mindtickle-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/mindtickle-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mindtickle-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mindtickle-data-model.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MindTickle
created: '2026-06-13'
description: Mindtickle is an AI-powered revenue productivity platform that unifies sales enablement, training, coaching, conversation intelligence, and digital sales rooms into a single solution. It provides REST and GraphQL APIs for managing readiness programs, user provisioning, content, call intelligence, and analytics for revenue teams.
finops:
- name: Mindtickle Finops
  service_category: ''
  slug: mindtickle-finops
graphqls:
- description: Mindtickle provides a public GraphQL API for its Call AI platform, offering programmatic access to call recordings, transcriptions, coaching scores, and conversation intelligence data. The REST API co
  name: Mindtickle GraphQL API
  slug: mindtickle-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mindtickle.png
layout: provider
modified: '2026-08-14'
name: Mindtickle
nav: Providers
network: true
overview: 'Mindtickle publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Enablement, Revenue Productivity, Sales Readiness, Coaching, and Conversation Intelligence.


  Mindtickle''s developer surface includes documentation, engineering blog, product news, status page, support, authentication, and 27 more developer resources.'
plans:
- name: Mindtickle Plans Pricing
  plan_count: 4
  slug: mindtickle-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Mindtickle Rate Limits
  slug: mindtickle-rate-limits
scopes:
- name: Mindtickle Scopes
  scope_count: 7
  slug: mindtickle-scopes
  summary_line: 7 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 48.7
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 18.2
    contract_quality: 38.9
    developer_ergonomics: 14.3
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 48.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 70.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/screenshots/mindtickle-2026-06-20T185602.png
security:
- kind: authentication
  name: Mindtickle Authentication
  slug: mindtickle-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Mindtickle Domain Security
  slug: mindtickle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mindtickle Vulnerability Disclosure
  slug: mindtickle-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Mindtickle Trust Center
  slug: mindtickle-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR, CSA STAR
slug: mindtickle
tags:
- Sales Enablement
- Revenue Productivity
- Sales Readiness
- Coaching
- Conversation Intelligence
- Learning Management
- Content Management
- Call AI
- Revenue Intelligence
website: https://www.mindtickle.com/
---
