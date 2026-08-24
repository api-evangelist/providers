---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.2
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: REST API for the Affise Performance platform enabling admins and affiliates to manage offers, track conversions, retrieve statistics, handle publisher payouts, and automate billing operations programm
  name: Affise Performance API
  slug: affise-performance-api
- description: Mobile Measurement Partner API enabling mobile app attribution tracking, install measurement, event tracking, and audience analytics for iOS, Android, and cross-platform mobile applications.
  name: Affise MMP API
  slug: affise-mmp-api
artifact_total: 12
asyncapis:
- description: ''
  name: Affise Postbacks Webhooks
  slug: affise-postbacks-webhooks
collections:
- collection_type: open
  name: API Documentation
  slug: open-affise
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/affise-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://srs.s4e.io/affise.com/report
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/affise-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/affise-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/affise-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/affise-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/affise-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/affise-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/affise-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/affise-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://affise.com/gdpr/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/affise-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/affise-postbacks-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/affise-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/affise-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/affise-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://affise.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://api.affise.com/docs3.2/
- group: start
  title: ''
  type: GettingStarted
  url: https://help-center.affise.com/en/articles/6463675-start-with-api-admins
- group: operate
  title: ''
  type: Support
  url: https://help-center.affise.com/en/
- group: build
  title: ''
  type: Postman
  url: https://github.com/affise/affise-postman-api-collection
- group: commercial
  title: ''
  type: TermsOfService
  url: https://affise.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://affise.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://affise.com/signup/
- group: company
  title: ''
  type: Website
  url: https://affise.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help-center.affise.com/en/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/affise
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/affise-com/
- group: company
  title: ''
  type: Blog
  url: https://affise.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://affise.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.affise.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/GetAffise
- group: commercial
  title: ''
  type: Plans
  url: plans/affise-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/affise-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/affise-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://affise.com/blog/feed/
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/affise-context.jsonld
created: '2026-06-13'
description: Affise is a performance marketing platform with a REST API for managing affiliate offers, publishers, conversions, payouts, and accessing detailed campaign analytics. The API supports both admin and affiliate panel operations using API key authentication with GET and POST methods across statistics, conversions, offers, partners, and billing endpoints.
finops:
- name: Affise Finops
  service_category: ''
  slug: affise-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/affise.png
jsonld:
- class_count: 37
  name: Affise Context
  property_count: 4
  slug: affise-context
layout: provider
mcp_servers:
- description: ''
  name: Affise MCP Server
  slug: affise-mcp-server
modified: '2026-08-13'
name: Affise
nav: Providers
network: true
overview: 'Affise publishes 1 API on the [APIs.io](https://apis.io/) network: Performance API. Tagged areas include Affiliate Marketing, Performance Marketing, Conversions, Publishers, and Analytics.


  The Affise catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Affise''s developer surface includes authentication, sandbox, API reference, getting-started guide, support, signup flow, documentation, and 32 more developer resources.'
plans:
- name: Affise Plans Pricing
  plan_count: 7
  slug: affise-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Affise Rate Limits
  slug: affise-rate-limits
score:
  band: strong
  composite: 66.0
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 30.3
    contract_quality: 67.7
    developer_ergonomics: 78.0
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 21.1
  previous_composite: 66.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/affise/refs/heads/main/screenshots/affise-2026-06-20T165649.png
security:
- kind: authentication
  name: Affise Authentication
  slug: affise-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Affise Domain Security
  slug: affise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Affise Vulnerability Disclosure
  slug: affise-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: affise
tags:
- Affiliate Marketing
- Performance Marketing
- Conversions
- Publishers
- Analytics
- Attribution
website: https://affise.com/
---
