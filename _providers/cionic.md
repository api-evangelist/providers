---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.4
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: The collections service of the CIONIC research platform. Path-versioned REST endpoints under /c/v{version}/{org}/ covering studies, protocols and protocol versions, collections and their files, stream
  name: CIONIC Research Platform API
  slug: research-platform-api
- description: The accounts service of the CIONIC research platform. Path-versioned REST endpoints under /a/v{version}/ covering account lookup and creation, the /accounts/@me self endpoint, downloadable access toke
  name: CIONIC Accounts API
  slug: accounts-api
artifact_total: 4
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cionicwear/cionic-data/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/cionicwear/cionic-data/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.cionic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cionic.com/platform
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/cionicwear/cionic-data/blob/main/README.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/cionicwear/cionic-data/blob/main/scripts/README.md
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cionicwear/cionic-data
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cionicwear
- group: operate
  title: ''
  type: Support
  url: https://support.cionic.com/
- group: company
  title: ''
  type: Blog
  url: https://go.cionic.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://go.cionic.com/rss.xml
- group: start
  title: ''
  type: SignUp
  url: https://cionic.com/a
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cionic.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cionic.com/legal/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.cionic.com/legal/data-disclosure
- group: build
  title: ''
  type: Packages
  url: packages/cionic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cionic-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cionic-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cionic-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cionic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cionic-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cionic-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cionic-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cionic-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cionic-llms.txt
created: '2026-08-09'
description: CIONIC Inc. is a neurotechnology company in Scotts Valley, California, founded in 2018 by Jeremiah Robison, that builds "bionic clothing" for people with neurological conditions that affect walking. Its flagship product, the FDA-cleared Cionic Neural Sleeve, combines inertial and surface-EMG sensing with functional electrical stimulation to analyze gait and assist dorsiflexion in conditions such as foot drop, multiple sclerosis, stroke and cerebral palsy. Alongside the consumer device CIONIC operates a research platform — the Cionic Research Kit — offering on-body hardware, iOS and Android collection apps, a web research portal for study and protocol management, a hosted JupyterLab analysis environment, and HIPAA-compliant participant data infrastructure. The company publishes an open-source Python client and command-line tooling for that platform's REST APIs, but the API reference and machine-readable contract itself sit behind a researcher account.
image: https://static.cionic.com/www/images/logo_green.svg
layout: provider
modified: '2026-08-09'
name: CIONIC
nav: Providers
network: true
overview: 'CIONIC publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Medical Devices, Wearables, and Neurotechnology.


  CIONIC''s developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, CLI, authentication, and 18 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 32.5
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 32.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Cionic Authentication
  slug: cionic-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Cionic Domain Security
  slug: cionic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cionic
tags:
- Company
- Health
- Medical Devices
- Wearables
- Neurotechnology
- Research
- Clinical Research
- Biomechanics
- Rehabilitation
- Digital Health
website: https://www.cionic.com/
---
