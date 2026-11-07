---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Basepic Com Agentic Access
  operation_count: 4
  slug: basepic-com-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- description: Upload an image, edit it, and get shareable links. Free, no API key.
  name: BasePic API
  slug: basepic-api
- baseURL: https://basepic.com
  baseurl_source: declared
  description: The Images API from BasePic — 3 operation(s) for images.
  name: BasePic Images API
  slug: basepic-com-images-api
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/basepic-com/well-known/basepic-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/basepic-com-security.txt
- group: agent
  href: https://artifacts.apis.io/basepic-com/well-known/basepic-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/basepic-com-well-known.yml
- group: agent
  href: https://artifacts.apis.io/basepic-com/agentic-access/basepic-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/basepic-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/basepic-com/rules/basepic-com-rules.yml
  title: ''
  type: Spectral
  url: rules/basepic-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/basepic-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/basepic-com/errors/basepic-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/basepic-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/basepic-com/conformance/basepic-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/basepic-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/basepic-com/llms/basepic-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/basepic-com-llms.txt
- group: other
  href: https://artifacts.apis.io/basepic-com/hosts/basepic-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/basepic-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/basepic-com/security/basepic-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/basepic-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://basepic.com
- group: docs
  title: ''
  type: Documentation
  url: https://basepic.com/
- group: docs
  title: ''
  type: APIReference
  url: https://basepic.com/llms.txt
created: '2026-10-26'
description: BasePic provides free image, video and file hosting services with direct links. Users can upload files up to 2 GB without registration, receiving short shareable URLs and direct download links. The platform offers tools such as image resizing, HEIC conversion, video compression, and document scanning, all performed in-browser without watermarks or sign‑up requirements.
image: https://basepic.com/og.png
layout: provider
modified: '2026-10-26'
name: BasePic
nav: Providers
network: true
overview: 'BasePic publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Images API, and 1 more. Tagged areas include Company, Image Hosting, File Sharing, and Video Hosting.


  The BasePic catalog on APIs.io includes 1 Spectral governance ruleset.


  BasePic''s developer surface includes documentation, API reference, and 11 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: BasePic API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: basepic-com-rules
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 42.9
    developer_ergonomics: 14.8
    discoverability: 64.3
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/basepic-com/basepic-com-2026-11-03T121550.png
security:
- kind: domain-security
  name: Basepic Com Domain Security
  slug: basepic-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: image-management
  slug: basepic-com-image-management
slug: basepic-com
tags:
- Company
- Image Hosting
- File Sharing
- Video Hosting
website: https://basepic.com
---
