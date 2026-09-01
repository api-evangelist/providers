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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mind-foundry-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mindfoundry.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.mindfoundry.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.mindfoundry.ai/contactus
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MindFoundry
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mindfoundry.ai/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/mind-foundry-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mind-foundry-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/mind-foundry-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mind-foundry-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mind-foundry-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/mind-foundry-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mind-foundry-rate-limits.yml
coverage:
  checked: '2026-08-25'
  detail: Mind Foundry's site is a 139-URL HubSpot marketing site for two defence products (SENTRY, NIGHTINGALE) with no developer, docs or API path in its own sitemap; the one public API it ever shipped, OPTaaS, has been silently retired — mindfoundry.ai/optaas 404s, its optaas.mindfoundry.ai and demo.optimize.mindfoundry.ai hosts are NXDOMAIN, and the MindFoundry GitHub organisation now reports 0 public repositories.
  evidence:
  - status: 200
    url: https://www.mindfoundry.ai/sitemap.xml
  - status: 404
    url: https://mindfoundry.ai/optaas
  - status: 200
    url: https://api.github.com/orgs/MindFoundry
  - status: 404
    url: https://www.mindfoundry.ai/.well-known/api-catalog
  - status: 0
    url: https://optaas.mindfoundry.ai/
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: Mind Foundry is an Oxford University spin-out, founded in 2016 and headquartered at Ewert House in Oxford, United Kingdom, that builds applied machine learning for high-stakes, real-world problems across defence, national security, insurance, infrastructure and government. Its current products are SENTRY, a multi-modal sensor-fusion capability that detects, classifies and tracks objects in time and space from raw sensor data, and NIGHTINGALE, AI-enabled acoustic intelligence for anti-submarine warfare that has been integrated with Thales systems. Mind Foundry delivers these as deployed and integrated systems for customers and prime contractors rather than as a public, self-serve developer API, and it publishes no developer portal, API reference or machine-readable specification. The company previously operated OPTaaS (Optimization as a Service), a Bayesian optimisation API with first-party Python and R clients; the OPTaaS service hosts and its GitHub client repositories are
  no longer reachable, and the PyPI client has had no release since January 2024. Mind Foundry publishes ISO 27001, Cyber Essentials Plus and JOSCAR certifications on its own site.
image: https://www.mindfoundry.ai/hubfs/MF%20Logo%20L.png
layout: provider
modified: '2026-08-25'
name: Mind Foundry
nav: Providers
network: true
overview: 'Mind Foundry is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Defence, and National Security.


  Mind Foundry''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Mind Foundry Plans Pricing
  plan_count: 0
  slug: mind-foundry-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Mind Foundry Rate Limits
  slug: mind-foundry-rate-limits
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 12.6
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Mind Foundry Domain Security
  slug: mind-foundry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mind-foundry
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Defence
- National Security
- Sensor Fusion
- Responsible AI
- Optimization
- United Kingdom
website: https://www.mindfoundry.ai/
---
