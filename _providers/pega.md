---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 9.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Constellation Digital Experience (DX) API — REST endpoints external systems use to create Launchpad/Platform cases and data objects, read them, and advance them by running assignment actions. Auth
  name: Pega DX API
  slug: pega-dx-api
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/pega/security/pega-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/pega-trust-center.yml
- group: other
  href: https://artifacts.apis.io/pega/hosts/pega-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pega-hosts.yml
- group: other
  href: https://artifacts.apis.io/pega/vendors/pega-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pega-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://community.pega.com/knowledgebase/capabilities/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.pega.com/about/news
- group: other
  title: ''
  type: Leadership
  url: https://www.pega.com/about/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://community.pega.com/products/whats-new/platform
- group: company
  title: ''
  type: Website
  url: https://pega.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pega.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pega.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pega.com/bundle/platform/page/platform/dx-api/dx-api-overview.html
- group: start
  title: ''
  type: GettingStarted
  url: https://academy.pega.com
- group: operate
  title: ''
  type: Support
  url: https://community.pega.com
- group: company
  title: ''
  type: Blog
  url: https://www.pega.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://launchpad.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://launchpad.io/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pega.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pega.com/privacy
- group: commercial
  href: https://artifacts.apis.io/pega/plans/pega-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pega-plans-pricing.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pegasystems
- group: build
  href: https://artifacts.apis.io/pega/packages/pega-packages.yml
  title: ''
  type: Packages
  url: packages/pega-packages.yml
- group: build
  href: https://artifacts.apis.io/pega/packages/pega-packages.yml
  title: ''
  type: SDKs
  url: packages/pega-packages.yml
- group: design
  href: https://artifacts.apis.io/pega/components/pega-components.yml
  title: ''
  type: Components
  url: components/pega-components.yml
- group: agent
  href: https://artifacts.apis.io/pega/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/pega/authentication/pega-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pega-authentication.yml
- group: design
  href: https://artifacts.apis.io/pega/conventions/pega-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pega-conventions.yml
- group: design
  href: https://artifacts.apis.io/pega/errors/pega-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pega-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pega/conformance/pega-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pega-conformance.yml
- group: auth
  href: https://artifacts.apis.io/pega/security/pega-trust-center.yml
  title: ''
  type: Compliance
  url: security/pega-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.pega.com/
- group: auth
  href: https://artifacts.apis.io/pega/security/pega-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pega-domain-security.yml
- group: design
  href: https://artifacts.apis.io/pega/lifecycle/pega-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pega-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.pega.com/bundle/platform/page/platform/release-notes/deprecated-and-removed-features.html
- group: agent
  href: https://artifacts.apis.io/pega/well-known/pega-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pega-well-known.yml
- group: agent
  href: https://artifacts.apis.io/pega/llms/pega-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pega-llms.txt
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://pega.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-07-17'
description: Pega (Pegasystems) is an enterprise low-code platform for AI-powered decisioning and workflow automation, spanning business process management (BPM), CRM, and customer engagement across financial services, insurance, healthcare, government, and manufacturing. External systems integrate with Pega Platform and Pega Launchpad through the Constellation Digital Experience (DX) API — a REST + OAuth 2.0 surface for creating and driving cases and data objects — and through first-party SDKs (React, Angular, Web Components, Mobile) that render Constellation DX Components. Pega also publishes first-party Agent Skills for building on Launchpad.
finops:
- has_sources: true
  method: derived
  name: Pega Finops
  primary_unit: launchpad units
  service_category: ''
  slug: pega-finops
  template: false
image: https://github.com/pegasystems.png
layout: provider
modified: '2026-07-20'
name: Pega
nav: Providers
network: true
overview: 'Pega is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Low-Code, Business Process Management, Workflow Automation, and CRM.


  Pega''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 28 more developer resources.'
plans:
- name: Pega Plans Pricing
  plan_count: 5
  slug: pega-plans-pricing
- name: Pega Price Estimates
  plan_count: 0
  slug: pega-price-estimates
random_paper: 5
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.0
    operational_transparency: 23.7
  previous_composite: 48.5
  provenance:
    conformance: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: fedramp
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pega/pega-2026-10-11T192133.png
security:
- kind: authentication
  name: Pega Authentication
  slug: pega-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Pega Domain Security
  slug: pega-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pega Trust Center
  slug: pega-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
skill_count: 1
skills:
- name: Drive a Launchpad case with the Pega DX API
  slug: pega-launchpad-dx-apis
slug: pega
tags:
- Company
- Low-Code
- Business Process Management
- Workflow Automation
- CRM
- Decisioning
- Artificial Intelligence
- Enterprise
- Case Management
website: https://pega.com
---
