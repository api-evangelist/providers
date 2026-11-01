---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Agentic AI banking platform API (no public machine‑readable contract discovered)
  name: Payman AI API
  slug: payman-ai-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: Compliance
  url: https://paymanai.com/security
- group: auth
  href: https://artifacts.apis.io/paymanai/security/paymanai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/paymanai-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/paymanai/conformance/paymanai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/paymanai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/paymanai/llms/paymanai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/paymanai-llms.txt
- group: other
  href: https://artifacts.apis.io/paymanai/hosts/paymanai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/paymanai-hosts.yml
- group: other
  href: https://artifacts.apis.io/paymanai/vendors/paymanai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/paymanai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/paymanai/security/paymanai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/paymanai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/paymanai/security/paymanai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/paymanai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/paymanai/security/paymanai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paymanai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://paymanai.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://paymanai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://paymanai.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://paymanai.com/agentic-banking
- group: company
  title: ''
  type: Blog
  url: https://paymanai.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paymanai.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paymanai.com/privacy-policy
created: '2026-10-21'
description: Payman AI, Inc provides agentic AI solutions for banks and credit unions, enabling autonomous handling of payments, transfers, account analysis, and customer interactions through voice or text interfaces. Their platform integrates with existing banking systems while maintaining strict security and compliance, offering a trusted AI-driven banking experience under the control of financial institutions.
image: https://paymanai.com/images/og-image.png
layout: provider
modified: '2026-10-21'
name: Payman AI, Inc
nav: Providers
network: true
overview: 'Payman AI, Inc is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Banking, FinTech, and Agentic.


  Payman AI, Inc''s developer surface includes documentation, getting-started guide, engineering blog, and 13 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 22.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Paymanai Domain Security
  slug: paymanai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Paymanai Vulnerability Disclosure
  slug: paymanai-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Paymanai Trust Center
  slug: paymanai-trust-center
  summary_line: SOC 2
slug: paymanai
tags:
- Company
- AI
- Banking
- FinTech
- Agentic
website: https://paymanai.com/
---
