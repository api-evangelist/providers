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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/yurts-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/yurts-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yurts-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.legionintel.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/yurts_stock/
- group: company
  title: ''
  type: Blog
  url: https://www.legionintel.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.legionintel.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.legionintel.com/terms-of-use-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.legionintel.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.legionintel.com/security
- group: auth
  title: ''
  type: Compliance
  url: conformance/yurts-conformance.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/YurtsAI
- group: start
  title: ''
  type: Login
  url: https://platform.legionintel.com/auth/signin
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yurts-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/yurts-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/yurts-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/yurts-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/yurts-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yurts-rate-limits.yml
coverage:
  checked: '2026-09-04'
  detail: 'Legion Intelligence (formerly Yurts) states in its own llms.txt that the platform supports MCP and "offers REST API extensibility", but there is no public developer portal: its sitemap has no /pricing, /docs or /developers entry, docs.legionintel.com is a dead Cloudflare origin whose plain-HTTP root 302s to an internal https://drive.google.com/a/legionintel.com, api.legionintel.com returns a zero-byte 404 for every path including the control probe, and platform.legionintel.com redirects every unknown path to /auth/signin — the interface is delivered inside a customer''s accredited deployment, not published.'
  evidence:
  - status: 525
    url: https://docs.legionintel.com/
  - status: 302
    url: http://docs.legionintel.com/
  - status: 404
    url: https://api.legionintel.com/openapi.json
  - status: 200
    url: https://platform.legionintel.com/auth/signin
  - status: 200
    url: https://www.legionintel.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-09-04'
description: Yurts (Yurts AI / Yurts Technologies, Inc.) is a San Rafael, California generative-AI company founded in 2022 that rebranded to Legion Intelligence, Inc. in April 2025; yurts.ai now redirects to legionintel.com. Legion builds governed, agentic AI for national security — AI agents that search, chat, draft and automate work across the systems defense, intelligence, energy, aerospace, manufacturing and MRO teams already use, with human command, scoped permissions and full attribution on every agent action. It ships as Legion Packs (role-based capability bundles) and Centurion, a deployable edge system for DDIL environments, and runs in cloud, on-prem, air-gapped and classified environments from IL2 through IL6. The company states the platform connects to 100+ systems, supports the Model Context Protocol and offers REST API extensibility, but publishes no public developer portal, API reference or machine-readable contract — the interface surface is delivered inside a customer deployment.
image: https://cdn.prod.website-files.com/680a8bc2d69bace9040bd4b1/68374e4d176f165b4380d743_3b24a0d733e3fae9510ffd4ef17d5e22_Legion-OG-1200x620.webp
layout: provider
modified: '2026-09-04'
name: Yurts
nav: Providers
network: true
overview: 'Yurts is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Agentic AI, National Security, and Defense.


  Yurts'' developer surface includes engineering blog, support, and 17 more developer resources.'
plans:
- name: Yurts Plans Pricing
  plan_count: 0
  slug: yurts-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Yurts Rate Limits
  slug: yurts-rate-limits
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 25.7
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 55.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Yurts Domain Security
  slug: yurts-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Yurts Vulnerability Disclosure
  slug: yurts-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Yurts Trust Center
  slug: yurts-trust-center
  summary_line: SOC 2 Type 2, SOC 1 Type 2, FedRAMP High, CMMC Level 2, NIST 800-53, HIPAA, GDPR, ITAR, DoD Impact Level IL2-IL6
slug: yurts
tags:
- Company
- Artificial Intelligence
- Agentic AI
- National Security
- Defense
- Generative AI
- Enterprise Search
- Retrieval Augmented Generation
- Edge AI
- Government
website: https://www.legionintel.com/
---
