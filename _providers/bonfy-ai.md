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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Bonfy.AI provides a developer API (details not publicly documented).
  name: Bonfy.AI API
  slug: bonfy-ai-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bonfy-ai/refs/heads/main/hosts/bonfy-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bonfy-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bonfy-ai/refs/heads/main/vendors/bonfy-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bonfy-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bonfy.ai/terms-use
- group: operate
  title: ''
  type: Support
  url: https://help.bonfy.ai/tickets?status=all&view=my_tickets&offset=0
- group: company
  title: ''
  type: Newsroom
  url: https://www.bonfy.ai/newsroom
- group: company
  title: ''
  type: Blog
  url: https://blog.bonfy.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bonfy-ai/refs/heads/main/security/bonfy-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bonfy-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bonfy.ai/
coverage:
  checked: '2026-10-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL spec found at discovered hosts.
  evidence:
  - status: timeout
    url: https://api.bonfy.ai/openapi.json
  - status: 404
    url: https://www.bonfy.ai/openapi.json
  - status: timeout
    url: https://api.bonfy.ai/v1/openapi.json
  - status: timeout
    url: https://api.bonfy.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: Bonfy.AI provides advanced data security solutions for enterprises, protecting against data risks, shadow AI, and ensuring contextual data enforcement across AI agents and platforms. Their offerings include data surface visibility, secure AI systems, and compliance tools for financial services, healthcare, and technology sectors, helping organizations mitigate AI‑driven threats and maintain governance.
image: https://www.bonfy.ai/hubfs/Bonfy-Featured-Image-Homepage.png
layout: provider
modified: '2026-10-02'
name: Bonfy.AI
nav: Providers
network: true
overview: 'Bonfy.AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Security, Artificial Intelligence, Enterprise, and Compliance.


  Bonfy.AI''s developer surface includes support, engineering blog, and 6 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bonfy Ai Domain Security
  slug: bonfy-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bonfy-ai
tags:
- Company
- Data Security
- Artificial Intelligence
- Enterprise
- Compliance
website: https://www.bonfy.ai/
---
