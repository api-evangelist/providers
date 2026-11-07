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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/ciromaciel-click/llms/ciromaciel-click-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ciromaciel-click-llms.txt
- group: agent
  href: https://artifacts.apis.io/ciromaciel-click/well-known/ciromaciel-click-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ciromaciel-click-well-known.yml
- group: other
  href: https://artifacts.apis.io/ciromaciel-click/hosts/ciromaciel-click-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ciromaciel-click-hosts.yml
- group: other
  href: https://artifacts.apis.io/ciromaciel-click/vendors/ciromaciel-click-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ciromaciel-click-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ciromaciel.click/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://ciromaciel.click/legal/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ciromaciel.click/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ciro-maciel
- group: company
  title: ''
  type: Blog
  url: https://blog.ciromaciel.click
- group: auth
  href: https://artifacts.apis.io/ciromaciel-click/security/ciromaciel-click-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ciromaciel-click-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ciromaciel.click/
coverage:
  checked: '2026-11-04'
  detail: GraphQL endpoint https://blob.ciromaciel.click/graphql returns 401 Unauthorized, blocking contract discovery.
  evidence:
  - status: 401
    url: https://blob.ciromaciel.click/graphql
  reason: auth-required
  state: gated
created: '2026-11-03'
description: Ciro Cesar Maciel is a software engineer with over twenty years of experience, author of books like O Novo Básico, creator of AI tools and infrastructure for applications. He shares knowledge through blogs, videos, and open-source projects, focusing on building with AI, programming education, and software architecture.
image: https://ciromaciel.click/opengraph.webp
layout: provider
modified: '2026-11-03'
name: Ciro Cesar Maciel
nav: Providers
network: true
overview: 'Ciro Cesar Maciel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Software Engineer, AI Tools, Open Source, Education, and Architecture.


  Ciro Cesar Maciel''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 7.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ciromaciel Click Domain Security
  slug: ciromaciel-click-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ciromaciel-click
tags:
- Software Engineer
- AI Tools
- Open Source
- Education
- Architecture
website: https://ciromaciel.click/
---
