---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
api_count: 1
apis:
- description: The Sprout Social Public API provides programmatic access to publishing, analytics, messaging, listening, and social care case data across major social networks. Requires Advanced plan or higher.
  name: Sprout Social API
  slug: sprout-social-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sprout-social-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sprout-social-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sproutsocial.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.sproutsocial.com/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sproutsocial
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sprout-social-inc-
- group: company
  title: ''
  type: Blog
  url: https://sproutsocial.com/insights/
- group: commercial
  title: ''
  type: Pricing
  url: https://sproutsocial.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sproutsocialstatus.com
- group: other
  title: ''
  type: X
  url: https://x.com/SproutSocial
- group: commercial
  title: ''
  type: Plans
  url: plans/sprout-social-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sprout-social-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sprout-social-finops.yml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.sproutsocial.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.sproutsocial.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.sproutsocial.com/docs/#getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.sproutsocial.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://sproutsocial.com/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sproutsocial.com/legal/api-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sproutsocial.com/legal/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://sproutsocial.com/responsible-disclosure-policy/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sprout-social-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.sproutsocial.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/sprout-social-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sprout-social-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sprout-social-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sprout-social-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sprout-social-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sprout-social-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sprout-social-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sprout-social-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sprout-social-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/sprout-social-packages.yml
- group: design
  title: ''
  type: Components
  url: components/sprout-social-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sprout-social-llms.txt
created: '2026-06-13'
description: Sprout Social is a social media management platform with a REST API for publishing posts, monitoring mentions, managing messages, accessing analytics, and reporting across social networks including Instagram, Facebook, LinkedIn, TikTok, YouTube, and X.
finops:
- name: Sprout Social Finops
  service_category: ''
  slug: sprout-social-finops
graphqls:
- description: '> **Provenance warning (2026-08-13).** Sprout Social does **not** publish a GraphQL API.'
  name: Sprout Social GraphQL Schema
  slug: sprout-social-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sprout-social.png
jsonld:
- class_count: 0
  name: Sprout Social Context
  property_count: 0
  slug: sprout-social
layout: provider
modified: '2026-08-13'
name: Sprout Social
nav: Providers
network: true
overview: 'Sprout Social publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social-Media, Social Media Management, Publishing, Analytics, and Reporting.


  The Sprout Social catalog on APIs.io includes 1 JSON-LD context.


  Sprout Social''s developer surface includes documentation, engineering blog, pricing, API reference, getting-started guide, support, signup flow, and 29 more developer resources.'
plans:
- name: Sprout Social Plans Pricing
  plan_count: 5
  slug: sprout-social-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Sprout Social Rate Limits
  slug: sprout-social-rate-limits
scopes:
- name: Sprout Social Scopes
  scope_count: 6
  slug: sprout-social-scopes
  summary_line: 6 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 61.8
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 48.9
    developer_ergonomics: 57.1
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 68.4
  previous_composite: 61.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sprout-social/refs/heads/main/screenshots/sprout-social-2026-08-17T082048.png
security:
- kind: authentication
  name: Sprout Social Authentication
  slug: sprout-social-authentication
  summary_line: http/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Sprout Social Domain Security
  slug: sprout-social-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sprout Social Vulnerability Disclosure
  slug: sprout-social-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
- kind: trust-center
  name: Sprout Social Trust Center
  slug: sprout-social-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: sprout-social
tags:
- Social-Media
- Social Media Management
- Publishing
- Analytics
- Reporting
- Messaging
- Listening
website: https://sproutsocial.com
---
