---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/knoetic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cpohq.com
- group: start
  title: ''
  type: Login
  url: https://app.knoetic.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.knoetic.com
- group: auth
  title: ''
  type: Compliance
  url: https://trust.knoetic.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/knoetic
- group: company
  title: ''
  type: Careers
  url: https://cpohq.com/careers
- group: auth
  title: ''
  type: TrustCenter
  url: security/knoetic-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/knoetic-llms.txt
created: '2026-07-17'
description: 'Knoetic is an HR technology company that operates CPOHQ, a platform built for Chief People Officers and senior people-function executives. The product combines three surfaces: a private, invite-only community of 3,000+ Chief People Officers (one member per company) who exchange confidential playbooks and benchmarks; an AI "Chief of Staff" that delivers personalized morning briefings and monitors market and talent trends; and a suite of workflow-specific AI agents for people analytics, performance insight, and peer benchmarking across the people function. The company was founded as Knoetic around a people-analytics product and has since consolidated its public brand on CPOHQ — knoetic.com now redirects to cpohq.com, while the customer application remains at app.knoetic.com. Knoetic has raised $50M+ from Accel, EQT Ventures, Menlo Ventures and angel investors. As of this enrichment pass Knoetic publishes no public API, developer portal, SDKs, or API documentation; the platform
  is a closed B2B SaaS offering sold to enterprise people teams. It does publish a Vanta-hosted trust center and displays a SOC 2 Type II attestation.'
image: https://cpohq.com/cpohq-social-preview.png
layout: provider
modified: '2026-07-19'
name: Knoetic
nav: Providers
network: true
overview: Knoetic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HR Tech, People Analytics, Human Resources, and Workforce Analytics.
random_paper: 14
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/knoetic/refs/heads/main/screenshots/knoetic-2026-07-25T224041.png
security:
- kind: domain-security
  name: Knoetic Domain Security
  slug: knoetic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Knoetic Trust Center
  slug: knoetic-trust-center
  summary_line: SOC 2 Type II
slug: knoetic
tags:
- Company
- HR Tech
- People Analytics
- Human Resources
- Workforce Analytics
- Artificial Intelligence
- AI Agents
- Software-as-a-Service
- Community
- Benchmarking
website: https://cpohq.com
---
