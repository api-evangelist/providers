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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/4basecare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.4basecare.com/
- group: company
  title: ''
  type: About
  url: https://www.4basecare.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://www.4basecare.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.4basecare.com/knowledge-centre
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.4basecare.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.4basecare.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/4basecare
- group: start
  title: ''
  type: x-ClinicianPortal
  url: https://galens.4basecare.com/
- group: other
  title: ''
  type: x-Publications
  url: https://www.4basecare.com/publications
- group: company
  title: ''
  type: Careers
  url: https://www.4basecare.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/4basecare
- group: other
  title: ''
  type: x-EquityZen
  url: https://equityzen.com/company/4basecare
- group: build
  title: ''
  type: Packages
  url: packages/4basecare-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/4basecare-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/4basecare-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/4basecare-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.4basecare.com/indian-subcontinent
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/4basecare-llms.txt
coverage:
  checked: '2026-09-05'
  detail: '4baseCare ships clinical genomics as an end-user service - PDF genomic reports and the login-gated Galens clinician web app - and has no developer program at all: the sitemap''s 32 URLs contain no developer, API or docs page, and the only API-shaped host, api.4basecare.com, answers 200 with the stock CodeIgniter "Welcome" page and 404s every spec, well-known and discovery path because it is the private backend for the Galens single-page app, not a published API.'
  evidence:
  - status: 200
    url: https://api.4basecare.com/
  - status: 404
    url: https://api.4basecare.com/openapi.json
  - status: 404
    url: https://api.4basecare.com/swagger.json
  - status: 200
    url: https://www.4basecare.com/sitemap.xml
  - status: 404
    url: https://www.4basecare.com/.well-known/agent-card.json
  - status: 404
    url: https://galens.4basecare.com/.well-known/security.txt
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=4basecare
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: 4baseCare is a precision oncology company founded in 2018, headquartered in Bengaluru, India with operations in Singapore, that combines next-generation-sequencing comprehensive genomic profiling with AI-driven clinical decision support to personalize cancer treatment. Its portfolio spans the TARGT family of tissue, liquid-biopsy and dual-source (SoLiQ) panels, germline and HRD testing, the OncoTwin AI insights layer, a Global Cancer Diversity Atlas of 30,000+ genomic profiles, molecular tumor board support, and the Oncobuddy patient program. Clinical results and decision support are delivered to oncologists through the Galens web portal at galens.4basecare.com. The company is Illumina Accelerator backed and closed a Series B round in 2024. As of the 2026-09-05 probe it publishes no developer program, no API documentation and no machine-readable API contract; the only API-shaped host, api.4basecare.com, is the private CodeIgniter application backend behind the Galens single-page
  app.
image: https://cdn.prod.website-files.com/68c7a1b38962ad22082ae3d4/6926b5f899d2743a3861d270_OpenGraph.jpg
layout: provider
modified: '2026-09-05'
name: 4baseCare
nav: Providers
network: true
overview: '4baseCare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Precision Oncology, Genomics, Healthcare, Cancer, and Diagnostics.


  4baseCare''s developer surface includes support, engineering blog, and 17 more developer resources.'
plans:
- name: 4Basecare Plans Pricing
  plan_count: 0
  slug: 4basecare-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: 4Basecare Rate Limits
  slug: 4basecare-rate-limits
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 4Basecare Domain Security
  slug: 4basecare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 4basecare
tags:
- Precision Oncology
- Genomics
- Healthcare
- Cancer
- Diagnostics
- Artificial Intelligence
- Life Sciences
- Clinical Decision Support
- Next Generation Sequencing
- India
website: https://www.4basecare.com/
---
