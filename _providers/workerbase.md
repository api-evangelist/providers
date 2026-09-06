---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://workerbase.com
- group: commercial
  title: ''
  type: Pricing
  url: https://workerbase.com/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://workerbase.com/en/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://workerbase.com/en/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://workerbase.com/en/security
- group: auth
  title: ''
  type: Compliance
  url: https://workerbase.com/en/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/workerbase
- group: operate
  title: ''
  type: Support
  url: https://workerbase.zendesk.com/hc/en-us
- group: build
  title: ''
  type: Packages
  url: packages/workerbase-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/workerbase-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/workerbase-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/workerbase-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/workerbase-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workerbase-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/workerbase-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/workerbase-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/workerbase-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/workerbase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workerbase-domain-security.yml
created: '2026-07-17'
description: Workerbase is a Munich-based connected-worker platform — a frontline execution layer for manufacturing that bridges ERP/MES planning and shopfloor operations with digital work instructions, dynamic task orchestration, quality and maintenance workflows, material logistics, an industrial smartwatch, and AI agents for the shopfloor. Its per-tenant platform API is reachable through a first-party JavaScript SDK and Node-RED nodes published on npm, covering tasks, users, roles, skills, locations, media, databases, connectors, and functions; customer documentation lives in a login-gated help center.
image: https://avatars.githubusercontent.com/u/28139586?v=4
layout: provider
modified: '2026-07-21'
name: Workerbase
nav: Providers
network: true
overview: 'Workerbase is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Connected Worker, Frontline Operations, and Digital Work Instructions.


  Workerbase''s developer surface includes pricing, engineering blog, support, authentication, and 15 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 20.5
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workerbase/refs/heads/main/screenshots/workerbase-2026-09-02T170931.png
security:
- kind: authentication
  name: Workerbase Authentication
  slug: workerbase-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Workerbase Domain Security
  slug: workerbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Workerbase Vulnerability Disclosure
  slug: workerbase-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Workerbase Trust Center
  slug: workerbase-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: workerbase
tags:
- Company
- Manufacturing
- Connected Worker
- Frontline Operations
- Digital Work Instructions
- Quality Management
- Maintenance
- Industrial IoT
website: https://workerbase.com
---
