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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.handle.com/
- group: company
  title: ''
  type: Blog
  url: https://www.handle.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.handle.com/hc/en-us
- group: operate
  title: ''
  type: Community
  url: https://buildingblocks.handle.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.handle.com/
- group: start
  title: ''
  type: Login
  url: https://app.handle.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.handle.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.handle.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.handle.com/security-and-trust/
- group: auth
  title: ''
  type: TrustCenter
  url: security/handle-trust-center.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.handle.com/
- group: company
  title: ''
  type: Partners
  url: https://www.handle.com/partners/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/handle-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/handle-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://www.handle.com/security-and-trust/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/handle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/handle-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/handle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/handle-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/handle-llms.txt
coverage:
  checked: '2026-08-22'
  detail: Handle's ERP Integrations page promises "Handle integrates with any ERP" and its own status page has monitored a component named "Main Portal API" since 2023-02-08, but the page's only CTAs are a Contact Sales form and an "Explore the docs" button that links to the trust page rather than to any documentation — there is no developer portal (developers/docs/developer.handle.com do not resolve) and api.handle.com answers unauthenticated callers with nothing but a JSON route hint, {"message":"specify a valid api route like {/api/integrations/{integration_name}/{action}"}.
  evidence:
  - status: 200
    url: https://www.handle.com/erp-integrations/
  - status: 200
    url: https://www.handle.com/contact-sales/
  - status: 404
    url: https://api.handle.com/api
  - status: 404
    url: https://api.handle.com/openapi.json
  - status: 404
    url: https://www.handle.com/developers
  - status: 0
    url: https://developers.handle.com/
  - status: 0
    url: https://docs.handle.com/
  - status: 200
    url: https://handle.statuspage.io/api/v2/components.json
  reason: sales-gate
  state: gated
created: '2026-08-22'
description: Handle (Handle Inc., handle.com) is a San Francisco software company, founded in 2018 by Patrick Hogan, Blake Robertson, Lucas Azevedo and Chris Woodard, that builds financial-operations software for the construction industry. The Handle platform covers lien and notice management, automated lien-waiver exchange, full-service research and verification, automatic state-by-state compliance deadlines, job sheets, credit applications, collections and construction-native online payments, unified by what the company calls its Construction Data Graph. It is sold to material suppliers, equipment dealers and subcontractors — customers named on its own site include Ferguson, ABC Supply, US LBM, Oldcastle, EquipmentShare, The Home Depot, Cemex, Builders FirstSource, Vulcan, Heidelberg Materials, Herc Rentals and Floor & Decor. Handle markets ERP integrations ("Handle integrates with any ERP") and operates a real API host at api.handle.com, and its own status page monitors components named
  "Main Portal API" and "Payment Portal API", but it publishes no developer portal, no API reference, and no machine-readable specification of any kind; the only public route to the integration surface is a Contact Sales form. Handle is SOC 2 Type 1 and Type 2 compliant and publishes a Vanta-hosted trust center. It raised a $27M Series B led by Marbruck with Energize Capital, Suffolk Technologies, Liquid 2 Ventures, RXR, WEX and Amex Ventures participating.
image: https://www.handle.com/wp-content/uploads/2026/06/homepage-2.png
layout: provider
modified: '2026-08-22'
name: Handle
nav: Providers
network: true
overview: 'Handle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Construction Finance, Lien Management, and Lien Waivers.


  Handle''s developer surface includes engineering blog, support, signup flow, and 17 more developer resources.'
plans:
- name: Handle Plans Pricing
  plan_count: 0
  slug: handle-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Handle Rate Limits
  slug: handle-rate-limits
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 21.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Handle Domain Security
  slug: handle-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Handle Vulnerability Disclosure
  slug: handle-vulnerability-disclosure
  summary_line: Hackerone · security.txt
- kind: trust-center
  name: Handle Trust Center
  slug: handle-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2
slug: handle
tags:
- Company
- Construction
- Construction Finance
- Lien Management
- Lien Waivers
- Accounts Receivable
- Credit Management
- Payments
- B2B Payments
- Payment Compliance
- ERP Integrations
- Collection
- Financial Operations
- Material Suppliers
- Equipment Dealers
website: https://www.handle.com/
---
