---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for agent actions such as listing services, getting service details, and submitting enquiries.
  name: Agent Actions API
  slug: agent-actions-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/aevumsecurity-com-sg/conformance/aevumsecurity-com-sg-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aevumsecurity-com-sg-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aevumsecurity-com-sg/llms/aevumsecurity-com-sg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aevumsecurity-com-sg-llms.txt
- group: other
  href: https://artifacts.apis.io/aevumsecurity-com-sg/a2a/aevumsecurity-com-sg-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aevumsecurity-com-sg-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aevumsecurity-com-sg/well-known/aevumsecurity-com-sg-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aevumsecurity-com-sg-well-known.yml
- group: other
  href: https://artifacts.apis.io/aevumsecurity-com-sg/hosts/aevumsecurity-com-sg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aevumsecurity-com-sg-hosts.yml
- group: other
  href: https://artifacts.apis.io/aevumsecurity-com-sg/vendors/aevumsecurity-com-sg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aevumsecurity-com-sg-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aevumsecurity-com-sg/security/aevumsecurity-com-sg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aevumsecurity-com-sg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aevumsecurity.com.sg/
- group: docs
  title: ''
  type: Documentation
  url: https://aevumsecurity.com.sg/services/
- group: start
  title: ''
  type: AgentPortal
  url: https://agents.aevumsecurity.com.sg/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aevumsecurity.com.sg/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aevumsecurity.com.sg/terms/
- group: operate
  title: ''
  type: Contact
  url: https://aevumsecurity.com.sg/contact/
created: '2026-10-31'
description: Aevum Security provides auditor-developed cybersecurity and managed solutions tailored for MAS‑regulated financial institutions and GovTech‑regulated technology vendors. Leveraging audit assurance frameworks, they deliver confidentiality, integrity, and availability controls through encryption, role‑based access, privileged access management, and continuous compliance monitoring. Their services include data protection, risk management, and security philosophy grounded in the CIA triad, aimed at protecting critical business assets and ensuring operational resilience.
image: https://aevumsecurity.com.sg/img/og-image.png
layout: provider
modified: '2026-10-31'
name: Aevum Security
nav: Providers
network: true
overview: 'Aevum Security is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Cybersecurity, Auditing, Financial Services, and Government Tech.


  Aevum Security''s developer surface includes documentation and 12 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 14.1
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aevumsecurity Com Sg Domain Security
  slug: aevumsecurity-com-sg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aevumsecurity-com-sg
tags:
- Security
- Cybersecurity
- Auditing
- Financial Services
- Government Tech
website: https://aevumsecurity.com.sg/
---
