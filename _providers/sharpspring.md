---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The SharpSpring (Constant Contact Lead Gen & CRM) Open API — a single HTTPS POST endpoint that accepts a JSON envelope of method, params and id, very similar to JSON-RPC. Version v1 resolves timestamp
  name: SharpSpring Open API
  slug: open-api
artifact_total: 7
asyncapis:
- description: ''
  name: Sharpspring Postbacks Webhooks
  slug: sharpspring-postbacks-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sharpspring-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sharpspring.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://knowledgebase.constantcontact.com/lead-gen-crm/articles/KnowledgeBase/50374-Understanding-Lead-Gen--CRM-Open-API-Overview?lang=en_US
- group: docs
  title: ''
  type: Documentation
  url: https://knowledgebase.constantcontact.com/lead-gen-crm/articles/KnowledgeBase/50374-Understanding-Lead-Gen--CRM-Open-API-Overview?lang=en_US
- group: docs
  title: ''
  type: APIReference
  url: https://knowledgebase.constantcontact.com/lead-gen-crm/articles/KnowledgeBase/50564-Understanding-Lead-Gen--CRM-Open-API-Methods?lang=en_US
- group: start
  title: ''
  type: GettingStarted
  url: https://knowledgebase.constantcontact.com/lead-gen-crm/articles/KnowledgeBase/50404-Understanding-Lead-Gen-CRM-Open-API-Example-Code?lang=en_US
- group: operate
  title: ''
  type: Support
  url: https://sharpspring.com/customer-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://knowledgebase.constantcontact.com/lead-gen-crm?lang=en_US
- group: company
  title: ''
  type: Blog
  url: https://www.constantcontact.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sharpspring
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sharpspring.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://sharpspring.com/agency-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.constantcontact.com/signup/lead-gen-crm/demo
- group: start
  title: ''
  type: Login
  url: https://api.sharpspring.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.constantcontact.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.constantcontact.com/legal/privacy-notice
- group: auth
  title: ''
  type: Security
  url: https://www.constantcontact.com/disclosure
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sharpspring-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/sharpspring-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sharpspring-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/sharpspring-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sharpspring-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sharpspring-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sharpspring-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sharpspring-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sharpspring-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sharpspring-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sharpspring-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/sharpspring-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sharpspring-postbacks-webhooks.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sharpspring-vulnerability-disclosure.yml
created: '2026-08-12'
description: SharpSpring — now sold as Constant Contact Lead Gen & CRM after Constant Contact acquired the company in 2021 — is a marketing automation and CRM platform for small businesses and digital marketing agencies, covering email marketing, landing pages, forms, visual automation workflows, social management, campaign tracking, lead scoring and a built-in sales CRM. Its developer surface is the SharpSpring Open API, a JSON-RPC-style HTTPS POST endpoint at api.sharpspring.com/pubapi/ that exposes roughly 120 published methods over leads, accounts, opportunities, campaigns, deal stages, emails, email jobs, lists and list members, fields, folders, notes, products and tasks. Authentication is a static account ID plus secret key generated in the application; there is no OAuth, no scopes and no OpenAPI description. Event delivery is handled by workflow and form Postback URLs rather than a webhook subscription API.
image: https://sharpspring.com/wp-content/uploads/2021/10/SharpSpring-From-CTCT-Logo-RGB-Color-1200.png
layout: provider
modified: '2026-08-12'
name: SharpSpring
nav: Providers
network: true
overview: 'SharpSpring publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Marketing Automation, CRM, and Email Marketing.


  The SharpSpring catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SharpSpring''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Sharpspring Plans Pricing
  plan_count: 0
  slug: sharpspring-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Sharpspring Rate Limits
  slug: sharpspring-rate-limits
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 57.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 68.4
  previous_composite: 47.0
  provenance:
    conformance: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sharpspring/refs/heads/main/screenshots/sharpspring-2026-08-17T081825.png
security:
- kind: authentication
  name: Sharpspring Authentication
  slug: sharpspring-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Sharpspring Domain Security
  slug: sharpspring-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sharpspring Vulnerability Disclosure
  slug: sharpspring-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: sharpspring
tags:
- Company
- Marketing
- Marketing Automation
- CRM
- Email Marketing
- Sales
- Leads
- Campaigns
- Automation
- Software-as-a-Service
website: https://sharpspring.com/
---
