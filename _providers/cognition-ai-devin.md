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
- description: Autonomous software engineer platform
  name: Devin
  slug: devin
artifact_total: 4
common:
- group: auth
  title: ''
  type: Compliance
  url: https://cognition.com/legal/security
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cognition-ai-devin/refs/heads/main/llms/cognition-ai-devin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cognition-ai-devin-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cognition-ai-devin/refs/heads/main/hosts/cognition-ai-devin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cognition-ai-devin-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cognition-ai-devin/refs/heads/main/vendors/cognition-ai-devin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cognition-ai-devin-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://cognition.com/legal/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cognition.com/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://cognition.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognition-ai-devin/refs/heads/main/security/cognition-ai-devin-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cognition-ai-devin-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognition-ai-devin/refs/heads/main/security/cognition-ai-devin-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cognition-ai-devin-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognition-ai-devin/refs/heads/main/security/cognition-ai-devin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cognition-ai-devin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cognition.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://cognition.com
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Cognition AI Devin is a subsidiary of Cognition that offers Devin, the first autonomous software engineer. The company builds tools that enable developers to collaborate with AI agents that can plan, write, test, and ship production code autonomously. Cognition AI Devin aims to expand human capacity by handling repetitive engineering tasks, allowing engineers to focus on architecture and problem solving. The platform integrates with existing codebases and development tools, providing a seamless AI‑augmented development experience.
image: https://cognition.com/opengraph-image.jpg?opengraph-image.0mzhc99j4lsox.jpg
layout: provider
modified: '2026-10-09'
name: Cognition Ai Devin
nav: Providers
network: true
overview: 'Cognition Ai Devin is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Autonomous Software Engineer and Enterprise AI.


  Cognition Ai Devin''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cognition Ai Devin Domain Security
  slug: cognition-ai-devin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cognition Ai Devin Vulnerability Disclosure
  slug: cognition-ai-devin-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Cognition Ai Devin Trust Center
  slug: cognition-ai-devin-trust-center
  summary_line: SOC 2, ISO 27001
slug: cognition-ai-devin
tags:
- Autonomous Software Engineer
- Enterprise AI
website: https://cognition.com
---
