---
agent_readiness:
  band: agent-ready
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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Read-only, unauthenticated JSON status API served from Empowerly's own status subdomain by Atlassian Statuspage. Exposes the overall page status indicator, the component roster (currently a single "Em
  name: Empowerly Status API
  slug: empowerly-status-api
artifact_total: 8
collections:
- collection_type: open
  name: Empowerly Status API
  slug: open-empowerly-status-api
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/empowerly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/empowerly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/empowerly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://empowerly.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/empowerly_stock/
- group: company
  title: ''
  type: Blog
  url: https://empowerly.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://empowerly.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://empowerly.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://empowerly.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.empowerly.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/empowerly
- group: operate
  title: ''
  type: StatusPage
  url: https://status.empowerly.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/empowerly-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/empowerly-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/empowerly-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/empowerly-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/empowerly-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/empowerly-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/empowerly-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/empowerly-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/empowerly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/empowerly-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/empowerly-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/empowerly-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/empowerly-well-known.yml
coverage:
  checked: '2026-08-12'
  detail: Empowerly runs a live production API host (api.empowerly.com/health returns 200 "Empowerly Production API is up and running") purely as the private backend for its student web portal, and publishes nothing around it — no developer portal, no docs, no spec, no SDKs, no GitHub org; developer.empowerly.com and docs.empowerly.com do not even resolve.
  evidence:
  - status: 200
    url: https://api.empowerly.com/health
  - status: 404
    url: https://api.empowerly.com/openapi.json
  - status: 404
    url: https://empowerly.com/developers
  - status: 404
    url: https://empowerly.com/api
  - status: 403
    url: https://empowerly.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/empowerly
  - status: 200
    url: https://status.empowerly.com/api/v2/summary.json
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: 'Empowerly is an education-technology company founded in 2017 by Hanmei Wu and Changxiao Xie that delivers personalized college admissions and career counseling to high-school students. The platform pairs students with a network of more than 100 counselors — including former college admission officers — and layers on data-driven tooling: a proprietary admissions calculator built from thousands of past student outcomes, college-list building, essay editing and review, interview preparation, and startup and research internship placement programs. Students and families work through the Empowerly web portal at app.empowerly.com; counseling packages are sold through an enrollment conversation rather than published price tiers. Empowerly publishes no public developer program, API documentation, or SDKs; the only publicly callable surface on its own domains is the Atlassian-hosted status page API at status.empowerly.com.'
image: https://empowerly.com/empowerly-icon.png
layout: provider
modified: '2026-08-12'
name: Empowerly
nav: Providers
network: true
overview: 'Empowerly publishes 1 API on the [APIs.io](https://apis.io/) network: Status API. Tagged areas include Company, education, edtech, college-admissions, and counseling.


  Empowerly''s developer surface includes engineering blog, pricing, authentication, and 23 more developer resources.'
plans:
- name: Empowerly Plans Pricing
  plan_count: 0
  slug: empowerly-plans-pricing
random_paper: 102
rate_limits:
- limit_count: 0
  name: Empowerly Rate Limits
  slug: empowerly-rate-limits
score:
  band: thin
  composite: 41.9
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 49.3
    developer_ergonomics: 19.6
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 26.3
  previous_composite: 41.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Empowerly Authentication
  slug: empowerly-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Empowerly Domain Security
  slug: empowerly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Empowerly Vulnerability Disclosure
  slug: empowerly-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Empowerly Trust Center
  slug: empowerly-trust-center
  summary_line: SOC 2 Type 2
slug: empowerly
tags:
- Company
- education
- edtech
- college-admissions
- counseling
- students
- career-services
- consumer-services
- status-page
website: https://empowerly.com/
---
