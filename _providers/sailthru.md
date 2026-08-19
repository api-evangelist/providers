---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.5
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The core Sailthru HTTPS API. All requests are GET, POST or DELETE calls to https://api.sailthru.com/<endpointName>, authenticated with api_key, an MD5 sig over the sorted parameter values, and a forma
  name: Sailthru API
  slug: sailthru-api
- description: The client-side Sailthru JavaScript tag (spm.v1.min.js, served from ak.sail-horizon.com) used for on-site behavior tracking, content-library sync, userSignUp/userSignUpConfirm calls and on-site person
  name: Sailthru JavaScript API (Personalization Engine)
  slug: sailthru-js-api
artifact_total: 9
asyncapis:
- description: ''
  name: Sailthru Postbacks Webhooks
  slug: sailthru-postbacks-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sailthru-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sailthru-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sailthru-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/engagements/cheetah-vdp
- group: auth
  title: ''
  type: Compliance
  url: https://trust.zetaglobal.com/?product=sailthru
- group: company
  title: ''
  type: Website
  url: https://zetaglobal.com/sailthru/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://products.zetaglobal.com/sailthru/Content/developers/overview.html
- group: docs
  title: ''
  type: Documentation
  url: https://products.zetaglobal.com/sailthru/Content/LandingPage.htm
- group: docs
  title: ''
  type: APIReference
  url: https://products.zetaglobal.com/sailthru/Content/developers/api-basics/introduction.html
- group: start
  title: ''
  type: GettingStarted
  url: https://products.zetaglobal.com/sailthru/Content/developers/api-basics/technical.html
- group: operate
  title: ''
  type: Support
  url: https://zetaglobal.com/about/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://zetaglobal.com/resource-center/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sailthru
- group: start
  title: ''
  type: SignUp
  url: https://my.sailthru.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zetaglobal.com/former-marigold-now-zeta-services-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zetaglobal.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://products.zetaglobal.com/sailthru/Content/ReleaseNotes/releasenotes-2026.htm
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sailthru-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/sailthru-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sailthru-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sailthru-cli.yml
- group: design
  title: ''
  type: Components
  url: components/sailthru-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sailthru-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sailthru-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sailthru-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sailthru-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sailthru-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sailthru-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sailthru-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sailthru-postbacks-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sailthru-llms.txt
created: '2026-08-12'
description: Sailthru is a cross-channel relationship-marketing and personalization platform built for media, publishing, retail and e-commerce brands, unifying email, SMS, mobile push, in-app and on-site messaging around a single customer profile with predictive segmentation and 1:1 content personalization. Founded in New York in 2008, it was acquired by CM Group (later Marigold) in 2018 and became part of Zeta Global in November 2025 when Zeta bought Marigold's enterprise software business; the product is now documented as Sailthru by Zeta. Its public HTTPS API lives at api.sailthru.com and covers users, lists, content, templates, blasts (campaigns), transactional sends, triggers, purchases, events, includes, ad plans and stats, authenticated with an api_key plus an MD5 signature computed over the request parameters. It is complemented by the Zephyr template language, a JavaScript on-site personalization tag, mobile SDKs, and API postbacks (webhooks) for opt-out, hardbounce, verify and
  profile-update events.
image: https://zetaglobal.com/wp-content/uploads/2025/12/ZetaMarigold-Landing-page-images-09-1.png
layout: provider
modified: '2026-08-12'
name: Sailthru
nav: Providers
network: true
overview: 'Sailthru publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email Marketing, Marketing Automation, Personalization, and Customer Data Platform.


  The Sailthru catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sailthru''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 24 more developer resources.'
plans:
- name: Sailthru Plans Pricing
  plan_count: 0
  slug: sailthru-plans-pricing
random_paper: 131
rate_limits:
- limit_count: 5
  name: Sailthru Rate Limits
  slug: sailthru-rate-limits
score:
  band: strong
  composite: 55.8
  delta: 2.2
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 45.1
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 68.4
  previous_composite: 53.6
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 59.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sailthru/refs/heads/main/screenshots/sailthru-2026-08-17T081714.png
security:
- kind: authentication
  name: Sailthru Authentication
  slug: sailthru-authentication
  summary_line: apiKey/requestSignature · 3 schemes
- kind: domain-security
  name: Sailthru Domain Security
  slug: sailthru-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sailthru Vulnerability Disclosure
  slug: sailthru-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt
- kind: trust-center
  name: Sailthru Trust Center
  slug: sailthru-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 27018:2019, ISO/IEC 27701, HDS, Privacy Mark, SOX, GDPR, CCPA, HITRUST, SIG Core, CAIQ, SOC 1 Type 2
slug: sailthru
tags:
- Company
- Email Marketing
- Marketing Automation
- Personalization
- Customer Data Platform
- Transactional Email
- SMS
- Push Notifications
- Retail
- Media and Publishing
website: https://zetaglobal.com/sailthru/
---
