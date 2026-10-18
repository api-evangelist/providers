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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Napier AI AML platform providing endpoints for client screening, transaction monitoring, and risk assessment.
  name: Napier AI API
  slug: napier-ai-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/napier-ai/refs/heads/main/llms/napier-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/napier-ai-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/napier-ai/refs/heads/main/hosts/napier-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/napier-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/napier-ai/refs/heads/main/vendors/napier-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/napier-ai-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.napier.ai/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.napier.ai/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/napier-ai/refs/heads/main/security/napier-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/napier-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.napier.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.napier.ai/resources
- group: company
  title: ''
  type: Blog
  url: https://www.napier.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.napier.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.napier.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.napier.ai/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.napier.ai/request-a-demo
coverage:
  checked: '2026-10-14'
  detail: Napier AI provides documentation pages but no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL contracts were found on its hosts.
  evidence:
  - status: 0
    url: https://api.napier.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Napier AI provides an AI‑powered Anti‑Money Laundering platform that helps financial institutions combat evolving threats. Their Continuum suite offers solutions for client screening, transaction monitoring, and risk assessment across banking, payments, and wealth management sectors. The platform combines machine learning with regulatory expertise to reduce false positives and streamline compliance workflows, delivering real‑time insights and automated reporting for modern AML operations.
image: https://cdn.prod.website-files.com/5c41f7230ea8d5489c8ce748/696e1686870fc026127c57a9_opengraph-img.png
layout: provider
modified: '2026-10-14'
name: Napier AI
nav: Providers
network: true
overview: 'Napier AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AML, Fintech, and Compliance.


  Napier AI''s developer surface includes documentation, engineering blog, support, signup flow, and 9 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Napier Ai Domain Security
  slug: napier-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: napier-ai
tags:
- Company
- Artificial Intelligence
- AML
- Fintech
- Compliance
website: https://www.napier.ai
---
