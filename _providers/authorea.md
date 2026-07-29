---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.authorea.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/authorea
- group: agent
  title: ''
  type: WellKnown
  url: well-known/authorea-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/authorea-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/authorea-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.authorea.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/authorea-domain-security.yml
created: '2026-07-17'
description: Authorea is a collaborative online platform for writing, editing, reviewing, and publishing scholarly and scientific documents. Founded in 2012 by Alberto Pepe and Nathan Jenkins, it lets researchers co-author articles in rich text or LaTeX, manage citations and references, embed data, figures, and code, run version-controlled review, and export to journal-specific styles. Authorea was acquired by Atypon in 2018 and is now operated as part of John Wiley & Sons, hosted on Atypon's Literatum publishing platform, where it supports preprints, journal submission, and open collaboration for the research community. It has no public developer API today; its earlier REST API was retired after the Wiley/Atypon acquisition, and the GitHub organization now publishes only document-processing tooling (LaTeXML, Pandoc, TeX styling) rather than API client SDKs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/authorea.png
layout: provider
modified: '2026-07-18'
name: Authorea
nav: Providers
network: true
overview: Authorea is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Scholarly Publishing, Academic Writing, Collaboration, and Research.
random_paper: 67
score:
  band: minimal
  composite: 8.2
  delta: -0.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 8.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Authorea Domain Security
  slug: authorea-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Authorea Vulnerability Disclosure
  slug: authorea-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: authorea
tags:
- Company
- Scholarly Publishing
- Academic Writing
- Collaboration
- Research
- Preprints
- LaTeX
- Wiley
website: https://www.authorea.com
---
