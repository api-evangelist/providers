---
agent_readiness:
  band: agent-aware
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
  score: 19.8
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 5
asyncapis:
- description: ''
  name: Supply Wisdom Webhooks
  slug: supply-wisdom-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/supply-wisdom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.supplywisdom.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.supplywisdom.com/product
- group: operate
  title: ''
  type: Support
  url: https://www.supplywisdom.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.supplywisdom.com/resources
- group: start
  title: ''
  type: Login
  url: https://app.supplywisdom.com/dashboard
- group: start
  title: ''
  type: SignUp
  url: https://www.supplywisdom.com/book-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.supplywisdom.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.supplywisdom.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://supplywisdom.trust.site
- group: auth
  title: ''
  type: Compliance
  url: https://supplywisdom.trust.site
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/supplywisdom
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/supply-wisdom-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/supply-wisdom-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/supply-wisdom-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/supply-wisdom-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/supply-wisdom-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/supply-wisdom-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/supply-wisdom-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/supply-wisdom-llms.txt
coverage:
  checked: '2026-08-29'
  detail: Supply Wisdom's entire platform is the tenant app at app.supplywisdom.com — the 222-URL sitemap on www.supplywisdom.com contains no developer, API or documentation page, docs.supplywisdom.com does not resolve, and the product page advertises webhook notifications and "fully integrated into your GRC solution" while publishing no reference, payload schema or spec for either, so the entire integration surface is reachable only from inside a paid tenant.
  evidence:
  - status: 200
    url: https://www.supplywisdom.com/product
  - status: 200
    url: https://www.supplywisdom.com/sitemap.xml
  - status: 200
    url: https://api.supplywisdom.com/openapi.json
  - status: 200
    url: https://api.supplywisdom.com/this-path-should-not-exist-xyz123
  - status: 404
    url: https://www.supplywisdom.com/openapi.json
  - status: 200
    url: https://app.supplywisdom.com/dashboard
  reason: customer-only-docs
  state: gated
created: '2026-08-29'
description: Supply Wisdom is a third-party and location risk intelligence SaaS platform that continuously monitors suppliers, vendors and operating locations across financial, cyber, compliance, ESG, operational, nth-party and geopolitical risk domains. The product is sold in three subscription shapes — Real-time Alerts, Comprehensive Intelligence (in-depth reports across 350+ risk metrics with 12-month look-back snapshots) and Continuous Monitoring (real-time coverage with AI-driven auto actions, configurable dashboards, and email, Slack and webhook notifications) — and is positioned to feed an organisation's existing GRC stack rather than replace it, with named partnerships into Archer, Aravo, Certa, IBM OpenPages, OneTrust, Black Kite, Fusion Risk Management and SecurityScorecard. The platform itself is a tenant application at app.supplywisdom.com; no public developer portal, API reference or machine-readable contract is published on any Supply Wisdom host.
image: https://framerusercontent.com/images/7wsvue431VgrTWr0Lbz2EG1OsE.png
layout: provider
modified: '2026-08-29'
name: Supply Wisdom
nav: Providers
network: true
overview: 'Supply Wisdom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Risk, Third-Party Risk Management, Supply Chain, and Governance Risk and Compliance.


  The Supply Wisdom catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Supply Wisdom''s developer surface includes documentation, support, engineering blog, signup flow, and 16 more developer resources.'
plans:
- name: Supply Wisdom Plans Pricing
  plan_count: 3
  slug: supply-wisdom-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Supply Wisdom Rate Limits
  slug: supply-wisdom-rate-limits
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 38.5
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Supply Wisdom Domain Security
  slug: supply-wisdom-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Supply Wisdom Trust Center
  slug: supply-wisdom-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: supply-wisdom
tags:
- Company
- Risk
- Third-Party Risk Management
- Supply Chain
- Governance Risk and Compliance
- Monitoring
- Intelligence
- Supplier Risk
- Operational Resilience
- ESG
website: https://www.supplywisdom.com/
---
