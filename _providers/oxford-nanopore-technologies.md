---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.5
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: API reference for Oxford Nanopore Technologies services
  name: Oxford Nanopore API
  slug: oxford-nanopore-api
- baseURL: https://ftp.ncbi.nlm.nih.gov
  baseurl_source: declared
  description: The Genomes API from Oxford Nanopore Technologies — 1 operation(s) for genomes.
  name: Oxford Nanopore Technologies Genomes API
  slug: oxford-nanopore-technologies-genomes-api
artifact_total: 5
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oxford-nanopore-technologies/refs/heads/main/rules/oxford-nanopore-technologies-rules.yml
  title: ''
  type: Spectral
  url: rules/oxford-nanopore-technologies-rules.yml
- group: auth
  title: ''
  type: Security
  url: https://nanoporetech.com/products/analyse/vulnerability-disclosure-guidance
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oxford-nanopore-technologies/refs/heads/main/conformance/oxford-nanopore-technologies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/oxford-nanopore-technologies-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oxford-nanopore-technologies/refs/heads/main/well-known/oxford-nanopore-technologies-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/oxford-nanopore-technologies-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/oxford-nanopore-technologies/refs/heads/main/well-known/oxford-nanopore-technologies-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/oxford-nanopore-technologies-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/oxford-nanopore-technologies/refs/heads/main/hosts/oxford-nanopore-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oxford-nanopore-technologies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/oxford-nanopore-technologies/refs/heads/main/vendors/oxford-nanopore-technologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oxford-nanopore-technologies-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/oxford-nanopore-technologies/refs/heads/main/packages/oxford-nanopore-technologies-packages.yml
  title: ''
  type: SDKs
  url: packages/oxford-nanopore-technologies-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/oxford-nanopore-technologies/refs/heads/main/packages/oxford-nanopore-technologies-packages.yml
  title: ''
  type: Packages
  url: packages/oxford-nanopore-technologies-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nanoporetech.com/about/terms-conditions-policies
- group: operate
  title: ''
  type: Support
  url: https://nanoporetech.com/support
- group: start
  title: ''
  type: SignUp
  url: https://register.nanoporetech.com/telomere-to-telomere-bundle
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nanoporetech.com/about/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://nanoporetech.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://nanoporetech.com/documentation/results?category=application-workflows
- group: company
  title: ''
  type: Blog
  url: https://nanoporetech.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nanoporetech
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oxford-nanopore-technologies/refs/heads/main/security/oxford-nanopore-technologies-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/oxford-nanopore-technologies-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oxford-nanopore-technologies/refs/heads/main/security/oxford-nanopore-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oxford-nanopore-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nanoporetech.com
coverage:
  checked: '2026-10-14'
  detail: API documentation at https://api.nanoporetech.com/api-docs returns HTML without a machine‑readable spec.
  evidence:
  - status: 200
    url: https://api.nanoporetech.com/api-docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Oxford Nanopore Technologies (ONT) develops and sells portable real-time DNA and RNA sequencing devices, consumables, and analysis software. Their platform enables researchers to sequence long reads directly from biological samples, supporting applications from genomics and transcriptomics to clinical diagnostics and environmental monitoring. ONT’s technology combines nanopore hardware, flow cells, library preparation kits, and cloud‑based informatics to deliver fast, scalable sequencing solutions worldwide.
image: https://nanoporetech.com/api/assets/f/196663/300x69/3d970cc105/ont-logo-black.svg
layout: provider
modified: '2026-10-14'
name: Oxford Nanopore Technologies
nav: Providers
network: true
overview: 'Oxford Nanopore Technologies is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Genomes API, and 1 more. Tagged areas include Company, Sequencing, Genomics, Bioinformatics, and Diagnostics.


  The Oxford Nanopore Technologies catalog on APIs.io includes 1 Spectral governance ruleset.


  Oxford Nanopore Technologies'' developer surface includes support, signup flow, documentation, engineering blog, and 16 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Oxford Nanopore Technologies API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: oxford-nanopore-technologies-rules
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 10.7
    developer_ergonomics: 23.8
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Oxford Nanopore Technologies Domain Security
  slug: oxford-nanopore-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Oxford Nanopore Technologies Vulnerability Disclosure
  slug: oxford-nanopore-technologies-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: oxford-nanopore-technologies
tags:
- Company
- Sequencing
- Genomics
- Bioinformatics
- Diagnostics
website: https://nanoporetech.com
---
