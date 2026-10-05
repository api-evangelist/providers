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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.terret.ai/security
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boostupai/refs/heads/main/hosts/boostupai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boostupai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boostupai/refs/heads/main/vendors/boostupai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boostupai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://terret.ai/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://terret.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://terret.ai/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.terret.ai/resources/tag/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boostupai/refs/heads/main/security/boostupai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/boostupai-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boostupai/refs/heads/main/security/boostupai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/boostupai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boostupai/refs/heads/main/security/boostupai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boostupai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.terret.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.terret.ai/resources
- group: company
  title: ''
  type: Blog
  url: https://www.terret.ai/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.terret.ai/demo
- group: start
  title: ''
  type: SignUp
  url: https://app.boostup.ai/login
coverage:
  checked: '2026-10-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's hosts; only HTML documentation pages were available.
  evidence:
  - status: 200
    url: https://app.boostup.ai/openapi.json
  - status: 200
    url: https://app.boostup.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: BoostUp.ai provides an AI‑driven revenue acceleration platform that combines pipeline forecasting, conversation intelligence, and automated deal‑closing tools. The solution helps sales teams uncover hidden opportunities, prioritize high‑value prospects, and automate follow‑ups, driving higher win rates and faster revenue growth. Powered by advanced machine learning, BoostUp.ai integrates with CRM systems to deliver real‑time insights and actionable recommendations across the sales funnel.
image: https://terret.ai/images/nexus-og-logo-only.jpg
layout: provider
modified: '2026-10-02'
name: BoostUp.ai
nav: Providers
network: true
overview: 'BoostUp.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Revenue, Sales, and Automation.


  BoostUp.ai''s developer surface includes documentation, engineering blog, pricing, signup flow, and 11 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boostupai Domain Security
  slug: boostupai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Boostupai Vulnerability Disclosure
  slug: boostupai-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Boostupai Trust Center
  slug: boostupai-trust-center
  summary_line: SOC 2, CSA STAR, FIPS 140
slug: boostupai
tags:
- Company
- Artificial Intelligence
- Revenue
- Sales
- Automation
website: https://www.terret.ai/
---
