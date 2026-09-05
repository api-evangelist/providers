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
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: The developer surface of the Virtualitics AI Platform. Developers author AI Apps in Python with the Virtualitics SDK (App, Step, Page, Section, Card, Elements, Assets, LLM/Iris, Store, Audit, Triggers
  name: Virtualitics AI Platform (VAIP) Developer Experience
  slug: virtualitics-ai-platform
- description: pyVIP is the Virtualitics Python API for Virtualitics Explore. It runs over a WebSocket connection between Virtualitics Explore (server) and a Python session (client), launched from the API section of
  name: Virtualitics Explore Python API (pyVIP)
  slug: virtualitics-explore-python-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/virtualitics-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/virtualitics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/virtualitics-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://virtualitics.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.virtualitics.com/hc/en-us/categories/34003471469587-Virtualitics-Developer-Experience
- group: docs
  title: ''
  type: Documentation
  url: https://docs.virtualitics.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://sdk.virtualitics.com/latest/api-reference/app/
- group: start
  title: ''
  type: GettingStarted
  url: https://sdk.virtualitics.com/latest/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://virtualitics.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://virtualitics.com/virtualitics-blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/virtualitics
- group: start
  title: ''
  type: SignUp
  url: https://accounts.virtualitics.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://virtualitics.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://virtualitics.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/virtualitics-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/virtualitics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/virtualitics-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/virtualitics-cli.yml
- group: design
  title: ''
  type: Components
  url: components/virtualitics-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/virtualitics-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/virtualitics-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/virtualitics-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/virtualitics-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/virtualitics-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virtualitics-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/virtualitics-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/virtualitics-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/virtualitics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/virtualitics-rate-limits.yml
created: '2026-09-04'
description: Virtualitics, Inc. is a Pasadena, California AI software company founded in 2016 on more than a decade of research at Caltech and NASA's Jet Propulsion Laboratory. It builds the Virtualitics AI Platform (VAIP), a secure deployment target for mission-critical AI Apps; Virtualitics Explore, a 3D/immersive data exploration client; Virtualitics Predict; the Integrated Readiness Optimization (IRO) application suite; and Iris, a natural-language AI agent over platform data. Its developer surface is Python-first rather than HTTP-first — the Virtualitics SDK (virtualitics-sdk) for authoring multi-step Apps, the Virtualitics CLI (virtualitics-cli, the `vaip` command) for packaging and deploying them into a customer tenant, and pyVIP, a Python API that drives Virtualitics Explore over a WebSocket connection. Deployments run on customer-controlled hosts including NIPR, SIPR, JWICS, ADVANA and ODIN across the U.S. military services.
image: https://virtualitics.com/wp-content/uploads/2026/06/Virtualitics_Logo_Black.png
layout: provider
modified: '2026-09-04'
name: Virtualitics
nav: Providers
network: true
overview: 'Virtualitics publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Data Analytics, Data Visualization, and Machine Learning.


  Virtualitics'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, CLI, and 22 more developer resources.'
plans:
- name: Virtualitics Plans Pricing
  plan_count: 0
  slug: virtualitics-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Virtualitics Rate Limits
  slug: virtualitics-rate-limits
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 71.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 66.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Virtualitics Authentication
  slug: virtualitics-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Virtualitics Domain Security
  slug: virtualitics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Virtualitics Vulnerability Disclosure
  slug: virtualitics-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Virtualitics Trust Center
  slug: virtualitics-trust-center
  summary_line: NIST SP 800-171, CMMC, SOC 2 Type 2, SOC 2 Type 3, CIS Top 20, FIPS 140-2
slug: virtualitics
tags:
- Company
- Artificial Intelligence
- Data Analytics
- Data Visualization
- Machine Learning
- Defense
- Government
- Python
- SDK
- Command Line Interface
website: https://virtualitics.com/
---
