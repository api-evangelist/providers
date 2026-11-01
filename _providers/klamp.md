---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/klamp/plans/klamp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/klamp-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/klamp/changelog/klamp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/klamp-changelog.yml
- group: design
  href: https://artifacts.apis.io/klamp/conventions/klamp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/klamp-conventions.yml
- group: auth
  href: https://artifacts.apis.io/klamp/authentication/klamp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/klamp-authentication.yml
- group: design
  href: https://artifacts.apis.io/klamp/conformance/klamp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/klamp-conformance.yml
- group: agent
  href: https://artifacts.apis.io/klamp/llms/klamp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/klamp-llms.txt
- group: other
  href: https://artifacts.apis.io/klamp/hosts/klamp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/klamp-hosts.yml
- group: other
  href: https://artifacts.apis.io/klamp/vendors/klamp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/klamp-vendors.yml
- group: auth
  href: https://artifacts.apis.io/klamp/security/klamp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/klamp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://klamp.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.klamp.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://klamp.ai/knowledge-base
- group: docs
  title: ''
  type: APIReference
  url: https://klamp.ai/knowledge-base
- group: start
  title: ''
  type: GettingStarted
  url: https://klamp.ai/embedded-ipaas
- group: operate
  title: ''
  type: Support
  url: https://klamp.ai/community-forum
- group: company
  title: ''
  type: Blog
  url: https://klamp.ai/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://klamp.ai/release-notes
- group: commercial
  title: ''
  type: Pricing
  url: https://klamp.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://klamp.ai/request-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://klamp.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://klamp.ai/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/klamp/workspace
coverage:
  checked: '2026-10-18'
  detail: The provider's documentation pages contain no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://klamp.ai/knowledge-base
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-17'
description: Klamp.ai provides an embedded iPaaS platform that enables seamless data migration and integration for SaaS products. It offers native connectors to hundreds of applications, allowing product teams to embed integration and migration capabilities directly into their offerings without extensive engineering effort. The solution supports AI‑mapped migrations, zero‑downtime data transfer, and a suite of tools for product managers, marketers, sales, and customer success teams to streamline workflows and enhance customer experiences.
image: https://storage.googleapis.com/klamp-cms-storage-bucket/og_image_5f21ef1888/og_image_5f21ef1888.png
layout: provider
modified: '2026-10-17'
name: Klamp.ai
nav: Providers
network: true
overview: 'Klamp.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, iPaaS, Data Migration, Software-as-a-Service, and Embedded Solutions.


  Klamp.ai''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 15 more developer resources.'
plans:
- name: Klamp Plans Pricing
  plan_count: 2
  slug: klamp-plans-pricing
random_paper: 5
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 48.2
    operational_transparency: 21.1
  previous_composite: 36.7
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
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Klamp Authentication
  slug: klamp-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Klamp Domain Security
  slug: klamp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: klamp
tags:
- Integration
- iPaaS
- Data Migration
- Software-as-a-Service
- Embedded Solutions
website: https://klamp.ai/
---
