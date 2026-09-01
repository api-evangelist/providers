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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instil-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.instil.io/
- group: company
  title: ''
  type: Blog
  url: https://blog.instil.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.instil.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.instil.io/terms-conditions
- group: start
  title: ''
  type: SignUp
  url: https://www.instil.io/get-demo-crm
- group: start
  title: ''
  type: Login
  url: https://app.instil.io/
- group: company
  title: ''
  type: About
  url: https://www.instil.io/about-us
- group: company
  title: ''
  type: BlogFeeds
  url: https://blog.instil.io/rss.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/weareinstil/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/weareinstil
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/weareinstil
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/instil-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/instil-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/instil-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/instil-lifecycle.yml
coverage:
  checked: '2026-08-14'
  detail: 'Instil ships only an end-user nonprofit CRM: www.instil.io has no /developers, /api, /integrations or /pricing page and no such URL in its sitemap, and the one API host it operates, api.instil.io, is the private AWS API Gateway backend for app.instil.io that answers 404 {"message":"Not Found"} on every OpenAPI, GraphQL, MCP and .well-known discovery path.'
  evidence:
  - status: 404
    url: https://api.instil.io/openapi.json
  - status: 404
    url: https://api.instil.io/graphql
  - status: 404
    url: https://www.instil.io/developers
  - status: 404
    url: https://www.instil.io/pricing
  - status: 404
    url: https://www.instil.io/.well-known/agent-card.json
  - status: 0
    url: https://docs.instil.io/
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Instil is a purpose-built fundraising CRM and revenue-intelligence platform for nonprofit organizations, built for major-gifts and development teams. It manages the full donor lifecycle across major gifts, capital campaigns, planned giving, grant tracking, and moves management, and layers AI on top with One-Click Briefings that assemble a constituent's giving history and contact record on demand and Voice AI Logging that transcribes calls and writes interactions back to Instil or Salesforce. Instil connects to the nonprofit tech stack through Salesforce, Stripe, Classy, Mailchimp, Constant Contact, Eventbrite, Google, Outlook, and Zapier. It is backed by Threshold Ventures. No public developer API, documentation, or SDKs are published at this time; integrations are delivered through packaged connectors and Zapier.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instil.png
layout: provider
modified: '2026-08-14'
name: Instil
nav: Providers
network: true
overview: 'Instil is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Non-Profit, CRM, and Fundraising.


  Instil''s developer surface includes engineering blog, signup flow, and 14 more developer resources.'
plans:
- name: Instil Plans Pricing
  plan_count: 0
  slug: instil-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instil/refs/heads/main/screenshots/instil-2026-07-25T222615.png
security:
- kind: domain-security
  name: Instil Domain Security
  slug: instil-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: instil
tags:
- Company
- Software-as-a-Service
- Non-Profit
- CRM
- Fundraising
- Donor Management
- Philanthropy
- Revenue Intelligence
website: https://www.instil.io/
---
