---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/directcase-ai/authentication/directcase-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/directcase-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/directcase-ai/conformance/directcase-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/directcase-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/directcase-ai/llms/directcase-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/directcase-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/directcase-ai/hosts/directcase-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/directcase-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.directcase.ai/gb/en/terms
- group: operate
  title: ''
  type: Support
  url: https://www.directcase.ai/gb/en/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.directcase.ai/gb/en/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.directcase.ai/gb/en/news
- group: docs
  title: ''
  type: Documentation
  url: https://www.directcase.ai/gb/en/docs/mcp
- group: company
  title: ''
  type: Blog
  url: https://blog.directcase.ai/cs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/directcase
- group: auth
  href: https://artifacts.apis.io/directcase-ai/security/directcase-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/directcase-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://directcase.ai/
coverage:
  checked: '2026-11-05'
  detail: Documentation pages are HTML without any published OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://www.directcase.ai/gb/en/docs/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DirectCase provides AI‑powered legal research, offering verified citations across European case law and legislation. Users receive up to ten free queries without a credit card, and the platform supports lawyers, solicitors, barristers and trainees. The service aims to streamline legal workflows with accurate, sourced information.
image: https://directcase-cms-uploads.s3.eu-north-1.amazonaws.com/directcase_og_en_bb92b1158b.webp
layout: provider
modified: '2026-11-05'
name: DirectCase
nav: Providers
network: true
overview: 'DirectCase is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Legal Tech, Artificial Intelligence, Research, Law, and Software-as-a-Service.


  DirectCase''s developer surface includes authentication, support, documentation, engineering blog, and 9 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Directcase Ai Authentication
  slug: directcase-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Directcase Ai Domain Security
  slug: directcase-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: directcase-ai
tags:
- Legal Tech
- Artificial Intelligence
- Research
- Law
- Software-as-a-Service
website: https://directcase.ai/
---
