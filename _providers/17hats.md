---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/17hats-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.17hats.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/17hats-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/17hats-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/17hats-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.17hats.com/
- group: company
  title: ''
  type: About
  url: https://www.17hats.com/about
- group: docs
  title: ''
  type: Documentation
  url: https://help.17hats.com/
- group: operate
  title: ''
  type: Support
  url: https://help.17hats.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.17hats.com/en/articles/3110556-what-is-17hats
- group: company
  title: ''
  type: Blog
  url: https://blog.17hats.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/17hats
- group: commercial
  title: ''
  type: Pricing
  url: https://www.17hats.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.17hats.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://www.17hats.com/loginredirect
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.17hats.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.17hats.com/privacy-policy
coverage:
  checked: '2026-08-05'
  detail: 17hats' only programmatic surface is an account API key issued from Account Settings > Integrations that authenticates its Zapier connector (2 contact triggers, 4 contact actions) — there is no 17hats-hosted API reference, and api.17hats.com / developer.17hats.com only answer because *.17hats.com is a wildcard catch-all that returns the same app shell for a hostname that does not exist.
  evidence:
  - status: 200
    url: https://help.17hats.com/en/articles/2761371-zapier-integration
  - status: 200
    url: https://zapier.com/apps/17hats/integrations
  - status: 404
    url: https://www.17hats.com/openapi.json
  - status: 404
    url: https://www.17hats.com/.well-known/api-catalog
  - status: 302
    url: https://nonexistent-xyz123.17hats.com/
  reason: marketplace-only
  state: gated
created: '2026-08-05'
description: 17hats is an all-in-one CRM and business-management platform for service-based small businesses and solopreneurs, built around the idea that a one-person business wears seventeen hats. The platform combines lead capture, client pipelines, contact and project management, online scheduling, quotes, contracts and e-signature, questionnaires, invoicing and online payments, bookkeeping, email and SMS texting, and workflow automation into a single subscription product. 17hats states it serves more than 25,000 business owners across 100+ industries, including photographers, designers, coaches, planners and other service providers. 17hats does not publish a public developer program, API reference, or machine-readable specification; its only documented programmatic surface is an account-level API key issued from Account Settings > Integrations that authenticates its Zapier app, which exposes contact triggers and actions only.
image: https://cdn.prod.website-files.com/5fb453e0437ba3e5108c7389/63409b6c8c1d69fa92f3339b_17hats-SocialShare-2022-HomePage.png
layout: provider
modified: '2026-08-05'
name: 17hats
nav: Providers
network: true
overview: '17hats is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRM, Small Business, Invoicing, and Scheduling.


  17hats'' developer surface includes authentication, documentation, support, getting-started guide, engineering blog, pricing, signup flow, and 10 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 25.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 40.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/17hats/refs/heads/main/screenshots/17hats-2026-08-07T160647.png
security:
- kind: authentication
  name: 17Hats Authentication
  slug: 17hats-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 17Hats Domain Security
  slug: 17hats-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 17Hats Vulnerability Disclosure
  slug: 17hats-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: 17hats
tags:
- Company
- CRM
- Small Business
- Invoicing
- Scheduling
- Bookkeeping
- Workflow-Automation
- Contract Management
- Payments
- Software-as-a-Service
website: https://www.17hats.com/
---
