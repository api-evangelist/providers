---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://waiv.com/
- group: docs
  title: ''
  type: Documentation
  url: https://waiv.com/precision-testing/destra
- group: operate
  title: ''
  type: Support
  url: https://waiv.com/contact
- group: company
  title: ''
  type: Blog
  url: https://waiv.com/news#Blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wearewaiv
- group: commercial
  title: ''
  type: TermsOfService
  url: https://waiv.com/policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://waiv.com/policies/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://waiv.com/news/waiv-achieves-dual-ce-marking-under-ivdr-propelling-ai-precision-testing-for-breast-and-colorectal-cancer-for-clinical-routine
- group: design
  title: ''
  type: Conformance
  url: conformance/waiv-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/waiv-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/waiv-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/waiv-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/waiv-rate-limits.yml
coverage:
  checked: '2026-08-17'
  detail: Waiv advertises a "Destra API" for wiring its CE-IVD marked AI pathology tests into a laboratory IMS, but the "Get Destra API" button on the Destra product page links to a single general "Get in contact" sales form with no developer or integration option, and no docs host, developer portal, or specification exists on any Waiv domain.
  evidence:
  - status: 200
    url: https://waiv.com/precision-testing/destra
  - status: 200
    url: https://waiv.com/contact
  - status: 404
    url: https://waiv.com/openapi.json
  - status: 404
    url: https://waiv.com/docs
  - status: 404
    url: https://waiv.com/llms.txt
  - status: 404
    url: https://waiv.com/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-08-17'
description: Waiv is a Paris-based AI precision-testing company spun out of Owkin (formerly Owkin Dx) that builds clinically validated, AI-powered diagnostic tests for oncology and digital pathology. Its products — RlapsRisk BC (breast-cancer distant-relapse risk), the MSIntuit Suite (MSI/dMMR pre-screening in colorectal, gastric and endometrial cancer), BRCAura RUO (gBRCA pre-screening) and TLS Detect — read routine H&E whole-slide images to accelerate biomarker detection, outcome prediction and treatment-response assessment. The tests are delivered through Destra, an AI-native digital pathology platform that lab and clinician users reach in the browser and that laboratories can wire into an existing IMS/LIS through the Destra API. RlapsRisk BC and MSIntuit CRC hold dual CE-IVD marking under the EU IVDR. Waiv raised $33M led by OTB Ventures and Alpha Intelligence Capital, with Serena, Karista and SistaFund participating, and later closed $35M total with CRB Health Tech. The Destra API is
  advertised on the product page but is sales-gated — there is no public developer portal, reference, or machine-readable specification.
image: https://cdn.prod.website-files.com/693aa5958f830a8ecab1c1eb/69aef2dbc9e80a879ba31dc1_open-graph-waiv-home.jpg
layout: provider
modified: '2026-08-17'
name: Waiv
nav: Providers
network: true
overview: 'Waiv is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Data, Artificial Intelligence, Healthcare, and Digital Pathology.


  Waiv''s developer surface includes documentation, support, engineering blog, and 10 more developer resources.'
plans:
- name: Waiv Plans Pricing
  plan_count: 0
  slug: waiv-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Waiv Rate Limits
  slug: waiv-rate-limits
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 18.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/waiv/refs/heads/main/screenshots/waiv-2026-09-02T170400.png
security:
- kind: domain-security
  name: Waiv Domain Security
  slug: waiv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: waiv
tags:
- Company
- Ai Data
- Artificial Intelligence
- Healthcare
- Digital Pathology
- Oncology
- Medical Diagnostics
- Precision Medicine
- Biomarkers
- Machine-Learning
- Life Sciences
- Medical Imaging
website: https://waiv.com/
---
