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
api_count: 1
apis:
- description: Bardeen is an AI-powered automation platform for automating repetitive tasks across web applications.
  name: Bardeen
  slug: bardeen
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/bardeen-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bardeen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bardeen-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bardeenai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bardeen
- group: company
  title: ''
  type: Website
  url: https://www.bardeen.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/bardeen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bardeen-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bardeen-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bardeen-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bardeen-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/bardeen-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bardeen-llms.txt
- group: auth
  title: ''
  type: Compliance
  url: https://www.bardeen.ai/security
- group: auth
  title: ''
  type: Security
  url: https://www.bardeen.ai/security
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bardeen.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bardeen.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bardeen.ai/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.bardeen.ai/start
- group: operate
  title: ''
  type: Support
  url: https://www.bardeen.ai/support
- group: company
  title: ''
  type: Blog
  url: https://www.bardeen.ai/blog
coverage:
  checked: '2026-08-29'
  detail: 'Bardeen ships a browser-extension automation product and no API: docs.bardeen.ai is NXDOMAIN, https://www.bardeen.ai/developer-program (which once advertised early SDK access) 301s to the homepage, and none of the 3,155 URLs in the sitemap is an API, SDK, webhook or developer page.'
  evidence:
  - status: 0
    url: https://docs.bardeen.ai
  - status: 301
    url: https://www.bardeen.ai/developer-program
  - status: 404
    url: https://www.bardeen.ai/openapi.json
  - status: 404
    url: https://www.bardeen.ai/.well-known/agent-card.json
  - status: 404
    url: https://www.getwiq.ai/openapi.json
  reason: no-developer-program
  state: none
created: '2026-03-27'
description: Bardeen is an AI automation platform from Bardeen Inc (San Francisco, CA) that automates repetitive go-to-market work — web scraping, web search, contact and company enrichment, and AI-assisted data tasks — from a browser extension that runs against the sites and SaaS tools a user is already signed in to. Work is metered in credits rather than API calls, and automations can run locally in the browser or in Bardeen's cloud. The company also ships WIQ (getwiq.ai), a Workflow Intelligence Platform that reconstructs how work actually happens from browser and system-of-record data. Bardeen consumes other people's APIs through native connectors and generic HTTP actions; it publishes no public API of its own.
finops:
- name: Bardeen Finops
  service_category: API
  slug: bardeen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bardeen.png
layout: provider
modified: '2026-08-29'
name: Bardeen
nav: Providers
network: true
overview: 'Bardeen publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Automation, Workflow-Automation, Web Scraping, Data Enrichment, and Browser Extension.


  Bardeen''s developer surface includes changelog, pricing, signup flow, support, engineering blog, and 16 more developer resources.'
plans:
- name: Bardeen Plans Pricing
  plan_count: 4
  slug: bardeen-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Bardeen Rate Limits
  slug: bardeen-rate-limits
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 13
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 4.7
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 29.3
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bardeen/refs/heads/main/screenshots/bardeen-2026-06-20T172958.png
security:
- kind: domain-security
  name: Bardeen Domain Security
  slug: bardeen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bardeen Vulnerability Disclosure
  slug: bardeen-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Bardeen Trust Center
  slug: bardeen-trust-center
  summary_line: SOC 2 Type 2, GDPR, CASA Tier 2, CASA Tier 3, OWASP ASVS
slug: bardeen
tags:
- AI Automation
- Workflow-Automation
- Web Scraping
- Data Enrichment
- Browser Extension
- Sales Automation
- No-Code
- Go-To-Market
website: https://www.bardeen.ai
---
