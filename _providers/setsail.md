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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.setsail.co/
- group: company
  title: ''
  type: Blog
  url: https://www.setsail.co/blog
- group: operate
  title: ''
  type: Support
  url: https://www.setsail.co/contact
- group: start
  title: ''
  type: Login
  url: https://app.setsail.co/splash
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.setsail.co/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zoominfo.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zoominfo.com/legal/terms-of-use
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.zoominfo.com/trust-center/your-privacy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/setsail-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/setsail-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.setsail.co/legal/vulnerability-reporting-policy
- group: design
  title: ''
  type: Conformance
  url: conformance/setsail-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.setsail.co/faq/is-setsail-secure
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/setsail-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/setsail-plans-pricing.yml
coverage:
  checked: '2026-08-13'
  detail: SetSail ships only an end-user product — the sole SetSail-served HTTP API is the private backend of its own customer app at https://app.setsail.co/api/, which answers {"error":"Authentication Error"} with HTTP 401 on every path including /api/openapi.json, and none of the 365 URLs in the sitemap or the 104 public FAQ/knowledge-base pages is a developer portal, API reference or spec (they describe only the CRM, email and calendar APIs SetSail consumes).
  evidence:
  - status: 401
    url: https://app.setsail.co/api/openapi.json
  - status: 404
    url: https://www.setsail.co/openapi.json
  - status: 404
    url: https://www.setsail.co/developers
  - status: 404
    url: https://www.setsail.co/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: SetSail is a revenue-operations and sales-AI platform (now part of ZoomInfo) that automatically captures sales activity data from email, calendar, and contacts and syncs it to Salesforce, then layers AI-powered revenue intelligence on top of it, including MEDDIC deal analysis, meeting preparation, deal alerts, and performance coaching. Insights are delivered to sales reps and leaders through Slack, email, the browser, and Salesforce, and activity data can be routed to Snowflake, Databricks, Tableau, and Looker for analytics. SetSail does not publish a public developer API, developer portal, or OpenAPI at this time; this profile captures its public identity and domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/setsail.png
layout: provider
modified: '2026-08-13'
name: SetSail
nav: Providers
network: true
overview: 'SetSail is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Revenue Operations, Sales Intelligence, and Artificial Intelligence.


  SetSail''s developer surface includes engineering blog, support, and 13 more developer resources.'
plans:
- name: Setsail Plans Pricing
  plan_count: 0
  slug: setsail-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Setsail Rate Limits
  slug: setsail-rate-limits
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 18.6
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/setsail/refs/heads/main/screenshots/setsail-2026-09-02T155027.png
security:
- kind: domain-security
  name: Setsail Domain Security
  slug: setsail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Setsail Vulnerability Disclosure
  slug: setsail-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: setsail
tags:
- Company
- Sales
- Revenue Operations
- Sales Intelligence
- Artificial Intelligence
- CRM
- Salesforce
- Sales Enablement
website: https://www.setsail.co/
---
