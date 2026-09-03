---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
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
api_count: 1
apis:
- description: Subscription-based, pre-built healthcare data feeds and scoring APIs that augment a client's internal datasets with PurpleLab's proprietary claims scoring, forecasting, ranking and segmentation. Purpl
  name: HealthNexus API Streams
  slug: healthnexus-api-streams
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://purplelab.com/
- group: other
  title: ''
  type: Platform
  url: https://purplelab.com/platform
- group: company
  title: ''
  type: About
  url: https://purplelab.com/company
- group: operate
  title: ''
  type: Support
  url: https://purplelab.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://purplelab.com/resources
- group: company
  title: ''
  type: BlogRSS
  url: https://purplelab.com/resources/rss.xml
- group: other
  title: ''
  type: Glossary
  url: https://purplelab.com/glossary
- group: company
  title: ''
  type: Careers
  url: https://purplelab.com/careers
- group: start
  title: ''
  type: Login
  url: https://healthnexus-sso.purplelab.com/login?domain=portal.purplelab.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://purplelab.com/terms-and-conditions-2026-01-29
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://purplelab.com/privacy
- group: commercial
  title: ''
  type: ProductPrivacyPolicy
  url: https://purplelab.com/product-privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/purplelab-inc/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/purplelabinc
- group: design
  title: ''
  type: Conformance
  url: conformance/purplelab-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/purplelab-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/purplelab-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/purplelab-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/purplelab-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/purplelab-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/purplelab-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/purplelab-llms.txt
coverage:
  checked: '2026-08-26'
  detail: PurpleLab markets "HealthNexus API Streams" but has retired its product page (purplelab.com/api-streams/ now 404s), publishes no developer portal or reference anywhere in its 238-URL sitemap, and routes every access request through a contact-us form - while the live platform API gateway at api.healthnexus.io answers every anonymous request, including all spec and .well-known paths, with 403 {"message":"Forbidden"}.
  evidence:
  - status: 404
    url: https://purplelab.com/api-streams/
  - status: 403
    url: https://api.healthnexus.io/openapi.json
  - status: 404
    url: https://api.purplelab.com/openapi.json
  - status: 200
    url: https://purplelab.com/sitemap.xml
  - status: 307
    url: https://portal.purplelab.com/
  reason: sales-gate
  state: gated
created: '2026-08-26'
description: PurpleLab is a healthcare data and analytics company headquartered in Wayne, Pennsylvania, whose HealthNexus platform gives life sciences, advertising agencies, financial services, payers and providers no-code access to real-world data and real-world evidence. HealthNexus aggregates billions of medical and pharmacy claims alongside provider, eligibility, remittance, EHR and mortality data into the CLEAR RWD dataset, which PurpleLab states is certified to HIPAA de-identification standards under the Expert Determination method. Alongside the no-code platform the company has marketed HealthNexus API Streams — subscription pre-built data feeds and scoring APIs covering provider profiles, locations, credentials, affiliations, performance and efficiency scores, payer influence and patient risk adjustment. PurpleLab has raised roughly $68M including a $40M Series B led by Primus Capital with Edison Partners, and acquired KAID Health in 2025. No public developer portal, API reference,
  or machine-readable contract is published; the API and platform surfaces sit behind HealthNexus SSO.
image: https://purplelab.com/hubfs/PurpleLab-website/web-app-manifest-512x512.png
layout: provider
modified: '2026-08-26'
name: PurpleLab
nav: Providers
network: true
overview: 'PurpleLab publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Health Data, Real-World Data, Real-World Evidence, and Medical Claims.


  PurpleLab''s developer surface includes support, engineering blog, and 20 more developer resources.'
plans:
- name: Purplelab Plans Pricing
  plan_count: 0
  slug: purplelab-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Purplelab Rate Limits
  slug: purplelab-rate-limits
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 20.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/purplelab/refs/heads/main/screenshots/purplelab-2026-09-02T152342.png
security:
- kind: authentication
  name: Purplelab Authentication
  slug: purplelab-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Purplelab Domain Security
  slug: purplelab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: purplelab
tags:
- Healthcare
- Health Data
- Real-World Data
- Real-World Evidence
- Medical Claims
- Pharmacy Claims
- Provider Data
- Healthcare Analytics
- Life Sciences
- Data Products
- HIPAA
- Company
website: https://purplelab.com/
---
