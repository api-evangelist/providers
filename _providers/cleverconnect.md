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
- description: Developer portal provides integration details.
  name: CleverConnect API
  slug: cleverconnect-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cleverconnect/refs/heads/main/llms/cleverconnect-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cleverconnect-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cleverconnect/refs/heads/main/hosts/cleverconnect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cleverconnect-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cleverconnect/refs/heads/main/vendors/cleverconnect-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cleverconnect-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cleverconnect.com/legal-notice
- group: operate
  title: ''
  type: Support
  url: https://help.cleverconnect.com/en/knowledgebase
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cleverconnect.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.cleverconnect.com/newsroom
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.cleverconnect.com/
- group: company
  title: ''
  type: Blog
  url: https://www.cleverconnect.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.cleverconnect.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cleverconnect/refs/heads/main/security/cleverconnect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cleverconnect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cleverconnect.com/
coverage:
  checked: '2026-10-09'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract discovered despite developer portal presence.
  evidence:
  - status: 200
    url: https://portal.cleverconnect.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: CleverConnect is an award‑winning talent acquisition platform that empowers HR teams with AI‑driven candidate relationship management, CRM, and recruitment automation. The service helps organizations streamline hiring, improve candidate experience, and reduce costs through secure, data‑driven insights and integrations.
image: https://cdn.prod.website-files.com/659d0760749449f0e55f7b53/67cafe60da569e1cfffd24bf_cleverconnect-opengraph-meta-image.avif
layout: provider
modified: '2026-10-08'
name: CleverConnect
nav: Providers
network: true
overview: 'CleverConnect is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Talent Acquisition, Artificial Intelligence, Recruiting, and HR Technology.


  CleverConnect''s developer surface includes support, engineering blog, documentation, and 9 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.1
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
  name: Cleverconnect Domain Security
  slug: cleverconnect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cleverconnect
tags:
- Company
- Talent Acquisition
- Artificial Intelligence
- Recruiting
- HR Technology
website: https://www.cleverconnect.com/
---
