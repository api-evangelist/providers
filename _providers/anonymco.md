---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://www.mozilla.org/en-US/anonym/
  - https://www.mozilla.org/en-US/anonym/how-it-works/
  - https://anonymportal.com/app-data-manager
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anonymco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anonymco.com
- group: company
  title: ''
  type: About
  url: https://www.mozilla.org/en-US/anonym/about/
- group: company
  title: ''
  type: Blog
  url: https://www.mozilla.org/en-US/anonym/news/
- group: start
  title: ''
  type: Login
  url: https://anonymportal.com/app-data-manager
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mozilla.org/en-US/anonym/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mozilla.org/en-US/anonym/terms-and-conditions/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anonymco-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/anonymco-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/anonymco-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/anonymco-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anonymco-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/anonymco-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/anonymco-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anonymco-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Anonym's API reference lives inside the customer Transparency Portal at anonymportal.com — an Angular SPA whose server returns the same 650-byte index.html for every path including /docs — and the gRPC backend it fronts, anonymapis.com (named in the portal's own CSP and environment config), resolves to an Azure address that refuses anonymous TCP connections on 443.
  evidence:
  - status: 200
    url: https://anonymportal.com/docs
  - status: 0
    url: https://anonymapis.com/openapi.json
  - status: 200
    url: https://anonymco.com/openapi.json
  - status: 404
    url: https://www.mozilla.org/en-US/anonym/pricing/
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: 'Anonym is a privacy-preserving advertising technology platform now operated by Mozilla, sitting between advertisers and major publishers to measure and optimize ad performance without exposing individual user data. It uses confidential computing and privacy-enhancing techniques to run performance measurement and campaign optimization across platforms including TikTok, Snapchat, Pinterest, and Reddit, replacing costly custom data-sharing systems with a single privacy-compliant setup. Anonym was surfaced as a portfolio company of Norwest Venture Partners; its public surface is a marketing site (anonymco.com, which wildcard-redirects every path to mozilla.org/en-US/anonym/) and a customer login portal (anonymportal.com). No public API, developer portal, OpenAPI, GraphQL, AsyncAPI, MCP server, agent card, SDK or CLI is published. Contract discovery did identify the real backend: Anonym''s own Transparency Portal declares a gRPC API host at anonymapis.com in both its Content-Security-Policy
  connect-src and its published Angular environment config, but that host refuses anonymous connections, and the API reference Mozilla describes ("API Integrations", "Data Upload", a Knowledge Base) sits behind the customer login.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anonymco.png
layout: provider
modified: '2026-08-12'
name: Anonym
nav: Providers
network: true
overview: 'Anonym is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Advertising Technology, Privacy, and Ad Measurement.


  Anonym''s developer surface includes engineering blog and 14 more developer resources.'
plans:
- name: Anonymco Plans Pricing
  plan_count: 0
  slug: anonymco-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 0
  name: Anonymco Rate Limits
  slug: anonymco-rate-limits
score:
  band: emerging
  composite: 17.5
  delta: 5.2
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 12.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/anonymco/refs/heads/main/screenshots/anonymco-2026-07-25T200307.png
security:
- kind: domain-security
  name: Anonymco Domain Security
  slug: anonymco-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Anonymco Vulnerability Disclosure
  slug: anonymco-vulnerability-disclosure
  summary_line: disclosure policy published
slug: anonymco
tags:
- Company
- Advertising
- Advertising Technology
- Privacy
- Ad Measurement
- Confidential Computing
- Mozilla
- Attribution
- Differential Privacy
- Trusted Execution Environment
- Marketing
website: https://anonymco.com
---
