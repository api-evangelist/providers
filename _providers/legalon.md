---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: REST API for the LegalOn contract platform. Documented capabilities cover contract file operations (upload, retrieve, update, delete), contract information management (register and update metadata suc
  name: LegalOn Contract API
  slug: contract-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.legalontech.com/
- group: company
  title: ''
  type: Website
  url: https://legalontech.jp
- group: company
  title: ''
  type: Blog
  url: https://www.legalontech.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.legalontech.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.legalontech.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.legalontech.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.legalontech.com/terms-and-conditions#Privacy-Policy
- group: auth
  title: ''
  type: Security
  url: https://www.legalontech.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.legalontech.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.legalontech.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.legalontech.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.legalontech.com/new-at-legalon
- group: operate
  title: ''
  type: Support
  url: https://legalontech.jp/contact
- group: company
  title: ''
  type: Press
  url: https://www.legalontech.com/newsroom
- group: company
  title: ''
  type: Careers
  url: https://www.legalontech.com/careers
- group: other
  title: ''
  type: CaseStudies
  url: https://www.legalontech.com/customers
- group: auth
  title: ''
  type: Authentication
  url: authentication/legalon-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/legalon-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/legalon-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/legalon-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/legalon-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/legalon-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/legalon-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/legalon-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/legalon-llms.txt
created: '2026-07-17'
description: LegalOn Technologies is a legal-technology company building AI software for in-house legal teams, corporate legal operations, and law firms. Its platform covers AI contract review and redlining, contract playbooks, matter management, a contract data vault, translation, entity and board management, and agentic legal workflows, with a Microsoft Word integration for reviewing agreements in place. Founded in Japan as LegalForce and now operating in both Japan (legalontech.jp) and the United States (legalontech.com), the company runs a sibling product family for governance (GovernOn), sales (DealOn), HR (WorkOn), and marketing compliance (DocumentOn). LegalOn publishes a REST API for contract files and contract metadata — upload, retrieve, update and delete contract documents, register and update contract information such as counterparties and contract types, link related documents, and list registered contracts — authenticated with OAuth 2.0 client credentials, intended for integration
  with contract management systems, CRM, and BI tooling. The API is announced publicly but its reference documentation is not published on the open web; access is arranged through the vendor. The company is backed by Hongshan and the SoftBank Vision Fund, and publishes SOC 2 Type II, ISO/IEC 27001:2022 and ISO/IEC 27017:2015 certifications through a public trust center.
image: https://cdn.prod.website-files.com/68c03413336317ed3e6c0cb5/68f4566ea04559817c98ad87_LegalOn_OG%201.png
layout: provider
modified: '2026-07-19'
name: LegalOn
nav: Providers
network: true
overview: 'LegalOn publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Legal, Legal Technology, and Contracts.


  LegalOn''s developer surface includes engineering blog, pricing, changelog, support, authentication, and 20 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 29.8
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/legalon/refs/heads/main/screenshots/legalon-2026-07-25T224826.png
security:
- kind: authentication
  name: Legalon Authentication
  slug: legalon-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Legalon Domain Security
  slug: legalon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Legalon Trust Center
  slug: legalon-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, GDPR
slug: legalon
tags:
- Company
- Technology
- Legal
- Legal Technology
- Contracts
- Contract Management
- Contract Lifecycle Management
- Artificial Intelligence
- Document-Management
- Compliance
- Governance
- Software-as-a-Service
- Japan
website: https://www.legalontech.com/
---
