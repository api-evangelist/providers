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
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.6
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The Moosend REST API (v3) enables programmatic access to email marketing and automation capabilities including managing email lists, subscribers, campaigns, segments, and transactional emails. Authent
  name: Moosend API
  slug: moosend-api
artifact_total: 11
collections:
- collection_type: open
  name: Moosend API
  slug: open-moosend
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/moosend-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/moosend-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moosend-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://moosend.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moosend.com/api-documentation?lang=en_US
- group: start
  title: ''
  type: DeveloperPortal
  url: https://moosend.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://moosendapp.docs.apiary.io/
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.moosend.com/user-guide?lang=en_US
- group: operate
  title: ''
  type: Support
  url: https://moosend.com/contact-us/support/
- group: start
  title: ''
  type: SignUp
  url: https://identity.moosend.com/register/
- group: start
  title: ''
  type: Login
  url: https://app.moosend.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moosend.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moosend.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moosend
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moosend
- group: company
  title: ''
  type: Blog
  url: https://moosend.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://moosend.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://moosend.statuspage.io
- group: other
  title: ''
  type: X
  url: https://x.com/moosend
- group: commercial
  title: ''
  type: Plans
  url: plans/moosend-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/moosend-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/moosend-finops.yml
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/moosend-context.jsonld
- group: build
  title: ''
  type: Packages
  url: packages/moosend-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/moosend-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moosend-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moosend-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moosend-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moosend-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moosend-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moosend-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/moosend-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moosend-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://moosend.com/trust/compliance/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/moosend-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://moosend.com/privacy-policy/disclosure/
- group: other
  title: ''
  type: Overlay
  url: overlays/moosend-openapi-overlay.yaml
created: '2026-06-13'
description: Moosend is an email marketing and automation platform with a REST API for managing mailing lists, campaigns, subscribers, automations, and tracking email performance metrics. The API uses HTTPS with API key authentication and provides programmatic access to email lists, subscriber management, campaign creation and scheduling, audience segmentation, transactional emails, and real-time reporting.
finops:
- name: Moosend Finops
  service_category: ''
  slug: moosend-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moosend.png
jsonld:
- class_count: 20
  name: Moosend Context
  property_count: 0
  slug: moosend-context
layout: provider
mcp_servers:
- description: ''
  name: moosend-mcp.yml
  slug: moosend-mcpyml
modified: '2026-08-13'
name: Moosend
nav: Providers
network: true
overview: 'Moosend publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email Marketing, Marketing Automation, Campaigns, Mailing Lists, and Subscribers.


  The Moosend catalog on APIs.io includes 1 JSON-LD context.


  Moosend''s developer surface includes authentication, documentation, API reference, support, signup flow, engineering blog, pricing, and 32 more developer resources.'
plans:
- name: Moosend Plans Pricing
  plan_count: 5
  slug: moosend-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 10
  name: Moosend Rate Limits
  slug: moosend-rate-limits
score:
  band: strong
  composite: 64.1
  delta: 27.8
  facets:
    commercial_clarity: 100.0
    contract_quality: 62.7
    developer_ergonomics: 63.0
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 63.2
  previous_composite: 36.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 50.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/moosend/refs/heads/main/screenshots/moosend-2026-06-20T185801.png
security:
- kind: authentication
  name: Moosend Authentication
  slug: moosend-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Moosend Domain Security
  slug: moosend-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Moosend Vulnerability Disclosure
  slug: moosend-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Moosend Trust Center
  slug: moosend-trust-center
  summary_line: ISO 27001, Certified Senders Alliance (CSA), GDPR, NIST SP 800-171, PCI DSS
slug: moosend
tags:
- Email Marketing
- Marketing Automation
- Campaigns
- Mailing Lists
- Subscribers
- Transactional Email
- SMTP
- Segmentation
- Analytics
- Email
- Newsletters
- Landing Pages
- Website Tracking
- Marketing
website: https://moosend.com/
---
