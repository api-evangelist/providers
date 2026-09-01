---
access_model:
  confidence: medium
  label: Paid, self-service product signup; no public API
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://socialsignin.com/go
  - https://socialsignin.com/go/checkout/
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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/socialsignin-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/socialsignin-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/socialsignin-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/socialsignin-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/socialsignin-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://socialsignin.com/
- group: company
  title: ''
  type: About
  url: https://socialsignin.com/about
- group: docs
  title: ''
  type: Documentation
  url: https://socialsigninwifi.zendesk.com/hc/en-us
- group: operate
  title: ''
  type: FAQ
  url: https://socialsigninwifi.zendesk.com/hc/en-us/articles/47737919206427-FAQs
- group: commercial
  title: ''
  type: Pricing
  url: https://socialsignin.com/go
- group: start
  title: ''
  type: SignUp
  url: https://socialsignin.com/go/checkout/
- group: company
  title: ''
  type: Blog
  url: https://socialsignin.com/articles
- group: commercial
  title: ''
  type: TermsOfService
  url: https://socialsign.in/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://socialsignin.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://socialsignin.com/contact
- group: start
  title: ''
  type: Login
  url: https://c.socialsign.in/client/
- group: company
  title: ''
  type: Partners
  url: https://socialsignin.com/partners
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/socialsign-in
coverage:
  checked: '2026-08-12'
  detail: 'SocialSign.in serves a live JSON API root at https://c.socialsign.in/api/ — it returns 200 with the placeholder body "API index" and every unknown child path answers application/json {"error": "page not found"} — but it sits inside the authenticated customer console at c.socialsign.in/client/, the 26-page public sitemap contains no developer or reference page, and the only programmatic capabilities the company names ("Advanced integrations", "Data mart") are features of the unpriced Enterprise tier.'
  evidence:
  - status: 200
    url: https://c.socialsign.in/api/
  - status: 404
    url: https://c.socialsign.in/api/v1
  - status: 200
    url: https://c.socialsign.in/client/
  - status: 404
    url: https://socialsignin.com/openapi.json
  - status: 200
    url: https://socialsignin.com/sitemap-pages.xml
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: 'SocialSign.in is a guest WiFi marketing platform that turns venue Wi-Fi login into a customer-acquisition and engagement channel. When guests connect to free Wi-Fi through branded splash pages, the platform captures opt-in contact data (email, phone, profile), measures visit frequency and dwell time, and syncs profiles to CRM and email/SMS marketing tools to trigger targeted campaigns across retail, hospitality, sports and entertainment, healthcare, and commercial real estate venues. It sells two products: the enterprise platform, sold through a contact-sales motion, and SocialSign.in Go, a self-serve packaged version with published per-location pricing. The company publishes no developer portal, no API reference, and no machine-readable specification of any kind; its product documentation lives in a public Zendesk help center covering portal setup and CRM/ESP connector configuration rather than any programmable interface. A JSON-emitting API root does exist at c.socialsign.in/api/
  inside the authenticated customer console, and the Enterprise tier advertises "Advanced integrations" and a "Data mart", but neither is documented publicly.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/socialsignin.png
layout: provider
modified: '2026-08-12'
name: SocialSign.in
nav: Providers
network: true
overview: 'SocialSign.in is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Guest WiFi, WiFi Marketing, Captive Portal, and Customer Data Platform.


  SocialSign.in''s developer surface includes documentation, FAQ, pricing, signup flow, engineering blog, support, and 12 more developer resources.'
plans:
- name: Socialsignin Plans Pricing
  plan_count: 3
  slug: socialsignin-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Socialsignin Rate Limits
  slug: socialsignin-rate-limits
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 28.1
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Socialsignin Domain Security
  slug: socialsignin-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: socialsignin
tags:
- Company
- Guest WiFi
- WiFi Marketing
- Captive Portal
- Customer Data Platform
- Location Analytics
- Retail Media
- Marketing
website: https://socialsignin.com/
---
