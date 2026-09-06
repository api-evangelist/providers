---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: human-only
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Public, read-only, unauthenticated JSON API for the Loomly status page, exposing overall system state, the four service components (Publishing, Analytics, Interactions, Website) and paginated incident
  name: Loomly Status API
  slug: loomly-status-api
- description: Loomly operates an OAuth 2.0 protected platform API that backs its Zapier app — 12 triggers (new post, post state updated, post publish successful/failed/required, new comment, new quick post, new cus
  name: Loomly Platform API (partner-gated)
  slug: loomly-platform-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.loomly.com
- group: docs
  title: ''
  type: Documentation
  url: https://loomly.zendesk.com/hc/en-us/
- group: start
  title: ''
  type: GettingStarted
  url: https://loomly.zendesk.com/hc/en-us/sections/38524587224347-Get-started
- group: operate
  title: ''
  type: Support
  url: https://loomly.zendesk.com/hc/en-us/requests/new
- group: company
  title: ''
  type: Blog
  url: https://www.loomly.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.loomly.com/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Loomly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/loomly
- group: other
  title: ''
  type: X
  url: https://x.com/LoomlySocial
- group: commercial
  title: ''
  type: Pricing
  url: https://www.loomly.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.loomly.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.loomly.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.loomly.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.loomly.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/loomly-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/loomly-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loomly-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/loomly-conventions.yml
- group: auth
  title: ''
  type: Security
  url: security/loomly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/loomly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/loomly-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loomly-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/loomly-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/loomly-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/loomly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loomly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/loomly-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/loomly-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Loomly runs no developer site and publishes no API reference or spec — its entire programmable surface (12 triggers, 2 write actions) is listed only on zapier.com, entered through an OAuth authorization endpoint at app.loomly.com/oauth/authorize that 302s to sign-in, and the api.loomly.com host a previous pass recorded does not resolve at all.
  evidence:
  - status: 404
    url: https://www.loomly.com/developers
  - status: 302
    url: https://app.loomly.com/oauth/authorize
  - status: 200
    url: https://zapier.com/apps/loomly/integrations
  - status: 404
    url: https://www.loomly.com/openapi.json
  reason: marketplace-only
  state: gated
created: '2026-06-13'
description: Loomly is a social media management and brand success platform for planning, creating, approving, scheduling and publishing content across Facebook, Instagram, LinkedIn, TikTok, YouTube, Pinterest, Snapchat, Threads, Bluesky and Google Business Profile, with collaboration and approval workflows, a content library, analytics and a community-management inbox. Loomly publishes no public developer API, API reference or machine-readable specification. Its only programmable surfaces are a partner-gated platform API reached through the Loomly Zapier app (12 triggers, 2 actions) over an OAuth 2.0 authorization flow at app.loomly.com, and a public read-only status API on status.loomly.com operated by SorryApp. Loomly was acquired by Bending Spoons on 2 January 2025.
finops:
- name: Loomly Finops
  service_category: ''
  slug: loomly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loomly.png
layout: provider
modified: '2026-08-13'
name: Loomly
nav: Providers
network: true
overview: 'Loomly publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Social-Media, Content Calendar, Scheduling, Approval Workflows, and Analytics.


  Loomly''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, changelog, and 21 more developer resources.'
plans:
- name: Loomly Plans Pricing
  plan_count: 4
  slug: loomly-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Loomly Rate Limits
  slug: loomly-rate-limits
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 55.0
    catalog_earned_first_party: 20.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 44.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loomly/refs/heads/main/screenshots/loomly-2026-06-20T184715.png
security:
- kind: authentication
  name: Loomly Authentication
  slug: loomly-authentication
  summary_line: oauth2/none · 0 schemes
- kind: domain-security
  name: Loomly Domain Security
  slug: loomly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Loomly Vulnerability Disclosure
  slug: loomly-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Loomly Trust Center
  slug: loomly-trust-center
  summary_line: trust center published
slug: loomly
tags:
- Social-Media
- Content Calendar
- Scheduling
- Approval Workflows
- Analytics
- Brand Management
- Publishing
- Community Management
- Marketing
- Social Media Management
website: https://www.loomly.com
---
