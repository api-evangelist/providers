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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Data-as-a-Service access to Onclusive's media intelligence corpus — 28M+ daily media content items across print, online, broadcast and social media, 300K+ verified journalist contacts, and 250K+ globa
  name: Onclusive Media API
  slug: onclusive-media-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://onclusive.com
- group: company
  title: ''
  type: Blog
  url: https://onclusive.com/resources/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onclusive.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onclusive.com/legal/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://onclusive.com/our-company/contact-us/
- group: auth
  title: ''
  type: TrustCenter
  url: security/airpr-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.onclusive.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airpr-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.onclusive.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AirPR
- group: auth
  title: ''
  type: Authentication
  url: authentication/airpr-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/airpr-scopes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/airpr-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/airpr-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/airpr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/airpr-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/airpr-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Onclusive markets a Media API but publishes no reference for it — the product page's only calls to action are "Arrange a Demo" and a contact form — and the AWS API Gateway Developer Portal at developer.onclusive.com that would carry the catalog renders an empty React shell to anonymous visitors, with its content bundle returning 403 AccessDenied from S3 and its backing REST API returning 403 "Missing Authentication Token" behind an Amazon Cognito login.
  evidence:
  - status: 200
    url: https://onclusive.com/what-we-do/monitoring/media-api/
  - status: 403
    url: https://rcbv8po81k.execute-api.us-east-1.amazonaws.com/prod/catalog
  - status: 403
    url: https://developer.onclusive.com/custom-content/content-fragments/home/index.md
  - status: 404
    url: https://onclusive.com/openapi.json
  - status: 404
    url: https://airpr.com/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: AirPR is a public relations analytics and media measurement company whose software helped communications teams quantify the business impact of earned media, tie coverage to web traffic and conversions, and benchmark share of voice against competitors. AirPR is now part of Onclusive, the media intelligence platform that monitors and enriches conversations across 3M+ online sources, 70K+ print outlets, 6K+ broadcast channels, and 25+ social platforms for PR, communications, and marketing professionals. It was surfaced as a portfolio company of 500 Global and added to the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airpr.png
layout: provider
modified: '2026-08-13'
name: AirPR
nav: Providers
network: true
overview: 'AirPR publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Public Relations, Media Intelligence, Media Monitoring, and Analytics.


  AirPR''s developer surface includes engineering blog, support, authentication, and 14 more developer resources.'
plans:
- name: Airpr Plans Pricing
  plan_count: 0
  slug: airpr-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Airpr Rate Limits
  slug: airpr-rate-limits
scopes:
- name: Airpr Scopes
  scope_count: 4
  slug: airpr-scopes
  summary_line: 4 scopes · authorizationCode/implicit
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 22.3
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airpr/refs/heads/main/screenshots/airpr-2026-07-25T195431.png
security:
- kind: authentication
  name: Airpr Authentication
  slug: airpr-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Airpr Domain Security
  slug: airpr-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Airpr Trust Center
  slug: airpr-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001, Cyber Essentials Plus, GDPR, CCPA, PDPA, Standard Contractual Clauses (SCC), EcoVadis (Committed, Oct 2025)
slug: airpr
tags:
- Company
- Public Relations
- Media Intelligence
- Media Monitoring
- Analytics
- Communications
- Marketing
- PR Measurement
- Onclusive
website: https://onclusive.com
---
