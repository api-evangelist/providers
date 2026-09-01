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
  url: security/bluestar-genomics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clearnotehealth.com/
- group: company
  title: ''
  type: Blog
  url: https://www.clearnotehealth.com/our-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.clearnotehealth.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ClearNote-Health
- group: operate
  title: ''
  type: Support
  url: https://www.clearnotehealth.com/get-in-touch/
- group: operate
  title: ''
  type: Contact
  url: https://www.clearnotehealth.com/get-in-touch/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clearnotehealth.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clearnotehealth.com/terms-of-use/
- group: company
  title: ''
  type: Careers
  url: https://www.clearnotehealth.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clearnotehealth/
coverage:
  checked: '2026-08-08'
  detail: 'ClearNote Health is a clinical laboratory diagnostics company whose product is the Avantect blood test ordered by clinicians through a hosted Formstack intake form, not software: clearnotehealth.com is a WordPress marketing site with no developer, docs, or api subdomain (all NXDOMAIN), and both first-party GitHub organizations hold only forks of open-source bioinformatics tooling (nf-core demultiplex/modules, airbyte, a grpcio build).'
  evidence:
  - status: 200
    url: https://www.clearnotehealth.com/
  - status: 404
    url: https://www.clearnotehealth.com/developers
  - status: 404
    url: https://www.clearnotehealth.com/api
  - status: 404
    url: https://www.clearnotehealth.com/openapi.json
  - status: 404
    url: https://www.clearnotehealth.com/llms.txt
  - status: 404
    url: https://www.clearnotehealth.com/.well-known/agent-card.json
  - status: 404
    url: https://www.avantect.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/clearnote-health
  reason: not-a-software-company
  state: none
created: '2026-08-08'
description: 'ClearNote Health (formerly Bluestar Genomics) is a US cancer detection company with offices in San Diego and San Mateo, California. Its proprietary 5hmC epigenomic platform combines cell-free DNA sequencing from a standard blood draw with machine learning to identify DNA-based alterations as cancer develops. The company commercializes Avantect, a suite of early-detection liquid biopsy tests for pancreatic and ovarian cancer that clinicians order through its laboratory, and Virtuoso, a research-use-only epigenomics platform sold to biopharma for drug discovery, therapy response and resistance research. ClearNote Health publishes no public developer program, API, SDK, or machine-readable specification: the clinician ordering path is a hosted intake form, and its public GitHub organization contains only forks of open-source bioinformatics tooling.'
image: https://www.clearnotehealth.com/wp-content/uploads/2025/10/ClearNote%C2%AEHealthLogo_rgb.png
layout: provider
modified: '2026-08-08'
name: ClearNote Health
nav: Providers
network: true
overview: 'ClearNote Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Biotechnology, Genomics, and Epigenomics.


  ClearNote Health''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 2
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Bluestar Genomics Domain Security
  slug: bluestar-genomics-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: bluestar-genomics
tags:
- Company
- Health
- Biotechnology
- Genomics
- Epigenomics
- Cancer Detection
- Diagnostics
- Liquid Biopsy
- Precision Medicine
- Life Sciences
website: https://www.clearnotehealth.com/
---
