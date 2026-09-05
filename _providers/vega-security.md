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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/vega-security-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vega-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vega.io/
- group: company
  title: ''
  type: Blog
  url: https://vega.io/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vega.io/
- group: start
  title: ''
  type: Login
  url: https://app.vega.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vegasecurity
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vega.io/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vega-security-lifecycle.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.vega.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vega.io/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vega-security-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vega-security-well-known.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.vega.io/
- group: company
  title: ''
  type: About
  url: https://vega.io/about
- group: company
  title: ''
  type: Careers
  url: https://vega.io/careers
- group: company
  title: ''
  type: Partners
  url: https://vega.io/partners
created: '2026-07-17'
description: Vega (vega.io) is an AI-native security operations platform that bills itself as the operating system for agentic SecOps in the post-SIEM era. Its Security Analytics Mesh (SAM) federates queries across security data sources in place -- with no ingestion, migration, or egress -- and powers agentic detection engineering, autonomous alert triage, and security analytics, continuously assessing detection coverage against MITRE ATT&CK. Backed by Accel. The product app and documentation are login-gated and no public API surface has been published yet.
image: https://cdn.prod.website-files.com/68791f04ead01339340acbbe/687e5eab154f5a8607c2f647_webclip.png
layout: provider
modified: '2026-07-21'
name: Vega Security
nav: Providers
network: true
overview: 'Vega Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Security Operations, SIEM, and Agentic AI.


  Vega Security''s developer surface includes engineering blog, documentation, and 15 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 15.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vega-security/refs/heads/main/screenshots/vega-security-2026-09-02T165558.png
security:
- kind: domain-security
  name: Vega Security Domain Security
  slug: vega-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vega Security Trust Center
  slug: vega-security-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CSA STAR
slug: vega-security
tags:
- Company
- Cybersecurity
- Security Operations
- SIEM
- Agentic AI
- Threat Detection
- Security Analytics
website: https://vega.io/
---
