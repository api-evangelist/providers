---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/causalyinc/refs/heads/main/llms/causalyinc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/causalyinc-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/causalyinc/refs/heads/main/a2a/causalyinc-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/causalyinc-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/causalyinc/refs/heads/main/well-known/causalyinc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/causalyinc-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/causalyinc/refs/heads/main/hosts/causalyinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/causalyinc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/causalyinc/refs/heads/main/vendors/causalyinc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/causalyinc-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.causaly.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.causaly.com/legal/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.causaly.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.causaly.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.causaly.com/resources/news
- group: company
  title: ''
  type: Blog
  url: https://www.causaly.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/causaly
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/causalyinc/refs/heads/main/security/causalyinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/causalyinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.causaly.com
coverage:
  checked: '2026-10-07'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on any discovered host.
  evidence:
  - status: 404
    url: https://api.causaly.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Causalyinc (Causaly) provides an agentic AI platform for life sciences, offering a biomedical knowledge graph, AI‑powered research tools, and data‑fabric solutions to accelerate drug discovery and development. The platform integrates generative AI copilots, scientific workflows, and enterprise data integration to help pharma and biotech teams uncover insights, mitigate clinical failures, and streamline target identification.
image: https://cdn.prod.website-files.com/66a8e5ccd2c6460e01d4d385/672df2a4ee2a2b11a52a6c72_OG%20Image%20-%20Home.png
layout: provider
modified: '2026-10-07'
name: Causalyinc
nav: Providers
network: true
overview: 'Causalyinc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Life Sciences, Drug Discovery, and Biomedical.


  Causalyinc''s developer surface includes engineering blog and 13 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Causalyinc Domain Security
  slug: causalyinc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: causalyinc
tags:
- Company
- Artificial Intelligence
- Life Sciences
- Drug Discovery
- Biomedical
website: https://www.causaly.com
---
