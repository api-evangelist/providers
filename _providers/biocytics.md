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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://biocytics.com/
- group: company
  title: ''
  type: About
  url: https://biocytics.com/our-story/
- group: company
  title: ''
  type: Blog
  url: https://biocytics.com/news/
- group: operate
  title: ''
  type: Support
  url: https://biocytics.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biocytics.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/biocytics-inc./
- group: auth
  title: ''
  type: DomainSecurity
  url: security/biocytics-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/biocytics-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/biocytics-llms.txt
coverage:
  checked: '2026-09-02'
  detail: BioCytics sells cell-therapy manufacturing, CRO, lab and biobank services rather than software, and its one software product, the BioDICE clinical enterprise suite, is an internal system used to run its own trials — the /biodice/ page names openEHR, HL7, FHIR, OMOP and SMART-on-FHIR as data standards but publishes no endpoint, no spec and no developer portal, every developer path on biocytics.com returns the WordPress 404 template, no api./docs./developer. subdomain resolves, and the two product-named domains (biodice.com, opendice.com) are third-party parked listings for sale rather than BioCytics hosts.
  evidence:
  - status: 404
    url: https://biocytics.com/openapi.json
  - status: 404
    url: https://biocytics.com/developers
  - status: 404
    url: https://biocytics.com/graphql
  - status: 404
    url: https://biocytics.com/llms.txt
  - status: 404
    url: https://biocytics.com/.well-known/api-catalog
  - status: 404
    url: https://biocytics.com/.well-known/agent-card.json
  - status: 200
    url: https://biocytics.com/wp-json/
  - status: 200
    url: https://biodice.com/
  - status: 200
    url: https://biocytics.com/biodice/
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: 'BioCytics, Inc. is a privately held biotechnology company in Huntersville, North Carolina, founded in 2005 by John Powderly, MD, CPI, and clinically incubated by the co-located Carolina BioOncology Institute cancer research clinic. Its name means "applications of living cells": the company runs a Human Applications Laboratory (HAL), a patient-driven and industry-driven BioBank, and a BioInformatics group, and sells cGMP cell-therapy manufacturing (CDMO), early-phase CRO services, clinical lab diagnostics and translational analytical services alongside its own autologous adaptive immune cell therapy (AAICT) pipeline for solid tumors. Its BioDICE platform — BioCytics Digitally Integrated Clinical Enterprise — is an internal EMR / EDC-CDM / lab-documentation / CTMS suite whose product page names openEHR, HL7, FHIR, OMOP and SMART-on-FHIR as the data standards it works with, and openEHR International lists BioCytics as a Bronze industry partner. None of that is exposed: BioCytics
  publishes no developer program, no public API, and no machine-readable API contract of any kind, and biocytics.com is a 26-page WordPress site whose only machine-readable surface is the CMS''s own unadvertised /wp-json/ index.'
image: https://biocytics.com/wp-content/uploads/2022/03/BioCytics-hires-Master-logo-long.png
layout: provider
modified: '2026-09-02'
name: BioCytics
nav: Providers
network: true
overview: 'BioCytics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Healthcare, and Oncology.


  BioCytics'' developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Biocytics Domain Security
  slug: biocytics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: biocytics
tags:
- Company
- Biotechnology
- Life Sciences
- Healthcare
- Oncology
- Cell Therapy
- Immunotherapy
- Clinical Trials
- CRO
- CDMO
- Biobank
- Personalized Medicine
- Research
website: https://biocytics.com/
---
