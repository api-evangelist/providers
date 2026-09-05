---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
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
    error_semantics: false
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
  score: 22.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: REST-first JSON API to Contently's vetted creative network and project workflow. Search creators, open NDA-scoped projects, brief and message contributors, submit draft reviews, approve and pay out wo
  name: Contently Talent API
  slug: contently-talent-api
artifact_total: 8
asyncapis:
- description: ''
  name: Contently Webhooks
  slug: contently-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://contently.com
- group: docs
  title: ''
  type: Documentation
  url: https://contently.com/platform/talent-api/
- group: docs
  title: ''
  type: APIReference
  url: https://contently.com/platform/talent-api/
- group: company
  title: ''
  type: Blog
  url: https://contently.com/strategist/
- group: operate
  title: ''
  type: Support
  url: https://support.contently.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contently
- group: start
  title: ''
  type: Login
  url: https://contently.com/signin/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contently.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contently.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://contently.com/trust/security/
- group: auth
  title: ''
  type: Security
  url: https://contently.com/trust/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/contently-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contently-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/contently-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/contently-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/contently-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/contently-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/contently-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/contently-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/contently-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/contently-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/contently-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/contently-llms.txt
created: '2026-07-17'
description: Contently is an end-to-end content marketing platform pairing enterprise content operations software with a vetted global network of 10,000+ freelance writers, editors, designers, and strategists, positioned for regulated industries such as financial services, healthcare, and insurance. Brands use Contently to plan editorial calendars, source and manage creative talent, run review-and-approval workflows with credentialed reviewers, publish across channels, and measure content performance. For developers Contently documents the Talent API, a REST-first JSON API secured with scoped OAuth2 that lets teams search vetted creators, open NDA-scoped projects, brief and message contributors, submit draft reviews, approve and pay out work, and check funded balances, with state-change webhooks over Slack, Teams, or raw HTTP. Contently also advertises an MCP server registering six tools, though no endpoint is published. No OpenAPI specification, reference documentation, or developer portal
  is published; API access is obtained through a sales conversation. Contently maintains SOC 2 Type II, GDPR, CCPA, HIPAA (BAA), and FINRA reviewer-pool posture with a published controls matrix.
image: https://contently.com/wp-content/themes/contently-redesign-theme/assets/images/brand/og-default-1200x630.png
layout: provider
modified: '2026-08-13'
name: Contently
nav: Providers
network: true
overview: 'Contently publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Content Marketing, Talent Marketplace, Freelance, and Content Creation.


  The Contently catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Contently''s developer surface includes documentation, API reference, engineering blog, support, authentication, and 18 more developer resources.'
plans:
- name: Contently Plans Pricing
  plan_count: 0
  slug: contently-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Contently Rate Limits
  slug: contently-rate-limits
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 38.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/contently/refs/heads/main/screenshots/contently-2026-07-25T210335.png
security:
- kind: authentication
  name: Contently Authentication
  slug: contently-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Contently Domain Security
  slug: contently-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Contently Vulnerability Disclosure
  slug: contently-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Contently Trust Center
  slug: contently-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA, HIPAA, FINRA
slug: contently
tags:
- Company
- Content Marketing
- Talent Marketplace
- Freelance
- Content Creation
- Publishing
- Editorial Workflow
- Regulated Content
- Compliance
website: https://contently.com
---
