---
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
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/secondsight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.secondsight.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.secondsight.ai/pricing-new/
- group: start
  title: ''
  type: Login
  url: https://www.secondsight.ai/login/
- group: start
  title: ''
  type: SignUp
  url: https://www.secondsight.ai/request-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.secondsight.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.secondsight.ai/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.secondsight.ai/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.secondsight.ai/insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.secondsight.ai/feed/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.secondsight.ai/
- group: auth
  title: ''
  type: Security
  url: https://www.secondsight.ai/security/
- group: auth
  title: ''
  type: Compliance
  url: https://www.secondsight.ai/security/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/second-sight-for-cyberinsurance
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/secondsight-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/secondsight-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/secondsight-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/secondsight-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/secondsight-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/secondsight-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/secondsight-vulnerability-disclosure.yml
coverage:
  checked: '2026-08-26'
  detail: SecondSight ships its cyber-insurance AI only as three logged-in SaaS workbenches; the 40-page sitemap on www.secondsight.ai contains no developer, API, docs or integration page, /developers/ /docs/ /integrations/ all 404, and the one live API host api.secondsight.ai answers every unauthenticated path — including /openapi.json, /swagger.json, /graphql and /mcp — with the same JSON 404 body {"error":"requested path is invalid"}.
  evidence:
  - status: 404
    url: https://api.secondsight.ai/openapi.json
  - status: 404
    url: https://www.secondsight.ai/developers/
  - status: 404
    url: https://www.secondsight.ai/.well-known/agent-card.json
  - status: 403
    url: https://forgeglobal.com/secondsight_stock/
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: SecondSight is a Bloomington, Indiana software company building a "vertical AI" operating system for cyber insurance and digital risk. Its Digital Risk Management Platform packages three SaaS surfaces — Company Workbench (digital asset inventory, privacy and vulnerability scanning, insurability preparation), Broker Workbench (client management, auto-complete applications, quote/bind automation, book value and portfolio analytics) and Underwriter Workbench (risk prediction, portfolio balancing, mitigation) — alongside Exposurescape, a digital-telematics engine for exposure detection and catastrophic-event forecasting. The company was founded in 2019, came out of stealth in 2022 with a seed round led by Tim Crown, and sells to brokers, carriers, MGUs and reinsurers. SecondSight publishes pricing, a SOC 2 security commitments page and a Better Stack status page for its Risk Workbench service, but as of this pass it operates no public developer program — no developer portal, API
  reference, SDK, or machine-readable contract of any kind is published.
image: https://www.secondsight.ai/wp-content/uploads/2023/01/second-sight-logo.svg
layout: provider
modified: '2026-08-26'
name: SecondSight
nav: Providers
network: true
overview: 'SecondSight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Cyber Insurance, Insurtech, and Risk Management.


  SecondSight''s developer surface includes pricing, signup flow, support, engineering blog, and 17 more developer resources.'
plans:
- name: Secondsight Plans Pricing
  plan_count: 0
  slug: secondsight-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Secondsight Rate Limits
  slug: secondsight-rate-limits
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 19.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 35.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Secondsight Domain Security
  slug: secondsight-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Secondsight Vulnerability Disclosure
  slug: secondsight-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Secondsight Trust Center
  slug: secondsight-trust-center
  summary_line: SOC 2
slug: secondsight
tags:
- Company
- Insurance
- Cyber Insurance
- Insurtech
- Risk Management
- Cybersecurity
- Underwriting
- Artificial Intelligence
- Analytics
website: https://www.secondsight.ai/
---
