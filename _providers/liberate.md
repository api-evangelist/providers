---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  - '{''url'': ''https://www.liberateinc.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.liberate.ai/ — a different registrable domain (liberateinc.com -> liberate.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: HTTP interface for triggering Liberate workflows. A workflow is started with a PUT request carrying a bearer token, a flow slug, and a JSON context object. Every customer receives their own unique end
  name: Liberate Orchestration Platform API
  slug: orchestration
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liberate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.liberateinc.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.liberateinc.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.liberateinc.com/docs/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.liberateinc.com/docs/calling-a-workflow
- group: operate
  title: ''
  type: Support
  url: http://signup.liberateinc.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.liberateinc.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.liberateinc.com/request-demo
- group: start
  title: ''
  type: Login
  url: https://app.liberateinc.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.liberateinc.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.liberateinc.com/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.vanta.com/liberateinc.com/trust/a3f4px3jh3gd2prixhl6
- group: auth
  title: ''
  type: Compliance
  url: https://www.liberateinc.com/security
- group: other
  title: ''
  type: Glossary
  url: https://www.liberateinc.com/glossary
- group: other
  title: ''
  type: CaseStudies
  url: https://www.liberateinc.com/case-studies
- group: company
  title: ''
  type: News
  url: https://www.liberateinc.com/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/liberate-inc/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/liberate-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/liberate-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/liberate-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/liberate-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/liberate-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/liberate-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/liberate-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liberate-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/liberate-trust-center.yml
created: '2026-07-17'
description: Liberate is an insurance-native AI company building generative voice, email, and SMS agents that resolve customer inquiries end-to-end for carriers, agencies, and brokers. Its "system of action" handles sales, servicing, and claims — verifying identity, gathering loss details, filing FNOL, and driving the downstream workflow — while integrating with core insurance systems such as Guidewire, Duck Creek, Vertafore, Applied, EZ Lynx, Salesforce, Insuresoft, TurboRater, Verisk, and CoreLogic. Underneath the AI agents sits the Liberate Orchestration Platform, a low-code workflow engine where developers compose modular workflows from connections, events, tasks, decision tables, and JSONata transformations, then version, release, and deploy them across QA and production environments. Workflows are triggered over HTTP with a bearer token against a per-customer integration endpoint. Liberate is backed by Redpoint Ventures and states SOC 2, HIPAA, PCI DSS, GDPR, and CCPA compliance.
image: https://cdn.prod.website-files.com/69d93976ca90059d5696cd0b/69d93976ca90059d5696cef7_Webclip.png
layout: provider
modified: '2026-07-19'
name: Liberate
nav: Providers
network: true
overview: 'Liberate publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Insurance, Insurtech, and Voice AI.


  Liberate''s developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, product news, changelog, and 19 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 33.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liberate/refs/heads/main/screenshots/liberate-2026-07-25T225016.png
security:
- kind: authentication
  name: Liberate Authentication
  slug: liberate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Liberate Domain Security
  slug: liberate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Liberate Trust Center
  slug: liberate-trust-center
  summary_line: SOC 2, HIPAA, PCI DSS, GDPR, CCPA
slug: liberate
tags:
- Company
- Artificial Intelligence
- Insurance
- Insurtech
- Voice AI
- AI Agents
- Workflow Orchestration
- Claims Automation
- Low-Code
- Contact Center
website: https://www.liberateinc.com/
---
