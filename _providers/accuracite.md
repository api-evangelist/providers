---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'Synchronous REST API for citation verification and claim-to-source lookup. Two operations, both POST and both keyed by an X-API-Key header: /api/v1/verify checks a citation string (or a bare URL, or a'
  name: AccuraCite API
  slug: accuracite-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accuracite-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accuracite-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/accuracite-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/accuracite-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/accuracite-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/accuracite-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/accuracite-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/accuracite-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/accuracite-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/accuracite-lifecycle.yml
- group: docs
  title: ''
  type: Documentation
  url: https://accuracite.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://accuracite.com/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://accuracite.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://accuracite.com/blog
- group: operate
  title: ''
  type: Support
  url: https://accuracite.com/feedback
- group: start
  title: ''
  type: SignUp
  url: https://accuracite.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://accuracite.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accuracite.com/privacy
created: '2026-08-31'
description: 'AccuraCite verifies bibliographies and finds real citations, catching AI-hallucinated references before they are published. Every citation supplied as raw text, BibTeX, RIS or an uploaded PDF is checked against eight academic indexes -- OpenAlex, Crossref, Semantic Scholar, PubMed, DBLP, arXiv, CORE and Google Scholar -- and returned as verified, mismatch or not_found, with the matched bibliographic record and a field-level list of what disagreed. A second surface runs the other direction: given a claim, it returns real papers whose abstracts actually support it rather than papers whose titles merely look related. Both are exposed over a small synchronous REST API (POST /api/v1/verify and POST /api/v1/generate) keyed by an X-API-Key header and metered from a shared monthly credit pool. AccuraCite is a solo-founder product built by a computer-science PhD after finding fabricated citations in a co-authored, partly AI-drafted paper.'
image: https://accuracite.com/static/img/og-image.png
layout: provider
modified: '2026-08-31'
name: AccuraCite
nav: Providers
network: true
overview: 'AccuraCite publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Citations, Research, Bibliography, Academic, and Verification.


  AccuraCite''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, signup flow, and 11 more developer resources.'
plans:
- name: Accuracite Plans Pricing
  plan_count: 5
  slug: accuracite-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Accuracite Rate Limits
  slug: accuracite-rate-limits
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 37.7
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/screenshots/accuracite-2026-09-02T144112.png
security:
- kind: authentication
  name: Accuracite Authentication
  slug: accuracite-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Accuracite Domain Security
  slug: accuracite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: accuracite
tags:
- Citations
- Research
- Bibliography
- Academic
- Verification
- AI Safety
---
