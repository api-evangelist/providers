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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://epicrispr.com/
- group: company
  title: ''
  type: About
  url: https://epicrispr.com/science/
- group: company
  title: ''
  type: Blog
  url: https://epicrispr.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://epicrispr.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://epicrispr.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://epicrispr.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://epicrispr.com/careers/
- group: other
  title: ''
  type: Sitemap
  url: https://epicrispr.com/sitemap_index.xml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epic-bio-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/epic-bio-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Epic Bio is Epicrispr Biotechnologies, a clinical-stage epigenetic-editing therapeutics company whose only host is a WordPress marketing site — the similarly named epic.bio belongs to Guerbet and open.epic.com belongs to Epic Systems, so neither of those API surfaces is this company's.
  evidence:
  - status: 404
    url: https://epicrispr.com/openapi.json
  - status: 404
    url: https://epicrispr.com/.well-known/agent-card.json
  - status: 404
    url: https://epicrispr.com/llms.txt
  - status: 404
    url: https://github.com/epicrispr
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: 'Epic Bio (legally Epicrispr Biotechnologies, Inc.) is a clinical-stage genetic medicines company in South San Francisco, California, founded in 2018 by Stanford CRISPR pioneer Stanley Qi, Ph.D. It develops epigenetic editing therapies that modulate gene expression without cutting DNA, built on its proprietary Gene Expression Modulation System (GEMS) platform — a combination of ultracompact DNA-binding proteins (CasMINI, CasONYX), tailored guide RNAs, and a large library of transcriptional and epigenomic modulators. Its lead program EPI-321 is in first-in-human clinical study for facioscapulohumeral muscular dystrophy (FSHD), with preclinical programs in alpha-1 antitrypsin deficiency and heterozygous familial hypercholesterolemia. The company is a therapeutics developer, not a software vendor: it publishes a corporate and scientific website but no developer program, public API, SDK, or machine-readable specification.'
image: https://epicrispr.com/wp-content/uploads/2024/11/epicrispr-logo-768x452-1.png
layout: provider
modified: '2026-08-12'
name: Epic Bio
nav: Providers
network: true
overview: 'Epic Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Genetic Medicine, Gene Editing, and CRISPR.


  Epic Bio''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Epic Bio Plans Pricing
  plan_count: 0
  slug: epic-bio-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Epic Bio Rate Limits
  slug: epic-bio-rate-limits
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/epic-bio/refs/heads/main/screenshots/epic-bio-2026-09-02T145410.png
security:
- kind: domain-security
  name: Epic Bio Domain Security
  slug: epic-bio-domain-security
  summary_line: TLSv1.3
slug: epic-bio
tags:
- Company
- Biotechnology
- Genetic Medicine
- Gene Editing
- CRISPR
- Epigenetics
- Therapeutics
- Life Sciences
- Clinical Stage
website: https://epicrispr.com/
---
