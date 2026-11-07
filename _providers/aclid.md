---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.aclid.bio
  baseurl_source: declared
  description: The Endpoints API from Aclid — 17 operation(s) for endpoints.
  name: Aclid Endpoints API
  slug: aclid-endpoints-api
artifact_total: 9
common:
- group: auth
  href: https://artifacts.apis.io/aclid/security/aclid-domain-security.yml
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
  href: https://artifacts.apis.io/aclid/authentication/aclid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aclid-authentication.yml
- group: design
  href: https://artifacts.apis.io/aclid/conventions/aclid-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aclid-conventions.yml
- group: design
  href: https://artifacts.apis.io/aclid/conventions/aclid-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aclid-conventions.yml
- group: design
  href: https://artifacts.apis.io/aclid/errors/aclid-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aclid-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aclid/lifecycle/aclid-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aclid-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/aclid/conformance/aclid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aclid-conformance.yml
- group: design
  href: https://artifacts.apis.io/aclid/data-model/aclid-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aclid-data-model.yml
- group: design
  href: https://artifacts.apis.io/aclid/components/aclid-components.yml
  title: ''
  type: Components
  url: components/aclid-components.yml
- group: build
  href: https://artifacts.apis.io/aclid/packages/aclid-packages.yml
  title: ''
  type: Packages
  url: packages/aclid-packages.yml
- group: commercial
  href: https://artifacts.apis.io/aclid/plans/aclid-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aclid-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/aclid/rate-limits/aclid-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aclid-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/aclid/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/aclid/llms/aclid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aclid-llms.txt
- group: other
  href: https://artifacts.apis.io/aclid/overlays/aclid-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aclid-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/aclid/well-known/aclid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aclid-well-known.yml
- group: auth
  href: https://artifacts.apis.io/aclid/well-known/aclid-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aclid-security.txt
- group: auth
  href: https://artifacts.apis.io/aclid/security/aclid-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aclid-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://dash.aclid.bio/.well-known/security.txt
- group: start
  href: https://artifacts.apis.io/aclid/sandbox/aclid-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aclid-sandbox.yml
- group: build
  href: https://artifacts.apis.io/aclid/errors/aclid-compliance-reason-codes.yml
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
overview: 'Aclid publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Endpoints API. Tagged areas include Biosecurity, Biosafety, Compliance, Synthetic Biology, and Life Sciences.


  The Aclid catalog on APIs.io includes 1 Spectral governance ruleset.


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
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Aclid API Rules
  rule_count: 44
  severity_counts:
    error: 35
    hint: 0
    info: 3
    warn: 6
  slug: aclid-rules
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 46.3
    developer_ergonomics: 42.3
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 39.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 24.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/aclid/aclid-2026-10-11T092656.png
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
skill_count: 2
skills:
- name: Screen a DNA order with Aclid
  slug: aclid-screen-a-dna-order
- name: Verify an Aclid customer and record the decision
  slug: aclid-verify-a-customer
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
- KYC
website: https://www.aclid.bio/
---
