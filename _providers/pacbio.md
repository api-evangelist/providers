---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: PacBio provides sequencing data APIs documented at the support documentation page.
  name: PacBio API
  slug: pacbio-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pacbio/refs/heads/main/well-known/pacbio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pacbio-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pacbio/refs/heads/main/hosts/pacbio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pacbio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pacbio/refs/heads/main/vendors/pacbio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pacbio-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pacb.com/legal-and-trademarks/terms-and-conditions-of-sale/
- group: operate
  title: ''
  type: Support
  url: https://www.pacb.com/support/
- group: start
  title: ''
  type: SignUp
  url: https://www.pacb.com/blog/register-now-isoform-sequencing/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.pacb.com/technology/roadmap/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pacb.com/legal-and-trademarks/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.pacb.com/about-us/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.pacb.com/leadership/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pacb.com/support/documentation/
- group: company
  title: ''
  type: Blog
  url: https://www.pacb.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pacbio/refs/heads/main/security/pacbio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pacbio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pacb.com
coverage:
  checked: '2026-10-14'
  detail: Documentation pages require JavaScript rendering and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://www.pacb.com/support/documentation/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Pacific Biosciences (PacBio) provides advanced DNA sequencing technologies that enable researchers to generate long, highly accurate reads for genomic analysis. Their platforms deliver real-time, single-molecule sequencing, supporting applications in research, clinical, and agricultural fields. PacBio’s solutions emphasize high consensus accuracy, enabling insights into complex genomes, structural variants, and epigenetic modifications.
image: https://www.pacb.com/wp-content/uploads/sequencing-system_featured-image_1200x628.png
layout: provider
modified: '2026-10-14'
name: PacBio
nav: Providers
network: true
overview: 'PacBio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sequencing, Genomics, Biotechnology, and Bioinformatics.


  PacBio''s developer surface includes support, signup flow, documentation, engineering blog, and 10 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 60.7
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pacbio Domain Security
  slug: pacbio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pacbio
tags:
- Company
- Sequencing
- Genomics
- Biotechnology
- Bioinformatics
website: https://www.pacb.com
---
