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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nextpoint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nextpointtx.com/
- group: company
  title: ''
  type: About
  url: https://nextpointtx.com/about-us/
- group: company
  title: ''
  type: News
  url: https://nextpointtx.com/news-publications/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nextpointtx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nextpointtx.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nextpoint-therapeutics
coverage:
  checked: '2026-08-26'
  detail: NextPoint Therapeutics is a clinical-stage oncology drug developer whose entire public surface is a seven-page WordPress marketing site (home, about, pipeline, science, news, terms, privacy) with no developer, API or documentation section; api./developer./docs./ portal./app./mcp.nextpointtx.com do not resolve in DNS, no GitHub organization exists under nextpointtx or nextpoint-therapeutics, and every spec path returns the site's 158,191-byte homepage catch-all byte-identical to a nonsense control URL.
  evidence:
  - status: 200
    url: https://nextpointtx.com/openapi.json
  - status: 404
    url: https://nextpointtx.com/llms.txt
  - status: 404
    url: https://nextpointtx.com/.well-known/security.txt
  - status: 200
    url: https://nextpointtx.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/nextpoint-therapeutics
  - status: 200
    url: https://nextpointtx.com/about-us/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: NextPoint Therapeutics, Inc. is a clinical-stage immuno-oncology biotechnology company headquartered at 238 Main Street, Cambridge, Massachusetts. Founded in 2019-2020 out of MPM Capital on discoveries by Gordon Freeman (Dana-Farber Cancer Institute) and XingXing Zang (Albert Einstein College of Medicine), it develops first-in-class precision therapeutics against the B7-H7/HHLA2 - KIR3DL3 immune checkpoint axis, combining direct tumor-cell killing with immunomodulation in a single molecule. Its pipeline spans three modalities - NPX887, an anti-B7-H7 monoclonal antibody with TMIGD2 co-stimulation and enhanced ADCC currently in Phase 1; NPX372, a 2:1 bispecific B7-H7 x CD3 T cell engager; and NPX125, a DAR8 antibody drug conjugate - all guided by a biomarker-driven patient selection strategy. Investors include Leaps by Bayer, Sanofi Ventures, MPM BioImpact, Catalio Capital, Dana-Farber, Invus, Arkin, Simcere, SixtyDegree and Pagoda Tree; its shares trade on private secondary marketplaces.
  It is a therapeutics developer rather than a software company and publishes no API, SDK, developer program or machine-readable specification.
image: https://nextpointtx.com/wp-content/uploads/2025/08/logo-nextpoint.png
layout: provider
modified: '2026-08-26'
name: NextPoint
nav: Providers
network: true
overview: 'NextPoint is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Immunotherapy.


  NextPoint''s developer surface includes product news and 6 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
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
  name: Nextpoint Domain Security
  slug: nextpoint-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nextpoint
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Immunotherapy
- Precision Medicine
- Clinical Stage
- Drug Development
- Healthcare
- Life Sciences
website: https://nextpointtx.com/
---
