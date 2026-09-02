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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/third-arc-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thirdarcbio.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thirdarcbio.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thirdarcbio.com/terms-of-service/
- group: company
  title: ''
  type: Blog
  url: https://thirdarcbio.com/news/
- group: operate
  title: ''
  type: Support
  url: mailto:info@thirdarcbio.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/third-arc-bio/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/third-arc-bio-llms.txt
coverage:
  checked: '2026-08-30'
  detail: Third Arc Bio is a clinical-stage antibody therapeutics developer; thirdarcbio.com is a Gatsby static marketing site with only science, pipeline, team, news and policy pages, and every contract-discovery path (/openapi.json, /swagger.json, /api-docs, /docs, /developers, /api, /graphql, /llms.txt) plus every /.well-known/ document returns the site's 404 body, while api., developer., docs. and mcp. subdomains do not resolve in DNS.
  evidence:
  - status: 200
    url: https://thirdarcbio.com/
  - status: 404
    url: https://thirdarcbio.com/openapi.json
  - status: 404
    url: https://thirdarcbio.com/developers
  - status: 404
    url: https://thirdarcbio.com/.well-known/agent-card.json
  - status: 404
    url: https://thirdarcbio.com/.well-known/api-catalog
  reason: not-a-software-company
  state: none
created: '2026-08-30'
description: Third Arc Bio is a clinical-stage biotechnology company headquartered in Lower Gwynedd, Pennsylvania, developing multifunctional antibodies that build immune synapses to precisely activate or inhibit T cells. Its ARCStim platform targets solid tumors and its ARCTag platform pursues tissue-specific precision immune regulation for immunology and inflammation (I&I) indications; lead program ARC101 is a bispecific T-cell engager in a Phase 1 trial in patients with CLDN6-expressing solid tumors. The company launched in 2022 with seed financing from Omega Funds, raised an oversubscribed $165M Series A, and closed a $52M Series A extension in February 2026 with Andreessen Horowitz joining the syndicate. Third Arc Bio publishes no public API, developer portal, SDK or machine-readable specification — it is a therapeutics developer, not a software vendor.
image: https://thirdarcbio.com/thirdarc-og-image.png
layout: provider
modified: '2026-08-30'
name: Third Arc Bio
nav: Providers
network: true
overview: 'Third Arc Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, Antibodies, and Oncology.


  Third Arc Bio''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Third Arc Bio Domain Security
  slug: third-arc-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: third-arc-bio
tags:
- Company
- Biotechnology
- Therapeutics
- Antibodies
- Oncology
- Immunology
- Life Sciences
- Clinical Stage
website: https://thirdarcbio.com/
---
