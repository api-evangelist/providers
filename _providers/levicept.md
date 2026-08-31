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
  url: security/levicept-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://levicept.com/
- group: company
  title: ''
  type: About
  url: https://levicept.com/about/
- group: company
  title: ''
  type: Blog
  url: https://levicept.com/news/
- group: operate
  title: ''
  type: Support
  url: https://levicept.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://levicept.com/privacy-policy/
- group: company
  title: ''
  type: Investors
  url: https://levicept.com/investors/
- group: other
  title: ''
  type: Team
  url: https://levicept.com/team/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/levicept-ltd/
coverage:
  checked: '2026-08-25'
  detail: Levicept Ltd is a clinical-stage biopharma developing the LEVI-04 biologic for osteoarthritis pain; its entire web presence is an eleven-page WordPress corporate site (about/science/trials/team/investors/news/contact) with no developer, API or integration page, and STEP 0b contract discovery on both levicept.com and www.levicept.com returned 404 for every OpenAPI, GraphQL, MCP, agent-card and /.well-known path.
  evidence:
  - status: 200
    url: https://levicept.com/
  - status: 404
    url: https://levicept.com/developers
  - status: 404
    url: https://levicept.com/openapi.json
  - status: 404
    url: https://levicept.com/graphql
  - status: 404
    url: https://levicept.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/levicept
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: 'Levicept Ltd is a UK-based clinical-stage biotechnology company headquartered at Innovation House, Discovery Park in Sandwich, Kent, developing LEVI-04, a fully human chimeric fusion protein combining the Fc fragment of human immunoglobulin G1 with the p75 neurotrophin receptor (p75NTR) for the treatment of chronic pain. LEVI-04 is a first-in-class neurotrophin-3 (NT-3) inhibitor designed to restore neurotrophin homeostasis and deliver analgesia without the use-limiting side effects — notably rapidly progressive osteoarthritis — seen with anti-NGF antibodies. The company completed a 510+ participant Phase II study in osteoarthritis of the knee (NCT05618782) that met all primary and secondary endpoints, published the results in The Lancet in March 2026, and had its IND accepted by the US FDA in January 2026. Levicept is backed by Medicxi, Pfizer Ventures, Gilde Healthcare, Advent Life Sciences and Innovate UK. Levicept is a therapeutics developer, not a software vendor: it operates
  a WordPress corporate website and publishes no API, SDK, developer portal or machine-readable contract of any kind.'
image: https://levicept.com/wp-content/uploads/2024/04/logo-1.png
layout: provider
modified: '2026-08-25'
name: Levicept
nav: Providers
network: true
overview: 'Levicept is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Therapeutics.


  Levicept''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 3
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Levicept Domain Security
  slug: levicept-domain-security
  summary_line: TLSv1.3 · DMARC
slug: levicept
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Therapeutics
- Clinical Trials
- Chronic Pain
- Osteoarthritis
- United Kingdom
website: https://levicept.com/
---
