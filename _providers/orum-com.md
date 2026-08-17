---
access_model:
  confidence: high
  label: Contact sales, 3-seat minimum, 500-dial free trial
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.orum.com/pricing
  trial: true
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 7
asyncapis:
- description: ''
  name: Orum Com Webhooks
  slug: orum-com-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/orum-com-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orum-com-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/orum-com-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orum-com-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/orum-com-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/orum-com-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.orum.com/product-updates
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/orum-com-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/orum-com-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/orum-com-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/orum-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/orum-com-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/orum-com-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/orum-com-packages.yml
- group: design
  title: ''
  type: Components
  url: components/orum-com-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orum-com-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orumhq
- group: docs
  title: ''
  type: Documentation
  url: https://support.orum.com/en-US/orum/directories
- group: start
  title: ''
  type: GettingStarted
  url: https://support.orum.com/en-US/orum/directories/4XGqC47h
- group: company
  title: ''
  type: Website
  url: https://www.orum.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.orum.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.orum.com/en-US/orum
- group: company
  title: ''
  type: Blog
  url: https://www.orum.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.orum.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.orum.com
- group: auth
  title: ''
  type: Compliance
  url: https://www.orum.com/platform/security
- group: auth
  title: ''
  type: Security
  url: https://www.orum.com/responsible_disclosure
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.orum.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orum.com/privacy
- group: other
  title: ''
  type: DataProcessingAddendum
  url: https://www.orum.com/data_processing_addendum
- group: other
  title: ''
  type: TechnicalAndOrganizationalMeasures
  url: https://www.orum.com/platform/security/technical-and-organizational-measures
- group: company
  title: ''
  type: Partners
  url: https://www.orum.com/partners
- group: other
  title: ''
  type: CaseStudies
  url: https://www.orum.com/customer-stories
- group: other
  title: ''
  type: Reports
  url: https://www.orum.com/reports-and-guides
- group: other
  title: ''
  type: Podcast
  url: https://www.orum.com/podcasts
- group: start
  title: ''
  type: Demo
  url: https://www.orum.com/request-demo
- group: company
  title: ''
  type: About
  url: https://www.orum.com/about
- group: company
  title: ''
  type: Careers
  url: https://www.orum.com/careers
created: '2026-08-04'
description: 'Orum is an AI-powered sales calling and performance platform, marketed as "The Calling Performance System for Sales Teams" and "the AI-powered Live Conversation Platform to supercharge sales activity, connect teams, and drive more revenue." Its products are a parallel Dialer (up to 5 lines on the Launch plan, 10 on Ascend), Salesfloor for virtual co-selling, a Coaching and Enablement suite, Orum AI trained on a claimed one billion-plus sales calls, and Scout, a set of AI data agents. It positions itself as purpose-built for maximizing live conversations and explicitly distinct from the dialers built into CRMs and sales-engagement platforms, integrating instead with Salesforce, HubSpot, Outreach, Salesloft, Gong Engage and Apollo. Pricing is two named plans, Launch and Ascend, both contact-sales with a three-seat minimum and no published figures, plus a free trial capped at 500 dials; AI Coaching and Webhooks are paid add-ons. Orum publishes NO request API — no OpenAPI, no API
  reference, no developer portal, no SDKs, no CLI, no MCP server, no llms.txt, and api./docs./developers.orum.com do not resolve. Its one machine-facing contract is an outbound webhook, and contrary to the first profiling pass it IS publicly documented: a help-center article publishes the single `call-disposition-added` event, the `{event, payload, test}` envelope, HMAC-SHA256 signature verification over an `x-webhook-signature` header, a 15-second ack timeout, an 8-attempt/30-minute exponential-backoff retry policy and three egress IPs. The article is simply unlinked from any directory and reachable only from the 2025-04-14 launch blog post. Orum also publishes a dated product-update feed, a status page, a trust portal, a responsible-disclosure policy, Auth0-backed SSO (SAML/OIDC/OAuth 2.0), a Chrome extension, and SOC 2 Type 2 plus ISO 27001:2022, 27017:2015, 27018:2019 and 27701:2019 attestations.'
image: https://cdn.sanity.io/images/w0eqmudi/production/2b821b473a58f9c3510eb28647c02e861d32727c-2000x1050.heif
layout: provider
modified: '2026-08-13'
name: Orum
nav: Providers
network: true
overview: 'Orum is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Sales, Sales Engagement, and Sales Dialer.


  The Orum catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Orum''s developer surface includes authentication, changelog, sandbox, documentation, getting-started guide, pricing, support, and 31 more developer resources.'
plans:
- name: Orum Com Plans Pricing
  plan_count: 2
  slug: orum-com-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 0
  name: Orum Com Rate Limits
  slug: orum-com-rate-limits
score:
  band: developing
  composite: 50.8
  delta: 31.6
  facets:
    commercial_clarity: 68.4
    contract_quality: 51.6
    developer_ergonomics: 43.5
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 55.3
  previous_composite: 19.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/orum-com/refs/heads/main/screenshots/orum-com-2026-08-07T190956.png
security:
- kind: authentication
  name: Orum Com Authentication
  slug: orum-com-authentication
  summary_line: saml/openIdConnect/oauth2/hmac-signature · 2 schemes
- kind: domain-security
  name: Orum Com Domain Security
  slug: orum-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Orum Com Vulnerability Disclosure
  slug: orum-com-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Orum Com Trust Center
  slug: orum-com-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, GDPR
slug: orum-com
tags:
- Company
- AI
- Sales
- Sales Engagement
- Sales Dialer
- Outbound Sales
- Sales Coaching
- Conversation Intelligence
- Telephony
- Revenue Operations
- Webhooks
- Parallel Dialing
- Sales Automation
website: https://www.orum.com/
---
