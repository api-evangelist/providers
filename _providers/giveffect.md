---
access_model:
  confidence: high
  label: Enterprise (free trial) · Requires approval
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://www.giveffect.com/pricing
  - https://www.giveffect.com/faq
  trial: true
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 2.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Giveffect's "open API" is available on the enterprise Ultimate+ plan and provides programmatic access to platform data (donors, donations, volunteers, campaigns, and events). It is explicitly carved o
  name: Giveffect API
  slug: giveffect-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/giveffect-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/giveffect-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/giveffect-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/giveffect-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/giveffect-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/giveffect-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/giveffect-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/giveffect-lifecycle.yml
- group: company
  title: ''
  type: Blog
  url: https://www.giveffect.com/nonprofit-resource-center
- group: company
  title: ''
  type: BlogRSS
  url: https://www.giveffect.com/nonprofit-resource-center/feed/
- group: operate
  title: ''
  type: FAQ
  url: https://www.giveffect.com/faq
- group: company
  title: ''
  type: Website
  url: https://www.giveffect.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.giveffect.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.giveffect.com
- group: start
  title: ''
  type: Login
  url: https://app.giveffect.com
- group: operate
  title: ''
  type: Support
  url: https://www.giveffect.com/schedule-a-call
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.giveffect.com/terms-of-use-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.giveffect.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.giveffect.com/security
coverage:
  checked: '2026-08-13'
  detail: Giveffect's API is a paid feature of the Ultimate+ tier only — the Ultimate pricing card reads "All system features (excludes open API)" — and https://www.giveffect.com/api 302s to the customer sign-in page, so the reference requires an active subscription; api.giveffect.com is live and answers JSON but returns its 404 envelope for /openapi.json, /swagger.json, /api-docs, /graphql, /mcp and every /.well-known/ path.
  evidence:
  - status: 302
    url: https://www.giveffect.com/api
  - status: 404
    url: https://api.giveffect.com/openapi.json
  - status: 200
    url: https://api.giveffect.com/
  - status: 200
    url: https://www.giveffect.com/pricing
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: 'Giveffect is an all-in-one nonprofit management platform that combines ten seamlessly connected systems into a single suite for charitable organizations: constituent relationship management (CRM), online fundraising and donation processing, peer-to-peer and event fundraising, volunteer management, membership management, email and marketing communications, wealth screening and major-gifts tools, website building, and smart automation and workflows. Giveffect exposes an optional "open API" on its enterprise (Ultimate+) tier for integrating the platform''s donor, donation, volunteer, and campaign data with external systems, and ships prebuilt integrations with QuickBooks Online, DonorSearch, Double the Donation, Zoom, The Giving Block, and Ez Scan. The company was surfaced as a Y Combinator portfolio company and enriched into the API Evangelist network.'
image: https://www.giveffect.com/assets/og_gesplash.jpg
layout: provider
modified: '2026-08-13'
name: Giveffect
nav: Providers
network: true
overview: 'Giveffect publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Non-Profit, Fundraising, CRM, and Donations.


  Giveffect''s developer surface includes changelog, engineering blog, FAQ, pricing, signup flow, support, and 13 more developer resources.'
plans:
- name: Giveffect Plans Pricing
  plan_count: 3
  slug: giveffect-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Giveffect Rate Limits
  slug: giveffect-rate-limits
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 29.3
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/giveffect/refs/heads/main/screenshots/giveffect-2026-07-25T215843.png
security:
- kind: authentication
  name: Giveffect Authentication
  slug: giveffect-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Giveffect Domain Security
  slug: giveffect-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Giveffect Vulnerability Disclosure
  slug: giveffect-vulnerability-disclosure
  summary_line: Hackerone
slug: giveffect
tags:
- Company
- Non-Profit
- Fundraising
- CRM
- Donations
- Volunteer Management
- Marketing Automation
- Software-as-a-Service
website: https://www.giveffect.com
---
