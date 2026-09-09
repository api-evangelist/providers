---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-09-08'
api_count: 1
apis:
- baseURL: https://api.aclid.bio
  baseurl_source: declared
  description: REST API for biosecurity screening and compliance automation. Initiate a pathogen/toxin sequence screen from a FASTA or FASTQ upload, a CSV of named sequences, or an inline JSON payload; poll or retri
  name: Aclid API
  slug: aclid-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aclid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aclid.bio/
- group: docs
  title: ''
  type: Documentation
  url: https://api.aclid.bio/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.aclid.bio/docs
- group: start
  title: ''
  type: Login
  url: https://dash.aclid.bio
- group: operate
  title: ''
  type: Support
  url: https://www.aclid.bio/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aclid.bio/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aclid.bio/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aclid.bio
- group: auth
  title: ''
  type: Authentication
  url: authentication/aclid-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aclid-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/aclid-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aclid-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aclid-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aclid-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aclid-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/aclid-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/aclid-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aclid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aclid-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aclid-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/aclid-openapi-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aclid-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/aclid-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aclid-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://dash.aclid.bio/.well-known/security.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aclid-sandbox.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/aclid-compliance-reason-codes.yml
created: '2026-09-06'
description: Aclid is a biosecurity and biosafety compliance automation platform for the synthetic biology supply chain. Gene synthesis providers, biofoundries and research institutions use Aclid to screen DNA/RNA orders for pathogenic, toxic and export-controlled sequence elements, to verify the customers placing those orders against international sanctions and watchlists, and to run and document the compliance review that regulators and the OSTP Framework for Nucleic Acid Synthesis Screening expect. The platform is delivered as a hosted dashboard plus a public REST API (api.aclid.bio) that initiates screens from FASTA, FASTQ, CSV or inline sequence payloads, returns structured findings with per-framework regulatory reason codes (US Commerce Control List, EU Dual-Use, Australia Group and others), manages customers and verifications, and issues hosted or embeddable customer-verification flows. Founded 2021 in New York by Kevin Flyangolts with scientific founder Harris H. Wang of Columbia
  University.
image: https://cdn.prod.website-files.com/671c02ec6144c945bfc5aa9c/6727db79308f1e1139096dd3_Logo.svg
layout: provider
modified: '2026-09-06'
name: Aclid
nav: Providers
network: true
overview: 'Aclid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biosecurity, Biosafety, Compliance, Synthetic Biology, and Life Sciences.


  Aclid''s developer surface includes documentation, API reference, support, authentication, sandbox, and 24 more developer resources.'
plans:
- name: Aclid Plans Pricing
  plan_count: 0
  slug: aclid-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Aclid Rate Limits
  slug: aclid-rate-limits
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 51.7
    developer_ergonomics: 42.3
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 41.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 38.8
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Aclid Authentication
  slug: aclid-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aclid Domain Security
  slug: aclid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aclid Vulnerability Disclosure
  slug: aclid-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: aclid
tags:
- Biosecurity
- Biosafety
- Compliance
- Synthetic Biology
- Life Sciences
- DNA Sequence Screening
- Sanctions Screening
- Export Control
- Biotechnology
- Risk Assessment
- Know Your Customer
website: https://www.aclid.bio/
---
