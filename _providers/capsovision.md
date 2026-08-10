---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://capsovision.com/
- group: start
  title: ''
  type: Login
  url: https://www.capsocloud.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capsovision.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://capsovision.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CapsoVision
- group: build
  title: ''
  type: Packages
  url: packages/capsovision-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/capsovision-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/capsovision-domain-security.yml
coverage:
  checked: '2026-08-09'
  detail: CapsoVision ships clinical software (CapsoCloud/CapsoView) but no developer program of any kind - its GitHub org has zero public repositories, and the CapsoCloud app's own JSON backend at www.capsocloud.com/api/ answers "Resource Not Found" to every unauthenticated path while every other path returns the same 13,322-byte AngularJS shell, so there is no public API, spec, or reference to read.
  evidence:
  - status: 200
    url: https://www.capsocloud.com/openapi.json
  - status: 404
    url: https://www.capsocloud.com/api-docs
  - status: 200
    url: https://www.capsocloud.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/CapsoVision/repos
  - status: 202
    url: https://capsovision.com/
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: 'CapsoVision, Inc. (Nasdaq: CV) is a commercial-stage medical technology company headquartered in Saratoga, California that develops advanced imaging and artificial-intelligence technologies for gastrointestinal disease detection and screening. Its CapsoCam Plus single-use capsule endoscope captures a 360-degree panoramic view of the small-bowel mucosa without external receiver equipment, and is paired with CapsoCloud, an account-gated cloud application, and CapsoView review software for physician image review and reporting. A next-generation CapsoCam Colon system is in development. CapsoVision publishes no public developer program, API reference, or machine-readable specification; CapsoCloud is an end-user clinical web and mobile application whose JSON backend is private to the product.'
image: https://mma.prnewswire.com/media/2593739/CapsoVision_Logo_horizontal_with_tagline_Logo.jpg
layout: provider
modified: '2026-08-09'
name: CapsoVision
nav: Providers
network: true
overview: 'CapsoVision is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Capsule Endoscopy, and Gastroenterology.


  CapsoVision''s developer surface includes support and 7 more developer resources.'
random_paper: 38
score:
  band: minimal
  composite: 12.1
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
security:
- kind: domain-security
  name: Capsovision Domain Security
  slug: capsovision-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: capsovision
tags:
- Company
- Medical Devices
- Healthcare
- Capsule Endoscopy
- Gastroenterology
- Medical Imaging
- Artificial Intelligence
- Cloud Software
website: https://capsovision.com/
---
