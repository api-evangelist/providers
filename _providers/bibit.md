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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bibit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://bibit.id/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bibit-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bibit-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bibit-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bibit-llms.txt
- group: company
  title: ''
  type: Website
  url: https://bibit.id
- group: company
  title: ''
  type: Blog
  url: https://blog.bibit.id
- group: operate
  title: ''
  type: Support
  url: https://faq.bibit.id/id/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bibit.id/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bibit.id/term
created: '2026-07-17'
description: Bibit is an Indonesian retail investment application that lets everyday users invest in mutual funds (reksa dana), government bonds (SBN/SBR/ORI), fixed-rate bonds, and stocks. Built for beginner investors, it uses robo-advisor technology to recommend diversified portfolios and is licensed by Indonesia's financial regulator OJK. Bibit operates within the Stockbit group and is a portfolio company of Prosus Ventures. As of this profile no public developer API, SDK, or developer portal is published; this repo tracks the company's public surface (security.txt, legal, help, blog) for the API Evangelist network.
image: https://assets.bibit.id/logos/thumbnail-bibit.jpg
layout: provider
modified: '2026-07-18'
name: Bibit
nav: Providers
network: true
overview: 'Bibit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Investment, Mutual Funds, and Wealth Management.


  Bibit''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 12.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Bibit Domain Security
  slug: bibit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bibit Vulnerability Disclosure
  slug: bibit-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bibit
tags:
- Company
- Fintech
- Investment
- Mutual Funds
- Wealth Management
- Indonesia
- Consumer Finance
website: https://bibit.id
---
