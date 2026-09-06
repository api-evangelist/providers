---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Urlbox Agentic Access
  operation_count: 5
  slug: urlbox-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.urlbox.com/v1
  baseurl_source: declared
  description: Create screenshot, PDF, and video renders.
  name: Urlbox Render API
  slug: urlbox-render-api
- baseURL: https://api.urlbox.com/v1
  baseurl_source: declared
  description: Stateless, cacheable HMAC-signed GET render URLs.
  name: Urlbox Render Links API
  slug: urlbox-render-links-api
- baseURL: https://api.urlbox.com/v1
  baseurl_source: declared
  description: Poll the status of asynchronous renders.
  name: Urlbox Status API
  slug: urlbox-status-api
- baseURL: https://api.urlbox.com/v1
  baseurl_source: declared
  description: Account render usage for the current billing period.
  name: Urlbox Usage API
  slug: urlbox-usage-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Urlbox Render API
  slug: open-urlbox-render-api
- collection_type: open
  name: Urlbox Render Render Links API
  slug: open-urlbox-render-links-api
- collection_type: open
  name: Urlbox Render Status API
  slug: open-urlbox-status-api
- collection_type: open
  name: Urlbox Render Usage API
  slug: open-urlbox-usage-api
- collection_type: open
  name: Urlbox API
  slug: open-urlbox
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/urlbox-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/urlbox-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/urlbox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/urlbox-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/urlbox-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/urlbox
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/urlbox
- group: company
  title: ''
  type: Website
  url: https://urlbox.com
- group: docs
  title: ''
  type: Documentation
  url: https://urlbox.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/urlbox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/urlbox-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/urlbox-finops.yml
created: '2026-06-20'
description: Urlbox is a website screenshot and rendering API that captures pixel-perfect screenshots, PDFs, and video (MP4/WebM) of any web page or raw HTML. Renders are requested synchronously, asynchronously (with polling or webhooks), or via signed HMAC render links, with hundreds of options for full-page capture, element selectors, PDF layout, ad/cookie-banner blocking, waiting, and S3 storage.
finops:
- name: Urlbox Finops
  service_category: Web and Application Services
  slug: urlbox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/urlbox.png
layout: provider
modified: '2026-06-20'
name: Urlbox
nav: Providers
network: true
overview: 'Urlbox publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Render API, Render Links API, Status API, and 1 more. Tagged areas include Screenshots, Rendering, PDF, Video, and Web Capture.


  Urlbox''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Urlbox Plans Pricing
  plan_count: 5
  slug: urlbox-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 6
  name: Urlbox Rate Limits
  slug: urlbox-rate-limits
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 56.3
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/urlbox/refs/heads/main/screenshots/urlbox-2026-06-20T200526.png
security:
- kind: authentication
  name: Urlbox Authentication
  slug: urlbox-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Urlbox Domain Security
  slug: urlbox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Urlbox Vulnerability Disclosure
  slug: urlbox-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Urlbox Trust Center
  slug: urlbox-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: urlbox
tags:
- Screenshots
- Rendering
- PDF
- Video
- Web Capture
website: https://urlbox.com
---
