---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - rate-limits
  - security
  trial: false
  try_now: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nucleus-genomics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mynucleus.com
- group: company
  title: ''
  type: Blog
  url: https://mynucleus.com/blog
- group: operate
  title: ''
  type: Support
  url: https://mynucleus.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://mynucleus.com/products
- group: start
  title: ''
  type: SignUp
  url: https://app.mynucleus.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mynucleus.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mynucleus.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nucleus-Genomics
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mynucleus.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.mynucleus.com
- group: auth
  title: ''
  type: Security
  url: https://app.mynucleus.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/nucleus-genomics-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nucleus-genomics-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nucleus-genomics-llms.txt
- group: auth
  title: ''
  type: Compliance
  url: conformance/nucleus-genomics-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nucleus-genomics-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nucleus-genomics-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nucleus-genomics-plans-pricing.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nucleus-genomics-vulnerability-disclosure.yml
coverage:
  checked: '2026-08-26'
  detail: Nucleus sells a direct-to-consumer DNA test and an IVF service and ships no developer surface at all - /developers, /api and /docs all 404 on mynucleus.com, the member app at app.mynucleus.com is a static Next.js export whose JavaScript bundle contains no API host, the GitHub org Nucleus-Genomics has zero public repositories, and the company's own llms.txt describes products and pricing without naming a single endpoint.
  evidence:
  - status: 404
    url: https://mynucleus.com/developers
  - status: 404
    url: https://mynucleus.com/openapi.json
  - status: 404
    url: https://app.mynucleus.com/openapi.json
  - status: 404
    url: https://app.mynucleus.com/graphql
  - status: 200
    url: https://api.github.com/orgs/Nucleus-Genomics/repos
  - status: 200
    url: https://mynucleus.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Nucleus Genomics (product brand "Nucleus", mynucleus.com) is a New York based consumer genomics company founded in 2021 by Kian Sadeghi. It sells a physician-ordered, clinical-grade DNA health test built on 30x whole-genome sequencing (Illumina NovaSeq X) across three products: Health (risk and trait insights across 900+ diseases), Family (preconception carrier screening across 2,000+ inheritable conditions) and IVF+ / Nucleus Embryo (genetics-forward IVF including polygenic embryo screening). Members access results through app.mynucleus.com and can download raw data as VCF or FASTQ. Sequencing is performed in the United States; the company states it is HIPAA compliant, CLIA certified and CAP accredited, and publishes a Vanta-hosted trust center. As of this profiling pass Nucleus publishes no public developer API, API reference, SDK or machine-readable contract — its published machine surface is an llms.txt, a security.txt, an Instatus status page and the trust center.'
image: https://framerusercontent.com/images/2PecGEIaH999a7wI1eyPKXhzb4.jpg
layout: provider
modified: '2026-08-26'
name: Nucleus Genomics
nav: Providers
network: true
overview: 'Nucleus Genomics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Genomics, Health, Consumer Genetics, and Whole Genome Sequencing.


  Nucleus Genomics'' developer surface includes engineering blog, support, pricing, signup flow, and 16 more developer resources.'
plans:
- name: Nucleus Genomics Plans Pricing
  plan_count: 3
  slug: nucleus-genomics-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Nucleus Genomics Rate Limits
  slug: nucleus-genomics-rate-limits
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 29.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nucleus-genomics/refs/heads/main/screenshots/nucleus-genomics-2026-09-02T150813.png
security:
- kind: domain-security
  name: Nucleus Genomics Domain Security
  slug: nucleus-genomics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nucleus Genomics Vulnerability Disclosure
  slug: nucleus-genomics-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Nucleus Genomics Trust Center
  slug: nucleus-genomics-trust-center
  summary_line: HIPAA, CLIA, CAP
slug: nucleus-genomics
tags:
- Company
- Genomics
- Health
- Consumer Genetics
- Whole Genome Sequencing
- Fertility
- IVF
- Carrier Screening
- Precision Medicine
- Biotechnology
website: https://mynucleus.com
---
