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
  band: agent-aware
  dimensions:
    agent_card: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/docdiffai-com/llms/docdiffai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docdiffai-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/docdiffai-com/well-known/docdiffai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docdiffai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/docdiffai-com/hosts/docdiffai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docdiffai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/docdiffai-com/vendors/docdiffai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docdiffai-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docdiffai.com/terms
- group: operate
  title: ''
  type: Support
  url: https://docdiffai.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docdiffai.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://docdiffai.com/blog
- group: auth
  href: https://artifacts.apis.io/docdiffai-com/security/docdiffai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docdiffai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docdiffai.com/
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on any discovered host.
  evidence:
  - status: 0
    url: https://api.docdiffai.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DocDiffAI provides a web-based service that compares two versions of business documents such as contracts, proposals, policies, or reports. It highlights wording changes, flags potentially important differences, and links each finding to the original source page. The platform offers a free deterministic diff for up to 100 combined pages and paid AI‑enhanced reviews with citation support, ensuring users can quickly understand revisions without needing an account.
image: https://docdiffai.com/og/docdiffai.webp
layout: provider
modified: '2026-11-05'
name: DocDiffAI
nav: Providers
network: true
overview: 'DocDiffAI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Document-Comparison, Artificial Intelligence, Software-as-a-Service, Legal Tech, and Contract Management.


  DocDiffAI''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Docdiffai Com Domain Security
  slug: docdiffai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: docdiffai-com
tags:
- Document-Comparison
- Artificial Intelligence
- Software-as-a-Service
- Legal Tech
- Contract Management
- Company
website: https://docdiffai.com/
---
