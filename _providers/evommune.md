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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.evommune.com/
- group: company
  title: ''
  type: About
  url: https://www.evommune.com/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://www.evommune.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.evommune.com/wp-content/uploads/2023/12/Evommune_privacy-statement_for_website.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.evommune.com/wp-content/uploads/2023/12/Evommune_privacy-statement_for_website.pdf
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.evommune.com/
- group: operate
  title: ''
  type: PressReleases
  url: https://ir.evommune.com/news-events/press-releases
- group: company
  title: ''
  type: Careers
  url: https://www.evommune.com/job-openings/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/evommune/
- group: other
  title: ''
  type: Pipeline
  url: https://www.evommune.com/development-pipeline/
- group: other
  title: ''
  type: Publications
  url: https://www.evommune.com/publications-posters/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evommune-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evommune-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/evommune_stock/
coverage:
  checked: '2026-08-12'
  detail: 'Evommune is a clinical-stage biopharmaceutical company (Nasdaq: EVMN) whose entire public surface is a WordPress marketing site and a hosted investor-relations portal — there is no developer section, no GitHub organization, no package on any registry, and every OpenAPI/GraphQL/MCP/agent-card path probed on both hosts returned 404; the only HTTP 200 API-shaped response is the stock WordPress REST API at /wp-json/, which is default CMS infrastructure rather than a product Evommune publishes.'
  evidence:
  - status: 404
    url: https://www.evommune.com/openapi.json
  - status: 404
    url: https://www.evommune.com/.well-known/agent-card.json
  - status: 404
    url: https://ir.evommune.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/evommune
  - status: 200
    url: https://www.evommune.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: 'Evommune, Inc. (Nasdaq: EVMN) is a clinical-stage biopharmaceutical company headquartered in Palo Alto, California, discovering and developing therapies that target the key drivers of chronic inflammatory disease. Founded in 2020 by the team behind Dermira, the company applies a human tissue-based translational approach to immunology and is advancing a clinical pipeline that includes EVO756, an oral small-molecule MRGPRX2 antagonist in Phase 2b development for chronic spontaneous urticaria and migraine prophylaxis, and an IL-18 binding protein fusion program licensed from AprilBio. Evommune publishes no developer program, no public API and no machine-readable API contract; its public web presence is a WordPress marketing site plus a hosted investor-relations portal.'
image: https://www.evommune.com/wp-content/uploads/2023/12/Evommune-blue-logo.svg
layout: provider
modified: '2026-08-12'
name: Evommune
nav: Providers
network: true
overview: Evommune is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Immunology.
random_paper: 15
score:
  band: minimal
  composite: 9.8
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Evommune Domain Security
  slug: evommune-domain-security
  summary_line: TLSv1.3 · DMARC
slug: evommune
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Immunology
- Drug Development
- Clinical Trials
- Healthcare
website: https://www.evommune.com/
---
