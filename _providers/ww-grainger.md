---
access_model:
  confidence: medium
  label: Gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://api.grainger.com/swagger.json
  - https://success.procurify.com/en/articles/9001922-grainger-punchout-overview
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
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ww-grainger-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wwgrainger
- group: company
  title: ''
  type: Website
  url: https://www.grainger.com
- group: design
  title: ''
  type: Conformance
  url: conformance/ww-grainger-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ww-grainger-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/ww-grainger-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ww-grainger-rate-limits.yml
coverage:
  checked: '2026-08-28'
  detail: Grainger runs a live API gateway at api.grainger.com whose only routed documentation path, /swagger.json, answers anonymous callers with HTTP 503 "ACCESS DENIED - Log onto the Grainger Network ... through a secure VPN connection", and its eProcurement PunchOut and X12 4010 EDI credentials are issued only by a Grainger account representative over a stated 4-6 week onboarding, so no contract or reference exists outside an active customer agreement.
  evidence:
  - status: 503
    url: https://api.grainger.com/swagger.json
  - status: 503
    url: https://api.grainger.com/swagger-ui.html
  - status: 404
    url: https://api.grainger.com/openapi.json
  - status: 404
    url: https://api.grainger.com/.well-known/api-catalog
  - status: 200
    url: https://success.procurify.com/en/articles/9001922-grainger-punchout-overview
  reason: customer-only-docs
  state: gated
created: '2026-03-21'
description: 'W. W. Grainger, Inc. (NYSE: GWW) is a Fortune 500 broad-line distributor of maintenance, repair and operating (MRO) products serving businesses and institutions across North America, Japan and the United Kingdom through roughly 331 branches, 34 distribution centers and its digital channels. Its system-to-system commerce runs through eProcurement rather than a public developer program: PunchOut catalogs into Ariba, Coupa, Jaggaer, SAP, Oracle and GHX, ANSI ASC X12 4010 EDI for purchase orders, acknowledgments, ship notices and invoices, and the KeepStock inventory-management program. Grainger operates an API gateway at api.grainger.com, but its Swagger surface answers anonymous callers with an ACCESS DENIED page requiring the Grainger corporate network, and integration credentials are issued only by a Grainger account representative, so no public API contract or reference is available to evaluate.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ww-grainger.png
layout: provider
modified: '2026-08-28'
name: W. W. Grainger
nav: Providers
network: true
overview: W. W. Grainger is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Industrial Supply, MRO, Distribution, and B2B eCommerce.
plans:
- name: Ww Grainger Plans Pricing
  plan_count: 0
  slug: ww-grainger-plans-pricing
press:
- date: '2026-05-25'
  title: Updated March 2025 - Investor Presentation
  url: https://s1.q4cdn.com/422144722/files/doc_presentations/2025/Mar/21/2025-March_GWW-Investor-Presentation-FINAL-3-28-25.pdf
- date: '2026-05-25'
  title: GRAINGER REPORTS RESULTS FOR THE FIRST QUARTER ...
  url: https://pressroom.grainger.com/news/press-release-details/2025/GRAINGER-REPORTS-RESULTS-FOR-THE-FIRST-QUARTER-2025/default.aspx
- date: '2026-05-25'
  title: GRAINGER REPORTS RESULTS FOR THE SECOND ...
  url: https://www.prnewswire.com/news-releases/grainger-reports-results-for-the-second-quarter-2025-302519237.html
- date: '2026-05-25'
  title: GRAINGER REPORTS RESULTS FOR THE THIRD ...
  url: https://pressroom.grainger.com/news/press-release-details/2025/GRAINGER-REPORTS-RESULTS-FOR-THE-THIRD-QUARTER-2025/default.aspx
- date: '2026-05-25'
  title: Grainger expands AI in sales, marketing, and KeepStock ...
  url: https://www.digitalcommerce360.com/2026/02/04/grainger-ai-sales-marketing-keepstock-tools/
random_paper: 17
rate_limits:
- limit_count: 0
  name: Ww Grainger Rate Limits
  slug: ww-grainger-rate-limits
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 8.3
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ww-grainger/refs/heads/main/screenshots/ww-grainger-2026-06-20T201645.png
security:
- kind: domain-security
  name: Ww Grainger Domain Security
  slug: ww-grainger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ww-grainger
tags:
- Fortune 500
- Industrial Supply
- MRO
- Distribution
- B2B eCommerce
- Procurement
- Supply Chain
- EDI
website: https://www.grainger.com
---
