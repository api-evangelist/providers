---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Codewords Agentic Access
  operation_count: 3
  slug: codewords-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- baseURL: https://runtime.codewords.ai
  baseurl_source: declared
  description: Run deployed CodeWords services and fetch results.
  name: Agemo Workflows API
  slug: codewords-workflows-api
artifact_total: 5
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/codewords/refs/heads/main/agentic-access/codewords-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/codewords-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/codewords/refs/heads/main/plans/codewords-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/codewords-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/codewords/refs/heads/main/rules/codewords-rules.yml
  title: ''
  type: Spectral
  url: rules/codewords-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/codewords/refs/heads/main/vocabulary/codewords-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/codewords-vocabulary.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/codewords/refs/heads/main/changelog/codewords-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/codewords-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/codewords/refs/heads/main/errors/codewords-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/codewords-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/codewords/refs/heads/main/conformance/codewords-conformance.yml
  title: ''
  type: Conformance
  url: conformance/codewords-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/codewords/refs/heads/main/llms/codewords-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/codewords-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/codewords/refs/heads/main/well-known/codewords-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/codewords-chatgpt-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/codewords/refs/heads/main/well-known/codewords-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/codewords-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/codewords/refs/heads/main/hosts/codewords-hosts.yml
  title: ''
  type: Hosts
  url: hosts/codewords-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/codewords/refs/heads/main/vendors/codewords-vendors.yml
  title: ''
  type: Vendors
  url: vendors/codewords-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.codewords.ai/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.codewords.ai/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://www.codewords.ai/developers
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/codewords/refs/heads/main/security/codewords-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/codewords-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.codewords.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.codewords.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.codewords.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.codewords.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.codewords.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.codewords.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.codewords.ai/support
created: '2026-10-16'
description: Agemo, operating under the brand CodeWords, provides AI‑driven workflow automation that lets users describe processes in natural language and instantly generate live WhatsApp and other tool integrations. The platform offers a visual UI, templates, and a marketplace of agents powered by Claude, ChatGPT, or Cursor, targeting businesses seeking to streamline repetitive tasks without building code. It emphasizes ease of use, rapid deployment, and extensibility through a growing ecosystem of connectors and custom agents.
image: https://www.codewords.ai/assets/cdn.prod.website-files.com/6946a9915525f9a896b45f44/69e8f4a48b849d5aa136d146_thumbnail-preview-2.png
layout: provider
modified: '2026-10-16'
name: Agemo
nav: Providers
network: true
overview: 'Agemo publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Workflows API. Tagged areas include Artificial Intelligence, Automation, Workflows, No-Code, and Software-as-a-Service.


  The Agemo catalog on APIs.io includes 1 Spectral governance ruleset.


  Agemo''s developer surface includes changelog, API reference, documentation, engineering blog, pricing, support, and 17 more developer resources.'
plans:
- name: Codewords Plans Pricing
  plan_count: 3
  slug: codewords-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Agemo API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: codewords-rules
score:
  band: developing
  composite: 44.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 49.0
    developer_ergonomics: 23.8
    discoverability: 73.2
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Codewords Domain Security
  slug: codewords-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: codewords
tags:
- Artificial Intelligence
- Automation
- Workflows
- No-Code
- Software-as-a-Service
- Productivity
website: https://www.codewords.ai/
---
