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
  url: security/scg-cell-therapy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scgcell.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://sg.linkedin.com/company/scgcell
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scg-cell-therapy-llms.txt
coverage:
  checked: '2026-08-26'
  detail: SCG Cell Therapy is a clinical-stage TCR-T cell therapy developer whose only web property is an Alibaba Cloud site-builder marketing site; there is no developer portal, no api./developer./docs. subdomain resolves in DNS, and no GitHub organization exists under any spelling of the company name.
  evidence:
  - status: 200
    url: https://www.scgcell.com/
  - status: 404
    url: https://www.scgcell.com/openapi.json
  - status: 404
    url: https://www.scgcell.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/scgcell
  - status: 429
    url: https://www.scgcell.com/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: SCG Cell Therapy Pte. Ltd. is a clinical-stage biotechnology company headquartered in Singapore, with operations across Singapore, China and Germany, developing novel immunotherapies for infectious diseases and the cancers they cause. The company targets the most common cancer-causing infections — Helicobacter pylori, human papillomavirus (HPV), hepatitis B virus (HBV) and Epstein-Barr virus (EBV) — and is advancing a pipeline of TCR-engineered T cell therapies, antibodies and therapeutic vaccines built on its proprietary GianTCR platform. Lead programs include SCG101, a first-in-class autologous HBV-specific TCR-T therapy targeting hepatitis B surface antigen in HBV-related hepatocellular carcinoma, and SCG142, a next-generation HPV E7-specific TCR-T therapy for HPV-associated solid tumors that received FDA IND clearance. SCG covers the full value chain from drug discovery and manufacturing through clinical development and commercialization. It is a therapeutics developer,
  not a software vendor, and publishes no public API, developer portal or machine-readable contract.
layout: provider
modified: '2026-08-26'
name: SCG Cell Therapy
nav: Providers
network: true
overview: SCG Cell Therapy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Cell Therapy, Immunotherapy, Oncology, and Infectious Diseases.
random_paper: 13
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 3
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
    operational_transparency: 0.0
  previous_composite: 2.9
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
  name: Scg Cell Therapy Domain Security
  slug: scg-cell-therapy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: scg-cell-therapy
tags:
- Biotechnology
- Cell Therapy
- Immunotherapy
- Oncology
- Infectious Diseases
- Clinical Trials
- Life Sciences
- Healthcare
- Pharmaceuticals
- Singapore
website: https://www.scgcell.com/
---
