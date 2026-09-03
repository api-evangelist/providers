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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.vektormedical.com/
- group: operate
  title: ''
  type: Support
  url: https://www.vektormedical.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.vektormedical.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vektormedical.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vektormedical.com/privacypolicy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vektor-Medical
- group: design
  title: ''
  type: Conformance
  url: conformance/vektor-medical-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/vektor-medical-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vektor-medical-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vektor-medical-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vektor-medical-llms.txt
coverage:
  checked: '2026-09-02'
  detail: 'Vektor Medical ships FDA-cleared vMap software but exposes no developer surface at all: www.vektormedical.com is a 13-page Webflow marketing site whose own sitemap has no /developers, /docs or /api page, every API-shaped and /.well-known path 404s, the GitHub org github.com/Vektor-Medical has 0 public repositories, and the only non-marketing host in certificate transparency, vmark.vektormedical.com, refuses connections on TCP/443.'
  evidence:
  - status: 404
    url: https://www.vektormedical.com/developers
  - status: 404
    url: https://www.vektormedical.com/openapi.json
  - status: 404
    url: https://www.vektormedical.com/.well-known/api-catalog
  - status: 200
    url: https://www.vektormedical.com/sitemap.xml
  - note: TCP/443 closed or filtered; no HTTP response. One bounded attempt, not retried.
    status: 0
    url: https://vmark.vektormedical.com/
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: Vektor Medical is a San Diego based medical technology company whose vMap system is an FDA-cleared and CE-marked, AI-based arrhythmia mapping solution. vMap analyzes standard 12-lead ECG data and produces beat-by-beat 2D and 3D cardiac source maps across all four chambers of the heart in about a minute, without requiring an invasive catheter-based mapping procedure. Electrophysiologists use it for triage, procedural planning and ablation guidance across focal and fibrillation-type arrhythmias and atrial and ventricular pacing. The product is delivered as Software as a Medical Device to hospitals and health systems under clinical agreements. Vektor Medical publishes no public developer program, API reference, or machine-readable API contract.
image: https://cdn.prod.website-files.com/5db9a6ed1744c7a1b2239493/64ff84ee4ddb658f592864ef_vmap-opengraph.png
layout: provider
modified: '2026-09-02'
name: Vektor Medical
nav: Providers
network: true
overview: 'Vektor Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Cardiology, and Electrophysiology.


  Vektor Medical''s developer surface includes support, engineering blog, and 9 more developer resources.'
plans:
- name: Vektor Medical Plans Pricing
  plan_count: 0
  slug: vektor-medical-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Vektor Medical Rate Limits
  slug: vektor-medical-rate-limits
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 5.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: domain-security
  name: Vektor Medical Domain Security
  slug: vektor-medical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vektor-medical
tags:
- Company
- Medical Devices
- Healthcare
- Cardiology
- Electrophysiology
- Artificial Intelligence
- Software as a Medical Device
- Diagnostics
website: https://www.vektormedical.com/
---
