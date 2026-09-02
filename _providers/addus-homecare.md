---
access_model:
  confidence: high
  label: No public API to access
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - contract-discovery
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
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://addus.com/
- group: company
  title: ''
  type: About
  url: https://addus.com/why-addus/
- group: other
  title: ''
  type: Team
  url: https://addus.com/team/
- group: operate
  title: ''
  type: Support
  url: https://addus.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://addus.com/careers/
- group: other
  title: ''
  type: Locations
  url: https://addus.com/locations/
- group: company
  title: ''
  type: Blog
  url: https://addus.com/blog/
- group: company
  title: ''
  type: BlogFeeds
  url: https://addus.com/feed/
- group: company
  title: ''
  type: Investors
  url: https://addus.gcs-web.com/
- group: operate
  title: ''
  type: PressReleases
  url: https://addus.gcs-web.com/news-releases
- group: commercial
  title: ''
  type: TermsOfService
  url: https://addus.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://addus.com/privacy-policy/
- group: other
  title: ''
  type: DataRights
  url: https://addus.com/data-rights-request/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/addus-homecare-inc
- group: auth
  title: ''
  type: DomainSecurity
  url: security/addus-homecare-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/addus-homecare-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/addus-homecare-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/addus-homecare-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/addus-homecare-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/addus-homecare-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/addus-homecare-finops.yml
coverage:
  checked: '2026-08-30'
  detail: Addus HomeCare delivers personal care, home health and hospice in the home and bills Medicaid and Medicare payers for it, so there is no product to expose as an API; the two hosts a prior profile listed, api.addus.com and developer.addus.com, return NXDOMAIN with no A record and no CNAME, and addus.com is a WordPress marketing site whose only JSON endpoint is WordPress core at /wp-json/, closed with 401 rest_not_logged_in.
  evidence:
  - status: 0
    url: https://api.addus.com/
  - status: 0
    url: https://developer.addus.com/docs
  - status: 404
    url: https://addus.com/openapi.json
  - status: 404
    url: https://addus.com/llms.txt
  - status: 404
    url: https://addus.com/.well-known/agent-card.json
  - status: 404
    url: https://addus.com/.well-known/api-catalog
  - status: 404
    url: https://addus.com/graphql
  - status: 401
    url: https://addus.com/wp-json/wp/v2
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: 'Addus HomeCare Corporation (NASDAQ: ADUS) is a US provider of personal care, home health and hospice services delivered in the home and community, headquartered at 6303 Cowboys Way, Frisco, Texas. It serves consumers across roughly three dozen states through a large field workforce of caregivers, nurses and therapists, with revenue coming predominantly from Medicaid and Medicaid-managed-care programs, Medicare and managed-care payers rather than from software. Addus is a care-delivery organization, not a software vendor: contract discovery on 2026-08-30 found no developer program, no public API, no SDK, no published package on any registry and no machine-readable contract of any kind. Its clinical and operational systems are supplied by partners — Homecare Homebase for the home-based care platform under a joint development agreement announced in April 2021, and CellTrak for Electronic Visit Verification — and any system-to-system exchange (HL7, payer X12 EDI, state EVV aggregators)
  is scoped by partner contract rather than by a public developer portal. Two earlier hosts on this profile, api.addus.com and developer.addus.com, were probed and do not resolve; they have been removed.'
finops:
- name: Addus Homecare Finops
  service_category: Home Care / Hospice / Home Health Services
  slug: addus-homecare-finops
image: /assets/icons/addus-homecare.png
layout: provider
modified: '2026-08-30'
name: Addus HomeCare
nav: Providers
network: true
overview: 'Addus HomeCare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Home Care, Home Health, Hospice, and Personal Care.


  Addus HomeCare''s developer surface includes support, engineering blog, and 19 more developer resources.'
plans:
- name: Addus Homecare Plans Pricing
  plan_count: 0
  slug: addus-homecare-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Addus Homecare Rate Limits
  slug: addus-homecare-rate-limits
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 85.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 16.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/addus-homecare/refs/heads/main/screenshots/addus-homecare-2026-06-20T164631.png
security:
- kind: domain-security
  name: Addus Homecare Domain Security
  slug: addus-homecare-domain-security
  summary_line: TLSv1.3 · DMARC
slug: addus-homecare
tags:
- Company
- Home Care
- Home Health
- Hospice
- Personal Care
- Healthcare Services
- Health
- Care Delivery
- Home and Community Based Services
- Fortune 1000
- Texas
website: https://addus.com/
---
