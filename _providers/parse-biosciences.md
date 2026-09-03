---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.parsebiosciences.com/
- group: company
  title: ''
  type: Blog
  url: https://www.parsebiosciences.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.parsebiosciences.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://app.trailmaker.parsebiosciences.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.parsebiosciences.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.parsebiosciences.com/legal/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/parse-biosciences
- group: design
  title: ''
  type: Conformance
  url: conformance/parse-biosciences-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/parse-biosciences-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/parse-biosciences-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/parse-biosciences-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/parse-biosciences-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/parse-biosciences-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/parse-biosciences-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parse-biosciences-domain-security.yml
coverage:
  checked: '2026-08-26'
  detail: Trailmaker's backend at api.app.trailmaker.parsebiosciences.com is live and answers every anonymous route with 401 "The request does not contain an authentication token.", and the only documentation Parse publishes for it is a Zendesk Help Center of end-user guides that assume a signed-in Trailmaker tenant — there is no public API reference, no spec at any discovery path, and the FASTQ upload token is minted inside the signed-in app.
  evidence:
  - status: 401
    url: https://api.app.trailmaker.parsebiosciences.com/v2/experiments/examples
  - status: 404
    url: https://api.app.trailmaker.parsebiosciences.com/v2/openapi.json
  - status: 404
    url: https://app.trailmaker.parsebiosciences.com/openapi.json
  - status: 403
    url: https://support.parsebiosciences.com/hc/en-us
  reason: customer-only-docs
  state: gated
created: '2026-08-26'
description: Parse Biosciences is a Seattle-based life-sciences company that makes Evercode, a split-pool combinatorial barcoding chemistry for single cell and single nuclei RNA sequencing that runs on standard lab equipment rather than a dedicated microfluidics instrument. Its product line spans Evercode WT Mini, WT, WT Mega and WT Penta whole transcriptome kits, Evercode TCR and BCR immune profiling, Evercode Fixation, Evercode WT FFPE, Gene Select and CRISPR Detect, alongside a GigaLab sequencing service for 10M+ cell projects. Data analysis is delivered through Trailmaker, a cloud application that takes Evercode FASTQ files through a pipeline and into interactive downstream analysis. Parse publishes no public developer API, SDK, or machine-readable API contract; Trailmaker is an end-user web application whose backend is authenticated with AWS Cognito and undocumented outside the product.
image: https://www.parsebiosciences.com/wp-content/uploads/2024/02/parsebio-home.png
layout: provider
modified: '2026-08-26'
name: Parse Biosciences
nav: Providers
network: true
overview: 'Parse Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Genomics, and Single-Cell Sequencing.


  Parse Biosciences'' developer surface includes engineering blog, support, and 13 more developer resources.'
plans:
- name: Parse Biosciences Plans Pricing
  plan_count: 0
  slug: parse-biosciences-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Parse Biosciences Rate Limits
  slug: parse-biosciences-rate-limits
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 16.4
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parse-biosciences/refs/heads/main/screenshots/parse-biosciences-2026-09-02T150911.png
security:
- kind: authentication
  name: Parse Biosciences Authentication
  slug: parse-biosciences-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Parse Biosciences Domain Security
  slug: parse-biosciences-domain-security
  summary_line: TLSv1.3 · DMARC
slug: parse-biosciences
tags:
- Company
- Biotechnology
- Life Sciences
- Genomics
- Single-Cell Sequencing
- Bioinformatics
- Scientific Software
- Data Analysis
- Laboratory
- Research
website: https://www.parsebiosciences.com/
---
