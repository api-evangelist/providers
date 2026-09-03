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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rapport-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rapportrx.com/
- group: company
  title: ''
  type: About
  url: https://www.rapportrx.com/about/
- group: operate
  title: ''
  type: Support
  url: https://www.rapportrx.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rapportrx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rapportrx.com/terms-of-use/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.rapportrx.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rapport-therapeutics/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rapport-therapeutics-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Rapport Therapeutics is a clinical-stage CNS drug developer whose product is a molecule pipeline (RAP-219 plus two discovery nAChR programs); www.rapportrx.com is a seventeen-page WordPress marketing site where every contract-discovery path — /openapi.json, /swagger.json, /api-docs, /graphql, /llms.txt and all seven /.well-known/ paths — returns 404, no api/developer/docs subdomain resolves, the RAP platform is an internal discovery capability that is never exposed, and the only machine-readable surface on the domain is the CMS's default, unadvertised /wp-json/ index describing pages and posts rather than a product API.
  evidence:
  - status: 404
    url: https://www.rapportrx.com/openapi.json
  - status: 404
    url: https://www.rapportrx.com/graphql
  - status: 404
    url: https://www.rapportrx.com/.well-known/api-catalog
  - status: 404
    url: https://www.rapportrx.com/.well-known/agent-card.json
  - status: 404
    url: https://www.rapportrx.com/llms.txt
  - status: 0
    url: https://developer.rapportrx.com/
  - status: 0
    url: https://investors.rapportrx.com/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Rapport Therapeutics, Inc. (Nasdaq: RAPP) is a clinical-stage biotechnology company headquartered in Boston, Massachusetts with research operations in San Diego, California, founded in 2022 and taken public in a $174 million IPO in June 2024. Rapport develops precision small-molecule medicines for central nervous system disorders using its proprietary RAP technology platform, which pairs human genetics with functional proteomics to identify receptor-associated proteins that confer neuroanatomical specificity — the goal being drugs that act only where the disease circuit lives rather than across the whole brain. Its lead clinical candidate, RAP-219, is a selective negative allosteric modulator of TARP-gamma-8-associated AMPA receptors in development for focal onset seizures, peripheral neuropathic pain and bipolar disorder, behind two discovery-stage nicotinic acetylcholine receptor programs targeting alpha-6 (chronic pain) and alpha-9-alpha-10 (hearing disorders). Rapport is
  a therapeutics developer, not a software vendor: the RAP platform is an internal discovery capability and the company publishes no developer program, no public API and no machine-readable API contract.'
image: https://www.rapportrx.com/wp-content/uploads/2023/02/rapportrx-yoast-logo.jpg
layout: provider
modified: '2026-08-26'
name: Rapport Therapeutics
nav: Providers
network: true
overview: 'Rapport Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Healthcare.


  Rapport Therapeutics'' developer surface includes support and 8 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rapport-therapeutics/refs/heads/main/screenshots/rapport-therapeutics-2026-09-02T152858.png
security:
- kind: domain-security
  name: Rapport Therapeutics Domain Security
  slug: rapport-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rapport-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Healthcare
- Neuroscience
- Central Nervous System
- Drug Discovery
- Clinical Trials
- Epilepsy
website: https://www.rapportrx.com/
---
