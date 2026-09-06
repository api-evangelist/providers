---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: A live, anonymous Model Context Protocol endpoint served from the Scripta Insights marketing host and advertised in the company's own /llms.txt. It is the stock Wix Site MCP server (platform-authored,
  name: Scripta Insights Site MCP
  slug: scripta-insights-site-mcp
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scripta-insights-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scriptainsights.com/
- group: company
  title: ''
  type: Blog
  url: https://www.scriptainsights.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.scriptainsights.com/contact
- group: start
  title: ''
  type: Login
  url: https://members.scriptainsights.com/register/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.scriptainsights.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scriptainsights.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scripta-insights-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/scripta-insights-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/scripta-insights-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/scripta-insights-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/scripta-insights-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scripta-insights-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/scripta-insights-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/scripta-insights-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/scripta-insights-trust-center.yml
coverage:
  checked: '2026-08-26'
  detail: Scripta's own Technology page lists "API-only" as one of five customer integration options and the api.scriptainsights.com host resolves and answers (Apache Tomcat), but every documentation path on it 404s and there is no developer portal, reference or machine-readable contract anywhere on the site — API access is obtained through the enterprise contact-sales form, not a published spec.
  evidence:
  - status: 200
    url: https://www.scriptainsights.com/technology
  - status: 404
    url: https://api.scriptainsights.com/openapi.json
  - status: 400
    url: https://www.scriptainsights.com/openapi.json
  - status: 200
    url: https://members.scriptainsights.com/api-docs
  reason: sales-gate
  state: gated
created: '2026-08-26'
description: 'Scripta Insights is a Boston-founded healthcare technology company that sells pharmacy benefit cost containment to self-insured employers, health plans, TPAs and benefits consultants. Its doctor-driven Rx Navigation platform layers on top of an existing plan design and PBM contract — no PBM change, no benefit redesign — and is built on two proprietary engines: Med Mapper, which maps nearly every drug on the market to safe, evidence-based clinical alternatives, and Rx Savings Mapper, which prices those alternatives against the employer''s own plan design, formulary, PBM contract and recent patient claims. Members receive personalized savings reports; plan sponsors receive utilization and savings reporting, fiduciary-compliance support, a GLP-1 Navigator and a Provider Navigator prescribing tool. Scripta integrates with cash-pay channels including Mark Cuban Cost Plus Drugs, RxSaveCard and Precision Coupons, and offers customer integration by SSO, an API-only connection, white-label,
  simple HTTP redirect or a data partner model — none of which is publicly documented.'
image: https://static.wixstatic.com/media/670dfe_c1d7cfb976094245b56a0862497fe945~mv2.jpg/v1/fill/w_2500,h_1312,al_c/670dfe_c1d7cfb976094245b56a0862497fe945~mv2.jpg
layout: provider
mcp_servers:
- description: ''
  name: Scripta Insights Site MCP
  slug: scripta-insights-site-mcp
modified: '2026-08-26'
name: Scripta Insights
nav: Providers
network: true
overview: 'Scripta Insights publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Pharmacy Benefits, Prescriptions, and Health Plans.


  Scripta Insights'' developer surface includes engineering blog, support, and 14 more developer resources.'
plans:
- name: Scripta Insights Plans Pricing
  plan_count: 0
  slug: scripta-insights-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Scripta Insights Rate Limits
  slug: scripta-insights-rate-limits
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 24.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa-cpra
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scripta-insights/refs/heads/main/screenshots/scripta-insights-2026-09-02T154618.png
security:
- kind: domain-security
  name: Scripta Insights Domain Security
  slug: scripta-insights-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Scripta Insights Vulnerability Disclosure
  slug: scripta-insights-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Scripta Insights Trust Center
  slug: scripta-insights-trust-center
  summary_line: HIPAA, SOC 2
slug: scripta-insights
tags:
- Company
- Healthcare
- Pharmacy Benefits
- Prescriptions
- Health Plans
- Employee Benefits
- Digital Health
- Healthcare Costs
- Insurance
- MCP
website: https://www.scriptainsights.com/
---
