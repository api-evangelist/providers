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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/academia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.academia.edu/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/academia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.academia.edu/
- group: operate
  title: ''
  type: Support
  url: https://support.academia.edu/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/academia-edu
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.academia.edu/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.academia.edu/privacy
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/academia-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/academia-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/academia-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Academia.edu is an end-user research-sharing product with no developer program of any kind - its own 2,624-line robots.txt enumerates the whole site with no /developers, /docs or API-reference section and Disallows the internal /v0/* JSON endpoints its web client calls to every named crawler, and the GitHub org's 81 public repositories are all internal Rails tooling and forks with no client SDK or specification.
  evidence:
  - status: 404
    url: https://www.academia.edu/llms.txt
  - status: 404
    url: https://www.academia.edu/.well-known/api-catalog
  - status: 404
    url: https://www.academia.edu/.well-known/agent-card.json
  - status: 200
    url: https://www.academia.edu/robots.txt
  - status: 200
    url: https://www.academia.edu/.well-known/security.txt
  - status: 403
    url: https://www.academia.edu/
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Academia (Academia.edu, Academia Inc.) is a San Francisco based platform for sharing and discovering academic research, founded in 2008 by Richard Price. Registered researchers upload papers, build public profiles, follow research interests and track readership analytics across a corpus of tens of millions of documents, and the company also runs the Academia journals program and sells Academia Premium subscriptions for advanced search, mentions, reader analytics and bulk PDF downloads. Academia publishes no public developer program, API reference or machine-readable specification; the /v0 JSON endpoints its own web client calls are explicitly disallowed to crawlers in robots.txt. It does publish an RFC 9116 security.txt with a named security contact and a disclosure posture, and a long per-crawler robots.txt that names AI and agent user-agents individually.
image: https://www.academia.edu/favicon.ico
layout: provider
modified: '2026-08-06'
name: Academia
nav: Providers
network: true
overview: 'Academia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Academic Research, research-papers, Scholarly Publishing, and Higher Education.


  Academia''s developer surface includes support and 10 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 14.0
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
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 14.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 37.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/academia/refs/heads/main/screenshots/academia-2026-08-07T160744.png
security:
- kind: domain-security
  name: Academia Domain Security
  slug: academia-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Academia Vulnerability Disclosure
  slug: academia-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: academia
tags:
- Company
- Academic Research
- research-papers
- Scholarly Publishing
- Higher Education
- Open Access
- academic-social-network
- Preprints
- research-discovery
website: https://www.academia.edu/
---
