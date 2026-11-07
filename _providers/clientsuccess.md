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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.clientsuccess.com/security-compliance
- group: design
  href: https://artifacts.apis.io/clientsuccess/conformance/clientsuccess-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clientsuccess-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clientsuccess/llms/clientsuccess-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clientsuccess-llms.txt
- group: auth
  href: https://artifacts.apis.io/clientsuccess/well-known/clientsuccess-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clientsuccess-help-security.txt
- group: agent
  href: https://artifacts.apis.io/clientsuccess/well-known/clientsuccess-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clientsuccess-well-known.yml
- group: other
  href: https://artifacts.apis.io/clientsuccess/hosts/clientsuccess-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clientsuccess-hosts.yml
- group: other
  href: https://artifacts.apis.io/clientsuccess/vendors/clientsuccess-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clientsuccess-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.clientsuccess.com/resources/sign-up-to-win-a-duffel-bag
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ClientSuccess
- group: auth
  href: https://artifacts.apis.io/clientsuccess/security/clientsuccess-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/clientsuccess-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/clientsuccess/security/clientsuccess-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clientsuccess-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clientsuccess.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.clientsuccess.com/platform/insights-and-analytics
- group: docs
  title: ''
  type: APIReference
  url: https://www.clientsuccess.com/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://www.clientsuccess.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.clientsuccess.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.clientsuccess.com/categories/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clientsuccess.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clientsuccess.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clientsuccess.com/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/clientsuccess/workspace
coverage:
  checked: '2026-10-09'
  detail: Provider docs at https://www.clientsuccess.com/mcp return HTML with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://www.clientsuccess.com/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: ClientSuccess provides a comprehensive customer success platform that helps businesses reduce churn, increase revenue, and deliver world‑class customer experiences. The SaaS solution combines AI‑driven insights, automation, and a unified portal for onboarding, journey management, and analytics, enabling teams to act on real‑time health scores, NPS, and product feedback. It integrates with major CRMs and support tools, offering a scalable, data‑driven approach to customer lifecycle management.
image: https://www.clientsuccess.com/images/cs-og-image.jpg
layout: provider
modified: '2026-10-08'
name: ClientSuccess
nav: Providers
network: true
overview: 'ClientSuccess is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Success, Software-as-a-Service, Artificial Intelligence, Analytics, and Integration.


  ClientSuccess'' developer surface includes signup flow, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 14 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.6
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 55.4
    operational_transparency: 13.2
  previous_composite: 31.0
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
    score: 15.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/clientsuccess/clientsuccess-2026-11-03T124425.png
security:
- kind: domain-security
  name: Clientsuccess Domain Security
  slug: clientsuccess-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Clientsuccess Trust Center
  slug: clientsuccess-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: clientsuccess
tags:
- Customer Success
- Software-as-a-Service
- Artificial Intelligence
- Analytics
- Integration
website: https://www.clientsuccess.com/
---
