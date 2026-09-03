---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.onelineage.com
- group: other
  title: ''
  type: Product
  url: https://www.onelineage.com/lineage-link
- group: other
  title: ''
  type: Services
  url: https://www.onelineage.com/services
- group: operate
  title: ''
  type: Support
  url: https://lineagelinkhelp.onelineage.com/support/s/
- group: start
  title: ''
  type: Login
  url: https://www.onelineage.com/customer-login
- group: company
  title: ''
  type: Blog
  url: https://www.onelineage.com/news-stories
- group: operate
  title: ''
  type: Contact
  url: https://www.onelineage.com/contact
- group: operate
  title: ''
  type: ContactSales
  url: https://www.onelineage.com/contact-sales
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.onelineage.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onelineage.com/privacy-notice
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.onelineage.com/cookie-policy
- group: auth
  title: ''
  type: EthicsCompliance
  url: https://www.onelineage.com/ethics-compliance
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.onelineage.com/overview/default.aspx
- group: company
  title: ''
  type: Careers
  url: https://careers.onelineage.com/
- group: company
  title: ''
  type: About
  url: https://www.onelineage.com/about-us
- group: other
  title: ''
  type: Technology
  url: https://www.onelineage.com/about-us/innovation-technology
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onelineage/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/onelineage
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCKrT_DOlm4icKdCJ7qNdTgg
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/lineagelogistics
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/onelineage/
- group: auth
  title: ''
  type: Authentication
  url: authentication/lineage-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lineage-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lineage-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lineage-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lineage-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lineage-llms.txt
created: '2026-07-17'
description: 'Lineage, Inc. (Nasdaq: LINE) is the world''s largest temperature-controlled warehousing and logistics REIT, operating a global cold-chain network of more than 480 facilities across North America, Europe and Asia-Pacific. It provides cold storage and automated warehousing, blast freezing, food manufacturing and processing support, direct-to-consumer fulfillment, and an integrated transportation arm spanning freight forwarding, customs brokerage, drayage, temperature-controlled rail, managed transportation and multi-vendor consolidation. Its customer-facing technology is Lineage Link, a supply chain platform providing real-time visibility into inventory, orders, appointments and shipment status across the facility network, supported by proprietary systems including the Sybil warehouse-optimization algorithm and the Lineage Eye computer-vision receiving system. Lineage publishes no public API, developer portal or API documentation as of 2026-07-19; customer integration runs through
  Lineage Link and account teams rather than a self-service developer program. This profile therefore captures the verified identity, discovery and domain-security surface rather than an API contract.'
image: https://www.onelineage.com/themes/custom/lineage_custom_new/assets/lineage_logo.svg
layout: provider
modified: '2026-07-19'
name: Lineage
nav: Providers
network: true
overview: 'Lineage is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Cold Chain, Warehousing, and Supply Chain.


  Lineage''s developer surface includes support, engineering blog, YouTube channel, authentication, and 23 more developer resources.'
random_paper: 11
scopes:
- name: Lineage Scopes
  scope_count: 21
  slug: lineage-scopes
  summary_line: 21 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 16.9
  provenance:
    conformance: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lineage/refs/heads/main/screenshots/lineage-2026-07-25T225222.png
security:
- kind: authentication
  name: Lineage Authentication
  slug: lineage-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Lineage Domain Security
  slug: lineage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lineage
tags:
- Company
- Logistics
- Cold Chain
- Warehousing
- Supply Chain
- Temperature Controlled
- Freight
- Transportation
- Food and Beverage
- REIT
website: https://www.onelineage.com
---
