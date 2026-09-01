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
  url: security/sherlock-biosciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sherlock.bio/
- group: other
  title: ''
  type: ParentCompany
  url: https://orasure.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SherlockBiosciences
- group: build
  title: ''
  type: Packages
  url: packages/sherlock-biosciences-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sherlock-biosciences-llms.txt
coverage:
  checked: '2026-08-27'
  detail: Sherlock Biosciences was acquired by OraSure Technologies in December 2024 and fully absorbed; its own domain sherlock.bio now returns a bare 301 to orasure.com, and every contract-discovery and .well-known path probed on sherlock.bio, orasure.com and www.orasure.com returned 404, leaving a molecular-diagnostics company that never ran a developer program with no surviving API surface of any kind.
  evidence:
  - status: 301
    url: https://sherlock.bio/
  - status: 404
    url: https://sherlock.bio/openapi.json
  - status: 404
    url: https://sherlock.bio/.well-known/agent-card.json
  - status: 404
    url: https://orasure.com/openapi.json
  - status: 404
    url: https://www.orasure.com/.well-known/api-catalog
  - status: 200
    url: https://github.com/SherlockBiosciences
  reason: defunct
  state: none
created: '2026-08-27'
description: Sherlock Biosciences is a molecular diagnostics company founded in 2019 out of the Broad Institute to commercialize SHERLOCK (Specific High-sensitivity Enzymatic Reporter unLOCKing), the CRISPR-based nucleic-acid detection method developed in the Zhang lab, alongside INSPECTR, an ambient-temperature synthetic-biology amplification platform. In May 2020 it received the first FDA Emergency Use Authorization ever granted to a CRISPR-based diagnostic, for SARS-CoV-2. The company developed disposable, instrument-free molecular self-tests, led by a combined Chlamydia trachomatis and Neisseria gonorrhoeae assay. OraSure Technologies acquired Sherlock Biosciences in December 2024 and absorbed it into its rapid-diagnostics portfolio; the sherlock.bio domain now permanently redirects to orasure.com. Sherlock Biosciences is a laboratory diagnostics developer and has never operated a public developer program, HTTP API, or machine-readable API contract.
layout: provider
modified: '2026-08-27'
name: Sherlock Biosciences
nav: Providers
network: true
overview: Sherlock Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Diagnostics, Molecular Diagnostics, CRISPR, Biotechnology, and Life Sciences.
random_paper: 5
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 4
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
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 4.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Sherlock Biosciences Domain Security
  slug: sherlock-biosciences-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sherlock-biosciences
tags:
- Diagnostics
- Molecular Diagnostics
- CRISPR
- Biotechnology
- Life Sciences
- Healthcare
- Infectious Disease
- Point of Care Testing
- Synthetic Biology
- Bioinformatics
- Acquired
website: https://sherlock.bio/
---
