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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/syntheticgenomics
- group: build
  title: ''
  type: Packages
  url: packages/synthetic-genomics-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synthetic-genomics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/synthetic-genomics-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/synthetic-genomics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/synthetic-genomics-rate-limits.yml
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Viridos_(company)
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/synthetic-genomics_stock/
coverage:
  checked: '2026-08-29'
  detail: Viridos sold substantially all of its algae biofuel technology in Chapter 11 and had its case dismissed on 2025-11-26; viridos.com now returns a 21-byte "403 | Access blocked" page from a SiteGround default vhost on every path, behind a certificate issued for giowm1252.siteground.biz, and the legacy syntheticgenomics.com domain was dropped and is now a Canadian online-casino affiliate site.
  evidence:
  - status: 403
    url: https://viridos.com/
  - status: 403
    url: https://viridos.com/openapi.json
  - status: 403
    url: https://viridos.com/.well-known/api-catalog
  - status: 403
    url: https://dspace.bio/
  - status: 200
    url: https://github.com/syntheticgenomics
  - status: 200
    url: https://cases.stretto.com/viridos/
  reason: defunct
  state: none
created: '2026-08-29'
description: Viridos, founded in 2005 as Synthetic Genomics, Inc. by J. Craig Venter and Hamilton Smith and renamed Viridos in September 2021, was a La Jolla, California synthetic-biology company that engineered microalgae genomes to produce low-carbon-intensity biofuels, running its algal biofuel program as a long-term research partnership with ExxonMobil. The company never published an API, a developer portal, or any machine-readable contract; its only public developer surface was a GitHub organization holding two first-party open-source projects - the AGPL-licensed sgidspace deep-learning protein annotation library and a sensor calibration app - alongside seven forks of third-party tools. Viridos filed for Chapter 11 bankruptcy in the District of Delaware on 2025-04-14, sold substantially all of its algae biofuel technology to Breakthrough Energy Ventures II, L.P., and the case was dismissed on 2025-11-26. Its website has served no content since roughly October 2025.
layout: provider
modified: '2026-08-29'
name: Viridos
nav: Providers
network: true
overview: Viridos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Synthetic Biology, Biotechnology, Genomics, and Biofuels.
plans:
- name: Synthetic Genomics Plans Pricing
  plan_count: 0
  slug: synthetic-genomics-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Synthetic Genomics Rate Limits
  slug: synthetic-genomics-rate-limits
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Synthetic Genomics Domain Security
  slug: synthetic-genomics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: synthetic-genomics
tags:
- Company
- Synthetic Biology
- Biotechnology
- Genomics
- Biofuels
- Algae
- Climate Tech
- Life Sciences
- Open-Source
- Defunct
---
