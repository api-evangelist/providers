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
api_count: 1
apis:
- description: Programmatic TypeScript / JavaScript API for building VS Code extensions. The Extension API exposes editor UI, language features, debugging adapters, themes, webviews, source control providers, tasks,
  name: Visual Studio Code Extension API
  slug: extension-api
artifact_total: 2
common:
- group: build
  href: https://artifacts.apis.io/visual-studio-code/cli/visual-studio-code-cli.yml
  title: ''
  type: CLI
  url: cli/visual-studio-code-cli.yml
- group: operate
  href: https://artifacts.apis.io/visual-studio-code/changelog/visual-studio-code-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/visual-studio-code-changelog.yml
- group: agent
  href: https://artifacts.apis.io/visual-studio-code/llms/visual-studio-code-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/visual-studio-code-llms.txt
- group: other
  href: https://artifacts.apis.io/visual-studio-code/hosts/visual-studio-code-hosts.yml
  title: ''
  type: Hosts
  url: hosts/visual-studio-code-hosts.yml
- group: build
  href: https://artifacts.apis.io/visual-studio-code/integrations/visual-studio-code-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/visual-studio-code-integration-edges.yml
- group: build
  href: https://artifacts.apis.io/visual-studio-code/packages/visual-studio-code-packages.yml
  title: ''
  type: SDKs
  url: packages/visual-studio-code-packages.yml
- group: build
  href: https://artifacts.apis.io/visual-studio-code/packages/visual-studio-code-packages.yml
  title: ''
  type: Packages
  url: packages/visual-studio-code-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://github.com/github-copilot/signup
- group: start
  title: ''
  type: GettingStarted
  url: https://code.visualstudio.com/docs/agents/quickstart
- group: auth
  href: https://artifacts.apis.io/visual-studio-code/security/visual-studio-code-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/visual-studio-code-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/vs-code
- group: company
  title: ''
  type: Website
  url: https://code.visualstudio.com
- group: docs
  title: ''
  type: Documentation
  url: https://code.visualstudio.com/docs
- group: other
  title: ''
  type: Download
  url: https://code.visualstudio.com/download
- group: build
  title: ''
  type: GitHub
  url: https://github.com/microsoft/vscode
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.visualstudio.com/vscode
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/microsoft/vscode/issues
- group: company
  title: ''
  type: Blog
  url: https://code.visualstudio.com/blogs
- group: operate
  title: ''
  type: ChangeLog
  url: https://code.visualstudio.com/updates
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: docs
  title: ''
  type: APIReference
  url: https://code.visualstudio.com/api/references/vscode-api
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://code.visualstudio.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-05-11'
description: Visual Studio Code is a free, open-source, cross-platform code editor developed by Microsoft for Windows, Linux, macOS, and the web, built on the MIT-licensed Code - OSS project and distinguished by features such as IntelliSense, debugging, integrated Git, and a marketplace with tens of thousands of extensions. VS Code is not a SaaS REST API; instead, developers extend the editor through the Extension API, a TypeScript / JavaScript programmatic interface that exposes nearly every aspect of the editor for customization. This index points to the Extension API documentation and surrounding developer resources.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/visual-studio-code.png
layout: provider
modified: '2026-11-04'
name: Visual Studio Code
nav: Providers
network: true
overview: 'Visual Studio Code is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Code Editor, Developer Tools, IDE, Open Source, and Extension API.


  Visual Studio Code''s developer surface includes CLI, changelog, signup flow, getting-started guide, documentation, GitHub presence, engineering blog, and 14 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.6
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 64.3
    operational_transparency: 21.1
  previous_composite: 11.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/visual-studio-code/visual-studio-code-2026-06-20T201102.png
security:
- kind: domain-security
  name: Visual Studio Code Domain Security
  slug: visual-studio-code-domain-security
  summary_line: TLSv1.3 · HSTS
slug: visual-studio-code
tags:
- Code Editor
- Developer Tools
- IDE
- Open Source
- Extension API
- Microsoft
website: https://code.visualstudio.com
---
