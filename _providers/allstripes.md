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
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allstripes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allstripes.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/allstripes
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/rdmd
coverage:
  checked: '2026-08-06'
  detail: PicnicHealth acquired AllStripes on 2023-10-23 and retired the brand; allstripes.com and app.allstripes.com now blanket-301 every path — /openapi.json, /swagger.json, /api-docs, /llms.txt and every /.well-known/ probe alike — to the picnichealth.com homepage, and there is no allstripes GitHub organization or published package anywhere.
  evidence:
  - status: 301
    url: https://allstripes.com/openapi.json
  - status: 301
    url: https://allstripes.com/.well-known/agent-card.json
  - status: 301
    url: https://allstripes.com/llms.txt
  - status: 301
    url: https://app.allstripes.com/
  - status: 404
    url: https://github.com/allstripes
  - status: 404
    url: https://registry.npmjs.org/allstripes
  reason: defunct
  state: none
created: '2026-08-06'
description: AllStripes was a San Francisco healthcare technology company, founded in 2017 as RDMD by Nancy Yu and Onno Faber, that built a research platform dedicated to rare disease. It retrieved, digitized and de-identified patients' medical records into regulatory-ready real-world evidence for biopharma drug development, and paired that with a patient application through which families affected by conditions such as Batten disease, Hunter syndrome and sickle cell anemia could participate in treatment research from home. The company raised roughly $74M in venture funding, including a $50M Series B in August 2021 led by Lux Capital with JAZZ Venture Partners, Spark Capital, Medidata, McKesson Ventures and Maveron. PicnicHealth acquired AllStripes on October 23, 2023 and folded the platform into its own; the AllStripes brand has since been retired, and allstripes.com and app.allstripes.com now issue blanket 301 redirects to picnichealth.com. AllStripes never published a public developer
  portal, REST/OpenAPI contract, SDK, or webhook surface, and no such surface survives the acquisition.
layout: provider
modified: '2026-08-06'
name: AllStripes
nav: Providers
network: true
overview: AllStripes is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Rare Disease, Real-World Data, and Real-World Evidence.
random_paper: 20
score:
  band: minimal
  composite: 2.9
  delta: -2.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allstripes/refs/heads/main/screenshots/allstripes-2026-08-07T161233.png
security:
- kind: domain-security
  name: Allstripes Domain Security
  slug: allstripes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: allstripes
tags:
- Company
- Health
- Rare Disease
- Real-World Data
- Real-World Evidence
- Life Sciences
- Clinical Research
- Medical Records
- Acquired
website: https://allstripes.com/
---
