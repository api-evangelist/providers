---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/immunis-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/immunis-llms.txt
- group: company
  title: ''
  type: Website
  url: https://immunisbiomedical.com/
- group: operate
  title: ''
  type: PressReleases
  url: https://immunisbiomedical.com/press-releases/
- group: operate
  title: ''
  type: Contact
  url: https://immunisbiomedical.com/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/immunisbiomedical/
coverage:
  checked: '2026-08-23'
  detail: Immunis, Inc. is a clinical-stage biotech developing secretome therapeutics; its full page inventory (46 pages, read from the site's own sitemap) contains no developer, API or documentation page, and every /openapi.json, /api-docs, /graphql, /llms.txt and /.well-known/* probe on immunisbiomedical.com returned the WordPress 404 page — the only machine-readable endpoint on the host is the site's default WordPress CMS REST API at /wp-json/.
  evidence:
  - status: 404
    url: https://immunisbiomedical.com/openapi.json
  - status: 404
    url: https://immunisbiomedical.com/.well-known/api-catalog
  - status: 404
    url: https://immunisbiomedical.com/llms.txt
  - status: 404
    url: https://immunisbiomedical.com/developers
  - status: 200
    url: https://immunisbiomedical.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: 'Immunis, Inc. is a private, clinical-stage biotechnology company headquartered in Irvine, California, developing immunomodulatory secretome biologics — the mixture of proteins and factors secreted by stem cells, rather than the cells themselves — as a treatment for age- and disease-related immune decline. Its lead candidate, IMM01-STEM, is under study in the STEM-MYO Phase 1/2a trial for muscle atrophy and sarcopenia, alongside a STEM-META Phase 2 program and a STEM-K9 veterinary program. Immunis is a therapeutics developer, not a software company: it publishes no developer portal, API, SDK, webhook surface, or machine-readable API contract of any kind. Its entire public surface is a WordPress marketing and clinical-trial-recruitment site whose only machine-readable endpoint is the default WordPress REST API at /wp-json/, which serves the CMS of that site and is not an Immunis API product.'
image: https://immunisbiomedical.com/wp-content/uploads/2026/06/ImmunisLogo.png
layout: provider
modified: '2026-08-23'
name: Immunis
nav: Providers
network: true
overview: Immunis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Therapeutics, and Clinical Trials.
random_paper: 14
score:
  band: minimal
  composite: 4.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: domain-security
  name: Immunis Domain Security
  slug: immunis-domain-security
  summary_line: TLSv1.3
slug: immunis
tags:
- Company
- Biotechnology
- Life Sciences
- Therapeutics
- Clinical Trials
- Regenerative Medicine
- Healthcare
- Longevity
- Sarcopenia
website: https://immunisbiomedical.com/
---
