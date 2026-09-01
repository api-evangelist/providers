---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 33.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: REST API for managing email campaigns, mailing lists, subscribers, templates, and analytics in Zoho Campaigns. Supports campaign creation, scheduling, sending, cloning, and reporting as well as contac
  name: Zoho Campaigns API
  slug: zoho-campaigns-api
- description: Resource-oriented JSON REST API for sending email at volume from Zoho Campaigns. Covers transmissions (create, schedule, reschedule, cancel, fetch), stored HTML/text templates, recipient lists, the su
  name: Zoho Campaigns Email API
  slug: zoho-campaigns-email-api
artifact_total: 11
asyncapis:
- description: ''
  name: Zoho Campaigns Email Api Webhooks
  slug: zoho-campaigns-email-api-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/campaigns/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.zoho.com/campaigns/help/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/campaigns/help/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://www.zoho.com/campaigns/help/developers/campaign-management.html
- group: start
  title: ''
  type: Quickstart
  url: https://www.zoho.com/campaigns/help/developers/access-token.html
- group: operate
  title: ''
  type: Support
  url: https://help.zoho.com/portal/en/community/zoho-campaigns
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zoho
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/zoho-campaigns/
- group: other
  title: ''
  type: X
  url: https://x.com/zohocampaigns
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/blog/campaigns/
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/campaigns/pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://www.zoho.com/campaigns/signup.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zoho.com/campaigns/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zoho.com/privacy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zoho.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.zoho.com/campaigns/whats-new.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/zoho-emailapi-b1/zoho-campaigns-email-api/collection/lhb7bxz/email-api-collection
- group: auth
  title: ''
  type: Security
  url: https://bugbounty.zohocorp.com/bb/info
- group: auth
  title: ''
  type: Compliance
  url: https://www.zoho.com/compliance.html
- group: commercial
  title: ''
  type: Plans
  url: plans/zoho-campaigns-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zoho-campaigns-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zoho-campaigns-finops.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zoho-campaigns-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zoho-campaigns-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zoho-campaigns-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zoho-campaigns-email-api-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zoho-campaigns-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zoho-campaigns-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zoho-campaigns-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zoho-campaigns-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zoho-campaigns-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/zoho-campaigns-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zoho-campaigns-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zoho-campaigns-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/zoho-campaigns-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-campaigns-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zoho-campaigns-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-campaigns-domain-security.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/zoho-campaigns.json
created: '2026-06-13'
description: Zoho Campaigns is Zoho Corporation's email marketing platform, and it exposes two distinct public API surfaces. The Zoho Campaigns API v1.1 is an RPC-over-HTTP interface for campaigns, mailing lists, contacts, segments, custom fields, merge tags, coupons, topics and automation workflows, authenticated with OAuth 2.0 against Zoho Accounts and returning JSON or XML selected with a resfmt query parameter. The Zoho Campaigns Email API v2 is a separate resource-oriented JSON REST API for transactional and bulk sending — transmissions, stored templates, recipient lists, suppression lists, sending and tracking domains, users, licensing, delivery reports and event webhooks — authenticated with an API key. Zoho publishes no OpenAPI for either surface; the machine-readable contract it does publish is a first-party Postman collection for the Email API.
finops:
- name: Zoho Campaigns Finops
  service_category: ''
  slug: zoho-campaigns-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-campaigns.png
layout: provider
modified: '2026-08-13'
name: Zoho Campaigns
nav: Providers
network: true
overview: 'Zoho Campaigns publishes 1 API on the [APIs.io](https://apis.io/) network: Email API. Tagged areas include Email Marketing, Campaigns, Mailing Lists, Subscribers, and Email Templates.


  The Zoho Campaigns catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zoho Campaigns'' developer surface includes documentation, API reference, quickstart, support, engineering blog, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Zoho Campaigns Plans Pricing
  plan_count: 5
  slug: zoho-campaigns-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Zoho Campaigns Rate Limits
  slug: zoho-campaigns-rate-limits
scopes:
- name: Zoho Campaigns Scopes
  scope_count: 15
  slug: zoho-campaigns-scopes
  summary_line: 15 scopes · authorizationCode
score:
  band: exemplar
  composite: 68.7
  coverage:
    artifact_dirs: 21
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 57.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 84.2
  previous_composite: 68.7
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-campaigns/refs/heads/main/screenshots/zoho-campaigns-2026-06-20T201934.png
security:
- kind: authentication
  name: Zoho Campaigns Authentication
  slug: zoho-campaigns-authentication
  summary_line: oauth2/apiKey · 3 schemes
- kind: domain-security
  name: Zoho Campaigns Domain Security
  slug: zoho-campaigns-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Campaigns Vulnerability Disclosure
  slug: zoho-campaigns-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Zoho Campaigns Trust Center
  slug: zoho-campaigns-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, ISO/IEC 20000-1, ISO 9001, ISO 22301, SOC 1 Type 2 (SSAE 18 / ISAE 3402), SOC 2 Type 2, SOC 2 + HIPAA Type 2, PCI DSS (SAQ-D), CSA STAR Self-Assessment, Cyber Essentials Plus, TX-RAMP, ENS (Esquema Nacional de Seguridad), NCA Class B (Saudi Arabia), NHS DSPT v8, GoBD, 21 CFR Part 11, EudraLex Annex 11, WCAG 2.2 AA
slug: zoho-campaigns
tags:
- Email Marketing
- Campaigns
- Mailing Lists
- Subscribers
- Email Templates
- A/B Testing
- Campaign Analytics
- Marketing Automation
- Transactional Email
- Webhook
website: https://www.zoho.com/campaigns/
---
