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
  band: agent-aware
  dimensions:
    agent_card: false
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
  score: 25.2
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The core CrowdTwist REST/JSON API for loyalty program members and their points economy — create, read, update and delete members; award points for activities; read the activity, reward and badge catal
  name: Oracle CrowdTwist Loyalty and Engagement API
  slug: crowdtwist-loyalty
- description: The point-of-sale side of CrowdTwist, served from a separate templated host. Purchase posts a receipt with line items, tenders and coupons and returns the per-item point breakdown including bonus-camp
  name: Oracle CrowdTwist Commerce (POS) API
  slug: crowdtwist-commerce
artifact_total: 10
asyncapis:
- description: ''
  name: Crowdtwist Data Push Webhooks
  slug: crowdtwist-data-push-webhooks
collections:
- collection_type: postman
  name: CrowdTwist Starter Kit
  slug: postman-crowdtwist-starter-kit
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crowdtwist-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crowdtwist.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/index.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/GettingStarted.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/GettingStarted.html
- group: operate
  title: ''
  type: Support
  url: https://support.oracle.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: build
  title: ''
  type: Postman
  url: postman/crowdtwist-starter-kit.postman_collection.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/crowdtwist-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crowdtwist-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crowdtwist-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crowdtwist-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/crowdtwist-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/crowdtwist-data-push-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/crowdtwist-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/crowdtwist-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crowdtwist-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/crowdtwist-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crowdtwist-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/crowdtwist-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crowdtwist-llms.txt
- group: auth
  title: ''
  type: Security
  url: security/crowdtwist-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crowdtwist-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/crowdtwist-trust-center.yml
created: '2026-07-17'
description: CrowdTwist is a customer loyalty and engagement platform founded in New York City in 2009 and accelerated through Techstars. It lets consumer brands build multi-channel loyalty programs that reward customers for purchases, social sharing, referrals, and other engagement across web, mobile, email, and social channels, with points redeemable for rewards. CrowdTwist exposed a REST API for managing members, tracking earning and redemption activities, and administering points, tiers, and campaigns. Oracle acquired CrowdTwist in March 2019 and folded it into Oracle CX Marketing as Oracle CrowdTwist Loyalty and Engagement; the standalone crowdtwist.com site now redirects to Oracle and the developer documentation is hosted on Oracle Help Center.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crowdtwist.png
layout: provider
modified: '2026-08-13'
name: CrowdTwist
nav: Providers
network: true
overview: 'CrowdTwist publishes 1 API on the [APIs.io](https://apis.io/) network: Oracle CrowdTwist Loyalty and Engagement API. Tagged areas include Company, Loyalty, Customer Engagement, Marketing, and Gamification.


  The CrowdTwist catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CrowdTwist''s developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, sandbox, and 19 more developer resources.'
plans:
- name: Crowdtwist Plans Pricing
  plan_count: 5
  slug: crowdtwist-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Crowdtwist Rate Limits
  slug: crowdtwist-rate-limits
score:
  band: developing
  composite: 50.7
  coverage:
    artifact_dirs: 18
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 42.7
    developer_ergonomics: 66.7
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 55.3
  previous_composite: 50.7
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crowdtwist/refs/heads/main/screenshots/crowdtwist-2026-07-25T210811.png
security:
- kind: authentication
  name: Crowdtwist Authentication
  slug: crowdtwist-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Crowdtwist Domain Security
  slug: crowdtwist-domain-security
  summary_line: TLSv1.2 · HSTS
- kind: vulnerability-disclosure
  name: Crowdtwist Vulnerability Disclosure
  slug: crowdtwist-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Crowdtwist Trust Center
  slug: crowdtwist-trust-center
  summary_line: trust center published
slug: crowdtwist
tags:
- Company
- Loyalty
- Customer Engagement
- Marketing
- Gamification
- Rewards
- Oracle
- CX Marketing
- Loyalty Programs
- Points
- Retail
- Commerce
- Segmentation
- Webhook
website: https://crowdtwist.com/
---
