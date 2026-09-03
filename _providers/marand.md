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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.marand.com/
- group: company
  title: ''
  type: About
  url: https://marand.com/en/about
- group: company
  title: ''
  type: Blog
  url: https://marand.com/en/blog
- group: company
  title: ''
  type: Careers
  url: https://marand.com/en/career
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://marand.com/en/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://marand.com/en/cookie-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/marand
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCZDBeAKUrpjCoPahqrhKswQ
- group: design
  title: ''
  type: Conformance
  url: conformance/marand-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/marand-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marand-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/marand-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/marand-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/marand-llms.txt
coverage:
  checked: '2026-09-02'
  detail: Marand markets TM Forum Open API implementations and holds public TM Forum conformance certificates for TMF633 and TMF673, but the APIs ship only inside licensed BSS components deployed at operator customers — marand.com has no developer section, and api/docs/developer.marand.com do not resolve, so the reference exists only for contracted tenants.
  evidence:
  - status: 200
    url: https://marand.com/en/products/cim
  - status: 404
    url: https://marand.com/openapi.json
  - status: 404
    url: https://marand.com/.well-known/api-catalog
  - status: 200
    url: https://s3.us-east-1.amazonaws.com/tmf-sfdc-public/Conformance/CON-01460/Marand-Certification%20Report-TMF633%20API-Mar2022.pdf
  reason: customer-only-docs
  state: gated
created: '2026-09-02'
description: Marand Software (Marand d.o.o., Ljubljana, Slovenia) builds cloud-native Business Support System components for communications service providers, positioned as a vendor of TM Forum Open Digital Architecture (ODA) components. Its product line covers a Unified Product Catalog, 360 Customer / Inventory, CPQ, CRM, Multiservice Enterprise Billing, AI/ML solutions and custom software services. Marand's components implement the TM Forum Information Framework (SID) and expose TM Forum Open APIs; the company is a TM Forum Open API Gold certified member, holds Open API conformance certifications for TMF633 (Service Catalog Management, 2022) and TMF673 (Geographic Address Management, 2023), achieved "Ready for ODA" status in March 2024, and co-authored the TMF760 Product Configuration API with Orange and Amdocs as one of the first fifth-generation TM Forum Open APIs. Marand publishes no public developer portal, API reference or machine-readable specification of its own — its APIs ship
  inside licensed components deployed at operator customers, and the contracts they implement are the TM Forum specifications.
image: https://marand.com/android-icon-192x192.png
layout: provider
modified: '2026-09-02'
name: Marand
nav: Providers
network: true
overview: 'Marand is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telecommunications, Business Support Systems, BSS, and TM Forum.


  Marand''s developer surface includes engineering blog, YouTube channel, and 12 more developer resources.'
plans:
- name: Marand Plans Pricing
  plan_count: 0
  slug: marand-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Marand Rate Limits
  slug: marand-rate-limits
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 12.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 36.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Marand Domain Security
  slug: marand-domain-security
  summary_line: TLSv1.3 · DMARC
slug: marand
tags:
- Company
- Telecommunications
- Business Support Systems
- BSS
- TM Forum
- Open Digital Architecture
- Open API
- Product Catalog
- CPQ
- CRM
- Billing
- Enterprise Software
- Standards Conformance
- Slovenia
website: https://www.marand.com/
---
