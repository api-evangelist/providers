---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The API root index the catalog backend serves
  name: Melorra Discovery API
  slug: melorra-discovery-api
- description: Gold, diamond and gemstone product listing and detail
  name: Melorra Products API
  slug: melorra-products-api
- description: Similar and recommended products
  name: Melorra Recommendations API
  slug: melorra-recommendations-api
- description: The silver product line, served by parallel endpoints
  name: Melorra Silver API
  slug: melorra-silver-api
artifact_total: 8
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/melorra-catalog-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.melorra.com/
- group: other
  title: ''
  type: APICatalog
  url: https://www.melorra.com/.well-known/api-catalog
- group: agent
  title: ''
  type: WellKnown
  url: well-known/melorra-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/melorra-llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://www.melorra.com/.well-known/api-catalog
- group: operate
  title: ''
  type: Support
  url: https://www.melorra.com/contactus/
- group: start
  title: ''
  type: SignUp
  url: https://www.melorra.com/sign-in/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.melorra.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.melorra.com/press/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MelorraTech
- group: build
  title: ''
  type: Packages
  url: packages/melorra-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/melorra-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/melorra-plans-pricing.yml
created: '2026-08-25'
description: Melorra is an Indian direct-to-consumer fine jewellery brand, founded in 2015 and operated by August Jewellery Pvt Ltd, selling lightweight, fashion-led gold, diamond, gemstone and silver jewellery designed for everyday and workwear rather than for weddings. It sells online at melorra.com and through an app and a network of experience centres, delivering BIS-hallmarked gold and IGI/SGL-certified stones across hundreds of Indian districts. Melorra runs a public, unauthenticated catalog API at services-catalog.melorra.com and — unusually for a retailer — publishes both an llms.txt and a machine-readable /.well-known/api-catalog document describing it, giving AI agents a documented path into a 21,000-product jewellery catalog. In January 2026 Senco Gold agreed to acquire a controlling 68% stake in August Jewellery.
image: https://assets.melorra.com/logo/favicon.ico
layout: provider
modified: '2026-08-25'
name: Melorra
nav: Providers
network: true
overview: 'Melorra publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Products API, Recommendations API, and 1 more. Tagged areas include Company, Jewellery, Retail, E-Commerce, and Product Catalog.


  Melorra''s developer surface includes documentation, support, signup flow, engineering blog, and 11 more developer resources.'
plans:
- name: Melorra Plans Pricing
  plan_count: 0
  slug: melorra-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Melorra Rate Limits
  slug: melorra-rate-limits
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 12.9
    developer_ergonomics: 30.4
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 23.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Melorra Authentication
  slug: melorra-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Melorra Domain Security
  slug: melorra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: melorra
tags:
- Company
- Jewellery
- Retail
- E-Commerce
- Product Catalog
- Direct to Consumer
- Fashion
- India
website: https://www.melorra.com/
---
