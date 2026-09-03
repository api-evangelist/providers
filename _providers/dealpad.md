---
access_model:
  confidence: high
  label: Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - https://www.dealpad.io/pricing
  - https://www.dealpad.io/request-demo
  trial: true
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dealpad-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dealpad.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dealpad.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.dealpad.io/request-demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dealpad.io/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dealpad-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/dealpad-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dealpad-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dealpad-lifecycle.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dealpad-io/
coverage:
  checked: '2026-08-13'
  detail: Dealpad sells "API integrations" as a line item on its $2,999/month Large tier behind a "Talk to our Enterprise Team" button, and publishes no reference, spec, or developer page anywhere — its only API is a session-authenticated /apiv1/ application backend that answers anonymous callers with HTTP 403.
  evidence:
  - status: 200
    url: https://www.dealpad.io/pricing
  - status: 403
    url: https://api.dealpad.io/apiv1/c/userLoad
  - status: 404
    url: https://www.dealpad.io/openapi.json
  - status: 404
    url: https://api.dealpad.io/openapi.json
  - status: 404
    url: https://www.dealpad.io/llms.txt
  - status: 526
    url: https://app.dealpad.io/
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: 'Dealpad is an AI-powered buyer-enablement and digital-sales-room platform for B2B sales teams. It centralizes the buyer and seller relationship into shared digital sales rooms, mutual action plans, and curated content, then layers "Sales Mind AI" predictive insight over each opportunity to help sellers progress complex, multi-stakeholder deals faster. Dealpad integrates with major CRMs including Salesforce, HubSpot, and Zoho, and targets sales leaders, account executives, and enterprise revenue teams. Added to the API Evangelist network as a portfolio company of 500 Global. Dealpad publishes no public developer API, OpenAPI definition, developer portal, SDK, or webhook catalog: "API integrations" is sold as a feature of the Large enterprise tier (from $2,999/month) behind a talk-to-sales gate, so the contract is not readable without a commercial conversation.'
image: https://www.dealpad.io/e45464bfae270d5d26cf.png
layout: provider
modified: '2026-08-13'
name: Dealpad
nav: Providers
network: true
overview: 'Dealpad is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales Enablement, Buyer Enablement, Digital Sales Room, and Sales.


  Dealpad''s developer surface includes pricing, signup flow, and 8 more developer resources.'
plans:
- name: Dealpad Plans Pricing
  plan_count: 3
  slug: dealpad-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Dealpad Rate Limits
  slug: dealpad-rate-limits
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dealpad/refs/heads/main/screenshots/dealpad-2026-07-25T211512.png
security:
- kind: domain-security
  name: Dealpad Domain Security
  slug: dealpad-domain-security
  summary_line: DMARC
slug: dealpad
tags:
- Company
- Sales Enablement
- Buyer Enablement
- Digital Sales Room
- Sales
- CRM
- B2B
- Artificial Intelligence
website: https://dealpad.io
---
