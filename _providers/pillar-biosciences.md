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
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pillar-biosciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pillarbiosci.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pillarbiosci.com/resources/
- group: operate
  title: ''
  type: Support
  url: https://www.pillarbiosci.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.pillarbiosci.com/company/pillar-news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pillarbiosci.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pillar-Biosciences-Inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pillar-biosciences
- group: build
  title: ''
  type: Packages
  url: packages/pillar-biosciences-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pillar-biosciences-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/pillar-biosciences-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pillar-biosciences-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pillar-biosciences-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pillar-biosciences-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pillar-biosciences-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Pillar sells NGS panels and the PiVAT analysis app, and PiVAT's own product page names its integration surface as bioinformatics FILE formats (FASTQ, BAM, VCF, PDF) rather than an API; the PiVAT app host answers HTTP 200 with the same 1,535-byte React SPA shell for /openapi.json and every other unknown path, and 403 for the whole /.well-known/ space, so there is no developer portal, contract or reference to read anywhere.
  evidence:
  - status: 200
    url: https://pivat.pillarbiosci.com/openapi.json
  - status: 403
    url: https://pivat.pillarbiosci.com/.well-known/agent-card.json
  - status: 404
    url: https://www.pillarbiosci.com/openapi.json
  - status: 404
    url: https://www.pillarbiosci.com/llms.txt
  - status: 200
    url: https://www.pillarbiosci.com/wp-sitemap-posts-page-1.xml
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Pillar Biosciences is a Natick, Massachusetts molecular diagnostics company, founded in 2014, that develops targeted next-generation sequencing (NGS) solutions for precision oncology. Its proprietary SLIMamp (Stem-Loop Inhibition Mediated amplification) chemistry enables highly multiplexed, single-tube PCR library preparation from as little as 2.5 ng of DNA, and its oncoReveal panel portfolio covers solid tumour tissue, liquid biopsy, haematologic malignancy, BRCA/HRD/methylation and inherited disease testing, alongside an InheritReveal line and a VersaTile machine-learning panel-design platform. Sequencing data is processed by PiVAT (Pillar Variant Analysis Toolkit), a secondary-analysis pipeline available as a local install or a HIPAA-scoped cloud deployment, with optional OncoKB-powered tertiary reporting. Pillar ships both research-use-only kits and an IVD product line, and raised a $34.5M round led by Illumina in 2025. Pillar publishes no public API, SDK or developer program;
  PiVAT's integration surface is bioinformatics file formats (FASTQ, BAM, VCF, PDF) behind a customer login.
image: https://www.pillarbiosci.com/wp-content/uploads/elementor/thumbs/Pillar_biosciences_logo-scaled-rsdcx7op9xcoyh7jq90gxuj6f8dx4edt9do6jp6ees.png
layout: provider
modified: '2026-08-26'
name: Pillar Biosciences
nav: Providers
network: true
overview: 'Pillar Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Genomics, Molecular Diagnostics, and Next-Generation Sequencing.


  Pillar Biosciences'' developer surface includes documentation, support, engineering blog, changelog, and 11 more developer resources.'
plans:
- name: Pillar Biosciences Plans Pricing
  plan_count: 0
  slug: pillar-biosciences-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 16.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Pillar Biosciences Domain Security
  slug: pillar-biosciences-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pillar-biosciences
tags:
- Company
- Life Sciences
- Genomics
- Molecular Diagnostics
- Next-Generation Sequencing
- Precision Oncology
- Bioinformatics
- Healthcare
- Laboratory Software
website: https://www.pillarbiosci.com/
---
