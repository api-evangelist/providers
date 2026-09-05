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
  - sandbox
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://api.kybb.app.merklescience.com/api/v1
  baseurl_source: declared
  description: Query and retrieve off-chain VASP due-diligence entities.
  name: Merkle Science VASP Entities API
  slug: merkle-science-vasp-entities-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Merkle Science KYBB (Know Your Blockchain Business) VASP Entities API
  slug: open-merkle-science-vasp-entities-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/merkle-science-kybb-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/merkle-science-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.merklescience.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/merkle-science-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://merklescience.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://kybb.docs.merklescience.com/
- group: docs
  title: ''
  type: Documentation
  url: https://kybb.docs.merklescience.com/docs/kybb-introduction
- group: docs
  title: ''
  type: APIReference
  url: https://kybb.docs.merklescience.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://kybb.docs.merklescience.com/reference/authentication
- group: auth
  title: ''
  type: Authentication
  url: authentication/merkle-science-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.merklescience.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@merklescience.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/merklescience
- group: start
  title: ''
  type: Login
  url: https://kybb.app.merklescience.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.merklescience.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.merklescience.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/merkle-science-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/merkle-science-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/merkle-science-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/merkle-science-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/merkle-science-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/merkle-science-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/merkle-science-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/merkle-science-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/merkle-science-well-known.yml
created: '2026-07-17'
description: Merkle Science is a blockchain analytics and predictive crypto risk platform that helps virtual asset businesses, financial institutions, and government agencies detect fraud, monitor transactions, and stay compliant with AML, KYC, and CFT regulations across 10,000+ crypto assets. Its product suite includes Compass (transaction and wallet monitoring), Tracker (forensic investigation and fund tracing), KYBB / Know Your Blockchain Business (counterparty due diligence and risk intelligence), Onchain Pulse (ecosystem monitoring and token risk scoring), and Institute (compliance training and certification). The public KYBB API exposes off-chain VASP due-diligence data — KYC/AML posture, supported coins and FIAT, permitted activities, regulatory alerts, licensing and legal-entity records, and jurisdictional restrictions. Merkle Science is backed by 500 Global.
image: https://www.merklescience.com/
layout: provider
modified: '2026-07-20'
name: Merkle Science
nav: Providers
network: true
overview: 'Merkle Science publishes 1 API on the [APIs.io](https://apis.io/) network: VASP Entities API. Tagged areas include Company, Blockchain Analytics, Cryptocurrency, Compliance, and AML.


  Merkle Science''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, sandbox, and 19 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 59.9
    developer_ergonomics: 47.0
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 40.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/merkle-science/refs/heads/main/screenshots/merkle-science-2026-08-07T172608.png
security:
- kind: authentication
  name: Merkle Science Authentication
  slug: merkle-science-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Merkle Science Domain Security
  slug: merkle-science-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Merkle Science Trust Center
  slug: merkle-science-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: merkle-science
tags:
- Company
- Blockchain Analytics
- Cryptocurrency
- Compliance
- AML
- KYC
- Risk
- Fraud Detection
- Due Diligence
- RegTech
website: https://merklescience.com
---
