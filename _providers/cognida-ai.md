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
- description: Enterprise AI automation API (no machine-readable spec discovered)
  name: Cognida AI API
  slug: cognida-ai-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cognida-ai/refs/heads/main/hosts/cognida-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cognida-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cognida-ai/refs/heads/main/vendors/cognida-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cognida-ai-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://main.cognida.ai/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://main.cognida.ai/press/cognida-acquires-automate
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognida-ai/refs/heads/main/security/cognida-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cognida-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://main.cognida.ai/
coverage:
  checked: '2026-10-09'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.cognida.ai/openapi.json
  - status: 403
    url: https://automate.cognida.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Cognida.ai provides enterprise AI solutions that bridge the gap between frontier AI capabilities and production systems. The company offers practical AI and data solutions for enterprises, including AI builders, FDE+ solutions, and automation tools. Their platform helps organizations automate finance, operations, and other business processes, delivering scalable, secure, and compliant AI implementations. Cognida.ai also offers consulting, integration, and support services to accelerate AI adoption across industries.
image: https://cdn.prod.website-files.com/68ff6d1fc0c7cde76abdc93b/6a88633e5462a02263a224a0_OG%20Image.png
layout: provider
modified: '2026-10-09'
name: Cognida.ai
nav: Providers
network: true
overview: Cognida.ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Enterprise, Automation, Data, and Platform.
random_paper: 4
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cognida Ai Domain Security
  slug: cognida-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cognida-ai
tags:
- Artificial Intelligence
- Enterprise
- Automation
- Data
- Platform
- Company
website: https://main.cognida.ai/
---
