---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.6
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The read-only WordPress REST content surface behind www.jnanatx.com — news posts (62), corporate pages (9), media (376), post categories (7), the `team` custom post type (9 profiles) and its `team-dep
  name: Jnana Therapeutics Content API
  slug: jnana-therapeutics-content-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jnana-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jnanatx.com/
- group: other
  title: ''
  type: Platform
  url: https://www.jnanatx.com/rapid-platform/
- group: other
  title: ''
  type: Programs
  url: https://www.jnanatx.com/programs/
- group: other
  title: ''
  type: Team
  url: https://www.jnanatx.com/team/
- group: company
  title: ''
  type: News
  url: https://www.jnanatx.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.jnanatx.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://www.jnanatx.com/join-us/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.jnanatx.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jnanatx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jnanatx.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jnana-therapeutics/
- group: other
  title: ''
  type: X
  url: https://x.com/jnanatx
- group: other
  title: ''
  type: ParentCompany
  url: https://www.otsuka.co.jp/en/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/jnana-therapeutics_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/jnana-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jnana-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jnana-therapeutics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jnana-therapeutics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jnana-therapeutics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jnana-therapeutics-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/jnana-therapeutics-content-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/jnana-therapeutics-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jnana-therapeutics-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jnana-therapeutics-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jnana-therapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-23'
description: 'Jnana Therapeutics Inc. is a biotechnology company headquartered at One Design Center Place, Suite 19-400, Boston, Massachusetts, that built RAPID — Reactive Affinity Probe Interaction Discovery — a next-generation chemoproteomics platform for discovering small-molecule medicines against target classes that conventional screening has struggled to drug, including SLC transporters, transcription factors, signaling scaffold proteins, phosphatases, GPCRs and helicases. RAPID runs in living cells: a proprietary Reactive Affinity Probe library covalently labels druggable pockets on a validated target, and a proprietary detection technology then screens large drug-like compound libraries for binders that displace the probe, yielding allosteric inhibitors, localization modulators and molecular glues without iterative structural biology. Its internal pipeline focuses on phenylketonuria (PKU) — where JNT-517, an oral inhibitor acting at a cryptic allosteric site on the SLC6A19 transporter,
  reached Phase 1b/2 — and on immune-mediated diseases including targets such as interferon regulatory factor 3 (IRF3), alongside biopharma collaborations that include Roche. Otsuka Pharmaceutical Co., Ltd. completed its acquisition of Jnana on 23 September 2024 for $800 million plus up to $325 million in development and regulatory milestones, making Jnana a direct subsidiary of Otsuka America, Inc.; Otsuka initiated a global Phase 3 trial of repinatrabit in PKU in December 2025. Jnana Therapeutics runs no developer program and publishes no product API, developer portal, API reference or SDK. The only machine-readable surface reachable without credentials is the WordPress REST content API behind www.jnanatx.com, catalogued here.'
image: https://www.jnanatx.com/wp-content/uploads/2022/09/cropped-android-chrome-512x512-1.png
layout: provider
modified: '2026-08-23'
name: Jnana Therapeutics
nav: Providers
network: true
overview: 'Jnana Therapeutics publishes 1 API on the [APIs.io](https://apis.io/) network: Content API. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and Chemoproteomics.


  Jnana Therapeutics'' developer surface includes product news, authentication, and 25 more developer resources.'
plans:
- name: Jnana Therapeutics Plans Pricing
  plan_count: 0
  slug: jnana-therapeutics-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Jnana Therapeutics Rate Limits
  slug: jnana-therapeutics-rate-limits
score:
  band: thin
  composite: 33.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 30.3
    contract_quality: 48.3
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Jnana Therapeutics Authentication
  slug: jnana-therapeutics-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Jnana Therapeutics Domain Security
  slug: jnana-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jnana-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- Chemoproteomics
- Rare Disease
- Immunology
- Life Sciences
- Clinical Trials
- content-api
website: https://www.jnanatx.com/
---
