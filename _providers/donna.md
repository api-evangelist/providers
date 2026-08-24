---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.askdonna.com
- group: company
  title: ''
  type: Blog
  url: https://www.askdonna.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.askdonna.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.askdonna.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.askdonna.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.askdonna.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.askdonna.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dealside
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.askdonna.com
- group: auth
  title: ''
  type: Compliance
  url: https://trust.askdonna.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.askdonna.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/donna-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/donna-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/donna-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/donna-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/donna-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/donna-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/donna-domain-security.yml
coverage:
  checked: '2026-08-14'
  detail: Donna ships only as an end-user SaaS product — full STEP 0b contract discovery across www/apex/app/docs hosts found no OpenAPI, no GraphQL, no MCP endpoint and no agent card, the marketing site has no /api, /docs or /developers route, and the company's own status page tracks four end-user surfaces (web app, mobile app, voice calling, notetaker) with no API component.
  evidence:
  - status: 404
    url: https://www.askdonna.com/developers
  - status: 404
    url: https://www.askdonna.com/openapi.json
  - status: 404
    url: https://www.askdonna.com/.well-known/agent-card.json
  - status: 522
    url: https://docs.askdonna.com/openapi.json
  - status: 200
    url: https://www.askdonna.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Donna is a voice-first, always-on AI assistant purpose-built for field sales teams, developed by Dealside and sold at askdonna.com. It automates the administrative work that surrounds selling in the field: preparing pre-meeting briefings, capturing and structuring meeting notes for both in-person and virtual calls, drafting follow-up emails and quotes, and writing captured data back into the CRM automatically. Donna integrates with the enterprise systems field reps already use, including Salesforce, HubSpot, Microsoft Dynamics 365, SAP, Outlook, and Google Calendar, and reports outcomes such as a 75% reduction in admin time, a 20% lift in sales conversion, and roughly 10x higher CRM adoption. Founded in 2024 by Nicolas Christiaen (CEO), Jonas Deprez (COO), and Xander Berkein (CTO), the company operates from Ghent, London, and New York and is backed by Point Nine, Frontline Ventures, Fortino Capital, Pitchdrive, and others. The platform is ISO 27001-certified and compliant with
  SOC 2, GDPR, and CCPA, with data encrypted in transit and never used to train AI models. Donna is a SaaS product and does not currently publish a public developer API, SDK, or MCP server surface; its only machine-readable public artifact is an llms.txt at askdonna.com, which describes the product for AI agents but exposes no callable operations.'
image: https://cdn.prod.website-files.com/68d14433cd550114f9ff7bf6/69e8bd055906bffcf55795e2_meta-image.png
layout: provider
modified: '2026-08-14'
name: Donna
nav: Providers
network: true
overview: 'Donna is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Sales, Field Sales, and CRM.


  Donna''s developer surface includes engineering blog, pricing, support, and 15 more developer resources.'
plans:
- name: Donna Plans Pricing
  plan_count: 0
  slug: donna-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Donna Rate Limits
  slug: donna-rate-limits
score:
  band: emerging
  composite: 22.5
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 22.5
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/donna/refs/heads/main/screenshots/donna-2026-07-25T212251.png
security:
- kind: domain-security
  name: Donna Domain Security
  slug: donna-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Donna Trust Center
  slug: donna-trust-center
  summary_line: ISO 27001, SOC 2, GDPR, CCPA
slug: donna
tags:
- Company
- Artificial Intelligence
- Sales
- Field Sales
- CRM
- Sales Enablement
- Voice AI
- Productivity
- Software-as-a-Service
- AI Assistant
website: https://www.askdonna.com
---
