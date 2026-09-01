---
access_model:
  confidence: high
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.kompyte.com/plans
  - https://www.kompyte.com/register
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://kompyte.com
- group: company
  title: ''
  type: Blog
  url: https://www.kompyte.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.kompyte.com/blog/rss.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kompyte.com/plans
- group: start
  title: ''
  type: SignUp
  url: https://www.kompyte.com/register
- group: start
  title: ''
  type: Login
  url: https://phi.kompyte.pro/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kompyte.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kompyte.com/privacy-policy
- group: other
  title: ''
  type: CaseStudies
  url: https://www.kompyte.com/case-studies/
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.kompyte.pro/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.kompyte.pro/en/
- group: operate
  title: ''
  type: SLA
  url: https://www.kompyte.com/sla/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kompyte-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kompyte-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kompyte-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kompyte-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kompyte-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kompyte-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/kompyte-components.yml
coverage:
  checked: '2026-08-13'
  detail: Kompyte ships only an end-user SaaS product — its sole programmatic surface is the session-gated application backend at phi.kompyte.pro/api/, which returns HTTP 403 {"error":"LOGIN REQUIRED"} for every path including /api/openapi.json, and no plan tier, help-center article or sitemap URL offers API access to buy or documentation to read.
  evidence:
  - status: 403
    url: https://phi.kompyte.pro/api/openapi.json
  - status: 404
    url: https://www.kompyte.com/developers
  - status: 404
    url: https://phi.kompyte.pro/openapi.json
  - status: 404
    url: https://www.kompyte.com/.well-known/agent-card.json
  - status: 404
    url: https://github.com/kompyte
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=kompyte
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Kompyte is a competitive intelligence and sales enablement platform sold as a Semrush product, and Adobe-owned since Adobe completed its acquisition of Semrush on 28 April 2026. It automates the tracking of competitors across their websites, pricing pages, product releases, content, ads, social channels and review sites. Captured changes are scored and summarized into AI-generated daily digests and continuously updated sales battlecards, so revenue teams can see what rivals changed and how to respond in live deals. Kompyte also supports win/loss capture and delivers intelligence into the tools sellers already use through CRM, chat, sales-enablement and file-storage integrations including Salesforce, HubSpot, Slack, Microsoft Teams, Highspot, Showpad, Guru, Gong, Trello, Google Drive and Microsoft OneDrive, and lets teams embed a hosted battlecard view into those tools with an iframe. Kompyte sells three contact-sales tiers with published product quotas and commits to a 99.9%
  uptime SLA, but publishes no public developer API, developer portal, API documentation, SDK, webhook catalog or agent surface; the application backend at phi.kompyte.pro/api/ answers HTTP 403 "LOGIN REQUIRED" to every anonymous request.
image: https://www.kompyte.com/hubfs/Kompyte_by-Semrush_Logo-Orange%26Black.png
layout: provider
modified: '2026-08-13'
name: Kompyte
nav: Providers
network: true
overview: 'Kompyte is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Competitive Intelligence, Sales Enablement, Market Intelligence, and Battlecards.


  Kompyte''s developer surface includes engineering blog, pricing, signup flow, support, and 15 more developer resources.'
plans:
- name: Kompyte Plans Pricing
  plan_count: 3
  slug: kompyte-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Kompyte Rate Limits
  slug: kompyte-rate-limits
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 24.6
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kompyte/refs/heads/main/screenshots/kompyte-2026-07-25T224143.png
security:
- kind: domain-security
  name: Kompyte Domain Security
  slug: kompyte-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kompyte
tags:
- Company
- Competitive Intelligence
- Sales Enablement
- Market Intelligence
- Battlecards
- Win-Loss Analysis
- Software-as-a-Service
- Marketing
website: https://kompyte.com
---
