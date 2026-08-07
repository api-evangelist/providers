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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-06'
api_count: 17
apis:
- description: The Care Plans API from Mon Ami — 4 operation(s) for care plans.
  name: Mon Ami Care Plans API
  slug: mon-ami-care-plans-api
- description: The Client Calls API from Mon Ami — 2 operation(s) for client calls.
  name: Mon Ami Client Calls API
  slug: mon-ami-client-calls-api
- description: The Clients API from Mon Ami — 4 operation(s) for clients.
  name: Mon Ami Clients API
  slug: mon-ami-clients-api
- description: The Copays API from Mon Ami — 2 operation(s) for copays.
  name: Mon Ami Copays API
  slug: mon-ami-copays-api
- description: The Documents API from Mon Ami — 2 operation(s) for documents.
  name: Mon Ami Documents API
  slug: mon-ami-documents-api
- description: The Funding Sources API from Mon Ami — 2 operation(s) for funding sources.
  name: Mon Ami Funding Sources API
  slug: mon-ami-funding-sources-api
- description: The Languages API from Mon Ami — 2 operation(s) for languages.
  name: Mon Ami Languages API
  slug: mon-ami-languages-api
- description: The People API from Mon Ami — 2 operation(s) for people.
  name: Mon Ami People API
  slug: mon-ami-people-api
- description: The Programs API from Mon Ami — 4 operation(s) for programs.
  name: Mon Ami Programs API
  slug: mon-ami-programs-api
- description: The Provider Referrals API from Mon Ami — 2 operation(s) for provider referrals.
  name: Mon Ami Provider Referrals API
  slug: mon-ami-provider-referrals-api
- description: The Providers API from Mon Ami — 2 operation(s) for providers.
  name: Mon Ami Providers API
  slug: mon-ami-providers-api
- description: The Services API from Mon Ami — 6 operation(s) for services.
  name: Mon Ami Services API
  slug: mon-ami-services-api
- description: The Sites API from Mon Ami — 1 operation(s) for sites.
  name: Mon Ami Sites API
  slug: mon-ami-sites-api
- description: The Tasks API from Mon Ami — 3 operation(s) for tasks.
  name: Mon Ami Tasks API
  slug: mon-ami-tasks-api
- description: The Visits API from Mon Ami — 2 operation(s) for visits.
  name: Mon Ami Visits API
  slug: mon-ami-visits-api
- description: The Volunteers API from Mon Ami — 2 operation(s) for volunteers.
  name: Mon Ami Volunteers API
  slug: mon-ami-volunteers-api
- description: The Webhooks API from Mon Ami — 2 operation(s) for webhooks.
  name: Mon Ami Webhooks API
  slug: mon-ami-webhooks-api
artifact_total: 21
asyncapis:
- description: ''
  name: Mon Ami Webhooks
  slug: mon-ami-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.monami.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.monami.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.monami.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.monami.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.monami.io/
- group: start
  title: ''
  type: Login
  url: https://app.monami.io/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.monami.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.monami.io/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.monami.io
- group: auth
  title: ''
  type: Compliance
  url: https://trust.monami.io
- group: company
  title: ''
  type: Blog
  url: https://www.monami.io/resources/?type=ar
- group: design
  title: ''
  type: Conformance
  url: conformance/mon-ami-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mon-ami-domain-security.yml
created: '2026-07-17'
description: Mon Ami is a modern data-management platform for aging and disability services, unifying case management, billing, evidence-based assessments, reporting, and compliance in one system. It serves State Units on Aging (SUAs), Area Agencies on Aging (AAAs), Intellectual & Developmental Disabilities (I/DD) programs, Long-Term Care Ombudsman offices, Medicaid HCBS providers, and Community Care Hubs. Mon Ami exposes a REST API (clients, care plans, services, copays, documents, programs, people, volunteers, referrals, tasks, visits, and webhooks) and treats interoperability as a design standard with open REST, HL7 FHIR R4, and secure SFTP. The platform is HIPAA and SOC 2 Type II certified and FedRAMP Ready.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mon-ami.png
layout: provider
modified: '2026-07-20'
name: Mon Ami
nav: Providers
network: true
overview: 'Mon Ami publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Care Plans API, Client Calls API, Clients API, and 14 more. Tagged areas include Company, Healthcare, Aging Services, Disability Services, and Case Management.


  The Mon Ami catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mon Ami''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 9 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 43.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 69.6
    developer_ergonomics: 37.0
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 43.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Mon Ami Authentication
  slug: mon-ami-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mon Ami Domain Security
  slug: mon-ami-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Mon Ami Trust Center
  slug: mon-ami-trust-center
  summary_line: SOC 2 Type II, HIPAA, FedRAMP Ready, WCAG 2.1 AA
slug: mon-ami
tags:
- Company
- Healthcare
- Aging Services
- Disability Services
- Case Management
- Care Coordination
- HL7 FHIR
- HIPAA
website: https://www.monami.io
---
