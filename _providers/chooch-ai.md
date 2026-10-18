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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chooch-ai/refs/heads/main/llms/chooch-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chooch-ai-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chooch-ai/refs/heads/main/hosts/chooch-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chooch-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chooch-ai/refs/heads/main/vendors/chooch-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chooch-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chooch.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chooch.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.chooch.com/news/
- group: company
  title: ''
  type: Blog
  url: https://www.chooch.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chooch-ai/refs/heads/main/security/chooch-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chooch-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chooch.com/
coverage:
  checked: '2026-10-08'
  detail: No public developer documentation or API specification was found on the company website.
  evidence:
  - status: 404
    url: https://www.chooch.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Chooch AI provides computer vision AI solutions focused on hospital inventory management, safety monitoring, remote patient monitoring, and manufacturing. Their platform automates inventory tracking, predicts shortages, and enhances safety through vision AI, helping healthcare facilities reduce costs and improve operational efficiency.
image: https://www.chooch.com/wp-content/uploads/2025/04/chooch-autonomous-ai-for-healthcare-facility-safety-care-1024x576.jpg
layout: provider
modified: '2026-10-08'
name: Chooch AI
nav: Providers
network: true
overview: 'Chooch AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Computer Vision, Healthcare, and Inventory.


  Chooch AI''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chooch Ai Domain Security
  slug: chooch-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chooch-ai
tags:
- Company
- Artificial Intelligence
- Computer Vision
- Healthcare
- Inventory
website: https://www.chooch.com/
---
