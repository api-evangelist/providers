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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Katonic provides an operating system for sovereign AI with various solutions.
  name: Katonic API
  slug: katonic-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/katonic/well-known/katonic-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/katonic-www-security.txt
- group: auth
  title: ''
  type: Compliance
  url: https://katonic.ai/trust
- group: auth
  title: ''
  type: Security
  url: https://katonic.ai/responsible-ai
- group: agent
  href: https://artifacts.apis.io/katonic/llms/katonic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/katonic-llms.txt
- group: auth
  href: https://artifacts.apis.io/katonic/well-known/katonic-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/katonic-security.txt
- group: agent
  href: https://artifacts.apis.io/katonic/well-known/katonic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/katonic-well-known.yml
- group: other
  href: https://artifacts.apis.io/katonic/hosts/katonic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/katonic-hosts.yml
- group: build
  href: https://artifacts.apis.io/katonic/packages/katonic-packages.yml
  title: ''
  type: SDKs
  url: packages/katonic-packages.yml
- group: build
  href: https://artifacts.apis.io/katonic/packages/katonic-packages.yml
  title: ''
  type: Packages
  url: packages/katonic-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://katonic.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://katonic.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/katonic-dev
- group: company
  title: ''
  type: Blog
  url: https://www.katonic.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://developers.katonic.ai/
- group: auth
  href: https://artifacts.apis.io/katonic/security/katonic-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/katonic-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/katonic/security/katonic-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/katonic-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/katonic/security/katonic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/katonic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://katonic.ai/
coverage:
  checked: '2026-10-20'
  detail: Docs endpoint returns 401 Unauthorized, indicating authentication required.
  evidence:
  - status: 401
    url: https://docs.katonic.ai/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-20'
description: Katonic.ai provides an operating system for sovereign AI, enabling enterprises to run AI workloads on their own infrastructure. The platform offers a suite of solutions across banking, government, telecommunications, healthcare, manufacturing, retail, energy, and insurance, with tools like AI Factory, Workroom, Studio, Control Room, AI Gateway, and Knowledge Engine. Katonic emphasizes security, responsible AI, and partnership integrations with NVIDIA, Cisco, Red Hat, and others, positioning itself as a comprehensive AI operating system for various industry needs.
image: https://www.katonic.ai/images/blog-og/og-image.png
layout: provider
modified: '2026-10-20'
name: Katonic.ai
nav: Providers
network: true
overview: 'Katonic.ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Enterprise, Sovereign AI, and Platform.


  Katonic.ai''s developer surface includes engineering blog, documentation, and 16 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Katonic Domain Security
  slug: katonic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Katonic Vulnerability Disclosure
  slug: katonic-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Katonic Trust Center
  slug: katonic-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: katonic
tags:
- Company
- Artificial Intelligence
- Enterprise
- Sovereign AI
- Platform
website: https://katonic.ai/
---
