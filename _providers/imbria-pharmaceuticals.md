---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imbria-pharmaceuticals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://imbria.com/
- group: company
  title: ''
  type: About
  url: https://imbria.com/our-story/
- group: company
  title: ''
  type: Blog
  url: https://imbria.com/investors-media/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://imbria.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://imbria.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://imbria.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://imbria.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/imbria/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/imbria-pharmaceuticals-llms.txt
coverage:
  checked: '2026-08-22'
  detail: Imbria Pharmaceuticals is a private clinical-stage biopharma developing ninerafaxstat for cardiovascular disease; imbria.com is a WordPress marketing site whose only machine-readable surface is the default WordPress core REST API at /wp-json/, and every developer-program path probed (/developers, /docs, /api, /openapi.json, /graphql, /llms.txt, /apis.json and eight /.well-known/ documents) returned the site's standard 404.
  evidence:
  - status: 404
    url: https://imbria.com/developers
  - status: 404
    url: https://imbria.com/openapi.json
  - status: 404
    url: https://imbria.com/.well-known/api-catalog
  - status: 404
    url: https://imbria.com/.well-known/agent-card.json
  - status: 200
    url: https://imbria.com/wp-json
  - status: 404
    url: https://github.com/imbria
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: Imbria Pharmaceuticals is a private, clinical-stage biopharmaceutical company based in the Boston area that is developing novel cardiovascular therapies targeting cardiac energy metabolism. Its lead candidate, ninerafaxstat, is a first-in-class partial fatty acid oxidation (pFOX) inhibitor designed to shift myocardial substrate utilization toward glucose oxidation, generating more ATP per unit of oxygen consumed and improving cardiac metabolic efficiency without affecting heart rate, rhythm, ejection fraction or blood pressure. Ninerafaxstat is in the global FORTITUDE-HCM Phase 2b trial (NCT07023614) for symptomatic non-obstructive hypertrophic cardiomyopathy (nHCM), which has no approved treatments, and holds FDA Orphan Drug Designation for that indication; a Phase 2b in cardiometabolic HFpEF is planned. The company is backed by RA Capital, SV Health Investors, Deep Track Capital, Catalio Capital Management, AN Ventures and Cytokinetics. Imbria is a therapeutics developer,
  not a software vendor, and publishes no public API, developer portal, SDK or machine-readable API contract.
image: https://imbria.com/wp-content/uploads/2025/09/imbria_logo-1.svg
layout: provider
modified: '2026-08-22'
name: Imbria Pharmaceuticals
nav: Providers
network: true
overview: 'Imbria Pharmaceuticals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Biotechnology, Life Sciences, and Cardiovascular.


  Imbria Pharmaceuticals'' developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imbria-pharmaceuticals/refs/heads/main/screenshots/imbria-pharmaceuticals-2026-09-02T145833.png
security:
- kind: domain-security
  name: Imbria Pharmaceuticals Domain Security
  slug: imbria-pharmaceuticals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: imbria-pharmaceuticals
tags:
- Company
- Pharmaceuticals
- Biotechnology
- Life Sciences
- Cardiovascular
- Clinical Trials
- Drug Development
- Healthcare
- Therapeutics
website: https://imbria.com/
---
