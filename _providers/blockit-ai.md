---
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/blockit-ai/llms/blockit-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blockit-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/blockit-ai/well-known/blockit-ai-security-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blockit-ai-security-security.txt
- group: agent
  href: https://artifacts.apis.io/blockit-ai/well-known/blockit-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blockit-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/blockit-ai/hosts/blockit-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blockit-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/blockit-ai/vendors/blockit-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blockit-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/blockit-ai/security/blockit-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blockit-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blockit.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.blockit.com
- group: company
  title: ''
  type: Blog
  url: https://www.blockit.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blockit.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blockit.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.blockit.com/contact
coverage:
  checked: '2026-10-24'
  detail: The provider's website does not expose any machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.blockit.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: Blockit AI provides an AI‑powered scheduling assistant that automates calendar management, meeting coordination, and time‑zone handling for individuals and teams. Leveraging natural language understanding, Blockit can parse conversational requests, suggest optimal meeting times, and integrate with major calendar platforms. The service targets productivity‑focused users and enterprises seeking to reduce the friction of scheduling, offering a free tier and paid plans with advanced features such as team collaboration, analytics, and custom integrations. Backed by Sequoia Capital, Blockit aims to become the go‑to virtual assistant for time management.
image: https://www.blockit.com/assets/og-blockit.png
layout: provider
modified: '2026-10-23'
name: Blockit AI
nav: Providers
network: true
overview: 'Blockit AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Scheduling, Productivity, and Calendar.


  Blockit AI''s developer surface includes documentation, engineering blog, support, and 9 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blockit Ai Domain Security
  slug: blockit-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: blockit-ai
tags:
- Company
- AI
- Scheduling
- Productivity
- Calendar
website: https://www.blockit.com
---
