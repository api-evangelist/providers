---
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
    well_known_catalog: true
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Sourcemap describes a secure real-time RESTful API used to integrate the traceability platform with ERP and enterprise data stacks (SAP, Salesforce Net Zero Cloud, Databricks) and with customs portals
  name: Sourcemap Platform API
  slug: sourcemap-platform-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sourcemap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sourcemap.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sourcemap.com/blog
- group: operate
  title: ''
  type: Support
  url: https://info.sourcemap.com/supplier-support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sourcemap.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sourcemap.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sourcemap-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/sourcemap-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/sourcemap-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sourcemap-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sourcemap.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/sourcemap-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sourcemap-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/sourcemap-packages.yml
coverage:
  checked: '2026-08-28'
  detail: Sourcemap markets "a secure real-time RESTful API" on its integrations page, and api.sourcemap.com does resolve to an Azure Application Gateway fronting a Kong router, but every anonymous path is refused with 403 Access Forbidden and x-robots-tag "noindex, nofollow, noarchive" while the 379-URL sitemap contains no developer, docs, reference, or pricing page at all — the only route to the contract is the Request a Demo form.
  evidence:
  - status: 403
    url: https://api.sourcemap.com/openapi.json
  - status: 404
    url: https://api.sourcemap.com/v1/openapi.json
  - status: 404
    url: https://www.sourcemap.com/pricing
  - status: 401
    url: https://status.sourcemap.com/
  - status: 200
    url: https://www.sourcemap.com/company/request-a-demo
  - status: 200
    url: https://www.sourcemap.com/llms.txt
  reason: sales-gate
  state: gated
created: '2026-08-28'
description: 'Sourcemap is an enterprise supply chain transparency and due diligence software company, founded at the MIT Media Lab by Leonardo Bonanni and headquartered in New York. Its platform performs n-tier supply chain mapping, automated sub-supplier discovery, bill-of-materials mapping, transaction-level chain-of-custody traceability, supplier watchlist screening and AI document review, so that brands and manufacturers can meet regulatory obligations including the EU Deforestation Regulation (EUDR), the Uyghur Forced Labor Prevention Act (UFLPA), the Corporate Sustainability Due Diligence Directive (CSDDD), CTPAT, conflict minerals rules and Section 232 tariff and customs enforcement. Sourcemap describes a real-time RESTful API and a data pipeline that moves structured data in both directions with SAP, Salesforce Net Zero Cloud, Databricks and the EU TRACES customs portal, but that API is sold and provisioned as part of an enterprise engagement: there is no public developer portal,
  no published API reference, no pricing page and no machine-readable contract on any Sourcemap host. Customers include Ferrero, Hershey, Woolworths and AG1.'
image: https://www.sourcemap.com/modules/core/client/img/brand/logo.png
layout: provider
modified: '2026-08-28'
name: Sourcemap
nav: Providers
network: true
overview: 'Sourcemap publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Supply Chain, Traceability, Supply Chain Transparency, and Due Diligence.


  Sourcemap''s developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: Sourcemap Plans Pricing
  plan_count: 0
  slug: sourcemap-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Sourcemap Rate Limits
  slug: sourcemap-rate-limits
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 18.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Sourcemap Domain Security
  slug: sourcemap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sourcemap
tags:
- Company
- Supply Chain
- Traceability
- Supply Chain Transparency
- Due Diligence
- Regulatory Compliance
- ESG
- Sustainability
- Risk Management
- Logistics
- Manufacturing
website: https://www.sourcemap.com/
---
