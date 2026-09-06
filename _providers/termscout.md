---
access_model:
  confidence: high
  label: Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - https://www.termscout.com/termscout-pricing
  - https://api.termscout.com/docs
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://api.termscout.com
  baseurl_source: declared
  description: The Contract Positions API from TermScout — 1 operation(s) for contract positions.
  name: TermScout Contract Positions API
  slug: termscout-contract-positions-api
- baseURL: https://api.termscout.com
  baseurl_source: declared
  description: The Contracts API from TermScout — 9 operation(s) for contracts.
  name: TermScout Contracts API
  slug: termscout-contracts-api
artifact_total: 8
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/termscout-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/termscout-data-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://termscout.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.termscout.com
- group: operate
  title: ''
  type: Support
  url: https://learn.termscout.com/knowledge
- group: commercial
  title: ''
  type: Pricing
  url: https://www.termscout.com/termscout-pricing
- group: start
  title: ''
  type: Login
  url: https://app.termscout.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.termscout.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.termscout.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: security/termscout-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.termscout.com/
- group: auth
  title: ''
  type: Security
  url: https://security.termscout.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/termscout-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/termscout-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/termscout-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/termscout-plans-pricing.yml
created: '2026-07-17'
description: 'TermScout is a contract intelligence and certification company for legal, procurement, and sales teams. Its platform analyzes and benchmarks commercial agreements against market standards, generates contract signals through Certify (AI contract analysis), and certifies contracts with TrustMark as an external, third-party signal of fairness that helps buyers and sellers close deals faster with less negotiation. TermScout was surfaced as a Techstars portfolio company and profiled in the API Evangelist network. TermScout does publish a machine-readable contract: an OpenAPI 3.0.1 definition for the "termscout-data" API is served anonymously at https://api.termscout.com/docs, covering contract upload, processing status, extracted fields, citations, predicted labels and red flags, playbook results, and aggregate market data across contract positions. The API itself is key-gated (x-api-key plus an Authorization bearer credential) and access is arranged through sales; there is no self-serve
  developer portal, SDK, or published API reference. Its end-user products are delivered through the app.termscout.com web application, which also publishes an llms.txt index of public TrustMark contract reports.'
image: https://www.termscout.com/hs-fs/hubfs/Vector%20(21).png
layout: provider
modified: '2026-08-14'
name: TermScout
nav: Providers
network: true
overview: 'TermScout publishes 2 APIs on the [APIs.io](https://apis.io/) network: Contract Positions API and Contracts API. Tagged areas include Company, Legal Tech, Contract Intelligence, Contract Certification, and Contract Analysis.


  TermScout''s developer surface includes engineering blog, support, pricing, and 14 more developer resources.'
plans:
- name: Termscout Plans Pricing
  plan_count: 3
  slug: termscout-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Termscout Rate Limits
  slug: termscout-rate-limits
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 4.5
    contract_quality: 48.6
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 42.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/termscout/refs/heads/main/screenshots/termscout-2026-08-17T082319.png
security:
- kind: authentication
  name: Termscout Authentication
  slug: termscout-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Termscout Domain Security
  slug: termscout-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Termscout Vulnerability Disclosure
  slug: termscout-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Termscout Trust Center
  slug: termscout-trust-center
  summary_line: SOC 2, GDPR, CCPA
slug: termscout
tags:
- Company
- Legal Tech
- Contract Intelligence
- Contract Certification
- Contract Analysis
- Procurement
- Legal Operations
- Sales Enablement
- Artificial Intelligence
- Contract Data
- Document Analysis
website: https://termscout.com/
---
