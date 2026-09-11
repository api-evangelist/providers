---
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 3
common:
- group: design
  title: ''
  type: Conformance
  url: conformance/adaptive-biotechnologies-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adaptive-biotechnologies-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adaptive-biotechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adaptivebiotech.com/
- group: operate
  title: ''
  type: Support
  url: https://www.adaptivebiotech.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.adaptivebiotech.com/blog/
- group: start
  title: ''
  type: Login
  url: https://clients.adaptivebiotech.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adaptivebiotech.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adaptivebiotech.com/online-privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.adaptivebiotech.com/licenses-and-accreditation/
- group: company
  title: ''
  type: Careers
  url: https://www.adaptivebiotech.com/career-listings/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.adaptivebiotech.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/adaptive-biotechnologies_stock/
coverage:
  checked: '2026-09-07'
  detail: Adaptive markets a live clonoSEQ integration surface — "40+ direct data connections across 200+ healthcare institutions", Epic Aura, Flatiron OncoEMR Molecular Profiling Integration and Carequality result delivery — but the only door is an 8-12 week engagement arranged with integration specialists at emrsupport@adaptivebiotech.com; there is no developer page in the 35-URL sitemap, no interface specification, and /openapi.json plus every named /.well-known path 404s on all four Adaptive-controlled hosts.
  evidence:
  - status: 200
    url: https://www.clonoseq.com/emr-integration/
  - status: 200
    url: https://clients.adaptivebiotech.com/login
  - status: 404
    url: https://www.adaptivebiotech.com/openapi.json
  - status: 404
    url: https://www.adaptivebiotech.com/.well-known/api-catalog
  - status: 200
    url: https://www.adaptivebiotech.com/page-sitemap.xml
  - status: 200
    url: https://api.github.com/orgs/AdaptiveBiotech/repos
  reason: sales-gate
  state: gated
created: '2026-09-07'
description: 'Adaptive Biotechnologies Corporation (Nasdaq: ADPT) is a Seattle, Washington immune-medicine company that reads and translates the adaptive immune system at scale. Founded in 2009 by brothers Chad Robins and Harlan Robins as Adaptive TCR Corporation, it built an immunosequencing platform that amplifies and sequences rearranged T-cell and B-cell receptor genes, then applies computational models to turn that receptor repertoire into clinical and research data. Its lead commercial product is clonoSEQ, an FDA-cleared next-generation sequencing assay for measurable residual disease (MRD) in multiple myeloma, B-cell acute lymphoblastic leukemia, chronic lymphocytic leukemia, mantle cell lymphoma and diffuse large B-cell lymphoma, run out of its CLIA-certified, CAP-accredited Seattle laboratory. It also sells immunoSEQ research assays with the cloud-based immunoSEQ Analyzer and the immuneACCESS public data repository, and MRD biopharma services to drug developers. Adaptive is a diagnostics
  and services company, not a software vendor: it publishes no developer portal, no public API reference and no machine-readable specification. Its integration surface is clinician-facing and delivered bilaterally — clonoSEQ orders and results flow through Epic (including Epic Aura), Flatiron Health''s OncoEMR via Molecular Profiling Integration, and Carequality/health information exchanges, arranged through its EMR integration specialists rather than through self-serve documentation.'
image: https://www.adaptivebiotech.com/wp-content/uploads/2021/01/adaptive-logo@2x-copy.png
layout: provider
modified: '2026-09-07'
name: Adaptive Biotechnologies
nav: Providers
network: true
overview: 'Adaptive Biotechnologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Genomics, and Immunology.


  Adaptive Biotechnologies'' developer surface includes support, engineering blog, and 11 more developer resources.'
plans:
- name: Adaptive Biotechnologies Plans Pricing
  plan_count: 0
  slug: adaptive-biotechnologies-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Adaptive Biotechnologies Rate Limits
  slug: adaptive-biotechnologies-rate-limits
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 17.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adaptive Biotechnologies Domain Security
  slug: adaptive-biotechnologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adaptive-biotechnologies
tags:
- Company
- Biotechnology
- Life Sciences
- Genomics
- Immunology
- Clinical Diagnostics
- Oncology
- Health Care
- Laboratory
- Precision Medicine
- Data
website: https://www.adaptivebiotech.com/
---
