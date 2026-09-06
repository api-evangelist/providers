---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: true
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
    well_known_catalog: true
  schema_version: 0.2
  score: 7.6
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: A portfolio of open source projects governed by the Confidential Computing Consortium covering Trusted Execution Environment runtimes, remote attestation services, trustworthy workload identity, and s
  name: Confidential Computing Consortium Projects
  slug: ccc-projects
- description: A working group and set of Internet Draft specifications under the Confidential Computing Consortium that define how confidential workloads establish, prove, and consume identity using remote attestat
  name: Trustworthy Workload Identity (TWI) Specifications
  slug: trustworthy-workload-identity
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/confidential-computing-consortium-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/confidential-computing
- group: company
  title: ''
  type: Website
  url: https://confidentialcomputing.io/
- group: docs
  title: ''
  type: Documentation
  url: https://confidentialcomputing.io/resources/white-papers-reports/
- group: other
  title: ''
  type: Projects
  url: https://confidentialcomputing.io/#projects
- group: build
  title: ''
  type: GitHub
  url: https://github.com/confidential-computing
- group: other
  title: ''
  type: Glossary
  url: https://github.com/confidential-computing/glossary
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/confidential-computing-consortium-vocabulary.yml
- group: other
  title: ''
  type: Governance
  url: https://github.com/confidential-computing/governance
- group: other
  title: ''
  type: Mailing Lists
  url: https://lists.confidentialcomputing.io/
- group: company
  title: ''
  type: Blog
  url: https://confidentialcomputing.io/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://confidentialcomputing.io/resources/newsroom/
- group: other
  title: ''
  type: Events
  url: https://confidentialcomputing.io/events/
- group: other
  title: ''
  type: Membership
  url: https://confidentialcomputing.io/join/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/confidential-computing
- group: operate
  title: ''
  type: Support
  url: https://confidentialcomputing.io/get-involved/contact-us/
- group: company
  title: ''
  type: Newsletter
  url: https://confidentialcomputing.io/get-involved/newsletter/
- group: company
  title: ''
  type: About
  url: https://confidentialcomputing.io/about/leadership/
- group: operate
  title: ''
  type: Community
  url: https://confidentialcomputing.io/committees/
- group: commercial
  title: ''
  type: Pricing
  url: https://confidentialcomputing.io/join/
- group: start
  title: ''
  type: SignUp
  url: https://confidentialcomputing.io/join/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linuxfoundation.org/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linuxfoundation.org/legal/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/confidential-computing-consortium-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/confidential-computing-consortium-api-catalog.json
- group: other
  title: ''
  type: ContentSignal
  url: https://confidentialcomputing.io/robots.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/confidential-computing-consortium-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/confidential-computing-consortium-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/confidential-computing-consortium-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/confidential-computing-consortium-rate-limits.yml
created: '2026-03-16'
description: The Confidential Computing Consortium (CCC) is a Linux Foundation project that brings together hardware vendors, cloud providers, and software developers to accelerate the adoption of confidential computing. CCC defines, advances, and standardizes hardware-based Trusted Execution Environments (TEEs) that protect data and code while in use, complementing existing protections for data at rest and in transit. The consortium governs open source projects and specifications spanning attestation, trustworthy workload identity, and TEE runtimes.
finops:
- name: Confidential Computing Consortium Finops
  service_category: API
  slug: confidential-computing-consortium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/confidential-computing-consortium.png
layout: provider
modified: '2026-09-05'
name: Confidential Computing Consortium
nav: Providers
network: true
overview: 'Confidential Computing Consortium publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Attestation, Confidential Computing, Hardware, Linux Foundation, and Open-Source.


  Confidential Computing Consortium''s developer surface includes documentation, GitHub presence, engineering blog, support, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Confidential Computing Consortium Plans Pricing
  plan_count: 4
  slug: confidential-computing-consortium-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Confidential Computing Consortium Rate Limits
  slug: confidential-computing-consortium-rate-limits
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 57.0
    catalog_earned_first_party: 17.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.4
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 33.3
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 33.3
    operational_transparency: 5.3
  previous_composite: 14.1
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/confidential-computing-consortium/refs/heads/main/screenshots/confidential-computing-consortium-2026-06-20T174850.png
security:
- kind: domain-security
  name: Confidential Computing Consortium Domain Security
  slug: confidential-computing-consortium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: confidential-computing-consortium
tags:
- Attestation
- Confidential Computing
- Hardware
- Linux Foundation
- Open-Source
- Privacy
- Security
- TEE
- Trusted Execution Environment
website: https://confidentialcomputing.io/
---
