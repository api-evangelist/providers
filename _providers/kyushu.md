---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Live OAI-PMH 2.0 metadata harvesting interface for the Kyushu University Institutional Repository (QIR), run by the Kyushu University Library. Returns scholarly metadata in the JPCOAR schema (metadata
  name: Kyushu University Institutional Repository (QIR) OAI-PMH
  slug: qir-oai-pmh
- description: 'Quarterly full-metadata TSV exports for Kyushu University Library digital collections, distributed through the Handle system. Covers the institutional repository (QIR) as well as rare materials, seal '
  name: QIR / Kyushu University Collections Bulk Metadata (TSV via Handle)
  slug: qir-bulk-tsv
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kyushu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kyushu-u.ac.jp/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.lib.kyushu-u.ac.jp/ja/metadata
- group: build
  title: ''
  type: GitHub
  url: https://github.com/RIIT-KyushuUniv
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/kyushu-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/kyushu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kyushu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kyushu-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Kyushu University (九州大学) is a national research university in Fukuoka, Japan, ranked #167 in the QS World University Rankings 2025. Its public, programmatic footprint is concentrated in the university library, which operates the Kyushu University Institutional Repository (QIR) and exposes scholarly metadata over a live OAI-PMH 2.0 interface using the JPCOAR schema, alongside quarterly bulk TSV downloads via the Handle system. Other institutional surfaces — the Elsevier Pure research portal and the Academic Staff researcher database — are public for browsing but do not document an open API. There is no central institution-wide developer portal; this profile catalogs only the endpoints that could be verified live.'
finops:
- name: Kyushu Finops
  service_category: Education
  slug: kyushu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kyushu.png
jsonld:
- class_count: 28
  name: Kyushu Context
  property_count: 1
  slug: kyushu-context
layout: provider
modified: '2026-06-03'
name: Kyushu University
nav: Providers
network: true
overview: 'Kyushu University publishes 1 API on the [APIs.io](https://apis.io/) network: Institutional Repository (QIR) OAI-PMH. Tagged areas include Education, Higher Education, University, Research, and Library.


  The Kyushu University catalog on APIs.io includes 1 JSON-LD context.


  Kyushu University''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Kyushu Plans Pricing
  plan_count: 2
  slug: kyushu-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 1
  name: Kyushu Rate Limits
  slug: kyushu-rate-limits
score:
  band: thin
  composite: 28.2
  delta: -3.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 45.2
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 32.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kyushu/refs/heads/main/screenshots/kyushu-2026-06-20T184233.png
security:
- kind: domain-security
  name: Kyushu Domain Security
  slug: kyushu-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: kyushu
tags:
- Education
- Higher Education
- University
- Research
- Library
- Institutional Repository
- OAI-PMH
- Open Access
- Japan
website: https://www.kyushu-u.ac.jp/en/
---
