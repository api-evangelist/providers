---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/photonic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://photonic.com/
- group: company
  title: ''
  type: About
  url: https://photonic.com/about-us/
- group: other
  title: ''
  type: Products
  url: https://photonic.com/products/
- group: other
  title: ''
  type: Technology
  url: https://photonic.com/technology/
- group: company
  title: ''
  type: Blog
  url: https://photonic.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://photonic.com/blog/feed/
- group: company
  title: ''
  type: PressRoom
  url: https://photonic.com/press-room/
- group: other
  title: ''
  type: Resources
  url: https://photonic.com/resources/
- group: company
  title: ''
  type: Careers
  url: https://photonic.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://photonic.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PhotonicInc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://photonic.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://photonic.com/terms-and-conditions/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/photonic-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Photonic Inc. is a pre-commercial quantum-hardware company whose entire web presence is a WordPress marketing site — /developers/, /docs/ and /api/ all return 404, no OpenAPI/Swagger responds at any probed path, every /.well-known/ path 404s, and the PhotonicInc GitHub org holds a single QLDPC research repository with no client library, so there is no developer program to profile rather than one we could not reach.
  evidence:
  - status: 404
    url: https://photonic.com/developers/
  - status: 404
    url: https://photonic.com/openapi.json
  - status: 404
    url: https://photonic.com/.well-known/agent-card.json
  - status: 200
    url: https://photonic.com/llms.txt
  - status: 200
    url: https://api.github.com/orgs/PhotonicInc
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Photonic Inc. is a Vancouver, British Columbia deep-tech company founded in 2016 by Dr. Stephanie Simmons and led by CEO Dr. Paul Terry, building distributed, fault-tolerant quantum computing and quantum networking on silicon T centre spin-photon qubits. Its "Entanglement First" architecture couples qubits that compute, store and emit telecom-band photons natively, so individual modules can be entangled over ordinary telecom fibre rather than scaled inside a single dilution refrigerator, and its SHYPS QLDPC error-correction codes cut the physical-qubit overhead of fault tolerance. Backed by Microsoft, British Columbia Investment Management Corp, RBC and TELUS, selected for Stage B of DARPA''s Quantum Benchmarking Initiative, and intending to deliver quantum computing through Azure and private systems. As of this profile Photonic is pre-commercial from an integration standpoint: it publishes no API, SDK, developer portal or machine-readable contract of any kind.'
image: https://photonic.com/wp-content/uploads/2026/02/cropped-Photonic_Symbol_Blue_white_space-192x192.png
layout: provider
modified: '2026-08-26'
name: Photonic
nav: Providers
network: true
overview: 'Photonic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Quantum Computing, Quantum Networking, Silicon Photonics, and Semiconductors.


  Photonic''s developer surface includes engineering blog and 14 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Photonic Domain Security
  slug: photonic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: photonic
tags:
- Company
- Quantum Computing
- Quantum Networking
- Silicon Photonics
- Semiconductors
- Deep Tech
- Research
- Hardware
- Canada
website: https://photonic.com/
---
