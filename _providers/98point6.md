---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/98point6-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.98point6.com/
- group: company
  title: ''
  type: Blog
  url: https://www.98point6.com/blogs/
- group: operate
  title: ''
  type: Support
  url: https://help.98point6.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/98point6
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.98point6.com/legal-and-privacy/#licenseagreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.98point6.com/legal-and-privacy/#privacypolicy
- group: auth
  title: ''
  type: Security
  url: https://www.98point6.com/responsible-disclosure-policy/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/98point6-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/98point6-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/98point6-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/98point6-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/98point6-conformance.yml
coverage:
  checked: '2026-08-06'
  detail: 98point6 licenses its virtual care platform — including the HL7/FHIR EMR integration and the branded-patient-experience SDK its own platform page advertises — only under a commercial agreement, so the entire public web presence is a fifteen-page WordPress marketing site whose only route to the integration surface is the "schedule a demo" form; developer.98point6.com, docs.98point6.com and api.98point6.com do not resolve in DNS at all.
  evidence:
  - status: 200
    url: https://www.98point6.com/platform/
  - status: 200
    url: https://www.98point6.com/campaign/schedule-demo/
  - status: 404
    url: https://www.98point6.com/developers/
  - status: 404
    url: https://www.98point6.com/.well-known/api-catalog
  - status: 404
    url: https://www.98point6.com/openapi.json
  - status: 200
    url: https://github.com/98point6
  reason: sales-gate
  state: gated
created: '2026-08-06'
description: 98point6 Technologies is a Seattle-based digital health software company, founded in 2015, that builds and licenses a cloud-based virtual care platform to health systems, payers and virtual care providers. After selling its own care-delivery division in 2023 it operates purely as a licensed software provider. The platform combines an AI-driven Automated Assistant for patient intake and visit documentation, a web-based Clinician Console with automated clinical decision support, and a white-labeled patient application, covering both asynchronous and real-time (messaging, audio, video) care. It advertises HL7 and FHIR based EMR integration with Epic and Cerner, SSO for patient login, and an SDK for building a fully branded patient experience, but that integration surface is delivered under a licensing agreement, so no developer portal, API reference or machine-readable specification is published publicly.
image: https://staging-marketing-uploads-gravitate-98point6-com.s3.us-west-2.amazonaws.com/uploads/2023/05/31164354/cropped-Brand_icon_transparent_bg-192x192.png
layout: provider
modified: '2026-08-06'
name: 98point6 Technologies
nav: Providers
network: true
overview: '98point6 Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Care, Telehealth, Virtual Care, and Digital Health.


  98point6 Technologies'' developer surface includes engineering blog, support, and 11 more developer resources.'
random_paper: 25
score:
  band: emerging
  composite: 19.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 19.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 38.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/98point6/refs/heads/main/screenshots/98point6-2026-08-07T160721.png
security:
- kind: domain-security
  name: 98Point6 Domain Security
  slug: 98point6-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 98Point6 Vulnerability Disclosure
  slug: 98point6-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: 98point6
tags:
- Company
- Health Care
- Telehealth
- Virtual Care
- Digital Health
- Electronic Health Records
- Clinical Decision Support
- Artificial Intelligence
- Software
website: https://www.98point6.com/
---
